# Arquitetura — modulos, estrutura e artefatos

## Ordem obrigatoria
Reconhecer antes de criar. Padrao orientado a responsabilidades; nomes abaixo sao fallback quando NAO existe destino canonico ou convencao adequada. Equivalente correto existente prevalece. Nao migrar tecnologia, mover arquivos em massa ou duplicar estrutura so para adotar os exemplos.

Primeiro: identidade/stack/entradas -> capacidades reais -> regras/contratos/dados -> consumidores -> limites dos modulos -> destino existente -> lacuna comprovada. Sem evidencias suficientes: NAO_DESCOBERTO, nao autorizacao para criar ou apagar.

## Padrao tecnico local

Em toda criacao ou alteracao, consultar o TRD/documento tecnico dono e a convencao do modulo antes de escolher linguagem, destino ou nome. Materializar as escolhas locais com o [modelo tecnico](../templates/PADRAO_TECNICO.md), no dono equivalente definido por [documentacao](DOCUMENTACAO.md#padroes-locais-preenchiveis); nao criar manual concorrente. O metodo central fornece responsabilidades e exemplos; o contrato local fixa os caminhos e escolhas concretos daquele projeto.

Registrar por escopo: linguagem/runtime e versoes permitidas; framework quando adotado; entrada/roteamento; raizes e limites dos modulos; nomes/extensoes de arquivos e simbolos; componentes, hooks quando houver, estado, acesso a dados, estilos, testes e documentos. Separar linguagem do produto de ferramentas de teste/build. Dependencia encontrada nao e tecnologia aprovada nem usada em producao. Conhecimento observado, proposta e decisao aprovada ficam distintos, com origem e revisao.

Para cada linguagem realmente adotada, manter um perfil de criacao: responsabilidade de cada tipo de arquivo, caminho/extensao, regra de nomes, estrutura interna (imports, API publica, corpo e exportacao quando aplicaveis), contratos de entrada/saida/erro, documento/DNA dono, exemplo real na revisao conferida e comandos de verificacao existentes. A referencia e para criacao E correcao. Se nao houver exemplo real, usar os exemplos condicionais abaixo para a primeira capacidade e registra-la como referencia somente apos conferida; nao inventar arquivos implementados ou aprovacoes.

Escolhas ainda indispensaveis sao resolvidas antes da parte dependente; o restante continua. Decisao expressa ja dada nao exige nova pergunta. Criar dentro da convencao aprovada e corrigir para cumpri-la nao reabre a escolha da stack. Trocar linguagem, biblioteca, raiz modular ou convencao global exige impacto e decisao expressa, atualizando o mesmo dono. Excecao tecnica nomeia escopo/arquivos, o que difere, motivo conhecido, origem/autorizacao e limite; o restante herda o contrato. Diferenca antiga sem origem e divergencia a investigar, nao excecao inventada.

### Exemplos de modulo financeiro por stack

Referencias para projeto sem convencao adequada, nao geradores de arvore. Adotar somente o exemplo compativel com a stack autorizada; registrar os caminhos concretos no perfil local e reutiliza-los nos proximos modulos. Framework com raiz/roteamento proprio mantem essa organizacao. Cada linha nasce com responsabilidade e consumidor reais; nao criar todos os arquivos apenas porque aparecem na tabela.

**PHP com JavaScript no navegador**, sem framework que ja determine outros destinos:

| Caminho de referencia | Responsabilidade e formato |
|---|---|
| `app/modules/financeiro/views/lancamentos.php` | Compor a tela com componentes compartilhados e dados normalizados; escapar saidas no contexto correto. Sem SQL ou regra financeira oficial na view. |
| `app/modules/financeiro/js/lancamentos.js` | Inicializar a tela, eventos e estados; funcoes com verbo + objeto, por exemplo `carregarLancamentos`. Usar o mecanismo de modulos/carregamento adotado, sem globals novos. |
| `app/modules/financeiro/js/lancamentos-filtros.js` | Extracao coesa de filtros quando necessaria e consumida pela tela; nao divisao por contagem de linhas. |
| `app/modules/financeiro/actions/ListarLancamentos.php` | Entrada registrada no roteador existente, normalizacao e chamada do contrato autorizado; nome de classe PascalCase se o projeto usar classes. |
| `app/modules/financeiro/services/LancamentosService.php` | Regra/orquestracao do dominio quando distinta; sem camada que apenas repasse chamadas. Autorizacao e efeitos oficiais ficam no servidor. |
| `app/modules/financeiro/repositories/LancamentosRepository.php` | Persistencia do modulo dono, consultas parametrizadas e escopo de acesso conforme contratos de dados/seguranca. |
| `tests/financeiro/ListarLancamentosTest.php` | Cenario relevante no runner PHP adotado; nome/sufixo seguem seu perfil, sem instalar outro runner pelo exemplo. |
| `docs/modulos/financeiro/SUMARIO.md` e `docs/modulos/financeiro/telas/lancamentos.md` | Entrada do modulo e dono da tela/cadeia, conforme DOCUMENTACAO; apontar para regras/contratos distintos apenas quando existirem. |

**React**, quando aprovado para a aplicacao ou para um escopo delimitado. O exemplo usa TypeScript somente se essa linguagem estiver adotada; em JavaScript usar `.jsx`/`.js` e os contratos de tipos do projeto. React nao escolhe por si backend, framework de rotas, biblioteca de estado ou build.

| Caminho de referencia | Responsabilidade e formato |
|---|---|
| `src/modules/financeiro/pages/LancamentosPage.tsx` | Compor a pagina e ligar a entrada do roteador aprovado; imports, componente nomeado PascalCase e exportacao conforme perfil local. |
| `src/modules/financeiro/components/ListaLancamentos.tsx` | Configurar colunas, dados e acoes do dominio usando a lista compartilhada; props explicitas, sem copiar seu markup/estilo/controle de carregamento. |
| `src/modules/financeiro/hooks/useListaLancamentos.ts` | Hook com prefixo `use`, estado/efeitos de uma responsabilidade e contrato de retorno; extrair por necessidade, nao para cada funcao. |
| `src/modules/financeiro/services/lancamentos-api.ts` | Adaptar o contrato HTTP/API existente; nao acessar banco nem definir autoridade financeira no navegador. |
| `src/modules/financeiro/types/lancamento.ts` | Tipo/contrato compartilhado do modulo quando houver consumidor e nao existir dono equivalente; evitar repetir o mesmo tipo por componente. |
| `src/modules/financeiro/index.ts` | Entrada publica minima somente se houver consumidores externos ao modulo; sem exportar todos os internos ou criar ciclos. |
| `src/ui/ListaDados.tsx`, `src/ui/Botao.tsx` e `src/ui/tokens.css` | Fontes compartilhadas realmente usadas; padrao visual aponta para elas. Sem nomes de dominio ou regras financeiras dentro da UI comum. |
| `tests/financeiro/lista-lancamentos.test.tsx` | Comportamentos relevantes no runner adotado; reutilizar localizacao/sufixo existentes. |
| `docs/modulos/financeiro/SUMARIO.md` e `docs/modulos/financeiro/telas/lancamentos.md` | Mesmos contratos documentais de responsabilidade, independentemente da linguagem. |

Nos componentes React, fixar no perfil local a convencao de exportacoes, props, composicao, propriedade do estado e efeitos, imports publicos e estrategia de estilos/testes. Seguir as [regras de composicao](https://react.dev/learn/your-first-component) e [Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) da versao adotada; funcao util comum que nao chama Hooks React nao ganha prefixo `use`. Hook especifico fica no modulo; compartilhado so e extraido para o dono comum quando consumidores reais justificarem. Nao adicionar dependencias ou duplicar estado para preencher o exemplo. PHP/JS existente nao migra para React por adotar este padrao.

CSS compartilhado guarda identidade e estados; CSS local apenas a composicao permitida por `interface`. SQL/migrations seguem instrumento/nome/ordenacao e [contrato de dados](DADOS.md#contrato-da-migration); os exemplos acima nao autorizam SQL solto. Outra linguagem adotada recebe seu perfil local com as mesmas responsabilidades, usando convencoes idiomaticas verificadas, sem copiar extensoes ou sintaxe de PHP/React.

### Formato interno dos arquivos de referencia

Sem convencao adequada, adotar os formatos abaixo no perfil local da stack autorizada. Ao reutilizar o exemplo, preencher responsabilidade e contratos reais, sem comentarios vazios ou marcadores ficticios. Cabecalho/DNA segue o dono de documentacao interna, sem reproduzir a especificacao inteira no codigo.

| Tipo | Ordem e limites de referencia |
|---|---|
| Classe PHP | Abertura PHP, declaracoes/namespace conforme autoload adotado, imports e classe com nome do arquivo; contrato publico claro e metodos coesos. Sem HTML na persistencia ou SQL na view. |
| View PHP | Preparacao minima dos dados recebidos e composicao da apresentacao; saidas escapadas e componentes comuns. Regra oficial permanece no dono do servidor. |
| Modulo JavaScript/TypeScript | Imports/dependencias explicitos, contratos/tipos pertinentes, funcoes coesas nomeadas e API publica minima. Exportacoes nomeadas como fallback de modulos ES; preservar carregador/framework existente. |
| Componente React JSX/TSX | Imports, contrato de props, componente nomeado PascalCase, composicao da UI e exportacao; exportacao default somente quando a convencao/framework pedir. Sem criar estado duplicado para valores derivados. |
| Hook React | Imports, entrada/retorno e funcao `use<Responsabilidade>`; chamadas de Hooks conforme regras oficiais, efeitos com ciclo/limpeza pertinentes e retorno explicito. Nao esconder toda a pagina em um hook gigante. |
| Tipo/contrato TypeScript | Nome e campos do contrato no dono; exportar somente o que tem consumidor. Nao copiar tipos por tela nem misturar efeitos de rede no arquivo de tipos. |
| CSS | Tokens/variantes no dono comum; seletores de composicao local delimitados; estados e modos aprovados. Nao redefinir identidade por modulo. |
| SQL/migration | Nome, ordenacao, transacao e reversao conforme instrumento e contrato de DADOS; criar o arquivo nao autoriza aplicar no banco. |
| Teste | Preparacao controlada, acao e verificacao de comportamento relevante; runner/sufixo/comando do perfil. Nao reproduzir a implementacao apenas para gerar cobertura. |
| Markdown | Titulo e responsabilidade, finalidade, regra vigente, vinculos de codigo/contratos/consumidores e evidencias pertinentes; sumario aponta ao dono. Sem pergunta aberta, manual duplicado ou historico como regra ativa. |

## Separacao de modulos
Modulo representa capacidade/coesa responsabilidade de negocio, nao cada tabela, pagina ou botao. Declarar dono da regra/dado, entradas publicas, dependencias e consumidores. Tela de um modulo usa contrato do dono, nao duplica calculo ou acessa sua tabela interna para contornar a regra.

Reutilizar modulo existente quando a responsabilidade pertence a ele. Criar modulo somente para responsabilidade distinta necessaria a capacidade aprovada. Extrair compartilhado apenas quando consumidores reais justificarem; nao criar `common`, `utils` ou `shared` como deposito generico.

Proposta de organizacao usa DE -> PARA com motivo, responsabilidade, consumidores, documentos, testes, preservacao e recuperacao. Mudanca de caminho reconcilia imports/autoload, rotas, assets, jobs, contratos, IDs, CI e documentacao no mesmo lote. Migrations publicadas e dados historicos nao sao reescritos por organizacao.

Antes de ampliar modulo ou capacidade transversal, aplicar [reutilizacao e propriedade](DADOS.md#reutilizacao-e-propriedade-de-dados). Distinguir dono da informacao de tela de captura, consumidor e origem. Um modulo removivel nao deve ser o unico dono de cadastros necessarios aos demais. Reutilizar o dono existente; nao criar um Core universal apenas para centralizar nomes.

Compartilhamento exige contrato explicito e politica de retirada; nao acesso livre a tabelas internas. Uma capacidade pode compartilhar cadastro e manter eventos operacionais separados. Atendimento/protocolo e canal de chat sao responsabilidades distintas quando outras operacoes dependem do atendimento. Planejar a retirada do consumidor sem desligar a capacidade compartilhada.

Publicacao de mudancas de dono/schema/contrato considera trabalhos concorrentes e versoes de produtores/consumidores. Registrar grupo de integracao quando uma metade nao for compativel com a versao restante. Reservar arquivo nao substitui essa verificacao.

## Responsabilidades, nao camadas vazias
Interface -> entrada/transporte/sessao -> normalizacao -> regra/autorizacao -> persistencia/contrato -> integridade no banco. Materializar apenas o necessario, idiomaticamente na stack. Funcao local de UI nao exige backend; efeito oficial nao fica apenas no navegador. Somente a persistencia do modulo dono acessa o banco, conforme [acesso ao banco](DADOS.md#acesso-ao-banco-somente-pela-persistencia-do-modulo).

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
| Migration | Diretorio e ordenacao do instrumento atual | Primeiro definir instrumento permitido; sem instrumento, propor antes de criar SQL solto ou aplicar no banco. Seguir o [contrato da migration](DADOS.md#contrato-da-migration) e o perfil local. |
| Script necessario | Scripts existentes da responsabilidade | `scripts/<responsabilidade>/<acao>.<ext>` com consumidor/comando real; nao script temporario versionado sem finalidade. |
| Check/pipeline de CI | Workflows e verificacoes existentes | `.github/workflows/<responsabilidade>.yml` em projeto GitHub, somente para comandos/checks de necessidade comprovada; privilegio minimo, sem segredo literal/deploy automatico implicito. |
| Documentacao | Destinos canonicos locais | Aplicar references/DOCUMENTACAO.md; nunca abrir arvore inteira antecipadamente. |

Nomes novos descritivos, estaveis, sem espacos/acentos para caminhos portateis; convencao existente coerente prevalece. Slug de modulo em minusculas com hifen quando a stack permitir; simbolos/namespace seguem a linguagem. Nao sufixar `2`, `novo`, `v2`, `old`, `backup` para contornar responsabilidade existente.

## Catalogo condicional de criacao
Esta tabela e consumida pelo gate de `analisar`. E previsao de tipos/destinos, nao autorizacao irrestrita: cada caminho precisa de necessidade, skill dona, consumidor e pedido autorizado. Sem linha aplicavel: exigir excecao `0393` antes da criacao.

| Categoria | Skill dona | Condicao de criacao |
|---|---|---|
| AGENTS.md e CLAUDE.md do bootstrap | iniciar-projeto | Ausentes, bootstrap autorizado, identidade preenchida, destino confirmado. Existente protegido nao pode ser sobrescrito. |
| Fonte, teste, asset ou configuracao do recurso | construir; interface quando visual | Capacidade/revisao aprovada, responsabilidade e consumidor reais, destino anterior ou fallback acima. Configuracao nao concede privilegios. |
| Documento ou indice canonico | documentacao | Conhecimento necessario sem destino equivalente; nome/escopo segundo referencia documental. |
| Migration/contrato persistente | construir e seguranca | Mudanca de dados necessaria e autorizacao da operacao; criar SQL nao autoriza aplica-lo. |
| Alteracao da distribuicao central | evoluir-padrao | Pedido de evolucao do metodo; skill/reference/template/manifests e verificacoes diretamente afetados, sem fabrica de arquivos. |
| Saidas de build, testes e instalacao autorizados | verificar; iniciar-projeto para bootstrap | Comando conhecido, destino gerado/cache/temp identificado, dados controlados e descarte/retencao definida. Inclui relatórios e screenshots pertinentes; nao permite notas paralelas. |
| Pasta `temp/` de perguntas e fila temporarias | construir | Pergunta ou trabalho/aceite pendente no alcance autorizado; somente `temp/` dentro da pasta privada nao versionada do projeto (ex.: `backup/temp/`), conforme [pasta temp](../skills/construir/SKILL.md#pasta-temp-de-perguntas-e-fila-temporarias); definicao visual escolhida fica no dono e a fila a referencia; excluida ao terminar sem pendencias. |
| Copia de trabalho para analise/teste | analisar | Fonte/ref confirmados, destino descartavel delimitado e separado do projeto; copia nao e nova fonte canonica nem autorizacao de sobrescrita. |
| Configuracao de qualidade, testes, telemetria ou CI | verificar; seguranca para dados/integração | Perfil compativel e adocao autorizados, reutilizar ferramentas/comandos e destinos existentes; gasto, contas, dados enviados e novas dependencias precisam de escopo especifico. |

Pasta so com conteudo necessario. Nome previsto sem necessidade nao autoriza criar. Nova dependencia, recurso externo, lockfile ou scaffolder exige avaliar todos os arquivos e efeitos produzidos antes de executar. Nao usar comando de terceiro para contornar a regra.
