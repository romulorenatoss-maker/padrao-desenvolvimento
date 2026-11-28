# Receita de construcao para abertura e resposta rapidas

## Indice

- [Perfil e estrutura](#perfil-e-estrutura)
- [Sequencia de abertura](#sequencia-de-abertura)
- [Interacao e carregamento](#interacao-e-carregamento)
- [Persistencia e contratos](#persistencia-e-contratos)
- [Preparacao do APK](#preparacao-do-apk)
- [Fontes tecnicas](#fontes-tecnicas)

## Perfil e estrutura

Usar a raiz/convencao existente. A tabela e referencia para a primeira
capacidade de um frontend TypeScript autorizado, nao ordem para criar
arquivos vazios. Em JavaScript manter responsabilidades com contratos
documentados; em React, a view pode ser TSX. Separacao de arquivos nao implica
baixar um script separado para cada arquivo: o build define chunks por uso.

| Arquivo de referencia | Responsabilidade, entrada e limite |
|---|---|
| `src/app/iniciar.ts` | Compor dependencias, abrir sessao local/primeira tela, registrar lifecycle e tempos. Nao sincronizar toda a base nem importar todos os modulos. |
| `src/modules/execucao/ui/ExecucaoView.ts` | Renderizar estado/projecao e emitir intencoes. Sem SQL, IndexedDB, token, API ou regra oficial dentro do componente. |
| `src/modules/execucao/application/registrar-acao.ts` | Validar a intencao local e pedir uma transacao ao repositorio; devolver recibo local/pendencia. Nao fazer duas gravacoes independentes para entidade e fila. |
| `src/modules/execucao/domain/contratos.ts` | Tipos, IDs, unidades, estados e versoes compartilhados do dominio. Nao duplicar o contrato por tela. |
| `src/modules/execucao/data/repositorio-local.ts` | Consultar projecoes/indexes paginados; transacionar dados e outbox por usuario/empresa. Nao carregar a tabela inteira para montar o primeiro item. |
| `src/platform/web/armazenamento.ts` | Adaptador IndexedDB, transacoes/migrations, erros de quota e troca de contexto. Nunca usar localStorage para uma base operacional crescente. |
| `src/platform/android/armazenamento.ts` | Adaptador SQLite/bridge quando adotado, com mesma semantica observavel. Plugin exige manutencao/compatibilidade conferidas; SQLite nao e criptografia por si. |
| `src/sync/coordenador.ts` | Conciliar outbox e deltas remotos com concorrencia limitada, prioridade e cancelamento; uma rodada ativa por contexto. |
| `src/updates/coordenador.ts` | Checar/baixar/validar e ativar versao em ponto seguro, sem bloquear entrada regular. Seguir o contrato de atualizacao. |
| `src/platform/contratos.ts` | Portas minimas realmente usadas para persistencia, rede, relogio e lifecycle. Sem framework de abstracoes universais. |
| `capacitor.config.ts` e `android/` | Configuracao e projeto Android quando o APK fizer parte do lote. Assets compilados locais; configuracao de release separada de desenvolvimento. |
| Testes e documentos no destino existente | Fluxo real, isolamento, falhas, budgets e build; nao copiar o exemplo como evidencia de implementacao. |

A raiz comum so e extraida quando existirem consumidores reais. Codigo de
dominio nao importa WebView, DOM, React ou Capacitor. Isolar deteccao de
plataforma na composicao/adaptadores; nao espalhar `if Android` por botoes.
Backend continua no dono atual; evitar dois sistemas independentes de regra.

## Sequencia de abertura

Construir e instrumentar nesta ordem:

1. **Entrada do processo/documento:** carregar somente shell, estilos criticos,
   fonte local/fallback e codigo necessario a primeira acao.
2. **Contexto local:** abrir armazenamento com migration minima compativel e
   conferir identidade/empresa/concessao offline. Nao pedir GPS, push, contatos
   ou atualizar pacotes antes disso. Nao retirar validacao de acesso para acelerar.
3. **Primeira projecao:** consultar campos e indices da primeira pagina/viewport
   com filtro/ordenacao estaveis. Fazer autorizacao e integridade pertinentes
   sobre esse conjunto ou projecao validada equivalente.
4. **Tela utilizavel:** mostrar dados locais autorizados, estado de sincronizacao
   verdadeiro, handlers e acao principal operantes. Registrar marco so depois
   de a tarefa poder ser executada; medir tambem sua conclusao.
5. **Trabalho posterior:** agendar envio/recebimento incremental, atualizacao,
   contadores e prefetch limitado. Pausar/ceder CPU/IO quando houver interacao;
   falha auxiliar tem tratamento independente.

Nao colocar `await sincronizarTudo()`, atualizacao, inventario completo, hash de
toda a base, bootstrap de todas as abas ou `Promise.all` de dependencias
opcionais antes da primeira tela. Um `async` com parse/loop pesado continua
ocupando a thread da interface; timer zero nao prova ausencia de bloqueio.

**Paginar de ponta a ponta:** limitar consulta, verificacao, transformacao,
serializacao, ponte e renderizacao. `listarTudo().slice(0, 50)` continua lendo
tudo. Buscar blocos em loop ate acabar e depois recortar tambem falha. Manter
projecoes/indices de forma incremental, com consistencia, invalidacao e
integridade equivalentes; nao simplesmente apagar verificacoes de seguranca.
Medir com volume operacional alto para descobrir custo proporcional ao total.

**Preparar o shell uma vez:** produzir assets estaticos no build e validar
pacotes na instalacao/atualizacao. Nao reconstruir HTML completo, reescrever CSS,
incorporar todos os recursos em base64 ou transferir a pagina inteira pela ponte
a cada abertura. Verificar integridade na leitura conforme o modelo de ameaca,
com manifestos/indices e caches validos; hash aprovado no passado nao autoriza
conteudo mutavel atual. Batches e projecoes pequenas limitam custo sem remover
isolamento, verificacao de origem ou autenticidade.

Distinguir quatro entradas: primeiro acesso sem dados, abertura fria com dados,
retomada de processo e troca de rota. Nao usar cache aquecido para provar
primeira instalacao. Sem dados locais, exibir estado honesto de provisionamento
ou indisponibilidade; nunca fabricar tarefas nem aguardar infinitamente.

## Interacao e carregamento

| Construir | Evitar e medir |
|---|---|
| Entrada/chunk por rota ou capacidade; import sob demanda | Importar painel administrativo, mapa, editor, PDF, graficos ou todas as abas na Execucao. Separar arquivo sem reduzir import inicial nao resolve. |
| Estado com dono unico; seletores e atualizacao do item afetado | Recarregar documento/WebView ou renderizar lista inteira a cada toque/autosave/sync; estado duplicado que exige conciliacao constante. |
| Consulta paginada + virtualizacao quando o DOM exigir | Milhares de linhas/componentes invisiveis. Virtualizar DOM sozinho nao reduz consulta nem serializacao. Preservar foco, teclado e acessibilidade. |
| Busca com debounce adequado, cancelamento e identidade da requisicao | Resposta atrasada sobrescrevendo filtro/empresa atual; polls sobrepostos, retry sem limite e listeners duplicados. |
| Worker/isolate para CPU pesada comprovada | JSON gigante, hashes, compressao ou imagem na thread da UI; transferir buffers/deltas quando disponivel e medir custo de copia/ponte. |
| Imagens dimensionadas, thumbnails e limites de anexos | Base64 em JSON/estado/global/localStorage; decodificar fotos originais para miniatura. |
| Atualizacao incremental e batches curtos | Consultas N+1, varredura completa por badge e locks longos na fila/banco durante interacao. |
| Liberar listeners, timers, observadores e recursos ao sair | Crescimento de heap apos cada ida/volta de tela; assinatura realtime duplicada. |
| Fontes/assets essenciais embarcados ou cacheados no perfil offline | CDN obrigatoria no primeiro toque, fontes bloqueantes, videos/imagens pesadas antes do conteudo util. |
| Feedback imediato, estado honesto e erro recuperavel | Spinner rapido usado para esconder demora da gravacao; esconder botao/funcao para cumprir budget. |

No servidor, aplicar a fonte de [desempenho de dados](../../../references/DADOS.md#desempenho-e-prova-de-consolidacao):
escopo autorizado, campos limitados, paginas, consultas em lote e indices
comprovados. Medir DNS/conexao, TLS, TTFB, cold start, pool, consulta, bytes e
renderizacao; nao culpar o navegador por espera do backend ou vice-versa.

## Persistencia e contratos

Definir interfaces pequenas que permitam testar o comportamento dos adaptadores.
Contrato minimo ilustrativo, a adaptar ao dominio e nao copiar como API pronta:

```ts
interface RepositorioExecucao {
  lerPagina(escopo: EscopoAutorizado, cursor?: string): Promise<PaginaLocal>;
  registrarComPendencia(comando: ComandoLocal): Promise<ReciboLocal>;
}
// registrarComPendencia confirma UMA transacao de dados + outbox.
// ReciboLocal identifica operacao e estado PENDENTE, nunca aceite do servidor.
interface Sincronizador {
  solicitarRodada(escopo: EscopoAutorizado): void;
  encerrarContexto(): Promise<void>;
}
// A abertura aguarda lerPagina; nao aguarda uma rodada de sincronizacao.
```

Especificar cancelamento, erros, schema, tenant/usuario, concorrencia e limites
nos contratos reais. Os tipos ilustrativos acima sao vocabulario, nao
implementacao. Testar IndexedDB e SQLite com a mesma suite de comportamentos.
Nao usar uma implementacao em memoria como prova de durabilidade.

Aplicar [offline e atualizacao](offline-atualizacao.md). A migracao de fila
legada importa pendencias de forma transacional/idempotente, valida contagem e
IDs e preserva a origem ate confirmar recuperacao; nunca limpar localStorage
antes de confirmar a conversao. Nao transformar recusas antigas em enviadas.

## Preparacao do APK

1. Confirmar frontend estatico empacotavel, `index.html` e build de producao.
   PHP continua no servidor via API; remover dependencia de HTML gerado
   remotamente para abrir offline. Reaproveitar contratos, nao empacotar sessao
   ou dados de uma pessoa no bundle.
2. Fixar versoes compativeis de runtime/CLI/Android/plugins, Node, JDK, SDK e
   Gradle pela documentacao da versao adotada; lockfile e wrapper reproduziveis.
   Nao gravar "latest" nem comandos com versoes inventadas.
3. Configurar appId, nome, `webDir` apontando ao build e origens de API. Em
   release, omitir `server.url` de live reload; desativar cleartext, mixed
   content e debug. HTTPS/allowlist e politica CSP compativeis com a aplicacao.
4. Rodar os comandos reais do projeto; sequencia de referencia:
   `npm ci` -> `npm run build` -> `npx cap sync android` ->
   `./gradlew assembleRelease` ou `./gradlew bundleRelease` dentro de `android/`.
   Node/npm e comandos so valem se adotados; Windows usa `gradlew.bat`.
5. Assinar pelo canal aprovado, com chaves fora do Git/logs e referencias
   seguras. Validar assinatura, appId, versionCode, permissoes, ABI, tamanho
   instalado e compatibilidade. APK debug nao e entrega release; AAB e pacote
   para distribuicao por loja, nao APK diretamente instalavel.
6. Instalar e testar o artefato exato em aparelho de referencia: abertura,
   operacao, encerramento/reabertura, offline apos provisionamento e upgrade
   preservando fila/dados. Conferir navegador e APK separadamente.

Permissoes nativas so quando a capacidade for usada. Origin allowlist nao
substitui autorizacao da API. Rotas externas nao confiaveis abrem fora da
WebView privilegiada; bridge nao aceita JavaScript, SQL, metodo ou caminho
arbitrarios. Tokens/chaves seguem [seguranca](../../../references/SEGURANCA.md).
Nao criar endpoints de debug nem desativar autenticacao para simplificar APK.

## Fontes tecnicas

Conferir compatibilidade na versao realmente adotada:

- [Capacitor: runtime web/nativo](https://capacitorjs.com/docs).
- [Configuracao Capacitor, webDir e server](https://capacitorjs.com/docs/config).
- [Workflow de build e sincronizacao](https://capacitorjs.com/docs/basics/workflow).
- [Arquitetura offline Android](https://developer.android.com/topic/architecture/data-layer/offline-first).
- [Dividir tarefas longas na web](https://web.dev/articles/optimize-long-tasks).
- [Riscos de bridge WebView](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges).
