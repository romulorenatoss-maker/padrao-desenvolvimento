# Documentacao — destinos e criacao minima

A skill dona e `romulo-documentacao`. Descobrir destinos canonicos antes de criar. Preservar nomes/IDs/vinculos corretos; fallback so quando nao existir equivalente. Sumario aponta, documento dono explica; nao copiar narrativa em cada consumidor.

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
| Historico de lote | `docs/changes/ALTERACOES.md` | Obrigatorio em toda entrega publicada, no mesmo commit: QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER (`romulo-construir`); sem certificado paralelo; respeitar o limite local de entradas e preservar as antigas no Git. |
| Inventario | `docs/architecture/INVENTARIO.jsonl` | Apenas quando instrumento local o exigir/consumir; nao criar cadastro manual universal por rotina. |

Todos os subdiretorios sao relativos ao modulo real; criar somente com documento util. Projeto com convencao equivalente nao recebe copia desta arvore. Documento por responsabilidade, nao por arquivo, funcao, botao, elemento decorativo ou execucao.

## Contratos de projeto e reconstrucao

Reutilizar fontes equivalentes e vincula-las no sumario; um documento existente pode ter secoes para estas responsabilidades. Nao impor tres arquivos vazios, repetir TELA.md nem escrever um manual novo por bug. Registrar decisoes suficientes ao recorte antes da primeira interface definitiva; completar os mesmos donos conforme as respostas. O metodo vale para pessoas e IAs, sem substituir responsabilidades e instrumentos locais.

- Briefing visual: cores semanticas, fontes/tamanhos/pesos, botoes e estados, cantos, espacamentos/densidade, variantes por tarefa, responsividade e acessibilidade. Valores aprovados ou referencia concreta aos tokens/componentes implementados; excecoes nominais e origem da aprovacao. Referencia renderizada acompanha a decisao. Padrao novo nao autoriza mudar a tela aprovada por iniciativa propria.
- Fluxo do app: tarefa/usuario -> entrada -> telas/cliques -> resultado e retorno; condicoes, estados de sucesso/erro/vazio/acesso e efeitos pertinentes. Referenciar DNAs, paginas e contratos donos, sem copiar campos/regras em todas as jornadas.
- TRD: stack e versoes permitidas, modulos/donos, dependencias e contratos, persistencia/RPCs, seguranca, operacao/entrega e o que fica fora do alcance. Vincular guias tecnicos existentes; configuracoes por nome/finalidade, nunca segredos ou dados privados. Proposta tecnica nao vira implementacao comprovada.

Guia modular de reconstrucao referencia o codigo/assets na revisao exata e os donos abaixo. O minimo e permitir que outra pessoa/IA localize e reproduza a cadeia sem depender da conversa; duas frases resumem a finalidade, nao limitam os contratos tecnicos.

| Peca | O que precisa ser localizavel e conferido |
|---|---|
| Modulo/capacidade | DNA existente, finalidade, dono, limites, fontes/simbolos, entradas/rotas/jobs e consumidores. |
| Contrato/API/RPC | Identidade nominal, fornecedor e consumidores, entrada/saida/unidades, condicoes, efeitos, recusas e erros. RPC inclui schema/nome/assinatura completa, migration/definicao dona, quem chama e controles de execucao/tenant/permissao aplicaveis; nao basta citar seu nome. |
| Dados e acesso | Schema/migrations na ordem, constraints, funcoes/triggers/RLS/policies pertinentes, permissao/auditoria e vinculos com o contrato; dados reais e secrets nao acompanham a copia. |
| Interface | Referencia aprovada, rota, arquivos/partials/assets, tokens, elementos/acoes/estados e peculiaridades; telas apontam ao briefing e suas regras donas. |
| Ambiente e entrega | Versoes/dependencias efetivamente usadas, nomes de configuracao segura, ordem de instalacao/migrations/integracao, comandos reais, artefato/revisao, verificacao e recuperacao compativel com dados. |
| Aceite e lacunas | Testes/fixtures controlados, cenarios/cadeias pertinentes, evidencias e limites; distinguir PROTOTIPO, REAL, PREVISTO e dependencia externa nao exercitada. |

Ao converter prototipo, o documento dono liga a revisao/fontes mostradas aos DNAs e regras aprovadas, com simulacoes, contrato real a substituir cada uma e o que ainda falta. Registrar comportamento de botoes, gatilhos, tempos, modos, unidades, disponibilidade, estados e regras de entrada/saida pertinentes. Contrato ainda inexistente e PROPOSTO/A_LOCALIZAR, nao API pronta nem autorizacao de criar banco. A entrevista nao e repetida se a decisao ja esta descrita. Fluxo de entrega/fechamento pertence a `romulo-prototipo-real`.

