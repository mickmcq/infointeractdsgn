#!/usr/bin/env python3
"""Push hwInstructions.qmd into Canvas assignment descriptions.

hwInstructions.qmd is the single source of truth for homework instructions.
This script renders it with pandoc (citations resolved from master.bib),
splits it at the headings, and writes

  * a Canvas page "Rules for all milestones": the project overview, the
    project-website and diverge/converge advice, the final presentation,
    milestone critiques, and project management;
  * a Canvas page "Rules for all exercises": file naming, the two sketches
    of good design, sketchbook, diverge/converge, time, storytelling, and
    the post-submission reflections;
  * a Canvas page "Optional exercises": the ungraded exercises;
  * each graded assignment's description: a short header box (link to the
    rules page, the files to submit, the points), then the assignment's own
    section, then (for exercises) its objectives, then the references it
    cites;
  * each assignment's points_possible, from POINTS below, written only when
    Canvas disagrees.

Images referenced from the qmd are uploaded to Canvas Files (folder
hwImages) when a file of the same name is not already in the course.

Usage:
    python3 hw2canvas.py --dry-run      # show what would change, write nothing
    python3 hw2canvas.py                # update the pages and descriptions
    python3 hw2canvas.py --print ID     # dump the generated HTML for one assignment
    python3 hw2canvas.py --print-page "Rules for all exercises"

Re-running is safe: everything is rewritten in place. Assignments not listed
in ASSIGNMENTS (in-class work, peer evals, the exam, attendance) are never
touched.

Credentials come from ~/courses/canvas-mcp/.env (CANVAS_API_TOKEN,
CANVAS_API_URL). Only the Python standard library is used.
"""

import argparse
import html
import json
import mimetypes
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
QMD = os.path.join(HERE, "hwInstructions.qmd")
BIB = os.path.join(HERE, "master.bib")
ENV_PATH = os.path.expanduser("~/courses/canvas-mcp/.env")

COURSE_ID = 1456671  # Fa26 INFORMATION/INTERACTION DESIGN (30525), I 320U
COURSE_GUARD = "INFORMATION/INTERACTION DESIGN"
IMAGE_FOLDER = "hwImages"

MILESTONE_RULES = "Rules for all milestones"
EXERCISE_RULES = "Rules for all exercises"
OPTIONAL_PAGE = "Optional exercises"

# ---------------------------------------------------------------- mapping
#
# Heading paths are tuples of heading-text prefixes, matched case-insensitively
# and scoped to the parent, so ("Exercises", "Exercise objectives", "Picking")
# and ("Exercises", "Mandatory", "Picking") are distinct.

MS = "Milestones"
EX = "Exercises"
MAND = (EX, "Mandatory Exercises")
OBJ = (EX, "Exercise objectives")

MILESTONE_NOTE = ("Team deliverable: every member submits the URL of the team website. "
                  "The milestone section on the website is what is graded.")


def milestone(path, points, files=None, note=MILESTONE_NOTE):
    return dict(kind="milestone", specific=path, objectives=None, points=points,
                files=files or [], note=note)


def exercise(stem, specific, objectives, points=5):
    files = [f"{n:02d}{stem}.jpg" for n in (1, 2, 3)]
    return dict(kind="exercise", specific=specific, objectives=objectives, points=points,
                files=files,
                note="Three photographs: the exercise itself plus two hand-drawn sketches "
                     "of good design. jpg, png, or pdf; one file per upload, no zip.")


