# Arquitetura

O padrao e orientado a responsabilidades, nao a nomes obrigatorios de pastas.

Responsabilidades conceituais pertinentes:
- interface/apresentacao;
- entrada/transporte/sessao;
- normalizacao;
- regra de negocio e autorizacao;
- persistencia/contratos;
- integridade no banco;
- integracoes e efeitos externos.

Um projeto pode combinar ou nomear essas responsabilidades de outra forma. Preserve a arquitetura existente quando ela separa corretamente interesses, e crie uma divisao nova apenas quando houver motivo tecnico real.

Antes de arquivo novo: qual responsabilidade nova, equivalente existente, consumidor real, dono e forma de retirada segura?
