# Romulo Dev Standard

Versao: 1.12.2
Repositorio oficial: `romulorenatoss-maker/romulo-dev-standard`.

## Entrada obrigatoria — sumario de diretrizes
Este README e o unico indice central de metodo e roteamento. O AGENTS.md de cada projeto guarda identidade, ambientes, ponte para este indice e protecoes/ponte documental locais; nao copia lista/contagem de skills, comandos de instalacao ou regras gerais. O AGENTS.md da raiz deste repositorio governa somente o padrao, nao e o modelo dos consumidores.

Em toda execucao tecnica, antes de escrever:
1. Ler o AGENTS.md local e as protecoes locais pertinentes. Identificar repositorio, worktree, branch, ambiente e alcance autorizado.
2. Resolver este indice no repositorio/ref oficial indicado pelo projeto; registrar versao e revisao obtidas. Fixar a mesma revisao para as leituras desta execucao, sem misturar arquivos de versoes diferentes. Ref `main` acompanha atualizacoes entre execucoes; pin explicito prevalece e exige migracao autorizada. Nao atualizar silenciosamente a politica no meio do lote.
3. Comparar a versao instalada das skills com a `Versao` deste README na ref oficial. Se forem diferentes, dizer ao responsavel "achei uma versao diferente do padrao (instalada X, oficial Y)", atualizar e recarregar as skills conforme [INSTALL.md](INSTALL.md) e so entao comecar a tarefa com a versao nova; vale para qualquer IA (Claude, Codex ou outra). Bloqueio: nenhuma tarefa comeca (nem analise que leve a escrita) com versao diferente da oficial. A propria IA atualiza por conta propria, sem pedir ao responsavel: atualiza o marketplace e o plugin em todos os escopos instalados (usuario e projeto) e confere com a listagem. Se o comando de atualizacao nao estiver no PATH, procurar o cliente embutido da superficie (ex.: o claude do app desktop); se ainda assim nao atualizar, parar e pedir ao responsavel, sem trabalhar na versao velha. Se a atualizacao so vale apos reiniciar, avisar e esperar a nova sessao. So no inicio da execucao: no meio de um lote, terminar o lote antes de atualizar. Conferir a distribuicao e as skills disponiveis pelo catalogo abaixo. Instalacao/atualizacao e recarga seguem [INSTALL.md](INSTALL.md). Ler arquivo nao comprova plugin ou hook ativo.
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
| [romulo-motion-principles](skills/romulo-motion-principles/SKILL.md) | Criar/revisar movimento no recorte de interface autorizado | Pacote completo Design Motion Principles, acessibilidade e movimento com finalidade na stack aprovada. |
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

## Entrega rapida, qualidade e rastreabilidade

