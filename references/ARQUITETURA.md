# Arquitetura — modulos, estrutura e artefatos

## Ordem obrigatoria
Reconhecer antes de criar. Padrao orientado a responsabilidades; nomes abaixo sao fallback quando NAO existe destino canonico ou convencao adequada. Equivalente correto existente prevalece. Nao migrar tecnologia, mover arquivos em massa ou duplicar estrutura so para adotar os exemplos.

Primeiro: identidade/stack/entradas -> capacidades reais -> regras/contratos/dados -> consumidores -> limites dos modulos -> destino existente -> lacuna comprovada. Sem evidencias suficientes: NAO_DESCOBERTO, nao autorizacao para criar ou apagar.

## Separacao de modulos
Modulo representa capacidade/coesa responsabilidade de negocio, nao cada tabela, pagina ou botao. Declarar dono da regra/dado, entradas publicas, dependencias e consumidores. Tela de um modulo usa contrato do dono, nao duplica calculo ou acessa sua tabela interna para contornar a regra.

Reutilizar modulo existente quando a responsabilidade pertence a ele. Criar modulo somente para responsabilidade distinta necessaria a capacidade aprovada. Extrair compartilhado apenas quando consumidores reais justificarem; nao criar `common`, `utils` ou `shared` como deposito generico.

Proposta de organizacao usa DE -> PARA com motivo, responsabilidade, consumidores, documentos, testes, preservacao e recuperacao. Mudanca de caminho reconcilia imports/autoload, rotas, assets, jobs, contratos, IDs, CI e documentacao no mesmo lote. Migrations publicadas e dados historicos nao sao reescritos por organizacao.

## Responsabilidades, nao camadas vazias
Interface -> entrada/transporte/sessao -> normalizacao -> regra/autorizacao -> persistencia/contrato -> integridade no banco. Materializar apenas o necessario, idiomaticamente na stack. Funcao local de UI nao exige backend; efeito oficial nao fica apenas no navegador.

## JavaScript por responsabilidade e tamanho
Vale para fontes JavaScript escritas a mao no prototipo e no real. Alvo: ate 300 linhas de codigo por arquivo; acima de 500, revisar e separar responsabilidades antes de fechar a entrega. Contar linhas de fonte legivel, desconsiderando linhas vazias e exclusivamente de comentario. Nao minificar, juntar instrucoes ou esconder templates em linhas gigantes para cumprir o numero. Gerados/minificados e dependencias de terceiros ficam fora dessa contagem, com origem identificada.

Separar por tarefa coesa e consumidor, nunca em partes numeradas ou por corte a cada 500 linhas. Arquivo acima do limite que permaneça coeso exige justificativa no dono existente: responsabilidade, motivo para nao extrair, consumidores e verificacoes; revisor/fiscal confere essa excecao. O tamanho sinaliza manutencao, nao garante arquitetura nem ausencia de bugs. Funcoes nomeiam uma tarefa e mantem entradas/saidas claras; extrair quando misturam responsabilidades, sem criar wrappers ou arquivos vazios.

Reutilizar destinos e nomes coerentes do modulo. Em PHP/JS puro sem equivalente, `app/modules/<modulo>/js/<tela>.js` inicia/coordena a tela; extracoes necessarias usam `<tela>-<responsabilidade>.js`, por exemplo canvas, regras, modais ou comandos. O nome descreve o que faz; nao usar `parte1`, `novo` ou `utils` para evitar definir responsabilidade. Criar somente partes realmente consumidas, e preservar a convencao idiomatica dos simbolos existentes; funcao nova usa verbo + objeto, como `abrirConfiguracao` ou `confirmarTransferencia`.

Antes de extrair: conferir estado/escopo, entradas publicas, eventos, ordem de carregamento, rotas/assets, testes e documentos. Manter interface publica minima e dependencias explicitas conforme o mecanismo JavaScript ja adotado; nao criar globals espalhados, dependencia circular, framework ou build novo. Preservar IDs, validacoes, tratamento de erro e comportamento aprovado; conferir carregamento e consumidores no mesmo lote. Identificacao interna segue [codigo e DNA](DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo).

No prototipo, usar a mesma divisao e contratos previstos para o real, com simulacao isolada do codigo reutilizavel. Conversao reaproveita a fonte aprovada e troca a simulacao pelo backend autorizado; regra critica nao migra para JS. Legado grande entra em lotes por modulo com mapa de consumidores e verificacao, sem refatoracao global automatica por ultrapassar o numero.

