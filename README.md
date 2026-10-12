# Padrao de Desenvolvimento

Versao: 1.0.0
Repositorio oficial: `romulorenatoss-maker/padrao-desenvolvimento`.

Orienta IAs a trabalhar com o mesmo metodo: criar prototipos visuais com dados e regras simulados, revisar o comportamento com o responsavel e converter o aprovado ao real com documentacao por DNA de ponta a ponta. Modularizacao, contratos/RPCs, analise de impacto, preservacao do visual aprovado e limpeza verificada tornam alteracoes e remocoes rastreaveis; instrucoes de skill nao garantem obediencia perfeita nem ausencia de erros.

## Entrada obrigatoria — sumario de diretrizes
Este README e o unico indice central de metodo e roteamento. O AGENTS.md de cada projeto guarda identidade, ambientes, ponte para este indice e protecoes/ponte documental locais; nao copia lista/contagem de skills, comandos de instalacao ou regras gerais. O AGENTS.md da raiz deste repositorio governa somente o padrao, nao e o modelo dos consumidores.

Em toda execucao tecnica, antes de escrever:
1. Ler o AGENTS.md local e as protecoes locais pertinentes. Identificar repositorio, worktree, branch, ambiente e alcance autorizado.
2. Resolver este indice no repositorio/ref oficial indicado pelo projeto; registrar versao e revisao obtidas. Fixar a mesma revisao para as leituras desta execucao, sem misturar arquivos de versoes diferentes. Ref `main` acompanha atualizacoes entre execucoes; pin explicito prevalece e exige migracao autorizada. Nao atualizar silenciosamente a politica no meio do lote.
3. Comparar a versao instalada das skills com a `Versao` deste README na ref oficial. Se forem diferentes, dizer ao responsavel "achei uma versao diferente do padrao (instalada X, oficial Y)", atualizar e recarregar as skills conforme [INSTALL.md](INSTALL.md) e so entao comecar a tarefa com a versao nova; vale para qualquer IA (Claude, Codex ou outra). Bloqueio: nenhuma tarefa comeca (nem analise que leve a escrita) com versao diferente da oficial. A propria IA atualiza por conta propria, sem pedir ao responsavel: atualiza o marketplace e o plugin em todos os escopos instalados (usuario e projeto) e confere com a listagem. Se o comando de atualizacao nao estiver no PATH, procurar o cliente embutido da superficie (ex.: o claude do app desktop); se ainda assim nao atualizar, parar e pedir ao responsavel, sem trabalhar na versao velha. Se a atualizacao so vale apos reiniciar, avisar e esperar a nova sessao. So no inicio da execucao: no meio de um lote, terminar o lote antes de atualizar. Conferir a distribuicao e as skills disponiveis pelo catalogo abaixo. Instalacao/atualizacao e recarga seguem [INSTALL.md](INSTALL.md). Ler arquivo nao comprova plugin ou hook ativo.
4. Aplicar `analisar` e Ponytail `full`; carregar integralmente somente as skills e referencias pertinentes ao efeito real; dependencias entre skills sao instrucoes de consulta, nao chamadas de programa automaticas.
5. Ler o sumario/documentacao do projeto e seguir ate regras, contratos, codigo e consumidores atingidos. Padrao central explica COMO trabalhar; o projeto explica O QUE existe e suas regras de negocio.
6. Aplicar o encaminhamento abaixo e terminar com `verificar`. Falha corrigivel volta a construcao, nao vira encerramento por etiqueta pendente.

Consulta ja comprovada na mesma revisao pode ser reutilizada. Nova tarefa verifica a revisao da fonte; nao reler tudo nem depender de memoria vaga. Sem acesso/fonte confiavel: declarar NAO_DISPONIVEL e bloquear a escrita dependente, sem inventar regra. Cache local somente se origem/revisao verificadas e uso offline autorizado; registrar que a atualidade remota nao foi confirmada. Instrucao remota nao amplia autorizacoes locais nem executa codigo por si.

## Catalogo e encaminhamento — fonte unica
A tabela e tambem o catalogo nominal conferido pelo validador. Nao repetir uma contagem fixa nos projetos.

