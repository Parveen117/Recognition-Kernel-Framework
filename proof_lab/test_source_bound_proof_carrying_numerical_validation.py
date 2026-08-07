#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab import source_bound_proof_carrying_numerical_validation as t47


class SourceBoundProofCarryingNumericalValidationTests(unittest.TestCase):
    def test_certificate_passes(self):
        result = t47.build_certificate()
        self.assertEqual(result["status"], t47.STATUS)
        self.assertTrue(all(result["checks"].values()))

    def test_pinned_digest(self):
        payload = t47.canonical_bytes(t47.build_certificate())
        actual = hashlib.sha256(payload).hexdigest()
        expected = Path("proof_lab/SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_EXPECTED.sha256").read_text().strip()
        self.assertEqual(actual, expected)

    def test_interval_division_rejects_zero(self):
        with self.assertRaises(ZeroDivisionError):
            t47.interval_div((Fraction(1), Fraction(2)), (Fraction(-1), Fraction(1)))

    def test_exact_boundary_fails_strict_claim(self):
        self.assertEqual(t47.classify_strict_upper(Fraction(1), Fraction(1), Fraction(1)), "FAIL_EXACT_EQUALITY")

    def test_uncertain_touch_remains_incomplete(self):
        self.assertEqual(t47.classify_strict_upper(Fraction(9, 10), Fraction(1), Fraction(1)), "INCOMPLETE")

    def test_narrower_claim_is_rejected(self):
        nodes = t47.canonical_trace_fixture()
        nodes[-1] = dict(nodes[-1], lower="1", upper="109/100")
        ok, reason, _ = t47.validate_trace(nodes, "root", "contract-A")
        self.assertFalse(ok)
        self.assertEqual(reason, "CLAIMED_INTERVAL_TOO_NARROW")

    def test_source_mismatch_rejected(self):
        nodes = t47.canonical_trace_fixture()
        nodes[0] = dict(nodes[0], source="other-source")
        ok, reason, _ = t47.validate_trace(nodes, "root", "contract-A")
        self.assertFalse(ok)
        self.assertEqual(reason, "SOURCE_MISMATCH")

    def test_theorem43_tail_is_exact_rational(self):
        upper = t47.theorem43_tail_upper(2, Fraction(1, 2), Fraction(2), Fraction(1), 4)
        self.assertEqual(upper, Fraction(3869, 56320))


if __name__ == "__main__":
    unittest.main()
