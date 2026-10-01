#!/usr/bin/env python3
"""Sync grid.rec to Canvas weekly modules.

grid.rec is the single source of truth for the semester schedule. This script
reads it and builds, in the Information and Interaction Design Canvas course,
one module per week plus a "Start here" module. Each week module holds an
overview page, the slide deck link, media, in-class exercises, reading files,
and the homework assigned or due that week.

Re-running is safe: modules are matched by their "Week NN (date)" prefix and
their items rebuilt; pages are matched by title and updated in place.

Grid fields used: Week, Topics, Exercises, Reading (@citekeys mapped in
READINGS, or a Canvas file name with a title in parentheses), Assigned, Due,
Media and Slides (Canvas file names or URLs with a title in parentheses).

Usage:
    python3 rec2canvas.py --dry-run      # print the plan, touch nothing
    python3 rec2canvas.py                # build/update the modules
    python3 rec2canvas.py --print-html   # dump the generated HTML and exit

Credentials come from ~/courses/canvas-mcp/.env (CANVAS_API_TOKEN, CANVAS_API_URL).
Only the Python standard library is used.
"""

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REC_PATH = os.path.join(HERE, "grid.rec")
ENV_PATH = os.path.expanduser("~/courses/canvas-mcp/.env")

COURSE_ID = 1456671  # Fa26 INFORMATION/INTERACTION DESIGN (30525), I 320U
COURSE_GUARD = "INFORMATION/INTERACTION DESIGN"
YEAR = 2026
CLASS_DAYS = ("mon", "wed")
SYLLABUS_FILE = "syllabus.html"
HW_PAGES = ("Rules for all milestones", "Rules for all exercises", "Optional exercises")  # from hw/hwInstructions/hw2canvas.py

# ---------------------------------------------------------------- mappings

# Citation key -> (display citation, file name in Canvas Files). File ids are
# looked up at run time, so re-uploading a file under the same name needs no
# change here; a new name (e.g. a different chapter) does.
READINGS = {
    "Rogers2023": ("Rogers, Sharp & Preece, <i>Interaction Design: Beyond Human-Computer Interaction</i>, 6th ed. (2023)", "Rogers2023ch1-3.pdf"),
    "Holtzblatt2005": ("Holtzblatt, Wendell & Wood, <i>Rapid Contextual Design</i> (2005)", "Holtzblatt2005ch3-5.pdf"),
    "Cooper2014": ("Cooper, Reimann, Cronin & Noessel, <i>About Face 4.0</i> (2014)", "Cooper2014ch1-3.pdf"),
    "Dodson2006": ("Dodson, <i>Keys to Drawing with Imagination</i> (2006)", "Dodson2006ch1-3.pdf"),
    "Tidwell2020": ("Tidwell, Brewer & Valencia, <i>Designing Interfaces</i>, 3rd ed. (2020)", "Tidwell2020.pdf"),
    "Rosenfeld2015": ("Rosenfeld, Morville & Arango, <i>Information Architecture: For the Web and Beyond</i>, 4th ed. (2015)", "Rosenfeld2015ch1-3.pdf"),
    "Wilkinson2005": ("Wilkinson, <i>The Grammar of Graphics</i> (2005)", "Wilkinson2005.pdf"),
    "Bertin2011": ("Bertin, <i>Semiology of Graphics</i> (2011)", "bertin.pdf"),
    "Kolko2025": ("Kolko, “What Should a Junior User Experience Designer Have in Their Portfolio?”, <i>Interactions</i> (2025)", "Kolko2025.pdf"),
}

# Canvas file name -> file id, filled by resolve_files() at run time.
FILE_IDS = {}


def file_id(name):
    return FILE_IDS.get(name)

# Regex over the lowercased Assigned/Due item text -> Canvas assignment id.
ASSIGNMENTS = [
    (r"^e1\b", 7763395), (r"^e2\b", 7763396), (r"^e3\b", 7763397), (r"^e4\b", 7763398),
    (r"^e5\b", 7763399), (r"^e6\b", 7763400), (r"^e7\b", 7763401), (r"^e8\b", 7763402),
    (r"^m1\b", 7763407), (r"^m2 contextual", 7763408), (r"^m2 peer", 7763409),
    (r"^m3\b", 7763410), (r"^m4\b", 7763411), (r"^m5\b", 7763412),
    (r"^final peer", 7763405), (r"^final exam", 7763404),
]

