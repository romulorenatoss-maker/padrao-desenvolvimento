---
name: desempenho-mobile
description: "Use desde a primeira construcao de app web/mobile e ao corrigir lentidao de abertura, toque ou navegacao, preparar PWA/offline/sincronizacao, empacotar APK ou implementar atualizacao automatica. Define caminho critico, contratos locais, receita de construcao, medicao e aceite, preservando a stack e as regras do projeto."
---

# Desempenho Web e Mobile

Construir para abrir e executar a tarefa principal rapidamente desde a primeira
capacidade. Aplicar tambem ao navegador; empacotar em APK nao corrige trabalho
excessivo. TypeScript organiza contratos, mas compila para JavaScript e nao
garante velocidade. Medir o resultado no ambiente alvo.

Esta skill e dona do perfil de execucao do cliente, abertura, resposta, offline,
empacotamento e atualizacao do app. Aplicar `analisar`, `construir`,
`documentacao`, `seguranca` e `verificar` no alcance pertinente. Regras gerais
de dados continuam em [DADOS](../../references/DADOS.md); identidade visual e
aceite continuam em `interface`. Nao criar outra fonte de regras de negocio.

## Leitura por efeito

| Efeito | Ler antes de construir |
|---|---|
| Nova tela/app, abertura ou resposta lenta, organizacao para APK | [Receita de construcao](references/construcao.md), incluindo a tabela de arquivos e a sequencia de abertura. |
| Persistencia local, fila, sincronizacao, sessao offline | [Contrato offline](references/offline-atualizacao.md#persistencia-e-sessao-local). |
| Atualizacao automatica, service worker, nova versao ou APK | [Atualizacao segura](references/offline-atualizacao.md#atualizacao-automatica-desde-a-primeira-versao). |
| Medir, comparar, aprovar velocidade ou diagnosticar regressao | [Medicao e aceite](references/medicao-aceite.md). |

## Procedimento obrigatorio

1. **Reconhecer o atual.** Conferir entrada/rota real, stack, build, API, origem
   dos dados, carregamento, plugins, armazenamento e atualizador existentes.
   Preservar padrao visual, seguranca, IDs e APIs. Diferenciar fato medido,
   achado no codigo e hipotese. Nao trocar framework como primeiro tratamento
   de lentidao.
2. **Fixar o perfil no dono.** Completar [PADRAO_TECNICO](../../templates/PADRAO_TECNICO.md#execucao-web-mobile-e-desempenho)
   no TRD equivalente: plataforma, dispositivos, volume, operacoes offline,
   validade da sessao, prioridades, orcamentos, canais de atualizacao e comandos.
   Usar decisoes ja dadas; perguntar somente o que bloquear a parte dependente.
3. **Definir a primeira tarefa utilizavel.** Nomear a acao que prova prontidao,
   os dados/recursos indispensaveis e os marcos de tempo. Splash, skeleton,
   spinner, HTML recebido ou WebView carregada nao significam tarefa pronta.
4. **Construir a abertura limitada.** Shell/assets locais quando aplicavel,
   autorizacao local valida e primeira projecao/pagina. Adiar sincronizacao,
   atualizacao regular, historico, mapa, outras abas e contadores. Nao ler,
   verificar, serializar ou montar toda a base para recortar depois.
5. **Construir a resposta e a gravacao.** Atualizar somente o estado afetado.
   Operacao permitida offline confirma armazenamento local somente depois de
   transacao duravel de alteracao + outbox; mostrar pendencia de envio.
   Efeito oficial exige confirmacao do servidor. Operacao exclusivamente online
   nao e simulada como concluida.
6. **Construir a sincronizacao e a recuperacao.** Lotes pequenos, cursor,
   idempotencia, dependencias, exclusoes, conflitos, isolamento e retomada apos
   encerramento. Sincronizar nao pode disputar toda a CPU/banco com a interacao.
7. **Construir a atualizacao.** Verificar/baixar em segundo plano e ativar em
   ponto seguro; preservar rascunhos, fila, schema e versao funcional anterior.
   Testar rede ausente, download parcial e falha de ativacao. Recurso planejado
   sem implementacao fica PENDENTE, nunca ATUALIZACAO_AUTOMATICA_ATIVA.
8. **Preparar e provar o destino.** Quando APK estiver no alcance, usar assets
   embarcados e pipeline real de build/assinatura. Distinguir web, PWA, APK
   hibrido e Android nativo. PHP no servidor nao vira Kotlin nem executa no APK.
9. **Medir e corrigir.** Capturar baseline e candidato com dados representativos,
   rede lenta/offline e build de producao. Corrigir o maior custo demonstrado,
   retestar o afetado e entregar quando os criterios forem satisfeitos.

## Perfis de tecnologia

| Situacao | Diretriz de construcao |
|---|---|
| PHP/JavaScript existente | Manter backend e regras oficiais. Modularizar carregamento e contratos; criar entrada estatica empacotavel/API somente no alcance da migracao autorizada. Nao presumir que a pagina PHP ja e um app offline. |
| Novo frontend web com destino APK, sem convencao equivalente | Perfil de referencia: TypeScript estrito, modulos ES e build de producao (Vite quando escolhido). Usar UI existente; sem framework, componentes DOM pequenos sao validos. React so se adotado/justificado. Fixar versoes compativeis e lockfile, sem instalar a lista por rotina. |
| Mesmo frontend no navegador e Android | PWA quando pertinente e Capacitor com assets locais para o APK, por adaptadores. Esse perfil usa WebView; documentar e medir essa escolha. Nao inserir outra camada Flutter apenas para exibir o mesmo site. |
| App Flutter ou nativo ja existente | Aplicar os mesmos contratos no runtime atual. Nao reescrever automaticamente nem empilhar runtimes; medir banco, ponte, renderizacao e lifecycle existentes. |
| Android nativo necessario/decidido | Kotlin/Compose em perfil proprio; reutilizar API, contratos, regras e design, com interface reimplementada. Exigir evidencia da necessidade/decisao; nao prometer conversao automatica de React/HTML para Kotlin. |

## Documentos e arquivos desde a primeira capacidade

Preencher o dono existente, sem arvore antecipada nem manual paralelo:

| Dono local | Conteudo obrigatorio no recorte |
|---|---|
| TRD/padrao tecnico | Perfil de plataforma, pastas, linguagem, adaptadores, abertura, budgets, dados/limites locais e atualizador. |
| Documento da tela | Acao que prova prontidao; essencial/adiado/sob demanda; estados local/pendente/confirmado/erro; metricas e consumidores. |
| Contrato da operacao/API | Identidade, permissao, payload, idempotencia, versoes, conflitos, cursor e fonte oficial. |
| Guia de reconstrucao/processo de entrega | Comandos, toolchain, build, assinatura por referencias seguras, canal de update, compatibilidade, ativacao e rollback. |
| Evidencias do lote/CI | SHA e artefato, aparelho, volume, rede/cache, traces e amostras; resultados antes/depois e o que nao foi executado. |

Na primeira versao funcional do app mobile autorizado, abertura local,
sincronizacao, recuperacao e atualizacao precisam existir no recorte combinado.
Nao adiar esses contratos para depois de construir todas as telas. Primeiro
login/provisionamento pode exigir rede; documentar o estado sem dados locais.
App apenas responsivo ou com botao "instalar" nao cumpre esse contrato.

## Conferencia e estados de entrega

O fiscal confronta diff, comportamento e evidencia, usando a [matriz de aceite](references/medicao-aceite.md#cenarios-de-aceite).
Nao aprovar por numero de arquivos, troca de linguagem, print, score isolado,
build concluido ou frase "offline first".

Separar: CODIGO_CONSTRUIDO, BUILD_GERADO, OFFLINE_VERIFICADO,
DESEMPENHO_MEDIDO, ATUALIZACAO_VERIFICADA e PUBLICADO. Cada item recebe
PASSOU/FALHOU/NAO_EXECUTADO/NAO_SE_APLICA justificado e revisao/alcance.
Ausencia de aparelho nao impede escrever/testar partes independentes, mas impede
afirmar desempenho mobile verificado. Falha corrigivel volta a construcao.

O [avaliador de evidencias](scripts/verificar_desempenho.py) compara amostras,
condicoes, hashes e orcamentos aprovados; nao captura traces nem prova sozinho
que uma medicao aconteceu. O [perfil de exemplo](assets/perfil-desempenho.exemplo.json)
e PROPOSTO e deve ser recusado pelo avaliador ate ser adaptado/aprovado no projeto.
Nao editar limites para fazer um resultado lento passar.

Publicar esta skill nao acelera apps existentes, nao gera APK, nao instala
atualizador e nao comprova ativacao em outra sessao. Adocao em cada consumidor
exige implementacao e medicao pertinentes, preservando protecoes locais.
