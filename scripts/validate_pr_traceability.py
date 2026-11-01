#!/usr/bin/env python3
"""Validação sintática mínima do PR. Não certifica DNA nem substitui revisão."""
import json, os, re, sys
from pathlib import Path
event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
pr = event.get("pull_request", {})
body = pr.get("body") or ""
required = ["## Issues relacionadas", "## Rastreabilidade", "## Evidências",
            "- DNA_IDs existentes:", "- Documentos donos e links:", "- Testes executados e resultados:"]
errors = [f"Campo ausente: {x}" for x in required if x not in body]
match = re.search(r"(?m)^- DNA_IDs existentes:\s*(.*)$", body)
if match and (not match.group(1).strip() or match.group(1).strip() in {"-", "N/A"}):
    errors.append("Informe DNA_IDs, DNA_PENDENTE justificado ou SEM_DNA_FUNCIONAL.")
if not re.search(r"(?i)(?:#\d+|https://github\.com/[^/]+/[^/]+/issues/\d+)", body):
    errors.append("Relacione uma Issue real no corpo do PR.")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Campos de rastreabilidade presentes; conferir conteúdo manualmente.")