Metadados nominais de codigo/RPC/consumidores ficam nos mapas/inventario que o projeto ja exige; geracao/conferencia usa instrumentos existentes quando disponiveis. Nao manter copias manuais concorrentes. Regra de negocio/finalidade aprovada precisa de descricao humana no dono; geracao de nomes nao a substitui. Sem instrumento comprovado, conferir o recorte e declarar o limite, nunca alegar rastreio completo por existir um DNA.

## Manutencao e limpeza do conhecimento vigente

Atualizar o mesmo item/DNA e os consumidores comprovadamente afetados no mesmo lote. Resumo curto permite achar a decisao; detalhes validos, excecoes, exemplos e conexoes permanecem no dono. Decisao substituida sai da especificacao ativa; nao narrar tentativas descartadas nem transferir texto obsoleto para notas paralelas. Ideia futura ainda valida permanece PREVISTO no dono atual, sem criar pagina/API/DNA ficticio; ao surgir pedido relacionado, recuperar essa ideia conforme `romulo-especificar`.

Retirar duplicacao somente depois de conferir dono, equivalencia, referencias e preservacao historica exigida. Registros tecnicos obrigatorios, pendencias reais e vinculos nominais nao sao descartados por tamanho. Recibos antigos ja preservados no Git podem sair da leitura corrente somente quando o contrato/instrumento local permite e suas referencias foram reconciliadas; nao apagar manifests usados por guardas nem esconder falta de construcao/teste. Mudanca interna sem conhecimento novo nao exige narrativa artificial, salvo registro local obrigatorio.

No fechamento, requisito/DNA -> dono -> fonte/contrato/RPC/dado -> consumidores/testes, e inverso, deve concordar no alcance. O fiscal independente confere o candidato exato e a limpeza prevista; nao aceita somente a declaracao de que o executor seguiu o manual. Conferencia documental nao certifica funcao, pixels ou deploy; `romulo-verificar` define a evidencia por efeito. Uma regra escrita nao instala nem substitui uma guarda executavel.

## Como escrever o documento da pagina (TELA.md ou equivalente)

Cabecalho minimo: identidade documental e dono existentes; nome/finalidade da pagina; rota, menu/submenu; estado PROTOTIPO/REAL e revisao das fontes. Agrupar abas/subabas e configuracoes no mesmo documento quando pertencem a essa pagina. Indicar os arquivos que a renderizam/interagem e as cadeias/contratos donos, sem listar arquivos sem relacao.

