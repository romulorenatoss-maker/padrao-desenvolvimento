# Dados e migrations

Frontend apresenta; backend decide efeitos oficiais; banco protege integridade.

Migration nasce somente quando a mudanca persistente exige. Migration publicada nao e reescrita; evolucao posterior e forward.

Antes de transformacao destrutiva: identificar conjunto, consumidores/constraints, preservacao ou transformacao, recuperacao, autorizacao e verificacao.

Nao usar TRUNCATE, CASCADE, exclusao em massa ou remocao de coluna/tabela como atalho generico.

Ensaiar transformacao destrutiva no ambiente permitido antes do oficial. Nao aplicar SQL produtivo manualmente para contornar instrumento ausente. Reuso de schema existente nao cria migration artificial.

## Acesso ao banco: somente pela persistencia do modulo

Consulta, comando SQL, RPC ou chamada ao cliente do banco ficam somente na camada de persistencia do modulo dono (repository, DAO, gateway ou equivalente idiomatico da stack). Service/regra decide e chama a persistencia; view, controller/action, job, rota e frontend nunca acessam o banco diretamente. Outro modulo le ou grava pelo contrato publico do dono, nunca pela tabela interna.

Para dar velocidade: um metodo por pergunta/efeito de negocio, nomeado pela tarefa (`listarAbertosDoCliente`, `registrarBaixa`), reutilizado pelas proximas telas; sem repository generico, query builder proprio, ORM ou framework novo. Filtro de tenant/empresa e permissao de dado ficam no metodo, nao repetidos em cada chamador.

Trava proporcional: o check local barra acesso ao banco fora da persistencia somente nos arquivos novos ou alterados do lote; legado nao bloqueia a entrega do dia e a contagem fora do lugar so pode cair. Lote que altera arquivo legado move o acesso que tocou; o restante sai em lotes por modulo, com teste da cadeia no ambiente de ensaio. Mover consulta preserva filtros, ordem, tipos, transacao e tratamento de erro.

## Contrato da migration

Toda migration nasce com:
1. identificador ordenado unico no instrumento vigente; numero repetido ou reservado por outro executor e bloqueio;
2. conferencia pos-aplicacao que devolve verdadeiro/falso e prova o efeito (objeto criado, coluna/constraint presente, dado transformado);
3. sem controle de transacao proprio quando o aplicador ja envolve a migration em transacao; operacao que nao roda em transacao e declarada como tal;
4. reversao correspondente no destino de rollback, ou declaracao `IRREVERSIVEL` com motivo, copia/backup exigido antes e caminho de recuperacao.

Check de formato roda antes de aplicar, no executor local e no CI quando houver; fora do contrato nao e aplicada. Aplicar, conferir e registrar o resultado sao uma unica operacao do instrumento; conferencia falsa interrompe e reverte quando possivel. Migration publicada nao e reescrita: correcao e nova migration. Para velocidade, o projeto mantem um modelo preenchivel e o check acusa erro antes do ensaio, nao no deploy.

## Prototipo x real nos dados

PROTOTIPO: nao cria migration, SQL, tabela ou chamada ao banco oficial. Dados vem de simulacao isolada com os mesmos metodos previstos da persistencia (assinatura e formato de retorno), e o documento dono registra o modelo previsto: tabela/entidade, campos com tipo/obrigatoriedade, origem, constraints e metodo que le/grava. Esse registro e o desenho do banco aprovado junto da tela.

REAL: na ordem de construir, a persistencia real implementa os mesmos metodos e substitui a simulacao sem mudar a tela; a migration nasce do modelo registrado (todos os campos aprovados), e ensaiada com dados controlados, conferida e so entao aplicada no oficial com autorizacao. Divergencia entre modelo previsto e necessidade real volta ao documento dono antes da migration.

## Perfil local de dados

Cada projeto com banco declara no seu destino canonico de arquitetura/processos, uma vez: instrumento e pasta das migrations, pasta/convencao do rollback, formato da conferencia, aplicador e comando do check de formato, nome da camada de persistencia, comando da trava de acesso ao banco e ambiente de ensaio. O padrao define o contrato; o perfil local define a sintaxe. Sem banco: NAO_SE_APLICA declarado. Sem perfil: criar o perfil antes da primeira migration ou trava, sem inventar instrumento paralelo ao existente.

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
