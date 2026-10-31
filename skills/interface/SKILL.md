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

### Entrevista inicial e escolha de ferramentas

No inicio da primeira interface ou de um novo padrao visual solicitado, conferir o briefing existente e perguntar UMA decisao ausente por vez: usuario/tarefa e dispositivos; direcao e referencias; cores e tipografia; botoes, cantos, espacamentos/densidade; estados, movimento e peculiaridades protegidas. A ordem segue a lacuna real, nao um questionario fixo; neste fluxo, nao agrupar varias escolhas na mesma pergunta, mesmo se outro roteiro sugerir agrupa-las. Nao repetir respostas ja dadas nem entrevistar de novo por um bug ou edicao pontual.

Salvar cada decisao vigente no dono do briefing previsto em [documentacao](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao). Proposta recebe PROPOSTO; somente a escolha explicita vira APROVADO. Depois, telas e TELA.md consultam esse dono e suas excecoes, sem copiar outra especificacao visual. Valores concretos e referencia renderizada ligam a escolha aos tokens/componentes implementados; apenas dizer "bonito" ou citar uma skill nao define um padrao.

Escolher recursos pelo efeito: direcao estetica/colecao de DESIGN.md ajuda a propor; image-to-code exige alvo visual escolhido e ajuda a reproduzir; guidelines revisam acessibilidade/usabilidade/performance; navegador/Playwright conferem renderizacao e regressao, nao decidem gosto nem editam layout por si. Confirmar fonte, revisao, compatibilidade e ferramentas realmente disponiveis. Nenhum recurso externo autoriza framework, dependencia, instalacao, troca de fonte canonica ou reforma de tela aprovada.

Quando o responsavel pedir comparacao de abordagens, preparar previas isoladas da MESMA pagina, com mesmo conteudo, estados, viewport e alcance. Comparar hierarquia, legibilidade/contraste, densidade, acoes, responsividade e fidelidade; declarar o que foi realmente executado. Duas propostas do mesmo modelo com instrucoes diferentes nao sao um benchmark de dois executores independentes. Imagem gerada e proposta, nao prova de UI funcional; bloqueio de renderizacao nao vira PASSOU.

Escolha aprovada fixa a referencia daquele projeto. Novas telas reutilizam tokens/componentes; tela antiga muda somente no lote autorizado, preservando regras, DNAs e peculiaridades. Nao carregar varias skills de gosto simultaneamente como ordens concorrentes nem obrigar uma comparacao A/B a cada ajuste. Reusar verificacoes aprovadas; corrigir falha e retestar somente o efeito atingido.

## 2. Uma fonte implementada, varios consumidores

Buscar componente/token/variante antes de criar. Reutilizar; estender quando semanticamente compativel; criar somente responsabilidade distinta necessaria. Nao criar Botao2, copias de modal ou um componente unico com dezenas de flags contraditorias.

Similaridade exige investigar e reutilizar o equivalente compativel; nao exige perguntar novamente quando o pedido e a referencia ja determinam a escolha. Antes de construir qualquer tela, modal, lista, campo, menu ou acao, procurar no projeto o que ja faz algo parecido (mesmo assunto, mesmo tipo de dado, mesma acao: garantia, anexo, lancamento pai/filhos, valor em moeda, selecao em lista, cor de menu, forma de carregar) por nome, rota, classe e DNA. Se houver alternativas com diferenca indispensavel ainda nao decidida, perguntar somente essa escolha. Quando o equivalente ja atende ao pedido, reutilizar sem segunda autorizacao. A implementacao usa componente compartilhado (um arquivo, uma fonte de estilo) e cada tela so informa de onde le e onde grava. Reutilizacao nao autoriza alterar todos os consumidores: mapear cada local atingido, pedir autorizacao para os locais adicionais e obter a confirmacao visual individual conforme a secao 6. Se nao for possivel limitar o efeito ao alcance autorizado, bloquear a escrita dependente e explicar, sem duplicar o componente para contornar a decisao. Proibido copiar markup/CSS de outra tela, recriar uma variante "parecida" ou dar cor/letra/espacamento proprios a um elemento que ja tem padrao no projeto. Valor em moeda usa a mascara compartilhada do projeto; lista de lancamentos segue a tela de referencia aprovada.

