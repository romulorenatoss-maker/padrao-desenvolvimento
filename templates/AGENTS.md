# AGENTS.md

## Identidade local
PROJETO: <nome>
REPOSITORIO_OFICIAL: <owner/repo>
BRANCH_OFICIAL: main
AMBIENTE_PRODUCAO: <quando aplicavel>
VERSAO_MINIMA_ROMULO_STANDARD: 1.4.0

Antes de qualquer escrita, confirmar projeto, repositorio, branch e ambiente atingido. Divergencia bloqueia a operacao afetada. Segredos nunca entram em codigo, documentacao, prompt, log ou Git.

## Bootstrap obrigatorio
Padrao: https://github.com/romulorenatoss-maker/romulo-dev-standard
Ponytail: https://github.com/DietrichGebert/ponytail

Antes de qualquer tarefa tecnica, detectar plataforma/superficie e confirmar plugin, versao minima, skills disponiveis na sessao e Ponytail. Instalacao, atualizacao e sessao aberta seguem o `INSTALL.md` da fonte central. Ja ativo na versao adequada: nao reinstalar. Arquivo no GitHub/disco nao prova descoberta pela sessao; leitura direta nao ativa plugin ou hooks.

Faltando: instalar/atualizar pelo mecanismo suportado quando autorizado, respeitando ambiente e escopo; sem permissao, mostrar os comandos pertinentes e o impedimento. Nao fingir carregamento. Claude Code compativel pode usar `/reload-plugins`; Codex deve confirmar redescoberta, usando nova thread/sessao quando necessaria. Nao inventar hot reload nem forcar a pessoa a perder a conversa se a superficie suporta recarga. Nao copiar skills para esconder falha.

Skills esperadas: `romulo-analisar`, `romulo-iniciar-projeto`, `romulo-auditar-projeto`, `romulo-especificar`, `romulo-interface`, `romulo-construir`, `romulo-seguranca`, `romulo-documentacao`, `romulo-prototipo-real`, `romulo-verificar`, `romulo-evoluir-padrao`.
Qualquer obrigatoria ausente: `ROMULO_STANDARD_NAO_DISPONIVEL`; Ponytail ausente: `PONYTAIL_NAO_DISPONIVEL`. Informar nominalmente o que falta. Confirme descoberta das 11, mas carregue o conteudo integral somente das skills pertinentes a tarefa, evitando contexto inutil.

## Roteamento obrigatorio em toda criacao/alteracao
1. `romulo-analisar` antes de escrever: regras locais, fontes canonicas vigentes, codigo e consumidores pertinentes.
2. Ponytail `full` como complemento, sem reduzir requisito, aprovacao, seguranca, documentacao ou teste. Nao ativar ultra por iniciativa propria.
3. `romulo-especificar` quando houver capacidade, regra, fluxo ou interface: tarefa de cada elemento, perguntas faltantes e proposta aprovada; correcao fiel ao contrato usa caminho curto.
4. `romulo-interface` em todo efeito visual/interativo, inclusive indireto em CSS/componente compartilhado: referencia aprovada, reutilizacao, peculiaridades e verificacao renderizada.
5. Skill principal da operacao, com documentacao e seguranca pertinentes; `romulo-verificar` antes de concluir e devolver falhas corrigiveis a construcao.

Operacoes: projeto vazio -> `romulo-iniciar-projeto`; auditoria ampla -> `romulo-auditar-projeto`; construir/alterar/bug -> `romulo-construir`; acesso/entrada/dados sensiveis/integracao -> `romulo-seguranca`; efeito documental -> `romulo-documentacao`; prototipo -> real -> `romulo-prototipo-real`; diretriz global -> `romulo-evoluir-padrao`.

Essas chamadas nao dependem de o usuario mencionar a skill. Consulta ja valida na mesma revisao pode ser reutilizada; nova alteracao nas fontes invalida a evidencia afetada. Sem efeito de produto/interface: justificar NAO_SE_APLICA, sem entrevista desnecessaria. Nao reproduzir especificacoes completas aqui; as skills sao as fontes donas.

## Arquitetura comum
Responsabilidades conceituais: View/interface (apresentacao e interacao) -> Action/entrada (transporte, sessao, metodo, protecao) -> Controller (normalizacao) -> Service (regra, autorizacao, escopo, estado) -> Repository/contrato (persistencia/consulta autorizada) -> Banco (integridade, constraints, transacoes e concorrencia pertinente).

A stack representa isso idiomaticamente. Nao criar camada vazia nem banco/API para acao puramente local. Regra critica nao fica somente no frontend; frontend nao concede autorizacao; backend revalida efeitos oficiais; banco protege invariantes pertinentes.

## Regras invariantes
Responsabilidade antes de pasta. Reconhecer antes de criar. Reutilizar antes de duplicar. Menor solucao que cumpra integralmente o pedido. Nao fabricar botoes, abas, dashboard, CRUD ou configuracoes sem tarefa comprovada; utilidade e aprovacao seguem `romulo-especificar`.

Referencia visual e peculiaridades seguem `romulo-interface`. Instalar o padrao nao altera CSS/componentes do projeto nem autoriza padronizacao em massa. Preservar o que esta correto e as diferencas aprovadas; nao impor arvore de outro projeto.

Documentacao acompanha a mudanca no mesmo lote no destino canonico, nao um arquivo por botao/funcao/agente. Nao criar arvore documental vazia. Ausencia de evidencia = NAO_VERIFICADO; verificacoes usam PASSOU, FALHOU, NAO_EXECUTADO e NAO_SE_APLICA.

Falha tecnica corrigivel no alcance exige correcao e novo teste; nao encerrar apenas com etiqueta pendente. Impedimento externo real deve ser declarado sem fingir conclusao. Prototipo nao comprova backend, persistencia ou seguranca; dados ficticios nunca migram para producao.

Preservar trabalho alheio e autorizacoes locais. Nao apagar dados, migrar destrutivamente, conceder permissoes, commitar, fazer push ou deploy sem autorizacao aplicavel. Commit, push, deploy e versao ativa sao estados distintos. Nunca desligar guardas/hook/protecao para passar.

## Evolucao
Regra global pertence a `romulorenatoss-maker/romulo-dev-standard`: `romulo-evoluir-padrao` -> fonte dona -> validar -> versionar -> publicar com autorizacao -> atualizar consumidores. Nao copiar regras para varios AGENTS.md. Identidade, infraestrutura, negocio, guardas e peculiaridades locais ficam no projeto. Migracao de versao e autorizacoes especificas nao podem ser contornadas pelo template.

## Particularidades locais
<preencher somente identidade, infraestrutura, negocio, docs canonicas, testes, deploy, autorizacoes e guardas deste projeto>
