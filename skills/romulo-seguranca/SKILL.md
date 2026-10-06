---
name: romulo-seguranca
description: Use junto da skill principal quando a tarefa toca autenticacao, autorizacao, sessao, entrada, banco, upload, segredo, integracao, permissao, escopo, dados sensiveis ou efeitos financeiros/criticos.
---

# Romulo Seguranca

Seguranca deve existir no runtime, nao apenas na documentacao.

Conforme o caso, verifique: autenticacao central; autorizacao no servidor; permissao especifica; escopo por objeto/tenant/empresa; negacao por padrao; validacao de entrada; SQL parametrizado; saida contextual; CSRF quando pertinente; segredo fora do codigo; upload restrito; integracao com privilegio minimo; auditoria sem vazamento; transacao, unicidade, idempotencia e concorrencia.

Ocultar interface nao protege endpoint. Identificador vindo do cliente nao comprova propriedade. Cache nao cria autorizacao. Nao desligue RLS, autenticacao, constraints, hooks ou protecoes legitimas para fazer teste passar.

Permissao nova nao implica concessao automatica. Mudanca destrutiva exige identificacao do conjunto, dependencias, recuperacao e autorizacao especifica.

Teste proporcionalmente tanto o caminho permitido quanto a recusa relevante quando a garantia de acesso mudou.

Nunca exponha segredos em resposta, commit, log ou documentacao.

Reutilizar controles centrais por referencia; nao repetir politica generica em cada modulo. Campo do cliente nao comprova permissao, empresa, preco, credito, saldo ou MFA.
