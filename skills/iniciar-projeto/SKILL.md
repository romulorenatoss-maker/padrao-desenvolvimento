---
name: iniciar-projeto
description: "Use na primeira adocao/instalacao autorizada do padrao, projeto novo ou migracao de bootstrap: setup guiado, diagnostico autorizado por modulo e AGENTS/CLAUDE ligados ao sumario, preservando contratos existentes."
---

# Iniciar Projeto

Fonte dona de criacao de AGENTS.md/CLAUDE.md e bootstrap do projeto. Padrao global/roteamento mora no [README central](../../README.md); instalacao/recarga em [INSTALL.md](../../INSTALL.md). Nao copiar catalogo de skills para cada projeto.

## Setup na primeira adocao

AGENTS ausente ou realmente vazio inicia a adocao como PENDENTE; preencher/criar o contrato pelo template apos resolver identidade e autorizacao, sem apagar codigo, banco, dados ou regras encontradas em outros donos. Pedido de recomecar o setup reabre a analise, nao zera o sistema. AGENTS com conteudo exige a migracao preservadora abaixo; nao apagar o arquivo para contornar protecao ou simular projeto novo.

Resolver identidade/fonte e ler o AGENTS atual antes de diagnostico amplo ou escrita. Conferir SETUP_PADRAO e sua referencia, se existentes. Ausente/PENDENTE: perguntar uma vez "Deseja usar o Padrao de Desenvolvimento para analisar o que esta fora do padrao e seus impactos?". Sim autoriza o diagnostico, nao correcao, mudanca de stack, publicacao ou recurso pago. Nao/adiamento permite seguir o pedido pontual com as verificacoes pertinentes; silencio deixa a decisao pendente. Registro previo evita repetir a pergunta; nova migracao relevante ou reabertura pedida tem escopo proprio. Nao diagnosticar o repositorio inteiro antes desse aceite.

Com aceite, investigar o sistema antes das perguntas: origem/link do repositorio, clone/caminho oficial, contratos/documentacao, linguagens e runtime realmente usados. Separar produto de ferramentas de teste/automacao e legado; arquivo ou dependencia antiga nao e autorizacao para reativar tecnologia. Mostrar as linguagens encontradas e as permitidas pelo contrato, depois perguntar "Mantemos as linguagens definidas neste projeto ou voce deseja avaliar alguma adicional?" somente se essa decisao ainda nao foi dada. Excecao exige justificativa/impacto e aprovacao exigidos localmente; nao introduzir framework/build nem remover linguagem usada por impulso.

Reutilizar clone oficial existente. Em primeiro clone, perguntar somente link/nome/local ainda ausentes e confirmar a proposta de caminho antes de criar; no Windows, sugerir `C:\projetos\<nome-confirmado>`, sem assumir pasta/marca ou mover outro checkout. Para outros sistemas, usar raiz autorizada adequada ao host. Verificar destino, remote/ref e arquivos existentes; nao sobrepor trabalho, duplicar o sistema, acessar segredo nem pedir senha no chat. Autorizacao de clone nao autoriza refazer produto/arquitetura.

Diagnostico usa auditar-projeto e as fontes locais: relatar por modulo o desvio comprovado ou lacuna, evidencia/local, por que o requisito existe, onde corrigir e impacto/risco. Preservar excecao/decisao aprovada e peculiaridade valida; sem acesso marcar NAO_VERIFICADO, sem prometer descobrir todos os erros. Incluir a verificacao curta de backup ja encaminhada abaixo. Registrar no dono/fila existentes; nao criar dossie ou camada/pasta so para preencher o padrao.

Depois do diagnostico, perguntar se deseja corrigir por modulo, apresentando o primeiro lote concreto (arquivos, impacto, preservacao e aceite). Aprovado o alcance, seguir analisar/especificar/construir/documentacao/verificar ate entregar e conferir aquele lote, com guarda e fiscal pertinentes; perguntar novamente apenas por decisao ausente ou efeito fora da autorizacao. Nao usar piloto automatico para apagar dados, redesenhar UI aprovada, conceder acesso ou publicar silenciosamente. Modulos restantes seguem a fila/autoridade combinadas, sem executores concorrentes duplicados.

Antes de criar/alterar a flag no AGENTS, mostrar o valor factual e perguntar "Posso registrar este estado do setup no AGENTS.md?", cumprindo a protecao local, inclusive 0393 quando exigido. Formato curto: SETUP_PADRAO: <estado>; registro=<dono/ancora existente>. Estados: PENDENTE (sem decisao), PERGUNTADO (questao apresentada; aguarda resposta), AUTORIZADO (diagnostico aceito), ANALISADO (diagnostico concluido com evidencias/pendencias registradas), ADIADO (recusado/adiado pelo dono). Marcar apenas o fato ocorrido; ANALISADO nao certifica sistema corrigido/seguro ou todos os modulos fechados. Guardar detalhes/alcance no dono e nao copiar questionario, catalogo ou certificado paralelo no AGENTS. Ao corrigir depois, atualizar a evidencia no mesmo dono e perguntar sobre a flag somente se seu estado/resumo realmente mudar.

