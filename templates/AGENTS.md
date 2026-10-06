# AGENTS.md

## Identidade local
PROJETO: <nome>
REPOSITORIO_OFICIAL: <owner/repo>
BRANCH_OFICIAL: main
AMBIENTE_PRODUCAO: <quando aplicavel>

Antes de qualquer escrita, confirmar projeto, repositorio, branch e ambiente atingido. Divergencia bloqueia a operacao afetada. Segredos nunca entram em codigo, documentacao, prompt, log ou Git.

## Bootstrap obrigatorio (Codex e Claude Code, mesmo fluxo)
Padrao: https://github.com/romulorenatoss-maker/romulo-dev-standard
Ponytail: https://github.com/DietrichGebert/ponytail

Antes de qualquer tarefa tecnica, nesta ordem:
1. detectar a plataforma: Codex ou Claude Code;
2. verificar se as 9 skills `romulo-*` estao carregadas na sessao;
3. verificar se Ponytail esta carregado na sessao;
4. faltando algo: instalar automaticamente com os comandos da plataforma (abaixo), cada comando separado;
5. sem permissao para executar: mostrar somente os comandos da plataforma e PARAR;
6. apos instalar/atualizar: pedir nova sessao/reload e PARAR ate ela abrir;
7. continuar somente depois de confirmar nominalmente as skills carregadas.

Arquivo no GitHub ou no disco nao conta: vale somente skill descoberta/carregada pela sessao. Ja carregado na versao adequada: nao reinstalar. Procedimento documentado: nao perguntar como instalar.

### Codex
Padrao:
```
codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main
codex plugin add romulo-dev-standard@romulo-dev-standard
codex plugin list
```
Confirmar `romulo-dev-standard@romulo-dev-standard` installed e enabled. Versao mais nova:
```
codex plugin marketplace upgrade romulo-dev-standard
codex plugin add romulo-dev-standard@romulo-dev-standard
```
Ponytail:
```
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```
Depois: abrir `/hooks`, revisar e confiar nos hooks do Ponytail, iniciar nova thread/sessao.

### Claude Code
Um comando por vez:
```
/plugin marketplace add romulorenatoss-maker/romulo-dev-standard
```
```
/plugin install romulo-dev-standard@romulo-dev-standard
```
```
/plugin marketplace add DietrichGebert/ponytail
```
```
/plugin install ponytail@ponytail
```
Versao mais nova: `/plugin marketplace update romulo-dev-standard`. Depois: reiniciar/recarregar a sessao.

### Confirmacao
Skills obrigatorias: `romulo-analisar`, `romulo-iniciar-projeto`, `romulo-auditar-projeto`, `romulo-construir`, `romulo-seguranca`, `romulo-documentacao`, `romulo-prototipo-real`, `romulo-verificar`, `romulo-evoluir-padrao`.
- qualquer uma faltando: `ROMULO_STANDARD_NAO_DISPONIVEL`; nao agir como se o padrao estivesse ativo;
- Ponytail indisponivel: `PONYTAIL_NAO_DISPONIVEL`; nao fingir execucao.

Bloqueio so de instalacao: mostrar os comandos primeiro, sem explicacao longa. Nao copiar skills manualmente para esconder falha do plugin.

### Fonte de verdade
- AGENTS.md local: somente peculiaridades do projeto (identidade, repositorio, ambiente, banco/deploy, autorizacoes, regras de negocio).
- Romulo Dev Standard: metodo comum. Ponytail: simplificacao complementar.

Nao copiar o conteudo das skills para o AGENTS.md.

## Padrao obrigatorio
Todos os projetos seguem a mesma arquitetura conceitual e o mesmo processo Romulo Dev Standard. Diferencas locais ficam apenas em identidade, infraestrutura, autorizacoes, guardas e regras de negocio especificas.

