---
name: especificar
description: Use antes de criar ou alterar capacidade, tela, aba, campo, botao, navegacao, regra ou integracao. Diferencie pedido direto de proposta; execute o pedido claro no prototipo e pergunte somente decisoes indispensaveis, preservando a confirmacao visual posterior. Em correcao fiel ao contrato, use a verificacao curta sem repetir entrevista.
---

# Especificar

Fonte dona da especificacao e da utilidade de cada elemento. Use depois de `analisar`; padrao visual pertence a `interface`, implementacao a `construir` e aceite a `verificar`. Nao duplica essas regras.

## Pedido direto ou proposta

Pedido imperativo, claro e executavel para criar, adicionar, mudar, corrigir ou alterar ja autoriza construir no alcance pedido. Informar entendimento em uma a tres linhas e prosseguir na mesma execucao: investigar, registrar, construir, testar e apresentar para confirmacao posterior; nunca encerrar em "entendi", "vou fazer" ou "posso construir?". A selecao de ambiente pertence a [prototipo-real](../prototipo-real/SKILL.md#ambiente-padrao-e-limites).

Pedido de ideias, sugestao, analise, planejamento ou "como ficaria?" sem ordem de executar recebe somente proposta. Decisao indispensavel ausente/contraditoria bloqueia apenas a parte dependente; perguntar essa decisao, nao repetir autorizacao do que ja esta definido. Ordem direta nao autoriza locais adicionais, alteracao alheia, dado oficial, permissao ou deploy.

## 1. Identificar a tarefa antes de desenhar

Reformule: quem executa qual tarefa, em qual contexto, para obter qual resultado. Nao substituir silenciosamente a solucao pedida por outra: explicar a equivalencia e obter aprovacao quando mudar a experiencia.

Leia primeiro a documentacao canonica, decisoes aprovadas, tela, componentes, rotas, contratos, regras e consumidores do recorte. Siga as dependencias encontradas. Nao invente comportamento porque um modulo tem um nome familiar; capacidade usada numa tela continua pertencendo ao modulo dono da regra.

Para projeto/capacidade nova, confrontar briefing visual, fluxo do app e TRD do projeto com o recorte conforme [contratos de projeto](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao). Descobrir quais telas/cliques/transicoes levam ao resultado e quais modulos/contratos/dados o sustentam; perguntar somente decisoes ausentes. Atualizar seus donos aprovados quando houver mudanca real, sem duplicar TELA.md nem refazer os tres contratos em cada bug. Reconstrucao fiel preserva o contrato de origem; diferenca solicitada e tratada como evolucao, sem presumir redesenho.

Procedimento obrigatorio antes da proposta: inspecionar a tela pedida no navegador quando disponivel e rastrear cada elemento atingido: eventos/gatilhos, modais, actions, services, contratos, dados, regras de disponibilidade e consumidores noutras telas/aparelhos, inclusive prototipo e real conforme o alvo. Conferir a finalidade original e os pedidos anteriores nas fontes canonicas e, se necessario, no historico Git; a ultima decisao autorizada prevalece. Identificar o que sera adicionado, alterado, movido, removido ou preservado e por que, incluindo consequencias nas regras ligadas ao recorte. A investigacao e profunda; a apresentacao e curta, no formato de `interface` secao 6. Elo inacessivel ou nao comprovado deve ser declarado, sem inventar conclusao.

Diferencie contrato aprovado de implementacao atual. Codigo existente evidencia comportamento, nao necessariamente aprovacao. Divergencia entre codigo, documento e decisao exige reconciliacao; nao documentar o bug como nova regra.

### Entender a finalidade e o impacto antes de mudar

Interpretar a fala do responsavel no contexto das decisoes vigentes: identificar o problema que ele quer resolver, para que o elemento foi criado e qual regra precisa continuar. Remover um botao, mover uma aba e encerrar a capacidade sao pedidos distintos; nao presumir que tirar da tela autoriza interromper dados ou consumidores.

Consultar primeiro sumario/mapa -> documento da pagina e aba -> regra/contrato dono -> paginas consumidoras -> codigo e dados pertinentes. Confrontar documentacao com comportamento atual e procurar tambem consumidores nao registrados pelos IDs, chamadas e contratos. Documento parcial/desatualizado nao permite afirmar impacto completo.

Antes de mudanca que rompa comportamento ou conexao, apresentar de forma curta: o que deixa de existir, quem recebe/devolve essa informacao, o efeito em cada local e onde a funcao continuara. Pedir somente a decisao ausente e aguardar antes da parte dependente; decisao explicitamente aprovada nao exige nova autorizacao de construcao. Alteracao visual sem romper contrato segue o fluxo curto autorizado e a confirmacao obrigatoria do resultado.

Quando faltar explicacao, investigar antes de perguntar. Se a intencao continuar desconhecida, perguntar de modo dirigido: "Para que este item serve e quem precisa da informacao dele?"; usar as respostas para completar o documento dono. Nao transformar uma deducao do codigo em intencao atribuida ao responsavel nem entrevistar novamente o que ja esta definido. O formato e a manutencao deste conhecimento pertencem a `documentacao`.

Antes de propor pagina/capacidade/conexao nova, buscar obrigatoriamente ideias, decisoes e vinculos futuros ja registrados sobre as entidades envolvidas: sumarios, documento dono, regras/contratos e assuntos do prototipo, pelos IDs existentes e nomes/termos pertinentes. Se houver proposta anterior, apresenta-la primeiro: "Voce havia explicado X para Y; esta registrado em Z como previsto/aprovado/construido. Este pedido acrescenta ou muda o que?". Usar as palavras/ideia comprovadas e citar a fonte; sugestao da IA nao vira pedido/aprovacao humana. Nao reconstruir a proposta do zero nem obrigar o usuario a repetir o que ja respondeu.

Essa recuperacao usa a especificacao vigente e ideias futuras ainda validas, nao versoes substituidas/sugestoes descartadas. Chat/historico pode esclarecer lacuna real, mas nao reativa decisao superada nem se torna dependencia permanente: reconciliar o conhecimento confirmado no documento dono conforme `documentacao`.

Antes de recuperar conversa antiga, conferir a [marcacao do contexto consolidado](../../references/DOCUMENTACAO.md#marcacao-do-contexto-consolidado) do recorte: SIM usa documento vigente e referencias; sem SIM permite conciliacao com contexto/historico temporario. Nova fala do responsavel pode incrementar ou substituir a decisao documentada com o impacto pertinente, sem reabrir o passado por iniciativa propria.

Conduzir o detalhamento de forma progressiva, uma questao indispensavel por vez quando o responsavel adotar entrevista pausada. Incorporar respostas novas preservando detalhes anteriores ainda validos e reavaliar impactos nos demais locais conectados. Decisao nova substitui somente o trecho que efetivamente mudou; conflito ausente nao cria nova autorizacao do mesmo escopo. Vagas lembrancas ou busca sem resultado nao permitem alegar que a ideia nunca existiu.

## 2. Checklist interno antes de perguntar

Para cada tema, marque RESOLVIDO_PELO_PEDIDO, RESOLVIDO_PELO_SISTEMA, PRECISA_DECISAO ou NAO_SE_APLICA. Registre a fonte/justificativa no destino canonico quando necessario. Sem acesso: NAO_DESCOBERTO, nao ausencia comprovada.

| Tema | O que descobrir |
|---|---|
| Objetivo | Usuario, tarefa, contexto de uso, resultado e limites do pedido. |
| Entrada e continuidade | Menu/rota/tela/aba de origem, proxima etapa, retorno e preservacao de contexto. |
| Responsabilidade | Modulo dono, capacidade existente, equivalentes reutilizaveis e o que fica intocado. |
| Regras | Decisoes vigentes, estados/transicoes permitidas, calculos/unidades e efeitos entre modulos. |
| Informacao | Campos indispensaveis, origem oficial, editavel/calculado/exibido/filtro/temporario e destino aplicavel. |
| Acoes | Tarefa atendida, condicao de disponibilidade, permissao, efeito observavel e recuperacao. |
| Integracao | Contratos reais, quem le/escreve, persistencia e consumidores afetados. |
| Visual | Referencia aprovada, componentes/tokens existentes, responsividade e peculiaridades protegidas. |
| Aceite | Cenarios observaveis de sucesso, falha, acesso, persistencia e efeitos pertinentes. |

Pergunte ao responsavel somente decisoes ausentes ou conflitantes que afetem a solucao. Agrupe perguntas em uma rodada curta, com recomendacao e consequencia das alternativas quando util. Em revisao iterativa, seguir a fila de `interface` secao 6: autorizar a construcao no alcance definido, apresentar uma tela/modal por vez e manter pendencia ate confirmacao explicita do resultado. A aprovacao de proposta nao substitui esse aceite posterior; silencio e novo pedido nao aprovam. Nao perguntar nome de arquivo, endpoint ou tamanho ja definido no projeto. Nao repetir resposta conhecida. Limites de acesso se resolvem por investigacao/autorizacao, nao pedindo que o usuario invente fatos tecnicos.

## 3. Proposta quando solicitada ou indispensavel

Quando o pedido for de proposta ou houver decisao indispensavel ainda ausente, apresentar somente o recorte/delta que exige escolha e aguardar essa resposta. Pedido direto claro segue a execucao imediata acima, inclusive para nova capacidade no prototipo: nao exigir aprovacao do entendimento antes de construir. Pedido ja acompanhado de proposta aprovada reutiliza essa revisao.

Na proposta, apresentar na linguagem da operacao, seguindo os titulos, mapa e confirmacao definidos em `interface` secao 6; na execucao direta, manter somente o entendimento curto e continuar. Mostrar somente o recorte afetado pelo pedido.

Nomeie telas, abas/subabas quando necessarias, entrada, finalidade de cada parte, campos, botoes e resultado de cada acao; informe estados, acesso, navegacao posterior, visual de referencia, impactos e aceite pertinentes ao recorte. Nao invente nomes de rotas, APIs, tabelas ou permissoes como se existissem: separar COMPROVADO, PROPOSTO e A_LOCALIZAR. Antes da implementacao dependente, localizar o elo ou aprovar a capacidade ausente no dono correto.

Decisao de composicao: tela para tarefa com identidade/fluxo proprio; aba para contexto da mesma entidade; modal/drawer para acao curta contextual; ampliar/reutilizar quando a responsabilidade e compativel. Nao usar porcentagem arbitraria nem forcar toda tarefa em modal.

Para criar/alterar a identidade visual, apresente referencia renderizada/prototipo do recorte com `interface` antes de propagar a mudanca. Aprovar a proposta funcional nao aprova automaticamente um visual ainda nao mostrado. Prototipo visual aprovado nao comprova integracao real.

Proposta de capacidade reutiliza primeiro dados e contratos compativeis, conforme DADOS. Nao perguntar ao responsavel qual tabela usar quando isso pode ser descoberto. Perguntar somente decisoes semanticas ausentes: mesma identidade ou papel distinto, finalidade, preservacao historica, retencao e destino de vinculos. Pedido claro continua executando no prototipo; dependencia adicional fora do alcance e apresentada nominalmente antes da escrita. Fonte: [reutilizacao e propriedade](../../references/DADOS.md#reutilizacao-e-propriedade-de-dados).

## 4. Contrato de utilidade de botoes e elementos

Toda acao criada ou alterada deve responder:
- qual requisito/decisao ou necessidade indispensavel ao fluxo a justifica;
- quem a utiliza, em qual contexto e pre-condicao;
- qual verbo/rotulo descreve o resultado observavel;
- qual comportamento local, navegacao, consulta ou mutacao executa;
- qual componente padrao, regra/contrato e evidencia a sustentam.

Pedido de remover botao: localizar suas copias e entradas alternativas, quem ainda chama sua funcao e qual regra motivou sua existencia. Informar se a capacidade termina ou continua em local nominal identificado. Se termina, retirar no alcance autorizado botao, gatilhos e codigo/registros exclusivos sem consumidor, incluindo mapas e prototipo atingidos; se continua, preservar somente os consumidores validos e atualizar suas ligacoes. Nao deixar botao oculto, handler orfao ou regra substituida ativa, nem apagar funcao compartilhada ainda necessaria. Reconciliar os testes existentes conforme o comportamento decidido.

Cancelar, voltar, fechar, tentar novamente e recursos de acessibilidade podem ser necessarios ao fluxo aprovado sem pedido individual. Justifique a necessidade; nao use isso para adicionar capacidades de negocio.

SEM_TAREFA_COMPROVADA: nao entra na proposta nem na implementacao nova. Proibido criar exportar, dashboard, cards de indicadores, filtros, CRUD completo, configuracoes ou atalhos somente por costume, simetria ou para preencher espaco. Elemento existente aparentemente inutil: investigar e propor remocao, nunca apagar sem alcance autorizado.

Revisao bidirecional: todo requisito aprovado tem solucao; todo elemento proposto tem razao. Um botao tecnicamente conectado pode continuar sem utilidade e deve ser corrigido na proposta. Nao esconder acao essencial num menu para parecer minimalista. Priorize a tarefa principal por contexto sem impor quantidade universal de botoes.

## 5. Escopo, aprovacao e mudancas

Informe CRIAR, ALTERAR, REUTILIZAR e PRESERVAR no registro existente, sem arquivo de plano paralelo. Associe proposta/revisao, fonte da aprovacao e criterios de aceite ao mapa/assunto canonico; atualize com `documentacao`.

Bug que apenas restaura contrato aprovado, texto ou ajuste visual que retorna ao padrao: consulta curta + informar diferenca + corrigir no alcance autorizado, sem entrevista nem redesenho. Nova regra/tarefa ou alteracao de peculiaridade expressamente pedida segue o mesmo alcance direto; delta nao decidido ou efeito adicional exige a decisao especifica antes da parte dependente. Em ambos os casos, efeito de UI exige apresentar e confirmar a implementacao conforme `interface` secao 6.

Acrescimo/edicao pontual segue `interface` secao 4: executar o pedido direto no prototipo, preservando o restante aprovado e resolvendo somente efeitos adicionais nao autorizados. O pedido funcional nao autoriza esse efeito colateral; nao alterar primeiro para mostrar depois. Se o existente permanece intacto, nao repetir autorizacao de construcao ja dada. Locais adicionais devem ser nominalmente autorizados e incluidos na fila; mudanca de ideia resolve expressamente o destino dos locais antigos ainda nao decidido.

Uma duvida bloqueia somente a parte dependente; nao construir essa parte por suposicao. Autorizacao de desenho, codigo, banco, concessao de permissao, commit/push e deploy continuam distintas conforme contrato local. Nao aumentar o escopo para resolver conveniencia tecnica.

## 6. Handoff e cenarios de aceite do metodo

A construcao recebe o pedido direto autorizado ou a proposta aprovada e seus vinculos; nao inventa decisoes ausentes nem exige aceite previo do candidato. Conferir novamente se surgiram mudancas concorrentes nas fontes antes de escrever. Na entrega, confrontar proposta e resultado com `verificar`.

Cenarios obrigatorios ao revisar esta skill (avaliacao de comportamento, nao teste automatico de IA):
- "Financeiro no cliente": localizar dono e contratos; propor integracao, nao criar financeiro paralelo.
- "Corrigir salvar": rastrear e restaurar a cadeia aprovada, nao perguntar novamente quais abas o sistema tem.
- "Criar tela nova": localizar referencia/escopo -> resolver so lacuna indispensavel -> construir no prototipo -> apresentar e confirmar cada item, sem segunda autorizacao de inicio.
- "Adicionar exportar porque cabe no cabecalho": recusar essa inclusao especulativa, sem remover requisitos legitimos.
- "Reaplicar padrao": preservar peculiaridade aprovada e consultar antes de muda-la.

Na revisao iterativa de prototipo, seguir o fluxo de entrega visual e autorizacao documental de [prototipo-real](../prototipo-real/SKILL.md#revisao-rapida-do-prototipo-e-documentacao-paralela), subordinado ao aceite explicito por item de `interface` secao 6. Essa aprovacao nao equivale a construcao/publicacao real.

## Conexoes funcionais no alcance autorizado

Aplicar a pergunta nominal para conectar outra tela/modulo somente quando houver efeito adicional nao autorizado. Diferenciar evidencia e hipotese; detalhes tecnicos indispensaveis dentro do pedido nao exigem nova autorizacao. Pedido direto continua construindo imediatamente no prototipo, sem pedir para comecar. Fonte dona: [conexoes funcionais e rastreabilidade bidirecional](../../references/DOCUMENTACAO.md#conexoes-funcionais-e-rastreabilidade-bidirecional), incluindo estados, auditoria seletiva e cenarios de aceite; nao duplicar esse esquema aqui.