# Regex over the lowercased Exercises item text -> Canvas (ungraded) assignment id.
EXERCISES = [
    (r"^design thinking", 7763394), (r"^triangles", 7763413), (r"^open ?/ ?close", 7798047),
    (r"^crazy eights", 7763393), (r"^ai personas", 7812043), (r"^in-class storyboards", 7763406),
    (r"^extreme emphasis", 7763403), (r"^bertin", 7763392), (r"^robert johnson", 7763389),
]

DAY_NAMES = {"mon": "Mon", "tue": "Tue", "wed": "Wed", "thu": "Thu", "fri": "Fri", "sat": "Sat", "sun": "Sun"}
DAY_OFFSET = {d: i for i, d in enumerate(("mon", "tue", "wed", "thu", "fri", "sat", "sun"))}
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

# ---------------------------------------------------------------- rec parsing


def parse_rec(path):
    """Return a list of records; each record is a dict field -> joined value."""
    records, cur, field, buf, cont = [], {}, None, [], False
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    lines.append("")

    def flush_field():
        nonlocal field, buf
        if field is not None:
            cur[field] = " ".join(s.strip() for s in buf).strip()
        field, buf = None, []

    for line in lines:
        if cont:
            cont = line.endswith("\\")
            buf.append(line[:-1] if cont else line)
            continue
        if line.startswith("%") or line.startswith("#") or line.startswith("+"):
            continue
        if not line.strip():
            flush_field()
            if cur:
                records.append(cur)
                cur = {}
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*):\s?(.*)$", line)
        if not m:
            buf.append(line)
            continue
        flush_field()
        field, val = m.group(1), m.group(2)
        cont = val.endswith("\\")
        buf = [val[:-1] if cont else val]
    flush_field()
    if cur:
        records.append(cur)
    return records


DAYS_RE = "|".join(DAY_NAMES)
DAY_TAG = re.compile(rf"^\(((?:{DAYS_RE})(?:\s*,\s*(?:{DAYS_RE}))*)\)\s*", re.I)


def parse_entries(value):
    """Split a field value into entries: dict(days, text).

    Entries are separated by ';'. A leading '(mon)' or '(mon, wed)' sets the
    day(s); an entry without a day tag inherits the previous entry's days.
    """
    entries, days = [], None
    for chunk in value.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = DAY_TAG.match(chunk)
        if m:
            days = [d.strip().lower() for d in m.group(1).split(",")]
            chunk = chunk[m.end():]
        chunk = chunk.strip().rstrip(",").strip()
        if chunk:
            entries.append({"days": days, "text": chunk})
    return entries


def parse_readings(value):
    """'@Rogers2023 (ch 1-3), @Bertin2011; Tufte2003.pdf (Tufte)' -> [(key_or_file, detail)]."""
    out = []
    for part in re.split(r"[;,]\s*(?=@|\S+\.\w+\s*\()", value):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"@(\w+)\s*,?\s*(.*)$", part)
        if m:
            key, detail = m.group(1), m.group(2).strip()
        else:
            m = re.match(r"^(\S+\.\w+)\s*(?:\((.*)\))?\s*$", part)
            if not m:
                continue
            key, detail = m.group(1), (m.group(2) or "").strip()
        detail = detail[1:-1].strip() if re.fullmatch(r"\(.*\)", detail) else detail
        out.append((key, detail))
    return out


def parse_media(value):
    """'usabilityTest.mp4 (Demo video); https://youtu.be/x (Talk)' -> [(target, title, is_url)]."""
    out = []
    for chunk in value.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.match(r"^(\S+)\s*(?:\((.*)\))?\s*$", chunk)
        if not m:
            continue
        target, title = m.group(1), (m.group(2) or m.group(1)).strip()
        out.append((target, title, bool(re.match(r"https?://", target))))
    return out


