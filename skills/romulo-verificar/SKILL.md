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

## Verificacao por efeito
- docs: vinculos resolvem e correspondem aos fatos;
- texto/estilo: trecho/tela funciona;
- backend: efeito/contrato alterado executa;
- acesso/escopo: caminho permitido e recusa pertinente;
- saldo/pagamento/estoque/repetivel: integridade e repeticao/concorrencia quando a garantia mudou;
- migration/remocao: ensaio, integridade e recuperacao;
- contrato compartilhado: consumidores atingidos validos;
- bug: caso que falhava passa;
- prototipo: fluxo local pertinente, sem fingir backend testado.

Nao executar bateria universal por rotina.

Pronto exige: alcance respeitado; codigo/docs reconciliados; nenhum artefato novo sem dono/consumidor; nenhum stub/fallback ficticio na cadeia real; fixtures de testes isoladas do runtime de producao; temporarios sem utilidade fora do versionamento; seguranca/integridade pertinentes; verificacao obrigatoria passou; nenhuma pendencia bloqueante escondida.

## Publicacao e concorrencia
Nao misturar, apagar ou reverter alteracao de outro executor. Candidato a commit contem somente o lote autorizado e sua documentacao. Nunca `--no-verify`, nunca desligar hook/protecao. Falha de publicacao nao autoriza reset destrutivo, amend/force ou perda de trabalho alheio. Migration real, concessao de permissao e operacao destrutiva mantem autorizacao propria.

## Aceite de produto, interface e conexoes
Consultar a proposta/revisao aprovada em `romulo-especificar`. Conferencia bidirecional: requisito sem entrega e elemento sem tarefa comprovada sao defeitos a corrigir. Efeito visual/interativo exige o roteiro renderizado de `romulo-interface`, inclusive peculiaridades e consumidores compartilhados.

Para cada acao atingida, provar o efeito aplicavel: local, navegacao, consulta ou mutacao. Em persistencia, confirmar reabertura/reload e telas consumidoras; em efeito critico, testar recusa, validacao, repeticao, concorrencia e recuperacao quando a garantia exigir. Nao forcar banco em acao puramente local.

Conferir a cadeia de usuario no navegador quando houver UI e as garantias de backend por teste pertinente. Screenshot nao comprova banco; build nao comprova botao; lista de imports nao comprova fluxo. Dados de teste controlados com integracao real no ambiente autorizado; nunca testar mutacao destrutiva em producao sem autorizacao especifica.

Registre no destino canonico ja existente: revisao/SHA testado, ambiente, cenario/rota, comando ou passos, resultado observado, evidencia e limites. Remover segredos/dados sensiveis dos artefatos. Mudanca posterior invalida evidencia dependente. Nao criar certificado paralelo.

Revisao estrutural desta distribuicao nao e teste comportamental do agente nem aceite de telas de projetos consumidores. Separar VALIDACAO_ESTRUTURAL, CENARIOS_DO_METODO, ACEITE_FUNCIONAL, ACEITE_VISUAL e ATIVACAO_NA_SESSAO; cada dimensao usa PASSOU/FALHOU/NAO_EXECUTADO/NAO_SE_APLICA com escopo claro.

Falha obrigatoria corrigivel retorna a `romulo-construir` e e retestada; NAO_EXECUTADO nao pode ser convertido em PASSOU. Proibido afrouxar teste, remover requisito, apagar baseline, desligar controle ou atualizar screenshot esperado sem aprovacao para obter aceite. Ausencia de recurso externo deve ser comprovada e declarada, nao mascarada.
