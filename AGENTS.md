# AGENTS.md — Romulo Dev Standard

PROJETO: Romulo Dev Standard
REPOSITORIO_OFICIAL: romulorenatoss-maker/romulo-dev-standard
BRANCH_OFICIAL: main
FINALIDADE: fonte central das diretrizes, skills, references, manifests e templates usados por todos os projetos Romulo.

Este arquivo governa somente este repositorio. Ele NAO e o template de projeto: o contrato distribuido aos projetos consumidores e `templates/AGENTS.md`; consulte-o quando a tarefa envolver esse contrato.

## Regras
- Mudanca global e feita aqui, via `romulo-evoluir-padrao`.
- Cada regra tem uma fonte dona (skill, reference, template ou manifesto). Nao manter duas copias completas da mesma especificacao; os demais artefatos referenciam a fonte dona.
- `templates/` sao artefatos distribuidos; alterar o template altera o comportamento dos consumidores.
- Mudanca em skills, manifests ou templates exige validar a distribuicao: JSON dos manifests, nomes e quantidade das 9 skills, marketplaces de Codex e Claude Code quando o mecanismo for afetado.
- Mudanca distribuivel incrementa a versao nos tres manifests (`plugin.json`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`) e no README.
- Nada de peculiaridade do Mixupa ou de qualquer projeto consumidor aqui.
- Segredos nunca entram em skill, template, documentacao ou Git.
