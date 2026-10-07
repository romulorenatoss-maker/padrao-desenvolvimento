# Documentacao — destinos e criacao minima

A skill dona e `romulo-documentacao`. Descobrir destinos canonicos antes de criar. Preservar nomes/IDs/vinculos corretos; fallback so quando nao existir equivalente. Sumario aponta, documento dono explica; nao copiar narrativa em cada consumidor.

## Fallback para projeto sem documentacao adequada
| Necessidade real | Destino padrao | Conteudo minimo |
|---|---|---|
| Entrada geral | `docs/SUMARIO.md` | Finalidade/stack em resumo, modulos reais e links para donos; sem catalogo de skills central. |
| Entrada do modulo | `docs/modulos/<modulo>/SUMARIO.md` | Capacidades, telas, dados, contratos e consumidores existentes; somente links que resolvem. |
| Motivo/limites de modulo | `docs/modulos/<modulo>/PORQUE.md` | Quando a justificativa/relacoes excederem o sumario: dono, limites, USA/USADO_POR, decisoes. Nao criar texto vazio. |
| Reconstrucao | `docs/modulos/<modulo>/RECONSTRUCAO.md` | Criar quando necessaria reproducao/reconstrucao: ordem, dependencias, configuracao e verificacao sem segredos. |
| Tela/aba | `docs/modulos/<modulo>/telas/<tela>.md` | Tarefa, entrada, elementos/acoes, estados, regra/contrato, referencia visual, peculiaridades e aceite. Agrupar abas relacionadas. |
| Cadeia funcional | `docs/modulos/<modulo>/cadeias/<capacidade>.md` | Entrada -> regra/autorizacao -> contrato/dado -> efeito/consumidores -> erros/testes. |
| Dados/contrato/acesso | `dados/<entidade>.md`, `contratos/<contrato>.md`, `seguranca/<capacidade>.md` no modulo | Somente quando houver responsabilidade distinta; caso pequeno cabe no mapa da capacidade. |
| Processo transversal local | `docs/architecture/processos/<processo>.md` | Guardas, autorizações ou procedimento ESPECIFICOS ao projeto; nao copiar diretrizes centrais. |
| Historico de lote | `docs/changes/ALTERACOES.md` | Quando exigido pelo fechamento: escopo/revisao, alteracoes, fontes e evidencias, sem certificado paralelo. |
| Inventario | `docs/architecture/INVENTARIO.jsonl` | Apenas quando instrumento local o exigir/consumir; nao criar cadastro manual universal por rotina. |

Todos os subdiretorios sao relativos ao modulo real; criar somente com documento util. Projeto com convencao equivalente nao recebe copia desta arvore. Documento por responsabilidade, nao por arquivo, funcao, botao, elemento decorativo ou execucao.

## Enxugar AGENTS/CLAUDE existentes sem perder regras
Classificar cada trecho: identidade/ponte/protecao curta -> AGENTS; metodo global -> referencia central vigente; regra de negocio/guarda/peculiaridade local -> dono documental existente. Destino local faltante usa a tabela acima se a migracao estiver autorizada. Registrar DE/PARA no registro canonico do lote, criar/validar destino e link antes de retirar texto da origem.

Protecao nao desaparece nem e enfraquecida por mudanca de lugar. Link de protecao deve ser leitura obrigatoria antes da escrita, inclusive por outros agentes. Se qualquer destino estiver indefinido, sem acesso ou ainda nao validado, preservar o trecho original. Nao substituir AGENTS protegido sem autorizacao especifica; mover seu conteudo tambem e alteracao. CLAUDE.md novo e ponte, nao copia de regras.

Proibidos como atalhos: PLANO.md, FINAL.md, V2.md, notas de agente, resumo/memoria paralela e backups documentais. Excecao nao prevista so pelo gate `0393`, sem contornar proibicao local explicita. Historico fica no Git; o estado atual necessario fica no dono canonico.
