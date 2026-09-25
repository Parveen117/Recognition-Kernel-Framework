"""Integrity checks for the canonical mathematics navigation surface."""

from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "MATHEMATICS_INDEX.md"
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class MathematicsIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = INDEX.read_text(encoding="utf-8")

    def test_required_navigation_layers_are_present(self) -> None:
        required = (
            "## 3. Algebra index",
            "## 4. Calculus and geometry index",
            "## 6. Full theorem register",
            "## 7. Parallel theorem registers",
            "## 8. Manuscript, certificate, and formal-evidence layers",
            "## 9. AI and contributor reading protocol",
            "## 10. Open gates that the index must never hide",
        )
        for heading in required:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.text)

    def test_all_local_markdown_links_resolve(self) -> None:
        missing: list[str] = []
        for raw_target in LINK_RE.findall(self.text):
            target = raw_target.strip().split(maxsplit=1)[0]
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            if path_text and not (ROOT / path_text).exists():
                missing.append(raw_target)
        self.assertEqual([], sorted(set(missing)))

    def test_internal_index_anchors_are_explicit(self) -> None:
        anchor_targets = {
            target[1:]
            for target in LINK_RE.findall(self.text)
            if target.startswith("#")
        }
        for anchor in sorted(anchor_targets):
            with self.subTest(anchor=anchor):
                self.assertIn(f'<a id="{anchor}"></a>', self.text)

    def test_numbered_capsules_01_through_77_are_unique_and_indexed(self) -> None:
        capsules = sorted((ROOT / "theorum").glob("[0-9][0-9]_*.md"))
        by_number: dict[int, list[Path]] = {}
        for capsule in capsules:
            by_number.setdefault(int(capsule.name[:2]), []).append(capsule)

        self.assertEqual(list(range(1, 78)), sorted(by_number))
        self.assertFalse(
            {number: paths for number, paths in by_number.items() if len(paths) != 1}
        )

        for capsule in capsules:
            relative = capsule.relative_to(ROOT).as_posix()
            with self.subTest(capsule=relative):
                self.assertIn(f"]({relative})", self.text)

    def test_every_public_parallel_theorem_is_indexed(self) -> None:
        directories = (
            "theorum/morphic_recognition",
            "theorum/recognition_topology",
            "theorum/singularity_calculus",
            "theorum/stratified_recognition",
            "theorum/thermodynamics",
            "theorum/thermodynamics/lambda_geometry",
        )
        for directory in directories:
            for theorem in sorted((ROOT / directory).glob("[0-9][0-9]_*.md")):
                relative = theorem.relative_to(ROOT).as_posix()
                with self.subTest(theorem=relative):
                    self.assertIn(f"]({relative})", self.text)

    def test_foundation_theorems_are_indexed(self) -> None:
        for theorem in sorted((ROOT / "theorems/foundation").glob("*.md")):
            relative = theorem.relative_to(ROOT).as_posix()
            with self.subTest(theorem=relative):
                self.assertIn(f"]({relative})", self.text)

    def test_repository_agent_instructions_route_to_the_index(self) -> None:
        instructions = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("MATHEMATICS_INDEX.md", instructions)
        self.assertIn("finite PASS is not a universal proof", instructions)


if __name__ == "__main__":
    unittest.main()
