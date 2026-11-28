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

## Conferencia obrigatoria do fiscal

Toda criacao, modificacao, correcao, remocao ou reorganizacao passa pelo fiscal antes de encerrar o lote. Seu trabalho e confrontar o pedido e TODAS as exigencias pertinentes das skills com o candidato real e os padroes locais, incluindo codigo, criacao de arquivos e documentacao. Nao limitar a revisao a "funciona" nem confiar apenas no resumo do construtor. Revisao independente quando disponivel/exigida; sem capacidade, separar os papeis conforme iniciar-projeto e declarar o limite, nunca simular outro revisor.

Ler o diff completo, arquivos novos/nao rastreados pertinentes e os donos/consumidores atingidos. Registrar no mecanismo de revisao existente requisito/fonte, alcance/arquivos, evidencia e PASSOU/FALHOU/NAO_EXECUTADO/NAO_SE_APLICA justificado. Nao criar certificado paralelo ou copiar todas as skills para um checklist permanente.

Antes de aceitar alegacao de entrega/aprovacao visual ou elegibilidade para publicacao, aplicar a [trava de encerramento da revisao visual](../interface/SKILL.md#trava-de-encerramento-da-revisao-visual). Confrontar pergunta efetivamente enviada, resposta original do responsavel e evidencia da candidata com pedido/item, ambiente e revisao; status ou resumo do executor nao bastam. Alegacao de conclusao/aceite sem essa cadeia e FALHOU e volta para a correcao prevista no dono. Registro honesto de espera nao e alegacao falsa nem aceite: preservar a pendencia, sem liberar o item para fechamento/publicacao.

| Efeito | O fiscal precisa confrontar |
|---|---|
| Linguagem e arquivo | Stack permitida por escopo; perfil e exemplo de cada tipo; extensao, nome, estrutura interna, imports/exports, finalidade e consumidor real. |
| Pastas e modulo | Raiz aprovada, responsabilidade, fronteiras/contratos publicos, reutilizacao e ausencia de copias/camadas vazias. |
| Componentes e hooks | Dono local/comum, contrato, estado/efeitos, convencao e verificacoes da stack adotada; sem dependencias ou tecnologia introduzidas pelo exemplo. |
| Abertura e resposta de app | Perfil, primeira acao utilizavel, custo limitado da consulta ate a UI, payload/ponte e amostras no dispositivo/volume/rede do contrato. Aplicar [desempenho-mobile](../desempenho-mobile/SKILL.md); score, screenshot, linguagem ou build nao provam velocidade. |
| Offline e atualizacao | Transacao local + outbox, isolamento, idempotencia, cursor/conflito/retomada, compatibilidade e ativacao/rollback ensaiados. Distinguir dados, assets web e binario; deploy web nao atualiza automaticamente APK embarcado. |
| Documentacao | Documento dono atualizado junto do codigo, sumario/IDs/links corretos, origem da decisao, exemplos reais e nenhuma regra contraditoria/duplicada. |
| Interface | Catalogo/revisao, matriz de composicao, medidas/condicoes, tokens/implementacao compartilhados, estados/carregamento, desktop/mobile e efeitos indiretos em consumidores. |
| Diferencas | Base/variante/configuracao/excecao/divergencia classificadas, propriedades e modos delimitados, origem verdadeira; sem aprovacao inventada. Excecao aplicada com os tres vinculos (`E##` no catalogo, `PADRAO_EXCECAO` abaixo do DNA, linha na tela); faltando um, reprova a aplicacao. Definicao ainda nao implementada nao certifica conformidade. |
| Paridade | A mesma peca nas telas tocadas e nas vizinhas tem a mesma forma; diferenca sem excecao/variante registrada reprova ou vira `D##`. ID de peca sem nome de modulo; um icone por significado. |
| Plugins usados | Lista `plugin -> skill -> tela/arquivo -> resultado` do construtor conferida contra a evidencia real (chamada da skill, achados, correcoes): Ponytail com `ponytail-review` no codigo; frontend-design e UI Design Review (celular e desktop) em toda tela/aba/modal criado ou alterado, antes de mostrar. Falta de uso, uso sem evidencia ou achado importante ignorado sem motivo reprova e volta ao construtor; plugin ausente so passa com o limite declarado. Ver [plugins de design](../interface/SKILL.md#plugins-de-design-na-construcao-e-revisao). |
| Cobertura e aceite | Alcance da migracao, consumidores realmente conferidos, evidencias de teste/apresentacao/aceite e pendencias preservadas. |

Decisao do fiscal para cada diferenca visual:

| Evidencia encontrada | Resultado naquele ponto |
|---|---|
| Excecao `E##` aplicada com tres vinculos | Conferir vigencia, base/revisao, tela, modo, propriedades autorizadas e evidencia. PASSOU somente se o delta observado corresponde ao autorizado; o restante continua herdado. Marcador sozinho nao basta. |
| Variante aprovada ou configuracao permitida | Conferir condicao de uso e propriedades previstas, alem do resultado. PASSOU somente dentro desse contrato. |
| Desvio sem cobertura de peca APROVADA | FALHOU; corrigir no alcance autorizado. Nao mudar a referencia para aceitar o desvio. |
| Peca OBSERVADO/A_DEFINIR ou origem incerta | Registrar `D##` e resolver somente a decisao dependente, uma pergunta por vez; nao presumir excecao ou padrao. |
| Peca PROPOSTO sem promocao decidida | Nao certificar como padrao nem impor heranca; preservar base aprovada e aceite local que existirem, resolver a lacuna pertinente. Proposta recusada nao volta como padrao. |

### Conferencia da composicao e das medidas

Confrontar a [matriz e medidas verificaveis](../interface/SKILL.md#matriz-de-composicao-e-medidas-verificaveis) com a fonte/revisao aprovada, o diff e a implementacao renderizada. Conferir regioes, centro/ancoras, condicoes de presenca/quebra, distancias entre bordas, tipografia, densidade e estados pertinentes. Registrar esperado/origem, observado, condicoes, delta e classificacao; codigo com o mesmo token/classe nao basta se overrides ou fontes carregadas mudarem o resultado.

Pedido restrito a largura exige preservar os outros invariantes e exercitar a quebra prevista. Listas equivalentes podem mudar dados/colunas, sem inventar outra densidade; conteudo longo segue a variante e nao prova desvio de altura por si. Screenshot sem fonte/escala nao certifica medidas CSS exatas; falta de renderizacao fica NAO_EXECUTADO/NAO_VERIFICADO. Comparacao controlada e medicao verificam fidelidade, nao aprovam a nova referencia.

Conferir que escolhas explicitas foram persistidas pelo [registro progressivo](../interface/SKILL.md#registro-progressivo-das-decisoes-visuais), mesmo com aplicacao pendente. Nao reprovar uma definicao salva por ainda nao estar construida; reprovar a alegacao de implementacao, cobertura ou aceite sem evidencia. Contradicao com fila temporaria, duplicacao de valores entre donos ou segunda entrevista de escolhas resolvidas exige correcao documental.

Fontes donas: [padrao tecnico local](../../references/ARQUITETURA.md#padrao-tecnico-local), [padroes locais preenchiveis](../../references/DOCUMENTACAO.md#padroes-locais-preenchiveis) e [catalogo de interface](../interface/SKILL.md#catalogo-local-e-promocao-de-uma-peca). Corrigir um arquivo tambem deve respeitar seu perfil; nao exigir reorganizar todo legado por um ajuste local. Desvio preexistente fora do alcance e declarado com local/evidencia e nao confundido com nova excecao aprovada.

Falha corrigivel no alcance devolve ao construtor com criterio violado, local e correcao necessaria; depois o fiscal confere o candidato corrigido e o efeito nas dependencias. Nao encerrar como conforme enquanto requisito aplicavel estiver falho ou sem verificacao indispensavel. Se houver impedimento, declarar entrega parcial/bloqueada e o ponto concreto. "Conforme" vale somente para revisao/alcance verificados, nao e certificacao de todo o sistema, garantia de obediencia futura ou substituto do aceite humano visual.

## Aceite por efeito
- App web/mobile, offline, APK ou update: executar a [matriz de desempenho e recuperacao](../desempenho-mobile/references/medicao-aceite.md#cenarios-de-aceite), no alcance aplicavel. Exigir baseline/candidato, perfis/artefatos e traces reais antes de aprovar velocidade; sem aparelho ou evidencia marcar NAO_EXECUTADO. Avaliador de JSON confere amostras/limites, nao autentica medicao; nao alterar budget para aprovar candidato lento.
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

Lote REAL com dados executa, conforme o [perfil local](../../references/DADOS.md#perfil-local-de-dados), o check de formato de toda migration nova e a trava de acesso ao banco fora da persistencia nos arquivos alterados; falha bloqueia a entrega, sem bypass.

Verificar os perfis de DADOS no candidato exato. Testar registro canonico atualizado por consumidor, recusa fora do escopo, preservacao apos retirada do consumidor, historico, conflitos de identidade, integridade e exclusao concorrente. Testar chat com historico acima do limite, retomada, notas internas, anexos compartilhados e invariantes de cadastro. Modelo/regex/check textual nao comprova comportamento do banco ou do executor.

Uma unificacao so pode ser declarada concluida no alcance quando o DE/PARA esta reconciliado, consumidores usam o contrato vigente, dados/permissao/historico permanecem corretos e medicao pertinente nao revela regressao sem decisao. Nao reprovar por numero de tabelas nem aceitar por simples reducao desse numero. Fonte: [perfis de DADOS](../../references/DADOS.md#reutilizacao-e-propriedade-de-dados).

## Retorno a construcao e publicacao
Falha corrigivel no alcance retorna a `construir`, corrige causa e retesta; nao encerrar apenas como pendencia. Recurso externo ausente exige impedimento concreto, sem prometer execucao futura. Nao afrouxar teste, esconder requisito, apagar baseline ou aceitar screenshot novo sem aprovacao para passar.

Preservar guardas, hooks, CI e fiscal independente quando exigidos pelo contrato local.

Conferir o [registro temporario e seu fechamento](../../references/DOCUMENTACAO.md#manutencao-e-limpeza-do-conhecimento-vigente) pelo diff real: caminhos/simbolos, DNAs, donos atualizados e consumidores atingidos, inclusive itens omitidos pelo executor. Encaminhar divergencias conforme a referencia e reconferir antes de fechar. Lote encerrado nao deixa temporario de mudancas; lote interrompido preserva o aberto. Conferir a [pasta temp](../construir/SKILL.md#pasta-temp-de-perguntas-e-fila-temporarias): sem pergunta entregue, decisao no dono e pasta excluida quando nada ficou aberto. Evidencia canonica/Git e manifestos/recibos exigidos seguem o ciclo local, sem apagamento para contornar guarda. Conferencia do lote nao certifica todo o repositorio.

Fiscal independente confere, alem do codigo, o fechamento documental de tudo o que as skills exigem para o lote: decisao gravada no documento do modulo/tela dono; entrada no historico de entregas com QUEM, COMMITS, FEZ, CONFERIU, FALTA e DESFAZER; limpeza dos registros de trabalho (perguntas abertas e tarefas/aceites pendentes somente na [pasta temp](../construir/SKILL.md#pasta-temp-de-perguntas-e-fila-temporarias), definicoes visuais escolhidas ja no dono com aplicacao separada, pergunta entregue retirada da fila, andamento/pendencias/mapas/marcas de "falta publicar" sem o que foi entregue); inventario/identidades e vinculos reconciliados; migrations aplicadas e conferidas quando o codigo depende delas. Ausencia de qualquer um e lacuna, nao observacao. Em lote que publica tela/aba/modal prototipado, o fiscal confere tambem a comparacao prototipo x real (`prototipo-real`, fechamento da conversao): diferencas no andamento, documento da tela so com o real e prototipo apagado quando nada sobrou. Ausencia e lacuna. Candidato contem somente o lote autorizado; sem `--no-verify`, reset destrutivo, amend/force, perda de trabalho alheio ou permissao concedida por conveniencia. Commit, push confirmado, deploy e versao ativa sao distintos.

## Cenarios de execucao imediata do metodo

Conferir os encaminhamentos de `especificar`, `interface` e `prototipo-real`, inclusive contradicoes que reintroduzam pergunta de inicio. Ensaios comportamentais no cliente usam ambiente autorizado e a fila existente, sem alterar produto por uma tarefa limitada ao padrao. Registrar comando/passos, revisao, resposta observada e limites; revisao textual nao executa um modelo nem aprova telas.

| Cenario | Resultado esperado |
|---|---|
| 1. Mude o texto do botao X para Y | Entendimento curto e construcao no prototipo na mesma execucao; sem "posso construir?". |
| 2. Adicione campo X no modal Y | Reutilizar modal atual, construir e apresentar aberto para confirmacao. |
| 3. Sugira uma tela | Apenas proposta; nenhuma construcao. |
| 4. Faca direto no real | Respeitar REAL e protecoes; nao presumir deploy. |
| 5. Mude X em A com impacto em B | Construir A se independente; autorizar B somente se fora do alcance vigente, ou bloquear a dependencia inseparavel. |
| 6. Tres telas autorizadas | Tres apresentacoes/aceites individuais, uma por vez. |
| 7. Novo pedido sem responder ao print | Manter primeiro item pendente; registrar/executar novo alcance autorizado. |
| 8. Corrija modal mostrado | Mesmo modal/DNA, nova candidata e confirmacao reaberta. |
| 9. Mude local da funcao | Resolver retirada/permanencia anterior ainda nao decidida. |
| 10. Cinco pedidos integralmente aprovados | Lote Git elegivel conforme `construir`, sem levar pendencias. |
| 11. Quinto pedido com tela nao aprovada | Nao contar como quinto nem enviar esse pedido. |
| 12. Navegador indisponivel | Construir recorte independente se possivel; IMPLEMENTADO_NAO_APRESENTADO, sem screenshot/aceite ficticio. |
| 13. Prototipo aprovado | Nao construir/publicar real automaticamente. |
| 14. Sessao reaberta | Recuperar fila/fonte atual; nao ressuscitar descartados nem presumir plugin recarregado. |
| 15. Esta lista ficou boa | Confirmar somente a revisao mostrada; perguntar se deve virar padrao quando a promocao ainda nao foi decidida. |
| 16. Use esta lista como padrao em todas as equivalentes | Registrar peca/revisao e alcance; varrer/migrar equivalentes sem nova permissao por tela; aceite dos resultados continua individual. |
| 17. Tabela desktop e cartoes mobile aprovados | Duas variantes da mesma peca, com contrato comum; nao excecoes arbitrarias nem aceite presumido do modo nao mostrado. |
| 18. Somente o menu mobile da tela X deve diferir | Registrar pedido, modo/propriedades e motivo conhecido; restante herda o padrao. |
| 19. Diferenca antiga sem origem | Investigar/classificar; nao inventar que foi a pedido nem substitui-la sem resolver o alcance e a intencionalidade incerta. |
| 20. Projeto sem pastas/documentacao | Materializar donos/perfis da primeira capacidade; criar somente arquivos usados, completar conforme as decisoes. |
| 21. Projeto PHP; exemplo React no pacote | Seguir o perfil PHP; exemplo nao autoriza trocar stack nem criar hooks. |
| 22. Modulo financeiro em React autorizado | Seguir perfil local ou exemplo condicional, contratos, nomes e documentacao; fiscal confere arquivos realmente criados. |
| 23. Catalogo/TRD existente | Completar equivalente e manter IDs; nao criar segunda fonte ou reabrir escolha aprovada. |
| 24. Codigo funciona, mas nome/pasta/documentacao violam contrato | Fiscal reprova o desvio no alcance, devolve para correcao e reconfere; funcionamento sozinho nao fecha a entrega. |
| 25. Mude o botao X (peca APROVADA), sem definir alcance | Listar consumidores e perguntar "troca em todas ou excecao so desta tela?" somente se a decisao ainda nao estiver expressa; nao alterar a peca comum sem esse alcance. |
| 26. Responsavel: "so aqui" | Registrar definicao no proximo `E##`; no lote de aplicacao, completar marcador abaixo do DNA e linha na tela. Restante herda o padrao. |
| 27. Responsavel: "em todas" | Nova revisao da peca e migracao dos equivalentes em lotes autorizados, com cobertura e aceite separados; sem perguntar de novo por tela. |
| 28. Diferenca achada sem pedido | "Nao esta no padrao (`<id>` Rn)"; sem excecao: APROVADO corrige, OBSERVADO/A_DEFINIR vira `D##` com pergunta unica. |
| 29. Peca nova aceita localmente sem resposta sobre promocao | Aceite local permanece; promocao pendente nao vira heranca obrigatoria. Resolver somente a escolha necessaria e nao reapresentar uma candidata recusada. |
| 30. Mesma peca diferente em duas telas | Fiscal reprova ou registra `D##`; nunca aceita as duas formas sem excecao/variante. |
| 31. Primeira interface sem padrao definido | Recuperar referencias, perguntar uma decisao ausente com opcoes e motivo; salvar cada escolha, completar apenas familias usadas. |
| 32. Use a tela aprovada como matriz e amplie somente a largura | Reusar composicao/pecas; registrar o delta de largura e preservar tipografia, densidade e demais invariantes, com comparacao controlada. |
| 33. Abas e posicao da acao ja foram escolhidas | Salvar ou recuperar essas regras; nao entrevistar de novo. Resolver apenas a condicao de quebra se ainda indispensavel e ausente. |
| 34. Ha somente screenshot, sem fonte/renderizacao acessivel | Referencia visual identificada; medidas observadas/estimadas e lacunas explicitas, sem px CSS ou familia de fonte certificados. |
| 35. Nova regra visual escolhida, codigo ainda nao alterado | Definicao salva imediatamente no dono; implementacao, apresentacao, aceite e cobertura continuam pendentes. |
| 36. Excecao de largura mobile numa tela com tres vinculos | Conferir somente esse delta/condicao autorizados; mudanca adicional de cor, fonte ou desktop continua sendo desvio. |
| 37. Nova lista com outras colunas ou mais registros | Configuracao do dominio muda; matriz, densidade e comportamento comuns permanecem, respeitando conteudo longo e variantes. |
| 38. Tela mostrada, pergunta apenas escrita na fila, executor declara entregue | Fiscal reprova a alegacao; retomar a candidata, reapresentar e enviar a pergunta conforme a trava de encerramento. |
| 39. Resposta usada pertence a outro item, ambiente ou candidata anterior alterada | Nao fechar com esse aceite; preservar o mesmo pedido/item e resolver a confirmacao da revisao correspondente. |
| 40. Cadeia de apresentacao, pergunta e aceite ja comprovada para a candidata atual | Reconhecer o aceite existente sem nova entrevista; conferir cobertura e demais requisitos aplicaveis. |

Sem execucao observada, marcar CENARIOS_DO_METODO/ACEITE_FUNCIONAL como NAO_EXECUTADO e distinguir da VALIDACAO_ESTRUTURAL. ACEITE_VISUAL e NAO_SE_APLICA em patch exclusivo do padrao; ensaio de consumidor continua pendente no seu proprio alcance autorizado.

## Validacao do proprio padrao
Executar os comandos do README central. Separar VALIDACAO_ESTRUTURAL, CENARIOS_DO_METODO, ACEITE_FUNCIONAL, ACEITE_VISUAL e ATIVACAO_NA_SESSAO com estados e escopo claros. Teste de parser/links e exemplos em prosa nao sao teste comportamental de modelo. Gate descrito em Markdown nao e fiscal universal de escrita; hook/permissao/sandbox requer implementacao e ensaio no ambiente antes de afirmar bloqueio mecanico.

## Fechamento de seguranca por risco

Quando o recorte tocar acesso, entrada, integracao ou efeito critico, aplicar seguranca e [a matriz de riscos/evidencia](../../references/SEGURANCA.md#auditoria-dirigida--oito-riscos). Triar pertinencia dos oito temas, sem exigir oito suites em todo ajuste; preservar recusas e checks locais obrigatorios. Achado deve apontar evidencia sanitizada, revisao/ambiente, fonte/runtime/aplicacao e estado COMPROVADO/SUSPEITA/NAO_VERIFICADO/NAO_SE_APLICA.

Retestar a correcao e consumidores afetados em ambiente autorizado com dados controlados. Nao concluir controle ativo por leitura/scanner, promover backend simulado ou omitir risco comprovado relevante para liberar a entrega; limites de acesso/ensaio ficam explicitos no registro existente. Auditoria em leitura nao autoriza abrir segredos, modificar dados/roles ou atacar producao. Fiscal independente confronta candidato e evidencias quando exigido; resultado estrutural do padrao nao certifica seguranca dos consumidores.

## Conexoes funcionais no alcance autorizado

Aplicar o gate por ligacao: testar entrada, contrato, persistencia aplicavel, consumidor e reflexos de edicao/cancelamento, preservando nao autorizados. Botao sem acao, contrato sem chamada e chamada sem efeito reprovam; distinguir simulacao, real, aceite visual e NAO_EXECUTADO. Fonte dona: [conexoes funcionais e rastreabilidade bidirecional](../../references/DOCUMENTACAO.md#conexoes-funcionais-e-rastreabilidade-bidirecional), incluindo estados, auditoria seletiva e cenarios de aceite; nao duplicar esse esquema aqui.

## Paridade e concorrencia

Quando o pedido tocar fontes concorrentes ou publicacao parcial, conferir [paridade da instancia](../prototipo-real/SKILL.md#evidencias-proporcionais-de-paridade) e [grupo de integracao funcional](../construir/SKILL.md#integracao-de-trabalhos-concorrentes). Cobrir conflito, composicao de fontes, residuos e compatibilidade no recorte pertinente; teste textual nao comprova bloqueio mecanico nem runtime.

### Rastreabilidade de entrega — complemento

Aplicar [registro obrigatório de Issue, PR e histórico](../../references/DOCUMENTACAO.md#registro-obrigatorio-de-issue-pr-e-historico-emenda-2026-10-31). Conferir IDs existentes, não inventar DNA, registrar pendências e evidências, e conciliar o diff real antes da integração.
