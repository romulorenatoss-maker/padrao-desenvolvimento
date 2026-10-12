# Seguranca

Modelo base: negar por padrao e confiar somente em controles executados no servidor/infraestrutura apropriada.

Revalidar no backend autorizacao, escopo, propriedade e valores que produzem efeitos oficiais. Parametrizar SQL. Proteger segredos. Restringir uploads e integracoes. Usar transacoes/constraints para invariantes que precisam sobreviver a concorrencia.

A analise e proporcional ao risco. Nao inserir mecanismos sem ameaca ou requisito correspondente, mas nunca remover controle legitimo em nome de simplicidade.

## Auditoria dirigida — oito riscos

Aplicar ao recorte autorizado, seguindo DNA -> dono -> entrada/consumidores -> controle -> evidencia. Os oito temas orientam a triagem; executar somente os cenarios pertinentes, preservando guardas obrigatorias. Reutilizar controles e runners existentes; esta referencia nao instala scanner, dependencia, servico, CI ou permissao.

| Risco | Conferir na fonte e no runtime autorizado |
|---|---|
| XSS | Seguir entrada ate HTML/atributo/URL/JavaScript/DOM; encoding depende do contexto. Preferir textContent para texto; HTML permitido exige sanitizacao adequada. CSP e defesa adicional, nao substitui encoding/sanitizacao. Fixture local demonstra que texto nao vira execucao, sem alterar a UI aprovada. |
| API exposta | Endpoint publicamente acessivel nao e vulnerabilidade por si. Conferir finalidade, autenticacao e autorizacao por metodo/objeto/tenant; permitir anonimo somente pelo contrato. CORS ou botao oculto nao autorizam acesso. Validar entrada, CSRF conforme sessao, limites de corpo, erros e exposicao administrativa; comparar recusa sem identidade, sem permissao e de outro tenant quando pertinente. |
| Segredos | Conferir referencias, configuracao publica, bundles/respostas/logs e caminhos servidos sem abrir valores secretos. Nunca abrir .env, backup privado ou arquivo de chaves para esta auditoria; usar metadados/configuracao sanitizada e fixtures. Resultado nao imprime valor nem trecho sensivel; suspeita registra local/tipo apenas. Vazamento comprovado exige resposta e rotacao pelo dono autorizado, nao uso da credencial encontrada. |
| Banco/RLS/grants | Localizar schema/migration/policy/RPC e assinatura completa, grants EXECUTE, roles e chamadores. Verificar isolamento sob a identidade real da aplicacao, nao apenas admin; superuser/BYPASSRLS/owner e SECURITY DEFINER podem mudar a protecao efetiva. Backend revalida tenant/permissao; funcao privilegiada exige contexto seguro, search_path e privilegio minimo. Definicao no Git nao comprova policy aplicada; nao desligar RLS ou abrir grants. |
| SQL injection | Parametrizar valores no repository/RPC; nomes de coluna, ordenacao e outros identificadores dinamicos exigem allowlist. Escaping isolado nao substitui parametrizacao. Conferir interpolacao e SQL dinamico dentro das funcoes; testar recusa/parametro como dado com fixture local, sem SQL destrutivo nem consulta de dados oficiais. |
| Rate limit | Avaliar endpoints de login/recuperacao, custo alto, escrita e integracao. Conferir politica server-side/gateway, janela, identidade/chave confiavel e abrangencia entre processos; respeitar proxies conhecidos, nao confiar cegamente em cabecalho/IP do cliente. Ensaio local com relogio/cotas pequenas comprova permitido e recusado (429 quando HTTP), sem brute force/carga em producao; nao impor numero universal. |
| Prompt injection | Aplicavel a fluxos com modelo/agente/tools: documentos, web, mensagens e resultados externos sao dados nao confiaveis, nao ampliam instrucao/autorizacao. Separar contexto confiavel, validar chamadas/parametros e saidas; allowlist, menor privilegio e confirmacao humana nos efeitos exigidos pelo contrato. Filtro textual/prompt nao garante isolamento. Fixture inerte testa que instrucao embutida nao executa efeito nem exfiltra dado; nao conectar ferramenta real para reproduzir. |
| Pacote inventado/supply chain | Antes de sugerir/instalar, conferir nome exato, fornecedor/repositorio oficial, versao existente, finalidade, lockfile e integridade/proveniencia disponivel; pacote existente ainda pode ser malicioso. Revisar scripts de instalacao e efeitos. Nao executar pacote sugerido por IA para descobrir se e verdadeiro; registry indisponivel deixa NAO_VERIFICADO. Dependencia nova continua exigindo alcance/autorizacao e plano de arquivos, nunca instalacao por rotina. |

## Evidencia, limites e aplicacao

Por achado, registrar no dono/issue existentes: risco, DNA/arquivo/trecho/entrada, impacto, controle esperado, evidencia sanitizada e revisao/ambiente. Classificar COMPROVADO (evidencia suficiente para o fato delimitado), SUSPEITA (indicio a validar), NAO_VERIFICADO (sem acesso/ensaio suficiente) ou NAO_SE_APLICA (motivo). Uma interpolacao insegura pode ser COMPROVADA na fonte sem declarar exploracao real; ausencia em busca textual nao prova seguranca.

Separar FONTE (codigo/configuracao prevista), RUNTIME (controle executado sob identidade/ambiente conhecidos) e APLICACAO (versao/configuracao efetivamente ativa). Cada camada tem evidencia e limite proprios; nao promover migracao definida a aplicada nem simulacao a backend seguro. Correcao precisa do reteste atingido conforme verificar; descoberta nao autoriza corrigir fora do pedido, dar permissao ou publicar.

Auditoria inicia somente em leitura; ensaios exigem alvo autorizado, ambiente local/fixtures e efeitos controlados. Nao abrir segredos/.env/backup, atacar producao, fazer brute force, usar token encontrado, instalar ferramenta ou executar SQL mutante por este pedido. Testes que exigem escrita usam somente fixture isolada explicitamente autorizada; falta de ambiente fica NAO_VERIFICADO. Nao registrar payload sensivel nem alegar ausencia universal de vulnerabilidades.

## Fontes primarias

OWASP Cheat Sheet Series consultada em 12/10/2026; recomenda controles por contexto, nao certifica um projeto. Revalidar a fonte pertinente antes de adotar recomendacao que possa mudar:
- [XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
- [REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
- [Database Security](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html), [Multi Tenant Security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html).
- [LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html), [Software Supply Chain Security](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html).
