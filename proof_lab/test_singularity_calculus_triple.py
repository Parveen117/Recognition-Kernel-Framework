from __future__ import annotations

import unittest

from proof_lab.singularity_calculus.verify_triple import (
    calibration_tables,
    pairwise_junctions_from_seam_tables,
    run_triple_calibration,
    triple_obstruction,
    wrong_sign_triple_expression,
)


class TripleNormalCrossingTests(unittest.TestCase):
    def test_compatible_seam_data_give_zero_triple_obstruction(self):
        beta1, beta2, beta3 = calibration_tables()
        j12, j13, j23 = pairwise_junctions_from_seam_tables(beta1, beta2, beta3)
        self.assertEqual(j12, (7, -2))
        self.assertEqual(j13, (1, 0))
        self.assertEqual(j23, (-6, 2))
        self.assertTrue(any(v != 0 for pair in (j12, j13, j23) for v in pair))
        self.assertEqual(triple_obstruction(j12, j13, j23), 0)

    def test_wrong_sign_formula_fails_on_compatible_data(self):
        beta1, beta2, beta3 = calibration_tables()
        j12, j13, j23 = pairwise_junctions_from_seam_tables(beta1, beta2, beta3)
        self.assertEqual(wrong_sign_triple_expression(j12, j13, j23), -2)
        self.assertNotEqual(wrong_sign_triple_expression(j12, j13, j23), 0)

    def test_corrupted_independent_junction_data_are_rejected(self):
        beta1, beta2, beta3 = calibration_tables()
        j12, j13, j23 = pairwise_junctions_from_seam_tables(beta1, beta2, beta3)
        corrupted_j23 = (j23[0], j23[1] + 5)
        self.assertEqual(triple_obstruction(j12, j13, corrupted_j23), 5)
        self.assertNotEqual(triple_obstruction(j12, j13, corrupted_j23), 0)

    def test_full_triple_calibration(self):
        self.assertEqual(
            run_triple_calibration()["status"],
            "PASS_TRIPLE_NORMAL_CROSSING_CALIBRATION",
        )


if __name__ == "__main__":
    unittest.main()
