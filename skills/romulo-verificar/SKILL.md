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

## Perfil de qualidade e testes para entregar rapido

Reutilizar comandos, guardas e runners existentes; perfil concreto por projeto no documento/processo dono, conforme `romulo-documentacao`. Confirmar a execucao e versao/escopo antes de marcar CONFIGURADO/VERIFICADO; ferramenta citada ou check criado nao e PASSOU. Projetos sem perfil recebem apenas a configuracao necessaria ao lote/adocao autorizados, sem instalar a lista inteira nem mudar arquitetura/runtime/build.

- Sintaxe/lint, contratos arquiteturais e procura de codigo sem consumidor respeitam as linguagens e entradas reais. Biome e opcao para JS/CSS/JSON e formatos suportados, nao valida PHP; PHP precisa de verificacao propria. Knip analisa arquivos/exports/dependencias JS/TS e exige entradas/configuracao reais, inclusive carregamentos dinamicos por PHP; achado nao autoriza remover consumidor. `arch-contract` encontrado e TypeScript, nao substitui guardas dos contratos PHP. `commitlint` valida mensagem de commit, nao a funcao. Nomes ambíguos/produtos nao confirmados sao resolvidos antes de instalar.
- Testes unitarios cobrem regra local relevante; integracao cobre persistencia, contrato e consumidores atingidos; end-to-end cobre os fluxos reais de usuario afetados/criticos. Playwright e opcao para navegador, inclusive interface PHP/JS, sem impor framework de produto. Fixtures isoladas e relogio controlado podem reduzir tempo de teste; nao fingem evidencia de hardware ou producao.
- Codecov e opcao para acompanhar cobertura produzida pelos runners; cobertura nao comprova regra correta. StrykerJS e opcao de mutacao para JS/TS para avaliar eficacia dos testes, sobretudo logica critica; nao valida PHP nem deve rodar toda vez que um rotulo mudar. Metas de cobertura/mutacao so conforme risco e contrato do projeto, sem porcentagem universal nem testes que apenas repetem o codigo.

Antes de mostrar o prototipo, checar o pedido/cadeia afetados e renderizacao conforme `romulo-prototipo-real`; depois, fechar checks obrigatorios e validacao de entrega. Executar verificacoes independentes em paralelo quando permitido, com dados/arquivos/ambientes separados; sequenciar as que dependem de correcao/mutacao. Cache seguro e reuso de evidencia da mesma revisao/alcance economizam tempo; fonte/dependencia alterada invalida a evidencia correspondente.

CI de PR executa checks requeridos e suites proporcionais/cadeias criticas, sem relaxar seguranca ou instrumentacao local obrigatoria. Reexecucao ou ampliacao precisa de nova mudanca, falha ou risco concreto. Corrigir causa -> retestar o afetado -> validou, entregar. Nao impor auditoria global/mutacao completa para pedido pontual; nao esconder falha relevante para ganhar velocidade.

