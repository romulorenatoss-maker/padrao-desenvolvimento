# Modelo de padrao tecnico do projeto

Modelo de preenchimento para o TRD ou documento equivalente, conforme [DOCUMENTACAO](../references/DOCUMENTACAO.md#padroes-locais-preenchiveis). Completar o dono existente; criar `docs/architecture/TRD.md` apenas sem equivalente. Resolver links no destino. Este modelo nao instala stack, nao cria arvore e nao aprova tecnologias.

## Identidade e fontes

Registrar projeto, repositorio/ref/revisao conferida, ambiente e alcance; sumario, arquitetura/contratos existentes e catalogo visual. Sem segredos. Distinguir observado, proposto e aprovado, com fonte/data/alcance da decisao. Remover instrucoes de preenchimento do documento adotado; lacunas reais recebem A_DEFINIR, nao exemplos como fatos.

## Stack por escopo

| Escopo | Linguagem/runtime e versao | Framework/ferramenta | Estado e origem | Fontes reais |
|---|---|---|---|---|
| Aplicacao no navegador | Preencher pelo projeto | Somente adotado | Evidencia/decisao | Entradas/configuracao |
| Aplicacao no servidor | Preencher se houver | Somente adotado | Evidencia/decisao | Entradas/configuracao |
| Persistencia e migrations | Preencher se houver | Instrumento existente | Evidencia/decisao | Dono/contratos |
| Testes, scripts e build | Separar do produto | Comandos existentes | Evidencia/decisao | Configuracao/runner |

Uma ferramenta de teste escrita em TypeScript nao transforma o produto PHP em React. Projeto misto delimita onde cada tecnologia pode ser usada e como se integra. Nova tecnologia exige decisao pertinente, nao nasce da sugestao de um gerador.

## Estrutura e nomes

Registrar raizes reais de entrada/rotas, modulos, UI comum, assets, testes, scripts e documentos; fronteiras publicas e consumidores. Reutilizar convencao existente. Sem equivalente, aplicar os [exemplos de financeiro PHP/React](../references/ARQUITETURA.md#exemplos-de-modulo-financeiro-por-stack), selecionando apenas arquivos necessarios. O exemplo adotado passa a orientar os outros modulos da mesma stack.

| Tipo de arquivo | Responsabilidade | Caminho/extensao e nome | Estrutura interna/API publica | Documento e exemplo conferido |
|---|---|---|---|---|
| Entrada/pagina/view | Compor capacidade e integrar rota | Perfil da stack | Imports/entrada/saida | Dono/revisao |
| Componente local | Apresentacao do dominio | Perfil da stack | Props/contrato e exportacao | Dono/revisao |
| Componente compartilhado | Peca comum com consumidores | Raiz comum existente | Variantes/contrato | ID do catalogo |
| Hook, quando React | Estado/efeitos de responsabilidade definida | Prefixo use e destino local/comum | Entrada, retorno, propriedade e ciclo | Consumidores/revisao |
| Servico/adaptador | Contrato com fornecedor/dominio | Perfil da stack | Entrada/saida, erros, autorizacao aplicavel | Contrato/revisao |
| Persistencia, quando servidor | Acesso ao dado pelo dono | Perfil da stack | Consultas/escopo/transacao pertinente | Contrato de dados |
| Tipos/validacao | Contrato realmente compartilhado | Perfil da linguagem | Simbolos publicos e consumidores | Dono/revisao |
| Estilo/token/asset | Identidade ou composicao permitida | Convencao adotada | Escopo e consumo | Catalogo visual |
| Teste | Comportamento/risco relevante | Runner e sufixo vigentes | Cenario e comando | Regra testada |
| Documento Markdown | Conhecimento de responsabilidade definida | Destinos documentais vigentes | Finalidade, regras, vinculos e evidencia | Sumario/dono |

Completar o perfil para CADA linguagem usada, inclusive formato interno e exemplo real; eliminar linhas nao aplicaveis ou justifica-las. Nao criar pastas/arquivos vazios para completar a tabela. Nomes de dominio seguem o vocabulario local; simbolos e extensoes seguem a linguagem. Sem partes numeradas, copias v2 ou deposito generico de utilitarios.

## Modulos e contratos

Registrar capacidade/dono, finalidade, entradas publicas, USA/USADO_POR, dados que possui/consome, seguranca e limites. Interface do modulo consome contratos, sem acessar internos de outro dono. Apontar para a documentacao modular existente, sem copiar toda a regra aqui.

No exemplo financeiro, a pagina coordena, a lista compoe a UI comum, o hook controla o estado pertinente, o adaptador consulta a API e o backend decide efeitos oficiais. Registrar apenas elos realmente implementados; prototipo identifica sua simulacao.

## Referencias por linguagem

Para cada tipo adotado, apontar arquivo/simbolo e revisao exemplares, por que serve de referencia e como criar/corrigir seguindo-o. Um caminho ilustrativo nao e prova de arquivo existente. Conferir imports/exports, nomes, contratos, erros, testes e documento/DNA; seguir [identificacao interna](../references/DOCUMENTACAO.md#identificacao-e-documentacao-interna-do-codigo), sem repetir manual em comentarios.

Quando ainda nao houver referencia real, documentar a convencao necessaria, construir a primeira capacidade e conferir antes de aponta-la como exemplo. Atualizar a referencia se o arquivo mudar; historico nao e contrato vigente automaticamente.

## Decisoes e excecoes

Cada decisao implementada guarda escopo, propriedades, justificativa conhecida, fonte/data, revisao e consumidores. Excecao nomeia exatamente arquivos/modulos e aspectos diferentes; o restante herda o padrao. Mudanca de stack/convencao nao e correcao cosmetica. Observacao sem origem comprovada nao vira "aprovado pelo responsavel".

Perguntas e respostas a construir seguem a pasta temp prevista em construir, sem fila no TRD. Decisao construida fica neste dono ou no documento especifico por referencia. Preservar decisoes vigentes e atualizar o mesmo dono conforme o projeto cresce.

## Verificacao e fiscal

Registrar comandos reais por linguagem/efeito, runner/ambiente, referencia do candidato e limites. O fiscal compara TODO arquivo criado/modificado do lote com o perfil aplicavel, documentos e consumidores; ausencia de check/evidencia nao e PASSOU. Desvio corrigivel retorna a construcao e exige nova conferencia. Resultado de interface inclui suas variantes e estados.

Manter evidencias no registro existente. Nao criar certificado paralelo nem afirmar que um documento instala ferramentas ou garante obediencia do executor.
