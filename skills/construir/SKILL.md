---
name: construir
description: "Use para implementar funcionalidades, corrigir bugs ou alterar codigo dentro do Padrao de Desenvolvimento, depois de analisar e antes de verificar."
---

# Construir

Construa o menor lote coerente que cumpra integralmente o pedido.

Fluxo: pedido/decisao -> impacto -> implementacao -> documentacao canonica atingida -> verificacao.

Preserve a arquitetura real. Quando o projeto usa separacao equivalente, respeite responsabilidades de interface/entrada, normalizacao, regra/autorizacao, persistencia/contrato e integridade de banco. Nao crie camada vazia apenas para satisfazer nomes.

Reutilize antes de criar. Arquivo novo exige responsabilidade nova ou separacao tecnicamente necessaria e consumidor real. Nao fabrique CRUD completo, dashboard, configuracao, exportacao ou abstracao para o futuro.

Bug: reproduzir/evidenciar -> localizar menor cadeia responsavel -> corrigir causa -> repetir cenario -> verificar dependencia direta.

Frontend apresenta; servidor decide efeitos oficiais; banco protege invariantes. Nao confie em campo do cliente para empresa, permissao, preco, saldo, estoque ou propriedade.

Nao misture refatoracao conveniente com o alcance pedido. Nao reverta trabalho alheio.

