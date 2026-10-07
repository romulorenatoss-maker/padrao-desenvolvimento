---
name: romulo-documentacao
description: Use quando uma alteracao muda comportamento, contrato, estrutura, responsabilidade, dado, acesso, dependencia ou conhecimento canonico e precisa reconciliar documentacao sem criar lixo documental.
---

# Romulo Documentacao

Documentacao explica responsabilidade, comportamento e vinculos; nao reescreve codigo em prosa.

Primeiro descubra os destinos canonicos ja adotados pelo projeto. Atualize o dono existente. Documento novo so nasce quando existe responsabilidade real sem destino adequado.

Nao crie documento por agente, execucao, arquivo, funcao, botao, campo ou linha. Evite PLANO, FINAL, V2, backup documental e relatorios paralelos quando a informacao cabe no registro canonico.

Registre fatos comprovados e decisoes aprovadas. Nao marque como real o que e previsto, simulado, local ou nao executado.

No fechamento deve ser possivel seguir, conforme aplicavel: artefato -> responsabilidade/identidade -> mapa ou documento dono -> consumidores pertinentes, e o inverso necessario para manutencao.

Mudanca interna sem efeito no conhecimento canonico nao exige reescrita artificial; registre/verifique somente quando o instrumento local exigir evidencia de fechamento.

Nao criar arquivo de memoria, resumo paralelo, documentacao de governanca ou pasta `agents/`. O Git preserva historico; a documentacao canonica preserva o estado necessario.

Se o modulo ainda nao tem destino documental durante construcao autorizada, criar somente os documentos necessarios a capacidade que nasce; nunca arvore documental vazia.

## Proposta, visual e rastreabilidade
Decisoes de `romulo-especificar`, referencia e peculiaridades de `romulo-interface` ficam nos mapas/assuntos canonicos do projeto, com revisao e fonte de aprovacao. Referenciar, nao copiar regras centrais para cada tela. Identificacao de peculiaridade na UI e eventual projecao usam a mesma fonte, sem listas manuais paralelas.

Manter o vinculo pedido/decisao -> tela/aba/acao -> contrato/regra/dado -> consumidores -> evidencia. Registre somente fatos verificados e preserve diferenca entre proposto, construido, testado e publicado. Documentar um defeito nao o transforma em regra aprovada nem substitui corrigi-lo.
