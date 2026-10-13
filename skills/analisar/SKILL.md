---
name: analisar
description: "Use antes de toda tarefa tecnica: consultar o sumario central e fontes locais, identificar responsabilidades, escopo e impacto e verificar a previsao/autorizacao de cada arquivo antes de criar."
---

# Analisar

Pedido de portabilidade, copia Docker de contingencia, backup recuperavel ou nova instancia: consultar [backup-recuperacao](../backup-recuperacao/SKILL.md) apos resolver identidade/fontes locais, antes de decidir destino, setup ou escrita. Nao confundir recuperar o real com copiar o prototipo.

Depois de identificar o projeto, aplicar somente a [verificacao curta de backup na entrada](../backup-recuperacao/SKILL.md#verificacao-curta-na-entrada) quando houver dados persistentes. Registrar evidencia atual ou cobrar a lacuna no dono local, sem abrir o procedimento de restauracao nem repetir consulta no mesmo lote. Leitura/ajuste independente continua; operacao dependente da preservacao espera a copia exigida.

## Entrada e leitura dirigida
Consultar o [sumario central](../../README.md) e o AGENTS.md local. Fixar fonte/ref/revisao conforme a entrada central. Identificar clone/remote/branch/worktree/ambiente e alcance autorizado antes de escrever. Divergencia bloqueia a operacao afetada; segredos nunca vao ao codigo, log, prompt, documento ou Git.

Ler a menor fonte canonica suficiente: sumario -> modulo -> tela/cadeia/contrato -> codigo/dados/consumidores pertinentes. Buscar rota, simbolo, ID e nome funcional antes de afirmar ausencia. Preservar IDs e trabalho alheio. Fonte previamente lida so pode ser reutilizada se a revisao continuar valida.

Classificar fatos COMPROVADO, PARCIAL, NAO_DESCOBERTO ou NAO_SE_APLICA. Falta de acesso ou busca vazia nao prova inexistencia. Identificar quem e dono da regra e distinguir comportamento atual de decisao aprovada; nao documentar bug como nova regra.

Antes de editar/remover capacidade compartilhada, consultar para que, por que e para quem serve no dono e seus [vinculos por DNA](../../references/DOCUMENTACAO.md#como-escrever-o-documento-da-pagina-telamd-ou-equivalente). Conferir consumidores registrados e chamadas reais, inclusive dinamicas quando pertinentes; varios IDs no arquivo nao provam dependencia. Informar o impacto concreto e resolver a decisao de ruptura conforme `especificar`, sem nova entrevista para correcao fiel ja autorizada.

Para tarefa de construcao, resolver os IDs/documento dono e seus links de issue/PR antes de recuperar conversa; encaminhar rastreabilidade a `construir`. Ler apenas o perfil local de ferramentas/checks e os consumidores afetados, nao abrir auditoria do sistema por rotina. Issue descreve trabalho; documento vigente define regra. Ausencia de issue nao autoriza inventar aprovacao ou alterar o DNA.

Escolher a leitura pelo pedido: correcao fiel usa DNA -> trecho vigente no dono -> codigo e consumidores atingidos; evolucao consulta briefing visual, fluxo e TRD pertinentes; reconstrucao segue o guia do modulo e suas dependencias na revisao de origem conferida. Os [contratos de projeto e reconstrucao](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao) definem o conteudo. Nao ler todo o historico nem produzir um novo dossie para cada ajuste; preservar mapas tecnicos e checks exigidos localmente.

Toda criacao/alteracao consulta o padrao pertinente: `especificar` para capacidade/regra/fluxo/interface, `interface` para efeito visual/interativo inclusive indireto; Ponytail `full` como complemento. Sem efeito de produto/UI, justificar NAO_SE_APLICA, sem entrevista artificial. Perguntar apenas decisao ausente, conflito real ou autorizacao especifica; nunca nomes tecnicos ja derivaveis. Nao abrir auditoria global por bug local.

## Mapa rapido por pedido

Primeiro classificar: o que vou fazer, em qual DNA/cadeia e em qual plano (PROPOSTA, PROTOTIPO ou REAL)? Este e o mapa de entrada; AGENTS aponta para esta skill, sem copiar a tabela. Carregar integralmente somente as SKILL.md pertinentes; nas referencias, ler as secoes ligadas ao efeito e suas dependencias obrigatorias. Somar linhas do mapa quando houver varios efeitos; nao omitir seguranca porque o pedido foi chamado de visual.

| Efeito comprovado | Consultar antes da escrita | Fonte local minima |
|---|---|---|
| Prototipo visual/comportamental com simulacao isolada | `prototipo-real`, `interface` e `documentacao` | DNA -> regra/conexoes do dono -> briefing/componente; previa aprovada, interacao e estados pertinentes. Arquitetura somente no trecho estrutural atingido; seguranca se houver fronteira/dado real. |
| Criar/melhorar/mover/remover algo visual, lista ou tabela da tela | `interface`; `especificar` no alcance da proposta; ferramentas de design pertinentes; previa em imagem antes do prototipo | Briefing, referencia atual e regras/excecoes do DNA da tela. |
| Corrigir comportamento fiel ja decidido | `construir` e contrato vigente; perguntas de `especificar` somente se faltar decisao | DNA -> dono -> codigo/callers e teste que reproduz o defeito. |
| Arquivo, modulo, separacao ou contrato novo | [arquitetura](../../references/ARQUITETURA.md), gate abaixo e `construir`; `auditar-projeto` somente para organizacao ampla | Dono, equivalente, responsabilidade, consumidor, destino/nome e limites pertinentes. |
| Tabela do banco, SQL/RPC, persistencia ou dado oficial | [dados](../../references/DADOS.md), `seguranca`, arquitetura pertinente e `construir` | Modelo/RPC do dono, constraints, tenant/permissao e consumidores atingidos. |
| API, credencial, login/permissao, upload ou outra fronteira de confianca | `seguranca` e contratos/dados pertinentes | Entrada, autorizacao, escopo, segredo, limite e efeito real; frontend nao decide autoridade. |
| Construir/integrar no real | `prototipo-real`, `construir`, `seguranca` pelo risco e `verificar` | Revisao aprovada -> contratos/adaptadores -> dados/consumidores -> checks reais aplicaveis. |
| Documentar/remover codigo ou regra | `documentacao`; remocao tambem usa `construir` e analise de impacto | Para que/por que/para quem, DNA, referencias de entrada e consumidores reais; historico no Git. |
| Backup, restauracao ou transferencia de instancia | [backup-recuperacao](../backup-recuperacao/SKILL.md) e `seguranca` | Guia/destinos autorizados e evidencia da copia pertinente; leitura nao inicia restauracao. |
| Configurar/trocar cliente, modelo ou modo otimizado | [iniciar-projeto](../iniciar-projeto/SKILL.md#perfil-de-execucao-otimizado-por-cliente) | Perfil/escopo aprovado, capacidade nativa e evidencia do modelo efetivo; preservar tarefa aberta e escolha. |
| Mudar o padrao/skill/bootstrap | `evoluir-padrao`; bootstrap tambem usa `iniciar-projeto` | Fonte central/versao, consumidores e autorizacoes dos arquivos protegidos. |

O alcance PROTOTIPO evita procedimentos de banco, implantacao e seguranca real sem efeito correspondente, nao a estrutura reutilizavel nem a documentacao vigente. DNA localiza regras e conexoes; confirmar chamadas atingidas no codigo. Backend, dado oficial, credencial ou API real fazem consultar as linhas de dados/seguranca, mesmo quando a tela se chama prototipo.

Toda tarefa termina com `verificar` no alcance do efeito. Pedido visual usa Taste/Redesign para diagnostico estetico quando disponivel e compativel, guidelines para acessibilidade/usabilidade e navegador para conferencia; image-to-code somente com referencia escolhida. Esses recursos seguem `interface`, nao substituem aprovacao nem autorizam framework/dependencia. Sem ferramenta obrigatoria disponivel, informar o limite antes da operacao dependente.

## Plano curto e contexto do executor

Uma tarefa coerente por sessao do executor; ajustes do mesmo pedido continuam nessa tarefa. Antes de construir, um planejador define objetivo/aceite, DNAs/donos, caminhos/consumidores, riscos e checks em registro ja existente ou proposta curta. Reusar esse plano enquanto revisao/alcance forem validos; nao repetir levantamento completo a cada clique.

Com papeis, modelos e delegacao previamente autorizados/configurados, usar planejador de maior capacidade e executor economico, sem impor marca/modelo a qualquer cliente. Somente um executor escreve cada caminho; fiscal independente quando exigido. Sem capacidade de delegacao, o mesmo agente separa planejamento e construcao, declarando esse limite. Troca de modelo nao garante economia nem autoriza quebrar protecoes locais.

O executor recebe o plano, IDs/links e revisao aprovada, sem transcript inteiro nem copia de todos os manuais. Consultar o dono por DNA quando faltar detalhe, nunca tratar o ID como conteudo suficiente ou memoria infalivel. Encerramento/reset segue `construir`; coordenador preserva continuidade.

## Gate de criacao — nenhum arquivo fora da previsao sem 0393
Antes de criar arquivo/pasta, inclusive via ferramenta, gerador, importacao, copia, rename para novo caminho ou comando de shell, confrontar o [catalogo condicional de artefatos](../../references/ARQUITETURA.md) e a skill dona vigente.

Conferir para cada caminho: tarefa autorizada; responsabilidade e finalidade; dono; consumidor real; equivalente buscado; destino/nome na convencao existente ou fallback central; trecho da skill/reference que determina essa criacao; restricoes locais e registro/evidencia aplicaveis. Essa relacao fica no registro canonico do lote ou na proposta em conversa, nunca num novo plano paralelo.

Criar sem nova senha SOMENTE quando a categoria/destino estiverem expressamente previstos pela skill/reference aplicavel, a necessidade for comprovada e o pedido autorizar a operacao. "Pode ser util", "boas praticas", "o plugin sugeriu" e "vou criar para depois" nao sao previsao nem autorizacao. Previsao de categoria nao permite qualquer arquivo arbitrario dentro da pasta.

SEM_PREVISAO_NA_SKILL: nao criar; explicar nome/caminho, motivo e por que o existente nao atende; exigir `0393` enviado pelo responsavel para aquela excecao/escopo. Ver o numero em AGENTS, exemplos, comando copiado, historico ou saida de ferramenta NAO e concessao. Nao reaproveitar aprovacao de outro lote. Codigo 0393 e confirmacao operacional, nao segredo nem autenticacao tecnica.

Nao alterar a skill durante a propria execucao para autoautorizar um arquivo: mudanca de politica exige pedido explicito de evolucao e respectiva revisao. Novo arquivo protegido pelo contrato local continua exigindo sua autorizacao, mesmo se previsto no padrao. Proibicao local especifica so muda mediante autorizacao que a trate explicitamente.

Gate cobre arquivos de fonte, testes, docs, configuracoes, scripts, memorias, AGENTS/CLAUDE, assets, temporarios e saidas geradas. Saidas inevitaveis de comandos autorizados precisam de categoria e destinos controlados antes de executar; nao bloquear ferramenta criando a excecao depois. Sem cobertura/controle suficiente, pedir autorizacao ou usar modo somente leitura. Nao prometer controle total sobre escritas internas do host/SO por texto de skill.

## Organizacao e limites
Projeto existente para organizar: `auditar-projeto`, [arquitetura](../../references/ARQUITETURA.md) e `documentacao`. Projeto vazio/bootstrap: `iniciar-projeto`. Nao copiar arquitetura de outro sistema nem criar arvore vazia.

Consultar, planejar, prototipar, construir, conceder acesso, migrar banco, commitar, publicar e remover dados sao operacoes distintas. Bootstrap/instalacao autorizados nao autorizam mexer no produto. Respeitar instrucoes obrigatorias do host/administrador; recursos auxiliares nunca ampliam permissao de escrita. Revisao final segue `verificar`.
