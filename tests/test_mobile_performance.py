"""Cenarios do avaliador com fixtures sinteticas; nao medem um app."""
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/desempenho-mobile"
SCRIPT = SKILL / "scripts/verificar_desempenho.py"
SPEC = importlib.util.spec_from_file_location("mobile_performance", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        clock_patch = mock.patch.object(MODULE, "datetime", wraps=datetime)
        clock = clock_patch.start()
        self.addCleanup(clock_patch.stop)
        clock.now.return_value = datetime(2020, 1, 1, 12, tzinfo=timezone.utc)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.evidence_root = self.root / "artifacts"
        self.evidence_root.mkdir()
        trace = self.evidence_root / "trace.json"
        trace.write_text('{"fixture": "unit test only"}\n', encoding="utf-8")
        self.artifact = {"path": "trace.json", "sha256": hashlib.sha256(trace.read_bytes()).hexdigest()}
        self.revision = "a" * 40
        self.environment = {"device": "fixture-device", "os": "fixture-os",
                            "runtime": "fixture-runtime", "physical_device": True}
        self.budget = {"id": "abertura", "unit": "ms", "stat": "p95", "limit": 1500,
                       "min_samples": 20, "scenario": "cold-local", "network": "offline",
                       "dataset": "fixture-large", "cache": "process-cold"}
        self.profile = {"schema_version": 1, "profile_id": "fixture", "state": "APROVADO",
                        "decision_ref": "unit-test-fixture-only", "require_physical_device": True,
                        "environment": self.environment, "max_regression_pct": 10,
                        "baseline": {"policy": "initial", "reason": "first unit-test fixture"},
                        "budgets": [self.budget], "required_checks": ["durabilidade"]}
        self.profile_path = self.root / "profile.json"
        self.report_path = self.root / "report.json"
        self.write_profile()
        metric = {key: self.budget[key] for key in ("id", *MODULE.CONDITIONS)}
        metric.update(samples=[1000] * 20, evidence=[self.artifact])
        self.report = {
            "schema_version": 1, "profile_id": "fixture", "profile_sha256": self.profile_hash(),
            "revision": self.revision, "build_id": "fixture-release", "build_mode": "release",
            "evidence_type": "MEASURED", "environment": self.environment,
            "measured_at": "2020-01-01T08:00:00-03:00", "metrics": [metric],
            "checks": [{"id": "durabilidade", "status": "PASSOU", "evidence": [self.artifact]}],
        }

    def write_profile(self):
        self.profile_path.write_text(json.dumps(self.profile), encoding="utf-8")

    def profile_hash(self):
        return hashlib.sha256(self.profile_path.read_bytes()).hexdigest()

    def bind_baseline(self, baseline):
        self.profile["baseline"] = {
            "policy": "required", "revision": baseline["revision"],
            "profile_sha256": baseline["profile_sha256"],
            "report_sha256": hashlib.sha256(json.dumps(baseline).encode()).hexdigest(),
        }
        self.write_profile()
        self.report["profile_sha256"] = self.profile_hash()

    def run_case(self, report=None, baseline=None):
        self.report_path.write_text(json.dumps(self.report if report is None else report), encoding="utf-8")
        baseline_path = None
        if baseline is not None:
            baseline_path = self.root / "baseline.json"
            baseline_path.write_text(json.dumps(baseline), encoding="utf-8")
        return MODULE.evaluate(self.profile_path, self.report_path, self.revision,
                               self.evidence_root, baseline_path)

    def test_matching_measurements_and_artifacts_pass(self):
        errors, values = self.run_case()
        self.assertEqual(errors, [])
        self.assertEqual(values, {"abertura": 1000})

    def test_percentile_is_computed_from_all_samples(self):
        self.report["metrics"][0]["samples"] = list(range(1, 21))
        errors, values = self.run_case()
        self.assertEqual(errors, [])
        self.assertEqual(values["abertura"], 19)

    def test_slow_tail_fails_even_if_mean_would_pass(self):
        self.report["metrics"][0]["samples"] = [100] * 18 + [2000, 3000]
        errors, values = self.run_case()
        self.assertTrue(any("excede" in e for e in errors))
        self.assertEqual(values["abertura"], 2000)

    def test_missing_metrics_and_duplicate_ids_fail(self):
        for metrics in ([], [self.report["metrics"][0]] * 2):
            with self.subTest(metrics=len(metrics)):
                candidate = copy.deepcopy(self.report)
                candidate["metrics"] = metrics
                self.assertTrue(self.run_case(candidate)[0])

    def test_insufficient_or_invalid_samples_fail(self):
        for samples in ([100], [True] * 20, [-1] * 20, ["100"] * 20,
                        [float("nan")] * 20, [float("inf")] * 20, [None] * 20):
            with self.subTest(sample=repr(samples[0])):
                candidate = copy.deepcopy(self.report)
                candidate["metrics"][0]["samples"] = samples
                self.assertTrue(self.run_case(candidate)[0])

    def test_candidate_revision_and_profile_are_bound(self):
        for field, value in (("revision", "b" * 40), ("profile_sha256", "0" * 64),
                             ("profile_id", "another-profile")):
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.report)
                candidate[field] = value
                self.assertTrue(self.run_case(candidate)[0])

    def test_different_conditions_cannot_claim_same_result(self):
        for field in MODULE.CONDITIONS:
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.report)
                candidate["metrics"][0][field] = "other"
                self.assertTrue(self.run_case(candidate)[0])

    def test_debug_mock_and_different_device_fail(self):
        for field, value in (("build_mode", "debug"), ("evidence_type", "EXAMPLE"),
                             ("environment", {"device": "desktop"}), ("build_id", ""),
                             ("measured_at", "2026-11-28T00:00:00"),
                             ("measured_at", "invalid")):
            with self.subTest(field=field, value=value):
                candidate = copy.deepcopy(self.report)
                candidate[field] = value
                self.assertTrue(self.run_case(candidate)[0])

    def test_future_measurement_fails_with_controlled_clock(self):
        self.report["measured_at"] = "2020-01-01T12:06:00+00:00"
        self.assertTrue(any("futuro" in e for e in self.run_case()[0]))
        self.report["measured_at"] = "2020-01-01T12:04:00+00:00"
        self.assertEqual(self.run_case()[0], [])

    def test_discrete_units_and_fraction_ratios(self):
        for unit, invalid in (("count", 0.5), ("bytes", 0.5), ("ratio", 1.1)):
            with self.subTest(unit=unit):
                self.profile["budgets"][0]["unit"] = unit
                self.write_profile()
                self.report["profile_sha256"] = self.profile_hash()
                self.report["metrics"][0]["unit"] = unit
                self.report["metrics"][0]["samples"] = [invalid] * 20
                self.assertTrue(self.run_case()[0])

    def test_unexecuted_failed_missing_and_duplicate_checks_fail(self):
        for checks in ([], [self.report["checks"][0]] * 2,
                       [{"id": "durabilidade", "status": "NAO_EXECUTADO", "evidence": [self.artifact]}],
                       [{"id": "durabilidade", "status": "FALHOU", "evidence": [self.artifact]}]):
            with self.subTest(checks=checks):
                candidate = copy.deepcopy(self.report)
                candidate["checks"] = checks
                self.assertTrue(self.run_case(candidate)[0])

    def test_missing_or_changed_evidence_fails(self):
        for evidence in ([], [{"path": "missing.json", "sha256": self.artifact["sha256"]}],
                         [{"path": "trace.json", "sha256": "0" * 64}]):
            with self.subTest(evidence=evidence):
                candidate = copy.deepcopy(self.report)
                candidate["metrics"][0]["evidence"] = evidence
                self.assertTrue(self.run_case(candidate)[0])
        (self.evidence_root / "trace.json").write_text("changed", encoding="utf-8")
        self.assertTrue(self.run_case()[0])

    def test_external_and_symlink_artifacts_fail(self):
        for name in ("../profile.json", str(self.profile_path), "C:\\private\\trace.json"):
            with self.subTest(name=name):
                candidate = copy.deepcopy(self.report)
                candidate["metrics"][0]["evidence"] = [{"path": name, "sha256": self.artifact["sha256"]}]
                self.assertTrue(self.run_case(candidate)[0])
        link = self.evidence_root / "link.json"
        try:
            link.symlink_to(self.evidence_root / "trace.json")
        except (OSError, NotImplementedError):
            self.skipTest("symlink indisponivel")
        candidate = copy.deepcopy(self.report)
        candidate["metrics"][0]["evidence"] = [{"path": "link.json", "sha256": self.artifact["sha256"]}]
        self.assertTrue(self.run_case(candidate)[0])

    def test_proposed_example_is_rejected(self):
        self.run_case()
        errors, _ = MODULE.evaluate(SKILL / "assets/perfil-desempenho.exemplo.json",
                                    self.report_path, self.revision, self.evidence_root)
        self.assertTrue(any("nao aprovado" in e for e in errors), errors)

    def test_invalid_profile_fails(self):
        original = copy.deepcopy(self.profile)
        for field, value in (("state", "PROPOSTO"), ("decision_ref", ""), ("budgets", []),
                             ("required_checks", []), ("required_checks", ["same", "same"]),
                             ("max_regression_pct", -1), ("require_physical_device", 1),
                             ("baseline", None), ("baseline", {"policy": "required"}),
                             ("baseline", {"policy": "initial", "reason": ""})):
            with self.subTest(field=field):
                self.profile = copy.deepcopy(original)
                self.profile[field] = value
                self.write_profile()
                self.assertTrue(self.run_case()[0])

    def test_physical_device_requirement_is_enforced(self):
        self.profile["environment"]["physical_device"] = False
        self.write_profile()
        self.report["profile_sha256"] = self.profile_hash()
        self.assertTrue(self.run_case()[0])

    def test_approved_budget_change_invalidates_old_report(self):
        self.profile["budgets"][0]["limit"] = 9999
        self.write_profile()
        self.assertTrue(self.run_case()[0])

    def test_regression_fails_below_absolute_budget(self):
        baseline = copy.deepcopy(self.report)
        baseline["revision"] = "b" * 40
        baseline["metrics"][0]["samples"] = [800] * 20
        self.bind_baseline(baseline)
        errors, _ = self.run_case(baseline=baseline)
        self.assertTrue(any("regressao" in e for e in errors), errors)

    def test_slow_baseline_is_allowed_for_honest_improvement(self):
        baseline = copy.deepcopy(self.report)
        baseline["revision"] = "b" * 40
        baseline["metrics"][0]["samples"] = [3000] * 20
        baseline.pop("checks")
        self.bind_baseline(baseline)
        self.assertEqual(self.run_case(baseline=baseline)[0], [])

    def test_baseline_conditions_must_match(self):
        baseline = copy.deepcopy(self.report)
        baseline["metrics"][0]["cache"] = "warm"
        self.bind_baseline(baseline)
        self.assertTrue(self.run_case(baseline=baseline)[0])

    def test_required_baseline_cannot_be_omitted_or_substituted(self):
        baseline = copy.deepcopy(self.report)
        baseline["revision"] = "b" * 40
        self.bind_baseline(baseline)
        self.assertTrue(any("baseline obrigatorio" in e for e in self.run_case()[0]))
        baseline["metrics"][0]["samples"] = [1200] * 20
        self.assertTrue(any("hash do baseline" in e for e in self.run_case(baseline=baseline)[0]))

    def test_initial_profile_cannot_claim_unapproved_comparison(self):
        baseline = copy.deepcopy(self.report)
        self.assertTrue(any("sem vinculo aprovado" in e for e in self.run_case(baseline=baseline)[0]))

    def test_duplicate_keys_and_malformed_json_fail_closed(self):
        self.run_case()
        for raw in ('{"schema_version": 1, "schema_version": 1}', "[]", "{", "null"):
            with self.subTest(raw=raw):
                self.report_path.write_text(raw, encoding="utf-8")
                errors, _ = MODULE.evaluate(self.profile_path, self.report_path, self.revision, self.evidence_root)
                self.assertTrue(errors)

    def test_cli_reports_success_and_failure(self):
        self.run_case()
        command = [sys.executable, str(SCRIPT), "--profile", str(self.profile_path),
                   "--report", str(self.report_path), "--revision", self.revision,
                   "--evidence-root", str(self.evidence_root)]
        good = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        self.assertIn("nao mede o app", good.stdout)
        (self.evidence_root / "trace.json").unlink()
        bad = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(bad.returncode, 1, bad.stdout + bad.stderr)


if __name__ == "__main__":
    unittest.main()