ASSIGNMENTS = {
    # milestones
    7763407: milestone((MS, "Milestone 1"), 5),
    7763408: milestone((MS, "Milestone 2"), 10),
    7763410: milestone((MS, "Milestone 3"), 5),
    7763411: milestone((MS, "Milestone 4"), 5),
    7763412: milestone((MS, "Milestone 5"), 10,
                       note="Team deliverable: every member submits the URL of the team website, "
                            "which must link to the walkthrough video. You may also upload the video."),
    # exercises
    7763395: exercise("drawAFace", MAND + ("Draw a face",), OBJ + ("Drawing a face",)),
    7763396: exercise("pickingUpAKey", MAND + ("Picking up a key",), OBJ + ("Picking up a key",)),
    7763397: exercise("widgetRedesign", MAND + ("Widget redesign",), OBJ + ("Widget redesign",)),
    7763398: exercise("recordInteraction", MAND + ("Record interaction",), OBJ + ("Record interaction",)),
    7763399: exercise("ambientNotification", MAND + ("Ambient notification",), OBJ + ("Ambient notification",)),
    7763400: exercise("corporateDirectory", MAND + ("Corporate directory",), OBJ + ("Corp directory",)),
    7763401: exercise("captions", MAND + ("Captions",), None),
    7763402: exercise("elevator", MAND + ("Thousand floor elevator",), OBJ + ("Elevator",)),
    # in-class, ungraded
    7763403: dict(kind="exercise", specific=(EX, "Other Exercises", "Extreme Emphasis"), objectives=None,
                  points=None, files=["extremeEmphasis.jpg"],
                  note="Done in class; ungraded. Upload a photograph of the lettered page from your sketchbook."),
}

# Points in the syllabus: milestones 5+10+5+5+10, exercises 8 x 5. The rest of
# the 100 is the exam (15) and attendance (10), which this script never touches.
TOTAL_POINTS = 75

# ---------------------------------------------------------------- pandoc + split

HEADING = re.compile(r"<h([1-6])\b[^>]*>(.*?)</h\1>", re.S)


def render_qmd():
    """Render the qmd body with pandoc; returns HTML (no standalone wrapper)."""
    cmd = ["pandoc", QMD, "-f", "markdown", "-t", "html", "--wrap=none",
           "--math-method=plain", "--citeproc", "--bibliography", BIB]
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def split_sections(doc_html):
    """Return (preamble_html, sections): sections is a list of dicts
    {level, title, body} in document order; body is the HTML between this
    heading and the next heading of any level."""
    parts = list(HEADING.finditer(doc_html))
    preamble = doc_html[: parts[0].start()] if parts else doc_html
    sections = []
    for i, m in enumerate(parts):
        end = parts[i + 1].start() if i + 1 < len(parts) else len(doc_html)
        title = re.sub(r"<[^>]+>", "", m.group(2))
        title = html.unescape(re.sub(r"\s+", " ", title)).strip()
        sections.append({"level": int(m.group(1)), "title": title, "body": doc_html[m.end():end]})
    return preamble, sections


class Doc:
    def __init__(self, doc_html):
        self.preamble, self.sections = split_sections(doc_html)
        # Reference entries by citekey, from the citeproc bibliography.
        self.refs = {m.group(1): m.group(0) for m in re.finditer(
            r'<div id="ref-([^"]+)" class="csl-entry"[^>]*>.*?</div>', doc_html, re.S)}
        # Footnotes by number.
        self.footnotes = {m.group(1): m.group(2) for m in re.finditer(
            r'<li id="fn(\d+)"[^>]*>(.*?)</li>', doc_html, re.S)}

    def _find(self, path):
        """Locate the section index for a path of heading-text prefixes."""
        idx, level_floor = -1, 0
        for prefix in path:
            found = None
            for j in range(idx + 1, len(self.sections)):
                s = self.sections[j]
                if idx >= 0 and s["level"] <= self.sections[idx]["level"]:
                    break  # left the parent
                if s["title"].lower().startswith(prefix.lower()) and s["level"] > level_floor:
                    found = j
                    break
            if found is None:
                raise KeyError(f"heading not found: {' > '.join(path)}")
            idx, level_floor = found, self.sections[found]["level"]
        return idx

    def section_html(self, path, include_children=True, demote=1, heading=True):
        """HTML of a section (heading + body [+ subsections])."""
        i = self._find(path)
        s = self.sections[i]
        out = [self._heading(s, demote) if heading else "", s["body"]]
        if include_children:
            for t in self.sections[i + 1:]:
                if t["level"] <= s["level"]:
                    break
                out.append(self._heading(t, demote))
                out.append(t["body"])
        return "".join(out)

    @staticmethod
    def _heading(s, demote):
        lvl = min(6, s["level"] + demote)
        return f"<h{lvl}>{html.escape(s['title'])}</h{lvl}>\n"

    def with_notes(self, frag):
        """Append the references and footnotes a fragment uses; inline the
        footnote markers so they no longer point at a missing anchor."""
        keys = []
        for m in re.finditer(r'data-cites="([^"]+)"', frag):
            for k in m.group(1).split():
                if k not in keys:
                    keys.append(k)
        fns = re.findall(r'<a href="#fn(\d+)"[^>]*><sup>\d+</sup></a>', frag)
        frag = re.sub(r'<a href="#fn(\d+)"[^>]*>(<sup>\d+</sup>)</a>', r"\2", frag)
        if fns:
            frag += "<h4>Notes</h4>\n" + "".join(
                f"<p><sup>{n}</sup> {self._strip_backref(self.footnotes.get(n, ''))}</p>\n" for n in fns)
        entries = [self.refs[k] for k in keys if k in self.refs]
        if entries:
            frag += "<h4>References</h4>\n" + "".join(entries)
        return frag

    @staticmethod
    def _strip_backref(note_html):
        note_html = re.sub(r'<a href="#fnref\d+"[^>]*>.*?</a>', "", note_html, flags=re.S)
        return re.sub(r"^\s*<p>(.*)</p>\s*$", r"\1", note_html.strip(), flags=re.S)

