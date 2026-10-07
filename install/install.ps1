# Verificacao somente leitura. Nenhum parametro antigo autoriza copia ou sobrescrita.
param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$LegacyArguments
)
$ErrorActionPreference = "Stop"
if ($LegacyArguments.Count -gt 0) {
  Write-Error "Flags legadas recusadas. Leia INSTALL.md; nenhum arquivo foi alterado."
  exit 2
}
$Root = Split-Path -Parent $PSScriptRoot
$Python = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $Python) { $Python = Get-Command python -ErrorAction SilentlyContinue }
if (-not $Python) { Write-Error "Python 3.10+ necessario; nada instalado."; exit 2 }
$Previous = $env:PYTHONDONTWRITEBYTECODE
try {
  $env:PYTHONDONTWRITEBYTECODE = "1"
  & $Python.Source (Join-Path $Root "scripts/validate_standard.py")
  $Result = $LASTEXITCODE
} finally {
  $env:PYTHONDONTWRITEBYTECODE = $Previous
}
if ($Result -ne 0) { exit $Result }
Write-Host "Pacote validado. Instalacao/migracao seguem INSTALL.md; nenhum arquivo de projeto foi copiado."
