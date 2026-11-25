# Modelo de padrao visual e de comportamento do projeto

Usar para completar catalogo/briefing equivalente, conforme [DOCUMENTACAO](../references/DOCUMENTACAO.md#padroes-locais-preenchiveis) e [interface](../skills/interface/SKILL.md#catalogo-local-e-promocao-de-uma-peca). Sem equivalente, destino: `docs/architecture/componentes/sistema.padrao_visual.md`. Resolver links no destino; nao copiar valores de outro projeto nem salvar placeholders como fatos.

## Identidade e fontes

Registrar projeto, dono do briefing/identidade, implementacao comum, sumario e revisao conferida. Valor tem um dono: se paleta/tipografia ja vivem no briefing ou tokens, referencia-los aqui. Preservar IDs e pecas parciais existentes. Este modelo define o que decidir; nao e uma colecao de escolhas previamente aprovadas.

## Matriz de cobertura

Preencher progressivamente ID/link dono, estado da definicao e implementacao. Estados de definicao: A_DEFINIR, OBSERVADO, PROPOSTO, APROVADO ou NAO_APLICAVEL justificado. Estado da definicao nao substitui cobertura dos consumidores. A matriz nao guarda perguntas abertas nem respostas a construir.

| Familia | Contrato a documentar conforme usada |
|---|---|
| Cores e tema | Papeis semanticos, valores/tokens, contraste, estados e temas adotados. |
| Letras e titulos | Familia, pesos, tamanhos, entrelinha; titulo de tela/secao, rotulos, texto e hierarquia. |
| Medidas e composicao | Alturas, espacamentos, densidade, largura, alinhamento, borda, raio, sombra e camadas. |
| Casca da tela | Esqueleto, topo, menu lateral, navegacao/retorno e composicoes por tarefa. |
| Abas e menus | Selecao, teclado, contexto e comportamento de menu de acoes, configuracao e ajuda. |
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
| Impressao | Ordem de carregamento, recibo, etiqueta, tamanho, cortes e dados pertinentes. |
| Movimento | Finalidade, duracao adotada, reducao de movimento e preservacao da operacao. |

Nao limitar a quantidade de pecas a esta tabela: cada responsabilidade reutilizavel necessaria ganha entrada; varias variantes podem pertencer a mesma peca. Familia nao usada nao exige implementacao futura.

## Ficha de peca

Repetir no dono somente para a peca realmente necessaria. Reutilizar ID existente; criar ID estavel conforme convencao local, nao um por pixel.

| Campo | Conteudo |
|---|---|
| Identidade | ID, nome, finalidade e quando usar/nao usar. |
| Definicao | Estado, origem da decisao, data e revisao aprovada; observado nao equivale a aprovado. |
| Contrato comum | Aparencia, medidas/tokens por referencia, conteudo permitido, semantica, acoes, estados e acessibilidade. |
| Desktop | Composicao, campos/acoes prioritarios e evidencia real da revisao. |
| Mobile | Composicao, acesso as tarefas e evidencia real da revisao; nao inferir do desktop. |
| Condicao de troca | Breakpoint/container/regra concretos da implementacao; larguras intermediarias pertinentes. |
| Implementacao | Arquivo, classe/simbolo/componente, fonte de estilo e controle de comportamento compartilhados. |
| Configuracao permitida | Dados, colunas, textos e acoes que consumidores podem informar sem criar outro padrao. |
| Variantes | Nome, condicao, propriedades diferentes e decisao; sem duplicar regra comum. |
| Consumidores | Rotas/telas/modais e DNAs/fontes reais, diretamente ou por mapa existente. |
| Excecoes | Links para excecoes nominais, propriedades protegidas e limites. |
| Evidencias | Referencia/revisao, estado implementado/verificado/apresentado/aprovado por modo/local. |
| Migracao | Alcance autorizado e cobertura factual; fila aberta permanece no mecanismo temporario previsto. |

Aprovacao de um exemplo como padrao nao prova que todos os consumidores ja usam a implementacao ou foram vistos pelo responsavel.

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

## Cobertura e conferencia

Usar mapa existente com consumidor/DNA, peca/revisao, modo, classificacao, diferenca, implementacao e evidencias. Separar encontrado, migrado, verificado, apresentado e aprovado; locais inacessiveis ficam NAO_VERIFICADO. Nao marcar sistema inteiro conforme por um teste ou por um componente atualizado.

O fiscal compara candidato, catalogo, implementacao comum, diferencas e consumidores reais em toda criacao/correcao. Falhas corrigiveis voltam a construcao; atualizacao da referencia para esconder desvio e invalida. Perguntas e confirmacoes abertas ficam somente na pasta temp de construir; decisoes construidas ficam no dono, com historico no Git.
