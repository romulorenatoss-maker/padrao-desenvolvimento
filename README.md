# Romulo Dev Standard

Padrao central e portatil para todos os projetos do Romulo.

## Objetivo
Uma unica fonte versionada define arquitetura, analise, inicializacao, construcao, seguranca, documentacao, prototipo para real, verificacao e evolucao do metodo. Cada projeto mantem no AGENTS.md apenas identidade e peculiaridades locais.

## Arquitetura comum
Todos os projetos seguem as mesmas responsabilidades conceituais:
View/interface -> Action/entrada -> Controller -> Service -> Repository/contrato -> Banco.

A stack pode representar essas responsabilidades de forma idiomatica, sem camadas vazias. Regra critica e autorizacao nao ficam apenas no frontend.

## Principios
- reconhecer antes de criar;
- responsabilidade antes de pasta;
- reutilizar antes de duplicar;
- criar apenas o necessario para a capacidade real;
- menor implementacao que cumpra integralmente o pedido;
- seguranca no runtime;
- documentacao canonica junto da mudanca;
- evidencia antes de declarar pronto;
- ausencia de evidencia = NAO_VERIFICADO;
- dados ficticios de prototipo nunca vao para producao;
- diretriz global e alterada no repositorio central, nunca copiada projeto a projeto.

## Skills
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

Ponytail (`DietrichGebert/ponytail`) e complemento externo para simplificacao, instalado no bootstrap (ver INSTALL.md). Nao substitui requisito, seguranca, documentacao, teste ou autorizacao.

## Uso
Use templates/AGENTS.md no projeto e templates/CLAUDE.md para Claude Code. O AGENTS faz o bootstrap: detecta, orienta/instala o plugin quando possivel, valida as 11 skills e roteia a tarefa.

Projeto vazio usa romulo-iniciar-projeto. Projeto existente usa romulo-auditar-projeto quando for necessaria analise ampla.

## Evolucao
Mudanca comum a todos os projetos usa romulo-evoluir-padrao e e feita aqui, na fonte dona da regra. Projetos locais nao devem manter forks de diretrizes globais.

Versao: 1.4.0

## Entrega de produto e interface (1.4.0)
Toda criacao/alteracao consulta as fontes vigentes por `romulo-analisar`. `romulo-especificar` exige tarefa para cada elemento, perguntas so por lacunas e proposta de telas/abas/acoes/conexoes aprovada; `romulo-interface` aplica referencia visual, componentes reais e peculiaridades protegidas. `romulo-construir` fecha a cadeia e corrige defeitos no alcance; `romulo-verificar` exige evidencia pertinente. Correcao local fiel ao contrato usa caminho curto, sem entrevista repetida.

Padrao visual e implementado no projeto consumidor com autorizacao, nao por instalar este plugin. Nao ha framework imposto, promessa de zero bugs ou garantia de ser superior a outro produto. Skills orientam comportamento; verificacoes da aplicacao devem existir e ser executadas no ambiente real autorizado.

## Atualizacao e compatibilidade
1.4.0 acrescenta duas skills; atualizar plugin e confirmar descoberta das 11. Consumidor fixado em versao anterior nao e migrado silenciosamente. AGENTS local antigo pode precisar, com autorizacao propria, atualizar somente versao minima, lista e roteamento; nunca substituir peculiaridades ou copiar especificacoes globais. A cadeia analisar/construir/verificar tambem chama as novas skills para nao depender apenas do template novo.

Sessao aberta, instalacao e comandos: fonte unica em [INSTALL.md](INSTALL.md). Ler texto diretamente nao prova plugin/hook ativo. Padronizacao de telas existentes comeca por levantamento e proposta; instalar o metodo nao autoriza editar/publicar todo o sistema.

## Verificar o pacote
Executar `python3 scripts/validate_standard.py` e `python3 -m unittest discover -s tests -v`. Requer Python 3.10+; sem dependencias Python externas. Validacao estrutural e cenarios negativos nao comprovam obediencia do modelo, qualidade visual ou funcionamento de projetos consumidores. Os cenarios descritivos de `romulo-especificar` servem para avaliacao comportamental separada.
