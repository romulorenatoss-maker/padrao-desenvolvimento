---
name: romulo-documentacao
description: "Use quando mudar comportamento, estrutura, contrato, regra, dado, acesso ou conhecimento canonico; aplicar destinos existentes ou fallback central e reconciliar vinculos no mesmo lote sem notas paralelas."
---

# Romulo Documentacao

Documentacao explica responsabilidade, comportamento e vinculos; nao reescreve codigo em prosa. Decisao respondida vive no documento do modulo dono; registro de perguntas e fila de trabalho guardam so o aberto (`romulo-construir`, limpeza dos registros de trabalho). Consultar `romulo-analisar` e [destinos documentais](../../references/DOCUMENTACAO.md). A referencia define nomes/conteudo quando nao existe equivalente; nao perguntar ao usuario nomes que o padrao ja determina.

Atualizar o dono existente. Documento novo somente por responsabilidade real sem destino adequado, no alcance autorizado e com previsao no gate. Nao criar documento por agente, arquivo, funcao, botao, campo, linha ou execucao. Sem arvore vazia, PLANO, FINAL, V2, backup documental, memoria ou certificado paralelo. Git preserva historico; o dono canonico preserva o estado util atual.

Registrar fatos comprovados e decisoes aprovadas, com fonte e revisao. Preservar IDs e distinguir previsto, simulado, construido, testado e publicado. No fechamento: artefato -> identidade/responsabilidade -> mapa/dono -> consumidores, e inverso pertinente. Mudanca interna sem efeito no conhecimento canonico nao exige narrativa artificial, salvo evidencia exigida por instrumento local.

Decisoes de `romulo-especificar` e referencia/peculiaridades de `romulo-interface` ficam no mapa/assunto local. Padrao geral permanece na skill central. Indicador de peculiaridade e projecao derivada usam a mesma fonte, sem listas manuais concorrentes.

