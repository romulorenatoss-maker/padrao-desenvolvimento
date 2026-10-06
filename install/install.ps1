param(
  [string]$ProjectPath = ".",
  [switch]$InstallSkills,
  [switch]$InitializeProject
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Project = (Resolve-Path $ProjectPath).Path

function Copy-Skills($target) {
  New-Item -ItemType Directory -Force -Path $target | Out-Null
  Get-ChildItem (Join-Path $Root "skills") -Directory | ForEach-Object {
    $dest = Join-Path $target $_.Name
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item (Join-Path $_.FullName "SKILL.md") (Join-Path $dest "SKILL.md") -Force
  }
}

if ($InstallSkills) {
  Copy-Skills (Join-Path $HOME ".agents\skills")
  Copy-Skills (Join-Path $HOME ".claude\skills")
  Write-Host "Skills instaladas para Codex e Claude no perfil atual."
}

if ($InitializeProject) {
  $agents = Join-Path $Project "AGENTS.md"
  $claude = Join-Path $Project "CLAUDE.md"

  if (Test-Path $agents) {
    Write-Host "AGENTS.md existente: NAO ALTERADO. Integre manualmente para preservar regras locais."
  } else {
    Copy-Item (Join-Path $Root "templates\AGENTS.md") $agents
    Write-Host "AGENTS.md criado a partir do template."
  }

  if (Test-Path $claude) {
    Write-Host "CLAUDE.md existente: NAO ALTERADO."
  } else {
    Copy-Item (Join-Path $Root "templates\CLAUDE.md") $claude
    Write-Host "CLAUDE.md criado apontando para AGENTS.md."
  }
}

if (-not $InstallSkills -and -not $InitializeProject) {
  Write-Host "Nada alterado. Use -InstallSkills e/ou -InitializeProject."
}
