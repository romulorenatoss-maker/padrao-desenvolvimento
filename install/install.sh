#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT="${1:-.}"

install_skills() {
  for target in "$HOME/.agents/skills" "$HOME/.claude/skills"; do
    mkdir -p "$target"
    for skill in "$ROOT"/skills/*; do
      [ -d "$skill" ] || continue
      mkdir -p "$target/$(basename "$skill")"
      cp "$skill/SKILL.md" "$target/$(basename "$skill")/SKILL.md"
    done
  done
}

init_project() {
  if [ -e "$PROJECT/AGENTS.md" ]; then
    echo "AGENTS.md existente: NAO ALTERADO."
  else
    cp "$ROOT/templates/AGENTS.md" "$PROJECT/AGENTS.md"
  fi
  if [ -e "$PROJECT/CLAUDE.md" ]; then
    echo "CLAUDE.md existente: NAO ALTERADO."
  else
    cp "$ROOT/templates/CLAUDE.md" "$PROJECT/CLAUDE.md"
  fi
}

case "${2:-all}" in
  skills) install_skills ;;
  project) init_project ;;
  all) install_skills; init_project ;;
  *) echo "Uso: install.sh <projeto> [skills|project|all]"; exit 2 ;;
esac
