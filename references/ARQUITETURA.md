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

Pasta so com conteudo necessario. Nome previsto sem necessidade nao autoriza criar. Nova dependencia, recurso externo, lockfile ou scaffolder exige avaliar todos os arquivos e efeitos produzidos antes de executar. Nao usar comando de terceiro para contornar a regra.
