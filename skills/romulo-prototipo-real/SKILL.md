---
name: romulo-prototipo-real
description: Use na revisao visual iterativa de prototipos e quando uma interface, fluxo ou regra aprovada for convertida, integrada, publicada ou comparada com o real.
---

# Romulo Prototipo para Real

Prototipo especifica a mudanca aprovada; nao comprova backend, persistencia, seguranca ou publicacao.

## Revisao rapida do prototipo e documentacao paralela

No trabalho iterativo definido como prototipo, manter o contexto e as correcoes na conversa coordenadora. Encaminhar ao construtor pedidos curtos e fieis, com alvo e resultado esperado, sem ampliar pedido visual para construcao real. Investigar somente a cadeia atingida e executar a alteracao ja autorizada sem repetir aprovacao; perguntar apenas decisao indispensavel ausente.

Aplicar primeiro no ambiente local de prototipo previsto pelo projeto e mostrar a tela renderizada no navegador/painel ao lado apos cada entrega. Conferir que a fonte alterada foi realmente carregada; editar arquivo, abrir URL ou enviar mensagem nao comprova atualizacao visual. Preservar edicoes nao salvas; usar aba separada quando necessario. Sem acesso visual, declarar o limite.

Depois de mostrar a versao, encerrar com a pergunta exata: "Posso documentar assim?". Correcao solicitada entra em seguida e atualiza o entendimento. OK autoriza documentar a versao mostrada. Quando o responsavel tiver explicitamente adotado este fluxo, passar a um novo pedido sem corrigir a entrega mostrada tambem autoriza documentar aquela versao; registrar essa fonte de autorizacao, sem inventar aceite funcional ou publicacao. Silencio sozinho nao autoriza documentar nem cria pendencia.

Com documentacao autorizada e delegacao disponivel, outro agente aplica `romulo-documentacao` aos destinos canonicos existentes enquanto o construtor continua. Entregar ao documentador o recorte/revisao mostrada, decisoes, arquivos e evidencias; separar propriedade dos arquivos para evitar sobrescrita e conferir a correspondencia antes de salvar o lote. Documentador nao altera codigo nem acrescenta regras. Sem delegacao disponivel, concluir a documentacao no mesmo agente sem prometer paralelismo.

Documentar ou aprovar o prototipo nao autoriza construir, integrar ou publicar no real. Exigir pedido explicito para essa conversao. Novo pedido nao cancela trabalho anterior em execucao quando o responsavel mandou aguardar sua conclusao.

## Prototipo nunca publica
Pedido de prototipo altera somente a copia local do prototipo. Nao editar arquivo que o real usa (codigo publicado, migracao, dado oficial) e nao fazer commit/push que dispare deploy (ex.: branch com deploy automatico) antes da ordem explicita do responsavel "construir no real". Para nao perder trabalho, salvar no Git as fontes alteradas do prototipo em `docs/prototipo/<modulo>/fontes/`, no mesmo caminho relativo do arquivo real (copia fiel, que mantem o identificador do original). Finalidade unica dessa pasta: guardar o prototipo sem publicar; o real nunca le dela. Registrar cada copia no sumario de prototipo do modulo. Na ordem de construir, levar a copia aprovada ao arquivo real e apagar a copia e o registro no mesmo lote. A guarda local de arvore documental deve aceitar esse destino. Protótipo deve parecer igual em qualquer aparelho: letra carregada pela pagina (nao a do sistema) e alertas de trabalho animados mesmo com reducao de movimento. Na ordem de construir, levar o aprovado ao real, testar e so entao publicar. Em duvida se o pedido e prototipo ou real, perguntar antes de escrever.

Antes da conversao identifique: finalidade, usuario/tarefa, gatilho, campos/origem, validacoes, estados, contrato, autorizacao/escopo, efeitos/consumidores, erros/recuperacao, aceite e impacto pertinentes.

Compare somente a cadeia atingida. Preserve interface e regras aprovadas. Troque simulacoes pelos contratos reais necessarios. Nao redesenhe durante a integracao sem aprovacao.

Direcao dos dados: real -> prototipo, nunca prototipo -> real. Nao transporte contas, usuarios, lancamentos, anexos, IDs, valores de exemplo, fixtures, localStorage/sessionStorage ou banco de prototipo para producao.

Na versao real, sem cadastro real autorizado, mostre estado vazio. Nao invente fallback ficticio.

Mantenha como PENDENTE/NAO_VERIFICADO tudo que nao foi construido, testado ou publicado. Codigo local pronto nao significa producao ativa.

Antes de marcar REAL, retire fontes ficticias da cadeia publicada, teste o backend pertinente e confirme a separacao de dados.

## Complementos
Quando o usuario pedir exemplo de interface no chat, apresentar prototipo visual interativo e responsivo do recorte (campos, abas, estados e interacoes), nao desenho em texto. Apos aprovacao, implementar fielmente; divergencia exige aprovacao previa.

Campo so vem preenchido no real quando o valor foi efetivamente registrado e continua valido e autorizado; nunca selecionar opcao automaticamente. Verificar o cenario sem cadastro e confirmar que nenhum dado do prototipo foi gravado no banco oficial.

Opcao ficticia encontrada no real exige rastrear e corrigir a origem; nao autoriza apagar cadastros legitimos ou historico.

Nao apagar proposta aprovada pendente porque outra parte foi publicada.

## Especificacao e visual na conversao
Aplicar `romulo-especificar` para confrontar a revisao aprovada e as conexoes reais; nao reabrir decisoes ja respondidas. Aplicar `romulo-interface` para preservar referencia e peculiaridades. Prototipo aprovado nao autoriza novas telas, botoes ou regras durante a conversao.

Falha tecnica corrigivel dentro do alcance segue o ciclo de `romulo-construir`; nao encerrar apenas marcando pendencia. Preservar os estados documentais de publicacao quando depender de autorizacao externa. Verificar a implementacao com `romulo-verificar` antes de declarar integracao real.

## Fechamento da conversao: prototipo x real
Ao publicar o real de uma tela, aba ou modal prototipado:
1. Comparar prototipo x real item por item (abas, modais, botoes, campos, filtros, estados e acoes), com a tela renderizada dos dois lados quando possivel. Dado ficticio nao conta como diferenca.
2. Item do prototipo que nao foi construido vira linha no andamento/fila do projeto como "diferenca prototipo x real a decidir", com o nome do item; nunca e descartado em silencio.
3. Item construido diferente do aprovado: corrigir ou registrar a decisao do responsavel no documento da tela.
4. O documento da tela/modulo passa a descrever so o real: retirar ponteiros ao prototipo (rota, arquivo, "abas aprovadas no prototipo", comparacoes). Fonte historica marcada como removida pode ficar como origem da decisao.
5. Quando nao sobrar item do prototipo por construir ou decidir, apagar os arquivos do prototipo daquela tela e suas referencias no mesmo lote (`romulo-construir`, remocao autorizada e limpeza dos registros de trabalho).
6. A entrada no historico de entregas diz o resultado da comparacao: sem diferenca, ou quais diferencas foram para o andamento.
