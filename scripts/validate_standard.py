#!/usr/bin/env python3
"""Valida a distribuicao local; nao instala plugins nem certifica comportamento de IA/UI."""
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
    "romulo-analisar": ("romulo-especificar", "romulo-interface"),
    "romulo-construir": ("romulo-especificar", "romulo-interface", "romulo-verificar"),
    "romulo-verificar": ("romulo-especificar", "romulo-interface", "romulo-construir"),
    "romulo-iniciar-projeto": ("romulo-especificar", "romulo-interface", "romulo-construir"),
    "romulo-prototipo-real": ("romulo-especificar", "romulo-interface", "romulo-verificar"),
    "romulo-documentacao": ("romulo-especificar", "romulo-interface"),
    "romulo-auditar-projeto": ("romulo-especificar", "romulo-interface"),
}


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    """JSON com chave duplicada nao pode mascarar configuracao."""
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("chave JSON duplicada")
        result[key] = value
    return result


def scalar(value: str) -> str:
    """Subset de metadados usado aqui: escalares de uma linha, nao um parser YAML geral."""
    if value.startswith('"'):
        parsed = json.loads(value)
        if not isinstance(parsed, str):
            raise ValueError("metadado deve ser texto")
        return parsed
    if value.startswith("'"):
        if not value.endswith("'") or len(value) < 2:
            raise ValueError("aspas incompletas")
        return value[1:-1].replace("''", "'")
    if not value or ": " in value or " #" in value or value in ("|", ">"):
        raise ValueError("escalar ambiguo: usar texto entre aspas em uma linha")
    return value


def validate(root: Path) -> list[str]:
    """Retorna divergencias estruturais sem rede, escrita ou execucao de arquivos do pacote."""
    root = root.resolve()
    errors: list[str] = []

    def read(relative: str) -> str:
        path = root / relative
        if not path.resolve().is_relative_to(root):
            raise ValueError("caminho fora da raiz")
        return path.read_text(encoding="utf-8")

    def load(relative: str) -> dict:
        obj = json.loads(read(relative), object_pairs_hook=unique_object)
        if not isinstance(obj, dict):
            raise ValueError("objeto JSON esperado")
        return obj

    manifests: list[dict] = []
    for relative in MANIFESTS:
        try:
            manifest = load(relative)
            if manifest.get("name") != NAME:
                errors.append(f"{relative}: nome do plugin divergente")
            version = manifest.get("version", "")
            if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
                errors.append(f"{relative}: versao invalida")
            if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
                errors.append(f"{relative}: descricao ausente")
            manifests.append(manifest)
        except (OSError, UnicodeError, ValueError):
            errors.append(f"{relative}: ausente, ilegivel ou JSON invalido")
    versions = [m.get("version") for m in manifests]
    if versions and any(v != versions[0] for v in versions):
        errors.append("manifests: versoes divergentes")
    version = versions[0] if versions and isinstance(versions[0], str) else ""
    if len(manifests) == 3 and manifests[2].get("skills") != "./skills/":
        errors.append(".codex-plugin/plugin.json: diretorio de skills divergente")

    for path, is_codex in ((".agents/plugins/marketplace.json", True),
                           (".claude-plugin/marketplace.json", False)):
        try:
            catalog = load(path)
            entries = catalog.get("plugins", [])
            if catalog.get("name") != NAME or not isinstance(entries, list) or len(entries) != 1:
                raise ValueError("catalogo divergente")
            entry = entries[0]
            if not isinstance(entry, dict) or entry.get("name") != NAME:
                raise ValueError("entrada divergente")
            expected = {"source": "local", "path": "./"} if is_codex else "./"
            if entry.get("source") != expected:
                raise ValueError("raiz do plugin divergente")
        except (OSError, UnicodeError, ValueError, TypeError):
            errors.append(f"{path}: marketplace invalido ou raiz incorreta")

    skills: dict[str, str] = {}
    directory = root / "skills"
    if not directory.is_dir() or directory.is_symlink():
        errors.append("skills: diretorio ausente ou link simbolico")
    else:
        for folder in sorted(directory.iterdir()):
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
                    raise ValueError("descricao ausente ou longa")
                skills[folder.name] = text
            except (OSError, UnicodeError, ValueError):
                errors.append(f"{relative}: corpo/metadados invalidos ou ausentes")
    if not skills:
        errors.append("skills: nenhuma skill valida")

    docs: dict[str, str] = {}
    for relative in ("README.md", "INSTALL.md", "templates/AGENTS.md", "AGENTS.md", "templates/CLAUDE.md"):
        try:
            docs[relative] = read(relative)
        except (OSError, UnicodeError, ValueError):
            errors.append(f"{relative}: ausente ou ilegivel")
    for relative in ("README.md", "INSTALL.md"):
        listed = re.findall(r"^- (romulo-[a-z0-9-]+)\s*$", docs.get(relative, ""), re.M)
        if set(listed) != set(skills) or len(listed) != len(set(listed)):
            errors.append(f"{relative}: lista nominal de skills divergente")
    if version and f"Versao: {version}" not in docs.get("README.md", ""):
        errors.append("README.md: versao divergente")
    if version and f"VERSAO_MINIMA_ROMULO_STANDARD: {version}" not in docs.get("templates/AGENTS.md", ""):
        errors.append("templates/AGENTS.md: versao minima divergente")
    if docs.get("templates/CLAUDE.md", "").strip() != "@AGENTS.md":
        errors.append("templates/CLAUDE.md: deve apontar somente para AGENTS.md")
    for name in skills:
        if f"`{name}`" not in docs.get("templates/AGENTS.md", ""):
            errors.append(f"templates/AGENTS.md: skill nao declarada: {name}")
    for relative, text in {**docs, **{f"skills/{n}/SKILL.md": t for n, t in skills.items()}}.items():
        unknown = set(SKILL_REF.findall(text)) - set(skills) - {NAME}
        if unknown:
            errors.append(f"{relative}: referencia a skill desconhecida: {', '.join(sorted(unknown))}")
        for count in re.findall(r"\b(\d+) skills\b", text):
            if int(count) != len(skills):
                errors.append(f"{relative}: contagem de skills desatualizada")
        for link in re.findall(r"\[[^\]]*\]\(([^ )]+)\)", text):
            if "://" in link or link.startswith("#"):
                continue
            target = (root / relative).parent / link.split("#", 1)[0]
            if not target.resolve().is_relative_to(root) or not target.is_file():
                errors.append(f"{relative}: link local invalido")
    for owner, targets in ROUTES.items():
        for target in targets:
            if target not in skills or f"`{target}`" not in skills.get(owner, ""):
                errors.append(f"roteamento: {owner} nao referencia {target}")
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
    print("PASSOU — estrutura, manifests, catalogos, versoes, skills e roteamento textual.")
    print("Nao certifica ativacao no host, comportamento do agente ou telas de consumidores.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
