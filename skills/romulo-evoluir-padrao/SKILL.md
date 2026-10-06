---
name: romulo-evoluir-padrao
description: Use quando uma diretriz global, regra de arquitetura, seguranca, documentacao, bootstrap, verificacao ou comportamento comum a todos os projetos precisar ser criada, corrigida ou aprimorada.
---

# Romulo Evoluir Padrao

Diretriz global pertence ao repositorio central:
romulorenatoss-maker/romulo-dev-standard

Nao corrigir uma regra global copiando ou divergindo texto em AGENTS.md de projetos individuais.

## Fluxo

1. provar que a mudanca e global e nao peculiaridade de um unico projeto;
2. localizar a skill, reference, template ou manifesto dono da regra;
3. alterar a menor fonte central necessaria;
4. atualizar referencias e templates somente quando realmente afetados;
5. incrementar a versao do padrao quando houver mudanca distribuivel;
6. validar manifestos, nomes de skills e bootstrap;
7. commit/push somente no repositorio central com autorizacao aplicavel;
8. atualizar/recarregar o plugin nos ambientes consumidores;
9. confirmar que uma sessao nova descobre a versao e as skills esperadas;
10. somente depois ajustar AGENTS locais quando houver peculiaridade ou migracao necessaria.

## Fonte unica

Ao mudar uma regra global: `romulo-evoluir-padrao` -> identificar a fonte dona -> alterar a skill/reference/template correta -> atualizar outros artefatos somente se forem consumidores daquela regra -> versionar -> validar -> publicar.

Nao manter duas copias completas da mesma especificacao. `AGENTS.md` da raiz governa este repositorio; `templates/AGENTS.md` e o contrato distribuido aos projetos.

## Regra de propriedade

- comportamento comum a todos os projetos -> skill/reference central;
- identidade, repo, banco, deploy, autorizacao e guardas particulares -> AGENTS.md local;
- simplificacao complementar -> Ponytail;
- segredo/credencial -> nunca em skill, template ou Git.

Nao duplicar uma regra global em varios AGENTS.md para contornar falha de distribuicao. Corrigir a distribuicao ou declarar o bloqueio.

Se uma mudanca global quebrar compatibilidade, registrar a versao e exigir migracao explicita em vez de alterar silenciosamente projetos fixados em versao anterior.
