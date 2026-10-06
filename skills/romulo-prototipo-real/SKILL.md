---
name: romulo-prototipo-real
description: Use sempre que uma interface, fluxo ou regra aprovada em prototipo for convertida, integrada, publicada ou comparada com a implementacao real.
---

# Romulo Prototipo para Real

Prototipo especifica a mudanca aprovada; nao comprova backend, persistencia, seguranca ou publicacao.

Antes da conversao identifique: finalidade, usuario/tarefa, gatilho, campos/origem, validacoes, estados, contrato, autorizacao/escopo, efeitos/consumidores, erros/recuperacao, aceite e impacto pertinentes.

Compare somente a cadeia atingida. Preserve interface e regras aprovadas. Troque simulacoes pelos contratos reais necessarios. Nao redesenhe durante a integracao sem aprovacao.

Direcao dos dados: real -> prototipo, nunca prototipo -> real. Nao transporte contas, usuarios, lancamentos, anexos, IDs, valores de exemplo, fixtures, localStorage/sessionStorage ou banco de prototipo para producao.

Na versao real, sem cadastro real autorizado, mostre estado vazio. Nao invente fallback ficticio.

Mantenha como PENDENTE/NAO_VERIFICADO tudo que nao foi construido, testado ou publicado. Codigo local pronto nao significa producao ativa.

Antes de marcar REAL, retire fontes ficticias da cadeia publicada, teste o backend pertinente e confirme a separacao de dados.

## Complementos
Quando o usuario pedir exemplo de interface no chat, apresentar prototipo visual interativo e responsivo do recorte (campos, abas, estados e interacoes), nao desenho em texto. Apos aprovacao, implementar fielmente; divergencia exige aprovacao previa.

Campo so vem preenchido no real quando o valor foi efetivamente registrado e continua valido e autorizado; nunca selecionar opcao automaticamente. Verificar o cenario sem cadastro e confirmar que nenhum dado do prototipo foi gravado no banco oficial.

Opcao ficticia encontrada no real exige rastrear e corrigir a origem; nao autoriza apagar cadastros legitimos ou historico.

Nao apagar proposta aprovada pendente porque outra parte foi publicada.
