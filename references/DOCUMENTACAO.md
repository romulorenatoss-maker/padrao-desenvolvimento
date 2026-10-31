# Documentacao — destinos e criacao minima

A skill dona e `documentacao`. Descobrir destinos canonicos antes de criar. Preservar nomes/IDs/vinculos corretos; fallback so quando nao existir equivalente. Sumario aponta, documento dono explica; nao copiar narrativa em cada consumidor.

## Fallback para projeto sem documentacao adequada
| Necessidade real | Destino padrao | Conteudo minimo |
|---|---|---|
| Entrada geral | `docs/SUMARIO.md` | Finalidade/stack em resumo, modulos reais e links para donos; sem catalogo de skills central. |
| Entrada do modulo | `docs/modulos/<modulo>/SUMARIO.md` | Capacidades, telas, dados, contratos e consumidores existentes; somente links que resolvem. |
| Briefing visual | `docs/architecture/BRIEFING_DESIGN.md` | Decisoes visuais aprovadas e referencias aos tokens/componentes; consultar antes de criar/alterar UI. |
| Fluxo do app | `docs/architecture/FLUXO_APP.md` | Jornadas entre telas, cliques e transicoes; regra detalhada continua no documento dono. |
| TRD | `docs/architecture/TRD.md` | Composicao tecnica aprovada, limites, contratos, dados, ambiente e entrega; nao substitui mapas do modulo. |
| Motivo/limites de modulo | `docs/modulos/<modulo>/PORQUE.md` | Quando a justificativa/relacoes excederem o sumario: dono, limites, USA/USADO_POR, decisoes. Nao criar texto vazio. |
| Reconstrucao | `docs/modulos/<modulo>/RECONSTRUCAO.md` | Criar quando necessaria reproducao/reconstrucao: ordem, dependencias, configuracao e verificacao sem segredos. |
| Tela/aba | `docs/modulos/<modulo>/telas/<tela>.md` | Documento dono por pagina; reutilizar `telas/<tela>/TELA.md` quando essa convencao ja existir. Tarefa, rota/menu, abas, elementos/DNA, finalidade, origem/consumidores, regras/contratos, estados, peculiaridades e aceite. Resumo em duas linhas por comportamento e detalhes necessarios por referencia. Agrupar abas relacionadas. |
| Cadeia funcional | `docs/modulos/<modulo>/cadeias/<capacidade>.md` | Entrada -> regra/autorizacao -> contrato/dado -> efeito/consumidores -> erros/testes. |
| Dados/contrato/acesso | `dados/<entidade>.md`, `contratos/<contrato>.md`, `seguranca/<capacidade>.md` no modulo | Somente quando houver responsabilidade distinta; caso pequeno cabe no mapa da capacidade. |
| Processo transversal local | `docs/architecture/processos/<processo>.md` | Guardas, autorizações ou procedimento ESPECIFICOS ao projeto; nao copiar diretrizes centrais. |
| Historico de lote | `docs/changes/ALTERACOES.md` | Obrigatorio em toda entrega publicada, no mesmo commit: QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER (`construir`); sem certificado paralelo; respeitar o limite local de entradas e preservar as antigas no Git. |
| Inventario | `docs/architecture/INVENTARIO.jsonl` | Apenas quando instrumento local o exigir/consumir; nao criar cadastro manual universal por rotina. |

Todos os subdiretorios sao relativos ao modulo real; criar somente com documento util. Projeto com convencao equivalente nao recebe copia desta arvore. Documento por responsabilidade, nao por arquivo, funcao, botao, elemento decorativo ou execucao.

## Contratos de projeto e reconstrucao

Reutilizar fontes equivalentes e vincula-las no sumario; um documento existente pode ter secoes para estas responsabilidades. Nao impor tres arquivos vazios, repetir TELA.md nem escrever um manual novo por bug. Registrar decisoes suficientes ao recorte antes da primeira interface definitiva; completar os mesmos donos conforme as respostas. O metodo vale para pessoas e IAs, sem substituir responsabilidades e instrumentos locais.

