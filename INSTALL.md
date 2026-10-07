# Instalacao e atualizacao

Fonte central: `romulorenatoss-maker/romulo-dev-standard`. A conta usada pelo cliente precisa ter leitura nesse repositorio privado. Versao desta distribuicao: 1.4.0. Fonte dos comandos: documentacao oficial ao final; confira `--help` da versao instalada se um comando nao for reconhecido.

## Antes de instalar
Identificar superficie (terminal, IDE, desktop ou cloud), versao do cliente, marketplace cadastrado, escopo instalado e permissoes. Nao assumir que plugin instalado no computador aparece numa sessao cloud. Preservar configuracoes, trabalho pendente e autorizacoes do projeto. Nao duplicar instalacao manual e via plugin.

## Codex
No terminal com Codex CLI que disponibilize estes comandos; um por vez:
```sh
codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main
codex plugin add romulo-dev-standard@romulo-dev-standard
codex plugin list
```
Ja instalado: atualizar o catalogo e a instalacao, sem recriar outro plugin:
```sh
codex plugin marketplace upgrade romulo-dev-standard
codex plugin add romulo-dev-standard@romulo-dev-standard
codex plugin list
```
Se a superficie/versao nao oferecer `plugin add`, use seu gerenciador de plugins para atualizar a instalacao a partir desse marketplace; nao inventar comando substituto nem editar cache interno. `marketplace upgrade` sozinho nao prova a versao ativa na conversa.

Depois, confirmar versao e descoberta nominal na sessao. Nao prometer hot reload universal no Codex: quando a sessao nao redescobrir, iniciar nova thread/sessao mantendo o contexto necessario na documentacao canonica. Nao usar geracao automatica/delegacao de codigo como parte desta instalacao.

Ponytail, somente se ainda ausente:
```sh
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```
Revisar/confiar nos hooks pelo mecanismo suportado (`/hooks` quando disponivel), sem conceder permissao ampla automaticamente. Confirmar `full`, nao `ultra`.

## Claude Code
Instalacao inicial numa sessao interativa que suporte plugins, um comando por vez:
```text
/plugin marketplace add romulorenatoss-maker/romulo-dev-standard
```
```text
/plugin install romulo-dev-standard@romulo-dev-standard
```
Ponytail, se ausente:
```text
/plugin marketplace add DietrichGebert/ponytail
```
```text
/plugin install ponytail@ponytail
```

Para atualizar o padrao JA instalado, no terminal (nao como slash command):
```sh
claude plugin marketplace update romulo-dev-standard
claude plugin update romulo-dev-standard@romulo-dev-standard
claude plugin list
```
Confirmar o escopo efetivo; em versao que nao o detecte, usar `--scope` conforme o escopo encontrado. Na conversa existente do Claude Code compativel:
```text
/reload-plugins
```
Nao precisa abrir outra conversa quando a recarga funcionar. Conferir a versao e as skills, inclusive `/romulo-dev-standard:romulo-especificar` e `/romulo-dev-standard:romulo-interface`. Se recarga nao estiver disponivel/falhar, usar a reinicializacao suportada. Nao usar `--force` sem revisar o motivo e a autorizacao pertinente.

Alternativa interativa de atualizacao: `/plugin` -> Installed -> selecionar o padrao -> Update now; aplicar recarga indicada pelo cliente. Atualizar apenas a listagem do marketplace nao basta para comprovar plugin atualizado.

Sessao cloud/browser pode nao carregar plugins instalados localmente nem os habilitados pelo repositorio. Identificar essa limitacao em vez de repetir comandos locais nela. Nao alegar que recarregar instala num ambiente diferente.

## Verificacao das 11 skills
Esperadas na descoberta da sessao:
- romulo-analisar
- romulo-iniciar-projeto
- romulo-auditar-projeto
- romulo-especificar
- romulo-interface
- romulo-construir
- romulo-seguranca
- romulo-documentacao
- romulo-prototipo-real
- romulo-verificar
- romulo-evoluir-padrao

