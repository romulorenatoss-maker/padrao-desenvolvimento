# Seguranca

Modelo base: negar por padrao e confiar somente em controles executados no servidor/infraestrutura apropriada.

Revalidar no backend autorizacao, escopo, propriedade e valores que produzem efeitos oficiais. Parametrizar SQL. Proteger segredos. Restringir uploads e integracoes. Usar transacoes/constraints para invariantes que precisam sobreviver a concorrencia.

A analise e proporcional ao risco. Nao inserir mecanismos sem ameaca ou requisito correspondente, mas nunca remover controle legitimo em nome de simplicidade.
