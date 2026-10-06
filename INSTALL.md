# Instalacao

## Via marketplace/plugin
O repositorio contem manifestos para Codex/Agent Plugins e Claude Code. Como o repositorio e privado, a conta/cliente precisa ter acesso ao GitHub correspondente.

Codex:
`codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main`

Depois instale/ative `romulo-dev-standard` pelo mecanismo de plugins disponivel no cliente.

Claude Code:
`/plugin marketplace add romulorenatoss-maker/romulo-dev-standard`
e depois instale `romulo-dev-standard@romulo-dev-standard`.

## Instalacao direta de skills
Clone este repositorio e, no Windows PowerShell:
`powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -InstallSkills`

Para inicializar um projeto que ainda nao tenha contrato:
`powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectPath C:\caminho\projeto -InitializeProject`

Se AGENTS.md ou CLAUDE.md ja existirem, o instalador NAO sobrescreve.

## Ponytail
Ponytail permanece dependencia externa. Instale a versao oficial separadamente. O Romulo Dev Standard exige seu uso quando disponivel, mas nao copia nem altera os arquivos do Ponytail.

## Projeto existente
Nao substitua AGENTS.md existente automaticamente. Rode primeiro `romulo-auditar-projeto`, compare regras locais e integre somente o que for autorizado.