def parse_week_header(value):
    """'03 (07 Sep) (Labor Day)' -> (3, date(2026,9,7), 'Labor Day'); 'Fall Break' -> (None, None, 'Fall Break')."""
    m = re.match(r"^(\d+)\s*\((\d+)\s+(\w{3})\)\s*(?:\((.*)\))?", value)
    if not m:
        return None, None, value.strip()
    n, day, mon, note = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    return n, dt.date(YEAR, MONTHS[mon], day), note


def build_weeks(records):
    weeks, prev_monday = [], None
    for r in records:
        n, monday, note = parse_week_header(r["Week"])
        if monday is None and prev_monday is not None:
            monday = prev_monday + dt.timedelta(days=7)
        weeks.append({
            "n": n, "monday": monday, "note": note or "",
            "topics": parse_entries(r.get("Topics", "")),
            "exercises": parse_entries(r.get("Exercises", "")),
            "reading": parse_readings(r.get("Reading", "")),
            "media": parse_media(r.get("Media", "")),
            "slides": [s for s in parse_media(r.get("Slides", "")) if s[2]],
            "assigned": parse_entries(r.get("Assigned", "")),
            "due": parse_entries(r.get("Due", "")),
        })
        prev_monday = monday
    return weeks

# ---------------------------------------------------------------- rendering


def esc(s):
    return html.escape(s, quote=False)


def fmt_date(d):
    return f"{d.day} {d.strftime('%b')}"


def day_date(w, day):
    return w["monday"] + dt.timedelta(days=DAY_OFFSET[day])


def week_label(w):
    if w["n"] is None:
        return f"{w['note']} ({fmt_date(w['monday'])})"
    return f"Week {w['n']:02d} ({fmt_date(w['monday'])})"


def week_topics(w):
    """Short topic list for the module name."""
    seen, out = set(), []
    for e in w["topics"]:
        first = re.split(r"[;:]", e["text"])[0].strip()
        if first.lower().startswith("guest speaker"):
            first = "Guest speaker"
        if first.lower() in ("syllabus", "last class day") or first.lower().startswith("final exam") or not first:
            continue
        if first.lower() not in seen:
            seen.add(first.lower())
            out.append(first)
    return out


def module_name(w):
    if w["n"] is None:
        return week_label(w)
    topics = week_topics(w)
    return f"{week_label(w)}: {' · '.join(topics)}" if topics else week_label(w)


def find_id(table, text):
    low = text.lower()
    for pat, aid in table:
        if re.search(pat, low):
            return aid
    return None


def assignment_url(aid):
    return f"/courses/{COURSE_ID}/assignments/{aid}"


def file_url(fid):
    return f"/courses/{COURSE_ID}/files/{fid}"


def on_day(entries, day):
    return [e["text"] for e in entries if e["days"] and day in e["days"]]


def notes(w):
    out = [w["note"]] if w["note"] else []
    for e in w["topics"] + w["exercises"]:
        if not e["days"] and e["text"] and e["text"] not in out:
            out.append(e["text"])
    return out


def reading_line(key, detail, warnings, week_n):
    """HTML for one reading; (cite, fname) from READINGS or a bare file name."""
    if key in READINGS:
        cite, fname = READINGS[key]
    elif "." in key:
        cite, fname = esc(detail or key), key
        detail = ""
    else:
        warnings.append(f"week {week_n}: reading {key} not in READINGS")
        cite, fname = esc(key), None
    fid = file_id(fname) if fname else None
    if fname and not fid:
        warnings.append(f"week {week_n}: no PDF for reading {key} ({fname})")
    det = f", {esc(detail)}" if detail else ""
    link = f' — <a href="{file_url(fid)}">PDF</a>' if fid else ""
    return f"{cite}{det}{link}", fname, fid


def render_item(e, table, verb, warnings, week_n):
    """One <li> for an assigned/due/exercise entry."""
    days = ", ".join(DAY_NAMES[d] for d in (e["days"] or [])) or "this week"
    aid = find_id(table, e["text"])
    if aid is None:
        warnings.append(f"week {week_n}: no Canvas assignment matched '{e['text']}' ({verb})")
        return f"<li><b>{days}:</b> {esc(e['text'])}</li>"
    return f"<li><b>{days}:</b> <a href=\"{assignment_url(aid)}\">{esc(e['text'])}</a></li>"


