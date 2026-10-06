# Instalacao

Repositorio privado: a conta/cliente precisa ter leitura em `romulorenatoss-maker/romulo-dev-standard`.

## Codex
```
codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main
codex plugin add romulo-dev-standard@romulo-dev-standard
codex plugin list
```
Abra nova sessao para descoberta das skills.

Atualizar:
```
codex plugin marketplace upgrade romulo-dev-standard
codex plugin add romulo-dev-standard@romulo-dev-standard
```

## Claude Code
Numa sessao interativa:
```
/plugin marketplace add romulorenatoss-maker/romulo-dev-standard
/plugin install romulo-dev-standard@romulo-dev-standard
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
Dependencia externa pela distribuicao oficial. Usar modo `full` quando disponivel. Indisponivel: `PONYTAIL_NAO_DISPONIVEL`.

## Evolucao do padrao
Diretriz global nova/corrigida usa `romulo-evoluir-padrao`: editar a fonte central dona da regra, versionar, validar manifests/skills, publicar e atualizar consumidores. Nao copiar regra global em varios AGENTS.md.
