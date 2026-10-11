# Documentacao — destinos e criacao minima

A skill dona e `romulo-documentacao`. Descobrir destinos canonicos antes de criar. Preservar nomes/IDs/vinculos corretos; fallback so quando nao existir equivalente. Sumario aponta, documento dono explica; nao copiar narrativa em cada consumidor.

## Fallback para projeto sem documentacao adequada
| Necessidade real | Destino padrao | Conteudo minimo |
|---|---|---|
| Entrada geral | `docs/SUMARIO.md` | Finalidade/stack em resumo, modulos reais e links para donos; sem catalogo de skills central. |
| Entrada do modulo | `docs/modulos/<modulo>/SUMARIO.md` | Capacidades, telas, dados, contratos e consumidores existentes; somente links que resolvem. |
| Motivo/limites de modulo | `docs/modulos/<modulo>/PORQUE.md` | Quando a justificativa/relacoes excederem o sumario: dono, limites, USA/USADO_POR, decisoes. Nao criar texto vazio. |
| Reconstrucao | `docs/modulos/<modulo>/RECONSTRUCAO.md` | Criar quando necessaria reproducao/reconstrucao: ordem, dependencias, configuracao e verificacao sem segredos. |
| Tela/aba | `docs/modulos/<modulo>/telas/<tela>.md` | Documento dono por pagina; reutilizar `telas/<tela>/TELA.md` quando essa convencao ja existir. Tarefa, rota/menu, abas, elementos/DNA, finalidade, origem/consumidores, regras/contratos, estados, peculiaridades e aceite. Resumo em duas linhas por comportamento e detalhes necessarios por referencia. Agrupar abas relacionadas. |
| Cadeia funcional | `docs/modulos/<modulo>/cadeias/<capacidade>.md` | Entrada -> regra/autorizacao -> contrato/dado -> efeito/consumidores -> erros/testes. |
| Dados/contrato/acesso | `dados/<entidade>.md`, `contratos/<contrato>.md`, `seguranca/<capacidade>.md` no modulo | Somente quando houver responsabilidade distinta; caso pequeno cabe no mapa da capacidade. |
| Processo transversal local | `docs/architecture/processos/<processo>.md` | Guardas, autorizações ou procedimento ESPECIFICOS ao projeto; nao copiar diretrizes centrais. |
| Historico de lote | `docs/changes/ALTERACOES.md` | Obrigatorio em toda entrega publicada, no mesmo commit: QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER (`romulo-construir`); sem certificado paralelo; respeitar o limite local de entradas e preservar as antigas no Git. |
| Inventario | `docs/architecture/INVENTARIO.jsonl` | Apenas quando instrumento local o exigir/consumir; nao criar cadastro manual universal por rotina. |

Todos os subdiretorios sao relativos ao modulo real; criar somente com documento util. Projeto com convencao equivalente nao recebe copia desta arvore. Documento por responsabilidade, nao por arquivo, funcao, botao, elemento decorativo ou execucao.

## Como escrever o documento da pagina (TELA.md ou equivalente)

Cabecalho minimo: identidade documental e dono existentes; nome/finalidade da pagina; rota, menu/submenu; estado PROTOTIPO/REAL e revisao das fontes. Agrupar abas/subabas e configuracoes no mesmo documento quando pertencem a essa pagina. Indicar os arquivos que a renderizam/interagem e as cadeias/contratos donos, sem listar arquivos sem relacao.

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
PREVISTO (quando houver): <ideia/conexao futura, finalidade e fonte; estado separado>
```

O bloco e um modelo de escrita, nao um formulario a repetir vazio: omitir campos NAO_SE_APLICA, integrar secoes/tabelas equivalentes existentes e tornar desconhecidos relevantes explicitos. Nao publicar placeholders como documentacao pronta. Mostrar condicoes exatas quando alteram comportamento; duas linhas resumem, nao substituem detalhes necessarios. As mesmas regras nao sao copiadas para cada item: usar link ao dono e registrar somente a aplicacao particular na pagina.

O detalhe funcional/tecnico da pagina solicitada fica no documento dela, ligado ao DNA do item e ao contrato dono. Quando recebe informacao de outra pagina, o documento da origem tambem explica por que cadastra/fornece essa informacao e aponta para o consumidor; o consumidor explica para que a usa e aponta para a origem. Por exemplo ilustrativo: Ativos/Estoque documenta identidade, disponibilidade e fornecimento do equipamento; Construtor documenta como esse vinculo habilita a maquina e referencia o contrato de entrada/saida. Cada lado descreve sua propria responsabilidade, com dados/arquivos/contratos pertinentes; nao copiar todo o detalhe do Construtor para Estoque nem atribuir regra de processamento ao cadastro de ativos. Consultar o vinculo nos dois sentidos antes de retirar qualquer ponta.

Intencoes futuras ainda sem pagina ficam em PREVISTO no dono atual/assunto do prototipo, com descricao rica suficiente para retomar e vinculo no sumario existente. Nao criar documento vazio da pagina futura. Ao surgir pedido relacionado, consultar e apresentar essa ideia antes de propor outra; manter exemplos/excecoes pertinentes nos detalhes e distinguir pedido humano de sugestao e de implementacao comprovada. Atualizar o mesmo item ao receber novas explicacoes, conforme `romulo-documentacao`.

Ao receber uma decisao, atualizar o item correspondente pelo ID. Ao mover, preservar identidade e ajustar LOCAL/rotas e links. Ao remover/alterar capacidade, conferir e atualizar os itens consumidores comprovadamente afetados, dizendo o novo destino e como a informacao continua (ou que interrupcao foi explicitamente aprovada). Mudanca apenas de aparencia nao presume alterar contrato. A manutencao e consulta seguem `romulo-documentacao` e `romulo-especificar`; nenhum documento passa a permitir uma regra de negocio nova por si.

## Enxugar AGENTS/CLAUDE existentes sem perder regras
Classificar cada trecho: identidade/ponte/protecao curta -> AGENTS; metodo global -> referencia central vigente; regra de negocio/guarda/peculiaridade local -> dono documental existente. Destino local faltante usa a tabela acima se a migracao estiver autorizada. Registrar DE/PARA no registro canonico do lote, criar/validar destino e link antes de retirar texto da origem.

Protecao nao desaparece nem e enfraquecida por mudanca de lugar. Link de protecao deve ser leitura obrigatoria antes da escrita, inclusive por outros agentes. Se qualquer destino estiver indefinido, sem acesso ou ainda nao validado, preservar o trecho original. Nao substituir AGENTS protegido sem autorizacao especifica; mover seu conteudo tambem e alteracao. CLAUDE.md novo e ponte, nao copia de regras.

Proibidos como atalhos: PLANO.md, FINAL.md, V2.md, notas de agente, resumo/memoria paralela e backups documentais. Excecao nao prevista so pelo gate `0393`, sem contornar proibicao local explicita. Historico fica no Git; o estado atual necessario fica no dono canonico.
