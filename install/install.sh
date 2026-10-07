#!/usr/bin/env bash
# Verificacao somente leitura; instalacao/migracao sao definidas no INSTALL.md.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ "$#" -ne 0 ]; then
  printf '%s\n' 'Flags legadas de copia/criacao recusadas. Leia INSTALL.md; nenhum arquivo foi alterado.' >&2
  exit 2
fi
export PYTHONDONTWRITEBYTECODE=1
if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/scripts/validate_standard.py"
elif command -v python >/dev/null 2>&1; then
  python "$ROOT/scripts/validate_standard.py"
else
  printf '%s\n' 'Python 3.10+ necessario para validar; instalacao nao foi executada.' >&2
  exit 2
fi
printf '%s\n' 'Validacao do pacote concluida; instalacao e migracao seguem INSTALL.md. Nenhum arquivo de projeto foi copiado.'