- Briefing visual: cores semanticas, fontes/tamanhos/pesos, botoes e estados, cantos, espacamentos/densidade, variantes por tarefa, responsividade e acessibilidade. Valores aprovados ou referencia concreta aos tokens/componentes implementados; excecoes nominais e origem da aprovacao. Referencia renderizada acompanha a decisao. Padrao novo nao autoriza mudar a tela aprovada por iniciativa propria.
- Fluxo do app: tarefa/usuario -> entrada -> telas/cliques -> resultado e retorno; condicoes, estados de sucesso/erro/vazio/acesso e efeitos pertinentes. Referenciar DNAs, paginas e contratos donos, sem copiar campos/regras em todas as jornadas.
- TRD: stack e versoes permitidas, modulos/donos, dependencias e contratos, persistencia/RPCs, seguranca, operacao/entrega e o que fica fora do alcance. Vincular guias tecnicos existentes; configuracoes por nome/finalidade, nunca segredos ou dados privados. Proposta tecnica nao vira implementacao comprovada.

O briefing visual tem uma fonte dona por projeto: reutilizar documento equivalente; na falta, `docs/architecture/BRIEFING_DESIGN.md`, ligado ao sumario. Uma colecao externa chamada DESIGN.md e referencia de proposta, nao segunda fonte da verdade. Tela/aba referencia o briefing e descreve apenas sua composicao/peculiaridade local; o padrao de entrevista e comparacao pertence a interface.

Para cada decisao visual, registrar somente o vigente: escopo/usuario/tarefa; estado PROPOSTO ou APROVADO e fonte da decisao; referencia visual/revisao; cores com papeis e valores; fonte/tamanhos/pesos; botoes e estados; cantos/espacamentos/densidade; responsividade/movimento; tokens/componentes consumidores; excecoes protegidas e limites de aplicacao. Resumo curto e valores suficientes para outra pessoa/IA reproduzir a escolha. DNAs existentes ligam elementos funcionais e telas; nao criar identidade por cor, pixel ou decoracao.

Antes da primeira UI definitiva, resolver as decisoes indispensaveis e mostrar a referencia representativa. Em projeto existente inconsistente, inventariar somente o alcance pedido e distinguir conforme, desvio, peculiaridade aprovada e nao verificado; novo briefing nao certifica migracao de todas as telas. Converter prototipo ao real conserva esse mesmo dono/referencia e atualiza os vinculos de implementacao, sem repetir entrevista ou criar manual paralelo.

Guia modular de reconstrucao referencia o codigo/assets na revisao exata e os donos abaixo. O minimo e permitir que outra pessoa/IA localize e reproduza a cadeia sem depender da conversa; duas frases resumem a finalidade, nao limitam os contratos tecnicos.

| Peca | O que precisa ser localizavel e conferido |
|---|---|
| Modulo/capacidade | DNA existente, finalidade, dono, limites, fontes/simbolos, entradas/rotas/jobs e consumidores. |
| Contrato/API/RPC | Identidade nominal, fornecedor e consumidores, entrada/saida/unidades, condicoes, efeitos, recusas e erros. RPC inclui schema/nome/assinatura completa, migration/definicao dona, quem chama e controles de execucao/tenant/permissao aplicaveis; nao basta citar seu nome. |
| Dados e acesso | Schema/migrations na ordem, constraints, funcoes/triggers/RLS/policies pertinentes, permissao/auditoria e vinculos com o contrato; dados reais e secrets nao acompanham a copia. |
| Interface | Referencia aprovada, rota, arquivos/partials/assets, tokens, elementos/acoes/estados e peculiaridades; telas apontam ao briefing e suas regras donas. |
| Ambiente e entrega | Versoes/dependencias efetivamente usadas, nomes de configuracao segura, ordem de instalacao/migrations/integracao, comandos reais, artefato/revisao, verificacao e recuperacao compativel com dados. |
| Aceite e lacunas | Testes/fixtures controlados, cenarios/cadeias pertinentes, evidencias e limites; distinguir PROTOTIPO, REAL, PREVISTO e dependencia externa nao exercitada. |

Ao converter prototipo, o documento dono liga a revisao/fontes mostradas aos DNAs e regras aprovadas, com simulacoes, contrato real a substituir cada uma e o que ainda falta. Registrar comportamento de botoes, gatilhos, tempos, modos, unidades, disponibilidade, estados e regras de entrada/saida pertinentes. Contrato ainda inexistente e PROPOSTO/A_LOCALIZAR, nao API pronta nem autorizacao de criar banco. A entrevista nao e repetida se a decisao ja esta descrita. Fluxo de entrega/fechamento pertence a `prototipo-real`.