# ---------------------------------------------------------------- assembly

MATH_SYMBOLS = {r"\times": "×", r"\pm": "±", r"\ldots": "…", r"\deg": "°"}


def tidy(frag):
    """Make pandoc's HTML behave inside the Canvas editor."""
    def math(m):
        body = m.group(1).strip()
        body = re.sub(r"^\\\((.*)\\\)$", r"\1", body).strip()
        return MATH_SYMBOLS.get(body, body)
    frag = re.sub(r'<span class="math inline">(.*?)</span>', math, frag, flags=re.S)
    frag = frag.replace("<figure>", "<div>").replace("</figure>", "</div>")
    frag = frag.replace(' data-fig-alt="', ' alt="')
    frag = re.sub(r"<figcaption[^>]*>(.*?)</figcaption>", r"<p><i>\1</i></p>", frag, flags=re.S)
    return frag


def rewrite_images(frag, file_ids, warnings):
    """Point <img src> and <a href> at Canvas Files when the target is a bare
    file name (no scheme, no path) that exists in the course."""
    def sub(m):
        name = os.path.basename(m.group(1))
        fid = file_ids.get(name)
        if not fid:
            warnings.append(f"image not found in Canvas Files: {name}")
            return m.group(0)
        return m.group(0).replace(m.group(1), f"/courses/{COURSE_ID}/files/{fid}/preview")
    frag = re.sub(r'<img\b[^>]*\bsrc="([^"]+)"', sub, frag)

    def link(m):
        name = m.group(1)
        if re.match(r"^[\w.-]+\.\w+$", name) and name in file_ids:
            return m.group(0).replace(f'href="{name}"', f'href="/courses/{COURSE_ID}/files/{file_ids[name]}"')
        if re.match(r"^[\w.-]+\.\w+$", name) and not name.endswith((".html", ".htm")):
            warnings.append(f"linked file not found in Canvas Files: {name}")
        return m.group(0)
    frag = re.sub(r'<a\b[^>]*\bhref="([^"#/:]+)"', link, frag)

    def fit(m):
        tag = m.group(0)
        if 'style="' in tag:
            return tag.replace('style="', 'style="max-width:100%;height:auto;', 1)
        return tag.replace("<img ", '<img style="max-width:100%;height:auto" ', 1)
    return re.sub(r"<img\b[^>]*>", fit, frag)


def header_box(spec, rules_url, rules_title):
    bits = [f'Read the <a href="{rules_url}">{rules_title}</a> first.']
    if spec.get("files"):
        names = ", ".join(f"<code>{f}</code>" for f in spec["files"])
        bits.append(f"Submit: {names}.")
    if spec.get("note"):
        bits.append(html.escape(spec["note"]))
    if spec.get("points") is not None:
        bits.append(f"{spec['points']} points.")
    return ('<div style="border-left:4px solid #bf5700;background:#f7f7f7;padding:8px 12px;margin-bottom:12px">'
            + " ".join(bits) + "</div>\n")


