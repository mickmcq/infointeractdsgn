-- Carry the .weekn span style (theme.scss: UT orange, bold italic) into
-- LaTeX output, where a bare span class would otherwise be dropped.
function Span(span)
  if not quarto.doc.is_format("latex") then return nil end
  if not span.classes:includes("weekn") then return nil end
  local out = pandoc.List({ pandoc.RawInline("latex", "\\weekn{") })
  out:extend(span.content)
  out:insert(pandoc.RawInline("latex", "}"))
  return out
end