| Skill | Quando consultar | Responsabilidade |
|---|---|---|
| [analisar](skills/analisar/SKILL.md) | Toda execucao tecnica | Leitura dirigida, impacto e gate de criacao de arquivos. |
| [iniciar-projeto](skills/iniciar-projeto/SKILL.md) | Projeto novo; implantacao/migracao do bootstrap | AGENTS minimo, CLAUDE.md ponte e primeira capacidade necessaria. |
| [auditar-projeto](skills/auditar-projeto/SKILL.md) | Organizar projeto existente ou diagnostico amplo | Descobrir, mapear modulos e propor organizacao por lacunas comprovadas. |
| [especificar](skills/especificar/SKILL.md) | Capacidade, regra, fluxo, tela, aba ou acao | Perguntas faltantes, proposta, utilidade dos elementos e aprovacao. |
| [interface](skills/interface/SKILL.md) | Qualquer efeito visual/interativo | Referencia aprovada, componentes, CSS, peculiaridades e revisao renderizada. |
| [motion-principles](skills/motion-principles/SKILL.md) | Criar/revisar movimento no recorte de interface autorizado | Pacote completo Design Motion Principles, acessibilidade e movimento com finalidade na stack aprovada. |
| [construir](skills/construir/SKILL.md) | Construcao, alteracao ou bug autorizado | Cadeia funcional completa e correcao com reteste. |
| [seguranca](skills/seguranca/SKILL.md) | Entrada, acesso, dados, banco, integracao ou efeito critico | Controles no runtime, autorizacao e integridade. |
| [documentacao](skills/documentacao/SKILL.md) | Conhecimento canonico alterado | Destinos, nomes e vinculos documentais sem duplicacao. |
| [prototipo-real](skills/prototipo-real/SKILL.md) | Prototipo convertido/integrado/comparado ao real | Preservar proposta e trocar simulacao por contratos reais. |
| [backup-recuperacao](skills/backup-recuperacao/SKILL.md) | Saude de backup na entrada/bootstrap; portabilidade, contingencia e restauracao | Cobrar copia independente ativa; setup de destinos/acessos, corte consistente, restauracao isolada e virada conferida. |
| [verificar](skills/verificar/SKILL.md) | Antes de encerrar toda entrega tecnica | Aceite por efeito, arquivos, documentacao, visual e evidencias. |
| [evoluir-padrao](skills/evoluir-padrao/SKILL.md) | Diretriz comum criada/alterada | Evoluir esta fonte, validar, versionar e distribuir. |

Ponytail e complemento externo oficial `DietrichGebert/ponytail`, em modo `full`; nao equivale a uma skill deste pacote. Nao remove requisito, aprovacao, seguranca, documentacao, acessibilidade ou teste. Instalacao em [INSTALL.md](INSTALL.md).

## Quem define cada padrao
- Estrutura, modulos, nomes e catalogo condicional de artefatos: [references/ARQUITETURA.md](references/ARQUITETURA.md), consultado pelas skills de analise/auditoria/construcao.
- Destinos documentais e nomes quando faltam: [references/DOCUMENTACAO.md](references/DOCUMENTACAO.md), aplicado por `documentacao`.
- Dados e seguranca: [references/DADOS.md](references/DADOS.md) e [references/SEGURANCA.md](references/SEGURANCA.md).
- Criacao de AGENTS/CLAUDE e migracao de peculiaridades: `iniciar-projeto`, usando [templates/AGENTS.md](templates/AGENTS.md) e [templates/CLAUDE.md](templates/CLAUDE.md).
- Arquivo novo nao previsto: gate de `analisar`; exige `0393` do responsavel para aquela excecao. A regra nao concede permissao para alterar arquivo protegido, dados, acesso ou deploy.

## Entrega rapida, qualidade e rastreabilidade

