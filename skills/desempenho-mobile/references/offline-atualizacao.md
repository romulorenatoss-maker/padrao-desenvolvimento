# Offline, sincronizacao e atualizacao do app

## Indice

- [Persistencia e sessao local](#persistencia-e-sessao-local)
- [Operacao e sincronizacao](#operacao-e-sincronizacao)
- [Atualizacao automatica desde a primeira versao](#atualizacao-automatica-desde-a-primeira-versao)
- [Canais de distribuicao](#canais-de-distribuicao)
- [Fontes tecnicas](#fontes-tecnicas)

## Persistencia e sessao local

Registrar o subconjunto necessario/autorizado para o trabalho, periodo de uso,
limites, indices e politica de retencao. Nao copiar todo o banco. UI acessa
persistencia local pelo repositorio/adaptador; isso nao concede acesso direto ao
banco central. IndexedDB e a referencia para dados estruturados web; SQLite e
opcao nativa por adaptador adotado. Cache Storage guarda recursos/respostas
explicitamente permitidos; nao e banco transacional de operacoes.

Separar usuario, empresa/tenant, ambiente e identidade da instalacao. Mudanca de
conta cancela callbacks/rodadas antigos e impede leituras/envios cruzados.
Logout bloqueia acesso aos dados anteriores; resolver pendencias pela politica
documentada antes de eventual exclusao. Nao enviar fila A autenticado como B.
Criptografia/chaves no dispositivo seguem o risco real; Preferences,
localStorage, IndexedDB e SQLite comuns nao sao cofres de credenciais.

Primeiro login exige autenticacao online; reabertura offline usa concessao local
previamente emitida/validada, com escopo e validade limitados. Preservar o prazo
ja definido pelo consumidor; nao promover um prazo particular a regra global.
Considerar relogio adulterado/retrocedido, expiracao e revogacao nao observavel
sem rede. Ao expirar, bloquear operacoes dependentes e preservar pendencias;
revalidar no servidor quando conectar. Nenhum cache transforma permissao
revogada em permissao vigente conhecida.

Listar cada acao: permitida offline, somente rascunho, somente leitura ou
exclusivamente online. Saldo, pagamento, estoque, autorizacao e conflitos
continuam decididos pelo dono oficial; registro local de intencao nao confirma
esses efeitos. Nao prometer revogacao remota instantanea sem conexao.

Tratar quota, armazenamento indisponivel, erro de transacao e corrupcao com
estado recuperavel. Pedir persistencia web quando apropriado e verificar
resultado; browser/usuario ainda pode remover dados. Nao prometer durabilidade
absoluta de PWA. Limitar anexos/cache e remover so itens reconstituiveis;
outbox/rascunhos nao sao lixo de cache. Nao usar limpeza total como reparo.
Registrar destino/recuperacao de anexos, sem base64 em JSON.

## Operacao e sincronizacao

Fluxo obrigatorio para escrita offline autorizada:

1. Validar forma/escopo e gerar ID estavel da operacao antes de enviar.
2. Em UMA transacao local, persistir alteracao/rascunho e registro de outbox,
   com usuario/tenant, entidade, versao-base, tipo, payload/versionamento,
   dependencias, tentativas e estado. Anexo precisa estar duravel/referenciado
   antes de confirmar sua inclusao; tratar falha entre arquivo e transacao.
3. Apos commit local, exibir "salvo neste aparelho; envio pendente". Quota ou
   falha nao pode resultar em "salvo". Nao esperar internet para esse recibo.
4. Enviar em lotes pequenos, respeitando ordem por entidade e dependencias.
   Priorizar pendencias sem impedir atualizacoes indispensaveis a sessao,
   versao-base ou conflito. Definir limites de itens, bytes, tempo e concorrencia.
5. Servidor revalida acesso/negocio e aplica idempotencia atomicamente com o
   efeito, escopada por tenant/identidade/operacao. Mesmo ID com payload
   diferente e conflito, nao nova escrita. Resposta perdida repete/reconcilia
   o mesmo ID; sem isso nao alegar "sem duplicidade".
   Retencao da deduplicacao cobre a janela de repeticao/reconciliacao da fila;
   apos expirar, reconciliar pelo ID permanente do efeito ou recusar/revisar.
   Fila antiga nunca transforma operacao ja aplicada em nova por expirar um TTL.
6. Confirmar dados locais e retirar/marcar a pendencia em transacao apos aceite
   oficial. Se o processo morrer entre aceite remoto e limpeza local, a
   repeticao do mesmo ID recupera o resultado sem duplicar o efeito.
7. Receber deltas por cursor opaco/versao estavel, inclusive exclusoes
   (tombstones) e mudancas de permissao. Commitar pagina e cursor juntos;
   nunca avancar cursor de uma pagina nao persistida. Snapshot inicial,
   cursor vencido e ressincronizacao precisam preservar outbox/rascunhos.

Uma rodada ativa por contexto e coordenacao entre abas/processos, por lock ou
lease transacional recuperavel. Booleano em memoria so protege aquela
instancia; nao basta para duas abas. Nao manter lock de UI/banco durante HTTP.
Retentativas com backoff, jitter, timeout e Retry-After quando aplicavel.
Offline/erro temporario preserva; 401/403 exige reautenticacao/revalidacao sem
loop; conflito exige conciliacao de versao; erro de regra vira recusa visivel
e recuperavel. Nao descartar silenciosamente nem repetir erro definitivo.

Acionar no inicio APOS a tela utilizavel, ao retomar, ao registrar pendencia e
ao recuperar conexao, com deduplicacao. `navigator.onLine` e indicio, nao prova
de API acessivel. Pausar/reduzir trabalho auxiliar oculto; reconciliar quando
retomar. Web Background Sync depende de suporte e ciclo do navegador.
WorkManager/tarefas nativas obedecem restricoes do SO; nao garantir JavaScript
continuo em segundo plano nem horario exato de sincronizacao.

Conflitos de estoque/financeiro/transicoes nao usam "ultimo ganha" generico.
Definir dono, versao e resolucao por operacao; eventual escolha do usuario
preserva ambas as evidencias. Adotar migrations versionadas e ensaiadas com
base anterior e fila pendente; migracao lenta precisa estrategia limitada,
progresso e compatibilidade, sem ficar em silencio na splash.

## Atualizacao automatica desde a primeira versao

Implementar o mecanismo no recorte mobile, nao somente documentar "futuro".
Usar o canal existente ou uma implementacao mantida e compativel; nao
inventar downloader/criptografia nem instalar servico pago sem necessidade.

Separar atualizacao de **dados**, **assets web**, **schema local** e **binario
nativo**. A cada mudanca liberada, o pipeline autorizado publica o artefato e
manifesto/canal correspondente; commit isolado ou `cap sync` nao publica nos
celulares. Atualizacao automatica do app nao e atualizacao da skill.

Fluxo obrigatorio, usando as garantias oficiais do canal quando ele gerenciar
assinatura, download e instalacao. Nao duplicar esses mecanismos com um
atualizador proprio nem presumir as mesmas capacidades em todos os canais:

1. Abrir a versao funcional local e tornar a tarefa utilizavel primeiro.
   Depois checar a versao no inicio/retomada e por periodicidade limitada.
   Falha/offline nao prende a abertura; evitar consultar a cada toque.
2. Baixar candidata em area separada com limites de bytes/armazenamento,
   timeout, retomada quando suportada e politica de rede/bateria. Nao concorrer
   agressivamente com envio de operacoes ou uso da tela.
3. Validar canal/origem, autenticidade e integridade dos arquivos pelo mecanismo
   do canal; conferir appId, shell/bridge/API/schema, plataforma e release
   quando aplicaveis.
   Hash recebido junto ao pacote em canal nao confiavel nao prova autoria.
   Em OTA proprio, manifesto assinado/chave confiavel e protecao contra replay;
   rotacao de chaves definida, sem segredo de assinatura no cliente.
4. Preparar migrations compativeis sem trocar o pacote ativo. Ativar somente
   com rascunho duravel, sem transacao em curso e em ponto seguro
   (proxima abertura/rota segura ou decisao do usuario quando necessaria).
   Fila pendente pode continuar se comprovadamente compativel; nao exigir rede
   para drenar toda a fila antes de uma atualizacao compativel.
   Preparar e validar o plano/candidata, nao alterar banco compartilhado
   incompativel enquanto clientes antigos operam. Coordenar abas/processos e
   conexoes; tratar versionchange/blocked no IndexedDB e exclusao mutua no
   adaptador nativo. Executar migration somente no ponto seguro, com estrategia
   transacional/compativel e recuperacao ensaiadas, preservando fila e rascunhos.
5. Em assets/slots controlados pelo app, trocar o ponteiro de forma atomica e
   conservar versao saudavel ate conferir primeira acao, persistencia, bridge e
   retomada. Rollback exige schema/fila compativeis; migration irreversivel
   impede presumir reversao segura. Em binario, usar instalacao e verificacoes
   do canal, sem prometer manter/reinstalar automaticamente o APK anterior.
6. Em falha de assets com fallback suportado, retomar a versao saudavel e
   quarentenar a candidata para nao repetir crash em todo boot. Para binario,
   preservar dados e usar recuperacao realmente suportada: rollout pausado e
   release corretiva com versionCode maior, ou rollback administrado
   comprovado. Nao desinstalar/limpar dados para fazer downgrade. Registrar
   versoes e motivo sem dados sensiveis.

Atualizacao de seguranca incompativel pode limitar capacidade pelo contrato
aprovado, com mensagem e recuperacao; nunca apagar fila, fabricar sucesso ou
desativar validacoes. Nao impor recarga a cada deploy. Compatibilidade API com
clientes anteriores precisa de janela e estrategia definidas antes de publicar.
Cache antigo so sai quando nao houver clientes ativos dependentes e existir
recuperacao; precache/limpeza nao inclui dados privados por padrao.

## Canais de distribuicao

| Canal | O que implementar e qual e o limite |
|---|---|
| Navegador/PWA | Service worker e assets com versoes/hashes, politica de atualizacao e cache de navegacao compativel. Candidata instala em paralelo e pode ficar em waiting. Coordenar abas, salvar estado e ativar/recarregar uma vez em ponto seguro; nao usar skipWaiting/clients.claim incondicionais com formulario ativo. Sem SW, nova navegacao consulta versao; aba aberta nao recebe codigo novo magicamente. |
| APK com Capacitor | Assets web sao os embarcados no binario. Deploy do site sozinho nao os atualiza. Escolher nova release APK/loja ou OTA de assets explicitamente adotado, assinado e compativel com bridge/API/schema e regras do canal. Plugins/permissoes/codigo Kotlin/Java exigem novo binario. |
| Google Play | Auto-update da loja e fluxos oficiais de in-app update conforme disponibilidade. Download flexivel pode ocorrer enquanto usa; consentimento/reinicio seguem API e estado. Nao prometer instalacao silenciosa/instantanea sob controle absoluto do app. |
| APK direto | Checar manifesto/versao e baixar de origem confiavel; conferir identidade/assinatura e encaminhar ao instalador do Android. Pode exigir autorizacao para essa origem e confirmacao do usuario. Manter funcionalidade segura enquanto aguarda. |
| Dispositivo corporativo gerenciado | Instalacao administrada somente com provisionamento, politica e capacidade MDM/Device Owner comprovados. Aparelho pessoal nao recebe esse privilegio por existir uma skill. |

Android normalmente impede instalar versionCode inferior; rollback silencioso
do APK nao e capacidade garantida de app comum. Rollback de assets em dois
slots e recuperacao de binario sao contratos distintos. Em PWA, ativacao de
service worker tambem exige estrategia de recuperacao ensaiada; guardar cache
antigo por si nao restaura automaticamente o worker ou um schema alterado.

Para service worker, definir escopo e navegacoes servidas offline, estrategia por
tipo de recurso, fallback e invalidacao. Nunca cachear resposta privada de um
usuario para outro, CSRF/token ou endpoint mutavel como se fosse asset publico.
Ler dados dinamicos do repositorio; bundle nao incorpora snapshots privados.

## Fontes tecnicas

- [Ciclo de vida de service worker](https://web.dev/articles/service-worker-lifecycle).
- [Limites e remocao de armazenamento](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria).
- [Background Synchronization API e compatibilidade](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API).
- [Armazenamento no Capacitor](https://capacitorjs.com/docs/guides/storage).
- [Android: trabalho persistente](https://developer.android.com/develop/background-work/background-tasks/persistent-work).
- [Play: atualizacoes dentro do app](https://developer.android.com/guide/playcore/in-app-updates).
- [Android: assinatura do app](https://developer.android.com/studio/publish/app-signing).
- [Android: versionCode e protecao contra downgrade](https://developer.android.com/studio/publish/versioning).
- [PackageInstaller e acao do usuario](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequireUserAction(int)).
