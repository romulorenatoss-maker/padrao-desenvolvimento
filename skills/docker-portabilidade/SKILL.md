---
name: docker-portabilidade
description: "Preparar e verificar um pacote Docker reproduzível de um sistema existente, incluindo web, agendador, dependências e procedimentos de dados, para instalação, reconstrução ou migração entre servidores, Supabase e PostgreSQL. Classificar compatibilidade antes de prometer troca somente por configuração."
---

# Docker e portabilidade do sistema

Transformar um projeto existente em um pacote de instalação reproduzível. Depois de preparar e ensaiar cada destino, permitir ao usuário informar o caminho do pacote e o destino para instalar, restaurar e verificar sem reconstrução manual do software. Empacotar o comportamento existente, não recriar o produto nem escolher outro banco por iniciativa própria.

## Entrada e alcance

Ler AGENTS/CLAUDE aplicáveis, estado/sumário e deployment/reconstrução do projeto. Confirmar raiz, revisão, ambientes e permissões reais. Reusar Dockerfile, configuração, exportador/restaurador e testes existentes; preservar trabalho não commitado e identificar a revisão exata realmente empacotada. Não alterar AGENTS ou o padrão central para instalar esta skill.

Se disponíveis, usar as skills locais de análise, segurança e backup/recuperação para o método do projeto. Esta skill cuida do pacote e da compatibilidade, não substitui esses contratos. Sem elas, seguir os contratos locais e as referências deste pacote; declarar a ausência, sem alegar leitura ou ativação. Consultar documentação oficial atual dos componentes e ajuda das ferramentas antes de gerar comandos dependentes de versão.

Reconhecer a operação solicitada: analisar, preparar pacote, ensaiar instalação, capturar dados, migrar ou liberar. Criar a skill ou preparar software não autoriza captura de dados, acesso a segredos, recursos pagos, restore, alteração de DNS, publicação, parada da origem ou exclusão. Reusar autorização humana já dada no alcance correspondente; perguntar somente alvo, escolha ou autorização que realmente faltar. Não repetir confirmações por etapa já autorizada.

Pedidos típicos: “prepare a caixa Docker deste projeto”; “instale o pacote deste caminho no Supabase”; “mude para um servidor com PostgreSQL”; “reconstrua em uma máquina limpa”. Docker empacota/executa processos em um servidor; não é um banco nem uma hospedagem por si. O domínio público aponta para a entrada web no host. PostgreSQL fornece banco; Supabase reúne banco e serviços, podendo ser externo ou instalado no host. Uma VPS/servidor próprio compatível pode executar o pacote sem Render/Vercel. Não afirmar que um serviço PostgreSQL ou projeto Supabase hospedado recebe o container web do produto. Não confundir caminho local do pacote, host do aplicativo e destino dos dados. “Supabase” e “PostgreSQL” identificam serviços de dados, não necessariamente onde o web vai rodar.

## Descobrir antes de empacotar

Levantar o mínimo necessário no código e no runtime acessível, distinguindo observado de não verificado:
- Web/CLI/workers, comandos de entrada, versões, extensões e plataforma CPU/SO.
- Quem dispara cada rotina, onde ficam travas/estado e o que funciona sem navegador aberto. Código de rotina não é relógio autônomo.
- Banco: versão, schemas, migrations, RPCs, roles/grants/RLS, extensões, sequências e consumidores.
- Auth/MFA/sessões, REST/PostgREST, Storage e objetos, Realtime, Edge Functions, filas e serviços externos realmente usados.
- Arquivos persistentes, volumes, integrações/callbacks e referências de chaves necessárias para decifrar dados; nunca seus valores no relatório.

Registrar dependência -> consumidor -> equivalente no destino -> configuração/adaptação necessária -> evidência/limite no dono local de deployment. Não criar dossiê paralelo quando já houver esse destino.

## Escolher o perfil

Partir da stack, do banco e dos serviços realmente usados pelo sistema, conforme o contrato autorizado; empacotá-los sem conversão automática de linguagem, framework ou motor. Sistema sem banco não recebe um só para completar o pacote. Os perfis Supabase/PostgreSQL abaixo são casos específicos, não uma lista fechada de tecnologias aceitas. Ler [destinos e transição](references/destinos-e-transicao.md) somente nas partes pertinentes ao perfil descoberto.

| Perfil | Significado | Quando basta configuração/restauração |
|---|---|---|
| stack-existente | Levar os runtimes, banco e serviços já usados pelo sistema | Versões, drivers, persistência, Auth/arquivos e demais dependências existentes preservados e ensaiados; não exige adotar Supabase/PostgreSQL. |
| supabase-existente | Mover web/agendador, mantendo o projeto Supabase atual | Runtime compatível, acessos e contratos verificados; dados continuam na mesma origem. Não é pacote autossuficiente de banco. |
| supabase-proprio | Levar também os serviços Supabase necessários para infraestrutura própria | Versões/serviços/contratos equivalentes ensaiados; contas, arquivos, funções e configuração operacional cobertos. |
| postgresql | PostgreSQL local ou gerenciado, com demais serviços explicitamente escolhidos | Projeto já usa PostgreSQL diretamente ou adaptadores equivalentes estão implementados e testados. PostgreSQL sozinho não fornece Auth, Storage, PostgREST ou Edge Functions. |

Por perfil, classificar CONFIGURACAO_E_RESTAURACAO, REQUER_ADAPTACAO ou NAO_VERIFICADO, sempre com motivo e evidência. Ausência de acesso é NAO_VERIFICADO. Não apresentar perfil funcional fictício nem usar um seletor de ambiente que ignore dependências. Não retirar módulos, permissões, MFA, RLS ou dados para fazer o destino parecer compatível.