## Destinos e nomes se faltarem
| Artefato necessario | Primeiro procurar | Fallback somente na ausencia comprovada |
|---|---|---|
| Modulo de negocio | Raiz modular e convencao do framework | `src/modules/<modulo>/` em projeto sem convencao; criar somente com primeiro arquivo usado. Em framework existente, usar sua raiz canonica, nao abrir src paralelo. |
| Implementacao da capacidade | Action/controller/service/repository/entrada equivalente | Arquivo nomeado pela capacidade/responsabilidade no modulo dono; classes em PascalCase, funcoes/arquivos na convencao idiomatica da stack. Sem extensao ou camadas artificiais. |
| UI da capacidade | Telas/views/componentes do modulo | View/componente com nome da tarefa no destino de interface do modulo; rota e consumidor no mesmo lote. |
| Tokens e componente visual compartilhado | Tema/CSS e componentes centrais | Destino compartilhado de interface na raiz existente; `src/ui/` apenas sem equivalente, com primeiro componente/token realmente consumido. |
| Teste | Runner, pasta e sufixo vigentes | `tests/<modulo>/` com nome da capacidade e convencao nativa; nao impor extensao, runner ou framework diferente. |
| Migration | Diretorio e ordenacao do instrumento atual | Primeiro definir instrumento permitido; sem instrumento, propor antes de criar SQL solto ou aplicar no banco. |
| Script necessario | Scripts existentes da responsabilidade | `scripts/<responsabilidade>/<acao>.<ext>` com consumidor/comando real; nao script temporario versionado sem finalidade. |
| Check/pipeline de CI | Workflows e verificacoes existentes | `.github/workflows/<responsabilidade>.yml` em projeto GitHub, somente para comandos/checks de necessidade comprovada; privilegio minimo, sem segredo literal/deploy automatico implicito. |
| Documentacao | Destinos canonicos locais | Aplicar references/DOCUMENTACAO.md; nunca abrir arvore inteira antecipadamente. |

Nomes novos descritivos, estaveis, sem espacos/acentos para caminhos portateis; convencao existente coerente prevalece. Slug de modulo em minusculas com hifen quando a stack permitir; simbolos/namespace seguem a linguagem. Nao sufixar `2`, `novo`, `v2`, `old`, `backup` para contornar responsabilidade existente.

## Catalogo condicional de criacao
Esta tabela e consumida pelo gate de `romulo-analisar`. E previsao de tipos/destinos, nao autorizacao irrestrita: cada caminho precisa de necessidade, skill dona, consumidor e pedido autorizado. Sem linha aplicavel: exigir excecao `0393` antes da criacao.

| Categoria | Skill dona | Condicao de criacao |
|---|---|---|
| AGENTS.md e CLAUDE.md do bootstrap | romulo-iniciar-projeto | Ausentes, bootstrap autorizado, identidade preenchida, destino confirmado. Existente protegido nao pode ser sobrescrito. |
| Fonte, teste, asset ou configuracao do recurso | romulo-construir; romulo-interface quando visual | Capacidade/revisao aprovada, responsabilidade e consumidor reais, destino anterior ou fallback acima. Configuracao nao concede privilegios. |
| Documento ou indice canonico | romulo-documentacao | Conhecimento necessario sem destino equivalente; nome/escopo segundo referencia documental. |
| Migration/contrato persistente | romulo-construir e romulo-seguranca | Mudanca de dados necessaria e autorizacao da operacao; criar SQL nao autoriza aplica-lo. |
| Alteracao da distribuicao central | romulo-evoluir-padrao | Pedido de evolucao do metodo; skill/reference/template/manifests e verificacoes diretamente afetados, sem fabrica de arquivos. |
| Saidas de build, testes e instalacao autorizados | romulo-verificar; romulo-iniciar-projeto para bootstrap | Comando conhecido, destino gerado/cache/temp identificado, dados controlados e descarte/retencao definida. Inclui relatórios e screenshots pertinentes; nao permite notas paralelas. |
| Copia de trabalho para analise/teste | romulo-analisar | Fonte/ref confirmados, destino descartavel delimitado e separado do projeto; copia nao e nova fonte canonica nem autorizacao de sobrescrita. |
| Configuracao de qualidade, testes, telemetria ou CI | romulo-verificar; romulo-seguranca para dados/integração | Perfil compativel e adocao autorizados, reutilizar ferramentas/comandos e destinos existentes; gasto, contas, dados enviados e novas dependencias precisam de escopo especifico. |

Pasta so com conteudo necessario. Nome previsto sem necessidade nao autoriza criar. Nova dependencia, recurso externo, lockfile ou scaffolder exige avaliar todos os arquivos e efeitos produzidos antes de executar. Nao usar comando de terceiro para contornar a regra.
