---
name: romulo-verificar
description: "Use antes de encerrar tarefa tecnica para verificar escopo, arquivos previstos/autorizados, comportamento, visual, documentacao, seguranca, consumidores e evidencias executadas."
---

# Romulo Verificar

Verificar proporcionalmente ao efeito, nao a quantidade de arquivos. Confrontar alcance autorizado, pedido/decisao aprovada, diff, consumidores, contratos, seguranca e documentacao. Estados de verificacao: PASSOU, FALHOU, NAO_EXECUTADO ou NAO_SE_APLICA. Ausencia de evidencia nao e PASSOU; nao declarar ausencia universal de defeitos.

## Testar, corrigir e entregar sem repeticao desnecessaria

Nao definir quantidade fixa de testes ou tentativas como meta. Escolher cenarios proporcionais ao pedido e aos consumidores realmente afetados; distinguir numero de cenarios, assercoes e execucoes ao informar resultados.

Executar o recorte. Se falhar, corrigir a causa e retestar o cenario que falhou e as dependencias atingidas pela correcao. Continuar enquanto houver falha corrigivel no alcance. Bloqueio externo concreto deve ser informado; repetir sem nova evidencia nao resolve.

Quando o comportamento solicitado e os pontos afetados estiverem validados, parar de ampliar ou repetir a bateria e entregar imediatamente o resultado. Nova rodada ou cobertura maior exige motivo concreto: nova alteracao, falha, dependencia afetada ou preocupacao ainda nao resolvida. Preservar verificacoes obrigatorias do projeto; nao trocar criterio de aceite por rapidez.

No prototipo iterativo, mostrar o recorte apos a checagem minima pertinente conforme `romulo-prototipo-real`, deixando claro o que ainda nao foi verificado. Com divisao expressamente autorizada, o documentador/revisor testa a funcao e pode corrigir desvios estritamente dentro do pedido; antes de editar codigo, combinar propriedade dos arquivos com o construtor. So marcar verificado depois da evidencia, sem confundir entrega visual com integracao real.

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

Ao mudar/remover elemento, conferir a finalidade aprovada e a continuidade da informacao nos consumidores conforme `romulo-especificar`. Documento dono e paginas afetadas devem concordar sobre IDs, regra referenciada e destino da capacidade; resumo curto nao substitui contrato tecnico. Conferir dependencias no codigo alem das ja registradas e declarar lacunas sem afirmar cobertura completa.

Em nova capacidade/conexao, conferir que ideias anteriores pertinentes foram consultadas/apresentadas e que o incremento preserva detalhes/decisoes ainda validos. Vinculo previsto nao e consumidor implementado nem teste executado; sem documento/pagina existente, nenhuma referencia falsa ou estado construido. Fonte permite distinguir explicacao do responsavel de sugestao da IA.

Testes reais em ambiente autorizado com dados controlados. Fixtures isoladas sao legitimas; nao fallback ficticio de producao. Novos testes, screenshots e saidas usam destinos previstos no catalogo; nao criar certificado, memoria ou plano paralelo. Executar comandos pertinentes descobertos no projeto, nunca alegar execucao sem resultado.

Registrar no dono canonico: escopo/revisao/SHA testado, ambiente, cenario/rota, comando/passos, resultado/evidencia e limites. Remover segredos/dados sensiveis. Mudanca posterior invalida evidencia dependente. Amostra declarada nao comprova execucao de todos os consumidores.

## Retorno a construcao e publicacao
Falha corrigivel no alcance retorna a `romulo-construir`, corrige causa e retesta; nao encerrar apenas como pendencia. Recurso externo ausente exige impedimento concreto, sem prometer execucao futura. Nao afrouxar teste, esconder requisito, apagar baseline ou aceitar screenshot novo sem aprovacao para passar.

Preservar guardas, hooks, CI e fiscal independente quando exigidos pelo contrato local.

Fiscal independente confere, alem do codigo, o fechamento documental de tudo o que as skills exigem para o lote: decisao gravada no documento do modulo/tela dono; entrada no historico de entregas com QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER; limpeza dos registros de trabalho (pergunta respondida fora do registro, andamento/fila/pendencias/mapas/marcas de "falta publicar" sem o que foi entregue, "respondida, a construir" onde ainda nao foi construido); inventario/identidades e vinculos reconciliados; migrations aplicadas e conferidas quando o codigo depende delas. Ausencia de qualquer um e lacuna, nao observacao. Em lote que publica tela/aba/modal prototipado, o fiscal confere tambem a comparacao prototipo x real (`romulo-prototipo-real`, fechamento da conversao): diferencas no andamento, documento da tela so com o real e prototipo apagado quando nada sobrou. Ausencia e lacuna. Candidato contem somente o lote autorizado; sem `--no-verify`, reset destrutivo, amend/force, perda de trabalho alheio ou permissao concedida por conveniencia. Commit, push confirmado, deploy e versao ativa sao distintos.

## Validacao do proprio padrao
Executar os comandos do README central. Separar VALIDACAO_ESTRUTURAL, CENARIOS_DO_METODO, ACEITE_FUNCIONAL, ACEITE_VISUAL e ATIVACAO_NA_SESSAO com estados e escopo claros. Teste de parser/links e exemplos em prosa nao sao teste comportamental de modelo. Gate descrito em Markdown nao e fiscal universal de escrita; hook/permissao/sandbox requer implementacao e ensaio no ambiente antes de afirmar bloqueio mecanico.
