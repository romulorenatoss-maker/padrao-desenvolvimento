---
name: romulo-interface
description: "Use em toda criacao, alteracao, correcao ou revisao com efeito visual ou interativo: telas, abas, botoes, icones, formularios, tabelas, CSS, tokens, componentes, navegacao e prototipos. Aplique a referencia aprovada, preserve peculiaridades e verifique a tela renderizada, sem inventar elementos ou estilos."
---

# Romulo Interface

Fonte dona da consistencia visual, composicao e peculiaridades. Use com `romulo-especificar` para proposta/utilidade, `romulo-construir` para conexoes e `romulo-verificar` para evidencias. Nao exige React, Tailwind, biblioteca ou estrutura de pastas especifica.

## 1. Descobrir e aprovar a referencia

Antes de editar, localizar sistema visual real: tokens/tema, componentes, layouts, exemplos aprovados, formatos, estados e peculiaridades do recorte. Inspecionar a renderizacao existente quando o ambiente permitir; sem navegador, declarar a verificacao visual nao executada, nao inventar screenshot.

Consultar o briefing visual do projeto conforme [contratos de projeto](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao): cores, letras, botoes, cantos, espacamentos e variantes aprovadas com valores/referencias concretos. Tela nova reutiliza esse contrato; alteracao consulta somente o trecho pertinente. Se faltar, propor o recorte necessario antes da UI definitiva. Briefing novo nao autoriza uniformizar telas antigas nem remover peculiaridades aprovadas; divergencias seguem a migracao e aprovacao das secoes 4 e 5.

O estilo mais repetido nao e necessariamente o melhor nem o aprovado. Em sistema inconsistente, propor uma referencia representativa na tecnologia existente e apresenta-la para aprovacao antes de espalhar alteracoes. Uma referencia util mostra formulario, tabela, botoes, abas/modal quando pertinentes e estados reais, nao apenas uma imagem decorativa.

Padrao GLOBAL significa identidade compartilhada dentro daquele projeto, nao mesma marca/aparencia em todos os projetos. Padroes por tarefa (lista, detalhe, formulario, operacao) podem compor o mesmo sistema. Excecao e desvio da referencia aprovada, nao variacao de layout ja prevista.

Sem referencia suficiente: apresentar proposta visual do recorte, aprovar e implementar so os tokens/componentes necessarios. Nao construir catalogo inteiro para uma unica funcao. Com referencia aprovada: reutilizar, sem reabrir perguntas resolvidas.

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

Use o contrato de utilidade de `romulo-especificar`. Rotulo diz a acao/resultado, nao "Clique aqui". Hierarquia reflete importancia, nao decoracao. Agrupe acoes secundarias sem esconder a essencial; mantenha destrutivas distintas. Nao fabrique botoes para preencher cards.

Use semantica nativa correta: link para destino, botao para acao, submit no formulario, controles de aba apropriados. Nome acessivel para acao so com icone; tooltip sozinho nao substitui. Preserve teclado, foco visivel, labels e anuncio de erro/resultado pertinentes.

Estado indisponivel explica o motivo quando necessario; nao e justificativa para entregar funcao ainda nao implementada. Loading nao pode ficar infinito; falha permite recuperacao e preserva dados digitados. Bloquear duplo clique na UI nao substitui integridade/idempotencia no servidor quando aplicavel.

Nao padronizar apenas classes: verificar tamanho computado/renderizado do icone, botao, texto, espaçamento, area clicavel e alinhamento. Tokens ajudam, mas nao garantem contraste, modo escuro ou acessibilidade automaticamente. Adote as metas de acessibilidade do projeto; avalie operacao por teclado, zoom e tecnologias assistivas conforme risco, combinando automacao e revisao manual.

## Estados de carregamento e movimento com finalidade

Toda interface criada/alterada trata os estados pertinentes; reutilizar o componente existente e registrar a aplicacao no documento dono. Skeleton cabe no conteudo assincrono ainda desconhecido, preservando dimensoes/foco e sem esconder dados ja conhecidos; operacao instantanea nao precisa de skeleton artificial. Lazy loading cabe em imagens/conteudo secundario pesado, nunca atrasa controles, alertas ou informacao essenciais. Carregamento termina em sucesso/erro recuperavel, preserva entradas e impede envio duplicado.

Progresso determinado usa medicao real; sem total conhecido, usar indicador indeterminado, nunca percentual inventado. Comando enviado nao e estado confirmado nem tarefa concluida. Animacao de entrada/saida ou troca de estado deve explicar a mudanca sem atrasar clique, teclado ou operacao frequente. Respeitar `prefers-reduced-motion`, sem perder a informacao/atencao do alerta. Nao colocar spinner, skeleton, fade ou hover em todo elemento por rotina.

Para criar ou revisar movimento, consultar `romulo-motion-principles`; carregar somente o workflow e referencias pertinentes ao recorte. A skill inclui o pacote completo importado, mas este padrao define preservacao, escopo, arquitetura e autorizacao. CSS/JavaScript nativos em projetos PHP puro; exemplo React/Framer Motion nao permite framework novo. Aplicar novos estados/movimentos de modo incremental nas tarefas autorizadas; nao animar/redesenhar telas aprovadas em massa.

## 4. Peculiaridade protegida, clara na propria tela

Padrao aprovado e obrigatorio, salvo excecao explicitamente aprovada. Antes de CRIAR ou ALTERAR uma excecao, apresentar o que difere, motivo, alcance e impacto, e pedir aprovacao. Preservar o aprovado fora da mudanca autorizada; peculiaridade registrada torna a protecao mais precisa, mas ausencia de marca especial nao autoriza reorganizar o existente. Uma peculiaridade nao vira padrao global sem decisao separada.

