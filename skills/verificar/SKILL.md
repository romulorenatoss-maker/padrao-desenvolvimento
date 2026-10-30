---
name: verificar
description: "Use antes de encerrar tarefa tecnica para verificar escopo, arquivos previstos/autorizados, comportamento, visual, documentacao, seguranca, consumidores e evidencias executadas."
---

# Verificar

Recuperacao/virada de instancia usa os criterios de [backup-recuperacao](../backup-recuperacao/SKILL.md#5-verificacao-relatorio-e-liberacao): corte/revisao, compatibilidade, dados/arquivos e controles antes da liberacao. Captura/dry-run ou validacao textual da skill nao certifica restauracao/ausencia de malware.

Conferir a evidencia ou pendencia da [verificacao curta de backup na entrada](../backup-recuperacao/SKILL.md#verificacao-curta-na-entrada), sem repetir consulta ainda atual. Lacuna nao pode desaparecer da entrega nem ser promovida a backup ativo; operacao dependente de preservacao continua bloqueada conforme seu contrato.

Verificar proporcionalmente ao efeito, nao a quantidade de arquivos. Confrontar alcance autorizado, pedido/decisao aprovada, diff, consumidores, contratos, seguranca e documentacao. Estados de verificacao: PASSOU, FALHOU, NAO_EXECUTADO ou NAO_SE_APLICA. Ausencia de evidencia nao e PASSOU; nao declarar ausencia universal de defeitos.

## Testar, corrigir e entregar sem repeticao desnecessaria

Nao definir quantidade fixa de testes ou tentativas como meta. Escolher cenarios proporcionais ao pedido e aos consumidores realmente afetados; distinguir numero de cenarios, assercoes e execucoes ao informar resultados.

Executar o recorte. Se falhar, corrigir a causa e retestar o cenario que falhou e as dependencias atingidas pela correcao. Continuar enquanto houver falha corrigivel no alcance. Bloqueio externo concreto deve ser informado; repetir sem nova evidencia nao resolve.

Quando o comportamento solicitado e os pontos afetados estiverem validados, parar de ampliar ou repetir a bateria e entregar imediatamente o resultado. Nova rodada ou cobertura maior exige motivo concreto: nova alteracao, falha, dependencia afetada ou preocupacao ainda nao resolvida. Preservar verificacoes obrigatorias do projeto; nao trocar criterio de aceite por rapidez.

No prototipo iterativo, mostrar o recorte apos a checagem minima pertinente conforme `prototipo-real`, deixando claro o que ainda nao foi verificado. Com divisao expressamente autorizada, o documentador/revisor testa a funcao e pode corrigir desvios estritamente dentro do pedido; antes de editar codigo, combinar propriedade dos arquivos com o construtor. So marcar verificado depois da evidencia, sem confundir entrega visual com integracao real.

## Perfil de qualidade e testes para entregar rapido

Reutilizar comandos, guardas e runners existentes; perfil concreto por projeto no documento/processo dono, conforme `documentacao`. Confirmar a execucao e versao/escopo antes de marcar CONFIGURADO/VERIFICADO; ferramenta citada ou check criado nao e PASSOU. Projetos sem perfil recebem apenas a configuracao necessaria ao lote/adocao autorizados, sem instalar a lista inteira nem mudar arquitetura/runtime/build.

- Sintaxe/lint, contratos arquiteturais e procura de codigo sem consumidor respeitam as linguagens e entradas reais. Biome e opcao para JS/CSS/JSON e formatos suportados, nao valida PHP; PHP precisa de verificacao propria. Knip analisa arquivos/exports/dependencias JS/TS e exige entradas/configuracao reais, inclusive carregamentos dinamicos por PHP; achado nao autoriza remover consumidor. `arch-contract` encontrado e TypeScript, nao substitui guardas dos contratos PHP. `commitlint` valida mensagem de commit, nao a funcao. Nomes ambíguos/produtos nao confirmados sao resolvidos antes de instalar.
- Testes unitarios cobrem regra local relevante; integracao cobre persistencia, contrato e consumidores atingidos; end-to-end cobre os fluxos reais de usuario afetados/criticos. Playwright e opcao para navegador, inclusive interface PHP/JS, sem impor framework de produto. Fixtures isoladas e relogio controlado podem reduzir tempo de teste; nao fingem evidencia de hardware ou producao.
- Codecov e opcao para acompanhar cobertura produzida pelos runners; cobertura nao comprova regra correta. StrykerJS e opcao de mutacao para JS/TS para avaliar eficacia dos testes, sobretudo logica critica; nao valida PHP nem deve rodar toda vez que um rotulo mudar. Metas de cobertura/mutacao so conforme risco e contrato do projeto, sem porcentagem universal nem testes que apenas repetem o codigo.

Antes de mostrar o prototipo, checar o pedido/cadeia afetados e renderizacao conforme `prototipo-real`; depois, fechar checks obrigatorios e validacao de entrega. Executar verificacoes independentes em paralelo quando permitido, com dados/arquivos/ambientes separados; sequenciar as que dependem de correcao/mutacao. Cache seguro e reuso de evidencia da mesma revisao/alcance economizam tempo; fonte/dependencia alterada invalida a evidencia correspondente.

CI de PR executa checks requeridos e suites proporcionais/cadeias criticas, sem relaxar seguranca ou instrumentacao local obrigatoria. Reexecucao ou ampliacao precisa de nova mudanca, falha ou risco concreto. Corrigir causa -> retestar o afetado -> validou, entregar. Nao impor auditoria global/mutacao completa para pedido pontual; nao esconder falha relevante para ganhar velocidade.

Conferir issue/PR e os [vinculos por DNA](../../references/DOCUMENTACAO.md#rastreabilidade-dna-issue-pr-e-commit), base e diff do lote, revisao/checks exigidos e autorizacao de integrar/publicar segundo `construir`. Protecao de branch/CI so e ativa com configuracao e ensaio no repositorio; regra em .md orienta agentes e nao comprova bloqueio mecanico. Guardas preexistentes continuam obrigatorias.

Em deploy de produto, conferir a revisao/artefato efetivamente testado, fontes/assets e versoes necessarias, configuracao do ambiente sem segredo, migrations aplicadas e compatibilidade dos consumidores. Publicar conteudo diferente do candidato testado exige nova verificacao atingida; nao inventar etapa de build para PHP/JS puro. Confirmar versao ativa e smoke test autorizado da cadeia; resultado falho exige parar a promocao e aplicar recuperacao prevista compativel com os dados. Voltar codigo nao desfaz escrita/migration automaticamente. Implantacao gradual e observabilidade seguem o perfil autorizado; nao instalar plataforma de deploy por esta regra.
Construir no real exige testes, lint e build que existam na stack/perfil do projeto; falha corrigivel volta a causa e reteste pertinente ate passar. Nao instalar build/framework ou executar checks sem relacao para preencher uma lista. Recurso/decisao/autorizacao indispensavel ausente bloqueia a parte dependente, sem declarar PASSOU. Reset do executor somente depois do encerramento conferido de `construir`.

## Arquivos, nomes e autorizacoes

JavaScript criado ou separado: conferir [tamanho e responsabilidade](../../references/ARQUITETURA.md#javascript-por-responsabilidade-e-tamanho), fonte legivel, excecao acima de 500 justificada/revisada, consumidor e ordem de carregamento reais. Conferir [identidade interna](../../references/DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo): cabecalho util, DNA junto do trecho e preservado ao mover, mapas/donos sem referencia exclusiva orfa. Contagem e marcadores nao certificam funcao, nem autorizam apagar legado ou mudar layout.

Reconciliar cada arquivo criado/alterado/removido/renomeado no candidato e os novos arquivos nao rastreados pertinentes ao trabalho. Confrontar previsao da skill/reference e necessidade com o gate de `analisar`; sem previsao, exigir evidencia do 0393 especifico antes de criar, nao autorizacao retroativa presumida. Diretorio vazio ou artefato sem finalidade/consumidor falha.

Confirmar sumario central consultado, fontes coerentes na mesma revisao e destinations canonicos. Bootstrap/migracao: AGENTS local minimo sem catalogo duplicado, ponte CLAUDE pertinente, nenhuma peculiaridade/guarda perdida, links de destino validos e autorizacao para alterar protegido. Nao afirmar que mudar o arquivo carregou o plugin/sessao.

## Aceite por efeito
- Docs: DNAs explicam para que, por que e para quem; links/donos e consumidores compartilhados correspondem aos fatos, sem duplicar a regra.
- Bug: cenario que falhava passa; dependencia compartilhada permanece valida.
- Backend/acesso: efeito/contrato real e caminho permitido/recusa pertinentes.
- Pagamento/saldo/estoque/repeticao: integridade, concorrencia, idempotencia e recuperacao quando a garantia mudou.
- Migration/remocao: ensaio, integridade, preservacao/recuperacao e autorizacao.
- Interface: proposta de `especificar` e revisao renderizada de `interface`, incluindo peculiaridades; comportamento da acao e fonte oficial conforme aplicabilidade.
- Prototipo: fluxo local pertinente e [ensaio de preservacao da fonte ativa e exemplos confirmados](../prototipo-real/SKILL.md#fonte-unica-ativa-da-tela-local), incluindo reload, reinicio do servico, reabertura e correspondencia da fonte com a resposta servida; sem fingir persistencia/seguranca real.
- Reconstrucao: origem/revisao e dependencias conferidas; cadeia executada no destino autorizado, contratos/RPCs e controles exercitados quando aplicaveis, interface comparada com a referencia. Guia referencia fontes reais; simulacao, dependencia externa e recorte nao executado permanecem explicitos, sem promessa de zero bugs.

Conferencia bidirecional: requisito sem entrega e elemento sem tarefa comprovada sao defeitos. Em mutacao, confirmar reabertura/reload e consumidores; botao local nao exige banco. Screenshot nao comprova persistencia, build nao comprova clique e imports nao comprovam fluxo.

Ao mudar/remover elemento, conferir finalidade aprovada e continuidade da informacao conforme `especificar`. Contrato compartilhado exige conferir consumidores e os efeitos em cada um; documento dono e paginas afetadas devem concordar sobre DNAs, regra e destino da capacidade. Resumo curto nao substitui contrato tecnico. Conferir dependencias no codigo alem das registradas e declarar lacunas sem afirmar cobertura completa.

Conferir residuos do lote nos dois sentidos conforme `construir`: requisito/DNA, dono, fonte/assets, contratos/RPCs/dados, consumidores e testes efetivamente envolvidos. Unidade criada sem consumidor ou referencia ativa ao removido e falha a corrigir; item compartilhado/historico/dinamico sem desuso comprovado nao e apagado. Preservar guardas e mapas locais, mesmo que a consulta humana fique mais curta.

Em edicao pontual/acrescimo visual, conferir que posicao, dimensoes, cores, animacoes e comportamento do existente fora do pedido foram preservados. Efeito colateral em layout aprovado exige evidencia da aprovacao previa conforme `interface`; pedido do novo elemento sozinho nao e essa evidencia. A regra de skill nao constitui bloqueio mecanico de edicao.

Em nova capacidade/conexao, conferir que ideias anteriores pertinentes foram consultadas/apresentadas e que o incremento preserva detalhes/decisoes ainda validos. Vinculo previsto nao e consumidor implementado nem teste executado; sem documento/pagina existente, nenhuma referencia falsa ou estado construido. Fonte permite distinguir explicacao do responsavel de sugestao da IA.

Conferir que o documento dono permite entender a decisao atual sem chat e nao conserva como alternativas vigentes regras substituidas ou sugestoes descartadas. Conferir links dos consumidores afetados, sem transformar consolidacao de conversa em auditoria ampla. Essa limpeza nao apaga historico Git, dados/auditoria nem pendencia real de implementacao.

Conferir o alcance de `CONTEXTO_CONSOLIDADO: SIM`: nao marcar documento inteiro por consolidar so uma aba, nem usar a marca como prova de funcionamento/publicacao. Conferir que o conteudo vigente e suficiente sem chat, mantendo lacunas de implementacao explicitas.

Recorte efetivamente conciliado sem marcador SIM ou ainda listado como pendente de consolidacao e fechamento documental incompleto: corrigir antes da entrega/commit, sem pedir ao responsavel para mandar marcar. Nao substituir a verificacao por marcar um recorte inacabado.

Testes reais em ambiente autorizado com dados controlados. Fixtures isoladas sao legitimas; nao fallback ficticio de producao. Novos testes, screenshots e saidas usam destinos previstos no catalogo; nao criar certificado, memoria ou plano paralelo. Executar comandos pertinentes descobertos no projeto, nunca alegar execucao sem resultado.

Registrar no dono canonico: escopo/revisao/SHA testado, ambiente, cenario/rota, comando/passos, resultado/evidencia e limites. Remover segredos/dados sensiveis. Mudanca posterior invalida evidencia dependente. Amostra declarada nao comprova execucao de todos os consumidores.

## Retorno a construcao e publicacao
Falha corrigivel no alcance retorna a `construir`, corrige causa e retesta; nao encerrar apenas como pendencia. Recurso externo ausente exige impedimento concreto, sem prometer execucao futura. Nao afrouxar teste, esconder requisito, apagar baseline ou aceitar screenshot novo sem aprovacao para passar.

Preservar guardas, hooks, CI e fiscal independente quando exigidos pelo contrato local.

Conferir o [registro temporario e seu fechamento](../../references/DOCUMENTACAO.md#manutencao-e-limpeza-do-conhecimento-vigente) pelo diff real: caminhos/simbolos, DNAs, donos atualizados e consumidores atingidos, inclusive itens omitidos pelo executor. Encaminhar divergencias conforme a referencia e reconferir antes de fechar. Lote encerrado nao deixa temporario de mudancas; lote interrompido preserva o aberto. Evidencia canonica/Git e manifestos/recibos exigidos seguem o ciclo local, sem apagamento para contornar guarda. Conferencia do lote nao certifica todo o repositorio.

Fiscal independente confere, alem do codigo, o fechamento documental de tudo o que as skills exigem para o lote: decisao gravada no documento do modulo/tela dono; entrada no historico de entregas com QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER; limpeza dos registros de trabalho (pergunta respondida fora do registro, andamento/fila/pendencias/mapas/marcas de "falta publicar" sem o que foi entregue, "respondida, a construir" onde ainda nao foi construido); inventario/identidades e vinculos reconciliados; migrations aplicadas e conferidas quando o codigo depende delas. Ausencia de qualquer um e lacuna, nao observacao. Em lote que publica tela/aba/modal prototipado, o fiscal confere tambem a comparacao prototipo x real (`prototipo-real`, fechamento da conversao): diferencas no andamento, documento da tela so com o real e prototipo apagado quando nada sobrou. Ausencia e lacuna. Candidato contem somente o lote autorizado; sem `--no-verify`, reset destrutivo, amend/force, perda de trabalho alheio ou permissao concedida por conveniencia. Commit, push confirmado, deploy e versao ativa sao distintos.

## Cenarios de execucao imediata do metodo

Conferir os encaminhamentos de `especificar`, `interface` e `prototipo-real`, inclusive contradicoes que reintroduzam pergunta de inicio. Ensaios comportamentais no cliente usam ambiente autorizado e a fila existente, sem alterar produto por uma tarefa limitada ao padrao. Registrar comando/passos, revisao, resposta observada e limites; revisao textual nao executa um modelo nem aprova telas.

| Cenario | Resultado esperado |
|---|---|
| 1. Mude o texto do botao X para Y | Entendimento curto e construcao no prototipo na mesma execucao; sem "posso construir?". |
| 2. Adicione campo X no modal Y | Reutilizar modal atual, construir e apresentar aberto para confirmacao. |
| 3. Sugira uma tela | Apenas proposta; nenhuma construcao. |
| 4. Faca direto no real | Respeitar REAL e protecoes; nao presumir deploy. |
| 5. Mude X em A com impacto em B | Construir A se independente; autorizar B antes de alterar, ou bloquear a dependencia inseparavel. |
| 6. Tres telas autorizadas | Tres apresentacoes/aceites individuais, uma por vez. |
| 7. Novo pedido sem responder ao print | Manter primeiro item pendente; registrar/executar novo alcance autorizado. |
| 8. Corrija modal mostrado | Mesmo modal/DNA, nova candidata e confirmacao reaberta. |
| 9. Mude local da funcao | Resolver retirada/permanencia anterior ainda nao decidida. |
| 10. Cinco pedidos integralmente aprovados | Lote Git elegivel conforme `construir`, sem levar pendencias. |
| 11. Quinto pedido com tela nao aprovada | Nao contar como quinto nem enviar esse pedido. |
| 12. Navegador indisponivel | Construir recorte independente se possivel; IMPLEMENTADO_NAO_APRESENTADO, sem screenshot/aceite ficticio. |
| 13. Prototipo aprovado | Nao construir/publicar real automaticamente. |
| 14. Sessao reaberta | Recuperar fila/fonte atual; nao ressuscitar descartados nem presumir plugin recarregado. |

Sem execucao observada, marcar CENARIOS_DO_METODO/ACEITE_FUNCIONAL como NAO_EXECUTADO e distinguir da VALIDACAO_ESTRUTURAL. ACEITE_VISUAL e NAO_SE_APLICA em patch exclusivo do padrao; ensaio de consumidor continua pendente no seu proprio alcance autorizado.

## Validacao do proprio padrao
Executar os comandos do README central. Separar VALIDACAO_ESTRUTURAL, CENARIOS_DO_METODO, ACEITE_FUNCIONAL, ACEITE_VISUAL e ATIVACAO_NA_SESSAO com estados e escopo claros. Teste de parser/links e exemplos em prosa nao sao teste comportamental de modelo. Gate descrito em Markdown nao e fiscal universal de escrita; hook/permissao/sandbox requer implementacao e ensaio no ambiente antes de afirmar bloqueio mecanico.

## Fechamento de seguranca por risco

Quando o recorte tocar acesso, entrada, integracao ou efeito critico, aplicar seguranca e [a matriz de riscos/evidencia](../../references/SEGURANCA.md#auditoria-dirigida--oito-riscos). Triar pertinencia dos oito temas, sem exigir oito suites em todo ajuste; preservar recusas e checks locais obrigatorios. Achado deve apontar evidencia sanitizada, revisao/ambiente, fonte/runtime/aplicacao e estado COMPROVADO/SUSPEITA/NAO_VERIFICADO/NAO_SE_APLICA.

Retestar a correcao e consumidores afetados em ambiente autorizado com dados controlados. Nao concluir controle ativo por leitura/scanner, promover backend simulado ou omitir risco comprovado relevante para liberar a entrega; limites de acesso/ensaio ficam explicitos no registro existente. Auditoria em leitura nao autoriza abrir segredos, modificar dados/roles ou atacar producao. Fiscal independente confronta candidato e evidencias quando exigido; resultado estrutural do padrao nao certifica seguranca dos consumidores.
