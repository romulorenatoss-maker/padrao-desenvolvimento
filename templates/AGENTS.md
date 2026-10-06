# AGENTS.md

## Identidade local
PROJETO: <nome>
REPOSITORIO_OFICIAL: <owner/repo>
BRANCH_OFICIAL: main
AMBIENTE_PRODUCAO: <quando aplicavel>

Antes de qualquer escrita, confirmar projeto, repositorio, branch e ambiente atingido. Divergencia bloqueia a operacao afetada. Segredos nunca entram em codigo, documentacao, prompt, log ou Git.

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