### Edicao pontual e acrescimo sem reorganizar o aprovado

Adicionar botao/campo ou corrigir funcao nao autoriza mudar posicao, ordem, dimensoes, cor, animacao ou comportamento de outros elementos. Conferir o recorte atual e efeitos de CSS/componentes compartilhados antes de editar. Se o pedido cabe sem alterar o existente aprovado, executar dentro da autorizacao vigente, sem pergunta artificial.

Nao usar "pequeno", "pouco" ou um limite de pixels para dispensar essa conferencia/aprovacao: ate uma linha deslocada e mudanca do existente. Dizer qual elemento muda e de onde para onde; informar medida quando efetivamente conferida no mesmo viewport/estado, sem estimar como fato. Variacoes dinamicas/responsivas ja previstas pelo contrato nao sao uma nova alteracao de layout por si.

Se para atender ao pedido precisar reduzir, deslocar ou alterar algo ja aprovado, parar antes dessa mudanca e fazer uma pergunta curta que diga exatamente o impacto real: "Para encaixar X, preciso reduzir Y e mover Z para cima. Quer ver a previa?" Usar os nomes reais e somente efeitos comprovados; nao substituir por "vou melhorar o layout" nem apresentar proposta gigante por esse ajuste. Autorizacao de acrescentar X nao aprova esses efeitos colaterais.

Se o responsavel pedir imagem, mostrar como ficaria em previa separada, preservando a tela/edicao aprovada; identificar que e proposta, nao entrega aplicada. So mexer no layout existente depois da aprovacao daquele impacto/previa; silencio nao aprova. Aprovacao explicita que ja inclua esses movimentos nao e perguntada novamente. Sem conseguir produzir a previa solicitada, declarar o impedimento e manter o layout atual.

Quando o responsavel definir que precisa VER a proposta antes de qualquer mudanca no layout existente, a previa visual anterior passa a ser obrigatoria para esse trabalho, mesmo que o deslocamento pareca minimo. A pergunta curta inicia essa proposta; nao equivale a permissao para editar a tela aprovada enquanto prepara a imagem.

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

   O impacto vem da investigacao da tela e da cadeia existente em `romulo-especificar`, incluindo finalidade anterior e decisoes vigentes, nunca apenas do que o botao aparenta fazer. Cada item ocupa uma linha curta: numero, ADICIONAR/ALTERAR/REMOVER/MOVER/PRESERVAR, elemento e local, antes -> depois, motivo e efeito nas regras ou conexoes atingidas. Separar efeitos diferentes em itens distintos; cobrir todas as consequencias comprovadas do recorte, incluindo a regra relacionada que precisa continuar e por que. Nao inventar impacto ou afirmar leitura de elo nao conferido.

   Na remocao, explicitar se a funcao deixa de existir ou onde continua e o destino dos seus gatilhos/copias; esconder o botao nao equivale a remover. Limpeza obrigatoria retira codigo e registros exclusivos que ficaram sem consumidor, preservando funcoes compartilhadas ainda usadas. Nao acrescentar um resumo generico de limpeza. Os numeros identificam os itens desta proposta, nao criam identidades tecnicas nem fila de pendencias; mante-los nas revisoes para o responsavel pedir "desfazer I003" ou corrigir aquele entendimento. Rever efeitos dependentes antes de desfazer, preservando decisoes posteriores e trabalho alheio.

   Encerrar com "Confirma que entendi corretamente e posso construir dessa forma?"; essa pergunta confirma entendimento, mapa e impacto e autoriza a proposta apresentada, nao pede certificacao tecnica. Perguntar antes somente decisoes indispensaveis ausentes, conforme `romulo-especificar`. Nao repetir confirmacao de proposta ja autorizada.
2. Nao criar acao, pergunta aberta, estado "aguardando resposta" ou pendencia documental apenas porque o responsavel nao respondeu ao "esta bom". Ao receber outro assunto, seguir esse pedido; nao insistir na pergunta anterior nem tratar o silencio como aceite registrado.
3. O responsavel define PROTOTIPO ou REAL quando mandar construir. Se a instrucao ou contexto ja definir o alvo, executar sem repetir a pergunta; se houver duvida concreta entre prototipar para ver e ajustar o real, perguntar onde antes da escrita dependente. Preservar a autorizacao ja dada; ausencia de resposta nao autoriza trocar o alvo, ampliar escopo ou publicar.
4. Pedido de correcao ou de construcao explicito: executar no alcance definido, testar e mostrar o resultado, sem exigir nova confirmacao da mesma decisao.
5. Registrar no destino canonico somente decisoes efetivamente dadas, trabalho tecnico realizado e pendencias reais. Nao registrar como acao a pergunta de satisfacao nem inventar uma resposta. Funcionamento e publicacao sao sustentados por evidencias do executor.
6. Decisao indispensavel ausente ou autorizacao especifica continua sendo perguntada; seu alcance dependente nao e decidido por silencio. Conferencias e testes tecnicos cabem ao executor.

Na revisao iterativa de prototipo, seguir o fluxo de entrega visual e autorizacao documental de [romulo-prototipo-real](../romulo-prototipo-real/SKILL.md#revisao-rapida-do-prototipo-e-documentacao-paralela). Essa autorizacao documental nao equivale a aceite funcional nem construcao/publicacao real.