| Parte | Contrato visual que deve vir da fonte aprovada |
|---|---|
| Tema e tipografia | Cores semanticas, contraste, hierarquia, fontes, formatos de data/moeda/unidade. |
| Layout | Densidade, largura, espacamento, alinhamento, breakpoints e composicoes por tarefa. |
| Botoes | Variantes semanticas, tamanhos, rotulo, icone, alinhamento e estados. |
| Icones | Familia coerente, dimensoes renderizadas e espessura; icone pequeno nao exige alvo clicavel pequeno. |
| Campos | Label, ajuda, obrigatoriedade, erro, altura, foco e estado de leitura. |
| Tabelas/listas | Densidade, colunas prioritarias, filtros/ordenacao/paginacao quando necessarios, conteudo longo e vazio. |
| Abas e navegacao | Selecao, contexto, teclado, URL/retorno quando pertinente; sem abas vazias. |
| Modal/drawer | Contexto, dimensoes, cabecalho, acoes, foco/retorno de foco e fechamento seguro. |
| Mensagens e estados | Carregando, vazio, erro recuperavel, sucesso, indisponivel e sem permissao quando aplicaveis. |
| Responsividade | Prioridade do conteudo, navegacao adaptada, reflow e overflow deliberado, sem ocultar tarefa essencial. |

Valores de identidade visual pertencem a tokens e componentes. CSS de composicao local pode existir, consumindo esses contratos sem redefinir arbitrariamente fontes, cores, botoes e medidas. Valores dinamicos de layout/graficos nao sao automaticamente violacao. Nao impor "zero CSS local" nem transformar toda variacao em token global.

Nao corrigir defeito local com seletor global abrangente, `!important` em cascata ou redefinicao de `svg`, `button`, `table` para todo o sistema. Causa compartilhada comprovada pode exigir correcao na fonte compartilhada, com impacto e consumidores verificados. Nunca trocar framework ou biblioteca de componentes so para padronizar.

## 3. Botoes com sentido e comportamento previsivel

Use o contrato de utilidade de `especificar`. Rotulo diz a acao/resultado, nao "Clique aqui". Hierarquia reflete importancia, nao decoracao. Agrupe acoes secundarias sem esconder a essencial; mantenha destrutivas distintas. Nao fabrique botoes para preencher cards.

Use semantica nativa correta: link para destino, botao para acao, submit no formulario, controles de aba apropriados. Nome acessivel para acao so com icone; tooltip sozinho nao substitui. Preserve teclado, foco visivel, labels e anuncio de erro/resultado pertinentes.

Estado indisponivel explica o motivo quando necessario; nao e justificativa para entregar funcao ainda nao implementada. Loading nao pode ficar infinito; falha permite recuperacao e preserva dados digitados. Bloquear duplo clique na UI nao substitui integridade/idempotencia no servidor quando aplicavel.

Nao padronizar apenas classes: verificar tamanho computado/renderizado do icone, botao, texto, espaçamento, area clicavel e alinhamento. Tokens ajudam, mas nao garantem contraste, modo escuro ou acessibilidade automaticamente. Adote as metas de acessibilidade do projeto; avalie operacao por teclado, zoom e tecnologias assistivas conforme risco, combinando automacao e revisao manual.

## Estados de carregamento e movimento com finalidade

Toda interface criada/alterada trata os estados pertinentes; reutilizar o componente existente e registrar a aplicacao no documento dono. Skeleton cabe no conteudo assincrono ainda desconhecido, preservando dimensoes/foco e sem esconder dados ja conhecidos; operacao instantanea nao precisa de skeleton artificial. Lazy loading cabe em imagens/conteudo secundario pesado, nunca atrasa controles, alertas ou informacao essenciais. Carregamento termina em sucesso/erro recuperavel, preserva entradas e impede envio duplicado.

