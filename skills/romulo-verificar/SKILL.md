---
name: romulo-verificar
description: "Use antes de encerrar tarefa tecnica para verificar escopo, arquivos previstos/autorizados, comportamento, visual, documentacao, seguranca, consumidores e evidencias executadas."
---

# Romulo Verificar

Verificar proporcionalmente ao efeito, nao a quantidade de arquivos. Confrontar alcance autorizado, pedido/decisao aprovada, diff, consumidores, contratos, seguranca e documentacao. Estados de verificacao: PASSOU, FALHOU, NAO_EXECUTADO ou NAO_SE_APLICA. Ausencia de evidencia nao e PASSOU; nao declarar ausencia universal de defeitos.

## Arquivos, nomes e autorizacoes
Reconciliar cada arquivo criado/alterado/removido/renomeado no candidato e os novos arquivos nao rastreados pertinentes ao trabalho. Confrontar previsao da skill/reference e necessidade com o gate de `romulo-analisar`; sem previsao, exigir evidencia do 0393 especifico antes de criar, nao autorizacao retroativa presumida. Diretorio vazio ou artefato sem finalidade/consumidor falha.

Confirmar sumario central consultado, fontes coerentes na mesma revisao e destinations canonicos. Bootstrap/migracao: AGENTS local minimo sem catalogo duplicado, ponte CLAUDE pertinente, nenhuma peculiaridade/guarda perdida, links de destino validos e autorizacao para alterar protegido. Nao afirmar que mudar o arquivo carregou o plugin/sessao.

## Aceite por efeito
- Docs: links/IDs/donos correspondem a fatos e consumidores.
- Bug: cenario que falhava passa; dependencia compartilhada permanece valida.
- Backend/acesso: efeito/contrato real e caminho permitido/recusa pertinentes.
- Pagamento/saldo/estoque/repeticao: integridade, concorrencia, idempotencia e recuperacao quando a garantia mudou.
- Migration/remocao: ensaio, integridade, preservacao/recuperacao e autorizacao.
- Interface: proposta de `romulo-especificar` e revisao renderizada de `romulo-interface`, incluindo peculiaridades; comportamento da acao e fonte oficial conforme aplicabilidade.
- Prototipo: fluxo local pertinente, sem fingir persistencia/seguranca real.

Conferencia bidirecional: requisito sem entrega e elemento sem tarefa comprovada sao defeitos. Em mutacao, confirmar reabertura/reload e consumidores; botao local nao exige banco. Screenshot nao comprova persistencia, build nao comprova clique e imports nao comprovam fluxo.

Testes reais em ambiente autorizado com dados controlados. Fixtures isoladas sao legitimas; nao fallback ficticio de producao. Novos testes, screenshots e saidas usam destinos previstos no catalogo; nao criar certificado, memoria ou plano paralelo. Executar comandos pertinentes descobertos no projeto, nunca alegar execucao sem resultado.

Registrar no dono canonico: escopo/revisao/SHA testado, ambiente, cenario/rota, comando/passos, resultado/evidencia e limites. Remover segredos/dados sensiveis. Mudanca posterior invalida evidencia dependente. Amostra declarada nao comprova execucao de todos os consumidores.

## Retorno a construcao e publicacao
Falha corrigivel no alcance retorna a `romulo-construir`, corrige causa e retesta; nao encerrar apenas como pendencia. Recurso externo ausente exige impedimento concreto, sem prometer execucao futura. Nao afrouxar teste, esconder requisito, apagar baseline ou aceitar screenshot novo sem aprovacao para passar.

Preservar guardas, hooks, CI e fiscal independente quando exigidos pelo contrato local. Candidato contem somente o lote autorizado; sem `--no-verify`, reset destrutivo, amend/force, perda de trabalho alheio ou permissao concedida por conveniencia. Commit, push confirmado, deploy e versao ativa sao distintos.

## Validacao do proprio padrao
Executar os comandos do README central. Separar VALIDACAO_ESTRUTURAL, CENARIOS_DO_METODO, ACEITE_FUNCIONAL, ACEITE_VISUAL e ATIVACAO_NA_SESSAO com estados e escopo claros. Teste de parser/links e exemplos em prosa nao sao teste comportamental de modelo. Gate descrito em Markdown nao e fiscal universal de escrita; hook/permissao/sandbox requer implementacao e ensaio no ambiente antes de afirmar bloqueio mecanico.
