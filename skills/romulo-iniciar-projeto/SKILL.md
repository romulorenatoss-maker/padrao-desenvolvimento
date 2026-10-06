---
name: romulo-iniciar-projeto
description: Use obrigatoriamente quando um projeto novo ou vazio for iniciado sob o Romulo Dev Standard, para criar a base minima comum sem gerar arquivos, camadas ou documentacao sem uso.
---

# Romulo Iniciar Projeto

Todos os projetos novos seguem a mesma arquitetura conceitual Romulo Dev Standard.

Antes de criar arquivos:
1. confirmar identidade do projeto, repositorio, branch, ambiente e stack autorizada;
2. confirmar AGENTS.md local e CLAUDE.md quando aplicavel;
3. confirmar Romulo Dev Standard e Ponytail realmente carregados;
4. identificar a primeira capacidade real que sera construida;
5. criar somente a estrutura necessaria para essa capacidade.

## Arquitetura comum

As responsabilidades seguem este modelo conceitual:
- View/interface: apresentacao e interacao;
- Action/entrada: transporte, sessao, metodo e protecao aplicavel;
- Controller: normalizacao de entrada e saida;
- Service: regra de negocio, autorizacao, escopo e estado;
- Repository/contrato: persistencia e consultas autorizadas;
- Banco: integridade, constraints, transacoes e concorrencia pertinente.

A stack pode materializar essas responsabilidades de formas diferentes, mas nao deve misturar regra critica no frontend, autorizacao apenas visual ou persistencia sem contrato.

Nao criar camada vazia. Nao criar CRUD completo, dashboard, exportacao, configuracao ou abstracao para uso futuro.

## Projeto vazio

Quando nao existir estrutura:
- criar AGENTS.md a partir do template oficial, preenchendo somente identidade e particularidades;
- criar CLAUDE.md com @AGENTS.md quando Claude Code for usado;
- criar a menor estrutura de codigo necessaria para a primeira capacidade;
- criar documentacao canonica minima somente quando a responsabilidade real nascer;
- criar testes proporcionais ao risco/efeito da capacidade;
- configurar segredos somente em runtime/ambiente seguro;
- nao criar banco, migration, permissao ou deploy sem necessidade e autorizacao.

## Verificacao inicial

Antes de concluir a inicializacao, confirmar:
- projeto/branch corretos;
- 9 skills Romulo descobertas;
- Ponytail disponivel ou estado explicitamente informado;
- primeira capacidade com dono e consumidores;
- ausencia de pastas/arquivos sem responsabilidade real;
- seguranca e documentacao pertinentes;
- romulo-verificar executado.

A inicializacao nao autoriza commit, push, deploy, criacao de banco ou alteracao destrutiva sem autorizacao local.
