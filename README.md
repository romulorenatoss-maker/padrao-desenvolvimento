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
- romulo-construir
- romulo-seguranca
- romulo-documentacao
- romulo-prototipo-real
- romulo-verificar
- romulo-evoluir-padrao

Ponytail (`DietrichGebert/ponytail`) e complemento externo para simplificacao, instalado no bootstrap (ver INSTALL.md). Nao substitui requisito, seguranca, documentacao, teste ou autorizacao.

## Uso
Use templates/AGENTS.md no projeto e templates/CLAUDE.md para Claude Code. O AGENTS faz o bootstrap: detecta, orienta/instala o plugin quando possivel, valida as 9 skills e roteia a tarefa.

Projeto vazio usa romulo-iniciar-projeto. Projeto existente usa romulo-auditar-projeto quando for necessaria analise ampla.

## Evolucao
Mudanca comum a todos os projetos usa romulo-evoluir-padrao e e feita aqui, na fonte dona da regra. Projetos locais nao devem manter forks de diretrizes globais.

Versao: 1.3.1
