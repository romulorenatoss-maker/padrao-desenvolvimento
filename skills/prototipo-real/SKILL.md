---
name: prototipo-real
description: Use na revisao visual iterativa de prototipos e quando uma interface, fluxo ou regra aprovada for convertida, integrada, publicada ou comparada com o real.
---

# Prototipo para Real

Prototipo especifica a mudanca aprovada; nao comprova backend, persistencia, seguranca ou publicacao.

Desde a criacao, aplicar a [divisao JavaScript por responsabilidade](../../references/ARQUITETURA.md#javascript-por-responsabilidade-e-tamanho) e a [identificacao interna por DNA](../../references/DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo). Usar fontes e interfaces reutilizaveis no real; manter simulacao separada e substituir somente o adaptador/contrato necessario na conversao autorizada, preservando IDs e interface. Isso reduz reescrita, sem fingir backend pronto nem importar dados ficticios.

## Ambiente padrao e limites

Pedido direto de interface/acao sem ambiente expresso usa PROTOTIPO por padrao; nao perguntar "prototipo ou real?" por rotina. Respeitar ambiente explicitamente indicado. "Faca no real" aciona a construcao real e suas salvaguardas, nao publicacao; "publique" exige destino e autorizacao proprios. Proposta/analise sem ordem de executar segue `especificar`.

Prototipo deve ser isolado e reversivel, sem banco/dados/rotas de producao nem push que dispare deploy. Sem ambiente seguro existente, declarar o bloqueio concreto; nao escrever no real, criar infraestrutura ou inventar isolamento por conveniencia. Executar somente partes independentes e autorizadas. Protecoes especificas, inclusive 0393 e acesso, continuam exigidas.

## Leitura proporcional e documento reutilizavel

Prototipo visual/comportamental com simulacao isolada consulta somente o DNA e seu documento dono, regras/conexoes do recorte e briefing/componentes pertinentes. Nao cria banco, API real nem executa checks de implantacao por rotina; preserva modularidade, separacao de dados e guardas locais. Dados reais, credenciais, acesso ou integracao reais exigem a consulta de seguranca pertinente antes da operacao, mesmo no prototipo.

Usar o mesmo documento canonico e DNA na conversao: registrar finalidade (para que/por que/para quem), regras, gatilhos/estados, origem/saida, fornecedor/consumidores e contrato real previsto no detalhe do recorte, sem repetir o manual tecnico. Marcar PROTOTIPO/PENDENTE e distinguir decidido, simulado e construido. Na ordem de construir no real, completar somente lacunas tecnicas indispensaveis, substituir adaptadores simulados pelos contratos autorizados e validar a cadeia atingida; nao inventar backend pronto nem recriar a especificacao.

## Revisao rapida do prototipo e documentacao paralela

No trabalho iterativo definido como prototipo, manter o contexto e as correcoes na conversa coordenadora e na fila persistente do projeto. Encaminhar ao construtor pedidos curtos e fieis, com alvo e resultado esperado, sem ampliar pedido visual para construcao real. Investigar somente a cadeia atingida e executar a alteracao ja autorizada sem repetir autorizacao de construcao; a confirmacao visual posterior do resultado continua obrigatoria.

Pedido direto claro segue `especificar`: informar entendimento curto e construir na mesma execucao no ambiente seguro definido acima, sem parar na explicacao. Previa de imagem somente quando solicitada ou quando ha decisao visual indispensavel, conforme `interface` secao 4. Depois de construir/testar, mostrar a tela renderizada na mesma aba visivel apos cada entrega. Conferir que a fonte alterada foi realmente carregada; editar arquivo, abrir URL ou enviar mensagem nao comprova atualizacao visual. Preservar edicoes nao salvas; segunda aba somente se o responsavel pedir. Sem acesso visual, declarar o limite e preservar a pendencia.

Aplicar a [fila de construcao e confirmacao visual obrigatoria](../interface/SKILL.md#6-fila-de-construcao-e-confirmacao-visual-obrigatoria): screenshot real por local/estado afetado, uma tela/modal por vez, pergunta especifica e confirmacao explicita da revisao mostrada. Sem resposta, o item permanece AGUARDANDO_CONFIRMACAO_VISUAL; novo pedido ou mudanca de assunto nao autorizam documentar a versao como aprovada. Depois do aceite, salvar a decisao no dono e conduzir ao proximo item, sem esperar que o responsavel procure as outras telas. Registrar proposta, trabalho tecnico e pendencia nao equivale a aprovar regra. A pergunta generica "Posso documentar assim?" nao substitui o aceite visual especifico.

Com documentacao autorizada e delegacao disponivel, outro agente aplica `documentacao` aos destinos canonicos existentes enquanto o construtor continua. Entregar ao documentador o recorte/revisao mostrada, decisoes, arquivos e evidencias; separar propriedade dos arquivos para evitar sobrescrita e conferir a correspondencia antes de salvar o lote. Documentador nao acrescenta regras nem altera codigo sem autorizacao. Quando o responsavel autorizar tambem revisao e correcao, pode testar e corrigir desvios do pedido no recorte entregue, apos combinar propriedade dos arquivos; seguir o ciclo de testes de `verificar`. Correcao que mude o resultado mostrado reabre o aceite afetado. Sem delegacao disponivel ou autorizada, concluir a documentacao no mesmo agente sem prometer paralelismo.

Documentar ou aprovar o prototipo nao autoriza construir, integrar ou publicar no real. Exigir pedido explicito para essa conversao. Novo pedido nao cancela trabalho anterior em execucao quando o responsavel mandou aguardar sua conclusao.

Issue e PR seguem `construir`, sem atrasar a entrega visual local por check externo opcional. Registrar alcance PROTOTIPO e fechar somente o que esse alcance entrega; tarefa de conversao real permanece aberta ate seu proprio aceite. Vincular DNA/issue/PR no dono, sem mapa paralelo. Publicar a skill ou atualizar plugin nao autoriza alterar interfaces de todos os projetos; adocao e incremental, preservando o lote em curso.

## Fonte unica ativa da tela local

Cada tela existente tem uma unica fonte ativa no prototipo local. Claude, Codex e outros executores editam os mesmos arquivos atuais da tela, seguindo a [pasta compartilhada de construir](../construir/SKILL.md#pasta-compartilhada-entre-ias). Alterar a tela significa editar essa implementacao; nao montar uma segunda tela por cima, esconder a antiga ou manter uma versao alternativa concorrente. Tela nova somente com pedido explicito do responsavel.

Registrar no documento dono existente a rota canonica, seus aliases/acessos locais, a view, JS e CSS ativos e o mecanismo que os serve. Todos os acessos locais daquela tela no mesmo ambiente de prototipo carregam essa mesma fonte. Uma fonte preservada em `docs/prototipo/<modulo>/fontes/` precisa estar ligada ao carregamento do prototipo; guardar ali sem o servidor a usar nao entrega a alteracao. Nao misturar a view antiga com assets de outra revisao. Copia gerada e cache nao sao fontes editaveis concorrentes: reutilizar o mecanismo existente para regenerar copias e invalidar caches a partir da fonte ativa ou servir essa fonte diretamente, sem voltar silenciosamente a uma versao antiga.

A ultima alteracao autorizada da implementacao deve ser salva imediatamente nos arquivos da fonte ativa, independentemente de commit, push ou fechamento da sessao. A proxima carga local e a reabertura apos queda/reinicio devem usar essa ultima fonte salva; nunca retomar silenciosamente uma implementacao anterior. Se a fonte atual estiver indisponivel, informar o impedimento em vez de servir uma copia antiga sem aviso. Commit preserva historico; nao ativa a tela. Preservar trabalho alheio e propriedade dos arquivos. Salvar codigo nao autoriza gravar campos de formulario ou mutacoes de negocio ainda nao confirmados pelo usuario; preservar essas edicoes sem recarregar a aba para cumprir um check.

Fonte local salva pode ser candidata em revisao: registrar separadamente a ultima revisao aprovada e o estado da candidata, sem promover pendencias a regra vigente. Confirmacao atualiza o mesmo dono/DNA da tela/modal e substitui somente o trecho aprovado; historico e contexto antigo nao sao fontes concorrentes. Ao iniciar nova prototipacao de capacidade ja convertida, partir exclusivamente do real atual conferido, documentando o novo delta no mesmo dono; nunca recuperar prototipo descartado. Desfazer/restaurar exige ordem explicita, analise do impacto e nova confirmacao visual.

Dados de exemplo e alteracoes confirmadas no prototipo devem usar o mecanismo persistente existente, isolado dos dados oficiais e dos outros ambientes/escopos pertinentes. Inicializar exemplos somente quando ainda ausentes; abrir, fechar, recarregar ou reiniciar o servico/sessao nao pode zerar, recriar nem repor valores anteriores sobre o estado confirmado. Reset, descarte ou substituicao de exemplos exige ordem explicita no alcance correspondente. Se o mecanismo existente nao preservar esse estado, corrigir a persistencia no recorte autorizado antes de declarar preservacao; nao criar banco ou armazenamento paralelo por rotina.

Antes de entregar ou passar para outra IA, ensaiar no ambiente autorizado: salvar a implementacao e confirmar uma alteracao de exemplo -> recarregar -> reiniciar o servico local -> reabrir a tela; conferir em cada etapa que a implementacao atual e os exemplos confirmados permanecem. Preservar edicoes nao confirmadas antes do ensaio e nao usar dados oficiais. Conferir rota/aliases, origem da view/assets e renderizacao conforme a revisao visual acima. Para arquivo/asset servido sem transformacao, comparar os bytes ou hash da fonte salva com a resposta carregada; quando houver transformacao/renderizacao, conferir a identidade da revisao/fontes e o resultado servido. HTTP 200, arquivo editado ou screenshot isolado nao comprova essa correspondencia nem persistencia. Divergencia exige corrigir o carregamento/persistencia e retestar o atingido; etapa indisponivel fica NAO_EXECUTADO com motivo concreto, sem declarar preservacao comprovada.

Conferir tambem autoload, dependencias PHP e contratos da cadeia que renderiza a fonte ativa. Uma copia-base obsoleta deve ser reconciliada com o codigo ja existente/autorizado, sem exigir novo commit ou deploy apenas para ativar trabalho local e sem sobrescrever WIP. Conferir a presenca da dependencia no clone e na revisao usada pela copia antes de afirmar que falta implementar ou publicar.

Adocao em projeto existente: reconciliar a fonte e os acessos da tela atingida, retirar do carregamento as versoes concorrentes e atualizar seus vinculos no dono, apos conferir consumidores. Nao apagar dados, historico ou referencias validas. Esta regra nao promove o prototipo ao real nem exige que ambientes publicados mostrem trabalho local nao publicado; a conversao continua exigindo a autorizacao abaixo.

## Prototipo nunca publica
Pedido de prototipo altera somente a copia local do prototipo. Nao editar arquivo que o real usa (codigo publicado, migracao, dado oficial) e nao fazer commit/push que dispare deploy (ex.: branch com deploy automatico) antes da ordem explicita do responsavel "construir no real". Para nao perder trabalho, salvar as fontes alteradas do prototipo em `docs/prototipo/<modulo>/fontes/`, no mesmo caminho relativo do arquivo real (copia fiel, que mantem o identificador do original); commit/push seguem a selecao de alteracoes aprovadas de `construir`. Finalidade unica dessa pasta: guardar o prototipo sem publicar; o real nunca le dela. Registrar cada copia no sumario de prototipo do modulo. Na ordem de construir, levar a copia aprovada ao arquivo real e apagar a copia e o registro no mesmo lote. A guarda local de arvore documental deve aceitar esse destino. Protótipo deve parecer igual em qualquer aparelho: letra carregada pela pagina (nao a do sistema) e alertas de trabalho conforme o contrato aprovado, respeitando reducao de movimento sem perder a informacao/atencao; seguir `interface` e nao alterar alertas existentes automaticamente. Na ordem de construir, levar o aprovado ao real, testar e so entao publicar. Ambiente omitido segue o padrao acima; perguntar antes da escrita somente se houver contradicao concreta ou destino indispensavel nao identificavel.

Antes da conversao identifique: finalidade, usuario/tarefa, gatilho, campos/origem, validacoes, estados, contrato, autorizacao/escopo, efeitos/consumidores, erros/recuperacao, aceite e impacto pertinentes.

Conferir no [documento dono](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao) a revisao/fontes aprovadas, DNAs e regras de cada item do recorte, simulacoes e contratos reais correspondentes. Documentacao ausente indispensavel e completada antes da implementacao dependente, sem repetir entrevista resolvida ou copiar regra para um novo dossie. Preservar a entrega visual rapida e a documentacao paralela autorizada; pendencia documental fica no registro existente ate o fechamento, nao equivale a backend pronto.

Compare somente a cadeia atingida. Preserve interface e regras aprovadas. Troque simulacoes pelos contratos reais necessarios. Nao redesenhe durante a integracao sem aprovacao.

Direcao dos dados: real -> prototipo, nunca prototipo -> real. Nao transporte contas, usuarios, lancamentos, anexos, IDs, valores de exemplo, fixtures, localStorage/sessionStorage ou banco de prototipo para producao.

Na versao real, sem cadastro real autorizado, mostre estado vazio. Nao invente fallback ficticio.

Mantenha como PENDENTE/NAO_VERIFICADO tudo que nao foi construido, testado ou publicado. Codigo local pronto nao significa producao ativa.

Antes de marcar REAL, retire fontes ficticias da cadeia publicada, teste o backend pertinente e confirme a separacao de dados.

Dados no prototipo e na conversao seguem [prototipo x real nos dados](../../references/DADOS.md#prototipo-x-real-nos-dados): simulacao com os metodos previstos da persistencia e modelo registrado no dono; migration e persistencia real somente na ordem de construir.

## Complementos
Quando o usuario pedir proposta visual no chat, seguir a previa em imagem de `interface`; construir o prototipo interativo somente quando solicitado, reutilizando a proposta aprovada. Pedido direto de simulacao/interacao respeita esse alcance e executa no prototipo; previa explicitamente solicitada e ainda nao aprovada permanece uma decisao pendente. Divergencia da proposta aprovada exige nova aprovacao antes de editar.

Campo so vem preenchido no real quando o valor foi efetivamente registrado e continua valido e autorizado; nunca selecionar opcao automaticamente. Verificar o cenario sem cadastro e confirmar que nenhum dado do prototipo foi gravado no banco oficial.

Opcao ficticia encontrada no real exige rastrear e corrigir a origem; nao autoriza apagar cadastros legitimos ou historico.

Nao apagar proposta aprovada pendente porque outra parte foi publicada.

## Especificacao e visual na conversao
Aplicar `especificar` para confrontar a revisao aprovada e as conexoes reais; nao reabrir decisoes ja respondidas. Aplicar `interface` para preservar referencia e peculiaridades. Prototipo aprovado nao autoriza novas telas, botoes ou regras durante a conversao. Mostrar o resultado real de cada local alterado pela fila de confirmacao visual; aprovacao do prototipo nao comprova nem aprova automaticamente a implementacao real ainda nao apresentada.

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
