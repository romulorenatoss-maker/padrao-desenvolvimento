---
name: evoluir-padrao
description: "Use quando mudar uma diretriz comum, arquitetura, seguranca, documentacao, bootstrap, estrutura, criacao de arquivos ou verificacao no repositorio central."
---

# Evoluir Padrao

Diretriz global pertence a `romulorenatoss-maker/padrao-desenvolvimento`. Ler AGENTS da raiz e [README central](../../README.md). O README e a entrada/catalogo; templates sao distribuiveis; AGENTS da raiz governa so este repo.

Fluxo: provar alcance global -> localizar skill/reference/template dono -> alterar menor fonte necessaria -> reconciliar consumidores -> versionar todos os manifests e README -> validar -> publicar com autorizacao aplicavel -> atualizar/recarregar consumidores -> comprovar ativacao ou declarar pendente.

Cada regra tem uma fonte dona. Referencias aprofundam e outras skills apontam; nao copiar especificacao completa nem adicionar skill redundante. Nao copiar lista/contagem/roteamento para AGENTS locais. Padrao de criacao de AGENTS/CLAUDE mora em `iniciar-projeto`; destinos/modulos em references/ARQUITETURA.md; documentos em references/DOCUMENTACAO.md; autorizacao de novos arquivos em `analisar`.

Gate de arquivos tambem se aplica aqui: preferir atualizar fontes existentes. Nova skill/reference/script somente quando determinado pela evolucao explicitamente solicitada e necessario a uma responsabilidade ausente, com nome, destino e consumidor declarados antes. Se fora da previsao, exigir 0393 especifico. Nao editar politica por iniciativa propria para legitimar arquivo que outra operacao desejava criar.

Validar manifestos, catalogo nominal, caminhos, links, templates, roteamento e cenarios negativos. Mudanca do modelo minimo exige atualizar o validador sem retirar verificacoes legitimas. Nao alegar execucao/ativacao de modelos ou plugins a partir de teste estrutural.

Mudanca de compatibilidade exige instrucao de migracao explicita. Consumidor nao e reescrito silenciosamente; guardas/dados/infraestrutura/regras de negocio locais ficam la. Migracao de AGENTS protegido requer sua autorizacao especifica e preservacao documental antes de remover texto. Segredos nunca entram em skill/template/Git.
