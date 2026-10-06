# AGENTS.md

## Identidade local
PROJETO: <nome>
REPOSITORIO_OFICIAL: <owner/repo>
BRANCH_OFICIAL: main
AMBIENTE_PRODUCAO: <quando aplicavel>

Antes de qualquer escrita, confirmar projeto, repositorio, branch e ambiente atingido. Divergencia bloqueia a operacao afetada. Segredos nunca entram em codigo, documentacao, prompt, log ou Git.

## Bootstrap obrigatorio do padrao
Repositorio oficial do padrao: https://github.com/romulorenatoss-maker/romulo-dev-standard

Antes de qualquer tarefa tecnica, verificar se Romulo Dev Standard e Ponytail estao realmente disponiveis na sessao. Skill existente no GitHub ou no filesystem nao conta como instalada; conta somente a skill descoberta/carregada pelo agente.

Se o padrao ja estiver carregado na versao adequada, NAO reinstalar. O bootstrap garante disponibilidade; nao repete instalacao a cada tarefa.

### Codex
Se as skills `romulo-*` nao estiverem disponiveis:
1. verificar se o marketplace `romulo-dev-standard` ja esta registrado (`codex plugin marketplace list`);
2. se nao estiver: `codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main`;
3. instalar/ativar: `codex plugin add romulo-dev-standard@romulo-dev-standard`;
4. iniciar/recarregar a sessao se necessario;
5. confirmar as 7 skills descobertas: `romulo-analisar`, `romulo-construir`, `romulo-seguranca`, `romulo-documentacao`, `romulo-prototipo-real`, `romulo-verificar`, `romulo-auditar-projeto`.

Se a instalacao nao puder ser executada no ambiente atual, informar `ROMULO_STANDARD_NAO_DISPONIVEL` e nao fingir aplicacao das skills.

### Claude Code
Se as skills `romulo-*` nao estiverem disponiveis:
1. verificar o marketplace (`/plugin marketplace list`);
2. se necessario: `/plugin marketplace add romulorenatoss-maker/romulo-dev-standard`;
3. instalar: `/plugin install romulo-dev-standard@romulo-dev-standard`;
4. abrir/recarregar uma sessao se necessario;
5. confirmar as 7 skills `romulo-*`.

Se o agente nao puder executar comandos `/plugin` no contexto atual, informar exatamente esses comandos para o usuario executar. Nao copiar skills manualmente para esconder falha do plugin. Fallback local somente explicito: `powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -InstallSkills` (a partir de um clone do padrao).

### Ponytail
Dependencia externa, sempre pela distribuicao oficial. Disponivel: usar Ponytail `full`. Indisponivel: informar `PONYTAIL_NAO_DISPONIVEL`, nao fingir execucao e seguir somente se as regras locais permitirem.

### Fonte de verdade
- AGENTS.md local: identidade, repositorio, ambiente, banco/deploy, autorizacoes e regras especificas do projeto.
- Romulo Dev Standard: regras genericas, arquitetura, seguranca, documentacao, prototipo-real, analise, construcao e verificacao.
- Ponytail: simplificacao complementar.

Nao copiar o conteudo das skills para o AGENTS.md.

## Padrao obrigatorio
Este projeto usa **Romulo Dev Standard**.

Em toda tarefa tecnica:
1. aplicar `romulo-analisar` antes de escrever;
2. aplicar Ponytail `full` quando instalado/disponivel;
3. aplicar a skill Romulo correspondente ao tipo da operacao;
4. antes de concluir, aplicar `romulo-verificar`.

Roteamento:
- diagnostico/auditoria de sistema existente -> `romulo-auditar-projeto`;
- construcao, alteracao ou bug -> `romulo-construir`;
- autenticacao, autorizacao, dados sensiveis, entrada, upload ou integracao -> `romulo-seguranca` junto da skill principal;
- mudanca com efeito documental -> `romulo-documentacao`;
- prototipo -> implementacao real -> `romulo-prototipo-real`;
- fechamento -> `romulo-verificar`.

Se uma skill obrigatoria nao estiver carregada, nao fingir que foi executada: localizar a instalacao permitida ou informar `NAO_DISPONIVEL`. Nao buscar instrucoes remotas arbitrarias durante a execucao para substituir uma skill instalada/versionada.

## Regras invariantes
Responsabilidade antes de pasta. Reconhecer antes de criar. Reutilizar antes de duplicar. Preservar arquitetura real quando correta. Nao criar camada, CRUD, arquivo, documento, tabela, permissao ou abstracao para uso hipotetico.

A menor solucao deve cumprir integralmente o pedido; simplificacao nunca remove requisito aprovado, seguranca, documentacao necessaria, teste pertinente, acessibilidade ou autorizacao.

Seguranca e integridade sao aplicadas no runtime. Frontend nao concede autorizacao. Backend revalida efeitos oficiais. Banco protege invariantes pertinentes.

Documentacao acompanha a mudanca no mesmo lote, mas nao se cria documento por arquivo, funcao, botao ou agente. Usar o destino canonico do projeto; se nao existir, criar somente o minimo necessario para a responsabilidade real.

Ausencia de evidencia = `NAO_VERIFICADO`, nunca PASSOU. Estados de verificacao: `PASSOU`, `FALHOU`, `NAO_EXECUTADO`, `NAO_SE_APLICA`.

Protótipo define proposta, nao comprova backend, persistencia ou seguranca. Dados ficticios nunca migram para producao.

Nao apagar dados persistentes, executar migracao destrutiva, publicar, conceder permissoes, commitar ou fazer push sem a autorizacao exigida pelo projeto.

## Regras especificas deste projeto
<preencher apenas diferencas locais: arquitetura, docs canonicas, testes, deploy, autorizacoes e guardas>