Descrever a decisao vigente por completo: o leitor deve compreender a pagina mesmo que a conversa original seja apagada. Fonte/data de aprovacao podem identificar proveniencia, mas um link ao chat nao substitui o conteudo aprovado. Revisao nova substitui a descricao superada no mesmo item e reconcilia referencias; nao manter duas regras concorrentes nem arquivo de propostas descartadas. Preservar historico tecnico obrigatorio e ideias futuras validas conforme `romulo-documentacao`.

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
RESUMO (ate duas linhas/frases curtas):
1. <o que faz e por que existe>
2. <de onde recebe, quem utiliza e o efeito relevante de mudar/remover>
REGRA DONA: <link + ancora do contrato/componente; regra local fica aqui>
DETALHE NESTA TELA: <o que mostra/coleta; gatilho, condicoes, estados e excecoes>
CONEXOES: <ID da origem/destino, documento/ancora, informacao e motivo do vinculo>
TECNICO: <arquivos/simbolos, action/contrato/dados efetivamente usados>
DECISAO/EVIDENCIA: <fonte da finalidade/aprovacao; revisao, verificacao e limites>
RASTREABILIDADE (quando existente): <repositorio, links de issue/PR e commit da entrega>
PREVISTO (quando houver): <ideia/conexao futura, finalidade e fonte; estado separado>
```

O bloco e um modelo de escrita, nao um formulario a repetir vazio: omitir campos NAO_SE_APLICA, integrar secoes/tabelas equivalentes existentes e tornar desconhecidos relevantes explicitos. Nao publicar placeholders como documentacao pronta. Mostrar condicoes exatas quando alteram comportamento; duas linhas resumem, nao substituem detalhes necessarios. As mesmas regras nao sao copiadas para cada item: usar link ao dono e registrar somente a aplicacao particular na pagina.

O detalhe funcional/tecnico da pagina solicitada fica no documento dela, ligado ao DNA do item e ao contrato dono. Quando recebe informacao de outra pagina, o documento da origem tambem explica por que cadastra/fornece essa informacao e aponta para o consumidor; o consumidor explica para que a usa e aponta para a origem. Por exemplo ilustrativo: Ativos/Estoque documenta identidade, disponibilidade e fornecimento do equipamento; Construtor documenta como esse vinculo habilita a maquina e referencia o contrato de entrada/saida. Cada lado descreve sua propria responsabilidade, com dados/arquivos/contratos pertinentes; nao copiar todo o detalhe do Construtor para Estoque nem atribuir regra de processamento ao cadastro de ativos. Consultar o vinculo nos dois sentidos antes de retirar qualquer ponta.

Intencoes futuras ainda sem pagina ficam em PREVISTO no dono atual/assunto do prototipo, com descricao rica suficiente para retomar e vinculo no sumario existente. Nao criar documento vazio da pagina futura. Ao surgir pedido relacionado, consultar e apresentar essa ideia antes de propor outra; manter exemplos/excecoes pertinentes nos detalhes e distinguir pedido humano de sugestao e de implementacao comprovada. Atualizar o mesmo item ao receber novas explicacoes, conforme `romulo-documentacao`.

Ao receber uma decisao, atualizar o item correspondente pelo ID. Ao mover, preservar identidade e ajustar LOCAL/rotas e links. Ao remover/alterar capacidade, conferir e atualizar os itens consumidores comprovadamente afetados, dizendo o novo destino e como a informacao continua (ou que interrupcao foi explicitamente aprovada). Mudanca apenas de aparencia nao presume alterar contrato. A manutencao e consulta seguem `romulo-documentacao` e `romulo-especificar`; nenhum documento passa a permitir uma regra de negocio nova por si.

## Rastreabilidade DNA, issue, PR e commit

No item/secao do documento dono, associar os IDs existentes aos links completos de issue e PR do repositorio correto e ao commit conferido. DNA identifica a capacidade/elemento estavel; issue identifica tarefa; PR identifica entrega. Nunca substituir/sufixar o DNA com o numero GitHub, inventar identificador para preencher campo ou usar numero solto sem repositorio. Uma issue/PR pode atingir varios DNAs e um DNA pode ter varias entregas; nao exigir correspondencia um-para-um.

Reutilizar campo/tabela/registro de lote existente. Se precisar de formato, usar uma linha curta por entrega: `DNA existente | owner/repo#issue (link) | owner/repo#PR (link) | commit conferido`. Antes de a PR/commit existirem, omitir o campo ou indicar ainda nao criado no registro de trabalho; nao prever numeros/SHA. Issue e PR tambem apontam para os DNAs e documentos pertinentes. O mapa/sumario atual aponta ao dono; nao criar arquivo de mapa paralelo, cadastro universal ou copia manual em cada consumidor.

Consulta rapida: mapa/DNA -> decisao vigente no dono -> issue/PR/commit quando a tarefa/evidencia exigir -> codigo/consumidores atingidos. Ticket antigo nao reativa regra superada e PR/issue fechada nao comprova deploy ou funcionamento. Manter conhecimento vigente completo no TELA.md/equivalente; o Git e o GitHub preservam historia de entregas, sem acumular alternativas antigas no item ativo. Vinculos dos consumidores continuam bidirecionais e sem especificacao duplicada.

Metodo comum fica no padrao central; AGENTS local guarda ponte e protecoes, nao copia lista de ferramentas/regras. No processo/PROJETO.md ou equivalente existente, registrar somente o perfil concreto: ferramenta e finalidade, versao/revisao, comando/check, ambiente, alcance e estado CONFIGURADO/VERIFICADO/PREVISTO/NAO_SE_APLICA. Marcar opcional e motivo quando pertinente; nunca registrar segredo ou alegar instalacao por citar o nome. Nao criar arquivo vazio so para repetir o perfil.

## Enxugar AGENTS/CLAUDE existentes sem perder regras
Classificar cada trecho: identidade/ponte/protecao curta -> AGENTS; metodo global -> referencia central vigente; regra de negocio/guarda/peculiaridade local -> dono documental existente. Destino local faltante usa a tabela acima se a migracao estiver autorizada. Registrar DE/PARA no registro canonico do lote, criar/validar destino e link antes de retirar texto da origem.

Protecao nao desaparece nem e enfraquecida por mudanca de lugar. Link de protecao deve ser leitura obrigatoria antes da escrita, inclusive por outros agentes. Se qualquer destino estiver indefinido, sem acesso ou ainda nao validado, preservar o trecho original. Nao substituir AGENTS protegido sem autorizacao especifica; mover seu conteudo tambem e alteracao. CLAUDE.md novo e ponte, nao copia de regras.

Proibidos como atalhos: PLANO.md, FINAL.md, V2.md, notas de agente, resumo/memoria paralela e backups documentais. Excecao nao prevista so pelo gate `0393`, sem contornar proibicao local explicita. Historico fica no Git; o estado atual necessario fica no dono canonico.
