---
name: romulo-verificar
description: Use obrigatoriamente antes de declarar concluida qualquer tarefa tecnica para confrontar o que foi pedido, o que mudou, documentacao, seguranca, consumidores e evidencias executadas.
---

# Romulo Verificar

Verifique proporcionalmente ao efeito real, nao por quantidade de arquivos.

Confronte:
- alcance autorizado versus diff/artefatos alterados;
- comportamento entregue versus pedido e decisao aprovada;
- novos artefatos versus dono, consumidor e necessidade;
- documentacao canonica versus versao entregue;
- contratos compartilhados versus consumidores atingidos;
- seguranca/integridade pertinentes;
- testes realmente executados e seus resultados;
- estado local, commit, push e deploy sem confundi-los.

Use somente PASSOU, FALHOU, NAO_EXECUTADO ou NAO_SE_APLICA para verificacoes. Ausencia de teste nunca vira PASSOU.

Se algo obrigatorio falhar, corrija a causa e repita a verificacao afetada. Nao esconda pendencia para produzir conclusao positiva.

Nao declare ausencia universal de defeitos. Informe limites da verificacao.

Quando o projeto possuir guardas, hooks, CI, fiscais documentais ou revisao independente, execute-os conforme o contrato local; esta skill nao os substitui.