Metadados nominais de codigo/RPC/consumidores ficam nos mapas/inventario que o projeto ja exige; geracao/conferencia usa instrumentos existentes quando disponiveis. Nao manter copias manuais concorrentes. Regra de negocio/finalidade aprovada precisa de descricao humana no dono; geracao de nomes nao a substitui. Sem instrumento comprovado, conferir o recorte e declarar o limite, nunca alegar rastreio completo por existir um DNA.

### Contrato documentado de propriedade e reutilizacao

No documento dono existente, registrar: significado/granularidade; ID/DNA; dono logico; destinos fisicos; chave/escopo; cardinalidade; fonte canonica; derivados/snapshots; contratos de leitura/escrita; consumidores reais e em construcao; decisao REUTILIZAR/ESTENDER/VINCULAR/SEPARAR/PRESERVAR_SNAPSHOT/CRIAR_COM_JUSTIFICATIVA; regras de equivalencia; acesso/finalidades; ciclo de vida e efeitos da retirada; estrategia de integridade/concorrencia; testes; revisao e estado da evidencia.

Indice aponta ao dono; consumidores registram somente seu uso e link reverso. Nao copiar a regra inteira para cada tela, modulo ou agente. Nao transformar mapa documental em tabela de runtime que registre cada leitura.

Diferenciar PROPOSTO, CONFIRMADO_NO_REPO, CONFIRMADO_NO_BANCO e CONFIRMADO_NO_RUNTIME. Identificar contagem exata versus estimada, escopo e momento. Vazia ou sem grep nao certifica desuso.

Unificacao inclui mapa nominal DE/PARA, IDs e consumidores migrados; regra descartada sai da especificacao ativa, preservando historico. Regra em Markdown nao comprova constraint instalada nem exclusao segura executada.

Modelo enxuto no dono do projeto, preenchido apenas com fatos e propostas claramente marcadas:

```text
ENTIDADE / DNA:
SIGNIFICADO E GRANULARIDADE:
DONO CANONICO / CONTRATO:
IDENTIDADE, EMPRESA E CARDINALIDADE:
FONTES FISICAS COMPROVADAS:
QUEM LE / GRAVA / SOLICITA EXCLUSAO:
DERIVADOS / SNAPSHOTS / INVALIDACAO:
DECISAO DE REAPROVEITAMENTO E MOTIVO:
RETIRAR VINCULO / REGISTRO / MODULO:
RETENCAO / INTEGRIDADE / CONCORRENCIA:
DE-PARA / ROLLBACK:
EVIDENCIAS E LIMITES POR AMBIENTE:
```

## Identificacao e documentacao interna do codigo

Codigo escrito a mao identifica arquivo, modulo dono, finalidade curta e documento canonico existente no cabecalho. Reutilizar metadados/convenções exigidos pelo projeto; na falta deles, usar `ARQUIVO_ID: arquivo:<caminho relativo>`, `MODULO_DONO: <modulo>`, `FINALIDADE: <uma frase>` e `DOCUMENTO_CANONICO: <caminho/ancora que resolve>`. Nao escrever placeholders como se fossem cadastro pronto, nem repetir a especificacao de negocio no cabecalho.

DNA fica imediatamente junto da unidade funcional que identifica (funcao, acao, handler ou entrada publica), nao apenas no topo do arquivo. Usar `DNA_ID` e a identidade estavel do mapa dono; auxiliares usam `DNA_AUX` quando a convencao local exigir. Exemplo ilustrativo de marcador: `/* DNA_ID: producao.transferencia.liberar::js.confirmarTransferencia */`. O mapa/dono define a identidade antes de introduzi-la; nao fabricar DNA para cada linha, variavel ou elemento decorativo, nem reduzir a granularidade nominal ja exigida pelo projeto.

Extracao conserva o DNA da mesma capacidade, atualiza caminho/simbolo nos mapas e aponta consumidores ao novo destino; nao trocar ID por renomear arquivo nem duplicar identidade entre implementacoes concorrentes. Copias aprovadas de prototipo seguem o contrato de prototipo-real e distinguem plano/revisao sem virar outra capacidade. Remocao confere finalidade, chamadores estaticos/dinamicos, assets, contratos, testes e documentos antes de retirar referencias exclusivas. DNA ajuda localizar, mas nao prova desuso sozinho.

