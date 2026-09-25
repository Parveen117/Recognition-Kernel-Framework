from __future__ import annotations

from fractions import Fraction
import unittest

from proof_lab.singularity_calculus.verify_general_complex import (
    corrupted_packet_fails,
    derived_packet_passes,
    jump_square_zero,
    run_general_complex_calibration,
    total_square,
    wrong_sign_jump_square_nonzero,
    wrong_total_square,
)


class GeneralNormalCrossingComplexTests(unittest.TestCase):
    def test_D_delta_squared_zero_across_dimensions(self):
        for n in range(2, 9):
            for degree in range(0, n - 1):
                self.assertTrue(jump_square_zero(n, degree), (n, degree))

    def test_alternating_sign_is_structural(self):
        self.assertTrue(wrong_sign_jump_square_nonzero())

    def test_total_differential_cross_terms_cancel(self):
        value = Fraction(17, 19)
        self.assertEqual(total_square(2, 0, 0, value, value), 0)
        self.assertEqual(total_square(3, 0, 0, value, value), 0)

    def test_wrong_total_sign_fails(self):
        value = Fraction(17, 19)
        self.assertNotEqual(wrong_total_square(2, value, value), 0)

    def test_derived_packets_pass_realizability_gate(self):
        for n, degree in ((3, 1), (4, 1), (5, 2), (6, 3), (8, 4)):
            self.assertTrue(derived_packet_passes(n, degree), (n, degree))

    def test_corrupted_packets_fail_realizability_gate(self):
        for n, degree in ((3, 1), (4, 1), (5, 2), (6, 3)):
            self.assertTrue(corrupted_packet_fails(n, degree), (n, degree))

    def test_full_general_complex_calibration(self):
        result = run_general_complex_calibration()
        self.assertEqual(
            result["status"],
            "PASS_GENERAL_NORMAL_CROSSING_COMPLEX_CALIBRATION",
        )
        self.assertGreater(result["nilpotence_case_count"], 20)


if __name__ == "__main__":
    unittest.main()