Progresso determinado usa medicao real; sem total conhecido, usar indicador indeterminado, nunca percentual inventado. Comando enviado nao e estado confirmado nem tarefa concluida. Animacao de entrada/saida ou troca de estado deve explicar a mudanca sem atrasar clique, teclado ou operacao frequente. Respeitar `prefers-reduced-motion`, sem perder a informacao/atencao do alerta. Nao colocar spinner, skeleton, fade ou hover em todo elemento por rotina.

Para criar ou revisar movimento, consultar `motion-principles`; carregar somente o workflow e referencias pertinentes ao recorte. A skill inclui o pacote completo importado, mas este padrao define preservacao, escopo, arquitetura e autorizacao. CSS/JavaScript nativos em projetos PHP puro; exemplo React/Framer Motion nao permite framework novo. Aplicar novos estados/movimentos de modo incremental nas tarefas autorizadas; nao animar/redesenhar telas aprovadas em massa.

## 4. Peculiaridade protegida, clara na propria tela

Padrao aprovado e obrigatorio, salvo excecao explicitamente aprovada. Se criar/alterar a excecao ja foi expressamente pedido, informar diferenca/motivo e executar nesse alcance. Excecao adicional nao pedida exige apresentar diferenca, motivo, alcance e impacto e obter autorizacao antes dessa parte. Preservar o aprovado fora da mudanca autorizada; peculiaridade registrada torna a protecao mais precisa, mas ausencia de marca especial nao autoriza reorganizar o existente. Uma peculiaridade nao vira padrao global sem decisao separada.

### Edicao pontual e previa quando necessaria

Adicionar, retirar ou ajustar um elemento nao autoriza mudar outros elementos aprovados. Conferir a tela atual e os consumidores de CSS/componentes compartilhados; descrever em frase curta exatamente o que muda, sem chamar um deslocamento de "pequeno" para dispensar aprovacao.

Pedido direto claro segue `especificar` e o ambiente de `prototipo-real`: construir imediatamente no alcance pedido, testar, abrir a implementacao e pedir confirmacao visual depois. Nao exigir imagem ou uma segunda autorizacao do entendimento para iniciar essa construcao.

Previa em imagem e opcional quando solicitada pelo responsavel ou quando uma decisao visual indispensavel permanece ausente. Nesse caso, partir da captura atual ou briefing, identificar origem/proposta e resolver somente essa escolha antes da parte dependente. Nao transformar uma edicao pontual definida em rodada obrigatoria de imagem/aprovacao. Pedido somente de ideias/previa nao autoriza construir.

A apresentacao e confirmacao da implementacao da secao 6 continuam obrigatorias, mesmo sem previa. Sem navegador/screenshot, pode construir o recorte independente autorizado, mas registrar IMPLEMENTADO_NAO_APRESENTADO/BLOQUEADO e explicar o limite; nunca fingir apresentacao ou aceite. Preservar edicoes nao salvas e nao criar outra aba por rotina. Imagem gerada continua sendo proposta, nao screenshot real nem autorizacao de construir/publicar no real.

Depois da edicao, confrontar o recorte com a referencia anterior e conferir as propriedades que deveriam permanecer. Mudanca fora do pedido e regressao a corrigir, nao melhoria presumida; nao alterar a referencia apenas para aceitar o desvio.

No mapa canonico da tela/componente, registrar: identificador estavel existente ou minimo necessario, escopo nominal (tela/aba/elemento), propriedade/comportamento protegido, motivo, referencia base, aprovador/fonte, revisao e limite de alteracao. Nao copiar esse cadastro manualmente para varios arquivos.

Quando houver peculiaridade, a propria tela deve permitir identifica-la: indicador discreto "Padrao especial aprovado" com detalhes, pelo mecanismo de administracao/revisao apropriado. Visibilidade respeita permissoes; usuario operacional nao precisa ver metadados tecnicos. Nao criar nova configuracao/toggle somente para esta finalidade se ja ha modo de revisao.

Indicador e verificacao consomem a mesma fonte canonica ou projecao derivada; nunca duas listas manuais. A implementacao concreta do indicador exige alcance de UI autorizado; escrever esta skill nao o instala nos projetos.