def render_overview(w, warnings):
    lbl = week_label(w)
    if w["n"] is None:
        return f"<h2>{esc(lbl)}</h2><p>No class this week.</p>"
    parts = [f"<h2>{esc(lbl)}</h2>"]
    for n in notes(w):
        parts.append(f"<p><i>{esc(n)}</i></p>")
    th = 'style="border:1px solid #999;padding:6px;text-align:left"'
    td = 'style="border:1px solid #999;padding:6px"'
    parts.append('<table style="border-collapse:collapse;width:100%"><thead><tr style="background:#f3f3f3">'
                 f"<th {th}></th><th {th}>In class</th><th {th}>Exercise</th></tr></thead><tbody>")
    for day in CLASS_DAYS:
        topics, exs = on_day(w["topics"], day), on_day(w["exercises"], day)
        if not topics and not exs:
            continue
        dlabel = f"{DAY_NAMES[day]} {fmt_date(day_date(w, day))}"
        ex_cells = []
        for t in exs:
            aid = find_id(EXERCISES, t)
            ex_cells.append(f'<a href="{assignment_url(aid)}">{esc(t)}</a>' if aid else esc(t))
        parts.append(f'<tr><th {th} style="white-space:nowrap">{esc(dlabel)}</th>'
                     f"<td {td}>{esc('; '.join(topics))}</td><td {td}>{'; '.join(ex_cells)}</td></tr>")
    parts.append("</tbody></table>")

    if w["slides"]:
        parts.append("<h3>Slides</h3><ul>")
        for url, title, _ in w["slides"]:
            parts.append(f'<li><a href="{esc(url)}">{esc(title)}</a></li>')
        parts.append("</ul>")

    if w["reading"]:
        parts.append("<h3>Read before class</h3><ul>")
        for key, detail in w["reading"]:
            line, _, _ = reading_line(key, detail, warnings, w["n"])
            parts.append(f"<li>{line}</li>")
        parts.append("</ul>")

    if w["media"]:
        parts.append("<h3>Media</h3><ul>")
        for target, title, is_url in w["media"]:
            if is_url:
                parts.append(f'<li><a href="{esc(target)}">{esc(title)}</a></li>')
            elif file_id(target):
                parts.append(f'<li><a href="{file_url(file_id(target))}">{esc(title)}</a> ({esc(target)})</li>')
            else:
                warnings.append(f"week {w['n']}: media file '{target}' not found in Canvas Files")
                parts.append(f"<li>{esc(title)} ({esc(target)})</li>")
        parts.append("</ul>")

    for verb, entries in (("Assigned", w["assigned"]), ("Due", w["due"])):
        if entries:
            parts.append(f"<h3>{verb} this week</h3><ul>")
            for e in entries:
                parts.append(render_item(e, ASSIGNMENTS, verb.lower(), warnings, w["n"]))
            parts.append("</ul>")

    parts.append('<p style="color:#666;font-size:90%">Homework is due at 11:59 PM on the day shown. '
                 'Full instructions for each assignment are in its Description on the Assignments page; '
                 'the rules that apply to all of them are on the Rules pages in the Start here module.</p>')
    return "\n".join(parts)


