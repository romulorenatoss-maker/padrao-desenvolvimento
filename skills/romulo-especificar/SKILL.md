---
name: romulo-especificar
description: Use antes de criar ou alterar capacidade, tela, aba, campo, botao, navegacao, regra ou integracao. Investigue o existente, pergunte so decisoes ausentes e apresente a proposta de telas, acoes e conexoes para aprovacao antes de construir. Em correcao fiel ao contrato, use a verificacao curta sem repetir entrevista.
---

# Romulo Especificar

Fonte dona da especificacao e da utilidade de cada elemento. Use depois de `romulo-analisar`; padrao visual pertence a `romulo-interface`, implementacao a `romulo-construir` e aceite a `romulo-verificar`. Nao duplica essas regras.

## 1. Identificar a tarefa antes de desenhar

Reformule: quem executa qual tarefa, em qual contexto, para obter qual resultado. Nao substituir silenciosamente a solucao pedida por outra: explicar a equivalencia e obter aprovacao quando mudar a experiencia.

Leia primeiro a documentacao canonica, decisoes aprovadas, tela, componentes, rotas, contratos, regras e consumidores do recorte. Siga as dependencias encontradas. Nao invente comportamento porque um modulo tem um nome familiar; capacidade usada numa tela continua pertencendo ao modulo dono da regra.

Procedimento obrigatorio antes da proposta: inspecionar a tela pedida no navegador quando disponivel e rastrear cada elemento atingido: eventos/gatilhos, modais, actions, services, contratos, dados, regras de disponibilidade e consumidores noutras telas/aparelhos, inclusive prototipo e real conforme o alvo. Conferir a finalidade original e os pedidos anteriores nas fontes canonicas e, se necessario, no historico Git; a ultima decisao autorizada prevalece. Identificar o que sera adicionado, alterado, movido, removido ou preservado e por que, incluindo consequencias nas regras ligadas ao recorte. A investigacao e profunda; a apresentacao e curta, no formato de `romulo-interface` secao 6. Elo inacessivel ou nao comprovado deve ser declarado, sem inventar conclusao.

Diferencie contrato aprovado de implementacao atual. Codigo existente evidencia comportamento, nao necessariamente aprovacao. Divergencia entre codigo, documento e decisao exige reconciliacao; nao documentar o bug como nova regra.

## 2. Checklist interno antes de perguntar

Para cada tema, marque RESOLVIDO_PELO_PEDIDO, RESOLVIDO_PELO_SISTEMA, PRECISA_DECISAO ou NAO_SE_APLICA. Registre a fonte/justificativa no destino canonico quando necessario. Sem acesso: NAO_DESCOBERTO, nao ausencia comprovada.

| Tema | O que descobrir |
|---|---|
| Objetivo | Usuario, tarefa, contexto de uso, resultado e limites do pedido. |
| Entrada e continuidade | Menu/rota/tela/aba de origem, proxima etapa, retorno e preservacao de contexto. |
| Responsabilidade | Modulo dono, capacidade existente, equivalentes reutilizaveis e o que fica intocado. |
| Regras | Decisoes vigentes, estados/transicoes permitidas, calculos/unidades e efeitos entre modulos. |
| Informacao | Campos indispensaveis, origem oficial, editavel/calculado/exibido/filtro/temporario e destino aplicavel. |
| Acoes | Tarefa atendida, condicao de disponibilidade, permissao, efeito observavel e recuperacao. |
| Integracao | Contratos reais, quem le/escreve, persistencia e consumidores afetados. |
| Visual | Referencia aprovada, componentes/tokens existentes, responsividade e peculiaridades protegidas. |
| Aceite | Cenarios observaveis de sucesso, falha, acesso, persistencia e efeitos pertinentes. |

Pergunte ao responsavel somente decisoes ausentes ou conflitantes que afetem a solucao. Agrupe perguntas em uma rodada curta, com recomendacao e consequencia das alternativas quando util. Em revisao iterativa, seguir `romulo-interface` secao 6: confirmar entendimento e conferir com o responsavel quando pertinente, sem criar pendencia pelo silencio; construir no prototipo ou real conforme o alvo definido e perguntar apenas decisoes indispensaveis ausentes. Nao perguntar nome de arquivo, endpoint ou tamanho ja definido no projeto. Nao repetir resposta conhecida. Limites de acesso se resolvem por investigacao/autorizacao, nao pedindo que o usuario invente fatos tecnicos.

## 3. Proposta obrigatoria depois das respostas

Antes de construir uma capacidade nova, mudar fluxo/regra ou redesenhar, apresente a proposta consolidada e aguarde aprovacao do responsavel. Ausencia de novas perguntas nao elimina a proposta. Pedido ja acompanhado de proposta explicitamente aprovada: referencie essa revisao e nao peca aprovacao de novo.

Apresente na linguagem da operacao, seguindo a ordem, os titulos em negrito, o mapa em arvore de texto e a pergunta de confirmacao definidos em `romulo-interface` secao 6. Mostrar somente o recorte afetado pelo pedido.

