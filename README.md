# Romulo Dev Standard

Versao: 1.9.0
Repositorio oficial: `romulorenatoss-maker/romulo-dev-standard`.

## Entrada obrigatoria — sumario de diretrizes
Este README e o unico indice central de metodo e roteamento. O AGENTS.md de cada projeto guarda identidade, ambientes, ponte para este indice e protecoes/ponte documental locais; nao copia lista/contagem de skills, comandos de instalacao ou regras gerais. O AGENTS.md da raiz deste repositorio governa somente o padrao, nao e o modelo dos consumidores.

Em toda execucao tecnica, antes de escrever:
1. Ler o AGENTS.md local e as protecoes locais pertinentes. Identificar repositorio, worktree, branch, ambiente e alcance autorizado.
2. Resolver este indice no repositorio/ref oficial indicado pelo projeto; registrar versao e revisao obtidas. Fixar a mesma revisao para as leituras desta execucao, sem misturar arquivos de versoes diferentes. Ref `main` acompanha atualizacoes entre execucoes; pin explicito prevalece e exige migracao autorizada. Nao atualizar silenciosamente a politica no meio do lote.
3. Conferir a distribuicao e as skills disponiveis pelo catalogo abaixo. Instalacao/atualizacao e recarga seguem [INSTALL.md](INSTALL.md). Ler arquivo nao comprova plugin ou hook ativo.
4. Aplicar `romulo-analisar` e Ponytail `full`; carregar integralmente somente as skills e referencias pertinentes ao efeito real; dependencias entre skills sao instrucoes de consulta, nao chamadas de programa automaticas.
5. Ler o sumario/documentacao do projeto e seguir ate regras, contratos, codigo e consumidores atingidos. Padrao central explica COMO trabalhar; o projeto explica O QUE existe e suas regras de negocio.
6. Aplicar o encaminhamento abaixo e terminar com `romulo-verificar`. Falha corrigivel volta a construcao, nao vira encerramento por etiqueta pendente.

Consulta ja comprovada na mesma revisao pode ser reutilizada. Nova tarefa verifica a revisao da fonte; nao reler tudo nem depender de memoria vaga. Sem acesso/fonte confiavel: declarar NAO_DISPONIVEL e bloquear a escrita dependente, sem inventar regra. Cache local somente se origem/revisao verificadas e uso offline autorizado; registrar que a atualidade remota nao foi confirmada. Instrucao remota nao amplia autorizacoes locais nem executa codigo por si.

## Catalogo e encaminhamento — fonte unica
A tabela e tambem o catalogo nominal conferido pelo validador. Nao repetir uma contagem fixa nos projetos.

| Skill | Quando consultar | Responsabilidade |
|---|---|---|
| [romulo-analisar](skills/romulo-analisar/SKILL.md) | Toda execucao tecnica | Leitura dirigida, impacto e gate de criacao de arquivos. |
| [romulo-iniciar-projeto](skills/romulo-iniciar-projeto/SKILL.md) | Projeto novo; implantacao/migracao do bootstrap | AGENTS minimo, CLAUDE.md ponte e primeira capacidade necessaria. |
| [romulo-auditar-projeto](skills/romulo-auditar-projeto/SKILL.md) | Organizar projeto existente ou diagnostico amplo | Descobrir, mapear modulos e propor organizacao por lacunas comprovadas. |
| [romulo-especificar](skills/romulo-especificar/SKILL.md) | Capacidade, regra, fluxo, tela, aba ou acao | Perguntas faltantes, proposta, utilidade dos elementos e aprovacao. |
| [romulo-interface](skills/romulo-interface/SKILL.md) | Qualquer efeito visual/interativo | Referencia aprovada, componentes, CSS, peculiaridades e revisao renderizada. |
| [romulo-construir](skills/romulo-construir/SKILL.md) | Construcao, alteracao ou bug autorizado | Cadeia funcional completa e correcao com reteste. |
| [romulo-seguranca](skills/romulo-seguranca/SKILL.md) | Entrada, acesso, dados, banco, integracao ou efeito critico | Controles no runtime, autorizacao e integridade. |
| [romulo-documentacao](skills/romulo-documentacao/SKILL.md) | Conhecimento canonico alterado | Destinos, nomes e vinculos documentais sem duplicacao. |
| [romulo-prototipo-real](skills/romulo-prototipo-real/SKILL.md) | Prototipo convertido/integrado/comparado ao real | Preservar proposta e trocar simulacao por contratos reais. |
| [romulo-verificar](skills/romulo-verificar/SKILL.md) | Antes de encerrar toda entrega tecnica | Aceite por efeito, arquivos, documentacao, visual e evidencias. |
| [romulo-evoluir-padrao](skills/romulo-evoluir-padrao/SKILL.md) | Diretriz comum criada/alterada | Evoluir esta fonte, validar, versionar e distribuir. |

