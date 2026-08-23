import unittest
from fractions import Fraction as F
from proof_lab.seam_flow_meter import (B_of, count, det_weights, precompute, run)
from proof_lab.lopa_ledger_contraction import invariant_even_basis


class TestSeamFlowMeter(unittest.TestCase):
    def test_ladder_identity_spot(self):
        basis = invariant_even_basis()
        M, S = precompute(basis)
        from proof_lab.lopa_ledger_contraction import build
        self.assertEqual(build(F(1, 4))[3], B_of(F(1, 4), len(basis), S))

    def test_det_route_consistency(self):
        basis = invariant_even_basis()
        M, S = precompute(basis)
        B = B_of(F(1, 8), len(basis), S)
        d = det_weights(M, B, F(1, 2))
        self.assertNotEqual(d, 0)

    def test_certificate(self):
        cert = run()
        self.assertEqual(cert["verdict"], "PASS")
        for v in cert["grid"].values():
            for b in v["flips"]:
                self.assertEqual((abs(b["jump"]) % 2 == 1), b["det_sign_flip"])


if __name__ == "__main__":
    unittest.main()
