# Dados e migrations

Frontend apresenta; backend decide efeitos oficiais; banco protege integridade.

Migration nasce somente quando a mudanca persistente exige. Migration publicada nao e reescrita; evolucao posterior e forward.

Antes de transformacao destrutiva: identificar conjunto, consumidores/constraints, preservacao ou transformacao, recuperacao, autorizacao e verificacao, conforme [retirada segura](#retirada-segura-de-dados-e-modulos).

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

## Reutilizacao e propriedade de dados

Antes de criar tabela, coluna, relacionamento, JSON persistente ou copia de cadastro, identificar o fato de negocio, sua granularidade, identidade, cardinalidade, dono, escopo de acesso, ciclo de vida, consumidores e carga. Consultar schema e contratos existentes, alem da documentacao. Sem acesso ao banco ativo, separar definicao no repositorio de objeto efetivamente confirmado.

Registrar uma decisao por capacidade no dono existente: REUTILIZAR, ESTENDER, VINCULAR, SEPARAR, PRESERVAR_SNAPSHOT ou CRIAR_COM_JUSTIFICATIVA. Apontar alternativas existentes examinadas, motivo de descarte ou aproveitamento, consumidor real e teste. Nome diferente de tela/modulo nao justifica tabela nova; campos parecidos nao provam que duas entidades devam ser unificadas.

Reutilizar quando significado, identidade, ciclo e acesso forem compativeis. Estender para atributos da mesma entidade. Relacionar para papeis ou vinculos; materializar relacao quando a cardinalidade/integridade exigir. Separar quando regras, historia, permissao, volume ou ciclo de vida forem distintos. Manter snapshot deliberado quando representa o fato na epoca da operacao, com fonte/versao/finalidade e sem escrita concorrente sobre o cadastro atual.

O objetivo e o menor modelo coerente e verificavel, nao o menor numero absoluto de tabelas. Nao substituir modelagem por tabela universal tipo/id/valor, JSON sem contrato ou centenas de colunas opcionais. Nao criar uma tabela por tela nem uma tabela fisica por tipo de mensagem se o modelo de eventos existente cumprir o contrato.

Cada informacao possui um dono canonico de escrita, que pode ser definido por entidade ou grupo coeso de atributos. Outro modulo consulta ou solicita alteracao pelo contrato publico do dono. Origem da captura e consumidor nao se tornam donos por terem criado a primeira linha. A retirada do consumidor nao apaga automaticamente o dado compartilhado.

Distinguir identidade, papel de negocio, canal de contato e autenticacao. Pessoa/organizacao pode exercer mais de um papel; cliente ou lead nao implica conta de login. Telefone/e-mail iguais nao autorizam unir pessoas automaticamente. Aplicar regras de equivalencia e escopo comprovadas, com tratamento explicito de ambiguidades. Nao compartilhar dados pessoais entre empresas por deduplicacao global presumida.

Relacao que representa identidade ou dependencia deve ter integridade e concorrencia demonstraveis. Preferir FK/unique/check adequados quando compativeis com o modelo. Relacao polimorfica ou ID embutido em JSON exige garantia equivalente explicita; um campo tipo + id ou um UUID solto nao prova existencia, escopo ou exclusao segura. Documentar representacoes derivadas, dono, atualizacao e invalidacao.

Coluna nova so e suficiente quando representa atributo ou relacao compativel com a entidade e a cardinalidade. Havendo multiplos contatos/endereco com identidade propria e consumidores externos, avaliar relacao explicita. Nao afirmar que uma view de JSON fornece automaticamente FK para cada elemento interno.

## Retirada segura de dados e modulos

Diferenciar desabilitar recurso, retirar codigo, remover vinculo, excluir registro, expurgar conteudo, anonimizar e remover estrutura. Uma ordem nao autoriza as demais por inferencia. Remocao de modulo nao se transforma em DROP/TRUNCATE de tudo com seu prefixo.

Classificar dados no recorte como CADASTRO_CANONICO, VINCULO, OPERACIONAL_EXCLUSIVO, HISTORICO_SNAPSHOT, DERIVADO ou FINALIDADE_NAO_COMPROVADA. Nome fisico/prefixo/origem de criacao nao substitui essa classificacao.

Antes da exclusao, descobrir referencias concretas e consumidores de codigo: FKs/constraints, tabelas relacionais, JSON relevante, views, RPCs, triggers, jobs, filas, anexos, integracoes e trabalhos concorrentes. Diario de acesso ou contador de referencias em memoria nao e autoridade para apagar. Sem uso observado nao significa sem finalidade.

Excluir primeiro o vinculo no alcance autorizado quando essa for a intencao. Dado canonico ou compartilhado permanece enquanto houver referencia valida ou finalidade propria. Ausencia de ultimo consumidor nao basta para apagar cadastro independente, catalogo geografico ou historico necessario.

Exclusao fisica exige conjunto/escopo e autorizacao definidos, politica de retencao satisfeita, referencias relevantes verificadas, recuperacao pertinente e teste de nao impacto. Apresentar estimativa e o que sera preservado, removido, desvinculado ou bloqueado, sem expor dados pessoais desnecessarios.

A ausencia de referencias deve ser revalidada no momento da escrita, com integridade transacional e protocolo de concorrencia adequado. Nao executar contar -> aguardar -> apagar fora da protecao. FK e regras do dono devem impedir referencia orfa; se houver relacoes sem FK, todos os escritores precisam respeitar o mesmo mecanismo. Nao apagar quando essa garantia depender de suposicao.

Cascade somente para filhos de propriedade exclusiva no sentido adequado, conforme politica e testes. Nao usar cascata como maneira de desabilitar protecoes. Nao criar gatilho que apague entidade pai compartilhada quando remover filho operacional. Desligar constraints/triggers para forcar limpeza e proibido fora de procedimento excepcional explicitamente autorizado e verificado.

Objeto de Storage e seu registro SQL nao compoem automaticamente uma transacao unica. Exclusao de arquivo compartilhado exige verificar todos os vinculos, impedir corrida com novas associacoes e executar operacao idempotente com resultado/retentativa registrados. Reutilizar o mecanismo existente; nao remover objeto usado como comprovante de outro modulo.

Desativacao de modulo inclui seus workers, entradas, tarefas pendentes e retries, para nao recriar registros ou efetuar envios depois da retirada. Preservar dados e capacidades de outros dominios. Dependencia desconhecida bloqueia apenas a exclusao afetada, nao toda a analise.

## Perfil de comunicacao e chat

Acionar este perfil quando o pedido envolver mensagens, conversas, atendimento por canal, participantes, entregas, leituras, anexos ou automacao de comunicacao. O perfil define limites de propriedade; nao ordena instalar um chat completo nem uma stack nova.

Separar conceitualmente: (a) identidade/cadastro e seus contatos; (b) papeis e vinculos de negocio; (c) autenticacao; (d) atendimento/protocolo utilizado por operacoes; (e) conversa e participante do canal; (f) mensagens/eventos; (g) entregas, leituras, filas e estados temporarios; (h) anexos/objetos e suas referencias. Reutilizar a separacao fisica existente quando satisfizer esses limites.

Chat consome o cadastro canonico. Pode solicitar gravacao de telefone, e-mail ou endereco pelo contrato do dono, com permissao, empresa, finalidade, validacao e controle de concorrencia. A origem da informacao fica rastreavel, mas o dado confirmado nao depende de manter a mensagem ou o modulo de chat.

Dado extraido de texto/IA nao substitui cadastro confirmado automaticamente. Distinguir dado observado/proposto de alteracao autorizada. Nao fundir identidades por telefone/e-mail coincidente, nem converter todo participante anonimo em cliente ou conta de acesso. Tratamento de visitante/desconhecido deve reutilizar o modelo atual e sua politica de retencao.

Limpar conversa ou desativar chat preserva cliente/pessoa/contato e vinculos independentes, incluindo suas telas e contratos. Remover contato/identidade e operacao distinta. Atendimento utilizado por pedido/OS/financeiro nao e propriedade exclusiva do chat, ainda que esteja em pasta/tabela com nome de Central.

Mensagens e conteudo volumoso nao pertencem a linha do cliente. Projecoes/resumos podem apoiar listagem, desde que derivadas, limitadas, rastreaveis e invalidaveis. Expurgo deve considerar texto, anexos, entradas de provedor, tarefas, busca, resumo, cache e embeddings pertinentes, sem manter copias que reconstituam indevidamente conteudo removido. Nao apagar historico com finalidade independente sem politica propria.

Politica de retencao existente e preservada ate decisao explicita. Nao escolher numero de dias, expurgo total, anonimizacao ou armazenamento permanente por costume.

## Endereco, localizacao e fatos historicos

Identificar antes de unificar: logradouro/geografia, endereco da entidade, local operacional, snapshot de entrega/OS, posicao GPS observada e resultado de rota/geocodificacao. Campos latitude/longitude ou rua parecidos nao significam o mesmo fato.

Reutilizar endereco/local equivalente quando ha identidade, finalidade e escopo compativeis. Distinguir corrigir cadastro compartilhado de mudar a associacao de uma pessoa para outro endereco. Nao atualizar snapshot historico como efeito colateral da alteracao do cadastro atual.

Nao deduplicar logradouro apenas pelo nome, nem forcar tabela de ruas quando a responsabilidade nao existir. Remover o ultimo vinculo de um endereco nao autoriza apagar catalogo territorial ou dados de historico. A politica de retirada segue a secao anterior.

## Arquivos e integracoes de armazenamento

A integracao dona define o perfil logico, provedor/endereco e adaptador backend; modulos consumidores usam seu contrato, nunca credenciais ou caminhos fisicos do fornecedor. Identidade persistente do arquivo e ID/chave relativa no perfil, vinculada a empresa/entidade e metadados necessarios, sem URL assinada/temporaria, segredo ou endereco absoluto como unica referencia. Backend resolve URL/acesso a partir do perfil vigente e revalida permissao/tenant. Banco guarda referencias; objetos externos precisam de copia propria.

Reutilizar convencao existente compativel. Quando ausente, chave privada estavel: `<tenant_id>/<modulo>/<entidade_id>/<arquivo_id>.<extensao_validada>`; adaptador pode mapear bucket/container/prefixo sem mudar identidade. Nome original e metadado, nao caminho confiavel; upload/tipo/tamanho e acesso seguem [seguranca](SEGURANCA.md). Declarar padrao e consumidores no dono de armazenamento/DNAs do projeto, sem inventar tabela/coluna/modulo ou reorganizar arquivos existentes por rotina.

Troca do perfil em Integracoes ou equivalente exige inventario de objetos e referencias, copia autorizada ao novo destino, confronto de quantidades/bytes/hashes e ensaio de leitura/upload/permissoes dos consumidores atingidos antes de ativar. Registros antigos com URL/endereco fisico exigem mapeamento explicito e migracao autorizada, nao substituicao cega de texto. Coordenar gravacoes em curso pelo perfil/corte adequado, preservar origem e retorno compativel; nao apagar originais antes da conferencia nem declarar que arrastar uma pasta moveu os metadados/RLS ou todos os dados.

## Desempenho e prova de consolidacao
Revalidar no servidor preco, desconto, credito, pagamento, saldo, estoque, capacidade, propriedade e transicoes criticas.

### Onde calcular: frontend, backend e banco

| Camada | Responsabilidade e limite |
|---|---|
| Frontend | Formatar moeda/data, controlar a interface e calcular previas com os campos autorizados ja carregados. Previa nao e valor oficial nem autoriza gravacao; nao baixar historico/cadastro inteiro para calcular, contar ou filtrar localmente. |
| Backend/service dono | Validar entrada, sessao, permissao, empresa, regras e transicoes; resolver precos e condicoes pelas fontes/contratos vigentes e coordenar a persistencia. Nao aceitar preco, desconto permitido, saldo ou total enviados pelo navegador como verdade. |
| Banco, pela persistencia do dono | Calcular/consolidar valores oficiais do pedido/fatura, saldos e movimentos; agregar, filtrar, ordenar e paginar conjuntos de registros. Usar SQL/RPC compativeis com a stack e confirmar valores e efeitos relacionados na mesma transacao, com constraints e controle de concorrencia. |

No pedido, quantidade, preco aplicavel, descontos, frete e tributos pertinentes devem produzir um total oficial conferido ao gravar, usando os dados/revisoes autorizados para aquela operacao. A previa do navegador e substituida pelo resultado confirmado. Definir decimais/unidades, precisao, arredondamento, idempotencia e tratamento de alteracao concorrente; calcular no banco nao torna uma formula incorreta em correta. Nao recalcular todo o historico a cada abertura: saldo/total derivado mantido por movimento so quando justificado, com atualizacao consistente, estorno e reconciliacao/reconstrucao verificaveis.

### Prioridade de abertura, badges e alertas

Classificar no documento da pagina existente o essencial para operar, os complementos adiaveis e os detalhes sob demanda. Primeiro validar sessao/escopo/permissao e entregar estrutura e primeira pagina de dados necessarios; nao preparar todas as abas, modais e detalhes antes de tornar a pagina utilizavel. Reutilizar verificacoes equivalentes na mesma requisicao, sem transformar isso em autorizacao antiga entre requisicoes.

Badges, contadores de menu e alertas informativos auxiliares carregam depois, de forma assincrona e independente da abertura. O frontend apresenta o resultado; a contagem vem de consulta agregada no banco, restrita ao usuario/empresa permitidos, sem montar os objetos completos nem fazer uma consulta por item. Atraso/falha nessa consulta nao bloqueia navegacao ou formulario. Alerta que determina permissao, manutencao, credito, saldo ou outra recusa critica continua validado no servidor antes da operacao; adiar o badge nao adia essa protecao.

Enquanto nao houver resultado, nao inventar numero nem confundir indisponibilidade com zero. Se houver cache existente autorizado, isolar por identidade/empresa/escopo, definir validade e invalidacao e distinguir dado anterior de confirmado. Remover o badge quando a consulta confirmar zero; descartar resposta atrasada de outro contexto. Nao compartilhar contagens privadas nem deixar cache conceder acesso.

Atualizar contagens afetadas depois de uma acao confirmada ou por mecanismo existente compativel com a necessidade de atualidade. Evitar consultas duplicadas, polls sobrepostos e repeticao agressiva em erro; limitar frequencia/concorrencia e pausar atualizacoes auxiliares de pagina oculta quando aplicavel. Nao criar um endpoint por badge ou infraestrutura nova por rotina.

### Verificacao por pagina

Medir abertura util, consultas/idas ao banco, bytes, espera de rede/backend e processamento/renderizacao no navegador com cardinalidade representativa; distinguir primeiro acesso e cache aquecido. Conferir planos/indices das consultas custosas, consultas por linha e agregados repetidos. Mover trabalho pesado para JavaScript pode apenas trocar a espera de rede por travamento da interface. Registrar orcamento de tempo pertinente ao fluxo, sem prometer velocidade por contagem de tabelas ou teste com banco vazio.

No recorte alterado, testar que badge lento/com erro nao prende a pagina nem falsifica zero; troca de usuario/empresa nao reaproveita resultado indevido; previa adulterada nao muda o total oficial; gravacao concorrente/repetida preserva os valores e efeitos relacionados. Registrar evidencia e limites no dono da pagina; ensaio textual do padrao nao certifica tempo, integridade ou comportamento de consumidor.

Nao carregar cadastro/historico inteiro para pagina, resumo ou detalhe. Filtrar escopo e selecionar campos no backend; evitar `SELECT *` em listagens e consultas por linha quando lote resolve. Paginacao/limites no servidor; ordenacao dinamica por lista permitida. Calculo oficial tem dono, unidade, precisao e arredondamento.

Cache nao cria autorizacao nem confirma operacao. Nao persistir dado privado no navegador por conveniencia. Nao criar cache, fila, worker, indice ou infraestrutura para esconder desenho ruim.

Medir desempenho por operacao, cardinalidade real, payload, consultas, indices, locks e planos, nunca pela quantidade de tabelas. Tabela vazia pode estar corretamente em uso; tabela preenchida pode ser redundante. Nao usar um alvo de reducao para justificar fusoes.

Chat consulta historico com pagina/limite e ordem estavel, sem carregar todas as mensagens na ficha de cliente. Garantir retomada apos desconexao e backlog maior que o limite segundo o contrato; nao pular registros silenciosamente. Anexos usam consulta em lote e leitura de objeto sob demanda, respeitando visibilidade.

Reutilizar filas, paginacao, indices e caches existentes. Indice/particao/banco separado/materializacao exigem evidencia da consulta/volume e teste, nao instalacao automatica por este perfil. Separacao de responsabilidade nao implica microservico ou banco fisico separado.

Fusao ou troca de dono tem mapa DE/PARA de IDs, conflitos, consumidores, contratos, permissoes, retencao e reversao. Preferir transicao compativel, com verificacao de equivalencia e retirada do legado somente apos confirmar consumidores. Nao manter duas fontes independentes de escrita. Se houver escrita dupla temporaria, definir consistencia, reconciliacao e fim desse mecanismo.

Nao alterar migration ja publicada para representar a nova historia. Nao gerar migration apenas porque um relatorio mencionou reaproveitamento. Prototipo nao grava no oficial; construcao e alteracao real dependem de suas autorizacoes.