Diferenca antiga sem registro: investigar; se origem/intentionalidade continuar incerta, perguntar antes de uniformizar a parte. Mudanca em token/componente compartilhado que atinja propriedade protegida exige aprovacao desse impacto. Correcao que nao toca a propriedade protegida nao exige nova aprovacao da tela inteira; o trecho efetivamente alterado continua sujeito a secao 6. Excecao nao desliga seguranca nem criterios de acessibilidade aplicaveis.

## 5. Migracao e verificacao visual

Padronizacao ampla autorizada: inventariar telas e consumidores reais, classificar conforme/desvio/peculiaridade/nao verificado, aprovar referencia e lotes; migrar de forma coerente. Nao declarar sistema inteiro padronizado por alterar um CSS. Pedido local: limitar a cadeia, salvo dependencia compartilhada comprovada e autorizada.

Para o recorte e consumidores afetados:
1. Renderizar no navegador; comparar com referencia aprovada no mesmo viewport, tema e dados controlados.
2. Conferir hierarquia, densidade, fontes, botoes, dimensoes reais de icones, espacamentos, alinhamento, campos, tabelas, modais e estados aplicaveis.
3. Exercitar tarefa principal, teclado/foco, mobile e desktop, pouco/muito conteudo e rotulos longos; zoom e demais cenarios conforme efeito.
4. Verificar console/rede e ligar falha a causa, sem registrar segredos. Distinguir erro introduzido de problema preexistente; ambos relevantes devem ser declarados.
5. Usar testes visuais/funcionais ja disponiveis. Adicionar a menor verificacao repetivel pertinente; novo runner apenas se necessario e autorizado.

Mudanca compartilhada exige avaliar todos os consumidores atingidos e testar cobertura justificada; amostra nao autoriza afirmar que todos foram executados. Screenshot comparativo prova diferenca visual, nao utilidade nem integracao. Nao atualizar baseline so para passar; exigir correspondencia com a decisao aprovada. A apresentacao para aceite cobre cada local alterado conforme a secao 6; amostragem tecnica nao dispensa esse aceite individual.

Falha corrigivel no alcance -> corrigir -> renderizar/testar de novo. Sem navegador, acesso ou referencia, informar impedimento e nao declarar aceite visual. A skill define o procedimento; nao e um fiscal automatico de pixels nem garantia de superioridade a outra ferramenta.

## 6. Fila de construcao e confirmacao visual obrigatoria

Esta secao e a fonte dona da fila e da confirmacao visual em PROTOTIPO e REAL. Autorizacao para construir, verificacao tecnica, apresentacao e aprovacao do resultado sao estados distintos. Nao aprovar regra, tela ou modal porque o codigo existe. Somente confirmacao explicita do responsavel aprova a revisao apresentada; silencio, novo pedido e mudanca de assunto nunca aprovam. Esta regra substitui o antigo fluxo de nao criar pendencia e de autorizacao por continuidade.

### Registrar e delimitar antes de construir

Registrar cada pedido antes da escrita no andamento/fila canonico ja existente. Na falta de fila separada, usar uma secao no documento dono existente, nao criar arquivo de memoria, modal de aprovacao, painel, banco ou sistema paralelo por rotina. Persistir o estado a cada transicao; chat e memoria do agente nao sao a unica copia. Reutilizar IDs/DNAs, inclusive a identidade propria de cada modal, sem criar outro modal ou copia por revisao.

O pedido guarda finalidade/motivo, solicitacao, plano PROTOTIPO/REAL, local exato (rota/tela/aba/modal/elemento), revisao base, revisao em analise, dependencias, itens de impacto, status, referencia da evidencia e resposta de aprovacao com data/origem. Cada local/estado alterado e um item filho identificavel do mesmo pedido. Uma funcao em varias telas nao recebe aceite em bloco por aprovar so uma delas. O registro aponta para a regra no dono; nao a duplica.