def render_full_schedule(weeks, warnings):
    """One page with the whole semester as a table."""
    td = 'style="border:1px solid #999;padding:6px;vertical-align:top"'
    th = 'style="border:1px solid #999;padding:6px;text-align:left;background:#f3f3f3"'
    out = ["<p>The whole semester on one page. Each week also has its own module with links to slides, "
           "readings, in-class exercises, and assignments.</p>",
           '<div style="overflow-x:auto"><table style="border-collapse:collapse;width:100%">',
           f"<thead><tr><th {th}>Week</th><th {th}>In class</th><th {th}>Reading</th>"
           f"<th {th}>Assigned</th><th {th}>Due</th></tr></thead><tbody>"]

    def col(entries, table=None):
        lines = []
        for e in entries:
            days = ", ".join(DAY_NAMES[d] for d in (e["days"] or []))
            aid = find_id(table, e["text"]) if table else None
            txt = f'<a href="{assignment_url(aid)}">{esc(e["text"])}</a>' if aid else esc(e["text"])
            lines.append((f"<b>{days}:</b> " if days else "") + txt)
        return "<br>".join(lines)

    for w in weeks:
        if w["n"] is None:
            out.append(f"<tr><td {td}><b>{esc(week_label(w))}</b></td><td colspan=\"4\" {td}>No class</td></tr>")
            continue
        inclass = col(w["topics"])
        if w["exercises"]:
            inclass += "<br><i>Exercises:</i> " + col(w["exercises"], EXERCISES)
        rd = "<br>".join(reading_line(k, d, warnings, w["n"])[0] for k, d in w["reading"])
        for target, title, is_url in w["media"]:
            href = target if is_url else (file_url(file_id(target)) if file_id(target) else None)
            rd += ("<br>" if rd else "") + (f'Media: <a href="{esc(href)}">{esc(title)}</a>' if href else f"Media: {esc(title)}")
        note = f"<br><i>{esc(w['note'])}</i>" if w["note"] else ""
        out.append(f"<tr><td {td}><b>{esc(week_label(w))}</b>{note}</td><td {td}>{inclass}</td>"
                   f"<td {td}>{rd}</td><td {td}>{col(w['assigned'], ASSIGNMENTS)}</td>"
                   f"<td {td}>{col(w['due'], ASSIGNMENTS)}</td></tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def start_here_body(existing_pages):
    items = [f'<li><a href="{file_url(file_id(SYLLABUS_FILE))}">Syllabus</a> '
             "(also under the Syllabus tab in the course menu)</li>",
             "<li>Semester schedule: the whole semester on one page (linked below)</li>"]
    for title in HW_PAGES:
        if title in existing_pages:
            items.append(f'<li><a href="/courses/{COURSE_ID}/pages/{existing_pages[title]["url"]}">{esc(title)}</a></li>')
    return ("<p>Class meets Monday and Wednesday. Bring your sketchbook and a phone or tablet with a camera "
            "every day.</p><ul>" + "".join(items) + "</ul>"
            "<p>Each week has a module containing an overview page, the slides, any media, the in-class "
            "exercises, the readings as PDFs, and the homework that is assigned or due that week. "
            "Homework comes in two kinds: <b>exercises</b> (individual, e1 to e8, each with two sketches of good "
            "design) and <b>milestones</b> (team project, m1 to m5).</p>")


def plan_items(w, warnings):
    """Return the ordered list of module items for a week as dicts."""
    items = []
    if w["n"] is None:
        items.append({"type": "SubHeader", "title": "No class this week"})
        return items
    items.append({"type": "Page", "title": f"{week_label(w)} overview", "page_title": f"{week_label(w)} overview"})
    for url, title, _ in w["slides"]:
        items.append({"type": "ExternalUrl", "title": f"Slides: {title}", "url": url, "new_tab": True})
    for target, title, is_url in w["media"]:
        if is_url:
            items.append({"type": "ExternalUrl", "title": f"Watch: {title}", "url": target, "new_tab": True})
        elif file_id(target):
            items.append({"type": "File", "content_id": file_id(target), "title": f"Watch: {title}"})
        else:
            items.append({"type": "SubHeader", "title": f"Watch: {title} ({target} not found)"})
    if w["exercises"]:
        items.append({"type": "SubHeader", "title": "In class"})
        for e in w["exercises"]:
            days = "/".join(DAY_NAMES[d] for d in (e["days"] or []))
            aid = find_id(EXERCISES, e["text"])
            t = f"{days}: {e['text']}" if days else e["text"]
            if aid:
                items.append({"type": "Assignment", "content_id": aid, "title": t, "indent": 1})
            else:
                warnings.append(f"week {w['n']}: no Canvas assignment matched exercise '{e['text']}'")
                items.append({"type": "SubHeader", "title": t, "indent": 1})
    if w["reading"]:
        items.append({"type": "SubHeader", "title": "Read before class"})
        for key, detail in w["reading"]:
            line, fname, fid = reading_line(key, detail, warnings, w["n"])
            plain = re.sub(r"<[^>]+>", "", line.split(" — ")[0])
            short = plain.split(",")[0]
            t = f"Read: {short}" + (f", {detail}" if detail and key in READINGS else "")
            if fid:
                items.append({"type": "File", "content_id": fid, "title": t, "indent": 1})
            else:
                items.append({"type": "SubHeader", "title": t, "indent": 1})
    for verb, entries in (("Assigned", w["assigned"]), ("Due", w["due"])):
        if not entries:
            continue
        items.append({"type": "SubHeader", "title": f"{verb} this week"})
        for e in entries:
            days = "/".join(DAY_NAMES[d] for d in (e["days"] or []))
            aid = find_id(ASSIGNMENTS, e["text"])
            t = f"{days}: {e['text']}" if days else e["text"]
            if aid is None:
                items.append({"type": "SubHeader", "title": t, "indent": 1})
                continue
            items.append({"type": "Assignment", "content_id": aid, "title": t, "indent": 1})
    return items

# ---------------------------------------------------------------- Canvas API


class Canvas:
    def __init__(self, base, token, dry_run=False):
        self.base = re.sub(r"/api/v1/?$", "", base.rstrip("/"))
        self.token = token
        self.dry = dry_run

    def _req(self, method, path, params=None, data=None):
        url = path if path.startswith("http") else self.base + path
        if params:
            url += "?" + urllib.parse.urlencode(params, doseq=True)
        body, headers = None, {"Authorization": f"Bearer {self.token}"}
        if data is not None:
            body = json.dumps(data).encode()
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=body, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                txt = r.read().decode()
                link = r.headers.get("Link", "")
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"{method} {path} -> {e.code}: {e.read().decode()[:500]}")
        return (json.loads(txt) if txt else None), link

    def get_all(self, path, params=None):
        params = dict(params or {})
        params["per_page"] = 100
        data, link = self._req("GET", path, params)
        out = list(data)
        while True:
            m = re.search(r'<([^>]+)>;\s*rel="next"', link)
            if not m:
                break
            data, link = self._req("GET", m.group(1))
            out.extend(data)
        return out

    def write(self, method, path, data=None):
        if self.dry:
            print(f"  [dry] {method} {path} {json.dumps(data) if data else ''}"[:160])
            return {"id": 0, "url": "dry-run"}
        res, _ = self._req(method, path, None, data)
        return res


