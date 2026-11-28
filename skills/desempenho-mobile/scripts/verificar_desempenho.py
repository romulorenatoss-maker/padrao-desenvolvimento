#!/usr/bin/env python3
"""Confere evidencias fornecidas e budgets; nao executa nem autentica medicoes."""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import sys

ID = re.compile(r"[a-z0-9][a-z0-9_.-]{0,79}")
SHA = re.compile(r"[a-f0-9]{40}")
SHA256 = re.compile(r"[a-f0-9]{64}")
CONDITIONS = ("unit", "scenario", "network", "dataset", "cache")
STATS = {"max", "p50", "p75", "p95", "p99"}
UNITS = {"ms", "bytes", "count", "ratio"}


class InvalidEvidence(ValueError):
    """Entrada inconsistente, incompleta ou sem evidencia conferivel."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidEvidence(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def finite_number(value: object) -> bool:
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value) and value >= 0
    except OverflowError:
        return False


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"chave JSON duplicada: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise InvalidEvidence(f"numero JSON nao finito: {value}")


def load_json(path: Path) -> tuple[dict, str]:
    require(path.stat().st_size <= 5 * 1024 * 1024, f"JSON maior que 5 MiB: {path.name}")
    raw = path.read_bytes()
    obj = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)
    require(isinstance(obj, dict), f"objeto JSON esperado: {path.name}")
    require(type(obj.get("schema_version")) is int and obj["schema_version"] == 1,
            f"schema_version invalida: {path.name}")
    return obj, hashlib.sha256(raw).hexdigest()


def index_items(items: object, label: str) -> dict[str, dict]:
    require(isinstance(items, list) and bool(items), f"{label}: lista vazia/ausente")
    indexed = {}
    for item in items:
        require(isinstance(item, dict), f"{label}: objeto esperado")
        key = item.get("id")
        require(isinstance(key, str) and ID.fullmatch(key) is not None,
                f"{label}: id invalido")
        require(key not in indexed, f"{label}: id duplicado: {key}")
        indexed[key] = item
    return indexed


def validate_profile(profile: dict) -> dict[str, dict]:
    require(profile.get("state") == "APROVADO", "perfil nao aprovado; exemplo/proposta nao certifica")
    require(nonempty(profile.get("profile_id")), "profile_id ausente")
    require(nonempty(profile.get("decision_ref")), "origem da decisao ausente")
    env = profile.get("environment")
    require(isinstance(env, dict), "environment ausente")
    for field in ("device", "os", "runtime"):
        require(nonempty(env.get(field)), f"environment.{field} ausente")
    require(type(env.get("physical_device")) is bool, "physical_device precisa ser booleano")
    physical = profile.get("require_physical_device")
    require(type(physical) is bool, "require_physical_device precisa ser booleano")
    require(not physical or env["physical_device"], "perfil exige aparelho fisico")
    require(finite_number(profile.get("max_regression_pct")), "max_regression_pct invalido")
    baseline = profile.get("baseline")
    require(isinstance(baseline, dict), "politica de baseline ausente")
    require(baseline.get("policy") in ("required", "initial"), "politica de baseline invalida")
    if baseline["policy"] == "initial":
        require(nonempty(baseline.get("reason")), "primeira medicao exige motivo registrado")
    else:
        for field, pattern in (("revision", SHA), ("profile_sha256", SHA256), ("report_sha256", SHA256)):
            value = baseline.get(field)
            require(isinstance(value, str) and pattern.fullmatch(value) is not None,
                    f"baseline.{field} invalido/ausente")
    checks = profile.get("required_checks")
    require(isinstance(checks, list) and bool(checks), "required_checks vazio/ausente")
    require(all(isinstance(x, str) and ID.fullmatch(x) for x in checks), "check id invalido")
    require(len(set(checks)) == len(checks), "required_checks duplicado")
    budgets = index_items(profile.get("budgets"), "budgets")
    for key, budget in budgets.items():
        require(budget.get("unit") in UNITS, f"{key}: unidade invalida")
        require(budget.get("stat") in STATS, f"{key}: estatistica invalida")
        require(finite_number(budget.get("limit")), f"{key}: limite invalido")
        samples = budget.get("min_samples")
        require(type(samples) is int and 1 <= samples <= 100000,
                f"{key}: min_samples invalido")
        for field in CONDITIONS:
            require(nonempty(budget.get(field)), f"{key}: {field} ausente")
    return budgets


def verify_artifacts(evidence: object, root: Path, label: str) -> None:
    require(isinstance(evidence, list) and bool(evidence), f"{label}: evidencia ausente")
    seen = set()
    for artifact in evidence:
        require(isinstance(artifact, dict), f"{label}: referencia de evidencia invalida")
        name, digest = artifact.get("path"), artifact.get("sha256")
        require(nonempty(name) and "\\" not in name and ":" not in name and "\x00" not in name,
                f"{label}: path invalido")
        relative = PurePosixPath(name)
        require(not relative.is_absolute() and ".." not in relative.parts and bool(relative.parts),
                f"{label}: path fora da raiz")
        require(name not in seen, f"{label}: evidencia duplicada")
        seen.add(name)
        require(isinstance(digest, str) and SHA256.fullmatch(digest) is not None,
                f"{label}: sha256 invalido")
        current = root
        for part in relative.parts:
            current = current / part
            require(not current.is_symlink(), f"{label}: symlink nao permitido")
        require(current.resolve().is_relative_to(root), f"{label}: path fora da raiz")
        require(current.is_file() and current.stat().st_size > 0,
                f"{label}: arquivo de evidencia ausente/vazio")
        actual = hashlib.sha256()
        with current.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                actual.update(block)
        require(actual.hexdigest() == digest, f"{label}: hash de evidencia divergente")


def statistic(samples: list[float], stat: str) -> float:
    values = sorted(samples)
    if stat == "max":
        return values[-1]
    rank = math.ceil(int(stat[1:]) * len(values) / 100)
    return values[rank - 1]


def inspect_report(report: dict, profile: dict, profile_hash: str, budgets: dict,
                   root: Path, revision: str | None, enforce: bool) -> tuple[dict, list[str]]:
    require(report.get("profile_id") == profile["profile_id"], "profile_id divergente")
    require(report.get("profile_sha256") == profile_hash, "hash do perfil divergente")
    actual_revision = report.get("revision")
    require(isinstance(actual_revision, str) and SHA.fullmatch(actual_revision) is not None,
            "revision precisa ser SHA completo")
    require(revision is None or actual_revision == revision, "revisao medida difere do candidato")
    require(nonempty(report.get("build_id")), "build_id ausente")
    require(report.get("build_mode") in ("release", "production"), "build nao e release/producao")
    require(report.get("evidence_type") == "MEASURED", "relatorio nao declara medicao real")
    require(report.get("environment") == profile["environment"], "ambiente/dispositivo divergente")
    require(type(report["environment"].get("physical_device")) is bool,
            "physical_device do relatorio invalido")
    when = report.get("measured_at")
    require(nonempty(when), "measured_at ausente")
    parsed_date = datetime.fromisoformat(when.replace("Z", "+00:00"))
    require(parsed_date.tzinfo is not None, "measured_at sem fuso horario")
    require(parsed_date <= datetime.now(timezone.utc) + timedelta(minutes=5),
            "measured_at no futuro (tolerancia de 5 minutos)")
    metrics = index_items(report.get("metrics"), "metrics")
    require(set(metrics) == set(budgets), "metricas faltantes ou nao previstas no perfil")
    values, errors = {}, []
    for key, budget in budgets.items():
        metric = metrics[key]
        for field in CONDITIONS:
            require(metric.get(field) == budget[field], f"{key}: condicao {field} divergente")
        samples = metric.get("samples")
        require(isinstance(samples, list) and budget["min_samples"] <= len(samples) <= 100000,
                f"{key}: numero de amostras insuficiente/invalido")
        require(all(finite_number(x) for x in samples), f"{key}: amostra invalida/nao finita")
        if budget["unit"] in ("count", "bytes"):
            require(all(type(x) is int for x in samples), f"{key}: count/bytes exigem inteiros")
        if budget["unit"] == "ratio":
            require(all(x <= 1 for x in samples), f"{key}: ratio precisa estar entre zero e um")
        verify_artifacts(metric.get("evidence"), root, key)
        value = statistic(samples, budget["stat"])
        values[key] = value
        if enforce and value > budget["limit"]:
            errors.append(f"{key}: {budget['stat']}={value:g} {budget['unit']} excede {budget['limit']:g}")
    if enforce:
        checks = index_items(report.get("checks"), "checks")
        require(set(checks) == set(profile["required_checks"]), "checks faltantes ou nao previstos")
        for key, check in checks.items():
            require(check.get("status") == "PASSOU", f"{key}: check nao passou/nao executado")
            verify_artifacts(check.get("evidence"), root, key)
    return values, errors


def evaluate(profile_path: Path, report_path: Path, revision: str, evidence_root: Path,
             baseline_path: Path | None = None) -> tuple[list[str], dict]:
    """Nao escreve, nao acessa rede e nao executa conteudo dos relatorios."""
    try:
        require(isinstance(revision, str) and SHA.fullmatch(revision) is not None,
                "--revision precisa ser SHA completo")
        require(not evidence_root.is_symlink(), "raiz de evidencias nao pode ser symlink")
        root = evidence_root.resolve()
        require(root.is_dir(), "raiz de evidencias ausente")
        profile, profile_hash = load_json(profile_path)
        budgets = validate_profile(profile)
        baseline_rule = profile["baseline"]
        require(baseline_path is not None or baseline_rule["policy"] == "initial",
                "baseline obrigatorio para comparar regressao")
        require(baseline_path is None or baseline_rule["policy"] == "required",
                "baseline fornecido sem vinculo aprovado no perfil")
        report, _ = load_json(report_path)
        values, errors = inspect_report(report, profile, profile_hash, budgets, root, revision, True)
        if baseline_path is not None:
            baseline, baseline_hash = load_json(baseline_path)
            require(baseline_hash == baseline_rule["report_sha256"], "hash do baseline divergente")
            previous, _ = inspect_report(baseline, profile, baseline_rule["profile_sha256"], budgets,
                                         root, baseline_rule["revision"], False)
            factor = 1 + profile["max_regression_pct"] / 100
            for key, value in values.items():
                if value > previous[key] * factor:
                    errors.append(f"{key}: regressao acima de {profile['max_regression_pct']:g}%")
        return errors, values
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, OverflowError) as exc:
        return [f"evidencia invalida: {exc}"], {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--evidence-root", required=True, type=Path)
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()
    errors, values = evaluate(args.profile, args.report, args.revision, args.evidence_root, args.baseline)
    for key, value in values.items():
        print(f"{key}: {value:g} (estatistica do perfil; percentil nearest rank)")
    if errors:
        print("FALHOU - evidencias/orcamentos")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASSOU - resultados fornecidos dentro do perfil aprovado.")
    if args.baseline is None:
        print("Primeira medicao conforme motivo no perfil; regressao nao comparada.")
    print("O fiscal deve conferir a origem dos traces; este script nao mede o app.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
