---
name: romulo-auditar-projeto
description: "Use para organizar um projeto existente ou diagnosticar arquitetura/documentacao/UI amplamente: descobrir a estrutura, separar responsabilidades reais, propor destinos e criar apenas faltas comprovadas dentro do alcance autorizado."
---

# Romulo Auditar Projeto

Primeira passagem somente leitura. "Organizar tudo" permite levantar todo o escopo do projeto, nao apagar, recriar ou migrar tudo silenciosamente. Confirmar identidade, branch/worktree, ambiente, alcance e fontes com `romulo-analisar`.

## Procedimento para projeto recebido
1. Ler entradas, stack/framework, rotas/jobs, componentes/views, regras/servicos/contratos, persistencia, autenticacao, testes, scripts, CI/deploy e documentacao progressivamente. Seguir dependencias reais, sem ler dados/segredos por curiosidade.
2. Mapear capacidades e donos: modulos existentes, limites, entradas, regra/dado pertencente, dependencias, quem usa/quem e usado. Modulo nao e sinonimo de tabela ou pagina.
3. Classificar CONFORME, PARCIAL, AUSENTE com necessidade comprovada, NAO_DESCOBERTO ou NAO_SE_APLICA. Separar problema funcional, estrutura, documentacao, seguranca, visual e operacao.
4. Consultar [destinos e nomes](../../references/ARQUITETURA.md) e [documentacao minima](../../references/DOCUMENTACAO.md). Reutilizar o equivalente correto; quando faltar, escolher o fallback sem fazer o responsavel inventar nomes/pastas. Nenhuma arvore padrao inteira e criada por rotina.
5. Apresentar DE/PARA: manter, reorganizar, criar, aposentar; motivo, dono, consumidores, arquivos/docs/IDs, riscos e verificacoes. Estrutura/regras/visual materialmente alterados pedem proposta e aprovacao com `romulo-especificar` e `romulo-interface` quando aplicavel. Registro no destino canonico existente, nao PLANO.md.
6. Com alcance aprovado, executar via `romulo-construir`, `romulo-documentacao` e seguranca pertinente; gate de `romulo-analisar` vale para cada novo destino. Mover nao significa duplicar nem perder historico/IDs.
7. Verificar fluxo/consumidores, imports/autoload/rotas, referencias, testes e documentacao apos cada lote coerente. Reaplicar o procedimento nao recria arquivos nem duplica modulos.

Se nao houver sumario, criar somente a entrada minima e os mapas necessarios ao recorte autorizado. Se nao houver AGENTS/CLAUDE, seguir `romulo-iniciar-projeto`; para existentes, migracao preserva peculiaridades e exige as autorizacoes locais. Descobrir antes de inicializar.

Auditoria nao autoriza automaticamente commit, push, deploy, acesso ao banco, mudanca destrutiva ou desativacao de guardas. Dependencia desconhecida bloqueia retirada daquele item. Nenhum modulo e separado apenas para corresponder a um nome de pasta.
