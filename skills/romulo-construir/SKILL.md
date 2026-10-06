---
name: romulo-construir
description: Use para implementar funcionalidades, corrigir bugs ou alterar codigo dentro do Romulo Dev Standard, depois de romulo-analisar e antes de romulo-verificar.
---

# Romulo Construir

Construa o menor lote coerente que cumpra integralmente o pedido.

Fluxo: pedido/decisao -> impacto -> implementacao -> documentacao canonica atingida -> verificacao.

Preserve a arquitetura real. Quando o projeto usa separacao equivalente, respeite responsabilidades de interface/entrada, normalizacao, regra/autorizacao, persistencia/contrato e integridade de banco. Nao crie camada vazia apenas para satisfazer nomes.

Reutilize antes de criar. Arquivo novo exige responsabilidade nova ou separacao tecnicamente necessaria e consumidor real. Nao fabrique CRUD completo, dashboard, configuracao, exportacao ou abstracao para o futuro.

Bug: reproduzir/evidenciar -> localizar menor cadeia responsavel -> corrigir causa -> repetir cenario -> verificar dependencia direta.

Frontend apresenta; servidor decide efeitos oficiais; banco protege invariantes. Nao confie em campo do cliente para empresa, permissao, preco, saldo, estoque ou propriedade.

Nao misture refatoracao conveniente com o alcance pedido. Nao reverta trabalho alheio.

Aplique romulo-seguranca quando houver superficie de seguranca e romulo-documentacao quando o conhecimento canonico mudar. Termine com romulo-verificar.
