# Instalacao, atualizacao e migracao local

A entrada e o catalogo de diretrizes ficam no [README.md](README.md). Nao copiar a lista de skills para este arquivo ou para AGENTS locais. A conta usada pelo cliente precisa de leitura no repositorio privado oficial. Executar instalacao apenas no ambiente/escopo autorizado, sem imprimir credenciais.

## Verificar antes de executar
Identificar Claude Code/Codex e superficie (terminal, IDE, desktop, cloud), versao e comandos suportados, instalacao existente e escopo. Configuracao local nao comprova instalacao no cloud. Confirmar identidade, protecoes e trabalho pendente do projeto. Nao instalar outro plugin, remover Figma ou alterar permissoes por este procedimento.

Resolver o README e templates da mesma revisao oficial indicada pelo AGENTS. O sumario informa quais skills existem e quando carregar cada uma. Instalar/habilitar o pacote necessario e confirmar descoberta nominal; ler integralmente so as skills pertinentes. Sem modo suportado, indicar o impedimento, nao inventar flags, editar cache interno ou dizer que carregou.

## Claude Code — comandos no terminal
Primeira instalacao, se o marketplace/plugin nao existir:
```sh
claude plugin marketplace add romulorenatoss-maker/romulo-dev-standard
claude plugin install romulo-dev-standard@romulo-dev-standard
```
Ja instalado:
```sh
claude plugin marketplace update romulo-dev-standard
claude plugin update romulo-dev-standard@romulo-dev-standard
claude plugin list
```
Confirmar escopo com a listagem; usar `--scope` correto se a versao instalada exigir. Nao forcar, aceitar comandos de instalacao adicionais ou conceder permissoes amplas sem revisar.

Na conversa aberta, quando suportado:
```text
/reload-plugins
```
Verificar resumo de carga, erros, versao e skills descobertas. Em interfaces que exigem que o usuario digite esse comando diretamente, informa-lo; nao alegar recarga feita por ferramenta. Se falhar/nao houver suporte, usar nova sessao conforme o cliente, sem prometer hot reload universal. A documentacao oficial descreve recarga em interfaces nao interativas compativeis, mas as ferramentas MCP podem depender de nova sessao.

Ponytail, apenas se ausente e autorizado:
```sh
claude plugin marketplace add DietrichGebert/ponytail
claude plugin install ponytail@ponytail
```
Confirmar modo full e hooks pelo mecanismo suportado. Nao ativar ultra nem confiar indiscriminadamente em hooks.

## Codex — marketplace e instalacao na superficie correta
Comandos do catalogo documentados; executar somente os disponiveis no cliente:
```sh
codex plugin marketplace list
codex plugin marketplace add romulorenatoss-maker/romulo-dev-standard --ref main
codex plugin marketplace upgrade romulo-dev-standard
```
Adicionar somente se ausente; atualizar somente o catalogo existente. Instalar/atualizar/habilitar o plugin pelo gerenciador suportado da superficie. `codex plugin add` nao e pressuposto universal: so usa-lo se o `--help` local o comprovar e explicar o escopo. Atualizar o marketplace sozinho nao confirma instalacao nem carga da conversa.

Para Ponytail ausente, cadastrar `DietrichGebert/ponytail` pelo mesmo mecanismo e instalar o plugin pelo gerenciador suportado. Revisar hooks, quando existirem, no mecanismo do cliente. Confirmar full e disponibilidade; nao prometer que recurso local aparece numa sessao cloud.

A sessao deve comprovar a redescoberta. Se nao suportar recarga, reiniciar/abrir nova sessao pelo mecanismo adequado; preservar contexto no dono documental, nao gerar memoria paralela. Configurar plugin nao delega geracao de codigo.

## AGENTS local e CLAUDE ponte
A skill dona e romulo-iniciar-projeto, indicada no catalogo central. Buscar [templates/AGENTS.md](templates/AGENTS.md), nunca copiar o AGENTS da raiz deste repositorio. Ler TODO o contrato atual, identificar protecoes e apresentar o diff de migracao. Preencher dados comprovados e remover campos opcionais nao aplicaveis; nao salvar placeholders.

Se AGENTS estiver protegido por 0393, a migracao fica pendente ate autorizacao especifica. Mencao da senha nesta documentacao nao autoriza. Antes de retirar regras locais, preservar seu conteudo em destinos canonicos validos e apontados; nao enfraquecer guardas para caber no template. Nao sobrescrever alteracoes de outro executor. Sem autorizacao, e permitido analisar/atualizar o plugin dentro do escopo autorizado, nao mudar o contrato protegido.

Quando requerido no projeto com Claude Code, criar CLAUDE.md ausente a partir de [templates/CLAUDE.md](templates/CLAUDE.md), contendo somente @AGENTS.md. Existente: preservar e reconciliar, nunca copiar regras globais ou usar /init para gerar um contrato concorrente. Claude moderno pode ler AGENTS diretamente; a ponte explicita continua o modelo portatil adotado pelo padrao quando CLAUDE for requerido.

## Recursos importados na distribuicao

A distribuicao inclui o pacote completo de movimento registrado no catalogo central, com revisao de origem e licenca dentro da pasta da skill. Atualizar o plugin completo instala tambem seus workflows/referencias; nao copiar SKILL.md avulso, nao instalar o pacote upstream separadamente nem executar instaladores de dependencias por exemplos. Na nova sessao, conferir a descoberta nominal e versao; sessao aberta termina o lote antes da migracao.

## Leitura direta nao e ativacao
Arquivos acessiveis podem orientar analise/bootstrap, registrando fonte e revisao. Isso nao ativa plugin nem hooks. Nao instalar copia avulsa de SKILL.md: quebra referencias relativas e cria fontes concorrentes. A construcao de produto permanece sujeita a disponibilidade exigida no projeto. Fontes indisponiveis nao podem ser inventadas.

## Instaladores legados
Em 1.5.0, `install/install.ps1` e `install/install.sh` tornam-se verificadores somente leitura. Eles NAO copiam skills avulsas nem criam AGENTS com placeholders, e recusam flags antigas de escrita. Usar os comandos nativos acima para o pacote completo e a skill de bootstrap para a migracao revisada. A mudanca evita sobrescrita silenciosa e preserva references/README junto do plugin. Nenhum script aqui concede 0393 automaticamente.

## Validar a fonte
Com Python 3.10+: `python3 scripts/validate_standard.py` e `python3 -m unittest discover -s tests -v`. Em Windows, usar `python` quando apropriado. Isso verifica distribuicao, nao instalacao na conta, padronizacao de telas nem bloqueio universal de arquivos.

## Fontes oficiais dos mecanismos
- OpenAI, empacotamento e marketplaces: https://developers.openai.com/plugins/build/plugins
- Claude Code, comandos de plugins/recarga: https://code.claude.com/docs/en/plugins/cli-reference
- Claude Code, CLAUDE.md/AGENTS.md e imports: https://code.claude.com/docs/en/memory
- Ponytail: https://github.com/DietrichGebert/ponytail