Nomeie telas, abas/subabas quando necessarias, entrada, finalidade de cada parte, campos, botoes e resultado de cada acao; informe estados, acesso, navegacao posterior, visual de referencia, impactos e aceite pertinentes ao recorte. Nao invente nomes de rotas, APIs, tabelas ou permissoes como se existissem: separar COMPROVADO, PROPOSTO e A_LOCALIZAR. Antes da implementacao dependente, localizar o elo ou aprovar a capacidade ausente no dono correto.

Decisao de composicao: tela para tarefa com identidade/fluxo proprio; aba para contexto da mesma entidade; modal/drawer para acao curta contextual; ampliar/reutilizar quando a responsabilidade e compativel. Nao usar porcentagem arbitraria nem forcar toda tarefa em modal.

Para criar/alterar a identidade visual, apresente referencia renderizada/prototipo do recorte com `romulo-interface` antes de propagar a mudanca. Aprovar a proposta funcional nao aprova automaticamente um visual ainda nao mostrado. Prototipo visual aprovado nao comprova integracao real.

## 4. Contrato de utilidade de botoes e elementos

Toda acao criada ou alterada deve responder:
- qual requisito/decisao ou necessidade indispensavel ao fluxo a justifica;
- quem a utiliza, em qual contexto e pre-condicao;
- qual verbo/rotulo descreve o resultado observavel;
- qual comportamento local, navegacao, consulta ou mutacao executa;
- qual componente padrao, regra/contrato e evidencia a sustentam.

Pedido de remover botao: localizar suas copias e entradas alternativas, quem ainda chama sua funcao e qual regra motivou sua existencia. Informar se a capacidade termina ou continua em local nominal identificado. Se termina, retirar no alcance autorizado botao, gatilhos e codigo/registros exclusivos sem consumidor, incluindo mapas e prototipo atingidos; se continua, preservar somente os consumidores validos e atualizar suas ligacoes. Nao deixar botao oculto, handler orfao ou regra substituida ativa, nem apagar funcao compartilhada ainda necessaria. Reconciliar os testes existentes conforme o comportamento decidido.

Cancelar, voltar, fechar, tentar novamente e recursos de acessibilidade podem ser necessarios ao fluxo aprovado sem pedido individual. Justifique a necessidade; nao use isso para adicionar capacidades de negocio.

SEM_TAREFA_COMPROVADA: nao entra na proposta nem na implementacao nova. Proibido criar exportar, dashboard, cards de indicadores, filtros, CRUD completo, configuracoes ou atalhos somente por costume, simetria ou para preencher espaco. Elemento existente aparentemente inutil: investigar e propor remocao, nunca apagar sem alcance autorizado.

Revisao bidirecional: todo requisito aprovado tem solucao; todo elemento proposto tem razao. Um botao tecnicamente conectado pode continuar sem utilidade e deve ser corrigido na proposta. Nao esconder acao essencial num menu para parecer minimalista. Priorize a tarefa principal por contexto sem impor quantidade universal de botoes.

## 5. Escopo, aprovacao e mudancas

Informe CRIAR, ALTERAR, REUTILIZAR e PRESERVAR no registro existente, sem arquivo de plano paralelo. Associe proposta/revisao, fonte da aprovacao e criterios de aceite ao mapa/assunto canonico; atualize com `romulo-documentacao`.

Bug que apenas restaura contrato aprovado, texto ou ajuste visual que retorna ao padrao: consulta curta + informar diferenca + corrigir no alcance autorizado, sem entrevista nem redesenho. Nova regra, nova tarefa, alteracao de peculiaridade protegida ou mudanca visual nao aprovada: apresentar apenas o delta para aprovacao.

Uma duvida bloqueia somente a parte dependente; nao construir essa parte por suposicao. Autorizacao de desenho, codigo, banco, concessao de permissao, commit/push e deploy continuam distintas conforme contrato local. Nao aumentar o escopo para resolver conveniencia tecnica.

## 6. Handoff e cenarios de aceite do metodo

A construcao recebe a revisao aprovada e seus vinculos, nao uma descricao solta. Conferir novamente se surgiram mudancas concorrentes nas fontes antes de escrever. Na entrega, confrontar proposta e resultado com `romulo-verificar`.

Cenarios obrigatorios ao revisar esta skill (avaliacao de comportamento, nao teste automatico de IA):
- "Financeiro no cliente": localizar dono e contratos; propor integracao, nao criar financeiro paralelo.
- "Corrigir salvar": rastrear e restaurar a cadeia aprovada, nao perguntar novamente quais abas o sistema tem.
- "Criar tela nova": perguntas faltantes -> proposta nominal de telas/abas/acoes -> aprovacao -> construir.
- "Adicionar exportar porque cabe no cabecalho": recusar essa inclusao especulativa, sem remover requisitos legitimos.
- "Reaplicar padrao": preservar peculiaridade aprovada e consultar antes de muda-la.