## Antes de qualquer criacao
Com `analisar`, identificar projeto/remote/branch/worktree/ambiente/stack, permissao de bootstrap e convencoes/arquivos existentes. Aplicar seu gate de criacao. Confirmar padrao e Ponytail realmente disponiveis antes de construcao de produto; a leitura das fontes de instalacao e verificacao permite resolver o bootstrap, nao fingir plugin ativo.

Incluir a [verificacao curta de backup](../backup-recuperacao/SKILL.md#verificacao-curta-na-entrada) no setup: identificar quem captura, de qual origem, para qual destino independente e qual rotina recorrente realmente funciona. Reutilizar o perfil local; ausencia/inatividade fica pendente e exige orientacao de setup. Nao criar pastas, replicas ou recursos pagos apenas por instalar a skill; projeto sem dados ainda exige captura antes da operacao real.

## AGENTS.md minimo
Usar [templates/AGENTS.md](../../templates/AGENTS.md), nunca o AGENTS.md da raiz central. Se ausente e bootstrap autorizado, preencher identidade, repositorio, branch, ambiente, referencia publica do banco quando houver, deploy, sumario local, protecoes e ponte repositorio/ref/README. Nao gravar placeholders nem exemplos como fatos; omitir metadado opcional nao aplicavel. Dados obrigatorios nao descobertos impedem a escrita do contrato; perguntar so o que a investigacao nao resolve.

Nao colocar lista, contagem, comandos de instalacao ou regras globais no AGENTS local. O sumario central determina as skills necessarias a cada execucao. Protecao local curta fica explicita; detalhes de negocio/guardas/peculiaridades ficam em donos locais obrigatoriamente referenciados, nunca no padrao global.

## CLAUDE.md ponte
Quando Claude Code fizer parte do ambiente, procurar CLAUDE.md e equivalentes de escopo ja utilizados antes de criar. Ausente e bootstrap autorizado: criar na raiz o nome EXATO `CLAUDE.md` com o conteudo de [templates/CLAUDE.md](../../templates/CLAUDE.md): `@AGENTS.md` e quebra de linha. Nao criar `claud.md`, nao copiar AGENTS nem acumular regras duplicadas. Mesmo em versao que leia AGENTS nativamente, esta ponte explicita e o modelo portatil adotado quando CLAUDE e requerido no projeto.

Se ja houver ponte correta, nao alterar. Se houver CLAUDE com regras proprias ou importacao equivalente, comparar, preservar e integrar somente com autorizacao aplicavel. Nao criar ponte concorrente sem necessidade. Evitar ciclos: CLAUDE -> AGENTS -> entrada central; AGENTS nao importa CLAUDE de volta. Confirmar leitura na sessao com mecanismo suportado; arquivo escrito nao significa automaticamente carregado.

## Migracao de contrato existente
Ler o contrato inteiro e as regras mais especificas. Apresentar o diff de migracao, mantendo identidade, guardas, IDs e peculiaridades. Aplicar [migracao documental](../../references/DOCUMENTACAO.md) com `documentacao`: mapear origem/destino, validar links e so entao remover narrativa redundante. Enquanto faltar destino ou autorizacao, manter o trecho original.

AGENTS protegido por 0393 nao e substituido nem reduzido sem 0393 explicito para ESSA migracao. Citacao do codigo na instrucao nao e aprovacao. Nao usar curl/copia/checkout para sobrescrever arquivo protegido. Nao apagar alteracoes locais nem usar reset, clean, amend ou force para facilitar. Se autorizada apenas leitura/instalacao, parar antes da mudanca do contrato/produto.

## Primeira capacidade e estrutura ausente
Projeto novo: identificar primeira capacidade, aplicar `especificar` para perguntas/proposta/aprovacao e `interface` para referencia visual quando houver UI. Construir com `construir`, usando [arquitetura e nomes](../../references/ARQUITETURA.md). Criar somente arquivos/pastas com uso imediato. Projeto existente desorganizado segue `auditar-projeto`, nao bootstrap destrutivo.

Antes da primeira interface definitiva, registrar as decisoes aprovadas do briefing visual, fluxo do app e TRD nos [donos existentes ou fallbacks](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao), ligados ao sumario local. Prototipo pode ajudar a decidir; nao preencher com valores inventados nem impor tres arquivos quando fontes equivalentes ja resolvem. Documentar somente o necessario ao recorte e completar conforme as decisoes; lacuna que impede construcao permanece explicita. Bootstrap nao obriga reentrevista nem migracao visual de projeto existente.

Pasta, modulo, migration, componente e documento nao nascem para uso futuro. Nao impor stack nem abrir camadas vazias. Testes e documentacao sao proporcionais ao efeito; segredos apenas em ambiente seguro. Verificar contratos locais, descoberta das skills pelo catalogo central, ponte, links e primeira capacidade com `verificar`. Bootstrap nao autoriza banco, concessao de permissao, commit/push ou deploy automaticamente.
