---
name: romulo-interface
description: "Use em toda criacao, alteracao, correcao ou revisao com efeito visual ou interativo: telas, abas, botoes, icones, formularios, tabelas, CSS, tokens, componentes, navegacao e prototipos. Aplique a referencia aprovada, preserve peculiaridades e verifique a tela renderizada, sem inventar elementos ou estilos."
---

# Romulo Interface

Fonte dona da consistencia visual, composicao e peculiaridades. Use com `romulo-especificar` para proposta/utilidade, `romulo-construir` para conexoes e `romulo-verificar` para evidencias. Nao exige React, Tailwind, biblioteca ou estrutura de pastas especifica.

## 1. Descobrir e aprovar a referencia

Antes de editar, localizar sistema visual real: tokens/tema, componentes, layouts, exemplos aprovados, formatos, estados e peculiaridades do recorte. Inspecionar a renderizacao existente quando o ambiente permitir; sem navegador, declarar a verificacao visual nao executada, nao inventar screenshot.

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

## 4. Peculiaridade protegida, clara na propria tela

Padrao aprovado e obrigatorio, salvo excecao explicitamente aprovada. Antes de CRIAR ou ALTERAR uma excecao, apresentar o que difere, motivo, alcance e impacto, e pedir aprovacao. Preservar somente o que foi protegido, nao congelar toda a tela por inferencia. Uma peculiaridade nao vira padrao global sem decisao separada.

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

## 6. Revisao com o responsavel, uma peca por vez

Quando o responsavel revisa telas/modais/funcoes, conduzir em etapas previsiveis:
1. Uma tela, modal ou funcao por vez. Antes de perguntar, abrir a tela no ambiente local/prototipo do projeto (copia do real), com a mudanca aplicada por cima da original, dados de exemplo criados pelo caminho real e o marcador de pendencia de publicacao do projeto. Tela nova aparece dentro da navegacao do sistema, nunca solta.
2. Resposta curta: o que mudou em uma a tres linhas e uma unica pergunta "Esta bom assim?". Nao listar outras perguntas, pendencias ou proximas etapas; elas ficam guardadas ate a vez delas.
3. Ajuste pedido: aplicar na mesma tela, recarregar e repetir a mesma pergunta. So avancar para a proxima peca depois do aceite explicito.
4. Comentario sobre outra tela no meio da revisao: confirmar em uma linha que foi anotado, registrar no registro canonico de perguntas do projeto com numero estavel, as palavras do responsavel e a tela/modulo, e voltar a pergunta atual. Se o comentario altera a peca em revisao, ajustar agora.
5. Quando chegar a vez do item da fila, abrir a tela e citar o pedido original ("Voce pediu: ...") antes da pergunta.
6. Aceite registrado: documentar a decisao no modulo/tela dono com `romulo-documentacao` e, no mesmo commit, tirar a pergunta do registro canonico de perguntas (ele guarda so as abertas). Enquanto nao estiver construida e publicada, ela fica no andamento/fila do projeto como "respondida, a construir"; ao construir, verificar e publicar, sai de la no mesmo lote (`romulo-construir`, limpeza dos registros de trabalho). Aceite visual de prototipo nao comprova integracao real.
