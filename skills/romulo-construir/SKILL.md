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

## Modulos, limites e remocao
Modulo novo so nasce quando a responsabilidade foi aprovada e nao pertence a modulo existente; criar somente arquivos usados pela primeira capacidade. Nao acessar tabela interna de outro modulo para contornar seu contrato. Nao copiar modulo para criar outro.

Limpeza separa:
- temporario/gerado reproduzivel: remover somente em destino descartavel, sem fonte unica nem trabalho pendente;
- codigo/doc aparentemente orfao: buscar caminho, nome, ID, simbolo, rota, imports, chamadas, menu, jobs, contratos, testes, assets e referencias dinamicas; classificar ATIVO, COMPARTILHADO, HISTORICO, COMPATIBILIDADE, GERADO/TEMPORARIO, CANDIDATO_A_REMOCAO ou FINALIDADE_NAO_COMPROVADA (este ultimo nao autoriza apagar);
- dados persistentes: nunca apagar por limpeza de codigo.

Remocao autorizada reconcilia no mesmo lote os vinculos afetados: codigo, rota/menu, consumidores, contrato, permissao exclusiva, docs, inventario e testes. Historico fica no Git; nao criar copias `old`, `backup` ou `v2`.

Nao abrir auditoria global nem refatorar modulo inteiro para corrigir defeito local conhecido.

## Entrada obrigatoria e construcao conectada
Antes de criar/alterar, consultar `romulo-especificar` e a revisao aprovada aplicavel; efeito de interface chama `romulo-interface`. Correcao fiel ao contrato usa o caminho curto dessas skills, nao dispensa leitura. Nao construir funcionalidade enquanto falta aprovacao exigida.

Cada elemento novo/alterado precisa da tarefa e do efeito definidos no contrato de utilidade. Nao fabricar botoes, abas, campos ou funcoes para parecer completo. Preserve requisito aprovado: remover/esconder um botao necessario nao corrige sua implementacao.

Implemente uma capacidade vertical coerente: entrada/navegacao -> tela/acao -> contrato -> regra/autorizacao -> persistencia quando aplicavel -> resposta -> estado/consumidores -> teste e documentacao. Essas sao responsabilidades, nao obrigacao de criar arquivo/camada para cada seta.

Classifique a acao: LOCAL, NAVEGACAO, CONSULTA ou MUTACAO. Fechar modal/trocar aba nao exige API; mutacao oficial nao pode ser fingida no estado local. Campo pode ser persistido, calculado, exibido, filtro ou temporario; nao inventar coluna para todo input.

Localize contratos/dados/consumidores reais antes de conectar. Capacidade ausente nasce no dono correto com necessidade aprovada, nao como modulo paralelo. Reutilize componentes/validacao/controle de acesso e preserve compatibilidade dos consumidores.

Sucesso persistente so apos confirmacao oficial; resultado incerto por falha de rede exige reconciliacao antes de repetir mutacao critica. Defina queries/dados/consumidores a atualizar, inclusive outras sessoes quando a regra exigir. Invalidacao de cache nao garante sincronizacao universal. Planeje erro, timeout, recuperacao, repeticao/concorrencia e estados pertinentes com `romulo-seguranca`.

Execute integracao real em ambiente autorizado com dados de teste controlados. Nao usar operacao real de cliente em producao para demonstracao. Fixture isolada de teste nao e fallback de producao.

## Ciclo de correcao ate o aceite
Construir -> executar -> observar -> corrigir a causa -> repetir verificacao e dependencias atingidas. Defeito tecnico corrigivel no alcance nao vira entrega encerrada apenas como pendencia. Se uma tentativa nao resolver, mudar diagnostico a partir das evidencias; nao repetir a mesma tentativa nem ampliar escopo silenciosamente.

Parar a parte dependente somente diante de decisao de negocio ausente, autorizacao especifica, risco fora do alcance ou recurso externo indispensavel indisponivel. Informar impedimento concreto, tentativas e o que falta; nao prometer execucao futura nem inventar sucesso. Concluir exige o aceite pertinente de `romulo-verificar`.
