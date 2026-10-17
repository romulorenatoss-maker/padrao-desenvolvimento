# Destinos e transição de dados

## Preservar a stack e o banco existentes

O perfil padrão deriva do sistema investigado: runtimes/linguagens, versões, banco ou ausência dele, Auth, arquivos e serviços realmente usados. Se já usa outro motor ou plataforma, empacotar e testar essa composição existente, sem converter ao PostgreSQL nem introduzir APIs Supabase. Confirmar drivers, formatos, permissões, captura/restauração e persistência por mecanismos compatíveis com a origem e o destino. Mudança de tecnologia exige plano e autorização próprios; um exemplo deste documento não a autoriza. As seções seguintes se aplicam apenas quando suas dependências estiverem presentes ou a migração correspondente tiver sido solicitada.

## Mesmo Supabase, novo host do aplicativo

Conservar projeto e dados; mover web/agendador e configurar URL pública, rede, callbacks e credenciais backend no destino. Dois hosts apontando para o mesmo Supabase não são banco isolado. Ensaios com escrita precisam de clone isolado ou dados de teste explicitamente autorizados. Somente um executor de negócio ativo após a virada, com proteção de concorrência também no banco. Não chamar esse perfil de cópia autossuficiente ou backup do Supabase.

## Supabase próprio em Docker

Usar distribuição oficial fixada em revisão, com imagens/digests e requisitos atuais verificados. Incluir apenas os serviços necessários e suas dependências, sem remover algo ainda chamado. Confrontar PostgreSQL, Auth, Storage, PostgREST, extensões e Edge Runtime; mesma marca do serviço não prova mesma versão/ABI.

Exportar/restaurar por mecanismo suportado e compatível, cobrindo os schemas reais e roles/owners/grants/RLS/funções/triggers/sequências necessários; conferir especialmente schemas customizados e gerenciados. Não assumir que retrato documental de schema ou sequência histórica de migrations é dump completo/restauração pronta. Não omitir objetos que falham nem desligar controles para importar “com sucesso”. Se o procedimento específico exigir suspender triggers durante importação, limitar ao restore isolado e comprovar estado restaurado antes de liberar; não tornar isso um bypass permanente.

Transferir separadamente bytes dos objetos, metadados, buckets e políticas, conservando IDs/caminhos e permissões. Copiar tabela storage.objects não copia os arquivos. Funções Edge, configuração de Auth/OAuth/SMTP, callbacks, certificados/DNS e integrações precisam ser reproduzidos separadamente quando usados. Preservar identidades e credenciais de senha por mecanismo de Auth suportado; nunca exportar senha em texto puro ou criar usuários substitutos silenciosamente. Mudança de chaves JWT pode exigir novo login. Material que decifra dados existentes precisa continuar disponível com segurança; não girar chaves indiscriminadamente. Chave ausente/trocada exige recuperar a referência correta e provar decifragem dirigida de conteúdo existente sem imprimir o claro; não resetar, recifrar ou descartar registros para fazer o teste passar.

## PostgreSQL puro ou gerenciado

Inventariar no código chamadas de API/RPC, Auth, schemas auth/storage, auth.uid/JWT, serviço de arquivos, funções Edge e Realtime realmente usados. Mapear cada contrato necessário para implementação equivalente real. PostgreSQL com os mesmos registros não substitui essas APIs. Mover um sistema que já usa MySQL/SQLite ou outro motor sem trocá-lo segue o perfil stack-existente; converter esses dados/contratos para PostgreSQL é uma migração adicional, não simples configuração.

Se houver dependência Supabase sem equivalente existente, marcar REQUER_ADAPTACAO; não gerar perfil funcional fictício. Reusar camada repository/serviço/contratos, sem inventar um framework universal de provedores. Adaptar somente portas necessárias depois da aprovação aplicável, preservar IDs/relacionamentos, política de sessão, autorização e escopo; testar êxitos e recusas. Configuração básica só basta depois de esses adaptadores estarem implementados e homologados para a revisão.

Para versão/extensão incompatível, não instalar versão arbitrária, fazer downgrade nem editar dados para esconder erro. Escolher destino compatível ou apresentar conversão específica. Confirmar também acesso de restore e limites do provedor gerenciado; não supor privilégios de superusuário.

## Captura, corte e retorno

1. Identificar fontes/destinos reais, mecanismos de preservação e alcance autorizado. Registrar RPO/RTO como metas e medir no ensaio; não prometer migração em minutos sem volume/velocidade conhecidos.
2. Preparar destino isolado, com negócio/envios parados. Verificar destinos reais de conectores, callbacks e tarefas restauradas, incluindo relógios no banco; bloquear efeitos externos antes do restore e do primeiro start, sem depender apenas de pausar workers web. Validar restauração prévia e cobertura dos dados/objetos antes do corte final.
3. No corte autorizado, parar novos escritores na origem, incluindo API, apps móveis/offline, workers, webhooks e outros executores; drenar operações em curso. Definir retenção/retry de eventos recebidos, sem responder sucesso e descartá-los. Para arquivos, coordenar um corte consistente com os registros que os referenciam.
4. Capturar e verificar snapshot final. Origem indisponível usa ponto recuperável conhecido, com perda potencial explicitada. Não inventar sincronização final.
5. Restaurar em destino limpo e privado, com fases/erros verificáveis. Conferir conteúdo, IDs/vínculos, constraints, sequências, owners/grants/RLS e leitura/gravação dos arquivos, além de contagens/hashes. Não liberar conjunto parcialmente restaurado como completo.
6. Testar fluxos/autorização e rotinas sem efeitos externos reais; preparar callbacks/DNS. Impedir escrita pela origem antiga, trocar endereços autorizados e só então liberar negócio/agendador no destino. Não depender apenas de TTL/DNS para impedir cliente antigo de escrever.
7. Verificar primeira execução real do agendador sem duplicar rodadas, monitorar e retomar backup independente da nova origem, quando previsto/autorizado. Preservar origem e ponto confiável até decisão de retirada.

Antes de novas escritas no destino, retorno pode reabrir a origem preservada com configuração coerente. Depois de novas escritas, exigir conciliação/reversão de dados antes de voltar; restaurar só DNS pode perder dados. Não apagar a origem/volume anterior como etapa automática de sucesso.

## Fontes para conferir na execução

Consultar versões e comandos reais na documentação oficial vigente, sem tratar valores de exemplos como atuais:
- [Docker Compose em produção](https://docs.docker.com/compose/how-tos/production/)
- [Imagens para várias plataformas](https://docs.docker.com/build/building/multi-platform/)
- [Supabase próprio em Docker](https://supabase.com/docs/guides/self-hosting/docker)
- [Restaurar Supabase hospedado em instalação própria](https://supabase.com/docs/guides/self-hosting/restore-from-platform)
- [Changelog Supabase](https://supabase.com/changelog)
- [Dump e restauração PostgreSQL](https://www.postgresql.org/docs/current/backup-dump.html)

Falha ao obter uma fonte não prova inexistência de recurso. Registrar a limitação e consultar outro canal oficial; não afirmar compatibilidade não conferida.