Se exigir adaptação, listar portas afetadas e apresentar o menor plano concreto para aprovação conforme contrato local. Separar código/contratos reaproveitados dos adaptadores a construir. Não refazer telas ou regra de negócio para mudar provedor. A frase “apenas mudar endereço” só vale para o perfil/revisão efetivamente ensaiados.

## Entrega obrigatória: pasta Docker transportável

Quando o pedido for criar o pacote, produzir uma pasta de entrega real, não somente plano, documentação, Dockerfile ou links para um registro. Reusar a pasta docker/ existente; se não houver, propor esse destino conforme a autorização e as regras locais. Dentro do destino autorizado, separar definições de infraestrutura versionáveis dos grandes artefatos de release ignorados pelo Git. Não embutir um clone concorrente do produto.

A pasta de release deve levar arquivos de imagem carregáveis no destino, Compose, exemplo de configuração, manifesto de integridade e operações reais de carregar/instalar/verificar. Incluir as imagens das dependências locais do perfil. No modo pedido de “transferir arquivos e rodar”, não exigir acesso ao Git/registro de imagens, novo build, download de código ou edição manual de tabelas após a transferência. Dependências externas inevitáveis ficam declaradas; credenciais e Docker compatível no host continuam pré-requisitos. Imagem apenas em registro é alternativa somente quando esse modo for escolhido pelo usuário.

Para levar dados também, a mesma pasta pode ser uma entrega PRIVADA contendo software e uma seção de snapshot cifrado, com controles de acesso e chave fora do pacote. Nunca publicar essa entrega completa em Git, registry, ZIP público ou pasta web. O software distribuível deve ser separável dos dados privados. Se não houver autorização/acesso para capturar os dados, entregar a parte de software possível e declarar o pacote completo PENDENTE, sem fingir reconstrução integral.

Só encerrar como pacote transportável verificado depois de copiá-lo para destino limpo e ensaiar carregamento, configuração mínima e instalação/restauração correspondente. Durante o ensaio, não depender dos fontes/volumes do host original. A skill é o procedimento; sua criação não é a geração desse pacote para um projeto.

## Montar e executar

Ler [contrato do pacote](references/contrato-do-pacote.md) antes de criar arquivos. Definir paths/criados/alterados, donos, consumidores, testes e reversão nos registros locais exigidos. Criar somente artefatos necessários ao destino autorizado; não gerar três implementações vazias.

Preparar imagens com versões/digests e contexto de build revisado, Compose com web e agendador como processos/serviços separados quando existentes ou necessários ao alcance, e as dependências necessárias. Uma imagem de aplicação pode atender aos dois comandos. Preferir o despachante e os workers existentes; se falta um relógio contínuo, projetar um executor que realmente invoque a rotina, sem loop improvisado em requisição web. Instalar Docker/Compose somente no host autorizado. Não colocar toda a plataforma dentro de uma única imagem monolítica.

Exigir para o agendador: isolamento de falhas, limites de lote/tempo, encerramento com SIGTERM, retomada, fuso e persistência apropriados, lease/trava e idempotência por operação. Restart do container não assegura esses controles. Trava em arquivo local não basta para duas instâncias. Host que dorme/desliga não cumpre calendário; escolher hospedagem sempre ativa ou declarar o impedimento antes de ativar. Não substituir cron externo por chamadas que dependem de uma tela aberta.

Separar software distribuível, dados privados e segredos. Imagens não carregam volume/banco remoto automaticamente. Gerar operação de captura/restauração somente quando autorizada e compatível, com falha explícita e estado retomável; nunca capturar na etapa docker build nem embutir dump/credencial na imagem. Não iniciar o app normalmente antes de concluir restauração e verificações.

Ao receber caminho + destino de perfil já homologado, conferir pacote, integridade, compatibilidade, identidade e configuração mínima; executar somente as operações autorizadas, sem refazer entrevista/arquitetura. Não executar scripts/SQL de pacote desconhecido sem conferir origem/conteúdo. Falha mantém destino isolado e origem preservada; não improvisar conversão de schema.

## Verificar e entregar

Ensaiar em destino limpo e isolado, sem envios/pagamentos/webhooks de negócio e sem apontar workers à produção. Validar Compose sem imprimir interpolação de segredos, construir/carregar imagens e verificar saúde. Uma configuração válida ou container rodando não prova aplicação pronta.

Provar os fluxos realmente usados: login/permissões/escopo, leitura/gravação, arquivos privados, RPCs, funções e integrações simuladas/seguras. Verificar rotina por relógio sem usuário conectado, retomada após queda e concorrência sem duplicação. Para dados, verificar integridade, IDs/vínculos, constraints, sequências e permissões além de contagens. Incluir reconstrução em host limpo; dois containers no mesmo host não provam suporte a outra arquitetura CPU.

Executar carga proporcional ao uso previsto. “1.000 usuários cadastrados” não define simultaneidade/RPS nem garante capacidade. Definir cenário/pico, medir latência/erros/recursos/atraso de fila e informar ambiente, duração e limites sem inventar resultados.

Entregar caminho do pacote, perfis e revisões, instrução curta de configuração e comandos reais de instalação/restauração/parada, resultado dos ensaios, pendências e retorno. Reportar separadamente SOFTWARE_PREPARADO, INSTALACAO_TESTADA, RESTAURACAO_TESTADA e DESTINO_LIBERADO, por perfil, com evidência; não escrever um certificado universal. Git/push/registro/ativação desta skill não são deploy ou migração.

A criação desta skill não instala infraestrutura nem migra o sistema. Em caso de dependência faltante, concluir o software independente possível e indicar exatamente o que impede a instalação completa.
