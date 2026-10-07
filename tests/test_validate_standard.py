"""Regressoes do validador estrutural, nao simulacao de uso das skills por modelos."""
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
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def edit(self, relative, before, after):
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(before, text)
        path.write_text(text.replace(before, after), encoding="utf-8")

    def test_distribution_passes(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_skill_fails(self):
        shutil.rmtree(self.root / "skills/romulo-interface")
        self.assertTrue(validate(self.root))

    def test_invalid_metadata_fails(self):
        cases = (("name: romulo-interface", "name: romulo-outro"),
                 ('description: "', 'description "'),
                 ("---\n", ""))
        path = self.root / "skills/romulo-interface/SKILL.md"
        original = path.read_text(encoding="utf-8")
        for before, after in cases:
            with self.subTest(before=before):
                path.write_text(original.replace(before, after, 1), encoding="utf-8")
                self.assertTrue(validate(self.root))
        path.write_text(original, encoding="utf-8")

    def test_empty_description_fails(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[2] = 'description: ""'
        path.write_text("\n".join(lines)+"\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_quoted_colon_is_valid(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[2] = 'description: "Texto valido: com dois pontos"'
        path.write_text("\n".join(lines)+"\n", encoding="utf-8")
        self.assertEqual(validate(self.root), [])

    def test_unquoted_colon_fails(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[2] = "description: Texto invalido: valor"
        path.write_text("\n".join(lines)+"\n", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_manifests_and_catalogs_fail_on_invalid_configuration(self):
        cases = (
            ("plugin.json", '"version": "1.4.0"', '"version": "1.3.1"'),
            ("plugin.json", '"version": "1.4.0"', '"version": null'),
            ("plugin.json", '"name": "romulo-dev-standard"', '"name": "outro"'),
            ("plugin.json", '"name": "romulo-dev-standard"', '"name": "x", "name": "romulo-dev-standard"'),
            (".codex-plugin/plugin.json", '"skills": "./skills/"', '"skills": "./ausente/"'),
            (".agents/plugins/marketplace.json", '"path": "./"', '"path": "../"'),
            (".claude-plugin/marketplace.json", '"source": "./"', '"source": "./outro"'),
        )
        for relative, before, after in cases:
            with self.subTest(relative=relative, before=before):
                path = self.root / relative
                original = path.read_text(encoding="utf-8")
                self.edit(relative, before, after)
                self.assertTrue(validate(self.root))
                path.write_text(original, encoding="utf-8")

    def test_missing_manifest_fails(self):
        (self.root / "plugin.json").unlink()
        self.assertTrue(validate(self.root))

    def test_invalid_json_fails(self):
        (self.root / "plugin.json").write_text("{", encoding="utf-8")
        self.assertTrue(validate(self.root))

    def test_lists_counts_versions_routes_and_links_fail(self):
        cases = (
            ("README.md", "- romulo-interface\n", ""),
            ("INSTALL.md", "- romulo-interface\n", "- romulo-interface\n- romulo-interface\n"),
            ("README.md", "11 skills", "9 skills"),
            ("README.md", "Versao: 1.4.0", "Versao: 1.0.0"),
            ("templates/AGENTS.md", "VERSAO_MINIMA_ROMULO_STANDARD: 1.4.0", "VERSAO_MINIMA_ROMULO_STANDARD: 1.3.1"),
            ("templates/CLAUDE.md", "@AGENTS.md", "@outro.md"),
            ("skills/romulo-construir/SKILL.md", "`romulo-interface`", "`romulo-fantasma`"),
            ("README.md", "[INSTALL.md](INSTALL.md)", "[INSTALL.md](nao-existe.md)"),
        )
        for relative, before, after in cases:
            with self.subTest(relative=relative, before=before):
                path = self.root / relative
                original = path.read_text(encoding="utf-8")
                self.edit(relative, before, after)
                self.assertTrue(validate(self.root))
                path.write_text(original, encoding="utf-8")

    def test_skill_symlink_fails(self):
        path = self.root / "skills/romulo-interface/SKILL.md"
        path.unlink()
        try:
            path.symlink_to(Path(self.temp.name) / "outside.md")
        except (OSError, NotImplementedError):
            self.skipTest("ambiente sem suporte a symlinks")
        self.assertTrue(validate(self.root))

    def test_cli_exit_codes(self):
        command = [sys.executable, str(ROOT / "scripts/validate_standard.py"), "--root", str(self.root)]
        good = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        (self.root / "plugin.json").write_text("[]", encoding="utf-8")
        bad = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(bad.returncode, 1, bad.stdout + bad.stderr)


if __name__ == "__main__":
    unittest.main()
