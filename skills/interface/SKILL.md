---
name: interface
description: "Use em toda criacao, alteracao, correcao ou revisao com efeito visual ou interativo: telas, abas, botoes, icones, formularios, tabelas, CSS, tokens, componentes, navegacao e prototipos. Aplique a referencia aprovada, preserve peculiaridades e verifique a tela renderizada, sem inventar elementos ou estilos."
---

# Interface

Acionar esta skill em todo pedido que atinja a apresentacao ou interacao da tela, inclusive efeito indireto; nao esperar que o responsavel diga "usar design". Usar a skill/ferramenta visual e de geracao/edicao de imagem disponivel e pertinente para diagnostico e previa conforme este fluxo, sem instalar recurso por rotina. Alteracao interna sem efeito de UI nao aciona redesenho.

Fonte dona da consistencia visual, composicao e peculiaridades. Use com `especificar` para proposta/utilidade, `construir` para conexoes e `verificar` para evidencias. Nao exige React, Tailwind, biblioteca ou estrutura de pastas especifica.

## 1. Descobrir e aprovar a referencia

Antes de editar, localizar sistema visual real: tokens/tema, componentes, layouts, exemplos aprovados, formatos, estados e peculiaridades do recorte. Inspecionar a renderizacao existente quando o ambiente permitir; sem navegador, declarar a verificacao visual nao executada, nao inventar screenshot.

Consultar o briefing visual do projeto conforme [contratos de projeto](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao): cores, letras, botoes, cantos, espacamentos e variantes aprovadas com valores/referencias concretos. Tela nova reutiliza esse contrato; alteracao consulta somente o trecho pertinente. Se faltar, propor o recorte necessario antes da UI definitiva. Briefing novo nao autoriza uniformizar telas antigas nem remover peculiaridades aprovadas; divergencias seguem a migracao e aprovacao das secoes 4 e 5.

Na proposta, confrontar o elemento com o equivalente aprovado em outros locais do sistema: listas, tabelas, botoes, telas, menus, cores e estados. Reutilizar o mesmo token/componente/variante e registrar nova decisao vigente no briefing/dono, com links no DNA; nao duplicar valores em cada TELA.md. Se os locais divergem e nao ha referencia aprovada, mostrar essa diferenca e propor a referencia antes de uniformizar. Ajuste local nao autoriza alterar os outros locais: migracao de consumidores compartilhados precisa do alcance e aprovacao pertinentes.

O estilo mais repetido nao e necessariamente o melhor nem o aprovado. Em sistema inconsistente, propor uma referencia representativa na tecnologia existente e apresenta-la para aprovacao antes de espalhar alteracoes. Uma referencia util mostra formulario, tabela, botoes, abas/modal quando pertinentes e estados reais, nao apenas uma imagem decorativa.

Padrao GLOBAL significa identidade compartilhada dentro daquele projeto, nao mesma marca/aparencia em todos os projetos. Padroes por tarefa (lista, detalhe, formulario, operacao) podem compor o mesmo sistema. Excecao e desvio da referencia aprovada, nao variacao de layout ja prevista.

Sem referencia suficiente: apresentar proposta visual do recorte, aprovar e implementar so os tokens/componentes necessarios. Nao construir catalogo inteiro para uma unica funcao. Com referencia aprovada: reutilizar, sem reabrir perguntas resolvidas.

### Catalogo local e promocao de uma peca

