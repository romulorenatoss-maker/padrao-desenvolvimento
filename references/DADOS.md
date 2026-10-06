# Dados e migrations

Frontend apresenta; backend decide efeitos oficiais; banco protege integridade.

Migration nasce somente quando a mudanca persistente exige. Migration publicada nao e reescrita; evolucao posterior e forward.

Antes de transformacao destrutiva: identificar conjunto, consumidores/constraints, preservacao ou transformacao, recuperacao, autorizacao e verificacao.

Nao usar TRUNCATE, CASCADE, exclusao em massa ou remocao de coluna/tabela como atalho generico.

Ensaiar transformacao destrutiva no ambiente permitido antes do oficial. Nao aplicar SQL produtivo manualmente para contornar instrumento ausente. Reuso de schema existente nao cria migration artificial.

## Desempenho
Revalidar no servidor preco, desconto, credito, pagamento, saldo, estoque, capacidade, propriedade e transicoes criticas.

Nao carregar cadastro/historico inteiro para pagina, resumo ou detalhe. Filtrar escopo e selecionar campos no backend; evitar `SELECT *` em listagens e consultas por linha quando lote resolve. Paginacao/limites no servidor; ordenacao dinamica por lista permitida. Calculo oficial tem dono, unidade, precisao e arredondamento.

Cache nao cria autorizacao nem confirma operacao. Nao persistir dado privado no navegador por conveniencia. Nao criar cache, fila, worker, indice ou infraestrutura para esconder desenho ruim.
