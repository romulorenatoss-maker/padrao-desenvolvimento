# Romulo Dev Standard

Padrão central e portátil para desenvolvimento assistido por agentes.

## Objetivo
Manter uma única fonte versionada para análise, construção, segurança, documentação, conversão de protótipo para real e verificação. Cada projeto mantém somente sua identidade, autorizações e exceções locais no AGENTS.md.

## Princípios
- reconhecer antes de criar;
- preservar a arquitetura real quando correta;
- responsabilidade antes de pasta;
- reutilizar antes de duplicar;
- menor implementação que cumpra integralmente o pedido;
- segurança no runtime;
- documentação canônica junto da mudança;
- evidência antes de declarar pronto;
- ausência de evidência = NAO_VERIFICADO;
- nunca transportar dados fictícios de protótipo para produção.

## Skills
- romulo-analisar
- romulo-construir
- romulo-seguranca
- romulo-documentacao
- romulo-prototipo-real
- romulo-verificar
- romulo-auditar-projeto

Ponytail é um complemento externo obrigatório nas tarefas técnicas quando estiver instalado/disponível. Ele não substitui requisitos, segurança, documentação, testes ou autorização.

## Uso
Use templates/AGENTS.md no projeto e templates/CLAUDE.md para Claude Code. As skills devem ser instaladas no mecanismo suportado pelo agente; não dependa de leitura remota do GitHub durante cada tarefa.

## Regra de portabilidade
O padrão não obriga outro sistema a copiar estrutura de pastas. Primeiro reconhece stack, responsabilidades e convenções; só propõe criação quando existir lacuna comprovada.

Versão inicial: 1.0.0