Desde a primeira UI, materializar o catalogo DENTRO do projeto conforme [padroes locais preenchiveis](../../references/DOCUMENTACAO.md#padroes-locais-preenchiveis), usando [PADRAO_VISUAL.md](../../templates/PADRAO_VISUAL.md) para completar o equivalente existente. Sem equivalente, usar o destino documental previsto. O modelo central lista o que decidir; o projeto guarda sua identidade, valores, comportamento, implementacao e aprovacoes. Nao copiar a identidade de outro produto nem criar catalogo concorrente ao ja usado.

Antes de criar OU alterar, consultar as pecas pertinentes, variantes desktop/mobile, estados, excecoes e consumidores, e conferir a fonte implementada. Cadastrar progressivamente cada peca nova com ID estavel, finalidade, contrato, implementacao, revisao e origem; lacunas ficam A_DEFINIR/PROPOSTO, sem assumir aprovacao. Preservar IDs e definicoes parciais existentes, completando somente o que falta. A quantidade de pecas nao e fixa.

Quando o responsavel aprovar uma peca nova ou escolher um exemplo existente e ainda faltar decidir sua promocao, perguntar uma vez: "Posso salvar esta [peca, tela e revisao] como padrao para os usos equivalentes em todo o sistema, com estas versoes desktop/mobile?". Mostrar as variantes que realmente existem; nao atribuir aprovacao mobile a uma previa so desktop. Nao repetir essa pergunta por cada uso de um padrao ja adotado. "Esta bom" confirma o item mostrado conforme a secao 6, mas sozinho nao promove toda a tela nem autoriza migracao global.

Se o responsavel ja disser "use esta lista como padrao em todo o sistema", registrar essa decisao expressa sem outra pergunta de inicio. Identificar exatamente a peca/propriedades e os equivalentes abrangidos; registrar referencia/revisao aprovada, variantes confirmadas e alcance da migracao. A aprovacao de um menu nao aprova automaticamente titulos, graficos e campos da mesma tela. Separar os fatos: aprovacao da peca como padrao, autorizacao de migracao, implementacao por consumidor, verificacao, apresentacao e aceite de cada resultado.

Com alcance global autorizado, varrer o sistema conforme secao 5 e migrar os equivalentes compativeis em lotes, sem pedir novamente permissao de construir por tela. Se so a definicao futura foi aprovada, aplicar nos novos usos e registrar a migracao antiga como nao autorizada. Decisao ausente, efeito fora do alcance, mudanca de regra/stack e propriedade de excecao protegida exigem resolver somente esse ponto. Nao bloquear partes independentes ja autorizadas.

O padrao vigente continua obrigatorio nas proximas criacoes/correcoes. Alteracao posterior, direta ou indireta por token/CSS/componente/dependencia, exige confrontar a revisao aprovada e os consumidores. Registrar nova decisao quando o responsavel mudar o padrao; nao substituir referencia para encobrir regressao. Historico fica no Git, e a atualizacao da skill central nao troca valores locais. Pedido de mudar peca APROVADA: listar os consumidores e perguntar "A peca `<id>` (Rn) e usada em [telas]. Troca o padrao em todas ou excecao so desta tela?", salvo se o responsavel ja disse "em todas" ou "so aqui"; o efeito segue o [ciclo de vida](#ciclo-de-vida-de-uma-peca).

### Ciclo de vida de uma peca

1. Catalogo na primeira interface: a primeira tela do projeto ja cria o catalogo local conforme [PADRAO_VISUAL.md](../../templates/PADRAO_VISUAL.md), com as pecas que ela usa.
2. Promocao: perguntar "Esta bom para gravar como padrao?" somente se esse alcance ainda nao foi decidido, nomeando peca, tela, revisao e modos vistos. Pedido expresso de padrao ja autoriza salvar a definicao, sem nova confirmacao.
3. Escolha explicita = definicao APROVADA na revisao identificada, preservando ID e revisoes existentes. Sem resposta, a candidata continua PROPOSTO, sem virar heranca obrigatoria; conservar a base aprovada, se houver, e resolver somente a dependencia. Recusa de promocao conserva o aceite local que existir; rejeicao da forma retira essa candidata dos usos futuros. Nao ressuscitar proposta recusada.
4. Heranca: novas criacoes/correcoes consultam a definicao vigente; registrar separadamente qual revisao cada consumidor efetivamente implementa. Aprovar a definicao nao comprova nem autoriza por si a migracao de todos.
5. Troca x excecao: troca = nova revisao (Rn+1) no catalogo e migracao dos equivalentes no alcance e lotes autorizados, com cobertura explicita; excecao = proximo `E##` (numero nunca reaproveitado) com tres vinculos no mesmo lote de aplicacao: linha na tabela de excecoes do catalogo; marcador `PADRAO_EXCECAO: E## <peca>` em comentario na linha abaixo do DNA da unidade alterada; linha `PADRAO_EXCECAO: E## <peca>` com link ao catalogo no documento da tela, fora do bloco estruturado ([documentacao](../../references/DOCUMENTACAO.md#padroes-locais-preenchiveis)). Antes de aplicar, registrar a definicao autorizada e deixar implementacao/marcador pendentes, sem inventar caminho ou evidencia.
6. Diferenca sem pedido: dizer "nao esta no padrao (`<id>` Rn)" e procurar excecao registrada. Sem excecao: peca APROVADA e corrigida no lote autorizado; peca OBSERVADO/A_DEFINIR vira divergencia `D##` e a pergunta vai ao responsavel uma por vez, pela pasta temp.

Paridade entre telas: a mesma peca com forma diferente em duas telas e defeito, salvo excecao ou variante registrada. ID de peca e neutro, sem nome de modulo; tela citada numa peca e so referencia. Icones: um icone por significado, mesma origem, desenho e tamanho; tela nova usa o do catalogo; icone novo e peca nova e pergunta ao responsavel.

### Desktop e mobile no mesmo padrao

Definir duas apresentacoes quando a tarefa pedir adaptacao: composicao, prioridade de campos, navegacao, acoes, filtros, largura/altura, toque, teclado e condicao concreta de troca. Desktop pode usar tabela e mobile cartoes; ambos pertencem a mesma peca/contrato com variantes nomeadas. Nao duplicar fonte de dados ou regra de negocio para trocar a apresentacao.

Documentar breakpoints ou condicoes de container conforme a implementacao aprovada, sem valores universais inventados. Registrar o que muda e o que permanece: dados, identidade, permissoes, acoes essenciais e contexto. Ocultar coluna no celular precisa preservar acesso a informacao necessaria e as tarefas. Conferir tambem larguras intermediarias, conteudo longo e troca de modo quando afetados.

Variante responsiva aprovada nao e excecao por tela. Uma diferenca exclusiva solicitada para o mobile de uma tela e excecao apenas nesse modo/propriedades; desktop e demais propriedades continuam herdados. Proposta/implementacao/verificacao/aceite de cada modo ficam distintos, sem aprovar automaticamente o modo nao apresentado.

### Entrevista inicial e escolha de ferramentas

Aplicar o [setup visual por referencia](#setup-visual-por-referencia) e o [registro progressivo](#registro-progressivo-das-decisoes-visuais) abaixo. O roteiro de descoberta e as fichas preenchiveis ficam no [modelo visual](../../templates/PADRAO_VISUAL.md); escolhas de um projeto nao se tornam defaults do metodo central.

### Setup visual por referencia

1. Localizar o catalogo/briefing, os pedidos explicitos ja dados e as telas/componentes aprovados antes de perguntar. Materializar ou completar somente o dono previsto, ligado ao sumario; "DNA visual" e o contrato local com identidade estavel, nao outro arquivo concorrente nem DNA funcional por pixel.
2. Escolher a referencia por tarefa (lista, formulario, detalhe ou operacao) no alcance ja aprovado. Examinar fonte, revisao e renderizacao disponiveis; identificar o que a referencia realmente define e o que falta. Uma tela aprovada pode fornecer composicao e pecas, sem impor seus campos/dados a outro modulo.
3. Perguntar UMA decisao ausente por vez, com exemplo/recorte concreto, opcoes pertinentes, recomendacao e o motivo pratico: efeito em densidade, legibilidade, espaco ou operacao. Se nao houver referencia, propor uma composicao minima identificada como PROPOSTO. Nao pedir ao responsavel numeros que podem ser extraidos da fonte aprovada, nem agrupar varias escolhas na mesma pergunta.
4. Registrar cada escolha conforme a secao seguinte e continuar o trecho ja autorizado. Nao aguardar um catalogo completo; lacuna bloqueia somente a parte que depende dela. Familias ainda nao usadas ficam A_DEFINIR ou NAO_APLICAVEL justificado. Reabrir apenas decisao nova ou contradicao indispensavel; bug, tela semelhante e escolha ja expressa nao repetem a entrevista.

### Registro progressivo das decisoes visuais

Salvar imediatamente cada definicao visual expressamente escolhida no dono persistente, mesmo antes de construir. Registrar ID/revisao, regra concreta, fonte/data da decisao, motivo conhecido, referencia e alcance: padrao do projeto, variante ou excecao nominal. Motivo tecnico sugerido pela IA fica identificado como sugestao; nao atribui-lo ao responsavel. Proposta ainda nao escolhida permanece PROPOSTO, nunca APROVADO por existir codigo ou silencio.

Separar definicao aprovada, autorizacao de aplicacao, implementacao, verificacao, apresentacao, aceite visual e cobertura. Por exemplo, uma regra de posicao pode estar APROVADA e sua implementacao NAO_IMPLEMENTADA; isso nao aprova a futura tela. Perguntas abertas, trabalho a executar e aceite pendente ficam na [pasta temp](../construir/SKILL.md#pasta-temp-de-perguntas-e-fila-temporarias), apontando para ID/revisao, sem duplicar a regra nem adiar seu registro. Esta distincao prevalece sobre a antiga restricao de guardar a decisao somente depois da construcao.

Pedido que declare "padrao", "sempre" ou equivalencia abrangida atualiza o trecho comum do projeto. Pedido "somente nesta tela" registra a peculiaridade no TELA.md/dono com os vinculos da secao 4. Se o alcance de uma mudanca ainda for ambiguo, conservar o padrao vigente e perguntar apenas se e geral ou local; nao generalizar toda aprovacao pontual. Registrar cada incremento na mesma ficha, preservando escolhas nao alteradas. Revogar/substituir somente o trecho decidido e manter historico no Git.

### Escolha e comparacao de ferramentas

Escolher recursos pelo efeito: direcao estetica/colecao de DESIGN.md ajuda a propor; image-to-code exige alvo visual escolhido e ajuda a reproduzir; guidelines revisam acessibilidade/usabilidade/performance; navegador/Playwright conferem renderizacao e regressao, nao decidem gosto nem editam layout por si. Confirmar fonte, revisao, compatibilidade e ferramentas realmente disponiveis. Nenhum recurso externo autoriza framework, dependencia, instalacao, troca de fonte canonica ou reforma de tela aprovada.

Quando o responsavel pedir comparacao de abordagens, preparar previas isoladas da MESMA pagina, com mesmo conteudo, estados, viewport e alcance. Comparar hierarquia, legibilidade/contraste, densidade, acoes, responsividade e fidelidade; declarar o que foi realmente executado. Duas propostas do mesmo modelo com instrucoes diferentes nao sao um benchmark de dois executores independentes. Imagem gerada e proposta, nao prova de UI funcional; bloqueio de renderizacao nao vira PASSOU.

Escolha aprovada fixa a referencia daquele projeto. Novas telas reutilizam tokens/componentes; tela antiga muda somente no lote autorizado, preservando regras, DNAs e peculiaridades. Nao carregar varias skills de gosto simultaneamente como ordens concorrentes nem obrigar uma comparacao A/B a cada ajuste. Reusar verificacoes aprovadas; corrigir falha e retestar somente o efeito atingido.

### Plugins de design na construcao e revisao

Uso obrigatorio (1.0.21): todo lote usa todos os plugins do setup no seu momento, sem esperar pedido: (1) Ponytail ativo em toda sessao e `ponytail-review` no codigo do candidato antes do fiscal; (2) frontend-design para o acabamento visual (espacamento, hierarquia, estados, consistencia) de toda tela, aba ou modal criado ou alterado, sempre preso ao molde/briefing e aos componentes ja existentes, sem inventar estetica nova nem trocar o padrao aprovado; (3) antes de mostrar qualquer tela nova ou alterada ao responsavel (secao 6), UI Design Review (`ui-review` e depois `ui-polish` nos itens importantes) na tela renderizada em celular e desktop, corrigindo dentro do padrao do projeto. O construtor entrega ao fiscal a lista `plugin -> skill -> tela/arquivo -> resultado (o que apontou e o que corrigiu ou por que nao corrigiu)`. A revisao nao substitui a aprovacao do responsavel nem autoriza mudar estrutura aprovada. Plugin ausente ou sem acesso: declarar o limite na lista, nunca fingir uso, e seguir a revisao visual ja prevista (secao 5). Nao usar outros plugins de design para este fim.

## 2. Uma fonte implementada, varios consumidores

Buscar componente/token/variante antes de criar. Reutilizar; estender quando semanticamente compativel; criar somente responsabilidade distinta necessaria. Nao criar Botao2, copias de modal ou um componente unico com dezenas de flags contraditorias.

Similaridade exige investigar e reutilizar o equivalente compativel; nao exige perguntar novamente quando o pedido e a referencia ja determinam a escolha. Antes de construir qualquer tela, modal, lista, campo, menu ou acao, procurar no projeto o que ja faz algo parecido (mesmo assunto, mesmo tipo de dado, mesma acao: garantia, anexo, lancamento pai/filhos, valor em moeda, selecao em lista, cor de menu, forma de carregar) por nome, rota, classe e DNA. Se houver alternativas com diferenca indispensavel ainda nao decidida, perguntar somente essa escolha. Quando o equivalente ja atende ao pedido, reutilizar sem segunda autorizacao. A implementacao usa componente compartilhado (um arquivo, uma fonte de estilo) e cada tela so informa de onde le e onde grava. Reutilizacao em pedido local nao amplia alcance: mapear cada local atingido e pedir autorizacao apenas para consumidores fora do escopo ja autorizado. Padronizacao global expressa cobre os equivalentes desse escopo conforme a secao 1, sem repetir permissao por local; a confirmacao visual individual do resultado continua conforme a secao 6. Se nao for possivel limitar o efeito ao alcance autorizado, bloquear a escrita dependente e explicar, sem duplicar o componente para contornar a decisao. Proibido copiar markup/CSS de outra tela, recriar uma variante "parecida" ou dar cor/letra/espacamento proprios a um elemento que ja tem padrao no projeto. Valor em moeda usa a mascara compartilhada do projeto; lista de lancamentos segue a tela de referencia aprovada.

| Parte | Contrato visual que deve vir da fonte aprovada |
|---|---|
| Tema e tipografia | Cores semanticas, contraste, hierarquia, fontes, formatos de data/moeda/unidade. |
| Titulos e secoes | Hierarquia semantica, tamanho/peso, distancia e relacao com acoes; nao derivar cada titulo por gosto. |
| Layout | Densidade, largura, espacamento, alinhamento, breakpoints e composicoes por tarefa. |
| Botoes | Variantes semanticas, tamanhos, rotulo, icone, alinhamento e estados. |
| Icones | Familia coerente, dimensoes renderizadas e espessura; icone pequeno nao exige alvo clicavel pequeno. |
| Campos | Label, ajuda, obrigatoriedade, erro, altura, foco e estado de leitura. |
| Tabelas/listas | Densidade, colunas prioritarias, filtros/ordenacao/paginacao quando necessarios, conteudo longo e vazio. |
| Abas e navegacao | Selecao, contexto, teclado, URL/retorno quando pertinente; sem abas vazias. |
| Modal/drawer | Contexto, dimensoes, cabecalho, acoes, foco/retorno de foco e fechamento seguro. |
| Mensagens e estados | Carregando, vazio, erro recuperavel, sucesso, indisponivel e sem permissao quando aplicaveis. |
| Responsividade | Variantes desktop/mobile e condicao de troca; prioridade, navegacao, reflow e overflow deliberado. |
| Ajuda, selos e avisos | Icone/texto, tooltip, estados, semantica de cores e acessibilidade. |
| Graficos, etapas, linha do tempo e mapa | Paleta/legenda, marcadores, estados/ordem e informacao equivalente acessivel; somente quando usados. |
| Impressao e formatos | Recibo/etiqueta/ordem, unidades, data/hora/fuso, numeros, quantidade e percentual conforme finalidade. |

Valores de identidade visual pertencem a tokens e componentes. CSS de composicao local pode existir, consumindo esses contratos sem redefinir arbitrariamente fontes, cores, botoes e medidas. Valores dinamicos de layout/graficos nao sao automaticamente violacao. Nao impor "zero CSS local" nem transformar toda variacao em token global.

Nao corrigir defeito local com seletor global abrangente, `!important` em cascata ou redefinicao de `svg`, `button`, `table` para todo o sistema. Causa compartilhada comprovada pode exigir correcao na fonte compartilhada, com impacto e consumidores verificados. Nunca trocar framework ou biblioteca de componentes so para padronizar.

### Matriz de composicao e medidas verificaveis

Registrar no mesmo catalogo a matriz aprovada para cada tipo de tela realmente usado, conforme as [fichas de composicao e medidas](../../templates/PADRAO_VISUAL.md#matriz-de-composicao). Identificar regioes e seus componentes compartilhados: menu, topo, titulo, abas, contexto/empresa, configuracao, ajuda, barra de busca/filtros/acoes, conteudo e rodape. Definir ordem, alinhamento relativo a qual container, distancia entre bordas, condicao de presenca e regra de quebra/rolagem. Ausencia de uma acao nao autoriza cria-la nem preencher seu espaco com decoracao.

Uma posicao precisa de condicao: "centralizado" informa centro de qual area; "a direita" informa regiao e comportamento quando falta espaco; configuracao informa quando existe para o contexto/aba e quem pode acessa-la. Se o pedido definir que o conjunto de abas desce uma linha, registrar o gatilho e o alinhamento na segunda linha; nao trocar por abas espremidas ou centralizar apenas no espaco sobrando. Esses sao exemplos de detalhamento de escolhas locais, nao defaults para todos os projetos.

Para cada medida pertinente, ligar propriedade/regra aprovada ao token/componente e registrar unidade, tipo (fixa, minima, maxima, fluida ou derivada), condicao/modo e origem/revisao. Distinguir valor declarado no CSS, estilo computado, caixa renderizada e alvo aprovado. Usar CSS px para dimensoes medidas; manter unidade/formula original de rem, %, clamp ou conteudo e o contexto de conversao. Registro de medicao e evidencia datada, nao uma segunda lista manual de tokens. Screenshot sem escala/fonte conferida permite observacao ou estimativa identificada, nunca certificar px CSS, familia de fonte ou token exato.

Conferir fonte realmente carregada, peso, entrelinha, padding, gap, borda, box-sizing, min/max, tema, seletores vencedores, heranca e ordem dos estilos no elemento real. A soma dessas propriedades pode alterar a altura mesmo com o mesmo token nominal. Classes iguais e `base.css` existente nao provam fonte unica em uso. Divergencia pede localizar a regra causadora e corrigir o dono apropriado, sem acumular overrides ou assumir que CSS antigo e aprovado.

Pedido de ampliar somente largura preserva tipografia, densidade, altura de controles/linhas, espacamentos internos, cores, bordas, raios e comportamento aprovados. Distribuir largura disponivel conforme a matriz; quebra necessaria segue a variante existente. Se ela nao resolver uma colisao, esclarecer somente esse ponto. Nao escalar toda a interface, aumentar a fonte para preencher espaco nem aceitar padding/altura herdados do destino. Na conversao de HTML/prototipo ao real, manter a mesma matriz, pecas e revisao; adaptar dados/contratos sem reinterpretar a aparencia.

Consumidor referencia matriz e pecas por ID/revisao, configura seus dados/colunas/acoes e registra apenas composicao ou excecao local autorizadas. Reusar shell/partial/componente e fonte de estilo reais; nao colar uma versao "parecida" em cada tela. Antes de entregar, comparar invariantes e deltas do pedido contra a referencia na revisao conferida, conforme secao 5.

## 3. Botoes com sentido e comportamento previsivel

Use o contrato de utilidade de `especificar`. Rotulo diz a acao/resultado, nao "Clique aqui". Hierarquia reflete importancia, nao decoracao. Agrupe acoes secundarias sem esconder a essencial; mantenha destrutivas distintas. Nao fabrique botoes para preencher cards.

Use semantica nativa correta: link para destino, botao para acao, submit no formulario, controles de aba apropriados. Nome acessivel para acao so com icone; tooltip sozinho nao substitui. Preserve teclado, foco visivel, labels e anuncio de erro/resultado pertinentes.

Estado indisponivel explica o motivo quando necessario; nao e justificativa para entregar funcao ainda nao implementada. Loading nao pode ficar infinito; falha permite recuperacao e preserva dados digitados. Bloquear duplo clique na UI nao substitui integridade/idempotencia no servidor quando aplicavel.

Nao padronizar apenas classes: verificar tamanho computado/renderizado do icone, botao, texto, espaçamento, area clicavel e alinhamento. Tokens ajudam, mas nao garantem contraste, modo escuro ou acessibilidade automaticamente. Adote as metas de acessibilidade do projeto; avalie operacao por teclado, zoom e tecnologias assistivas conforme risco, combinando automacao e revisao manual.

## Estados de carregamento e movimento com finalidade

Toda interface criada/alterada trata os estados pertinentes; reutilizar o componente existente e registrar a aplicacao no documento dono. Skeleton cabe no conteudo assincrono ainda desconhecido, preservando dimensoes/foco e sem esconder dados ja conhecidos; operacao instantanea nao precisa de skeleton artificial. Lazy loading cabe em imagens/conteudo secundario pesado, nunca atrasa controles, alertas ou informacao essenciais. Carregamento termina em sucesso/erro recuperavel, preserva entradas e impede envio duplicado.

Progresso determinado usa medicao real; sem total conhecido, usar indicador indeterminado, nunca percentual inventado. Comando enviado nao e estado confirmado nem tarefa concluida. Animacao de entrada/saida ou troca de estado deve explicar a mudanca sem atrasar clique, teclado ou operacao frequente. Respeitar `prefers-reduced-motion`, sem perder a informacao/atencao do alerta. Nao colocar spinner, skeleton, fade ou hover em todo elemento por rotina.

Para criar ou revisar movimento, consultar `motion-principles`; carregar somente o workflow e referencias pertinentes ao recorte. A skill inclui o pacote completo importado, mas este padrao define preservacao, escopo, arquitetura e autorizacao. CSS/JavaScript nativos em projetos PHP puro; exemplo React/Framer Motion nao permite framework novo. Aplicar novos estados/movimentos de modo incremental nas tarefas autorizadas; nao animar/redesenhar telas aprovadas em massa.

### Contrato de listas e carregamento

Cada tipo de lista compartilhada define aparencia E comportamento, independentemente dos dados/colunas do modulo. Registrar no catalogo e implementar no dono comum:

- densidade: fonte/peso/entrelinha, altura ou altura minima de cabecalho/linha, padding de celulas, espaco entre colunas, bordas, selecao, selos, icones e acoes; usar a [ficha de densidade](../../templates/PADRAO_VISUAL.md#densidade-de-listas-e-tabelas), distinguindo altura declarada de altura efetiva;
- entrada inicial: gatilho da consulta, prioridade de dados, indicador pertinente e termino em resultado/erro; nunca mostrar "vazio" antes da resposta;
- atualizacao com dados ja visiveis: indicador sem apagar contexto/foco, tratamento de dados anteriores e estado confirmado;
- busca, filtros e ordenacao: gatilho, atraso quando necessario, combinacao/reset e tratamento de respostas fora de ordem; valores concretos pertencem ao projeto;
- paginacao ou outro modo de navegacao aprovado: posicao, tamanho/contagem quando disponiveis, mudanca de pagina e ajuste apos exclusao;
- estados distintos: sem registros, sem resultado do filtro, erro com nova tentativa, indisponivel/sem permissao conforme contrato; erro nunca vira lista vazia silenciosa;
- apos criar/editar/excluir: atualizacao/invalidation pertinente, preservacao ou reset deliberado de filtros, ordem, pagina, selecao, rolagem e retorno de foco;
- desktop/mobile: apresentacoes e acesso as mesmas tarefas, preservacao do contexto na troca e variantes aprovadas.

Consumidor informa contratos de dados, colunas, rotulos e acoes permitidas; isso nao autoriza reinventar carregamento, botao, fonte ou espacamento. Diferenca funcional necessaria (por exemplo atualizacao continua em painel operacional) precisa de variante/contrato documentado e justificativa, nao flags contraditorias numa lista universal. Infraestrutura de consultas pode variar por fonte/volume, preservando o comportamento aprovado; registrar limitacoes e nao prometer que padronizar UI torna APIs identicas. Conferir as [prioridades de abertura](../../references/DADOS.md#prioridade-de-abertura-badges-e-alertas) quando houver dados reais.

## 4. Peculiaridade protegida, clara na propria tela

Padrao aprovado e obrigatorio, salvo excecao explicitamente aprovada. Se criar/alterar a excecao ja foi expressamente pedido, informar diferenca/motivo e executar nesse alcance. Excecao adicional nao pedida exige apresentar diferenca, motivo, alcance e impacto e obter autorizacao antes dessa parte. Preservar o aprovado fora da mudanca autorizada; peculiaridade registrada torna a protecao mais precisa, mas ausencia de marca especial nao autoriza reorganizar o existente. Uma peculiaridade nao vira padrao global sem decisao separada.

### Edicao pontual e previa quando necessaria

Adicionar, retirar ou ajustar um elemento nao autoriza mudar outros elementos aprovados. Conferir a tela atual e os consumidores de CSS/componentes compartilhados; descrever em frase curta exatamente o que muda, sem chamar um deslocamento de "pequeno" para dispensar aprovacao.

Pedido direto claro segue `especificar` e o ambiente de `prototipo-real`: construir imediatamente no alcance pedido, testar, abrir a implementacao e pedir confirmacao visual depois. Nao exigir imagem ou uma segunda autorizacao do entendimento para iniciar essa construcao.

Previa em imagem e opcional quando solicitada pelo responsavel ou quando uma decisao visual indispensavel permanece ausente. Nesse caso, partir da captura atual ou briefing, identificar origem/proposta e resolver somente essa escolha antes da parte dependente. Nao transformar uma edicao pontual definida em rodada obrigatoria de imagem/aprovacao. Pedido somente de ideias/previa nao autoriza construir.

A apresentacao e confirmacao da implementacao da secao 6 continuam obrigatorias, mesmo sem previa. Sem navegador/screenshot, pode construir o recorte independente autorizado, mas registrar IMPLEMENTADO_NAO_APRESENTADO/BLOQUEADO e explicar o limite; nunca fingir apresentacao ou aceite. Preservar edicoes nao salvas e nao criar outra aba por rotina. Imagem gerada continua sendo proposta, nao screenshot real nem autorizacao de construir/publicar no real.

Depois da edicao, confrontar o recorte com a referencia anterior e conferir as propriedades que deveriam permanecer. Mudanca fora do pedido e regressao a corrigir, nao melhoria presumida; nao alterar a referencia apenas para aceitar o desvio.

No mapa canonico da tela/componente, registrar: identificador estavel, escopo nominal (tela/aba/elemento e desktop/mobile), propriedades/comportamentos que diferem, referencia base, motivo conhecido, aprovador/fonte do pedido, revisao e limite de alteracao. Pedido expresso sem motivo adicional recebe "pedido expresso do responsavel; motivo adicional nao informado". Nunca inventar a justificativa ou dizer "a pedido" sem evidencia. Nao copiar esse cadastro manualmente para varios arquivos.

Excecao sobrepoe SOMENTE as propriedades e os modos nomeados; todo o restante continua herdando o padrao. Classificar diferencas como PADRAO_BASE, VARIANTE_APROVADA, CONFIGURACAO_PERMITIDA, EXCECAO_A_PEDIDO ou DIVERGENCIA_NAO_ESCLARECIDA. Dados, colunas e textos previstos pelo contrato sao configuracao permitida; desktop/mobile aprovados sao variantes. Diferenca sem origem comprovada nao e excecao aprovada. Cada consumidor aponta a classificacao e o dono, sem duplicar valores.

Quando houver peculiaridade, a propria tela deve permitir identifica-la: indicador discreto "Padrao especial aprovado" com detalhes, pelo mecanismo de administracao/revisao apropriado. Visibilidade respeita permissoes; usuario operacional nao precisa ver metadados tecnicos. Nao criar nova configuracao/toggle somente para esta finalidade se ja ha modo de revisao.

Indicador e verificacao consomem a mesma fonte canonica ou projecao derivada; nunca duas listas manuais. A implementacao concreta do indicador exige alcance de UI autorizado; escrever esta skill nao o instala nos projetos.

Diferenca antiga sem registro: investigar; se origem/intentionalidade continuar incerta, perguntar antes de uniformizar a parte. Mudanca em token/componente compartilhado que atinja propriedade protegida exige aprovacao desse impacto. Correcao que nao toca a propriedade protegida nao exige nova aprovacao da tela inteira; o trecho efetivamente alterado continua sujeito a secao 6. Excecao nao desliga seguranca nem criterios de acessibilidade aplicaveis.

## 5. Migracao e verificacao visual

Padronizacao ampla autorizada: varrer todos os modulos/rotas/telas/modais e consumidores reais do escopo, incluindo estilos inline, tokens, componentes, variantes, estados e chamadas/carregamentos. Confrontar busca no codigo, documentos e renderizacao quando acessivel; busca textual sozinha nao prova comportamento nem ausencia de uso dinamico. Inventario usa dono existente, com local/DNA, peca/revisao, implementacao, modo, classificacao da secao 4, diferenca concreta, origem e cobertura. Inacessivel fica NAO_VERIFICADO.

A referencia explicitamente escolhida rege os equivalentes compativeis; a mais frequente nao vira padrao automaticamente. Manter DE/PARA e lotes de migracao com dependencias e preservacao. Alcance global ja autorizado dispensa repetir autorizacao de construcao por consumidor/lote; apresentar os resultados e obter aceite conforme secao 6. Divergencia de origem incerta e excecao protegida seguem secao 4. Pedido local permanece limitado a sua cadeia.

Depois da migracao, repetir a busca pelos usos atingidos para localizar copias, overrides e fontes paralelas; reconciliar codigo/documentacao e retirar somente residuos comprovados e autorizados. Distinguir encontrado, implementado, verificado, apresentado e aprovado por consumidor/modo. Nao declarar sistema inteiro padronizado por alterar um CSS, nem certificar locais nao conferidos. O fiscal confronta esta cobertura com o diff real conforme `verificar`.

Para o recorte e consumidores afetados:
1. Renderizar no navegador; comparar com referencia aprovada identificada por fonte/revisao, no mesmo viewport, zoom, tema, fontes carregadas, dados e estados controlados. Conferir a instancia/rota efetiva; nao comparar duas imagens de origens desconhecidas.
2. Confrontar matriz e medidas pertinentes: valor esperado/origem, computado/caixa real, delta e classificacao. Conferir tipografia, densidade, botoes/icones, espacamentos entre regioes e bordas, campos, tabelas, modais e estados. Pedido de largura confere explicitamente os invariantes preservados; diferenca por dado/rotulo longo nao vira mudanca de densidade por inferencia.
3. Exercitar tarefa principal, teclado/foco, mobile e desktop, pouco/muito conteudo e rotulos longos; zoom e demais cenarios conforme efeito.
4. Verificar console/rede e ligar falha a causa, sem registrar segredos. Distinguir erro introduzido de problema preexistente; ambos relevantes devem ser declarados.
5. Usar testes visuais/funcionais ja disponiveis. Adicionar a menor verificacao repetivel pertinente; novo runner apenas se necessario e autorizado.

Mudanca compartilhada exige avaliar todos os consumidores atingidos e testar cobertura justificada; amostra nao autoriza afirmar que todos foram executados. Screenshot comparativo prova diferenca visual, nao utilidade nem integracao. Nao atualizar baseline so para passar; exigir correspondencia com a decisao aprovada. A apresentacao para aceite cobre cada local alterado conforme a secao 6; amostragem tecnica nao dispensa esse aceite individual.

Falha corrigivel no alcance -> corrigir -> renderizar/testar de novo. Sem navegador, acesso ou referencia, informar impedimento e nao declarar aceite visual. A skill define o procedimento; nao e um fiscal automatico de pixels nem garantia de superioridade a outra ferramenta.

## 6. Fila de construcao e confirmacao visual obrigatoria

Esta secao e a fonte dona da fila e da confirmacao visual em PROTOTIPO e REAL. Autorizacao para construir, verificacao tecnica, apresentacao e aprovacao do resultado sao estados distintos. Nao aprovar regra, tela ou modal porque o codigo existe. Somente confirmacao explicita do responsavel aprova a revisao apresentada; silencio, novo pedido e mudanca de assunto nunca aprovam. Esta regra substitui o antigo fluxo de nao criar pendencia e de autorizacao por continuidade.

### Registrar e delimitar antes de construir

Registrar cada pedido antes da escrita no andamento/fila existente. Perguntas abertas, tarefas de construcao e confirmacoes pendentes seguem exclusivamente a [pasta temp](../construir/SKILL.md#pasta-temp-de-perguntas-e-fila-temporarias), sem fila em documento de tela/modulo versionado. Definicao visual expressa entra imediatamente no dono pelo [registro progressivo](#registro-progressivo-das-decisoes-visuais); a fila aponta para ID/revisao, sem duplicar a regra. Persistir transicoes e preservar o aberto; chat/memoria nao sao a unica copia. Reutilizar IDs/DNAs de tela/modal, sem criar painel, banco ou sistema de aprovacao paralelo.

O pedido guarda finalidade/motivo, solicitacao, plano PROTOTIPO/REAL, ambiente/local exato (rota/tela/aba/modal/elemento), revisao base, revisao em analise, dependencias, itens de impacto, status, referencia da evidencia visual, pergunta efetivamente enviada e resposta explicita do responsavel. Pergunta e resposta guardam texto e origem/data disponiveis, vinculados ao pedido/item e a revisao apresentada; ausencia fica registrada como pendencia, nunca preenchida por inferencia. Cada local/estado alterado e um item filho identificavel do mesmo pedido. Uma funcao em varias telas nao recebe aceite em bloco por aprovar so uma delas. O registro aponta para a regra no dono; nao a duplica.

Para proposta de capacidade/fluxo ou redesenho, apresentar **Entendimento** (ate tres linhas), **Mapa em arvore** (fluxo em texto normal) e **Impacto** (I001, I002 etc.). O mapa usa o fluxo conferido no sistema, com botoes, condicoes e consequencias; exemplo nao conferido e ilustrativo. Cada impacto informa ADICIONAR/ALTERAR/REMOVER/MOVER/PRESERVAR, elemento/local, antes -> depois, motivo e efeito nas regras/conexoes. Pedido direto segue a execucao de `especificar`; previa solicitada/decisao visual ausente segue a secao 4, sem entrevista ampla. Ligar os identificadores de impacto aos itens da fila e preserva-los nas correcoes.

Somente para proposta solicitada ou decisao indispensavel, encerrar com "Confirma que entendi corretamente e posso construir dessa forma?". Nunca usar essa pergunta para interromper pedido direto claro. Nao repetir autorizacao do mesmo escopo ja explicitamente dada. Isso autoriza construir a revisao, nao aprova o resultado ainda nao mostrado. Ambiente omitido segue PROTOTIPO conforme `prototipo-real`; contradicao concreta bloqueia apenas a parte dependente, sem trocar ambiente por silencio.

Antes de modificar local FORA do alcance ja autorizado, inclusive consumidor compartilhado, perguntar: "Esse pedido tambem afeta [tela/modal/local]: [alteracao e motivo]. Deseja que eu altere la tambem?". Locais nomeados ou abrangidos por padronizacao global expressa dos equivalentes entram em construcao. Consumidor equivalente descoberto depois continua coberto por esse alcance; efeito adicional nao abrangido volta a autorizacao. Nao repetir essa pergunta por tela quando o responsavel ja autorizou a migracao global. Registrar o local adicional como AGUARDANDO_AUTORIZACAO_DE_ESCOPO; construir o trecho independente do local pedido enquanto aguarda. Se impossivel isolar, bloquear somente a dependencia, sem duplicar o componente para contornar. Nao aproveitar o pedido para redesenhar o restante, adicionar campos/regras ou recuperar elementos descartados.

### Mostrar uma tela ou modal por vez

Fluxo por item: REGISTRADO -> EM_CONSTRUCAO_PROTO (ou EM_CONSTRUCAO no real expressamente pedido) -> IMPLEMENTADO_NAO_APRESENTADO -> AGUARDANDO_CONFIRMACAO_VISUAL -> APROVADO. Correcao usa EM_REVISAO e repete apresentacao; impedimento usa BLOQUEADO com motivo. Adiamento, cancelamento ou substituicao exigem decisao do responsavel e nao contam como aprovacao.

Depois de implementar, verificar e passar pela [revisao dos plugins de design](#plugins-de-design-na-construcao-e-revisao) quando instalados, salvar a fonte e abrir a rota/aba/selecao correta na mesma aba acessivel ao responsavel, sem perder edicoes nao salvas. Abrir o modal quando a mudanca estiver nele e posicionar o elemento visivelmente. Confirmar que a revisao servida e a atual. URL enviada ou navegador oculto nao comprovam que o usuario viu a tela.

Capturar e apresentar screenshot REAL da implementacao de cada tela/modal/estado alterado, com pedido/item, local, revisao e descricao do delta. Mostrar antes/depois quando necessario para entender movimento/remocao. Usar destino de evidencia ja previsto, dados controlados e nenhuma credencial/dado privado em print ou Git. Imagem gerada e previa, nunca screenshot de implementacao. Captura nao substitui testes de clique, regra, acesso ou persistencia.

Perguntar somente sobre o item ativo: "Pedido [ID], item [n/N]: na [tela/modal], fiz [alteracao] para [motivo]. Esta bom assim? Confirma esta versao?". Manter a tela e a evidencia correspondentes a essa pergunta. Sem possibilidade de abrir a pagina para o usuario, informar o limite; o print real pode ser o meio de revisao se ele aceitar explicitamente esse meio. Sem evidencia visual real disponivel, manter IMPLEMENTADO_NAO_APRESENTADO/BLOQUEADO, nunca inventar apresentacao ou aceite.

### Confirmacao obrigatoria e conducao da fila

Aguardar a resposta. "Sim", "esta bom", "aprovado", "beleza" ou equivalente inequivoco aprova somente o item ativo e a revisao exibida. Resposta ambigua exige esclarecer esse item. Nao usar autorizacao de construir como resposta de aceite, nem aprovar outros itens com a mesma resposta.

Sem confirmacao, manter AGUARDANDO_CONFIRMACAO_VISUAL e retomar a pergunta especifica na proxima interacao pertinente. O ciclo e mostrar -> perguntar -> aguardar -> corrigir quando pedido -> mostrar novamente -> confirmar. Nao enviar perguntas repetidas sem nova interacao, simular execucao em segundo plano ou insistir apos adiamento/cancelamento explicito. Pode registrar novos pedidos, mas eles nao encerram, apagam ou aprovam a pendencia anterior. Uma pergunta de aceite por vez; o usuario pode mudar a ordem ou adiar explicitamente.

Confirmou: registrar evidencia/resposta/revisao no dono, salvar a decisao vigente e conduzir imediatamente ao proximo item pendente, abrindo seu local e apresentando o respectivo print. Nao encerrar com "feito" quando ainda houver locais a conferir nem esperar que o usuario descubra as outras telas. Se interromper, persistir o item atual, a ordem restante e o impedimento; retomar desse ponto na proxima execucao, sem afirmar trabalho assincrono.

Correcao mantem o mesmo pedido/item, atualiza a candidata/revisao e sua evidencia, e exige nova apresentacao/pergunta/aceite do trecho atingido, preservando o restante aprovado. Alteracao posterior que atinja trecho ja aprovado reabre somente o aceite afetado e invalida seu screenshot anterior. Uma tela aprovada nao aprova a regra inteira: o pedido pai so fica aprovado quando todos os locais/estados afetados aplicaveis tiverem aceite da revisao atual e os checks pertinentes passarem. Para commit/push, seguir o contador e a selecao de lote de `construir`.

### Trava de encerramento da revisao visual

Antes de declarar uma revisao visual entregue, concluida ou aprovada, encerrar seu pedido/item por conclusao/aprovacao, retirar sua pendencia da fila como entregue ou conta-lo no lote elegivel para publicacao, conferir a cadeia abaixo no registro existente contra as evidencias originais. Status APROVADO escrito pelo executor, tabela preenchida ou resumo do construtor nao substituem essa conferencia. Adiamento, cancelamento ou substituicao expressos seguem o registro da decisao do responsavel, sem exigir aceite do resultado abandonado nem contar como aprovacao/elegibilidade.

| Conferencia | Evidencia exigida para o mesmo pedido/item e candidata |
|---|---|
| Identidade | ID do pedido/item, local/estado alterado e referencia verificavel da revisao apresentada, correspondente ao resultado que se pretende fechar. |
| Apresentacao | Tela/aba/modal correto aberto no ambiente de revisao autorizado e acessivel ao responsavel, com a revisao servida conferida; meio alternativo somente nas condicoes de print real aceito previstas acima. |
| Renderizacao | Verificacao do resultado renderizado e evidencia visual real apresentada daquele local/estado; codigo salvo, URL ou captura de outra revisao nao bastam. |
| Pergunta enviada | Texto da pergunta de aceite efetivamente enviado ao responsavel, com origem/data disponiveis e vinculo ao item/revisao. Rascunho, frase somente no arquivo, promessa de perguntar ou status de espera nao comprovam envio. |
| Resposta recebida | Resposta original, explicita e inequivoca do responsavel sobre a revisao apresentada, com texto e origem/data disponiveis. Autorizacao de construir, aprovacao de uma definicao visual, teste aprovado, silencio ou resposta sobre outro item/revisao/ambiente nao aprovam esse resultado. |

Usar link/ID da mensagem ou evento quando disponivel; caso a superficie nao os forneca, registrar o trecho original com origem/contexto e data disponiveis que permitam localizar a interacao. Nao inventar identificadores, datas, autoria, envio ou resposta; evidencia inacessivel/insuficiente permanece nao verificada. Reutilizar a fila e o destino canonico previstos, sem criar certificado, sistema de aprovacao ou segunda copia da regra.

Se a pergunta foi pulada ou nao ha evidencia de envio, reabrir o mesmo local na candidata correta, verificar/apresentar a alteracao e enviar de fato, na conversa, a pergunta pronta de "Mostrar uma tela ou modal por vez" antes de encerrar o turno. Registrar so a intencao de perguntar nao repara a omissao. Se acesso ou evidencia visual impedirem a apresentacao, declarar o limite e manter IMPLEMENTADO_NAO_APRESENTADO/BLOQUEADO; nao inventar que a pergunta visual foi cumprida.

Com apresentacao e pergunta comprovadas, mas sem resposta, manter AGUARDANDO_CONFIRMACAO_VISUAL. E permitido terminar o turno informando "Implementado e apresentado; aguardando confirmacao visual", preservando a fila; nao declarar entrega concluida, promover para publicacao ou contar esse pedido como aprovado. Nao repetir a pergunta sem nova interacao nem bloquear trabalho independente ja autorizado. Correcao do responsavel segue o mesmo pedido/item e o ciclo de nova candidata acima, sem usar o aceite anterior para o trecho modificado.

Somente a cadeia completa permite registrar o aceite e seguir ao fechamento, ainda sujeito aos demais checks e autorizacoes. Aceite valido ja comprovado para o mesmo resultado nao exige nova pergunta. Antes de fechar o pedido pai, conferir todos os itens aplicaveis; uma resposta nao libera outras telas/estados. Salvar a fonte autorizada e informar andamento continuam permitidos. NAO_SE_APLICA requer ausencia de efeito visual no recorte, nunca falta de resposta. Esta trava define o dever do executor e do fiscal; nao afirma instalar bloqueio mecanico no cliente.

### Mudanca de ideia e fonte vigente

Quando um novo pedido mudar local/escopo anterior, recuperar a decisao vigente e perguntar sobre o delta ainda nao decidido: "Voce havia pedido em [locais X/Y]. Agora pediu [Z]. E para remover de X/Y tambem ou manter?". Nao repetir o que a ordem atual ja decidiu expressamente; nao remover nem duplicar por inferencia. Inclusoes e remocoes autorizadas entram como itens relacionados e sao apresentadas nos respectivos locais. Pedido cancelado/substituido nao reaparece como tarefa ativa.

A revisao aprovada substitui a especificacao anterior do trecho no mesmo dono/DNA; uma unica definicao vigente por tela/modal. Revisao em construcao permanece candidata, separada do estado aprovado; salvar a fonte local nao autoriza promove-la ao real. Historico fica no Git para desfazer/restaurar explicitamente, nunca para reconstruir automaticamente o que foi descartado. Restauracao e nova revisao sujeita a impacto, verificacao e confirmacao, sem apagar decisoes posteriores ou trabalho alheio.

Adocao sobre trabalho existente: alteracao sem evidencia de aprovacao fica PENDENTE_DE_REVISAO, nao aprovada retroativamente; preservar codigo/trabalho alheio, mapear o recorte e apresentar. Apos conversao autorizada, retirar apenas o prototipo efetivamente substituido conforme `prototipo-real`; uma nova prototipacao parte do real atual, nunca de copias antigas.

A aprovacao visual nao substitui teste nem autoriza publicacao, mudanca de permissao ou banco. Promocao a padrao global segue a decisao expressa e o alcance registrados na secao 1; aceite local sozinho nao basta. Registrar fatos tecnicos e propostas e permitido; so a escolha expressa aprova a definicao e so o aceite da revisao apresentada aprova o resultado visual. Uma regra de posicao ja escolhida nao aguarda a construcao para ser salva nem aprova a tela futura. Documentacao e evidencias usam os donos existentes; esta skill nao instala fila executavel, hook ou bloqueio mecanico no cliente.

## Conexoes funcionais no alcance autorizado

A fila visual cobre os locais realmente afetados e autorizados da cadeia; cada tela/modal/estado exige screenshot real e confirmacao propria. Outra tela aprovada permanece intacta; ausencia de navegador nao autoriza prova inventada. Fonte dona: [conexoes funcionais e rastreabilidade bidirecional](../../references/DOCUMENTACAO.md#conexoes-funcionais-e-rastreabilidade-bidirecional), incluindo estados, auditoria seletiva e cenarios de aceite; nao duplicar esse esquema aqui.

## Paridade e concorrencia

Na revisao entre IAs, aplicar [instancia e fonte ativa verificaveis](../prototipo-real/SKILL.md#instancia-e-fonte-ativa-verificaveis): screenshot/identidade e aceite de cada estado, sem recuperar modal antigo por cache/overlay. Preservar candidato pendente; aprovar um item nao aprova outros.