Plugin instalado/habilitado, versao adequada, skill descoberta e skill lida/aplicada sao evidencias diferentes. Confirmar nomes/versao, nao apenas contagem; carregar conteudo conforme tarefa. Falta obrigatoria: `ROMULO_STANDARD_NAO_DISPONIVEL`; Ponytail ausente: `PONYTAIL_NAO_DISPONIVEL`. Nunca fingir aplicacao ou hook ativo.

## Janela existente: leitura nao e instalacao
A sessao pode ler arquivos acessiveis e usa-los como instrucoes, mas isso nao muda o plugin carregado. Somente com autorizacao explicita para leitura direta, indicar `DIRETRIZES_LIDAS_MANUALMENTE` e fonte/revisao; nao declarar plugin/hook ativo. Essa leitura permite analise/proposta, nao contorna exigencia local de bootstrap para construcao. Se faltar acesso ao repositorio privado, informar a limitacao; nao procurar copia publica por suposicao.

Texto para enviar na conversa atual depois da atualizacao/recarga:
```text
Leia o AGENTS.md vigente do projeto e confirme o Romulo Dev Standard 1.4.0 ou superior, as 11 skills e Ponytail full realmente disponiveis. Nao alegue instalacao por apenas ler arquivos. Antes de criar/alterar telas, abas, botoes, CSS ou funcoes, aplique romulo-analisar, romulo-especificar e romulo-interface conforme impacto; depois romulo-construir, romulo-seguranca e romulo-documentacao pertinentes, terminando com romulo-verificar. Para a padronizacao ampla, comece levantando telas/componentes/regras/peculiaridades existentes, faca apenas perguntas faltantes e apresente proposta de telas, acoes, conexoes e referencia visual para minha aprovacao. Nao crie elementos sem tarefa comprovada nem altere diferenca protegida. Defeito corrigivel no alcance deve ser corrigido e retestado, nao apenas marcado pendente. Preserve autorizacoes e trabalho alheio; nao altere AGENTS protegido, banco, permissoes ou deploy sem a autorizacao exigida.
```

## Migracao de consumidores
1.4.0 adiciona duas skills e fortalece o fluxo das existentes. Atualizar plugin e confirmar descoberta. Consumidor fixado em versao anterior pode exigir migracao autorizada de versao minima/lista/roteamento no AGENTS local; nao sobrescrever esse arquivo nem peculiaridades. `templates/CLAUDE.md` continua apontando a `@AGENTS.md`. Instalar esta distribuicao nao implementa design system nem padroniza telas automaticamente.

## Fallback manual ja existente
Somente com autorizacao explicita e clone validado deste repositorio, usar os instaladores em `install/`. Eles copiam skills para o perfil; nao comprovam descoberta pela sessao nem instalam Ponytail. Nao usar para esconder falha de plugin ou sobrescrever skills customizadas sem avaliar conflito.
```powershell
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -InstallSkills
```
Para criar AGENTS/CLAUDE apenas quando ausentes:
```powershell
powershell -ExecutionPolicy Bypass -File .\install\install.ps1 -ProjectPath C:\caminho\projeto -InitializeProject
```

## Validacao da fonte
Requer Python 3.10+. No clone central: `python3 scripts/validate_standard.py` e `python3 -m unittest discover -s tests -v` (Windows: `python` se apropriado). Esses comandos nao instalam plugins, nao acessam producao e nao testam interface de consumidor. Registrar ativacao no host separadamente.

## Referencias oficiais consultadas
- OpenAI, pacote e marketplaces: https://developers.openai.com/plugins/build/plugins
- Claude Code, instalacao e atualizacao: https://code.claude.com/docs/en/discover-plugins
- Claude Code, comandos e recarga: https://code.claude.com/docs/en/plugins/cli-reference
- Ponytail, fonte oficial: https://github.com/DietrichGebert/ponytail
