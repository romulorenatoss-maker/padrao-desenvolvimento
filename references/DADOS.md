# Dados e migrations

Frontend apresenta; backend decide efeitos oficiais; banco protege integridade.

Migration nasce somente quando a mudanca persistente exige. Migration publicada nao e reescrita; evolucao posterior e forward.

Antes de transformacao destrutiva: identificar conjunto, consumidores/constraints, preservacao ou transformacao, recuperacao, autorizacao e verificacao.

Nao usar TRUNCATE, CASCADE, exclusao em massa ou remocao de coluna/tabela como atalho generico.
