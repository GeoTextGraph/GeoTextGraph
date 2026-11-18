-- Allow the long category labels to wrap within the PDF page margins.
function Table(tbl)
  if #tbl.head.rows > 0 then
    local first_header = pandoc.utils.stringify(tbl.head.rows[1].cells[1].contents)
    if first_header == "Category" then
      tbl.colspecs = {
        {pandoc.AlignLeft, 0.62},
        {pandoc.AlignRight, 0.18},
        {pandoc.AlignRight, 0.20}
      }
    end
  end
  return tbl
end

-- Preserve the Markdown author block's centering when producing LaTeX/PDF.
function RawBlock(block)
  if FORMAT:match("latex") and block.format == "html" then
    if block.text:match('^<div align="center">%s*$') then
      return pandoc.RawBlock("latex", "\\begin{center}")
    elseif block.text:match("^</div>%s*$") then
      return pandoc.RawBlock("latex", "\\end{center}")
    end
  end
end

-- The report title is centered and uses normal font weight inside its HTML block.
function Header(header)
  if FORMAT:match("latex") and header.level == 1 then
    local title = pandoc.write(pandoc.Pandoc({pandoc.Plain(header.content)}), "latex")
    return pandoc.RawBlock("latex", "{\\LARGE " .. title .. "\\par}\\medskip")
  end
end