Em toda tarefa tecnica:
1. aplicar `romulo-analisar` antes de escrever;
2. aplicar Ponytail `full` (padrao em toda tarefa tecnica);
3. aplicar a skill Romulo correspondente ao tipo da operacao;
4. antes de concluir, aplicar `romulo-verificar`.

Roteamento:
- projeto novo/vazio/bootstrap -> `romulo-iniciar-projeto`;
- diagnostico/auditoria de sistema existente -> `romulo-auditar-projeto`;
- construcao, alteracao ou bug -> `romulo-construir`;
- autenticacao, autorizacao, dados sensiveis, entrada, upload ou integracao -> `romulo-seguranca` junto da skill principal;
- mudanca com efeito documental -> `romulo-documentacao`;
- prototipo -> implementacao real -> `romulo-prototipo-real`;
- fechamento -> `romulo-verificar`;
- mudanca de diretriz global do metodo -> `romulo-evoluir-padrao`.

Projeto vazio/sem estrutura funcional: `romulo-iniciar-projeto`, criando somente o necessario para a primeira capacidade real. Projeto existente: nao criar estrutura; `romulo-analisar` (ou `romulo-auditar-projeto` se amplo), preservar o que esta conforme e corrigir somente lacunas comprovadas.

Se uma skill obrigatoria nao estiver carregada, nao fingir que foi executada: instalar/atualizar pelo mecanismo suportado ou informar `NAO_DISPONIVEL`.

## Arquitetura comum
Todos os projetos usam estas responsabilidades conceituais:
- View/interface: apresentacao e interacao;
- Action/entrada: transporte, sessao, metodo e protecao aplicavel;
- Controller: normalizacao de entrada/saida;
- Service: regra, autorizacao, escopo e estado;
- Repository/contrato: persistencia e consultas autorizadas;
- Banco: integridade, constraints, transacoes e concorrencia aplicavel.

A stack pode materializar essas responsabilidades de forma idiomatica, mas nao pode deslocar regra critica para o frontend, usar autorizacao apenas visual ou contornar contratos de persistencia. Nao criar camada vazia.

## Regras invariantes
Responsabilidade antes de pasta. Reconhecer antes de criar. Reutilizar antes de duplicar. Aplicar a arquitetura comum sem fabricar estrutura sem uso.

A menor solucao deve cumprir integralmente o pedido; simplificacao nunca remove requisito aprovado, seguranca, documentacao necessaria, teste pertinente, acessibilidade ou autorizacao.

Seguranca e integridade sao aplicadas no runtime. Frontend nao concede autorizacao. Backend revalida efeitos oficiais. Banco protege invariantes pertinentes.

Documentacao acompanha a mudanca no mesmo lote, mas nao se cria documento por arquivo, funcao, botao ou agente. Usar o destino canonico do projeto; se nao existir, criar somente o minimo necessario para a responsabilidade real.

Ausencia de evidencia = `NAO_VERIFICADO`, nunca PASSOU. Estados: `PASSOU`, `FALHOU`, `NAO_EXECUTADO`, `NAO_SE_APLICA`.

Prototipo define proposta, nao comprova backend, persistencia ou seguranca. Dados ficticios nunca migram para producao.

Nao apagar dados persistentes, executar migracao destrutiva, publicar, conceder permissoes, commitar ou fazer push sem a autorizacao exigida pelo projeto.

## Evolucao do padrao
Se uma diretriz comum a todos os projetos precisar mudar, nao alterar varios AGENTS.md. Usar `romulo-evoluir-padrao`, alterar primeiro a skill/reference/template dona da regra em `romulorenatoss-maker/romulo-dev-standard`, versionar, validar, publicar e atualizar o plugin nos consumidores. AGENTS.md local recebe apenas peculiaridades locais.

## Regras especificas deste projeto
<preencher somente identidade, infraestrutura, regras de negocio, docs canonicas, testes, deploy, autorizacoes e guardas peculiares ao projeto>
