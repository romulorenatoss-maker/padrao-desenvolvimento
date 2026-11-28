# Modelo de padrao visual e de comportamento do projeto

Usar para completar catalogo/briefing equivalente, conforme [DOCUMENTACAO](../references/DOCUMENTACAO.md#padroes-locais-preenchiveis) e [interface](../skills/interface/SKILL.md#catalogo-local-e-promocao-de-uma-peca). Sem equivalente, destino: `docs/architecture/componentes/sistema.padrao_visual.md`. Resolver links no destino; nao copiar valores de outro projeto nem salvar placeholders como fatos.

## Identidade e fontes

Registrar projeto, dono do briefing/identidade, implementacao comum, sumario e revisao conferida. Valor tem um dono: se paleta/tipografia ja vivem no briefing ou tokens, referencia-los aqui. Preservar IDs e pecas parciais existentes. Este modelo define o que decidir; nao e uma colecao de escolhas previamente aprovadas.

## Setup e decisoes vigentes

Aplicar o [setup por referencia](../skills/interface/SKILL.md#setup-visual-por-referencia): primeiro recuperar decisoes e exemplos aprovados; perguntar somente o que falta ao recorte, uma decisao por vez, com opcoes concretas, recomendacao e motivo. A ordem abaixo orienta a descoberta, nao e um questionario a copiar no documento do projeto nem exige decidir todas as familias antes de trabalhar.

| Descobrir quando pertinente | Por que decidir ou recuperar essa referencia |
|---|---|
| Tarefa, usuarios e dispositivos | Determinar quais dados, acoes e modos precisam caber e continuar acessiveis. |
| Tela matriz por tipo de tarefa | Reutilizar uma composicao aprovada de lista, formulario, detalhe ou operacao. |
| Menu, topo, titulo, abas e contexto | Fixar ordem, alinhamentos, ocupacao e distancias entre regioes antes de inserir conteudo. |
| Tipografia e densidade | Preservar hierarquia, legibilidade, quantidade de informacao e altura efetiva dos elementos. |
| Tema, cores, bordas e selos | Definir peso visual, papeis semanticos e estados sem inventar outra identidade por tela. |
| Acoes, busca, filtros e configuracao | Tornar localizacao, hierarquia, presenca e resposta ao clique previsiveis. |
| Abertura, fechamento e retorno | Preservar contexto, foco, selecao e entradas em menus, modais e paineis. |
| Espaco insuficiente, zoom e estados | Definir quebra, rolagem e prioridades sem reduzir arbitrariamente fontes/alvos ou ocultar tarefa essencial. |

Salvar cada definicao expressamente escolhida de imediato conforme [registro progressivo](../skills/interface/SKILL.md#registro-progressivo-das-decisoes-visuais). Usar a ficha da peca/matriz como dono, sem manter uma segunda tabela com os mesmos valores. Perguntas abertas e tarefas/aceites pendentes ficam na fila temporaria, por link. Campos minimos da decisao:

| Campo | Como preencher |
|---|---|
| Identidade e alcance | ID/revisao existente; propriedade/peca e padrao do projeto, variante ou tela/modo excepcional. |
| Regra escolhida | Condicao e resultado concretos; distinguir invariantes de configuracao permitida. |
| Motivo e autoria | Motivo conhecido e origem/data do pedido; justificativa sugerida pela IA identificada como tal. |
| Referencia | Tela/rota, trecho/componente e revisao aprovados, evidencia disponivel e modos realmente vistos. |
| Definicao e aplicacao | Estado da definicao e autorizacao de migracao separados de implementacao, verificacao, apresentacao e aceite. |

Uma regra escolhida pode estar APROVADA e NAO_IMPLEMENTADA. Uma captura aprovada pode ainda ter medidas A_DEFINIR. Uma medicao de codigo existente pode estar OBSERVADA sem ser o alvo aprovado. Registrar essas diferencas; nenhuma delas autoriza preencher lacunas por palpite ou certificar a tela futura.

## Matriz de cobertura

Preencher progressivamente ID/link dono, estado da definicao e implementacao. Estados de definicao: A_DEFINIR, OBSERVADO, PROPOSTO, APROVADO ou NAO_APLICAVEL justificado. Estado da definicao nao substitui cobertura dos consumidores. A matriz aponta para as decisoes vigentes; nao guarda perguntas abertas nem fila de trabalho.

| Familia | Contrato a documentar conforme usada |
|---|---|
| Cores e tema | Papeis semanticos, valores/tokens, contraste, estados e temas adotados. |
| Letras e titulos | Familia/arquivo e fallback, pesos reais, tamanhos, entrelinha, espaco entre letras; titulo de tela/secao, rotulos, dados e hierarquia. |
| Medidas e composicao | Alturas/larguras fixas, minimas, maximas ou fluidas, margens/padding/gap, densidade, alinhamento, borda, raio, sombra e camadas. |
| Casca da tela | Esqueleto, topo, menu lateral expandido/recolhido, navegacao/retorno, bordas de referencia e composicoes por tarefa. |
| Abas e menus | Area de centralizacao/alinhamento, ordem, selecao, quebra do conjunto, teclado, contexto, abertura/ancora e fechamento. |
| Botoes e icones | Tipos semanticos, tamanhos, conjunto/espessura, icone ou texto, alvo de interacao e estados. |
| Barra de acoes, filtros e busca | Posicao, prioridades, combinacao, aplicacao/limpeza e comportamento. |
| Campos | Texto, lista, sugestoes/cadastro, selecao, moeda, data, mascara, anexo e outros efetivamente usados. |
| Formularios | Colunas, ordem, alinhamento de rotulos, ajuda, validacao e preservacao das entradas. |
| Foco e indisponibilidade | Teclado, foco visivel, desabilitado, somente leitura, motivo e permissao. |
| Listas e tabelas | Cabecalho/colunas, densidade, acoes por linha, pai/filhos, selecao e conteudo longo. |
| Ciclo da lista | Consulta inicial, atualizacao, busca/filtros/ordem, paginacao, concorrencia, erro/retry e retorno apos mutacao. |
| Vazio e carregando | Distinguir sem registros, sem resultados, carregamento inicial, atualizacao e falha. |
| Desktop e mobile | Composicoes, tabela/cartoes, navegacao, condicao de troca e preservacao das tarefas/contexto. |
| Modais e paineis | Padrao, confirmacao, pagamento quando houver; tamanho, acoes, foco e fechamento. |
| Selos, links e anexos | Semantica, cores, estado, visualizacao, acao e acesso. |
| Avisos e ajuda | Mensagem local, alerta, aviso rapido, tooltip e texto acessivel. |
| Graficos | Tipos usados, cores semanticas, legenda, escala, estados e alternativa de leitura. |
| Etapas e linha do tempo | Andamento, ordem, estado, eventos e rastro conforme a capacidade. |
| Mapa | Pinos, agrupamento, cores, numeracao, legenda e selecao. |
| Formatos | Data, hora/fuso, numero, moeda, unidade/quantidade e percentual conforme finalidade. |
| Selecao em lote | Marcacao, barra de acoes do lote, contagem e limpeza. |
| Ordenacao | Gatilho, indicador de direcao, ordem inicial e preservacao. |
| Icones | Origem unica, um icone por significado, desenho, tamanho e nome acessivel. |
| Valores financeiros | Sinal, cor de entrada/saida, zero, casas decimais e preco sem sinal. |
| Topo da tela | Ordem/posicao de titulo, abas, contexto/empresa, ajuda, configuracao e acoes; condicao de presenca e regra quando falta espaco. |
| Configuracao pendente | Indicador, contagem, onde aparece e quem pode resolver. |
| Atalhos de teclado | Teclas adotadas, escopo e conflito com campos. |
| Offline | Indicacao sem conexao, o que continua disponivel e sincronizacao. |
| Notificacoes | Onde aparecem, contagem, leitura e destino. |
| Permissao e sem acesso | Acao indisponivel com motivo, tela sem acesso e o que fica visivel. |
| Senha e confirmacao forte | Quando pedir, formato e falha. |
| Cancelar x apagar | Quando cancelar, quando apagar, texto do verbo, motivo e rastro. |
| Impressao e exportar | Ordem de carregamento, recibo, etiqueta, tamanho, cortes, exportacao do filtrado e dados pertinentes. |
| Movimento | Finalidade, duracao adotada, reducao de movimento e preservacao da operacao. |

Nao limitar a quantidade de pecas a esta tabela: cada responsabilidade reutilizavel necessaria ganha entrada; varias variantes podem pertencer a mesma peca. Familia nao usada nao exige implementacao futura.

## Ficha de peca

Repetir no dono somente para a peca realmente necessaria. Reutilizar ID existente; criar ID estavel conforme convencao local, nao um por pixel.

| Campo | Conteudo |
|---|---|
| Identidade | ID, nome, finalidade e quando usar/nao usar. |
| Definicao | Estado, origem/data e motivo conhecido da decisao, revisao aprovada e alcance; observado nao equivale a aprovado. |
| Contrato comum | Aparencia, medidas/tokens por referencia, composicao, conteudo permitido, semantica, acoes, estados e acessibilidade. |
| Desktop | Composicao, campos/acoes prioritarios e evidencia real da revisao. |
| Mobile | Composicao, acesso as tarefas e evidencia real da revisao; nao inferir do desktop. |
| Condicao de troca | Breakpoint/container/regra concretos da implementacao; larguras intermediarias pertinentes. |
| Implementacao | Arquivo, classe/simbolo/componente, fonte de estilo e controle de comportamento compartilhados. |
| Medidas e comportamento | Referenciar fichas abaixo com propriedades, condicoes e evidencia; separar regra aprovada do resultado efetivamente medido. |
| Configuracao permitida | Dados, colunas, textos e acoes que consumidores podem informar sem criar outro padrao. |
| Variantes | Nome, condicao, propriedades diferentes e decisao; sem duplicar regra comum. |
| Consumidores | Rotas/telas/modais e DNAs/fontes reais, diretamente ou por mapa existente. |
| Excecoes | Links para excecoes nominais, propriedades protegidas e limites. |
| Evidencias | Referencia/revisao, estado implementado/verificado/apresentado/aprovado por modo/local. |
| Migracao | Alcance autorizado e cobertura factual; fila aberta permanece no mecanismo temporario previsto. |

Aprovacao de um exemplo como padrao nao prova que todos os consumidores ja usam a implementacao ou foram vistos pelo responsavel.

## Matriz de composicao

Preencher para cada tipo de tela realmente usado, dentro do catalogo existente, reaproveitando sua identidade e as pecas. Uma tela concreta pode ser a referencia da matriz; registrar a revisao aprovada, nao apenas uma URL mutavel. TELA.md referencia a matriz/pecas e documenta seus dados, acoes e peculiaridades, sem copiar valores comuns.

| Campo da matriz | Conteudo verificavel |
|---|---|
| Identidade e finalidade | ID/revisao, tipo de tarefa e tela/rota de referencia; escopo e modos aprovados. |
| Fonte reutilizavel | Shell/layout/partial/componente e estilos realmente usados, com arquivo/simbolo/revisao. |
| Regioes | Menu, topo/titulo, abas, contexto/empresa, configuracao/ajuda, barra de acoes/filtros, conteudo e rodape, somente quando existentes. |
| Ordem e ancoragem | Ordem das regioes e dos controles, container de referencia e alinhamento horizontal/vertical de cada uma. |
| Presenca | Quando regiao/acao existe ou fica indisponivel, por contexto/aba/permissao; ausencia nao cria controle vazio. |
| Espaco e distribuicao | Largura util/maxima, alturas, padding/gap/bordas e colunas que crescem, encolhem ou conservam medida. |
| Quebra e rolagem | Condicao concreta de troca; conjunto ou item que muda de linha, nova ordem/alinhamento, overflow e rolagem da pagina ou do conteudo. |
| Invariantes | Propriedades que todos os consumidores equivalentes preservam; configuracoes e variantes permitidas por referencia. |
| Consumidores e prova | Telas/fontes reais, revisao implementada, evidencia e estado de cobertura por modo. |

Exemplos de precisao, validos somente se escolhidos no projeto: abas no centro geometrico da area de conteudo, conjunto inteiro na segunda linha quando colidir; acao principal na direita da barra com quebra definida; engrenagem junto ao seletor de empresa quando o contexto oferecer configuracao. Uma captura isolada pode mostrar a posicao, mas nao comprova a condicao de quebra nem o comportamento de abertura.

### Relacoes de espacamento

Registrar as distancias pertinentes entre bordas identificadas, com direcao, condicao e token/regra dona. Distinguir borda externa, borda interna e caixa de conteudo; nao registrar apenas "espaco = pequeno". Usar os pares que existem na matriz:

- menu -> inicio da area de conteudo e limite direito do conteudo -> borda da area util;
- topo/titulo -> abas e borda inferior do cabecalho/abas -> primeira barra ou conteudo;
- titulo -> acao, seletor de contexto -> configuracao/ajuda e distancia entre botoes;
- filtros/busca -> tabela, cabecalho -> primeira linha, celula -> texto/icone e lista -> paginacao;
- titulo de secao -> campos, label -> input, input -> ajuda/erro e distancia entre grupos;
- borda de modal/painel -> cabecalho/corpo/rodape e controle disparador -> menu/popover.

Se a distancia resultar da soma de padding, margin, gap e borda, registrar essa composicao e os tokens donos; nao criar uma segunda margem para compensar sem localizar a causa.

## Medidas e evidencia

Usar uma ficha/tabela por peca ou grupo coerente, somente com propriedades pertinentes. Referenciar o valor no seu dono; os valores computados sao fotografias de uma revisao/condicao, nao outra fonte manual de tokens.

| Campo da medicao | Registro |
|---|---|
| Propriedade e alvo | Nome CSS ou relacao entre elementos; ID da peca, elemento/estado e seletor/componente real. |
| Regra aprovada | Valor ou referencia ao token/contrato na revisao escolhida; A_DEFINIR se ainda nao determinado. |
| Tipo e unidade | Fixa, minima, maxima, fluida ou derivada; px CSS, rem, %, formula ou conteudo, conforme a fonte. |
| Declarado e origem | Valor/formula no arquivo, token, seletor, revisao e regra vencedora relevante; observado nao significa aprovado. |
| Computado e caixa | Estilo computado e dimensao renderizada quando medidos; altura de linha, padding, bordas e min/max que explicam a caixa. |
| Condicoes | Rota/instancia, estado, viewport/container, zoom, tema, fonte carregada, dados controlados e modo. |
| Evidencia e delta | Metodo/data/revisao, captura ou medicao disponivel, esperado x observado e classificacao da diferenca. |

Guardar unidade/formula original e resultado em CSS px quando medido; rem depende da fonte raiz e % depende do container. Altura minima nao equivale a altura fixa. Nao transformar medidas de captura em px CSS exatos, adivinhar a fonte ou assumir que o CSS do destino e a referencia aprovada. Sem acesso a fonte/renderizacao, registrar OBSERVADO/ESTIMADO ou NAO_VERIFICADO e a lacuna especifica.

Cobrir quando usado: fonte/tamanho/peso/entrelinha; largura/altura/min/max; margens/padding/gap; bordas (lado, espessura, estilo e cor), raio e sombra; cor de texto/fundo por estado; dimensao/espessura do icone e area interativa; alinhamento, camadas e overflow. Medida fluida continua sendo um contrato preciso; nao fixar todas as dimensoes em px para simular padronizacao. Metas de acessibilidade e comportamento no zoom permanecem aplicaveis.

### Densidade de listas e tabelas

Definir por variante aprovada e reutilizar nos consumidores equivalentes, independentemente do numero de registros e dos nomes das colunas:

- tipografia de cabecalho, dado principal/secundario, numeros e totais; peso/entrelinha e alinhamento;
- altura fixa ou minima de cabecalho/linha, padding vertical/horizontal, borda divisoria e espaco entre colunas;
- largura fixa/minima/flexivel por papel de coluna, distribuicao da area util e alinhamento de numeros/acoes;
- tamanho e padding de selos, checkbox, icones e botoes da linha, que tambem podem determinar sua altura;
- selecao, hover, foco, agrupamento pai/filhos, indentacao, expansao, total e acao em lote quando usados;
- conteudo longo: quebra, truncamento e acesso ao conteudo completo; variante para multiplas linhas quando necessaria;
- relacao com filtros, carregamento/vazio/erro e paginacao, conforme o contrato de comportamento.

Aumentar a largura util nao aumenta fonte, padding ou altura da linha. Mesma densidade nao significa mesma altura absoluta para conteudos que quebram em mais linhas; registrar a regra e comparar com dados/estados equivalentes. Diferenca visual de peso tambem depende de cores, bordas, fundos e quantidade de selos; nao inferir maior altura so pela aparencia.

### Interacao e estados

Para botoes, abas, menus, configuracoes, overlays e listas, registrar gatilho, resultado/destino, ancora/posicao, largura/altura, direcao de abertura e colisao com bordas, foco inicial/retorno, teclado, clique fora/Escape/fechamento quando pertinentes e preservacao de dados/contexto. Registrar carregando, atualizado, vazio, erro, selecionado, desabilitado e somente leitura conforme usados, incluindo aparencia e resposta; nenhum percentual ou prazo ficticio. Valores e regras vem do projeto, sem comportamento universal presumido por este modelo.

## Exemplo de preenchimento: lista de dados

Exemplo de estrutura, sem escolher valores ou declarar aprovacao por antecipacao:

- Peca: lista compartilhada do projeto; usar seu ID real. A tela informa colunas, rotulos, fonte de dados e acoes autorizadas.
- Contrato comum: preencher carregamento inicial/atualizacao, filtros/ordem, pagina, estados vazio/sem resultado/erro, respostas fora de ordem e retorno apos editar/excluir conforme interface.
- Desktop: registrar a composicao decidida, por exemplo tabela quando escolhida.
- Mobile: registrar a composicao decidida, por exemplo cartoes quando escolhidos; ambos consomem o mesmo contrato e preservam as tarefas essenciais.
- Referencia: arquivo/simbolo, rota, revisao e capturas reais quando disponiveis. Exemplo sem implementacao fica PROPOSTO, sem links ficticios.
- Promocao: apos o aceite da peca, perguntar se deve virar padrao global quando ainda nao decidido. Pedido global ja expresso dispensa repeticao.
- Aplicacao: encontrar equivalentes e migrar somente o alcance autorizado, com verificacao e aceite por local; nao usar CSS copiado por tela.

## Diferencas e excecoes

| Campo | Registro necessario |
|---|---|
| Classificacao | PADRAO_BASE, VARIANTE_APROVADA, CONFIGURACAO_PERMITIDA, EXCECAO_A_PEDIDO ou DIVERGENCIA_NAO_ESCLARECIDA. |
| Escopo | Tela/modal/elemento, consumidor, modo desktop/mobile e condicao. |
| Base | ID e revisao do padrao herdado. |
| Diferenca | Propriedades/comportamentos exatos; restante continua herdado. |
| Motivo e origem | Pedido/decisao comprovados e motivo conhecido; sem motivo adicional, registrar esse fato. |
| Protecao | Limite de alteracao, dependencia compartilhada e evidencia/revisao pertinente. |

Variante responsiva aprovada pertence ao padrao. Sem origem nao escrever "a pedido". Uma solicitacao local nao muda todos os consumidores nem autoriza alterar propriedades adicionais.

Tabelas do dono, conforme o [ciclo de vida](../skills/interface/SKILL.md#ciclo-de-vida-de-uma-peca). Numeros `E##`, `V##` e `D##` nunca sao reaproveitados.

### Excecoes registradas

| ID | Peca (rev.) | Escopo | Diferenca exata | Origem | Aplicado em (arquivo + DNA) | Tela (doc) | Estado |
|---|---|---|---|---|---|---|---|

Estado da definicao: VIGENTE, AGUARDANDO_DONO ou ENCERRADA; aplicacao e evidencia ficam separadas. Excecao aplicada exige o marcador `PADRAO_EXCECAO: E## <peca>` em comentario abaixo do DNA e a linha correspondente no documento da tela. Definicao autorizada antes da implementacao registra aplicacao pendente, sem inventar arquivo/DNA ou marcar conformidade. Na aplicacao, completar os tres vinculos no mesmo lote. TELA.md detalha o delta local por referencia; o catalogo permite localizar seu alcance, sem outra copia de valores comuns.

### Variantes aprovadas

| ID | Peca | Modo | Diferenca | Origem | Estado |
|---|---|---|---|---|---|

### Divergencias

| ID | Assunto | Detalhe | Situacao | Perguntado em |
|---|---|---|---|---|

Situacao: FALTA_APLICAR (peca APROVADA, corrigir), AGUARDANDO_DONO (peca OBSERVADO/A_DEFINIR, uma pergunta por vez pela pasta temp) ou ENCERRADA.

## Cobertura e conferencia

Usar mapa existente com consumidor/DNA, peca/revisao, modo, classificacao, diferenca, implementacao e evidencias. Separar encontrado, migrado, verificado, apresentado e aprovado; locais inacessiveis ficam NAO_VERIFICADO. Nao marcar sistema inteiro conforme por um teste ou por um componente atualizado.

O fiscal compara candidato, catalogo, matriz, medidas, implementacao comum, diferencas e consumidores reais em toda criacao/correcao. Excecao so cobre a base/revisao, propriedades, modos e locais autorizados; ter `E##` nao aprova o restante. Falhas corrigiveis voltam a construcao; atualizacao da referencia para esconder desvio e invalida. Definicoes visuais escolhidas ficam imediatamente no dono, com aplicacao/aceite separados e historico no Git. Perguntas, tarefas e confirmacoes abertas ficam somente na pasta temp de construir, por referencia.
