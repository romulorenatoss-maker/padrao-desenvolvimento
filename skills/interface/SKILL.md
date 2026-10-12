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

Padrao aprovado e obrigatorio, salvo excecao explicitamente aprovada. Antes de CRIAR ou ALTERAR uma excecao, apresentar o que difere, motivo, alcance e impacto, e pedir aprovacao. Preservar o aprovado fora da mudanca autorizada; peculiaridade registrada torna a protecao mais precisa, mas ausencia de marca especial nao autoriza reorganizar o existente. Uma peculiaridade nao vira padrao global sem decisao separada.

### Edicao pontual e previa em imagem por padrao

Adicionar, retirar ou ajustar um elemento nao autoriza mudar outros elementos aprovados. Conferir a tela atual e os consumidores de CSS/componentes compartilhados; descrever em frase curta exatamente o que muda, sem chamar um deslocamento de "pequeno" para dispensar aprovacao.

Qualquer criacao ou alteracao com diferenca visual exige, por padrao, uma imagem da proposta ANTES de editar a interface: posicao, ordem, lista, fonte, cor, tamanho, espacamento ou apresentacao. Partir de captura da tela existente e identificar sua origem real ou prototipo; nunca chamar a captura do prototipo de producao. Sem tela existente, usar o briefing e marcar a proposta como tela nova. Nao alterar a tela em uso nem seus dados para produzir essa imagem.

Mostrar a imagem e o efeito proposto; pedidos de ajuste atualizam a imagem, ate aprovacao explicita da revisao. So entao construir fielmente no prototipo, atualizar a mesma aba visivel e comparar o renderizado com a proposta. Preservar edicoes nao salvas; outra aba somente se pedida pelo responsavel. Imagem aprovada autoriza esse visual no prototipo, nao regra de negocio, banco, construcao real ou publicacao. Silencio nao aprova; aprovacao de outra revisao nao cobre mudancas posteriores.

Dispensar a imagem somente quando o responsavel pedir explicitamente edicao direta, "sem previa", ou desligar esse comportamento; respeitar o alcance dessa escolha e manter as outras protecoes. Alteracao exclusivamente interna, sem diferenca visual, nao exige imagem. Falta da ferramenta/captura necessaria e impedimento a declarar, nao permissao para editar primeiro. Preferir uma previa focada; nao prometer economia de creditos ou rapidez so por gerar imagem.

Depois da edicao, confrontar o recorte com a referencia anterior e conferir as propriedades que deveriam permanecer. Mudanca fora do pedido e regressao a corrigir, nao melhoria presumida; nao alterar a referencia apenas para aceitar o desvio.

No mapa canonico da tela/componente, registrar: identificador estavel existente ou minimo necessario, escopo nominal (tela/aba/elemento), propriedade/comportamento protegido, motivo, referencia base, aprovador/fonte, revisao e limite de alteracao. Nao copiar esse cadastro manualmente para varios arquivos.

Quando houver peculiaridade, a propria tela deve permitir identifica-la: indicador discreto "Padrao especial aprovado" com detalhes, pelo mecanismo de administracao/revisao apropriado. Visibilidade respeita permissoes; usuario operacional nao precisa ver metadados tecnicos. Nao criar nova configuracao/toggle somente para esta finalidade se ja ha modo de revisao.

Indicador e verificacao consomem a mesma fonte canonica ou projecao derivada; nunca duas listas manuais. A implementacao concreta do indicador exige alcance de UI autorizado; escrever esta skill nao o instala nos projetos.

Diferenca antiga sem registro: investigar; se origem/intentionalidade continuar incerta, perguntar antes de uniformizar a parte. Mudanca em token/componente compartilhado que atinja propriedade protegida exige aprovacao desse impacto. Correcao que nao toca a propriedade protegida nao exige nova aprovacao da tela inteira. Excecao nao desliga seguranca nem criterios de acessibilidade aplicaveis.

## 5. Migracao e verificacao visual

Padronizacao ampla autorizada: inventariar telas e consumidores reais, classificar conforme/desvio/peculiaridade/nao verificado, aprovar referencia e lotes; migrar de forma coerente. Nao declarar sistema inteiro padronizado por alterar um CSS. Pedido local: limitar a cadeia, salvo dependencia compartilhada comprovada.

Para o recorte e consumidores afetados:
1. Renderizar no navegador; comparar com referencia aprovada no mesmo viewport, tema e dados controlados.
2. Conferir hierarquia, densidade, fontes, botoes, dimensoes reais de icones, espacamentos, alinhamento, campos, tabelas, modais e estados aplicaveis.
3. Exercitar tarefa principal, teclado/foco, mobile e desktop, pouco/muito conteudo e rotulos longos; zoom e demais cenarios conforme efeito.
4. Verificar console/rede e ligar falha a causa, sem registrar segredos. Distinguir erro introduzido de problema preexistente; ambos relevantes devem ser declarados.
5. Usar testes visuais/funcionais ja disponiveis. Adicionar a menor verificacao repetivel pertinente; novo runner apenas se necessario e autorizado.