def build_description(doc, spec, rules_urls, file_ids, warnings):
    title = MILESTONE_RULES if spec["kind"] == "milestone" else EXERCISE_RULES
    parts = [header_box(spec, rules_urls.get(title, "#"), title)]
    parts.append(doc.section_html(spec["specific"], demote=0))
    if spec.get("objectives"):
        parts.append("<h3>Objectives</h3>\n")
        parts.append(doc.section_html(spec["objectives"], heading=False))
    body = doc.with_notes("".join(parts))
    return rewrite_images(tidy(body), file_ids, warnings)


def build_milestone_rules(doc, file_ids, warnings):
    body = ("<p>The milestones together make up the team project. Each milestone's full "
            "instructions are in its Description on the Assignments page; the rules and "
            "advice below apply to all of them.</p>")
    body += doc.section_html((MS,), include_children=False, heading=False)
    for path in ((MS, "Create a project website"), (MS, "Diverge, then converge"),
                 (MS, "Final project presentation"), (MS, "Milestone critiques"),
                 (MS, "Project management")):
        body += doc.section_html(path, demote=0)
    body += footer()
    return rewrite_images(tidy(doc.with_notes(body)), file_ids, warnings)


def build_exercise_rules(doc, file_ids, warnings):
    body = ("<p>Exercises are individual work. Each exercise's full instructions are in its "
            "Description on the Assignments page; the rules below apply to all of them. "
            "Ungraded exercises you may try for feedback are on the "
            f"<a href=\"__OPTIONAL__\">{OPTIONAL_PAGE}</a> page.</p>")
    body += doc.section_html((EX, "Completing exercises"), demote=0)
    body += doc.section_html((EX, "Exercise reflection"), demote=0)
    body += footer()
    return rewrite_images(tidy(doc.with_notes(body)), file_ids, warnings)


def build_optional_page(doc, file_ids, warnings):
    body = doc.section_html((EX, "Other Exercises"), demote=0, heading=False)
    body += footer()
    return rewrite_images(tidy(doc.with_notes(body)), file_ids, warnings)