Em criacao ou separacao de JavaScript autorizada, aplicar [responsabilidades, nomes e limites](../../references/ARQUITETURA.md#javascript-por-responsabilidade-e-tamanho) e [cabecalho/DNA junto da unidade funcional](../../references/DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo). Reconciliar carregamento, interface publica, mapas e consumidores; comentario/ID nao substitui contrato ou teste. Prototipo segue a mesma organizacao reutilizavel, com simulacao isolada.

Aplique seguranca quando houver superficie de seguranca e documentacao quando o conhecimento canonico mudar. Termine com verificar.

## Modulos, limites e remocao
Modulo novo so nasce quando a responsabilidade foi aprovada e nao pertence a modulo existente; criar somente arquivos usados pela primeira capacidade. Nao acessar tabela interna de outro modulo para contornar seu contrato. Nao copiar modulo para criar outro.

Limpeza separa:
- temporario/gerado reproduzivel: remover somente em destino descartavel, sem fonte unica nem trabalho pendente;
- codigo/doc aparentemente orfao: buscar caminho, nome, ID, simbolo, rota, imports, chamadas, menu, jobs, contratos, testes, assets e referencias dinamicas; classificar ATIVO, COMPARTILHADO, HISTORICO, COMPATIBILIDADE, GERADO/TEMPORARIO, CANDIDATO_A_REMOCAO ou FINALIDADE_NAO_COMPROVADA (este ultimo nao autoriza apagar);
- dados persistentes: nunca apagar por limpeza de codigo.

Remocao autorizada reconcilia no mesmo lote os vinculos afetados: codigo, rota/menu, consumidores, contrato, permissao exclusiva, docs, inventario e testes. Historico fica no Git; nao criar copias `old`, `backup` ou `v2`.

Rastrear nos dois sentidos: requisito/DNA -> dono -> codigo/assets -> entrada/contrato/RPC -> dados e consumidores -> teste, conforme os elos realmente existentes. Substituir uma ponta exige conferir as demais e retirar residuos exclusivos comprovados; mapa tecnicamente exigido continua nominal e atualizado. Busca textual vazia nao prova desuso dinamico. Migrations publicadas, auditoria e dados historicos nao sao residuos de codigo; sem prova ou autorizacao, declarar o limite em vez de apagar.

Limpeza dos registros de trabalho: registro de perguntas, andamento/fila, pendencias, mapas de construcao e marcas de "falta publicar" guardam so o que esta aberto. O lote que constroi e publica uma entrega retira, no mesmo commit, tudo o que ela concluiu nesses registros (pergunta respondida, linha do andamento, item da fila, pendencia, marca). Decisao fica no documento do modulo dono, nunca no registro. Nenhum lote fecha deixando registro de coisa ja entregue; o historico fica no Git.

Substituicao de decisao pelo responsavel: identificar o comportamento anterior, a nova regra e seus consumidores antes de alterar. No mesmo lote, retirar efetivamente codigo, validacoes, textos, controles e referencias que ficaram sem uso ou contradizem a nova decisao; reconciliar pedidos/perguntas/fila e mapas documentais, inclusive prototipo, para descrever a versao atual. Nao acumular regras antigas como alternativas ativas nem pedir aprovacao de pedido substituido. Preservar historico no Git, dados persistentes e trabalho alheio; remocao depende de consumidores conferidos. Testar a nova regra e a ausencia do comportamento antigo no alcance atingido. Sem evidencia de retirada, nao afirmar limpeza concluida.


Historico de entregas: toda entrega publicada ganha, no mesmo commit, uma entrada no topo do historico de lote do projeto ([destinos documentais](../../references/DOCUMENTACAO.md)) com QUEM (qual IA ou pessoa), COMMITS, FEZ (o que do prototipo/pedido aprovado ficou construido no real), CONFERIU, FALTA e DESFAZER. E por ela que outra IA responde o que ja foi construido. Lote publicado sem essa entrada nao fecha.

Nao abrir auditoria global nem refatorar modulo inteiro para corrigir defeito local conhecido.

## Reconstrucao fiel de modulo

Confirmar origem/revisao, destino e alcance autorizados; consultar o [guia de reconstrucao](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao) e conferir fontes, assets, contratos, dados/RPCs, configuracao e consumidores reais. Reutilizar a implementacao aprovada na ordem de suas dependencias, preservando stack, limites, interface e DNAs da mesma capacidade; nao criar arquitetura paralela nem importar identidade, dados privados ou segredos de outro projeto. Dependencia ausente e lacuna a resolver no dono, nao oportunidade de fabricar substituto.

Criar/aplicar banco, instalar dependencias e publicar sao autorizacoes distintas. Ensaiar a cadeia no destino permitido com dados controlados e comparar comportamento/interface com a referencia; registrar dependencias externas nao exercitadas. Reconstrucao parcial nao e copia completa certificada; corrigir desvios do alcance e atualizar o guia existente, sem duplicar a regra de negocio em prosa.

## Entrada obrigatoria e construcao conectada
Antes de criar/alterar, consultar `especificar` e a revisao aprovada aplicavel; efeito de interface chama `interface`. Correcao fiel ao contrato usa o caminho curto dessas skills, nao dispensa leitura. Nao construir funcionalidade enquanto falta aprovacao exigida.

Cada elemento novo/alterado precisa da tarefa e do efeito definidos no contrato de utilidade. Nao fabricar botoes, abas, campos ou funcoes para parecer completo. Preserve requisito aprovado: remover/esconder um botao necessario nao corrige sua implementacao.

Implemente uma capacidade vertical coerente: entrada/navegacao -> tela/acao -> contrato -> regra/autorizacao -> persistencia quando aplicavel -> resposta -> estado/consumidores -> teste e documentacao. Essas sao responsabilidades, nao obrigacao de criar arquivo/camada para cada seta.

Classifique a acao: LOCAL, NAVEGACAO, CONSULTA ou MUTACAO. Fechar modal/trocar aba nao exige API; mutacao oficial nao pode ser fingida no estado local. Campo pode ser persistido, calculado, exibido, filtro ou temporario; nao inventar coluna para todo input.

Localize contratos/dados/consumidores reais antes de conectar. Capacidade ausente nasce no dono correto com necessidade aprovada, nao como modulo paralelo. Reutilize componentes/validacao/controle de acesso e preserve compatibilidade dos consumidores.

Sucesso persistente so apos confirmacao oficial; resultado incerto por falha de rede exige reconciliacao antes de repetir mutacao critica. Defina queries/dados/consumidores a atualizar, inclusive outras sessoes quando a regra exigir. Invalidacao de cache nao garante sincronizacao universal. Planeje erro, timeout, recuperacao, repeticao/concorrencia e estados pertinentes com `seguranca`.

Execute integracao real em ambiente autorizado com dados de teste controlados. Nao usar operacao real de cliente em producao para demonstracao. Fixture isolada de teste nao e fallback de producao.

## Ciclo de correcao ate o aceite
Construir -> executar -> observar -> corrigir a causa -> repetir verificacao e dependencias atingidas. Defeito tecnico corrigivel no alcance nao vira entrega encerrada apenas como pendencia. Se uma tentativa nao resolver, mudar diagnostico a partir das evidencias; nao repetir a mesma tentativa nem ampliar escopo silenciosamente.

Parar a parte dependente somente diante de decisao de negocio ausente, autorizacao especifica, risco fora do alcance ou recurso externo indispensavel indisponivel. Informar impedimento concreto, tentativas e o que falta; nao prometer execucao futura nem inventar sucesso. Concluir exige o aceite pertinente de `verificar`.

## Previsao de arquivos e estrutura
Antes de qualquer arquivo novo, aplicar o gate de `analisar` e os [destinos e nomes](../../references/ARQUITETURA.md). Sem previsao expressa e necessidade comprovada, exigir `0393` especifico; nao executar gerador antes desse exame. Organizacao ampla usa `auditar-projeto`. Sem equivalente, usar o fallback autorizado, sem inventar arvore ou perguntar convencao que ja esta definida.

## Salvamento frequente no Git
Salvar os arquivos no disco durante o trabalho. Fazer commit de preservacao a cada 5 alteracoes logicas concluidas e verificadas, ou antes ao encerrar o trabalho, interromper ou receber "salvar tudo". Uma alteracao logica e um ajuste de comportamento, interface ou regra com seus consumidores/documentos; nao contar teclas, arquivos ou decisoes ainda nao implementadas. Nao esperar a quinta quando o lote ja estiver pronto.

Incluir todas as alteracoes autorizadas acumuladas, inclusive codigo real, fontes do prototipo local, regras pedidas, mapas documentais, testes e remocoes pertinentes. "Salvar tudo" autoriza reunir esses lotes; inventariar tambem arquivos novos e excluidos, conferir diff e indice e adicionar caminhos explicitamente, nunca `git add -A`. Trabalho paralelo em arquivo compartilhado e preservado; trabalho alheio fora do alcance exige ordem expressa, nao e apagado nem incluido silenciosamente. Excluir segredos, dados privados e gerados descartaveis; fonte unica de prototipo nao e descartavel.

Executar guardas e verificacoes proporcionais antes do commit; nao contornar falhas, protegidos ou autorizacoes especificas. Se o gatilho chegar com bloqueio, informar o impedimento concreto e preservar no disco, sem fingir commit. Commit de preservacao nao certifica conclusao funcional. Confirmar SHA e arquivos gravados; push segue autorizacao aplicavel e deve ter resultado confirmado separadamente. Esta regra orienta o executor: nao instala autosave, contador ou hook automatico.

## Issue, PR e publicacao sem atrasar o prototipo

Toda tarefa logica de correcao, melhoria ou nova funcao tem issue no repositorio dono. Buscar equivalente aberto antes de criar; ajustes do mesmo pedido atualizam a mesma issue, nao geram uma por arquivo, clique, teste ou pergunta. Registrar objetivo, alcance PROTOTIPO/REAL, criterios de aceite e IDs/documentos atingidos, sem copiar toda a especificacao. Criar e atualizar uma vez por marco util; indisponibilidade externa fica explicita no registro existente e nao bloqueia a alteracao local ja autorizada, mas deve ser reconciliada antes da integracao/publicacao.

Para integrar/publicar, trabalhar com PR ligada a cada issue pertinente. A descricao informa problema e resultado, alcance, documentos/DNA, validacao e limites; usar `Closes #numero` somente quando a entrega cumpre o aceite daquela issue. Entrega parcial referencia a issue sem encerra-la. PR de prototipo nao autoriza conversao/deploy real; seguir `prototipo-real`. Abrir draft cedo quando util, atualizar a mesma PR; nao abrir outra por rodada de ajuste.

Separar salvar de integrar: commits de preservacao continuam frequentes; enviar o lote autorizado para uma branch de entrega e abrir PR para a branch oficial, sem push direto que contorne esse fluxo. A pasta compartilhada conserva sua branch e os arquivos atuais: e permitido criar/enviar uma ref de entrega a partir do commit conferido sem fazer checkout, worktree, stash ou reset nessa pasta. Conferir base remota e todos os commits/diffs da ref; nao carregar por acidente trabalhos acumulados fora do lote. Se nao for possivel isolar a entrega com seguranca, combinar a estrategia antes de mexer na pasta. Nao atualizar a copia a partir da branch oficial enquanto houver trabalho paralelo nao salvo.

Merge/publicacao exigem autorizacao aplicavel e checks/revisao requeridos; nao desativar guardas nem usar bypass. Confirmar separadamente PR integrada, SHA publicado e versao ativa quando houver deploy. Nao instalar automerge, protecao de branch ou pipeline de produto por esta regra; requer configuracao autorizada e verificacao. Projeto com contrato local conflitante migra explicitamente, sem aplicar a nova politica no meio de um lote.

Mudancas concorrentes, humanas ou de IAs, precisam de dono/revisor identificados no fluxo existente e base/candidato conferidos. Antes de integrar, verificar se head, dependencias ou base de integracao mudaram desde a evidencia; atualizar somente a verificacao atingida e revisao aplicavel. CODEOWNERS e checks obrigatorios sao opcoes de instrumentacao com configuracao/ensaio autorizados, nao protecao instalada pelo manual. Na pasta compartilhada, combinar propriedade de arquivos antes de editar; nao adotar isolamento/troca de branch contra o contrato local.

No localhost, a entrega visual apos a checagem pertinente continua imediata; registrar issue e fazer verificacoes independentes em paralelo quando ja autorizado. Nao aguardar auditoria global, cobertura total ou servico opcional para mostrar o recorte; cumprir os checks obrigatorios antes de integrar. Documentacao usa os [vinculos DNA/issue/PR](../../references/DOCUMENTACAO.md#rastreabilidade-dna-issue-pr-e-commit).

## Pasta compartilhada entre IAs
Quando mais de uma IA (Claude, Codex ou outra) trabalha no mesmo projeto, todas usam a mesma pasta e o mesmo prototipo; o que vale e o estado atual aprovado pelo responsavel, independente de qual IA fez ou alterou por ultimo.
1. A pasta permanece na branch combinada, normalmente a oficial no projeto existente. Nela e proibido trocar de branch, criar worktree, usar stash, reset, checkout de arquivo, restore ou clean: esses comandos tiram dos arquivos o trabalho de outra IA. A branch oficial remota recebe entregas por PR conforme a secao anterior; isso nao exige trocar a branch desta pasta.
2. Antes de alterar um arquivo, reler como ele esta no disco naquele momento e alterar por cima. Nunca gravar uma copia inteira guardada antes (cache, scratch, versao do Git): isso apaga a alteracao feita depois por outra IA. A ultima alteracao feita sobre o estado atual e a que vale.
   Para telas locais, seguir a [fonte unica ativa de prototipo-real](../prototipo-real/SKILL.md#fonte-unica-ativa-da-tela-local); compartilhar a pasta nao basta se cada acesso carrega uma copia diferente.
3. Commit leva o estado atual dos arquivos dos pedidos autorizados, sem separar autoria, inclusive lotes acumulados quando o responsavel manda "salvar tudo"; seguir Salvamento frequente no Git e adicionar somente caminhos conferidos, nunca `git add -A` da pasta inteira.
4. Antes de atualizar a pasta a partir da branch oficial remota, commitar o pedido em andamento. Se houver alteracao sem commit que nao e do pedido, nao atualizar por cima: avisar o responsavel e esperar.
5. Analisar o trabalho de outra IA e somente leitura, com relatorio ao responsavel (certo, errado, pela metade). Mexer, mover, juntar ou publicar esse trabalho so com ordem expressa do responsavel.
6. Ambiente local unico: todas as IAs usam o mesmo prototipo/servidor local e o mesmo banco de teste definidos nas protecoes locais do projeto. Antes de iniciar, conferir se ja esta no ar e reaproveitar; nunca subir segunda instancia. Sem ordem expressa do responsavel, nao criar container, banco, volume, porta ou servidor de teste/previa novo; ensaio com banco usa o banco de teste existente com desfazer ao final. Recurso temporario autorizado e removido pela propria IA ao terminar, informando a remocao; container parado ou volume orfao encontrado e listado ao responsavel e apagado so com ok dele.

Para testes e criterio de parada, seguir [verificar](../verificar/SKILL.md#testar-corrigir-e-entregar-sem-repeticao-desnecessaria): validar o pedido, corrigir falhas e retestar os pontos atingidos; validou, entregar sem repeticao ou ampliacao sem motivo.

Perfil otimizado e mecanismos por cliente seguem [iniciar-projeto](../iniciar-projeto/SKILL.md#perfil-de-execucao-otimizado-por-cliente); configuracao nao comprova ativacao.

## Encerramento e reset da sessao do executor

Antes do reset: verificar aceite/checks e fiscal exigido, salvar fonte e documentacao canonica, conferir Git/recibo pertinentes e registrar resultado/pendencias e proxima tarefa no registro existente. Pendencia que impede fechar o proprio recorte, aprovacao aguardada, agente ainda ativo ou escrita compartilhada sem liberacao impedem o reset. Pendencias externas ao alcance entregue ficam no dono, sem inventar conclusao.

Depois desse fechamento, executar o reset real somente na sessao do executor e pelo mecanismo suportado/configurado do cliente, conforme autorizacao vigente; `/clear` nao e um comando universal de shell. Nao resetar o coordenador, interromper trabalho, apagar memoria/documentos/dados ou criar outro executor concorrente. Se o host nao expoe esse mecanismo, declarar reset nao executado; nao simular limpeza dizendo que esqueceu.

Confirmar o novo contexto/identificador quando aplicavel, preservando projeto/caminho/ambiente e regras de acesso. A proxima tarefa carrega AGENTS -> mapa de `analisar` -> skills pertinentes -> registro/DNA, sem recuperar historico inteiro. Essa diretriz nao instala hooks nem garante economia de creditos. Nao fazer reset a cada pequena correcao da mesma tarefa.