Conferir issue/PR e os [vinculos por DNA](../../references/DOCUMENTACAO.md#rastreabilidade-dna-issue-pr-e-commit), base e diff do lote, revisao/checks exigidos e autorizacao de integrar/publicar segundo `romulo-construir`. Protecao de branch/CI so e ativa com configuracao e ensaio no repositorio; regra em .md orienta agentes e nao comprova bloqueio mecanico. Guardas preexistentes continuam obrigatorias.

Em deploy de produto, conferir a revisao/artefato efetivamente testado, fontes/assets e versoes necessarias, configuracao do ambiente sem segredo, migrations aplicadas e compatibilidade dos consumidores. Publicar conteudo diferente do candidato testado exige nova verificacao atingida; nao inventar etapa de build para PHP/JS puro. Confirmar versao ativa e smoke test autorizado da cadeia; resultado falho exige parar a promocao e aplicar recuperacao prevista compativel com os dados. Voltar codigo nao desfaz escrita/migration automaticamente. Implantacao gradual e observabilidade seguem o perfil autorizado; nao instalar plataforma de deploy por esta regra.
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
- Reconstrucao: origem/revisao e dependencias conferidas; cadeia executada no destino autorizado, contratos/RPCs e controles exercitados quando aplicaveis, interface comparada com a referencia. Guia referencia fontes reais; simulacao, dependencia externa e recorte nao executado permanecem explicitos, sem promessa de zero bugs.

Conferencia bidirecional: requisito sem entrega e elemento sem tarefa comprovada sao defeitos. Em mutacao, confirmar reabertura/reload e consumidores; botao local nao exige banco. Screenshot nao comprova persistencia, build nao comprova clique e imports nao comprovam fluxo.

Ao mudar/remover elemento, conferir a finalidade aprovada e a continuidade da informacao nos consumidores conforme `romulo-especificar`. Documento dono e paginas afetadas devem concordar sobre IDs, regra referenciada e destino da capacidade; resumo curto nao substitui contrato tecnico. Conferir dependencias no codigo alem das ja registradas e declarar lacunas sem afirmar cobertura completa.

Conferir residuos do lote nos dois sentidos conforme `romulo-construir`: requisito/DNA, dono, fonte/assets, contratos/RPCs/dados, consumidores e testes efetivamente envolvidos. Unidade criada sem consumidor ou referencia ativa ao removido e falha a corrigir; item compartilhado/historico/dinamico sem desuso comprovado nao e apagado. Preservar guardas e mapas locais, mesmo que a consulta humana fique mais curta.

Em edicao pontual/acrescimo visual, conferir que posicao, dimensoes, cores, animacoes e comportamento do existente fora do pedido foram preservados. Efeito colateral em layout aprovado exige evidencia da aprovacao previa conforme `romulo-interface`; pedido do novo elemento sozinho nao e essa evidencia. A regra de skill nao constitui bloqueio mecanico de edicao.

Em nova capacidade/conexao, conferir que ideias anteriores pertinentes foram consultadas/apresentadas e que o incremento preserva detalhes/decisoes ainda validos. Vinculo previsto nao e consumidor implementado nem teste executado; sem documento/pagina existente, nenhuma referencia falsa ou estado construido. Fonte permite distinguir explicacao do responsavel de sugestao da IA.

Conferir que o documento dono permite entender a decisao atual sem chat e nao conserva como alternativas vigentes regras substituidas ou sugestoes descartadas. Conferir links dos consumidores afetados, sem transformar consolidacao de conversa em auditoria ampla. Essa limpeza nao apaga historico Git, dados/auditoria nem pendencia real de implementacao.

Conferir o alcance de `CONTEXTO_CONSOLIDADO: SIM`: nao marcar documento inteiro por consolidar so uma aba, nem usar a marca como prova de funcionamento/publicacao. Conferir que o conteudo vigente e suficiente sem chat, mantendo lacunas de implementacao explicitas.

Recorte efetivamente conciliado sem marcador SIM ou ainda listado como pendente de consolidacao e fechamento documental incompleto: corrigir antes da entrega/commit, sem pedir ao responsavel para mandar marcar. Nao substituir a verificacao por marcar um recorte inacabado.

Testes reais em ambiente autorizado com dados controlados. Fixtures isoladas sao legitimas; nao fallback ficticio de producao. Novos testes, screenshots e saidas usam destinos previstos no catalogo; nao criar certificado, memoria ou plano paralelo. Executar comandos pertinentes descobertos no projeto, nunca alegar execucao sem resultado.

Registrar no dono canonico: escopo/revisao/SHA testado, ambiente, cenario/rota, comando/passos, resultado/evidencia e limites. Remover segredos/dados sensiveis. Mudanca posterior invalida evidencia dependente. Amostra declarada nao comprova execucao de todos os consumidores.

## Retorno a construcao e publicacao
Falha corrigivel no alcance retorna a `romulo-construir`, corrige causa e retesta; nao encerrar apenas como pendencia. Recurso externo ausente exige impedimento concreto, sem prometer execucao futura. Nao afrouxar teste, esconder requisito, apagar baseline ou aceitar screenshot novo sem aprovacao para passar.

Preservar guardas, hooks, CI e fiscal independente quando exigidos pelo contrato local.

Fiscal independente confere, alem do codigo, o fechamento documental de tudo o que as skills exigem para o lote: decisao gravada no documento do modulo/tela dono; entrada no historico de entregas com QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER; limpeza dos registros de trabalho (pergunta respondida fora do registro, andamento/fila/pendencias/mapas/marcas de "falta publicar" sem o que foi entregue, "respondida, a construir" onde ainda nao foi construido); inventario/identidades e vinculos reconciliados; migrations aplicadas e conferidas quando o codigo depende delas. Ausencia de qualquer um e lacuna, nao observacao. Em lote que publica tela/aba/modal prototipado, o fiscal confere tambem a comparacao prototipo x real (`romulo-prototipo-real`, fechamento da conversao): diferencas no andamento, documento da tela so com o real e prototipo apagado quando nada sobrou. Ausencia e lacuna. Candidato contem somente o lote autorizado; sem `--no-verify`, reset destrutivo, amend/force, perda de trabalho alheio ou permissao concedida por conveniencia. Commit, push confirmado, deploy e versao ativa sao distintos.

## Validacao do proprio padrao
Executar os comandos do README central. Separar VALIDACAO_ESTRUTURAL, CENARIOS_DO_METODO, ACEITE_FUNCIONAL, ACEITE_VISUAL e ATIVACAO_NA_SESSAO com estados e escopo claros. Teste de parser/links e exemplos em prosa nao sao teste comportamental de modelo. Gate descrito em Markdown nao e fiscal universal de escrita; hook/permissao/sandbox requer implementacao e ensaio no ambiente antes de afirmar bloqueio mecanico.