Para proposta de capacidade/fluxo ou redesenho, apresentar **Entendimento** (ate tres linhas), **Mapa em arvore** (fluxo em texto normal) e **Impacto** (I001, I002 etc.). O mapa usa o fluxo conferido no sistema, com botoes, condicoes e consequencias; exemplo nao conferido e ilustrativo. Cada impacto informa ADICIONAR/ALTERAR/REMOVER/MOVER/PRESERVAR, elemento/local, antes -> depois, motivo e efeito nas regras/conexoes. Pedido direto segue a execucao de `especificar`; previa solicitada/decisao visual ausente segue a secao 4, sem entrevista ampla. Ligar os identificadores de impacto aos itens da fila e preserva-los nas correcoes.

Somente para proposta solicitada ou decisao indispensavel, encerrar com "Confirma que entendi corretamente e posso construir dessa forma?". Nunca usar essa pergunta para interromper pedido direto claro. Nao repetir autorizacao do mesmo escopo ja explicitamente dada. Isso autoriza construir a revisao, nao aprova o resultado ainda nao mostrado. Ambiente omitido segue PROTOTIPO conforme `prototipo-real`; contradicao concreta bloqueia apenas a parte dependente, sem trocar ambiente por silencio.

Antes de modificar local adicional, inclusive consumidor de componente compartilhado ou tela fora da visualizacao atual, perguntar: "Esse pedido tambem afeta [tela/modal/local]: [alteracao e motivo]. Deseja que eu altere la tambem?". Somente locais expressamente autorizados entram em construcao. Impacto descoberto depois volta a essa autorizacao. Registrar o local adicional como AGUARDANDO_AUTORIZACAO_DE_ESCOPO; construir o trecho independente do local pedido enquanto aguarda. Se impossivel isolar, bloquear somente a dependencia, sem duplicar o componente para contornar. Nao aproveitar o pedido para redesenhar o restante, adicionar campos/regras ou recuperar elementos descartados.

### Mostrar uma tela ou modal por vez

Fluxo por item: REGISTRADO -> EM_CONSTRUCAO_PROTO (ou EM_CONSTRUCAO no real expressamente pedido) -> IMPLEMENTADO_NAO_APRESENTADO -> AGUARDANDO_CONFIRMACAO_VISUAL -> APROVADO. Correcao usa EM_REVISAO e repete apresentacao; impedimento usa BLOQUEADO com motivo. Adiamento, cancelamento ou substituicao exigem decisao do responsavel e nao contam como aprovacao.

Depois de implementar e verificar, salvar a fonte e abrir a rota/aba/selecao correta na mesma aba acessivel ao responsavel, sem perder edicoes nao salvas. Abrir o modal quando a mudanca estiver nele e posicionar o elemento visivelmente. Confirmar que a revisao servida e a atual. URL enviada ou navegador oculto nao comprovam que o usuario viu a tela.

Capturar e apresentar screenshot REAL da implementacao de cada tela/modal/estado alterado, com pedido/item, local, revisao e descricao do delta. Mostrar antes/depois quando necessario para entender movimento/remocao. Usar destino de evidencia ja previsto, dados controlados e nenhuma credencial/dado privado em print ou Git. Imagem gerada e previa, nunca screenshot de implementacao. Captura nao substitui testes de clique, regra, acesso ou persistencia.

Perguntar somente sobre o item ativo: "Pedido [ID], item [n/N]: na [tela/modal], fiz [alteracao] para [motivo]. Esta bom assim? Confirma esta versao?". Manter a tela e a evidencia correspondentes a essa pergunta. Sem possibilidade de abrir a pagina para o usuario, informar o limite; o print real pode ser o meio de revisao se ele aceitar explicitamente esse meio. Sem evidencia visual real disponivel, manter IMPLEMENTADO_NAO_APRESENTADO/BLOQUEADO, nunca inventar apresentacao ou aceite.

### Confirmacao obrigatoria e conducao da fila

Aguardar a resposta. "Sim", "esta bom", "aprovado", "beleza" ou equivalente inequivoco aprova somente o item ativo e a revisao exibida. Resposta ambigua exige esclarecer esse item. Nao usar autorizacao de construir como resposta de aceite, nem aprovar outros itens com a mesma resposta.