Mudanca compartilhada exige avaliar todos os consumidores atingidos e testar cobertura justificada; amostra nao autoriza afirmar que todos foram executados. Screenshot comparativo prova diferenca visual, nao utilidade nem integracao. Nao atualizar baseline so para passar; exigir correspondencia com a decisao aprovada.

Falha corrigivel no alcance -> corrigir -> renderizar/testar de novo. Sem navegador, acesso ou referencia, informar impedimento e nao declarar aceite visual. A skill define o procedimento; nao e um fiscal automatico de pixels nem garantia de superioridade a outra ferramenta.

## 6. Confirmar entendimento sem criar pendencia por silencio

1. Para proposta de capacidade/fluxo ou redesenho, apresentar nesta ordem, com os titulos em negrito: **Entendimento** (no maximo tres linhas curtas confirmando o pedido), **Mapa em árvore** (fluxo em texto normal) e **Impacto** (itens I001., I002. e assim por diante). Edicao pontual/acrescimo que exige alterar layout ja aprovado usa a pergunta curta da secao 4, sem repetir esse formato amplo; a autorizacao do efeito colateral continua obrigatoria. O mapa nao usa tabela, bloco de codigo ou lousa: item/pergunta principal centralizado, linhas e ramificacoes para esquerda e direita, botoes, condicoes Sim/Nao e consequencias. Usar o fluxo conferido no sistema; exemplo nao conferido deve ser identificado como ilustrativo.

   O impacto vem da investigacao da tela e da cadeia existente em `especificar`, incluindo finalidade anterior e decisoes vigentes, nunca apenas do que o botao aparenta fazer. Cada item ocupa uma linha curta: numero, ADICIONAR/ALTERAR/REMOVER/MOVER/PRESERVAR, elemento e local, antes -> depois, motivo e efeito nas regras ou conexoes atingidas. Separar efeitos diferentes em itens distintos; cobrir todas as consequencias comprovadas do recorte, incluindo a regra relacionada que precisa continuar e por que. Nao inventar impacto ou afirmar leitura de elo nao conferido.

   Na remocao, explicitar se a funcao deixa de existir ou onde continua e o destino dos seus gatilhos/copias; esconder o botao nao equivale a remover. Limpeza obrigatoria retira codigo e registros exclusivos que ficaram sem consumidor, preservando funcoes compartilhadas ainda usadas. Nao acrescentar um resumo generico de limpeza. Os numeros identificam os itens desta proposta, nao criam identidades tecnicas nem fila de pendencias; mante-los nas revisoes para o responsavel pedir "desfazer I003" ou corrigir aquele entendimento. Rever efeitos dependentes antes de desfazer, preservando decisoes posteriores e trabalho alheio.

   Encerrar com "Confirma que entendi corretamente e posso construir dessa forma?"; essa pergunta confirma entendimento, mapa e impacto e autoriza a proposta apresentada, nao pede certificacao tecnica. Perguntar antes somente decisoes indispensaveis ausentes, conforme `especificar`. Nao repetir confirmacao de proposta ja autorizada.
2. Nao criar acao, pergunta aberta, estado "aguardando resposta" ou pendencia documental apenas porque o responsavel nao respondeu ao "esta bom". Ao receber outro assunto, seguir esse pedido; nao insistir na pergunta anterior nem tratar o silencio como aceite registrado.
3. O responsavel define PROTOTIPO ou REAL quando mandar construir. Se a instrucao ou contexto ja definir o alvo, executar sem repetir a pergunta; se houver duvida concreta entre prototipar para ver e ajustar o real, perguntar onde antes da escrita dependente. Preservar a autorizacao ja dada; ausencia de resposta nao autoriza trocar o alvo, ampliar escopo ou publicar.
4. Pedido de correcao ou de construcao explicito: executar no alcance definido, testar e mostrar o resultado, sem exigir nova confirmacao da mesma decisao.
5. Registrar no destino canonico somente decisoes efetivamente dadas, trabalho tecnico realizado e pendencias reais. Nao registrar como acao a pergunta de satisfacao nem inventar uma resposta. Funcionamento e publicacao sao sustentados por evidencias do executor.
6. Decisao indispensavel ausente ou autorizacao especifica continua sendo perguntada; seu alcance dependente nao e decidido por silencio. Conferencias e testes tecnicos cabem ao executor.

Na revisao iterativa de prototipo, seguir o fluxo de entrega visual e autorizacao documental de [prototipo-real](../prototipo-real/SKILL.md#revisao-rapida-do-prototipo-e-documentacao-paralela). Essa autorizacao documental nao equivale a aceite funcional nem construcao/publicacao real.
