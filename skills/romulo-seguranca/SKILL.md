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

## Observabilidade compatível e sem vazamento

Operacoes oficiais precisam de evidencia operacional proporcional ao risco: resultado/erro sanitizado, duracao quando pertinente, correlation_id e identidade autorizada de modulo/entidade/usuario/tenant. Reutilizar logs/auditoria existentes; conectar navegador -> action -> service -> repository/API quando o fluxo justificar, sem gravar automaticamente payload, conversa, token ou dado pessoal. Auditoria de negocio e telemetria de diagnostico tem finalidades e retencoes distintas.

Definir no perfil local como coletar, consultar e alertar falhas relevantes; OpenTelemetry e uma opcao de instrumentacao/exportacao, nao armazena nem visualiza os dados sozinho. Sentry, Datadog e New Relic sao alternativas a avaliar por necessidade, suporte da stack, custo, privacidade e infraestrutura; nao instalar os tres nem duplicar instrumentacao por rotina. Usar apenas SDKs/endpoints e configuracoes autorizados e compativeis, credenciais no backend/gestor seguro. Disponibilidade, erros, latencia e falhas de integracao entram conforme o escopo real; sem alertas que ninguem recebe ou indicadores ficticios.

Configuracao exige alcance/aprovacao pertinentes para conta, gasto, envio/retencao de dados e ambiente; citar ferramenta na skill nao a instala. Preferir a menor instrumentacao que permita reproduzir/localizar a falha. Falha do exportador nao pode derrubar operacao nem levar segredo ao log; verificar sucesso, falha, sanitizacao e custo/limites pertinentes antes de declarar observabilidade ativa. Perfil e estado ficam no documento/processo dono segundo `romulo-documentacao`.