Sem confirmacao, manter AGUARDANDO_CONFIRMACAO_VISUAL e retomar a pergunta especifica na proxima interacao pertinente. O ciclo e mostrar -> perguntar -> aguardar -> corrigir quando pedido -> mostrar novamente -> confirmar. Nao enviar perguntas repetidas sem nova interacao, simular execucao em segundo plano ou insistir apos adiamento/cancelamento explicito. Pode registrar novos pedidos, mas eles nao encerram, apagam ou aprovam a pendencia anterior. Uma pergunta de aceite por vez; o usuario pode mudar a ordem ou adiar explicitamente.

Confirmou: registrar evidencia/resposta/revisao no dono, salvar a decisao vigente e conduzir imediatamente ao proximo item pendente, abrindo seu local e apresentando o respectivo print. Nao encerrar com "feito" quando ainda houver locais a conferir nem esperar que o usuario descubra as outras telas. Se interromper, persistir o item atual, a ordem restante e o impedimento; retomar desse ponto na proxima execucao, sem afirmar trabalho assincrono.

Correcao atualiza o mesmo item/revisao, preservando o restante aprovado. Alteracao posterior que atinja trecho ja aprovado reabre somente o aceite afetado e invalida seu screenshot anterior. Uma tela aprovada nao aprova a regra inteira: o pedido pai so fica aprovado quando todos os locais/estados afetados aplicaveis tiverem aceite da revisao atual e os checks pertinentes passarem. Para commit/push, seguir o contador e a selecao de lote de `construir`.

### Mudanca de ideia e fonte vigente

Quando um novo pedido mudar local/escopo anterior, recuperar a decisao vigente e perguntar sobre o delta ainda nao decidido: "Voce havia pedido em [locais X/Y]. Agora pediu [Z]. E para remover de X/Y tambem ou manter?". Nao repetir o que a ordem atual ja decidiu expressamente; nao remover nem duplicar por inferencia. Inclusoes e remocoes autorizadas entram como itens relacionados e sao apresentadas nos respectivos locais. Pedido cancelado/substituido nao reaparece como tarefa ativa.

A revisao aprovada substitui a especificacao anterior do trecho no mesmo dono/DNA; uma unica definicao vigente por tela/modal. Revisao em construcao permanece candidata, separada do estado aprovado; salvar a fonte local nao autoriza promove-la ao real. Historico fica no Git para desfazer/restaurar explicitamente, nunca para reconstruir automaticamente o que foi descartado. Restauracao e nova revisao sujeita a impacto, verificacao e confirmacao, sem apagar decisoes posteriores ou trabalho alheio.

Adocao sobre trabalho existente: alteracao sem evidencia de aprovacao fica PENDENTE_DE_REVISAO, nao aprovada retroativamente; preservar codigo/trabalho alheio, mapear o recorte e apresentar. Apos conversao autorizada, retirar apenas o prototipo efetivamente substituido conforme `prototipo-real`; uma nova prototipacao parte do real atual, nunca de copias antigas.

A aprovacao visual nao substitui teste nem autoriza publicacao, mudanca de permissao, banco ou promocao a padrao global. Registrar fatos tecnicos e propostas e permitido, mas nao marca-los como regras aprovadas antes deste aceite. Documentacao e evidencias usam os donos existentes; esta skill nao instala fila executavel, hook ou bloqueio mecanico no cliente.

## Conexoes funcionais no alcance autorizado

A fila visual cobre os locais realmente afetados e autorizados da cadeia; cada tela/modal/estado exige screenshot real e confirmacao propria. Outra tela aprovada permanece intacta; ausencia de navegador nao autoriza prova inventada. Fonte dona: [conexoes funcionais e rastreabilidade bidirecional](../../references/DOCUMENTACAO.md#conexoes-funcionais-e-rastreabilidade-bidirecional), incluindo estados, auditoria seletiva e cenarios de aceite; nao duplicar esse esquema aqui.

## Paridade e concorrencia

Na revisao entre IAs, aplicar [instancia e fonte ativa verificaveis](../prototipo-real/SKILL.md#instancia-e-fonte-ativa-verificaveis): screenshot/identidade e aceite de cada estado, sem recuperar modal antigo por cache/overlay. Preservar candidato pendente; aprovar um item nao aprova outros.