def load_env(path):
    env = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def resolve_files(cv, weeks, warnings):
    """Fill FILE_IDS for every file name the grid or the tables refer to.

    When several files share a name (re-uploads), the most recently updated
    one wins and a warning names the duplicates.
    """
    c = f"/api/v1/courses/{COURSE_ID}"
    names = {SYLLABUS_FILE} | {fname for _, fname in READINGS.values()}
    for w in weeks:
        names |= {t for t, _, is_url in w["media"] if not is_url}
        names |= {k for k, _ in w["reading"] if "." in k}
    files = cv.get_all(f"{c}/files", {"sort": "updated_at", "order": "desc"})
    for name in sorted(names):
        matches = [f for f in files if f.get("display_name") == name]
        if not matches:
            warnings.append(f"file not found in Canvas Files: {name}")
            continue
        FILE_IDS[name] = matches[0]["id"]
        if len(matches) > 1:
            warnings.append(f"{len(matches)} files named {name}; using newest (id {matches[0]['id']}), "
                            f"others: {', '.join(str(f['id']) for f in matches[1:])}")


def sync(weeks, cv, warnings):
    c = f"/api/v1/courses/{COURSE_ID}"
    course, _ = cv._req("GET", c)
    if COURSE_GUARD not in course["name"].upper():
        sys.exit(f"Refusing: course {COURSE_ID} is '{course['name']}'")
    print(f"Course: {course['name']}")
    resolve_files(cv, weeks, warnings)

    existing_modules = cv.get_all(f"{c}/modules")
    by_name = {m["name"]: m for m in existing_modules}
    existing_pages = {p["title"]: p for p in cv.get_all(f"{c}/pages")}

    def upsert_page(title, body):
        if title in existing_pages:
            p = existing_pages[title]
            cv.write("PUT", f"{c}/pages/{p['url']}", {"wiki_page": {"title": title, "body": body, "published": True}})
            print(f"  updated page: {title}")
            return p["url"]
        p = cv.write("POST", f"{c}/pages", {"wiki_page": {"title": title, "body": body, "published": True}})
        print(f"  created page: {title}")
        existing_pages[title] = p
        return p.get("url", re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"))

    def upsert_module(name, position, match_prefix):
        # Match on the stable prefix ("Week 05 (21 Sep)") so topic renames still update in place.
        found = next((m for n, m in by_name.items() if n.startswith(match_prefix)), None)
        if found:
            if found["name"] != name or found["position"] != position:
                cv.write("PUT", f"{c}/modules/{found['id']}", {"module": {"name": name, "position": position}})
            print(f"module (existing): {name}")
            for it in cv.get_all(f"{c}/modules/{found['id']}/items"):
                cv.write("DELETE", f"{c}/modules/{found['id']}/items/{it['id']}")
            return found["id"]
        m = cv.write("POST", f"{c}/modules", {"module": {"name": name, "position": position}})
        print(f"module (new): {name}")
        by_name[name] = {**m, "name": name, "position": position}
        return m["id"]

    def add_item(mid, it, pos):
        payload = {"type": it["type"], "position": pos, "indent": it.get("indent", 0)}
        if it.get("title"):
            payload["title"] = it["title"]
        if it["type"] == "Page":
            payload["page_url"] = it["page_url"]
        elif it["type"] in ("Assignment", "File"):
            payload["content_id"] = it["content_id"]
        elif it["type"] == "ExternalUrl":
            payload["external_url"] = it["url"]
            payload["new_tab"] = it.get("new_tab", False)
        res = cv.write("POST", f"{c}/modules/{mid}/items", {"module_item": payload})
        if it["type"] in ("ExternalUrl", "SubHeader") and not cv.dry:
            cv.write("PUT", f"{c}/modules/{mid}/items/{res['id']}", {"module_item": {"published": True}})

    def publish_module(mid):
        cv.write("PUT", f"{c}/modules/{mid}", {"module": {"published": True}})

    # Start here
    sched_url = upsert_page("Semester schedule", render_full_schedule(weeks, warnings))
    start_url = upsert_page("Start here", start_here_body(existing_pages))
    mid = upsert_module("Start here", 1, "Start here")
    start_items = [{"type": "Page", "page_url": start_url, "title": "Start here"}]
    if file_id(SYLLABUS_FILE):
        start_items.append({"type": "File", "content_id": file_id(SYLLABUS_FILE), "title": "Syllabus"})
    start_items.append({"type": "Page", "page_url": sched_url, "title": "Semester schedule"})
    for title in HW_PAGES:
        if title in existing_pages:
            start_items.append({"type": "Page", "page_url": existing_pages[title]["url"], "title": title})
        else:
            warnings.append(f"page '{title}' not found; run hw/hwInstructions/hw2canvas.py to create it")
    for pos, it in enumerate(start_items, start=1):
        add_item(mid, it, pos)
    publish_module(mid)

    # Weeks
    for i, w in enumerate(weeks, start=2):
        name = module_name(w)
        mid = upsert_module(name, i, week_label(w))
        for pos, it in enumerate(plan_items(w, warnings), start=1):
            if it["type"] == "Page":
                it["page_url"] = upsert_page(it["page_title"], render_overview(w, warnings))
            add_item(mid, it, pos)
            print(f"   + {it['type']:<11} {it.get('title', '')}")
        publish_module(mid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--print-html", action="store_true", help="dump generated overview HTML to stdout and exit")
    args = ap.parse_args()

    weeks = build_weeks(parse_rec(REC_PATH))
    warnings = []

    if args.print_html:
        for w in weeks:
            print(f"\n<!-- {module_name(w)} -->")
            print(render_overview(w, warnings))
            for it in plan_items(w, warnings):
                print("  ITEM", it["type"], it.get("title"))
        print("\n<!-- full schedule -->")
        print(render_full_schedule(weeks, warnings))
        for wmsg in sorted(set(warnings)):
            print("WARNING:", wmsg, file=sys.stderr)
        return

    env = load_env(ENV_PATH)
    cv = Canvas(env["CANVAS_API_URL"], env["CANVAS_API_TOKEN"], dry_run=args.dry_run)
    sync(weeks, cv, warnings)
    for wmsg in sorted(set(warnings)):
        print("WARNING:", wmsg, file=sys.stderr)


if __name__ == "__main__":
    main()