Tarefas logicas usam issue e entregas usam PR vinculada segundo `romulo-construir`, preservando o prototipo localhost e os checks obrigatorios. Consulta segue mapa/DNA -> documento dono -> links qualificados de issue/PR/commit -> consumidores atingidos, conforme [documentacao](references/DOCUMENTACAO.md#rastreabilidade-dna-issue-pr-e-commit). Tickets rastreiam trabalho; documento vigente define regra.

Qualidade/testes por perfil compativel do projeto em `romulo-verificar`; observabilidade em `romulo-seguranca`; estados visuais em `romulo-interface` e movimento no pacote importado `romulo-motion-principles`. Essas regras nao instalam servicos/dependencias nem reformam telas antigas automaticamente. Definir comandos reais no documento/processo local existente e aplicar incrementalmente ao alcance autorizado.

## Uso de recursos externos
Skills instaladas, recursos embutidos e conectores nao concedem autorizacao de escrita. `init`, geradores de plugins/skills/documentos, memorias, Figma e demais ferramentas tambem passam pelo gate de artefatos de `romulo-analisar` quando usados neste trabalho. Nao fabricar CLAUDE.md longo, planos ou copias de regras por sugestao automatica.

Nao remover plugins ou mudar permissoes por uma lista colada no chat. Confirmar superficie, origem, escopo, uso e autorizacao. Recurso opcional sem uso pode ser desabilitado no escopo adequado apos decisao; nao enfraquecer revisao de seguranca nem permissoes para reduzir avisos. Delegacao exige autorizacao do responsavel; no fluxo iterativo autorizado, separar construtor e documentador conforme `romulo-prototipo-real`, preservando o revisor independente quando aplicavel.

## Validacao e limites
Executar `python3 scripts/validate_standard.py` e `python3 -m unittest discover -s tests -v`, com Python 3.10+ (usar `python` no Windows quando apropriado). Sem dependencias Python externas. O validador confere estrutura, catalogo, links, templates e roteamento textual; nao impede toda escrita do sistema operacional, nao instala plugins e nao comprova obediencia do modelo ou qualidade de telas. Bloqueio mecanico de escrita exige hook/permissao/sandbox do ambiente, implantado e testado com autorizacao propria; nao alegar blindagem apenas pelo Markdown.

## Contratos consultados por efeito

Correcao fiel: DNA -> trecho vigente no dono -> codigo/consumidores -> teste atingido. Evolucao: briefing visual, fluxo do app e TRD pertinentes; reconstrucao: revisao exata de fontes/assets e guia modular com contratos/RPCs/dados/seguranca/ordem/aceite. Conteudo e destinos em [references/DOCUMENTACAO.md](references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao); implementacao e limpeza em `romulo-construir`, verificacao/fiscal em `romulo-verificar`. Resumo rapido e referencia ao detalhe, sem retirar mapas nominais ou checks locais.

A tela do prototipo aprovado ja e documentada no dono vigente, com estado PROTOTIPO, DNAs, regras, revisao/fontes e simulacoes/contratos a integrar. Conversao atualiza a mesma fonte e verifica prototipo x real, sem refazer entendimento nem duplicar manual. Falta indispensavel e resolvida antes da implementacao dependente; a entrega visual local continua rapida conforme `romulo-prototipo-real`.

## Migracao 1.12.1 -> 1.12.2

Pedido da [issue #7](https://github.com/romulorenatoss-maker/romulo-dev-standard/issues/7), autorizado pelo responsavel com 0393 para aplicar e publicar o patch aprovado. [references/SEGURANCA.md](references/SEGURANCA.md#auditoria-dirigida--oito-riscos) concentra oito riscos, controles, evidencia e limites; `romulo-seguranca` fornece a invocacao de auditoria em leitura e `romulo-verificar` confere fechamento/reteste atingido. Nao exige oito suites em todo ajuste nem cria scanner, dependencia, permissao ou nova skill.

Alcance: essas tres fontes, este README e os tres manifests existentes (plugin.json, .claude-plugin/plugin.json e .codex-plugin/plugin.json), sete caminhos centrais; nenhum codigo de consumidor alterado. Fonte d096da6bc2e7edb48633e3b6814612d1d822f35d e recibo8c3cf6e integrados na PR #8, maincbd95b7acdd5dfaa54d3382d80f1eaeec4eb24cc; workflow38226716729 concluido com sucesso e fiscal COMMIT OK. Os comandos de verificacao continuam os deste README.

Compatibilidade: sem mudanca de stack, templates, nomes, catalogo ou comandos centrais. Terminar lotes na revisao fixada; apos publicacao confirmada, atualizar/recarregar conforme [INSTALL.md](INSTALL.md) e comprovar ativacao. Consumidores preservam guardas/escopo local; auditoria nao abre .env/backup/chaves, modifica dados/roles, executa ataque em producao ou autoriza correcao fora do pedido.

Fonte, runtime e aplicacao ativa tem evidencias separadas; resultado estrutural ou conversa nao certifica seguranca do produto nem obediencia do modelo. Publicacao, instalacao e recarga precisam de comprovacao propria; rollback e nova PR localizada, preservando alteracoes posteriores e controles legitimos.

Registro: QUEM: Codex, seguranca_sistema e fiscal independente revisor_candidato. COMMITS: [PR #8 / commits](https://github.com/romulorenatoss-maker/romulo-dev-standard/pull/8/commits), fonte d096da6bc2e7edb48633e3b6814612d1d822f35d. FEZ: patch aprovado dos oito riscos, invocacao de auditoria e fechamento por efeito. CONFERIU: fonte correspondente ao patch exato, sete caminhos, validador PASSOU, 26 cenarios aprovados e dois symlink NAO_EXECUTADO no Windows; fiscal sem bloqueio no candidato. CONSUMIDORES: gerenciadores Codex e Claude confirmaram1.12.2 instalada/habilitada (Claude user/project); novas sessoes conferiram12skills, Claude carregou romulo-seguranca pela ferramenta Skill. FALTA: recarga de conversas antigas nao comprovada; isso nao certifica hooks, obediencia ou runtime dos produtos. DESFAZER: nova PR localizada, preservando trabalho posterior.

## Migracao 1.12.0 -> 1.12.1

Pedido da [issue #5](https://github.com/romulorenatoss-maker/romulo-dev-standard/issues/5), autorizado com 0393 nesta conversa. Explicita divisao/nomes/limites de JS escrito a mao, cabecalho e DNA junto do trecho funcional, com fonte reutilizavel do prototipo ao real. Donos: [arquitetura](references/ARQUITETURA.md#javascript-por-responsabilidade-e-tamanho) e [documentacao interna](references/DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo). Nao instala linter/framework, muda stack, refatora consumidores automaticamente ou altera interface aprovada.

Registro desta revisao: QUEM: Codex, fiscal independente fiscal_salvamento. COMMITS: [PR #6 / commits](https://github.com/romulorenatoss-maker/romulo-dev-standard/pull/6/commits), fonte 834e0805be766208982221bd05d65caaa2a8c40f e recibo na mesma PR. FEZ: regras e referencias de JS/cabecalho/DNA/prototipo, nove arquivos centrais; nenhum codigo de consumidor alterado. CONFERIU: validador e diff sem erros, suite local26 cenarios PASSOU e2 symlink NAO_EXECUTADO no Windows, fiscal COMMIT OK nos nove hashes; [checks da PR](https://github.com/romulorenatoss-maker/romulo-dev-standard/pull/6/checks) identificam a revisao CI. FALTA: ativacao comprovada de sessoes abertas e ajustes dos consumidores em lotes proprios; texto/CI nao certificam obediência do modelo nem produto. DESFAZER: nova PR localizada, preservando trabalho posterior e compatibilidade dos consumidores.

## Migracao 1.11.0 -> 1.12.0

Revisao da [issue #3](https://github.com/romulorenatoss-maker/romulo-dev-standard/issues/3), autorizada pelo responsavel com 0393 em 11/10/2026. Centraliza briefing, fluxo/TRD e guia de reconstrucao nos donos existentes, explicita RPCs e rastreio bidirecional, preserva o fiscal e condensa narrativa repetida. Nao altera os contratos de arquitetura/dados/seguranca, stack, dados, IDs, guardas, aprovacao de layout ou alvo PROTOTIPO/REAL. Instalar o metodo nao cria documentos vazios, muda telas ou configura protecao/CI/deploy do consumidor.

Terminar lotes em curso na revisao fixada. Depois da publicacao autorizada, atualizar pacote e comprovar recarga conforme [INSTALL.md](INSTALL.md); migracao de AGENTS protegido ou guarda local exige autorizacao propria. Adocao/limpeza no consumidor precisa conferir suas fontes, instrumentos e referencias; nao apagar manifests/recibos por volume. Versionamento nao comprova ativacao em sessoes abertas nem que todo modulo esta documentado.

Registro desta revisao: QUEM: Codex, com fiscal independente. COMMITS: [PR #4 / commits](https://github.com/romulorenatoss-maker/romulo-dev-standard/pull/4/commits), vinculada a [issue #3](https://github.com/romulorenatoss-maker/romulo-dev-standard/issues/3). FEZ: consulta, contratos de projeto/reconstrucao, limpeza da narrativa central e correcao do fechamento parcial de prototipo; nenhuma tela/codigo/banco de consumidor alterados. CONFERIU: validador e suite locais (26 cenarios aprovados, 2 symlink nao executados no Windows), diff sem erros; fiscal identificou risco de perder detalhe aprovado ainda nao convertido, corrigido e reconferido sem bloqueio textual restante no recorte. CI de cada commit consta na [PR](https://github.com/romulorenatoss-maker/romulo-dev-standard/pull/4/checks). FALTA: recarga comprovada de sessoes abertas e adocao/testes dos consumidores; revisao textual e CI da distribuicao nao certificam produto ou comportamento de modelos. DESFAZER: reversao por PR localizada preservando trabalho posterior e migracao pertinente dos consumidores.

Migracoes anteriores ficam no [README versionado da 1.11.0](https://github.com/romulorenatoss-maker/romulo-dev-standard/blob/bc7bc0948808c6009792447a2ebb6ecbb52139d5/README.md), sem segunda versao de regras na leitura corrente. A entrega 1.11.0 e rastreavel pela [PR #2](https://github.com/romulorenatoss-maker/romulo-dev-standard/pull/2); regras vigentes estao nas fontes donas do catalogo e a compatibilidade dos instaladores em INSTALL.md.

## Base da analise de equipes e entregas

As praticas foram confrontadas com [qualidade documental DORA](https://dora.dev/capabilities/documentation-quality/), [gestao de mudancas de banco DORA](https://dora.dev/capabilities/database-change-management/), [engenharia de releases Google SRE](https://sre.google/sre-book/release-engineering/) e [CODEOWNERS/revisao GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). Essas fontes fundamentam consulta util, reproducao, compatibilidade e verificacoes; nao ampliam autorizacao nem prometem ausencia de erros. Nao copiar infraestrutura de grande empresa para resolver um ajuste local.
