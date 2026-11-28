# Medicao, orcamentos e aceite

## Indice

- [Contrato de medicao](#contrato-de-medicao)
- [Orcamentos iniciais](#orcamentos-iniciais)
- [Cenarios de aceite](#cenarios-de-aceite)
- [Avaliador de evidencias](#avaliador-de-evidencias)
- [Fontes tecnicas](#fontes-tecnicas)

## Contrato de medicao

Registrar no dono da tela e no perfil tecnico: revisao Git, build/artefato e
modo release/producao, dispositivo/modelo/RAM/SO, browser/WebView, volume e
distribuicao dos dados, tamanho da fila/anexos, estado de cache/processo,
rede/latencia/banda, temperatura/energia pertinentes, instrumentacao e comandos.
Evidencia sanitizada nao contem tokens, clientes reais nem payload sensivel.

Medir separadamente: primeiro acesso/provisionamento, abertura fria com dados,
abertura/retomada aquecida, navegacao, toque ate feedback, toque ate gravacao
local duravel e ate confirmacao remota, scroll, sync, update e uso prolongado.
Definir inicio/fim concretos de cada marco. Loader visivel nao e gravacao;
carregamento de HTML nao e tela utilizavel. Medir a primeira acao de negocio
para impedir que apenas se mova toda a demora para o primeiro toque.

Capturar amostras brutas e p50/p95 quando pertinente, com numero de amostras
definido pelo perfil e variabilidade; o numero nao e meta artificial de testes.
Comparar baseline e candidato no mesmo perfil/volume/rede. Nao selecionar so
a melhor rodada nem misturar cold start e warm start. Manter traces e logs
com timestamps/medidas por etapa, relacao ao artefato e local recuperavel.
Se perfil mudar, declarar nova serie; nao alegar melhoria comparavel.

Diagnosticar por etapa: processo/shell, concessao local, migration/banco,
consulta, integridade, projecao, serializacao, ponte, parse/execucao JS,
layout/paint e acao; no remoto, rede, backend, consultas e bytes. Instrumentacao
na fonte sem captura real fica NAO_EXECUTADO.

Usar ferramentas ja disponiveis: Performance/User Timing/DevTools e testes de
fluxo no navegador; Perfetto/Macrobenchmark no Android quando compativeis;
instrumentacao do runtime em Flutter/nativo. Lighthouse e evidencia de
laboratorio web, nao certifica APK, escrita offline ou INP de usuarios reais.
Emulador e throttling ajudam diagnostico, mas nao substituem o aparelho alvo.

Medir entrada JS/CSS por transferencia comprimida E bytes descomprimidos/parse,
payload inicial, numero de consultas/round trips, itens processados, bridge,
heap/RSS e crescimento apos ciclos, frame times/jank e tempo de tarefas longas.
Teto de seguranca de 32 MB nao e budget de performance. Limite de 300 linhas
tambem nao mede bytes carregados nem trabalho executado.

## Orcamentos iniciais

Os valores abaixo sao **propostas de partida**, a adaptar ao aparelho/fluxo e
registrar com origem. Nao sao resultado observado nem promessa universal.
Requisito aprovado do projeto prevalece; baseline ruim nao vira meta aceitavel.

| Metrica | Proposta e condicao |
|---|---|
| Abertura fria local utilizavel | p95 ate 1.500 ms, app provisionado, release, aparelho de referencia, sem rede. |
| Retomada local utilizavel | p95 ate 700 ms, contexto/armazenamento validos, mesmo aparelho. |
| Toque ate feedback visual | p95 ate 100 ms; medir tambem conclusao da acao, sem spinner como falso sucesso. |
| Toque ate commit local de acao simples | p95 ate 200 ms, transacao de dados + outbox; fotos grandes e operacoes distintas recebem perfil proprio. |
| Dependencia de rede antes de abrir local | Zero chamadas aguardadas no caminho critico quando existir concessao/local valido. Medir trace com API parada/lenta. |
| JS inicial web | Exemplo de 250 KiB gzip; incluir dependencias transitivas e justificar excecoes pelo fluxo, tambem medir parse/CPU. Nao e teto universal de APK. |
| Dados da primeira pagina | Budget de itens/bytes/consultas explicitado; o custo nao deve exigir percorrer todo o catalogo antes de recortar a pagina. |
| Regressao no mesmo perfil | Exemplo: reprovar aumento acima de 10% na metrica protegida mesmo dentro do teto absoluto, considerando variabilidade conforme contrato. |

Como referencia externa para **experiencia web de campo**, Core Web Vitals usa
p75 com LCP <= 2,5 s, INP <= 200 ms e CLS <= 0,1. Registrar origem das medidas
e separar campo de laboratorio; esses indicadores nao substituem marcos de
abertura/acao do app. Nao prometer 60 FPS constantes: medir frames fora do
budget da taxa do dispositivo e jank no fluxo representativo.

O fiscal nao pode aumentar teto, trocar aparelho, limpar dados ou reduzir
volume para fazer candidato passar. Mudanca de budget precisa justificativa,
origem da decisao e nova comparacao honesta; resultado antigo continua registrado.

## Cenarios de aceite

Selecionar pelo efeito real e incluir os obrigatorios do contrato local:

| Cenario | Evidencia exigida |
|---|---|
| API lenta/parada com dados e sessao local validos | Primeira acao dentro do budget; sync e update nao compoem a barreira. |
| Sem dados na primeira instalacao | Estado claro de provisionamento/offline, sem tarefas inventadas e sem espera infinita. |
| Base local pequena e volume operacional alto | Primeira pagina limitada na consulta, validacao, projecao, ponte e UI; registrar itens/bytes/consultas processados. |
| Mapa, badge ou atualizacao indisponiveis | Operacao principal continua; estado auxiliar honesto e retry limitado. |
| Navegacao, lista longa e uso repetido | Resposta, jank, memoria/listeners e primeira acao medidas; sem reload completo por toque. |
| Encerrar processo logo apos recibo local | Entidade, outbox e anexos prometidos reaparecem; memoria/mock nao serve de prova. |
| Servidor gravou, resposta se perdeu | Reenvio do mesmo ID nao duplica efeito; mesmo ID/payload diferente e recusado. |
| Fila antiga retorna apos prazo de deduplicacao | Reconciliar pelo efeito permanente ou recusar/revisar; nunca aplicar novamente porque o TTL expirou. |
| Duas abas/processos e retomada | Coordenacao recuperavel, sem duplicidade nem lock permanente. |
| Trocar usuario/empresa, expirar concessao, revogar acesso | Nenhum vazamento/envio cruzado; recusas preservadas e pendencias protegidas. |
| Quota cheia, transacao falha e cache removido | Nao anunciar "salvo"; preservar pendencias existentes e oferecer recuperacao prevista. |
| Sync interrompido/exclusoes/cursor expirado | Cursor avanca junto dos dados; nenhuma exclusao perdida ou outbox apagada por novo snapshot. |
| Update com formulario/fila pendentes | Estado duravel preservado, ativacao segura, compatibilidade de schema/API/bridge e retomada. |
| Pacote corrompido, assinatura/origem invalida ou replay | Rejeitar candidata; manter versao saudavel e dados. |
| Download/ativacao interrompidos ou crash do novo app | Em assets, fallback compativel quando suportado; em binario, recuperacao pelo canal real. Nao prometer downgrade silencioso nem apagar dados para reinstalar. |
| Mudanca de plugin/permissao nativa | Nova release binaria pelo canal correto; nao fingir que deploy web atualizou o APK. |
| APK release em aparelho e offline provisionado | Mesmo artefato assinado/identificado abre, responde, conserva fila e atualiza pelo canal ensaiado. |

Fiscal confronta trace/artefato e diff, nao apenas o resumo do executor.
Nao certificar performance no aparelho por build, print, teste de parser,
types, numero de arquivos ou texto "offline first". Nao desativar permissao,
integridade, idempotencia ou durabilidade para atingir um tempo.

## Avaliador de evidencias

Executar o script desta skill com Python 3.10+; nao precisa instalar pacotes.
Ele e uma guarda de resultados fornecidos, nao runner de navegador/aparelho.

```sh
python3 CAMINHO_DA_SKILL/scripts/verificar_desempenho.py \
  --profile PERFIL_APROVADO.json \
  --report RELATORIO_CANDIDATO.json \
  --revision SHA_COMPLETO_TESTADO \
  --evidence-root PASTA_DAS_EVIDENCIAS
```

Em otimizacao/comparacao, exigir `--baseline RELATORIO_ANTERIOR.json` e o
vinculo aprovado desse baseline no perfil. Primeira medicao sem baseline
precisa de motivo registrado e nao pode alegar regressao comparada.
Reutilizar o perfil/runner/evidencias do projeto; so materializar JSON quando
essa guarda for adotada. O [exemplo](../assets/perfil-desempenho.exemplo.json)
tem estado PROPOSTO: adaptar dispositivos, cenarios, checks, budgets e origem
da decisao antes de adota-lo; nao trocar o estado para simular aprovacao.

Contrato JSON do perfil:

- `schema_version: 1`, `profile_id`, `state: "APROVADO"`, `decision_ref`.
- `environment`: `device`, `os`, `runtime` e `physical_device`; a exigencia
  de aparelho fisico e controlada por `require_physical_device`.
- `max_regression_pct` e `budgets`: IDs unicos com `unit`, `stat`
  (`max`/`p50`/`p75`/`p95`/`p99`), `limit`, `min_samples`, `scenario`,
  `network`, `dataset` e `cache`.
- `required_checks`: IDs de cenarios funcionais que precisam de evidencia.
- `baseline`: `policy: "required"` para otimizar/comparar, com `revision`,
  `report_sha256` e `profile_sha256` do relatorio anterior exato. O perfil
  anterior pode ter outro hash; dispositivo/cenario/rede/dataset/cache/unidades
  precisam coincidir com os atuais. Primeira medicao usa `policy: "initial"` e
  `reason` documentado, sem afirmar comparacao; nao e dispensa para otimizacao.

Contrato JSON do relatorio:

- `schema_version: 1`, `profile_id`, `profile_sha256` (bytes exatos do perfil),
  `revision` (40 hex), `build_id`, `build_mode` (`release`/`production`),
  `evidence_type: "MEASURED"`, `environment` e `measured_at` (ISO 8601 com fuso).
- `metrics`: um item por budget com `id`, `unit`, `scenario`, `network`,
  `dataset`, `cache`, `samples` numericas nao negativas e `evidence`.
- `checks`: um item por check exigido com `id`, `status: "PASSOU"` e `evidence`.
- Cada `evidence` e lista nao vazia de objetos `path` relativo a raiz e
  `sha256` do arquivo real. Paths externos/symlinks e hashes divergentes falham.
  Referenciar capturas que permitam ao fiscal confrontar amostras e condicoes.

`count`/`bytes` usam amostras inteiras; `ratio` usa fracao de zero a um.
Data no futuro alem de cinco minutos de tolerancia falha. O baseline pode
exceder o teto atual e nao precisa ter todos os checks funcionais aprovados:
serve de comparacao, nunca de dispensa para os checks do candidato. O hash do
relatorio e a revisao vinculados impedem escolher outro baseline ao executar.

Percentil usa nearest rank (`ceil(p * n / 100)`), informado na saida.
Entrada ausente, duplicada, malformada, nao finita, perfil proposto, SHA/condicao
divergente, check sem execucao/evidencia ou limite excedido resulta em saida 1.
Nao preencher relatorio com numeros inventados. Hash e formato validos nao
atestam a origem verdadeira da medicao: o fiscal ainda verifica os artefatos.
Uma execucao aprovada vale apenas para esse perfil, candidato e alcance.

## Fontes tecnicas

- [Core Web Vitals e limiares](https://web.dev/articles/vitals).
- [User Timing para marcos de aplicacao](https://developer.mozilla.org/en-US/docs/Web/API/User_Timing_API).
- [Android: tempo de inicializacao](https://developer.android.com/topic/performance/vitals/launch-time).
- [Android: Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview).
