---
name: prototipo-real
description: Use na revisao visual iterativa de prototipos e quando uma interface, fluxo ou regra aprovada for convertida, integrada, publicada ou comparada com o real.
---

# Prototipo para Real

Prototipo especifica a mudanca aprovada; nao comprova backend, persistencia, seguranca ou publicacao.

Desde a criacao, aplicar a [divisao JavaScript por responsabilidade](../../references/ARQUITETURA.md#javascript-por-responsabilidade-e-tamanho) e a [identificacao interna por DNA](../../references/DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo). Usar fontes e interfaces reutilizaveis no real; manter simulacao separada e substituir somente o adaptador/contrato necessario na conversao autorizada, preservando IDs e interface. Isso reduz reescrita, sem fingir backend pronto nem importar dados ficticios.

## Leitura proporcional e documento reutilizavel

Prototipo visual/comportamental com simulacao isolada consulta somente o DNA e seu documento dono, regras/conexoes do recorte e briefing/componentes pertinentes. Nao cria banco, API real nem executa checks de implantacao por rotina; preserva modularidade, separacao de dados e guardas locais. Dados reais, credenciais, acesso ou integracao reais exigem a consulta de seguranca pertinente antes da operacao, mesmo no prototipo.

Usar o mesmo documento canonico e DNA na conversao: registrar finalidade (para que/por que/para quem), regras, gatilhos/estados, origem/saida, fornecedor/consumidores e contrato real previsto no detalhe do recorte, sem repetir o manual tecnico. Marcar PROTOTIPO/PENDENTE e distinguir decidido, simulado e construido. Na ordem de construir no real, completar somente lacunas tecnicas indispensaveis, substituir adaptadores simulados pelos contratos autorizados e validar a cadeia atingida; nao inventar backend pronto nem recriar a especificacao.

## Revisao rapida do prototipo e documentacao paralela

No trabalho iterativo definido como prototipo, manter o contexto e as correcoes na conversa coordenadora. Encaminhar ao construtor pedidos curtos e fieis, com alvo e resultado esperado, sem ampliar pedido visual para construcao real. Investigar somente a cadeia atingida e executar a alteracao ja autorizada sem repetir aprovacao; perguntar apenas decisao indispensavel ausente.

Para efeito visual, cumprir primeiro a previa e aprovacao de imagem de `interface`; pedido de melhorar uma lista ou mover um botao ja aciona esse fluxo. Depois da aprovacao ou dispensa explicita, aplicar no ambiente local de prototipo previsto pelo projeto e mostrar a tela renderizada na mesma aba visivel apos cada entrega. Conferir que a fonte alterada foi realmente carregada; editar arquivo, abrir URL ou enviar mensagem nao comprova atualizacao visual. Preservar edicoes nao salvas; segunda aba somente se o responsavel pedir. Sem acesso visual, declarar o limite.

Depois de mostrar a versao, encerrar com a pergunta exata: "Posso documentar assim?". Correcao solicitada entra em seguida e atualiza o entendimento. OK autoriza documentar a versao mostrada. Quando o responsavel tiver explicitamente adotado este fluxo, passar a um novo pedido sem corrigir a entrega mostrada tambem autoriza documentar aquela versao; registrar essa fonte de autorizacao, sem inventar aceite funcional ou publicacao. Silencio sozinho nao autoriza documentar nem cria pendencia.

Com documentacao autorizada e delegacao disponivel, outro agente aplica `documentacao` aos destinos canonicos existentes enquanto o construtor continua. Entregar ao documentador o recorte/revisao mostrada, decisoes, arquivos e evidencias; separar propriedade dos arquivos para evitar sobrescrita e conferir a correspondencia antes de salvar o lote. Documentador nao acrescenta regras nem altera codigo sem autorizacao. Quando o responsavel autorizar tambem revisao e correcao, pode testar e corrigir desvios do pedido no recorte entregue, apos combinar propriedade dos arquivos; seguir o ciclo de testes de `verificar`. Sem delegacao disponivel, concluir a documentacao no mesmo agente sem prometer paralelismo.

Documentar ou aprovar o prototipo nao autoriza construir, integrar ou publicar no real. Exigir pedido explicito para essa conversao. Novo pedido nao cancela trabalho anterior em execucao quando o responsavel mandou aguardar sua conclusao.

Issue e PR seguem `construir`, sem atrasar a entrega visual local por check externo opcional. Registrar alcance PROTOTIPO e fechar somente o que esse alcance entrega; tarefa de conversao real permanece aberta ate seu proprio aceite. Vincular DNA/issue/PR no dono, sem mapa paralelo. Publicar a skill ou atualizar plugin nao autoriza alterar interfaces de todos os projetos; adocao e incremental, preservando o lote em curso.

## Prototipo nunca publica
Pedido de prototipo altera somente a copia local do prototipo. Nao editar arquivo que o real usa (codigo publicado, migracao, dado oficial) e nao fazer commit/push que dispare deploy (ex.: branch com deploy automatico) antes da ordem explicita do responsavel "construir no real". Para nao perder trabalho, salvar no Git as fontes alteradas do prototipo em `docs/prototipo/<modulo>/fontes/`, no mesmo caminho relativo do arquivo real (copia fiel, que mantem o identificador do original). Finalidade unica dessa pasta: guardar o prototipo sem publicar; o real nunca le dela. Registrar cada copia no sumario de prototipo do modulo. Na ordem de construir, levar a copia aprovada ao arquivo real e apagar a copia e o registro no mesmo lote. A guarda local de arvore documental deve aceitar esse destino. Protótipo deve parecer igual em qualquer aparelho: letra carregada pela pagina (nao a do sistema) e alertas de trabalho conforme o contrato aprovado, respeitando reducao de movimento sem perder a informacao/atencao; seguir `interface` e nao alterar alertas existentes automaticamente. Na ordem de construir, levar o aprovado ao real, testar e so entao publicar. Em duvida se o pedido e prototipo ou real, perguntar antes de escrever.

Antes da conversao identifique: finalidade, usuario/tarefa, gatilho, campos/origem, validacoes, estados, contrato, autorizacao/escopo, efeitos/consumidores, erros/recuperacao, aceite e impacto pertinentes.

Conferir no [documento dono](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao) a revisao/fontes aprovadas, DNAs e regras de cada item do recorte, simulacoes e contratos reais correspondentes. Documentacao ausente indispensavel e completada antes da implementacao dependente, sem repetir entrevista resolvida ou copiar regra para um novo dossie. Preservar a entrega visual rapida e a documentacao paralela autorizada; pendencia documental fica no registro existente ate o fechamento, nao equivale a backend pronto.

Compare somente a cadeia atingida. Preserve interface e regras aprovadas. Troque simulacoes pelos contratos reais necessarios. Nao redesenhe durante a integracao sem aprovacao.

Direcao dos dados: real -> prototipo, nunca prototipo -> real. Nao transporte contas, usuarios, lancamentos, anexos, IDs, valores de exemplo, fixtures, localStorage/sessionStorage ou banco de prototipo para producao.

Na versao real, sem cadastro real autorizado, mostre estado vazio. Nao invente fallback ficticio.

Mantenha como PENDENTE/NAO_VERIFICADO tudo que nao foi construido, testado ou publicado. Codigo local pronto nao significa producao ativa.

Antes de marcar REAL, retire fontes ficticias da cadeia publicada, teste o backend pertinente e confirme a separacao de dados.

## Complementos
Quando o usuario pedir proposta visual no chat, seguir a previa em imagem de `interface`; apos aprovacao, construir o prototipo interativo e responsivo do recorte. Pedido explicito de simulacao/interacao respeita esse alcance, sem substituir uma previa de imagem ainda pendente. Divergencia da proposta aprovada exige nova aprovacao antes de editar.

Campo so vem preenchido no real quando o valor foi efetivamente registrado e continua valido e autorizado; nunca selecionar opcao automaticamente. Verificar o cenario sem cadastro e confirmar que nenhum dado do prototipo foi gravado no banco oficial.

Opcao ficticia encontrada no real exige rastrear e corrigir a origem; nao autoriza apagar cadastros legitimos ou historico.

Nao apagar proposta aprovada pendente porque outra parte foi publicada.

## Especificacao e visual na conversao
Aplicar `especificar` para confrontar a revisao aprovada e as conexoes reais; nao reabrir decisoes ja respondidas. Aplicar `interface` para preservar referencia e peculiaridades. Prototipo aprovado nao autoriza novas telas, botoes ou regras durante a conversao.

Falha tecnica corrigivel dentro do alcance segue o ciclo de `construir`; nao encerrar apenas marcando pendencia. Preservar os estados documentais de publicacao quando depender de autorizacao externa. Verificar a implementacao com `verificar` antes de declarar integracao real.

## Fechamento da conversao: prototipo x real
Ao publicar o real de uma tela, aba ou modal prototipado:
1. Comparar prototipo x real item por item (abas, modais, botoes, campos, filtros, estados e acoes), com a tela renderizada dos dois lados quando possivel. Dado ficticio nao conta como diferenca.
2. Item do prototipo que nao foi construido vira linha no andamento/fila do projeto como "diferenca prototipo x real a decidir", com nome/ID e referencia ao detalhe aprovado no dono; nunca e descartado em silencio nem reduzido a um nome sem suas regras/fontes.
3. Item construido diferente do aprovado: corrigir ou registrar a decisao do responsavel no documento da tela.
4. Somente o recorte efetivamente convertido passa a descrever o real: retirar seus ponteiros ativos ao prototipo (rota, arquivo, comparacoes), preservando a origem historica da decisao quando pertinente. Itens ainda nao convertidos permanecem no MESMO documento dono, com detalhes/fontes aprovados e estado PROTOTIPO/PENDENTE explicito; publicar uma aba/modal nao autoriza apagar as demais. Retirar esses detalhes somente apos conversao ou descarte explicitamente autorizado.
5. Quando nao sobrar item do prototipo por construir ou decidir, apagar os arquivos do prototipo daquela tela e suas referencias no mesmo lote (`construir`, remocao autorizada e limpeza dos registros de trabalho).
6. A entrada no historico de entregas diz o resultado da comparacao: sem diferenca, ou quais diferencas foram para o andamento.

O fiscal independente exigido pelo projeto confere esse candidato e a revisao aprovada, nao apenas o texto do recibo. Mudanca posterior invalida a evidencia atingida; revisao/documentacao aprovadas nao substituem execucao real ou prova de versao ativa.