Documentacao interna de entrada publica/contrato nao obvio descreve finalidade, parametros/tipos/unidades, retorno ou Promise, erros e efeitos relevantes; usar JSDoc ou convencao equivalente existente sem instalar gerador. Comentario explica decisao, restricao ou cuidado que o codigo nao mostra. Nao comentar cada linha nem repetir nomes obvios; regra detalhada, aprovacao e conexoes vivem no documento dono. Sem segredo/dado privado nos exemplos. Limites, nomes e separacao pertencem a [arquitetura JavaScript](ARQUITETURA.md#javascript-por-responsabilidade-e-tamanho).

## Manutencao e limpeza do conhecimento vigente

Atualizar o mesmo item/DNA e os consumidores comprovadamente afetados no mesmo lote. Resumo curto permite achar a decisao; detalhes validos, excecoes, exemplos e conexoes permanecem no dono. Decisao substituida sai da especificacao ativa; nao narrar tentativas descartadas nem transferir texto obsoleto para notas paralelas. Ideia futura ainda valida permanece PREVISTO no dono atual, sem criar pagina/API/DNA ficticio; ao surgir pedido relacionado, recuperar essa ideia conforme `especificar`.

Retirar duplicacao somente depois de conferir dono, equivalencia, referencias e preservacao historica exigida. Registros tecnicos obrigatorios, pendencias reais e vinculos nominais nao sao descartados por tamanho. Recibos antigos ja preservados no Git podem sair da leitura corrente somente quando o contrato/instrumento local permite e suas referencias foram reconciliadas; nao apagar manifests usados por guardas nem esconder falta de construcao/teste. Mudanca interna sem conhecimento novo nao exige narrativa artificial, salvo registro local obrigatorio.

No fechamento, requisito/DNA -> dono -> fonte/contrato/RPC/dado -> consumidores/testes, e inverso, deve concordar no alcance. O fiscal independente confere o candidato exato e a limpeza prevista; nao aceita somente a declaracao de que o executor seguiu o manual. Conferencia documental nao certifica funcao, pixels ou deploy; `verificar` define a evidencia por efeito. Uma regra escrita nao instala nem substitui uma guarda executavel.

O executor documenta ao alterar, sem esperar o fiscal. Quando houver registro temporario do lote, reutilizar o instrumento existente: caminhos/simbolos alterados, DNAs e donos documentais, estado da conciliacao e pendencias; nao copiar regras para ele. O fiscal confronta esse registro com o diff real, inclusive omissoes e consumidores atingidos, aponta divergencias ao executor e reconfere a correcao. So altera documentacao com autorizacao e propriedade dos caminhos; seu delta recebe revisao independente. Ao encerrar, retirar o temporario pelo fluxo autorizado, depois dos checks/recibos exigidos; preservar evidencia no dono/Git. Em interrupcao ou falha, manter o aberto para retomar. Manifest usado pela guarda e recibo obrigatorio seguem seu ciclo local, sem apagamento antecipado ou certificado paralelo.

## Como escrever o documento da pagina (TELA.md ou equivalente)

Cabecalho minimo: identidade documental e dono existentes; nome/finalidade da pagina; rota, menu/submenu; estado PROTOTIPO/REAL e revisao das fontes. Agrupar abas/subabas e configuracoes no mesmo documento quando pertencem a essa pagina. Indicar os arquivos que a renderizam/interagem e as cadeias/contratos donos, sem listar arquivos sem relacao.

Descrever a decisao vigente por completo: o leitor deve compreender a pagina mesmo que a conversa original seja apagada. Fonte/data de aprovacao podem identificar proveniencia, mas um link ao chat nao substitui o conteudo aprovado. Revisao nova substitui a descricao superada no mesmo item e reconcilia referencias; nao manter duas regras concorrentes nem arquivo de propostas descartadas. Preservar historico tecnico obrigatorio e ideias futuras validas conforme `documentacao`.

### Marcacao do contexto consolidado

Usar no cabecalho do TELA.md/documento equivalente `CONTEXTO_CONSOLIDADO: SIM` somente apos reconciliar finalidade, decisoes vigentes, detalhes e conexoes daquele recorte e salva-los no dono. No documento inteiro, SIM exige cobrir todas as paginas/abas que ele declara; quando apenas uma aba/recorte esta consolidado, colocar o marcador na secao nominal correspondente. Ausencia ou `CONTEXTO_CONSOLIDADO: NAO` significa conciliacao ainda nao concluida. Nao marcar automaticamente porque existe arquivo ou para fazer uma guarda passar.

Concluiu essa conciliacao, quem a executou deve gravar SIM imediatamente no MESMO lote, antes de encerrar a tarefa ou commitar a entrega; nao deixar "falta marcar consolidado" para outra IA nem exigir novo pedido/aprovacao so para aplicar o marcador factual. Retirar a pendencia documental desse recorte dos registros existentes, preservando duvidas realmente abertas e pendencias de construcao/teste/publicacao. Com parte ainda incompleta, marcar somente a secao efetivamente concluida, sem promover a pagina inteira.

No recorte marcado SIM, consultar o documento vigente e donos referenciados; nao recuperar conversas antigas para reinterpretar/reativar decisoes dele. Pedido novo do responsavel e acrescentado/corrigido no mesmo dono, com impacto e autorizacao aplicaveis. Se faltar detalhe indispensavel, registrar a lacuna e perguntar conforme o fluxo adotado, sem preencher por regra antiga superada. Codigo/contratos continuam sendo conferidos para implementar e validar.

No recorte sem SIM, pode consultar contexto do chat e historico disponivel como apoio temporario, confrontando com documentacao existente, codigo e decisoes posteriores. Conciliar conflitos, salvar somente contexto vigente no dono e entao marcar o recorte. Em tarefas entre telas marcadas e nao marcadas, aplicar esse criterio a cada uma; nao migrar todo o sistema por essa regra.

Essa marcacao identifica consolidacao do conhecimento, nao aceite visual, funcao construida/testada/publicada nem autorizacao de mudar layout; `STATUS_DOCUMENTACAO` e estados de implementacao/verificacao continuam independentes. E metadado do documento, nao novo indicador/botao na interface.

Para cada item funcional, usar uma secao ancorada ao identificador ja existente. O nome visivel sozinho nao identifica o item: informar pagina, aba, modal/etapa e posicao quando relevante. Referenciar `DNA_ID`/`DNA_AUX` da capacidade e `ELEMENTO_ID`/`COMPONENTE_ID` quando existentes; nao inventar DNA por elemento decorativo nem trocar IDs para caber no modelo. Um comportamento compartilhado conserva sua identidade e ganha referencias nos consumidores.

Formato de cada item, preenchido somente com fatos/decisoes identificados:

```text
<ID existente> — <nome funcional/visivel>
LOCAL: <rota/pagina > aba/subaba > modal/etapa > item>
RESUMO (ate duas frases curtas):
1. <para que serve e por que existe>
2. <para quem serve: usuario e/ou capacidade consumidora>
REGRA DONA: <link + ancora do contrato/componente; regra local fica aqui>
CONEXOES: <DNA | recebe de/fornece a/compartilha | dono/ancora | o que usa e por que | efeito de mudar/remover>
DETALHE: <regra particular, condicoes/estados/excecoes; arquivos/simbolos, action/contrato/dados pertinentes>
DECISAO/EVIDENCIA: <fonte da finalidade/aprovacao; revisao, verificacao e limites>
RASTREABILIDADE (quando existente): <repositorio, links de issue/PR e commit da entrega>
```

O bloco e um modelo de escrita, nao um formulario a repetir vazio: omitir campos NAO_SE_APLICA, integrar secoes/tabelas equivalentes existentes e tornar desconhecidos relevantes explicitos. Nao publicar placeholders como documentacao pronta. Mostrar condicoes exatas quando alteram comportamento; duas linhas resumem, nao substituem detalhes necessarios. As mesmas regras nao sao copiadas para cada item: usar link ao dono e registrar somente a aplicacao particular na pagina.

Uma tela/arquivo pode reunir varios DNAs: cada comportamento conserva sua identidade e resumo; agrupar o que tiver a mesma responsabilidade, sem misturar regras independentes. Contrato/componente compartilhado tem uma unica definicao dona e os consumidores existentes identificados pelos seus DNAs, documentos e pelo que usam. Nas telas consumidoras, registrar somente a aplicacao local e o link de volta; dois IDs no mesmo arquivo nao comprovam dependencia. Reutilizar mapa/tabela de consumidores existente, sem manter outra lista concorrente.

O detalhe funcional/tecnico fica na pagina solicitada e referencia o contrato dono. Origem explica o que fornece e por que; consumidor explica para que usa. Exemplo ilustrativo: Estoque fornece identidade/disponibilidade do ativo; Construtor usa esse vinculo para habilitar a maquina e aponta para o contrato de entrada/saida. Cada lado guarda somente sua responsabilidade. Antes de editar/remover contrato compartilhado, conferir ambos os sentidos e as chamadas reais, mostrar quais consumidores perdem/mudam informacao e preservar continuidade ou obter a decisao exigida para a ruptura. Ausencia de vinculo documentado nao prova ausencia de consumidor.

Intencoes futuras ainda sem pagina ficam em PREVISTO no dono atual/assunto do prototipo, com descricao rica suficiente para retomar e vinculo no sumario existente. Nao criar documento vazio da pagina futura. Ao surgir pedido relacionado, consultar e apresentar essa ideia antes de propor outra; manter exemplos/excecoes pertinentes nos detalhes e distinguir pedido humano de sugestao e de implementacao comprovada. Atualizar o mesmo item ao receber novas explicacoes, conforme `documentacao`.

Ao receber uma decisao, atualizar o item correspondente pelo ID. Ao mover, preservar identidade e ajustar LOCAL/rotas e links. Ao remover/alterar capacidade, conferir e atualizar os itens consumidores comprovadamente afetados, dizendo o novo destino e como a informacao continua (ou que interrupcao foi explicitamente aprovada). Mudanca apenas de aparencia nao presume alterar contrato. A manutencao e consulta seguem `documentacao` e `especificar`; nenhum documento passa a permitir uma regra de negocio nova por si.

## Rastreabilidade DNA, issue, PR e commit

No item/secao do documento dono, associar os IDs existentes aos links completos de issue e PR do repositorio correto e ao commit conferido. DNA identifica a capacidade/elemento estavel; issue identifica tarefa; PR identifica entrega. Nunca substituir/sufixar o DNA com o numero GitHub, inventar identificador para preencher campo ou usar numero solto sem repositorio. Uma issue/PR pode atingir varios DNAs e um DNA pode ter varias entregas; nao exigir correspondencia um-para-um.

Reutilizar campo/tabela/registro de lote existente. Se precisar de formato, usar uma linha curta por entrega: `DNA existente | owner/repo#issue (link) | owner/repo#PR (link) | commit conferido`. Antes de a PR/commit existirem, omitir o campo ou indicar ainda nao criado no registro de trabalho; nao prever numeros/SHA. Issue e PR tambem apontam para os DNAs e documentos pertinentes. O mapa/sumario atual aponta ao dono; nao criar arquivo de mapa paralelo, cadastro universal ou copia manual em cada consumidor.

Consulta rapida: mapa/DNA -> decisao vigente no dono -> issue/PR/commit quando a tarefa/evidencia exigir -> codigo/consumidores atingidos. Ticket antigo nao reativa regra superada e PR/issue fechada nao comprova deploy ou funcionamento. Manter conhecimento vigente completo no TELA.md/equivalente; o Git e o GitHub preservam historia de entregas, sem acumular alternativas antigas no item ativo. Vinculos dos consumidores continuam bidirecionais e sem especificacao duplicada.

Metodo comum fica no padrao central; AGENTS local guarda ponte e protecoes, nao copia lista de ferramentas/regras. No processo/PROJETO.md ou equivalente existente, registrar somente o perfil concreto: ferramenta e finalidade, versao/revisao, comando/check, ambiente, alcance e estado CONFIGURADO/VERIFICADO/PREVISTO/NAO_SE_APLICA. Marcar opcional e motivo quando pertinente; nunca registrar segredo ou alegar instalacao por citar o nome. Nao criar arquivo vazio so para repetir o perfil.

## Enxugar AGENTS/CLAUDE existentes sem perder regras
Classificar cada trecho: identidade/ponte/protecao curta -> AGENTS; metodo global -> referencia central vigente; regra de negocio/guarda/peculiaridade local -> dono documental existente. Destino local faltante usa a tabela acima se a migracao estiver autorizada. Registrar DE/PARA no registro canonico do lote, criar/validar destino e link antes de retirar texto da origem.

Protecao nao desaparece nem e enfraquecida por mudanca de lugar. Link de protecao deve ser leitura obrigatoria antes da escrita, inclusive por outros agentes. Se qualquer destino estiver indefinido, sem acesso ou ainda nao validado, preservar o trecho original. Nao substituir AGENTS protegido sem autorizacao especifica; mover seu conteudo tambem e alteracao. CLAUDE.md novo e ponte, nao copia de regras.

Proibidos como atalhos: PLANO.md, FINAL.md, V2.md, notas de agente, resumo/memoria paralela e backups documentais. Excecao nao prevista so pelo gate `0393`, sem contornar proibicao local explicita. Historico fica no Git; o estado atual necessario fica no dono canonico.

## Conexoes funcionais e rastreabilidade bidirecional

Fonte dona do mapa de ligacoes; atualizar a cadeia/documento existente do projeto, sem arquivo YAML, indice universal, banco ou skill nova por campo. Aplicar sob demanda a campos, acoes, status, modais, eventos, calculos e contratos novos/alterados. Pedido direto claro continua executavel imediatamente no prototipo no local solicitado; analise/proposta sem ordem nao escreve codigo; REAL expresso nao presume deploy.

Rastrear pedido/regra -> capacidade/DNA -> entradas -> processamento/contrato -> saidas -> consumidores -> testes -> aprovacao, e o percurso inverso do consumidor ate a decisao aprovada. Investigar finalidade, origem, entrada, modulo dono, destino, quem usa, reflexos de editar/excluir/cancelar/recalcular, prova e autorizacao. Buscar sinonimos e simbolos tecnicos em eventos, handlers, rotas, imports, DTOs, queries, tabelas, jobs e chamadas dinamicas; ampliar o recorte conforme evidencias. Busca literal vazia nao comprova ausencia.

| Classificacao da ligacao | Tratamento |
|---|---|
| COMPROVADA | Fonte e consumidor localizados no codigo/contrato; reutilizar e testar. A referencia sozinha nao prova funcionamento. |
| EXIGIDA_PELO_PEDIDO | Necessaria dentro do local autorizado; implementar e testar no mesmo pedido, sem nova autorizacao de detalhe tecnico interno. |
| INFERIDA_A_CONFIRMAR | Hipotese plausivel, nao fato nem autorizacao; explicar evidencia/motivo e perguntar antes de alterar outro local. |
| EXISTENTE_NAO_VERIFICADA | Referencia existe, funcionamento ainda nao demonstrado; executar verificacao. |
| INEXISTENTE | Ausencia limitada ao alcance inspecionado; propor somente se pertinente, sem inventar contrato. |
| FORA_DO_ESCOPO | Consumidor conhecido e nao autorizado; preservar e registrar impacto/pendencia. |
| DESCARTADA | Rejeitada explicitamente; nao ressuscitar via historico ou memoria. |

Mapa compacto no dono: ID/DNA estavel; objetivo/regra; fonte da decisao e autorizacao; ambiente e revisao candidata; entrada; fornecedor do dado/calculo e contrato real; saida; consumidores nominais com caminho/ID/DNA, contrato, classificacao e estado; prova executada e aceite por local. Contrato nao encontrado e A_LOCALIZAR, nunca nome ficticio de API. Origem descreve o que fornece; consumidor referencia o que usa. Atualizar ou invalidar os vinculos quando fonte, contrato ou revisao mudar; nao duplicar a especificacao em cada tela.

Pergunta nominal para efeito adicional: "Voce pediu [X] em [A]. Identifiquei [B/contrato C] que [usa ou pode precisar do resultado], porque [evidencia ou hipotese]. Deseja conectar tambem em [B]? O que ja esta aprovado sera preservado." Nao esperar o responsavel descobrir sozinho a ligacao. Agrupar impactos reais e priorizar decisoes, sem entrevistas genericas nem alterar primeiro para perguntar depois. Dependencia tecnica interna indispensavel ao pedido nao e novo local de negocio; se um contrato compartilhado atingir inevitavelmente consumidor nao autorizado, bloquear somente esse trecho, sem copiar a regra para contornar a decisao.

Exemplo ilustrativo: frete em Pedidos exige investigar total, cotacao, endereco, financeiro, entrega/documentos, cancelamento e relatorios; sao candidatos, nao destinos obrigatorios universais. Diferenciar frete cobrado do cliente, custo de transportadora e previsao. Se o contrato do total ja consome o campo, verificar a ligacao; outra tela nao autorizada fica pendente. Novo desconto pede conferir total/pedido/financeiro; novo cancelamento pede conferir detalhe, edicao, notificacoes e relatorios pertinentes. Nenhum exemplo afirma contratos de um projeto real.

### Prova e estados por ligacao

Comprovar interface/evento, calculo/condicoes/recusas, persistencia aplicavel, efeito no consumidor, reflexos de atualizacao/cancelamento e regressao do nao autorizado. PROTOTIPO mostra simulacao isolada com dados de teste; REAL exige contratos/persistencia exercitados no ambiente autorizado. Screenshot nao prova contrato, banco ou acesso. NAO_EXECUTADO exige motivo e mantem o elo pendente.

Estados separados: UI_CONSTRUIDA (nao afirma integracao), CADEIA_PROTO_CONECTADA (simulacao executada), REAL_CONECTADO (contratos/dados reais exercitados), CONSUMIDOR_PENDENTE_DE_AUTORIZACAO, CONEXAO_NAO_VERIFICADA, AGUARDANDO_CONFIRMACAO_VISUAL e CAPACIDADE_APROVADA. Esta ultima exige todas as ligacoes obrigatorias do alcance aprovado implementadas, testadas e aceitas no ambiente correspondente. Botao sem acao, contrato sem chamada, chamada sem efeito e integracao so descrita nao passam. Nao marcar REAL com mocks, fixtures ou localStorage. Entregar parte independente como "trecho local construido; integracao pendente"; nao esconder utilidade nem afirmar completude. Preservar a fila e screenshot real/aceite individual de interface; aprovar uma tela nao aprova as demais. Cinco alteracoes so contam para salvamento quando integralmente aprovadas, conforme construir.

### Auditoria seletiva de capacidades orfas

Somente no modulo/capacidade indicado: partir da rota/elemento/DNA e rastrear origem e destino. Classificar ATIVA_E_CONECTADA, PARCIAL, SEM_CONSUMIDOR_COMPROVADO, REFERENCIA_OBSOLETA, INFERIDA_A_CONFIRMAR ou NAO_VERIFICADA. Mostrar antes, ligacao proposta/destino, motivo, risco e teste. Perguntar por locais adicionais, registrar a resposta na fila e executar apenas o autorizado. Nao apagar automaticamente unidade aparentemente orfa nem migrar consumidores por esta regra; chamadas dinamicas podem existir. Correcao exige teste do ciclo e aceite dos locais afetados.

### Cenarios de aceitacao da regra

Matriz para avaliacao, nao recibo de execucao comportamental de IA. Testes de texto/links verificam distribuicao; navegador, comportamento e ativacao de plugin/sessao exigem evidencias proprias. Quando indisponiveis, registrar NAO_EXECUTADO e motivo.

| Caso | Cenario e resultado exigido |
|---|---|
| C01 | Frete em Pedidos: descobrir fornecedor e consumidores, nao concluir pelo campo. |
| C02 | Total ja consome frete: executar fluxo e conferir exibicao. |
| C03 | Financeiro candidato: perguntar antes de alterar a tela. |
| C04 | Financeiro nao autorizado: manter pendencia sem bloquear Pedidos independente. |
| C05 | Financeiro autorizado: conectar, testar e apresentar para aceite proprio. |
| C06 | Custo logistico e cobranca distintos: nao misturar sem decisao. |
| C07 | Adicione X: entendimento de ate tres linhas e construcao imediata no prototipo. |
| C08 | So analise X: nao escrever codigo. |
| C09 | Real expresso: respeitar ambiente/controles, sem deploy presumido. |
| C10 | Botao sem acao: reprovar conclusao funcional. |
| C11 | Contrato sem chamada: registrar ligacao faltante. |
| C12 | Chamada sem efeito: falha, nunca PASSOU. |
| C13 | Consumidor dinamico: busca vazia nao autoriza ausencia/remocao. |
| C14 | Componente compartilhado: mapear consumidores e obter escopo adicional. |
| C15 | Outra tela aprovada: preservar; nova revisao somente se afetada. |
| C16 | Tres locais autorizados: tres provas visuais e aceites separados. |
| C17 | Sem screenshot/navegador: nao inventar prova, manter aceite pendente. |
| C18 | Mudanca de local: decidir manter ou remover o anterior conforme interface. |
| C19 | Conversao real: reinspecionar contratos, dados e consumidores. |
| C20 | Regra descartada: nao usar historico como fonte ativa. |
| C21 | Orfa aparente: auditoria seletiva, sem remocao ou alteracao automatica. |
| C22 | Cinco aprovados: commit/push do lote aprovado, sem segredo ou deploy de prototipo. |
| C23 | Consulta contextual: IDs/referencias do recorte, sem carregar projeto inteiro. |
| C24 | Inferencia: explicar hipotese, nao registrar como comprovada. |
