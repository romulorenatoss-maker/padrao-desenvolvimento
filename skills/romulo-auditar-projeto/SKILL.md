---
name: romulo-auditar-projeto
description: Use ao levar o Romulo Dev Standard para um sistema existente, ou quando o usuario pedir diagnostico amplo de arquitetura/documentacao, para descobrir o que existe e quais lacunas reais precisam ser corrigidas sem impor uma arvore padrao.
---

# Romulo Auditar Projeto

A primeira passagem e somente leitura, salvo autorizacao explicita diferente.

Reconheca progressivamente: identidade/repositorio/branch; stack e entradas; estrutura funcional; frontend/backend; persistencia; autenticacao/autorizacao; integracoes; testes; documentacao; scripts; CI/CD e deploy pertinentes.

Nao use nomes de pasta como criterio de conformidade. Descubra onde cada responsabilidade realmente vive.

Para cada area pertinente classifique:
- CONFORME: responsabilidade existe e evidencias sustentam;
- PARCIAL: existe mas possui lacuna comprovada;
- AUSENTE: necessidade real comprovada sem implementacao/destino;
- NAO_SE_APLICA;
- NAO_DESCOBERTO: evidencia/acesso insuficiente.

Compare com os principios do Romulo Dev Standard e com as regras locais. Separe lacuna funcional, arquitetural, documental, seguranca, teste e operacao.

Priorize risco e dependencia. Proponha a menor adequacao que preserve o que esta correto. Nao crie pastas vazias, wrappers, CRUDs ou documentos apenas para fazer o projeto parecer com outro.

A auditoria nao autoriza automaticamente escrita, migracao, remocao, commit, push ou deploy.

Auditoria de produto/acoes consulta `romulo-especificar`; de consistencia visual e peculiaridades consulta `romulo-interface`. Padronizacao ampla pedida exige inventario de telas/componentes e proposta de referencia antes da migracao. Isso nao transforma toda tarefa local em auditoria global.
