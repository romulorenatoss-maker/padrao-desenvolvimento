# Instalacao

Repositorio privado: a conta/cliente precisa ter leitura em `romulorenatoss-maker/romulo-dev-standard`.

## Codex
```
codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main
codex plugin add romulo-dev-standard@romulo-dev-standard
codex plugin list
```
Confirme `romulo-dev-standard@romulo-dev-standard` installed e enabled. Abra nova sessao para descoberta das skills.

Ponytail:
```
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```
Abra `/hooks`, revise e confie nos hooks do Ponytail, e inicie nova thread/sessao.

Atualizar:
```
codex plugin marketplace upgrade romulo-dev-standard
codex plugin add romulo-dev-standard@romulo-dev-standard
```

## Claude Code
Numa sessao interativa, um comando por vez:
```
/plugin marketplace add romulorenatoss-maker/romulo-dev-standard
```
```
/plugin install romulo-dev-standard@romulo-dev-standard
```
```
/plugin marketplace add DietrichGebert/ponytail
```
```
/plugin install ponytail@ponytail
```
Reinicie a sessao.

Atualizar:
```
/plugin marketplace update romulo-dev-standard
```
Reinicie a sessao.

## Verificacao das 9 skills
Uma sessao nova deve descobrir:
- romulo-analisar
- romulo-iniciar-projeto
- romulo-auditar-projeto
- romulo-construir
- romulo-seguranca
- romulo-documentacao
- romulo-prototipo-real
- romulo-verificar
- romulo-evoluir-padrao

Se alguma faltar: `ROMULO_STANDARD_NAO_DISPONIVEL`. Nao fingir aplicacao.

## Projeto vazio
Depois do bootstrap, use `romulo-iniciar-projeto`. Ele cria apenas a base necessaria para a primeira capacidade real, seguindo a arquitetura comum.

## Projeto existente
Use `romulo-auditar-projeto` para diagnostico amplo antes de migracao estrutural ou documental.

## Fallback manual
Somente com autorizacao explicita, a partir de clone deste repositorio:
```
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -InstallSkills
```

Inicializar somente AGENTS/CLAUDE quando ausentes:
```
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectPath C:\caminho\projeto -InitializeProject
```

## Ponytail
Dependencia externa: `DietrichGebert/ponytail` (comandos acima por plataforma). Modo `full` por padrao em toda tarefa tecnica. Indisponivel: `PONYTAIL_NAO_DISPONIVEL`.

## Fluxo do agente
O mesmo para Codex e Claude Code, definido em `templates/AGENTS.md` (secao Bootstrap): detectar plataforma, verificar padrao e Ponytail carregados, instalar automaticamente quando permitido, senao mostrar os comandos e parar, exigir nova sessao, confirmar as 9 skills.

## Evolucao do padrao
Diretriz global nova/corrigida usa `romulo-evoluir-padrao`: editar a fonte central dona da regra, versionar, validar manifests/skills, publicar e atualizar consumidores. Nao copiar regra global em varios AGENTS.md.
