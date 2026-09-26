import unittest
from fractions import Fraction as F
from proof_lab.selective_release import (chi_of_u, face_enclosure, moment4, run)


class TestSelectiveRelease(unittest.TestCase):
    def test_characters(self):
        self.assertEqual(chi_of_u(F(3, 2)), [F(0), F(-2), F(0), F(1)])
        self.assertEqual(chi_of_u(F(2)), [F(1), F(0), F(-3), F(0), F(1)])

    def test_degree8_moments(self):
        self.assertEqual(moment4((8, 0, 0, 0)), F(7, 128))
        self.assertEqual(moment4((4, 4, 0, 0)), F(3, 640))

    def test_ladder_law_instance(self):
        lo0, hi0 = face_enclosure(0, F(1, 8))
        lo1, hi1 = face_enclosure(1, F(1, 8))
        self.assertTrue(hi1 / lo0 <= F(1, 8) / 4)

    def test_certificate(self):
        cert = run()
        self.assertEqual(cert["verdict"], "PASS")
        for v in cert["grid"].values():
            self.assertTrue(v["outward_certificate"])
            self.assertNotIn("UNRIPE_REFUSED", str(v["count_equalities"]))


if __name__ == "__main__":
    unittest.main()