def footer():
    return ("<p><i>These instructions are maintained in one place and pushed to Canvas; "
            "the Canvas copy is current.</i></p>")

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

    def upload_file(self, course_path, local_path, folder):
        """Three-step Canvas upload; returns the new file's id (0 in dry-run)."""
        name = os.path.basename(local_path)
        if self.dry:
            print(f"  [dry] upload {name} -> {folder}/")
            return 0
        ctype = mimetypes.guess_type(name)[0] or "application/octet-stream"
        meta, _ = self._req("POST", f"{course_path}/files", data={
            "name": name, "size": os.path.getsize(local_path), "content_type": ctype,
            "parent_folder_path": folder, "on_duplicate": "overwrite"})
        boundary = "----hw2canvas" + os.urandom(8).hex()
        parts = []
        for k, v in meta["upload_params"].items():
            parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode())
        with open(local_path, "rb") as f:
            blob = f.read()
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{name}\"\r\n"
                     f"Content-Type: {ctype}\r\n\r\n".encode() + blob + b"\r\n")
        parts.append(f"--{boundary}--\r\n".encode())
        body = b"".join(parts)
        req = urllib.request.Request(meta["upload_url"], data=body, method="POST",
                                     headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
        with urllib.request.urlopen(req, timeout=120) as r:
            txt = r.read().decode()
            location = r.headers.get("Location")
        info = json.loads(txt) if txt.strip().startswith("{") else None
        if not info or "id" not in info:
            if not location:
                raise RuntimeError(f"upload of {name} returned neither JSON nor Location")
            info, _ = self._req("GET" if "confirm" not in location else "POST", location)
        return info["id"]


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

# ---------------------------------------------------------------- main


def image_names(doc_html):
    return sorted({os.path.basename(m.group(1)) for m in re.finditer(r'<img\b[^>]*\bsrc="([^"]+)"', doc_html)
                   if not re.match(r"https?://", m.group(1))})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--print", type=int, metavar="ASSIGNMENT_ID", help="print generated HTML for one assignment")
    ap.add_argument("--print-page", metavar="TITLE", help="print generated HTML for one of the pages")
    args = ap.parse_args()

    doc_html = render_qmd()
    doc = Doc(doc_html)
    warnings = []

    total = sum(spec.get("points") or 0 for spec in ASSIGNMENTS.values())
    if total != TOTAL_POINTS:
        print(f"WARNING: points in ASSIGNMENTS add to {total}, not {TOTAL_POINTS}; check the syllabus",
              file=sys.stderr)

    builders = {MILESTONE_RULES: build_milestone_rules, EXERCISE_RULES: build_exercise_rules,
                OPTIONAL_PAGE: build_optional_page}

    if args.print:
        print(build_description(doc, ASSIGNMENTS[args.print], {}, {}, warnings))
        return
    if args.print_page:
        print(builders[args.print_page](doc, {}, warnings))
        return

    env = load_env(ENV_PATH)
    cv = Canvas(env["CANVAS_API_URL"], env["CANVAS_API_TOKEN"], dry_run=args.dry_run)
    c = f"/api/v1/courses/{COURSE_ID}"
    course, _ = cv._req("GET", c)
    if COURSE_GUARD not in course["name"].upper():
        sys.exit(f"Refusing: course {COURSE_ID} is '{course['name']}'")
    print(f"Course: {course['name']}")

    # Image ids by name (newest wins); upload what is missing.
    files = cv.get_all(f"{c}/files", {"sort": "updated_at", "order": "desc"})
    file_ids = {}
    for f in files:
        file_ids.setdefault(f["display_name"], f["id"])
    for name in image_names(doc_html):
        if name in file_ids:
            continue
        local = os.path.join(HERE, name)
        if not os.path.exists(local):
            warnings.append(f"image missing locally and in Canvas: {name}")
            continue
        file_ids[name] = cv.upload_file(c, local, IMAGE_FOLDER)
        print(f"uploaded image: {name} -> {IMAGE_FOLDER}/")

    # Pages. Build the optional page first so the exercise rules can link to it.
    existing = {p["title"]: p for p in cv.get_all(f"{c}/pages")}
    urls = {}

    def upsert_page(title, body):
        if title in existing:
            slug = existing[title]["url"]
            cv.write("PUT", f"{c}/pages/{slug}", {"wiki_page": {"body": body, "published": True}})
            print(f"updated page: {title}  ({len(body)} chars)")
        else:
            p = cv.write("POST", f"{c}/pages", {"wiki_page": {"title": title, "body": body, "published": True}})
            slug = p.get("url") or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            existing[title] = {"url": slug}
            print(f"created page: {title}  ({len(body)} chars)")
        urls[title] = f"/courses/{COURSE_ID}/pages/{slug}"
        return urls[title]

    upsert_page(OPTIONAL_PAGE, build_optional_page(doc, file_ids, warnings))
    upsert_page(MILESTONE_RULES, build_milestone_rules(doc, file_ids, warnings))
    upsert_page(EXERCISE_RULES,
                build_exercise_rules(doc, file_ids, warnings).replace("__OPTIONAL__", urls[OPTIONAL_PAGE]))

    # Assignment descriptions.
    live = {a["id"]: a for a in cv.get_all(f"{c}/assignments")}
    for aid, spec in ASSIGNMENTS.items():
        if aid not in live:
            warnings.append(f"assignment {aid} not found in course")
            continue
        name = live[aid]["name"]
        desc = build_description(doc, spec, urls, file_ids, warnings)
        payload = {"description": desc}
        have, want = live[aid].get("points_possible"), spec.get("points")
        if want is not None and have != want:
            payload["points_possible"] = want
        cv.write("PUT", f"{c}/assignments/{aid}", {"assignment": payload})
        print(f"updated description: {name}  ({len(desc)} chars)")
        if "points_possible" in payload:
            print(f"updated points: {name}  {have} -> {want}")

    for w in sorted(set(warnings)):
        print("WARNING:", w, file=sys.stderr)


if __name__ == "__main__":
    main()
