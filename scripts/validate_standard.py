#!/usr/bin/env python3
"""Valida distribuicao/roteamento textual; nao certifica host, IA ou bloqueio de escrita."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

NAME = "romulo-dev-standard"
MANIFESTS = ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")
SKILL_REF = re.compile(r"\bromulo-[a-z0-9]+(?:-[a-z0-9]+)*\b")
ROUTES = {
    "romulo-analisar": ("romulo-especificar", "romulo-interface", "romulo-verificar"),
    "romulo-construir": ("romulo-analisar", "romulo-especificar", "romulo-interface", "romulo-verificar"),
    "romulo-verificar": ("romulo-analisar", "romulo-especificar", "romulo-interface", "romulo-construir"),
    "romulo-iniciar-projeto": ("romulo-analisar", "romulo-especificar", "romulo-interface", "romulo-construir"),
    "romulo-prototipo-real": ("romulo-especificar", "romulo-interface", "romulo-verificar"),
    "romulo-documentacao": ("romulo-analisar", "romulo-especificar", "romulo-interface"),
    "romulo-auditar-projeto": ("romulo-analisar", "romulo-especificar", "romulo-interface"),
}
DOCS = ("README.md", "INSTALL.md", "AGENTS.md", "templates/AGENTS.md", "templates/CLAUDE.md",
        "references/ARQUITETURA.md", "references/DOCUMENTACAO.md", "references/DADOS.md",
        "references/SEGURANCA.md", "references/PROTOTIPO_REAL.md")


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("chave JSON duplicada")
        result[key] = value
    return result


def scalar(value: str) -> str:
    """Subset usado pelo pacote: escalares de uma linha, nao YAML geral."""
    if value.startswith('"'):
        parsed = json.loads(value)
        if not isinstance(parsed, str):
            raise ValueError("metadado nao textual")
        return parsed
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise ValueError("aspas incompletas")
        return value[1:-1].replace("''", "'")
    if not value or ": " in value or " #" in value or value in ("|", ">", "null", "true", "false"):
        raise ValueError("escalar ambiguo")
    return value


def validate(root: Path) -> list[str]:
    """Valida apenas arquivos do pacote, sem rede ou escrita."""
    root = root.resolve()
    errors: list[str] = []

    def safe_path(relative: str) -> Path:
        path = root / relative
        if not path.resolve().is_relative_to(root):
            raise ValueError("caminho fora da raiz")
        current = path
        while current != root:
            if current.is_symlink():
                raise ValueError("link simbolico nao aceito na distribuicao")
            if current.parent == current:
                raise ValueError("caminho invalido")
            current = current.parent
        return path

    def read(relative: str) -> str:
        return safe_path(relative).read_text(encoding="utf-8")

    def load(relative: str) -> dict:
        obj = json.loads(read(relative), object_pairs_hook=unique_object)
        if not isinstance(obj, dict):
            raise ValueError("objeto esperado")
        return obj

    manifests: dict[str, dict] = {}
    for relative in MANIFESTS:
        try:
            manifest = load(relative)
            if manifest.get("name") != NAME:
                errors.append(f"{relative}: nome divergente")
            version = manifest.get("version")
            if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
                errors.append(f"{relative}: versao invalida")
            if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
                errors.append(f"{relative}: descricao ausente")
            manifests[relative] = manifest
        except (OSError, UnicodeError, ValueError):
            errors.append(f"{relative}: ausente, ilegivel ou JSON invalido")
    versions = [m.get("version") for m in manifests.values()]
    if versions and any(v != versions[0] for v in versions):
        errors.append("manifests: versoes divergentes")
    version = manifests.get("plugin.json", {}).get("version")
    if manifests.get(".codex-plugin/plugin.json", {}).get("skills") != "./skills/":
        errors.append(".codex-plugin/plugin.json: diretorio de skills divergente")

    for relative, expected in ((".agents/plugins/marketplace.json", {"source": "local", "path": "./"}),
                               (".claude-plugin/marketplace.json", "./")):
        try:
            catalog = load(relative)
            entries = catalog.get("plugins")
            if catalog.get("name") != NAME or not isinstance(entries, list) or len(entries) != 1:
                raise ValueError("catalogo invalido")
            if not isinstance(entries[0], dict) or entries[0].get("name") != NAME or entries[0].get("source") != expected:
                raise ValueError("plugin/raiz divergentes")
        except (OSError, UnicodeError, ValueError, TypeError):
            errors.append(f"{relative}: marketplace invalido")

    skills: dict[str, str] = {}
    try:
        directory = safe_path("skills")
        folders = sorted(directory.iterdir())
    except (OSError, ValueError):
        folders = []
        errors.append("skills: diretorio ausente/ilegivel")
    for folder in folders:
        if not folder.is_dir() or folder.is_symlink():
            errors.append(f"skills/{folder.name}: pasta de skill esperada")
            continue
        relative = f"skills/{folder.name}/SKILL.md"
        try:
            text = read(relative)
            parts = text.split("---\n", 2)
            if len(parts) != 3 or parts[0] or not parts[2].strip():
                raise ValueError("frontmatter/corpo ausente")
            fields: dict[str, str] = {}
            for line in parts[1].strip().splitlines():
                key, separator, value = line.partition(": ")
                if not separator or key in fields:
                    raise ValueError("metadado invalido/duplicado")
                fields[key] = scalar(value.strip())
            if fields.get("name") != folder.name or not re.fullmatch(r"romulo-[a-z0-9]+(?:-[a-z0-9]+)*", folder.name):
                raise ValueError("nome divergente")
            if not 1 <= len(fields.get("description", "").strip()) <= 1024:
                raise ValueError("descricao invalida")
            skills[folder.name] = text
        except (OSError, UnicodeError, ValueError):
            errors.append(f"{relative}: corpo/metadados invalidos ou ausentes")
    if not skills:
        errors.append("skills: nenhuma skill valida")

    docs: dict[str, str] = {}
    for relative in DOCS:
        try:
            docs[relative] = read(relative)
        except (OSError, UnicodeError, ValueError):
            errors.append(f"{relative}: ausente/ilegivel")
    readme = docs.get("README.md", "")
    rows = re.findall(r"^\| \[(romulo-[a-z0-9-]+)\]\((skills/[^)]+)\) \| ([^|]+) \| ([^|]+) \|$", readme, re.M)
    names = [row[0] for row in rows]
    if set(names) != set(skills) or len(names) != len(set(names)):
        errors.append("README.md: catalogo nominal divergente/duplicado")
    for name, path, trigger, responsibility in rows:
        if path != f"skills/{name}/SKILL.md" or not trigger.strip() or not responsibility.strip():
            errors.append(f"README.md: destino/gatilho/responsabilidade invalidos para {name}")
    if not isinstance(version, str) or f"Versao: {version}" not in readme:
        errors.append("README.md: versao divergente")

    template = docs.get("templates/AGENTS.md", "")
    required_fields = ("PROJETO:", "REPOSITORIO_OFICIAL:", "BRANCH_OFICIAL:", "DOCUMENTACAO_LOCAL:",
                       "PROTECOES_LOCAIS:", f"PADRAO_REPOSITORIO: https://github.com/romulorenatoss-maker/{NAME}",
                       "PADRAO_REF: main", "PADRAO_ENTRADA: README.md")
    if any(field not in template for field in required_fields):
        errors.append("templates/AGENTS.md: identidade/ponte/protecao incompleta")
    if len(template.splitlines()) > 40 or set(SKILL_REF.findall(template)) - {NAME}:
        errors.append("templates/AGENTS.md: deixou de ser minimo ou duplicou skills")
    if re.search(r"\b\d+ skills\b|VERSAO_MINIMA|plugin (?:install|add|update|marketplace)", template):
        errors.append("templates/AGENTS.md: catalogo/instalacao/versao duplicados")
    if "0393" not in template or "protecoes locais" not in template.lower():
        errors.append("templates/AGENTS.md: protecao ausente")
    if docs.get("templates/CLAUDE.md", "") != "@AGENTS.md\n":
        errors.append("templates/CLAUDE.md: ponte deve ser @AGENTS.md e quebra de linha")
    if "README.md" not in docs.get("AGENTS.md", "") or "templates/AGENTS.md" not in docs.get("AGENTS.md", ""):
        errors.append("AGENTS.md: dono central/template nao distinguidos")
    if not re.search(r"\[README.md\]\(README.md\)", docs.get("INSTALL.md", "")):
        errors.append("INSTALL.md: nao aponta para catalogo central")
    if re.search(r"^- romulo-[a-z0-9-]+\s*$", docs.get("INSTALL.md", ""), re.M):
        errors.append("INSTALL.md: catalogo duplicado")

    texts = {**docs, **{f"skills/{n}/SKILL.md": t for n, t in skills.items()}}
    for name in skills:
        for resource in (root / "skills" / name).rglob("*.md"):
            relative = resource.relative_to(root).as_posix()
            if relative in texts:
                continue
            try:
                texts[relative] = read(relative)
            except (OSError, UnicodeError, ValueError):
                errors.append(f"{relative}: recurso ausente/ilegivel ou inseguro")
    for relative, text in texts.items():
        unknown = set(SKILL_REF.findall(text)) - set(skills) - {NAME}
        if unknown:
            errors.append(f"{relative}: skill desconhecida: {', '.join(sorted(unknown))}")
        for count in re.findall(r"\b(\d+) skills\b", text):
            if int(count) != len(skills):
                errors.append(f"{relative}: contagem desatualizada")
        for link in re.findall(r"\[[^\]]*\]\(([^ )]+)\)", text):
            if "://" in link or link.startswith("#"):
                continue
            target = (Path(relative).parent / link.split("#", 1)[0]).as_posix()
            try:
                if not safe_path(target).is_file():
                    raise ValueError("alvo nao e arquivo")
            except (OSError, ValueError):
                errors.append(f"{relative}: link local invalido: {link}")
    for owner, targets in ROUTES.items():
        for target in targets:
            if target not in skills or f"`{target}`" not in skills.get(owner, ""):
                errors.append(f"roteamento: {owner} nao referencia {target}")
    for name, fragments in {
        "romulo-analisar": ("SEM_PREVISAO_NA_SKILL", "0393", "../../references/ARQUITETURA.md"),
        "romulo-iniciar-projeto": ("../../templates/AGENTS.md", "../../templates/CLAUDE.md", "0393"),
        "romulo-auditar-projeto": ("../../references/ARQUITETURA.md", "../../references/DOCUMENTACAO.md"),
        "romulo-documentacao": ("../../references/DOCUMENTACAO.md",),
    }.items():
        if any(fragment not in skills.get(name, "") for fragment in fragments):
            errors.append(f"{name}: referencia/gate obrigatorio ausente")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("FALHOU — validacao estrutural")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASSOU — manifests, catalogo central, skills, templates, links e roteamento textual.")
    print("Nao certifica ativacao no host, comportamento do agente, telas ou bloqueio universal de escrita.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
