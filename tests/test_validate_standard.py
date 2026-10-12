"""Testes positivos/negativos da distribuicao, nao avaliacao de modelos ou UI."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.validate_standard import validate

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))

    def edit(self, relative, before, after):
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(before, text)
        path.write_text(text.replace(before, after), encoding="utf-8")

    def assert_mutations_fail(self, cases):
        for relative, before, after in cases:
            with self.subTest(relative=relative, before=before):
                path = self.root / relative
                original = path.read_text(encoding="utf-8")
                self.edit(relative, before, after)
                self.assertTrue(validate(self.root))
                path.write_text(original, encoding="utf-8")

    def test_distribution_passes(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_skill_fails(self):
        shutil.rmtree(self.root / "skills/romulo-interface")
        self.assertTrue(validate(self.root))

    def test_invalid_metadata_fails(self):
        self.assert_mutations_fail([
            ("skills/romulo-interface/SKILL.md", "name: romulo-interface", "name: romulo-outro"),
            ("skills/romulo-interface/SKILL.md", 'description: "', 'description "'),
        ])

    def test_duplicate_metadata_fails(self):
        self.edit("skills/romulo-interface/SKILL.md", "name: romulo-interface", "name: romulo-interface\nname: romulo-interface")
        self.assertTrue(validate(self.root))

    def test_missing_frontmatter_and_body_fail(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        original = path.read_text(encoding="utf-8")
        for text in (original.replace("---\n", "", 1), original.split("---\n", 2)[0] + "---\nname: romulo-interface\ndescription: ok\n---\n"):
            with self.subTest(text=text[:40]):
                path.write_text(text, encoding="utf-8")
                self.assertTrue(validate(self.root))

    def test_empty_description_fails(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[2] = 'description: ""'
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_quoted_colon_is_valid(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[2] = 'description: "Texto valido: com dois pontos"'
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertEqual(validate(self.root), [])

    def test_unquoted_colon_fails(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[2] = "description: Texto invalido: valor"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_manifests_and_catalogs_fail_on_invalid_configuration(self):
        version = json.loads((self.root / "plugin.json").read_text())["version"]
        self.assert_mutations_fail([
            ("plugin.json", f'"version": "{version}"', '"version": "0.0.0"'),
            ("plugin.json", f'"version": "{version}"', '"version": null'),
            ("plugin.json", '"name": "romulo-dev-standard"', '"name": "outro"'),
            ("plugin.json", '"name": "romulo-dev-standard"', '"name": "x", "name": "romulo-dev-standard"'),
            (".codex-plugin/plugin.json", '"skills": "./skills/"', '"skills": "./ausente/"'),
            (".agents/plugins/marketplace.json", '"path": "./"', '"path": "../"'),
            (".claude-plugin/marketplace.json", '"source": "./"', '"source": "./outro"'),
        ])

    def test_missing_manifest_fails(self):
        (self.root / "plugin.json").unlink()
        self.assertTrue(validate(self.root))

    def test_invalid_json_fails(self):
        for text in ("{", "[]", "null"):
            with self.subTest(text=text):
                (self.root / "plugin.json").write_text(text, encoding="utf-8")
                self.assertTrue(validate(self.root))

    def test_catalog_requires_all_skills_once(self):
        path = self.root / "README.md"
        original = path.read_text(encoding="utf-8")
        row = next(line for line in original.splitlines(True) if line.startswith("| [romulo-interface]"))
        for replacement in ("", row + row):
            with self.subTest(replacement=bool(replacement)):
                path.write_text(original.replace(row, replacement), encoding="utf-8")
                self.assertTrue(validate(self.root))

    def test_catalog_wrong_destination_fails(self):
        self.edit("README.md", "[romulo-interface](skills/romulo-interface/SKILL.md)", "[romulo-interface](skills/romulo-construir/SKILL.md)")
        self.assertTrue(validate(self.root))

    def test_readme_version_mismatch_fails(self):
        version = json.loads((self.root / "plugin.json").read_text())["version"]
        self.edit("README.md", f"Versao: {version}", "Versao: 0.0.0")
        self.assertTrue(validate(self.root))

    def test_template_must_be_minimal_and_unversioned(self):
        path = self.root / "templates/AGENTS.md"
        original = path.read_text(encoding="utf-8")
        for extra in ("\n- romulo-interface\n", "\n11 skills\n", "\nVERSAO_MINIMA: 1.5.0\n", "\n" * 45):
            with self.subTest(extra=extra[:30]):
                path.write_text(original + extra, encoding="utf-8")
                self.assertTrue(validate(self.root))

    def test_template_identity_and_pointer_required(self):
        self.assert_mutations_fail([
            ("templates/AGENTS.md", "PADRAO_ENTRADA: README.md", "PADRAO_ENTRADA: AGENTS.md"),
            ("templates/AGENTS.md", "PROTECOES_LOCAIS:", "OUTRO:"),
            ("templates/AGENTS.md", "0393", ""),
        ])

    def test_claude_must_only_import_agents(self):
        path = self.root / "templates/CLAUDE.md"
        for text in ("@README.md\n", "@AGENTS.md\nOutra regra\n", "`@AGENTS.md`\n", "@AGENTS.md"):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                self.assertTrue(validate(self.root))

    def test_install_must_reference_central_catalog(self):
        self.assert_mutations_fail([("INSTALL.md", "[README.md](README.md)", "README.md")])
        path = self.root / "INSTALL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n- romulo-interface\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_unknown_skill_and_broken_links_fail(self):
        self.assert_mutations_fail([
            ("skills/romulo-construir/SKILL.md", "`romulo-interface`", "`romulo-fantasma`"),
            ("README.md", "[INSTALL.md](INSTALL.md)", "[INSTALL.md](nao-existe.md)"),
            ("README.md", "[INSTALL.md](INSTALL.md)", "[INSTALL.md](../../outside.md)"),
        ])

    def test_missing_reference_fails(self):
        (self.root / "references/ARQUITETURA.md").unlink()
        self.assertTrue(validate(self.root))

    def test_motion_package_resources_and_license_required(self):
        paths = ("LICENSE", "workflows/create.md", "workflows/audit.md",
                 "references/motion-cookbook.md", "references/demo-shell.html")
        for relative in paths:
            with self.subTest(relative=relative):
                path = self.root / "skills/romulo-motion-principles" / relative
                content = path.read_bytes()
                path.unlink()
                self.assertTrue(validate(self.root))
                path.write_bytes(content)

    def test_nested_skill_reference_link_is_checked(self):
        self.edit("skills/romulo-motion-principles/workflows/create.md",
                  "../SKILL.md", "../../outside.md")
        self.assertTrue(validate(self.root))

    def test_artifact_gate_references_required(self):
        self.assert_mutations_fail([
            ("skills/romulo-analisar/SKILL.md", "SEM_PREVISAO_NA_SKILL", "OUTRO_ESTADO"),
            ("skills/romulo-iniciar-projeto/SKILL.md", "../../templates/CLAUDE.md", "../../README.md"),
        ])

    def test_symlink_outside_root_fails(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        path.unlink()
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("NAO LER", encoding="utf-8")
        try:
            path.symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("ambiente sem symlinks")
        self.assertTrue(validate(self.root))

    def test_symlink_inside_root_also_fails(self):
        path = self.root / "templates/CLAUDE.md"
        path.unlink()
        try:
            path.symlink_to(self.root / "README.md")
        except (OSError, NotImplementedError):
            self.skipTest("ambiente sem symlinks")
        self.assertTrue(validate(self.root))

    def test_missing_root_is_reported(self):
        self.assertTrue(validate(self.root / "does-not-exist"))

    def test_cli_exit_codes(self):
        command = [sys.executable, str(ROOT / "scripts/validate_standard.py"), "--root", str(self.root)]
        good = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        (self.root / "plugin.json").write_text("[]", encoding="utf-8")
        bad = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(bad.returncode, 1, bad.stdout + bad.stderr)

    def test_legacy_installer_is_read_only_and_rejects_write_modes(self):
        bash = shutil.which("bash")
        if sys.platform == "win32" and shutil.which("git"):
            git_bash = Path(shutil.which("git")).parent.parent / "bin/bash.exe"
            if git_bash.is_file():
                bash = str(git_bash)
        if not bash:
            self.skipTest("bash indisponivel")
        script = self.root / "install/install.sh"
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        good = subprocess.run([bash, str(script)], capture_output=True, text=True, timeout=10)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        bad = subprocess.run([bash, str(script), str(self.root), "all"], capture_output=True, text=True, timeout=10)
        self.assertEqual(bad.returncode, 2, bad.stdout + bad.stderr)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
