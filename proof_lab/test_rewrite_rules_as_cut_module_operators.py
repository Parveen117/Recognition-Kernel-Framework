from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.native_seam_gap_odd_covariance import F0, F1
from proof_lab.paninian_seam_calculus import GAM
from proof_lab.rewrite_rules_as_cut_module_operators import build_certificate, canonical_bytes, certificate_sha256, col_support, realize, sp_mass, sp_mul, sp_sub
from proof_lab.seam_compensated_confluence_verdict import word_rules

EXPECTED = Path(__file__).with_name("REWRITE_RULES_AS_CUT_MODULE_OPERATORS_EXPECTED.sha256")


class RewriteRulesAsCutModuleOperatorsTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("rewrite_rules_as_cut_module_operators.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "float("):
            self.assertNotIn(forbidden, src)

    def test_lopa_chah_commutator_nonzero_without_memory_zero_conflict_with_memory(self) -> None:
        R = realize(GAM, word_rules(False))
        C = sp_sub(sp_mul(R["mats"]["1.3.9"], R["mats"]["7.3.77"], R["n"]), sp_mul(R["mats"]["7.3.77"], R["mats"]["1.3.9"], R["n"]))
        self.assertTrue(C)
        self.assertEqual(sp_mass(C), 2 * len(col_support(C)))
        Rm = realize(GAM, word_rules(True))
        Cm = sp_sub(sp_mul(Rm["mats"]["1.3.9"], Rm["mats"]["7.3.77"], Rm["n"]), sp_mul(Rm["mats"]["7.3.77"], Rm["mats"]["1.3.9"], Rm["n"]))
        self.assertEqual(Cm, {})

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_REWRITE_RULES_AS_CUT_MODULE_OPERATORS_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
