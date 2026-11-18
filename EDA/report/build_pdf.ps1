$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    pandoc 'dbpedia_eda_report.md' --from=gfm --standalone --pdf-engine=xelatex --resource-path=. --lua-filter=table_layout.lua -V 'geometry:a4paper,margin=20mm' -V 'fontsize=10pt' -V 'colorlinks=true' --output='dbpedia_eda_report.pdf'
    if ($LASTEXITCODE -ne 0) { throw "Pandoc failed with exit code $LASTEXITCODE" }
}
finally {
    Pop-Location
}
