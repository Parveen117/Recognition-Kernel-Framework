from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "objects" / "certificates" / "O15_FOUNDATIONAL_AUDIT_V0_1" / "verify.py"
SPEC = importlib.util.spec_from_file_location("o15_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class O15CatalogueTests(unittest.TestCase):
    def test_full_audit_passes(self) -> None:
        result = MODULE.run_audit()
        self.assertEqual(result["status"], "PASS_O15_NATIVE_OBJECT_FOUNDATIONAL_AUDIT")
        self.assertTrue(all(x["passed"] for x in result["obligations"]))
        self.assertTrue(all(x["passed"] for x in result["negative_controls"]))

    def test_all_fifteen_ids_are_unique(self) -> None:
        ledger = json.loads((ROOT / "objects" / "STATUS_LEDGER.json").read_text(encoding="utf-8"))
        ids = [x["id"] for x in ledger["objects"]]
        self.assertEqual(ids, [f"O{i:02d}" for i in range(1, 16)])
        self.assertEqual(len(ids), len(set(ids)))

    def test_open_claims_fail_closed(self) -> None:
        ledger = json.loads((ROOT / "objects" / "STATUS_LEDGER.json").read_text(encoding="utf-8"))
        open_claims = set(ledger["global_open_claims"])
        self.assertIn("Riemann Hypothesis", open_claims)
        self.assertIn("prime modularity", open_claims)
        self.assertIn("infinite seam determinant", open_claims)

    def test_canonical_result_round_trip(self) -> None:
        result = MODULE.run_audit()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"
            path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            loaded = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(loaded, result)


if __name__ == "__main__":
    unittest.main()
