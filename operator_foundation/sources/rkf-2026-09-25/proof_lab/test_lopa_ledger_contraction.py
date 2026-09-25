import unittest
from fractions import Fraction as F
from proof_lab.lopa_ledger_contraction import (bessel_I_lo_hi, inertia, moment4, run)


class TestLopaLedgerContraction(unittest.TestCase):
    def test_moments(self):
        self.assertEqual(moment4((2, 0, 0, 0)), F(1, 4))
        self.assertEqual(moment4((2, 2, 0, 0)), F(1, 24))
        self.assertEqual(moment4((1, 0, 0, 0)), F(0))

    def test_bessel_bracket(self):
        lo, hi = bessel_I_lo_hi(1, F(2))
        self.assertTrue(lo <= hi and hi - lo < F(1, 10 ** 20))
        self.assertTrue(F(15, 10) < lo < F(16, 10))   # I_1(2) = 1.5906...

    def test_native_elimination(self):
        W = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
        self.assertEqual(inertia(W)[0], 1)

    def test_certificate(self):
        cert = run()
        self.assertEqual(cert["verdict"], "PASS")
        for v in cert["grid"].values():
            self.assertTrue(F(v["beta_sil"]) < F(v["r_half"]))


if __name__ == "__main__":
    unittest.main()
