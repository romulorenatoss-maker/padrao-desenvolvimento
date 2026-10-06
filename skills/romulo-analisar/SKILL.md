---
name: romulo-analisar
description: Use antes de qualquer tarefa tecnica, alteracao, correcao, implementacao ou revisao para reconhecer o projeto, localizar a responsabilidade real, delimitar impacto e impedir criacao ou mudanca por suposicao.
---

# Romulo Analisar

Antes de escrever:
1. confirme repositorio, branch, ambiente e alcance autorizado;
2. leia o AGENTS.md local e regras locais mais especificas;
3. localize a menor fonte canonica suficiente: sumario/mapa/contrato pertinente e depois codigo atingido;
4. identifique dono funcional, implementacao existente, consumidores pertinentes, dados, autorizacao e verificacao aplicavel;
5. declare mentalmente o que muda, o que deve ser preservado e como provar o resultado;
6. busque por rota, simbolo, ID e nome funcional antes de concluir que algo nao existe.

Classifique fatos como COMPROVADO, PARCIAL, NAO_DESCOBERTO ou NAO_SE_APLICA. Busca vazia nao prova inexistencia.

Nao crie plano em arquivo. Nao abra auditoria global para uma tarefa local. Nao transforme convencao deste padrao em estrutura obrigatoria quando o projeto possui equivalente correto.

Quando Ponytail estiver instalado/disponivel, use-o em modo full para procurar complexidade desnecessaria, sem reduzir requisito, seguranca, documentacao ou teste.
