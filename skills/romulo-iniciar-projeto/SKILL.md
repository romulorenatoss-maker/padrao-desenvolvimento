---
name: romulo-iniciar-projeto
description: "Use em projeto novo ou na implantacao/migracao do bootstrap: AGENTS.md minimo ligado ao sumario central, CLAUDE.md apontando para AGENTS e apenas a estrutura necessaria, preservando contratos locais existentes."
---

# Romulo Iniciar Projeto

Fonte dona de criacao de AGENTS.md/CLAUDE.md e bootstrap do projeto. Padrao global/roteamento mora no [README central](../../README.md); instalacao/recarga em [INSTALL.md](../../INSTALL.md). Nao copiar catalogo de skills para cada projeto.

## Antes de qualquer criacao
Com `romulo-analisar`, identificar projeto/remote/branch/worktree/ambiente/stack, permissao de bootstrap e convencoes/arquivos existentes. Aplicar seu gate de criacao. Confirmar padrao e Ponytail realmente disponiveis antes de construcao de produto; a leitura das fontes de instalacao e verificacao permite resolver o bootstrap, nao fingir plugin ativo.

## AGENTS.md minimo
Usar [templates/AGENTS.md](../../templates/AGENTS.md), nunca o AGENTS.md da raiz central. Se ausente e bootstrap autorizado, preencher identidade, repositorio, branch, ambiente, referencia publica do banco quando houver, deploy, sumario local, protecoes e ponte repositorio/ref/README. Nao gravar placeholders nem exemplos como fatos; omitir metadado opcional nao aplicavel. Dados obrigatorios nao descobertos impedem a escrita do contrato; perguntar so o que a investigacao nao resolve.

Nao colocar lista, contagem, comandos de instalacao ou regras globais no AGENTS local. O sumario central determina as skills necessarias a cada execucao. Protecao local curta fica explicita; detalhes de negocio/guardas/peculiaridades ficam em donos locais obrigatoriamente referenciados, nunca no padrao global.

## CLAUDE.md ponte
Quando Claude Code fizer parte do ambiente, procurar CLAUDE.md e equivalentes de escopo ja utilizados antes de criar. Ausente e bootstrap autorizado: criar na raiz o nome EXATO `CLAUDE.md` com o conteudo de [templates/CLAUDE.md](../../templates/CLAUDE.md): `@AGENTS.md` e quebra de linha. Nao criar `claud.md`, nao copiar AGENTS nem acumular regras duplicadas. Mesmo em versao que leia AGENTS nativamente, esta ponte explicita e o modelo portatil adotado quando CLAUDE e requerido no projeto.

Se ja houver ponte correta, nao alterar. Se houver CLAUDE com regras proprias ou importacao equivalente, comparar, preservar e integrar somente com autorizacao aplicavel. Nao criar ponte concorrente sem necessidade. Evitar ciclos: CLAUDE -> AGENTS -> entrada central; AGENTS nao importa CLAUDE de volta. Confirmar leitura na sessao com mecanismo suportado; arquivo escrito nao significa automaticamente carregado.

## Migracao de contrato existente
Ler o contrato inteiro e as regras mais especificas. Apresentar o diff de migracao, mantendo identidade, guardas, IDs e peculiaridades. Aplicar [migracao documental](../../references/DOCUMENTACAO.md) com `romulo-documentacao`: mapear origem/destino, validar links e so entao remover narrativa redundante. Enquanto faltar destino ou autorizacao, manter o trecho original.

AGENTS protegido por 0393 nao e substituido nem reduzido sem 0393 explicito para ESSA migracao. Citacao do codigo na instrucao nao e aprovacao. Nao usar curl/copia/checkout para sobrescrever arquivo protegido. Nao apagar alteracoes locais nem usar reset, clean, amend ou force para facilitar. Se autorizada apenas leitura/instalacao, parar antes da mudanca do contrato/produto.

## Primeira capacidade e estrutura ausente
Projeto novo: identificar primeira capacidade, aplicar `romulo-especificar` para perguntas/proposta/aprovacao e `romulo-interface` para referencia visual quando houver UI. Construir com `romulo-construir`, usando [arquitetura e nomes](../../references/ARQUITETURA.md). Criar somente arquivos/pastas com uso imediato. Projeto existente desorganizado segue `romulo-auditar-projeto`, nao bootstrap destrutivo.

Antes da primeira interface definitiva, registrar as decisoes aprovadas do briefing visual, fluxo do app e TRD nos [donos existentes ou fallbacks](../../references/DOCUMENTACAO.md#contratos-de-projeto-e-reconstrucao), ligados ao sumario local. Prototipo pode ajudar a decidir; nao preencher com valores inventados nem impor tres arquivos quando fontes equivalentes ja resolvem. Documentar somente o necessario ao recorte e completar conforme as decisoes; lacuna que impede construcao permanece explicita. Bootstrap nao obriga reentrevista nem migracao visual de projeto existente.

Pasta, modulo, migration, componente e documento nao nascem para uso futuro. Nao impor stack nem abrir camadas vazias. Testes e documentacao sao proporcionais ao efeito; segredos apenas em ambiente seguro. Verificar contratos locais, descoberta das skills pelo catalogo central, ponte, links e primeira capacidade com `romulo-verificar`. Bootstrap nao autoriza banco, concessao de permissao, commit/push ou deploy automaticamente.