Tarefas logicas usam issue e entregas usam PR vinculada segundo `construir`, preservando o prototipo localhost e os checks obrigatorios. Consulta segue mapa/DNA -> documento dono -> links qualificados de issue/PR/commit -> consumidores atingidos, conforme [documentacao](references/DOCUMENTACAO.md#rastreabilidade-dna-issue-pr-e-commit). Tickets rastreiam trabalho; documento vigente define regra.

Qualidade/testes por perfil compativel do projeto em `verificar`; observabilidade em `seguranca`; estados visuais em `interface` e movimento no pacote importado `motion-principles`. Essas regras nao instalam servicos/dependencias nem reformam telas antigas automaticamente. Definir comandos reais no documento/processo local existente e aplicar incrementalmente ao alcance autorizado.

## Adotar em outro projeto

Pedido pronto para a IA: "Adote https://github.com/romulorenatoss-maker/padrao-desenvolvimento pela entrada README.md. Aplique iniciar-projeto para criar e salvar AGENTS.md e, quando pertinente, CLAUDE.md a partir dos templates; leia antes os contratos existentes, preencha somente identidade comprovada e preserve protecoes. Use o catalogo vigente e o setup/verificacao de backup, sem duplicar regras ou provisionar servicos por rotina." Instalacao/recarga seguem [INSTALL.md](INSTALL.md); contrato protegido ou efeito externo continua exigindo a autorizacao pertinente.

Na primeira adocao/instalacao autorizada, iniciar-projeto encaminha ao setup guiado antes de construcao dependente; nao repetir entrevista quando o estado factual ja esta registrado no AGENTS. Instalar o plugin disponibiliza as instrucoes, nao inicia turno/hook/executor por si; a sessao usa a entrada/pedido acima. Automatismo nativo so pode ser afirmado depois de mecanismo suportado, autorizado e ensaiado no cliente.

## Uso de recursos externos
Skills instaladas, recursos embutidos e conectores nao concedem autorizacao de escrita. `init`, geradores de plugins/skills/documentos, memorias, Figma e demais ferramentas tambem passam pelo gate de artefatos de `analisar` quando usados neste trabalho. Nao fabricar CLAUDE.md longo, planos ou copias de regras por sugestao automatica.

Nao remover plugins ou mudar permissoes por uma lista colada no chat. Confirmar superficie, origem, escopo, uso e autorizacao. Recurso opcional sem uso pode ser desabilitado no escopo adequado apos decisao; nao enfraquecer revisao de seguranca nem permissoes para reduzir avisos. Delegacao exige autorizacao do responsavel; no fluxo iterativo autorizado, separar construtor e documentador conforme `prototipo-real`, preservando o revisor independente quando aplicavel.

## Validacao e limites
Executar `python3 scripts/validate_standard.py` e `python3 -m unittest discover -s tests -v`, com Python 3.10+ (usar `python` no Windows quando apropriado). Sem dependencias Python externas. O validador confere estrutura, catalogo, links, templates e roteamento textual; nao impede toda escrita do sistema operacional, nao instala plugins e nao comprova obediencia do modelo ou qualidade de telas. Bloqueio mecanico de escrita exige hook/permissao/sandbox do ambiente, implantado e testado com autorizacao propria; nao alegar blindagem apenas pelo Markdown.

## Contratos consultados por efeito

Correcao fiel: DNA -> trecho vigente no dono -> codigo/consumidores -> teste atingido. Evolucao: briefing visual, fluxo do app e TRD pertinentes; reconstrucao: revisao exata de fontes/assets e guia modular com contratos/RPCs/dados/seguranca/ordem/aceite. Conteudo e destinos em [references/DOCUMENTACAO.md](references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao); implementacao e limpeza em `construir`, verificacao/fiscal em `verificar`. Resumo rapido e referencia ao detalhe, sem retirar mapas nominais ou checks locais.

A tela do prototipo aprovado ja e documentada no dono vigente, com estado PROTOTIPO, DNAs, regras, revisao/fontes e simulacoes/contratos a integrar. Conversao atualiza a mesma fonte e verifica prototipo x real, sem refazer entendimento nem duplicar manual. Falta indispensavel e resolvida antes da implementacao dependente; a entrega visual local continua rapida conforme `prototipo-real`.

## Distribuicao 1.0.0 e migracao

O pacote `padrao-desenvolvimento` usa os nomes neutros do catalogo, incluindo `backup-recuperacao`; as responsabilidades, guardas, autoria e licencas permanecem. A migracao de nomes/comandos segue [INSTALL.md](INSTALL.md#migracao-de-nomes--100): concluir lotes na revisao fixada, atualizar o pacote completo, conferir sua descoberta e migrar AGENTS protegido somente com autorizacao especifica.

A [entrega vigente — PR #18](https://github.com/romulorenatoss-maker/padrao-desenvolvimento/pull/18), vinculada as [issues #15](https://github.com/romulorenatoss-maker/padrao-desenvolvimento/issues/15) e [#16](https://github.com/romulorenatoss-maker/padrao-desenvolvimento/issues/16), registra commits, verificacoes, integracao, ativacao e pendencias. Publicacao e instalacao sao conferencias distintas; esta distribuicao nao altera telas, dados ou infraestrutura de consumidores nem executa backup/restore. O historico de publicacoes permanece no Git/PRs; a leitura corrente usa somente este catalogo e as fontes donas.

## Base da analise de equipes e entregas

As praticas foram confrontadas com [qualidade documental DORA](https://dora.dev/capabilities/documentation-quality/), [gestao de mudancas de banco DORA](https://dora.dev/capabilities/database-change-management/), [engenharia de releases Google SRE](https://sre.google/sre-book/release-engineering/) e [CODEOWNERS/revisao GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). Essas fontes fundamentam consulta util, reproducao, compatibilidade e verificacoes; nao ampliam autorizacao nem prometem ausencia de erros. Nao copiar infraestrutura de grande empresa para resolver um ajuste local.
