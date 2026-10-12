# Dados e migrations

Frontend apresenta; backend decide efeitos oficiais; banco protege integridade.

Migration nasce somente quando a mudanca persistente exige. Migration publicada nao e reescrita; evolucao posterior e forward.

Antes de transformacao destrutiva: identificar conjunto, consumidores/constraints, preservacao ou transformacao, recuperacao, autorizacao e verificacao.

Nao usar TRUNCATE, CASCADE, exclusao em massa ou remocao de coluna/tabela como atalho generico.

Ensaiar transformacao destrutiva no ambiente permitido antes do oficial. Nao aplicar SQL produtivo manualmente para contornar instrumento ausente. Reuso de schema existente nao cria migration artificial.

## Portabilidade e recuperacao

Preparar/migrar uma instancia, backup recuperavel ou contingencia Docker segue [backup-recuperacao](../skills/backup-recuperacao/SKILL.md), dono do setup, perfis compativeis, corte/restauracao/verificacao e recuperacao apos incidente. Perfil local preserva revisao/schema/contratos, integridade e acesso; nao supor que dump/replica ou troca de DATABASE_URL restaura todos os servicos.

## Arquivos e integracoes de armazenamento

A integracao dona define o perfil logico, provedor/endereco e adaptador backend; modulos consumidores usam seu contrato, nunca credenciais ou caminhos fisicos do fornecedor. Identidade persistente do arquivo e ID/chave relativa no perfil, vinculada a empresa/entidade e metadados necessarios, sem URL assinada/temporaria, segredo ou endereco absoluto como unica referencia. Backend resolve URL/acesso a partir do perfil vigente e revalida permissao/tenant. Banco guarda referencias; objetos externos precisam de copia propria.

Reutilizar convencao existente compativel. Quando ausente, chave privada estavel: `<tenant_id>/<modulo>/<entidade_id>/<arquivo_id>.<extensao_validada>`; adaptador pode mapear bucket/container/prefixo sem mudar identidade. Nome original e metadado, nao caminho confiavel; upload/tipo/tamanho e acesso seguem [seguranca](SEGURANCA.md). Declarar padrao e consumidores no dono de armazenamento/DNAs do projeto, sem inventar tabela/coluna/modulo ou reorganizar arquivos existentes por rotina.

Troca do perfil em Integracoes ou equivalente exige inventario de objetos e referencias, copia autorizada ao novo destino, confronto de quantidades/bytes/hashes e ensaio de leitura/upload/permissoes dos consumidores atingidos antes de ativar. Registros antigos com URL/endereco fisico exigem mapeamento explicito e migracao autorizada, nao substituicao cega de texto. Coordenar gravacoes em curso pelo perfil/corte adequado, preservar origem e retorno compativel; nao apagar originais antes da conferencia nem declarar que arrastar uma pasta moveu os metadados/RLS ou todos os dados.

## Desempenho
Revalidar no servidor preco, desconto, credito, pagamento, saldo, estoque, capacidade, propriedade e transicoes criticas.

Nao carregar cadastro/historico inteiro para pagina, resumo ou detalhe. Filtrar escopo e selecionar campos no backend; evitar `SELECT *` em listagens e consultas por linha quando lote resolve. Paginacao/limites no servidor; ordenacao dinamica por lista permitida. Calculo oficial tem dono, unidade, precisao e arredondamento.

Cache nao cria autorizacao nem confirma operacao. Nao persistir dado privado no navegador por conveniencia. Nao criar cache, fila, worker, indice ou infraestrutura para esconder desenho ruim.