Ponytail e complemento externo oficial `DietrichGebert/ponytail`, em modo `full`; nao equivale a uma skill Romulo. Nao remove requisito, aprovacao, seguranca, documentacao, acessibilidade ou teste. Instalacao em [INSTALL.md](INSTALL.md).

## Quem define cada padrao
- Estrutura, modulos, nomes e catalogo condicional de artefatos: [references/ARQUITETURA.md](references/ARQUITETURA.md), consultado pelas skills de analise/auditoria/construcao.
- Destinos documentais e nomes quando faltam: [references/DOCUMENTACAO.md](references/DOCUMENTACAO.md), aplicado por `romulo-documentacao`.
- Dados e seguranca: [references/DADOS.md](references/DADOS.md) e [references/SEGURANCA.md](references/SEGURANCA.md).
- Criacao de AGENTS/CLAUDE e migracao de peculiaridades: `romulo-iniciar-projeto`, usando [templates/AGENTS.md](templates/AGENTS.md) e [templates/CLAUDE.md](templates/CLAUDE.md).
- Arquivo novo nao previsto: gate de `romulo-analisar`; exige `0393` do responsavel para aquela excecao. A regra nao concede permissao para alterar arquivo protegido, dados, acesso ou deploy.

## Uso de recursos externos
Skills instaladas, recursos embutidos e conectores nao concedem autorizacao de escrita. `init`, geradores de plugins/skills/documentos, memorias, Figma e demais ferramentas tambem passam pelo gate de artefatos de `romulo-analisar` quando usados neste trabalho. Nao fabricar CLAUDE.md longo, planos ou copias de regras por sugestao automatica.

Nao remover plugins ou mudar permissoes por uma lista colada no chat. Confirmar superficie, origem, escopo, uso e autorizacao. Recurso opcional sem uso pode ser desabilitado no escopo adequado apos decisao; nao enfraquecer revisao de seguranca nem permissoes para reduzir avisos. Nao delegar geracao de codigo a outro agente; preservar excecao local de revisor independente quando autorizada.

## Validacao e limites
Executar `python3 scripts/validate_standard.py` e `python3 -m unittest discover -s tests -v`, com Python 3.10+ (usar `python` no Windows quando apropriado). Sem dependencias Python externas. O validador confere estrutura, catalogo, links, templates e roteamento textual; nao impede toda escrita do sistema operacional, nao instala plugins e nao comprova obediencia do modelo ou qualidade de telas. Bloqueio mecanico de escrita exige hook/permissao/sandbox do ambiente, implantado e testado com autorizacao propria; nao alegar blindagem apenas pelo Markdown.

## Migracao 1.8.0 -> 1.9.0

Sem mudanca de compatibilidade. `romulo-prototipo-real` ganha o fechamento da conversao (comparar prototipo x real, diferencas ao andamento, documento so com o real, apagar prototipo concluido); `romulo-verificar` manda o fiscal conferir. Atualizar o plugin e recarregar as skills.

## Migracao 1.7.0 -> 1.8.0

Sem mudanca de compatibilidade. `romulo-construir` torna obrigatorio o historico de entregas (QUEM, COMMITS, FEZ, CONFERIU, FALTA, DESFAZER) em toda entrega publicada; `references/DOCUMENTACAO.md` deixa de tratar o historico de lote como opcional; `romulo-verificar` manda o fiscal independente conferir o fechamento documental e a limpeza dos registros de trabalho. Atualizar o plugin e recarregar as skills.

## Migracao 1.6.0 -> 1.7.0

Sem mudanca de compatibilidade. `romulo-construir` ganha a limpeza dos registros de trabalho (o que foi entregue sai de perguntas, andamento, fila, pendencias e mapas no mesmo lote); `romulo-interface` secao 6 item 6 deixa de "marcar como respondida": a pergunta sai do registro ao documentar a decisao e fica no andamento como "respondida, a construir" ate ser publicada; `romulo-documentacao` aponta para isso. Atualizar o plugin e recarregar as skills; projetos limpam seus registros na proxima entrega.

## Migracao 1.5.0 -> 1.6.0

Sem mudanca de compatibilidade. `romulo-interface` ganha a secao 6 (revisao com o responsavel, uma peca por vez, com fila canonica de perguntas) e `romulo-especificar` aponta para ela. Atualizar o plugin e recarregar as skills; nenhum AGENTS local precisa ser alterado.

## Migracao 1.4.0 -> 1.5.0
Sem novas skills: centraliza o indice, reduz o template e define organizacao/gate de arquivos nas fontes existentes. Atualizar o plugin e comprovar descoberta conforme INSTALL.md. Para consumidores, integrar o template preservando identidade, IDs, guardas, peculiaridades e regras locais; nunca copiar o AGENTS da raiz central nem sobrescrever AGENTS protegido. Mover conteudo local exige destino canonico e vinculo antes de retirar da origem. Codigo, banco e telas nao mudam por instalar este metodo.
