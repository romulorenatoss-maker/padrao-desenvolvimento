# Instalacao

O repositorio e privado: a conta/cliente precisa ter acesso de leitura ao GitHub `romulorenatoss-maker/romulo-dev-standard`.

## Codex
```
codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main
codex plugin add romulo-dev-standard@romulo-dev-standard
codex plugin list
```
`codex plugin list` deve mostrar `romulo-dev-standard@romulo-dev-standard  installed, enabled`. Abra uma nova sessao Codex para as skills serem descobertas.

Atualizar instalacao existente:
```
codex plugin marketplace upgrade romulo-dev-standard
codex plugin add romulo-dev-standard@romulo-dev-standard
```

## Claude Code
Numa sessao `claude` interativa:
```
/plugin marketplace add romulorenatoss-maker/romulo-dev-standard
/plugin install romulo-dev-standard@romulo-dev-standard
```
Reinicie a sessao para carregar as skills.

Atualizar instalacao existente:
```
/plugin marketplace update romulo-dev-standard
```
e reinicie a sessao.

## Verificacao das 7 skills
Em uma sessao nova, as skills abaixo devem aparecer na lista de skills do agente (nao basta existirem no disco):
- romulo-analisar
- romulo-construir
- romulo-seguranca
- romulo-documentacao
- romulo-prototipo-real
- romulo-verificar
- romulo-auditar-projeto

Se alguma faltar: informar `ROMULO_STANDARD_NAO_DISPONIVEL` e nao fingir aplicacao.

## Fallback manual (somente explicito)
Use apenas quando o mecanismo de plugin nao estiver disponivel e o usuario autorizar. A partir de um clone deste repositorio, no Windows PowerShell:
```
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -InstallSkills
```
Copia as skills para `~/.agents/skills` e `~/.claude/skills`. Para atualizar, rode `git pull` no clone e repita o comando. Nao use o fallback para esconder falha do plugin.

Para inicializar um projeto sem contrato:
```
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectPath C:\caminho\projeto -InitializeProject
```
Se AGENTS.md ou CLAUDE.md ja existirem, o instalador NAO sobrescreve.

## Ponytail
Dependencia externa: instale pela distribuicao oficial (https://github.com/DietrichGebert/ponytail). O Romulo Dev Standard exige Ponytail `full` quando disponivel, mas nao copia nem altera seus arquivos. Indisponivel: `PONYTAIL_NAO_DISPONIVEL`.

## Projeto existente
Nao substitua AGENTS.md existente automaticamente. Rode primeiro `romulo-auditar-projeto`, compare regras locais e integre somente o que for autorizado.