Registrar [rastreabilidade DNA, issue, PR e commit](../../references/DOCUMENTACAO.md#rastreabilidade-dna-issue-pr-e-commit) junto ao item/lote dono; preservar identidade, usar links qualificados e atualizar o mapa existente. Issue/PR apontam de volta para IDs/documentos; nao criar outro mapa nem usar o ticket como fonte da regra vigente. Perfil concreto de ferramentas/checks fica no processo/PROJETO.md equivalente existente conforme a referencia, sem duplicar o metodo no AGENTS.

## Conhecimento vivo das paginas e suas conexoes

Cada pagina criada tem um documento dono util; reutilizar `TELA.md` ou equivalente existente, com secoes para abas relacionadas, seguindo [Como escrever o documento da pagina](../../references/DOCUMENTACAO.md#como-escrever-o-documento-da-pagina-telamd-ou-equivalente). Regras compartilhadas ficam no contrato/componente dono. Cada pagina consumidora aponta para a regra e explica por que a usa, sem copiar a mesma especificacao para varios locais.

O documento vigente da pagina e a fonte canonica das decisoes dela: conter o contexto completo necessario para entender finalidade, regras e conexoes sem acessar o chat. Conversas servem de apoio temporario para recuperar/esclarecer conhecimento ausente; a decisao confirmada entra no dono, nao fica somente no chat ou em nota paralela. Sumarios/inventario apontam para essa fonte, nao competem com ela. Pedido humano novo pode alterar a decisao e exige atualizar o documento; documento nao autoriza negar essa mudanca nem tratar divergencia do codigo como regra aprovada.

Ao consolidar uma pagina/aba, aplicar a [marcacao do contexto consolidado](../../references/DOCUMENTACAO.md#marcacao-do-contexto-consolidado). Ela define quais recortes ja usam exclusivamente o conhecimento vigente documentado e quais ainda podem recuperar conversas/historico. Consolidacao e incremental: nova explicacao atualiza o dono; a marca nao congela a regra nem comprova implementacao.

Terminou a conciliacao do recorte, marcar `CONTEXTO_CONSOLIDADO: SIM` e reconciliar sua pendencia documental no mesmo lote antes da entrega/commit. O executor faz esse fechamento sem pedir nova autorizacao para a marca, nem deixar a conclusao para outro agente; seguir os limites de alcance definidos na referencia.

Para cada comportamento identificado pelo DNA existente, manter uma explicacao rapida de ate duas linhas curtas: (1) o que faz e por que existe; (2) de onde recebe, quem utiliza e qual efeito relevante uma alteracao/remocao provoca. Vincular ao ID, local visual e fonte dona. O limite vale para esse resumo por item: detalhar abaixo as condicoes, excecoes, dados, contratos e arquivos/simbolos necessarios, sem cortar regra critica para caber. Linha visual varia por dispositivo; usar duas frases curtas como referencia.

Registrar decisao/intencao com sua fonte, comportamento implementado com revisao/evidencia e divergencias pendentes de forma distinta. Informacao desconhecida permanece explicita ate a pergunta/resposta pertinente; documentacao nao comprova execucao.

Preservar a riqueza util da explicacao humana: finalidade, motivacao, exemplos, excecoes, condicoes e conexoes futuras. As duas linhas sao somente o resumo do item; os detalhes continuam no dono canonico. Pergunta respondida sai da fila aberta e sua resposta entra no item/assunto correspondente. Registrar fonte e data/revisao da decisao; nao copiar conversa inteira, perder excecao relevante ao resumir, nem criar memoria funcional paralela.

Ideia para modulo/tela ainda inexistente fica no documento da entidade atual ou no assunto existente do prototipo, vinculada no sumario pertinente para descoberta futura, como PREVISTO - NAO CONSTRUIDO; aprovacao do desenho e estado de construcao sao separados. Descrever finalidade e conexao pretendida, sem fabricar caminho/link resolvido, DNA de implementacao, tabela ou API. Ao criar o consumidor autorizado, ligar a documentacao existente ao seu ID/documento real e conferir novamente a proposta. O previsto nao autoriza criar modulo, banco, interface ou publicar.

Cada resposta/incremento atualiza a mesma fonte e, quando pertinente, os documentos dos consumidores existentes afetados; manter vinculos coerentes e explicar o efeito do novo detalhe. Preservar detalhes/decisoes anteriores ainda validos; os substituidos saem da especificacao vigente, sem narrar todas as tentativas nem transportar texto obsoleto para outro arquivo. Sugestao descartada nao vira regra ou pendencia; ideia futura ainda valida conserva PREVISTO. Historico tecnico fica no Git e registros de auditoria/entrega exigidos, sem reescreve-los/apaga-los por esta limpeza. Antes de nova proposta, a consulta obrigatoria deste conhecimento segue `romulo-especificar`.

Ao criar, editar, mover ou remover capacidade, reconciliar no mesmo recorte o documento dono e os documentos de TODAS as paginas/abas comprovadamente afetadas: links/IDs, entrada/saida, motivo da dependencia e novo destino da funcao/informacao. Descobrir consumidores reais antes de declarar cobertura; nao criar listas concorrentes nem repetir a regra em cada consumidor. Pagina sem impacto nao exige narrativa nova. Nao apagar o historico nem romper continuidade de dados por retirar um controle visual.

Configuracoes transversais, como engrenagem e suas abas, registram finalidade, escopo e excecoes no dono; telas referenciam esse contrato. Descrever o padrao nao autoriza instalar o elemento em todas as paginas. A entrevista e a apresentacao do impacto seguem `romulo-especificar`.

Migrar texto de AGENTS/CLAUDE usa DE/PARA e preservacao descritos na referencia; a reducao do arquivo nao pode excluir protecao nem usar uma referencia ainda inexistente. Se a autorizacao de arquivo protegido faltar, nao mover/apagar seu conteudo. Consultar `romulo-iniciar-projeto` para bootstrap/ponte e `romulo-verificar` para fechamento.

Mudanca de diretriz GLOBAL segue `romulo-evoluir-padrao` na fonte central; regra financeira, tela, permissão, infraestrutura ou guarda peculiar continua no projeto. Regra de arquivo prevista em skill nao dispensa documentar a criacao quando o contrato exigir.

Na revisao iterativa de prototipo, seguir o fluxo de entrega visual e autorizacao documental de [romulo-prototipo-real](../romulo-prototipo-real/SKILL.md#revisao-rapida-do-prototipo-e-documentacao-paralela). Essa autorizacao documental nao equivale a aceite funcional nem construcao/publicacao real.
