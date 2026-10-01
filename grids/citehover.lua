-- Run after --citeproc. Copies each bibliography entry into the title
-- attribute of its citation so hovering shows the full reference, then
-- drops the bibliography block so the table stands alone.
local refs = {}

function Pandoc(doc)
  local kept = {}
  for _, b in ipairs(doc.blocks) do
    if b.t == 'Div' and b.identifier == 'refs' then
      for _, entry in ipairs(b.content) do
        if entry.t == 'Div' then
          local id = entry.identifier:gsub('^ref%-', '')
          refs[id] = pandoc.utils.stringify(entry)
        end
      end
    else
      table.insert(kept, b)
    end
  end
  doc.blocks = kept
  return doc:walk {
    Cite = function(c)
      local tips = {}
      for _, ci in ipairs(c.citations) do
        if refs[ci.id] then table.insert(tips, refs[ci.id]) end
      end
      if #tips > 0 then
        return pandoc.Span(c.content, {class = 'citation', title = table.concat(tips, '\n')})
      end
    end
  }
end
