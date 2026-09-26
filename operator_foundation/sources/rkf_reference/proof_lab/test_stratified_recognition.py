from __future__ import annotations

from fractions import Fraction
import unittest

from proof_lab.stratified_recognition.verify import (
    append_observer,
    blind_dimension,
    faithful,
    identity,
    matrix,
    run_calibration,
    scalar_sum_zero,
    truncation_observer,
    typed_zero,
)


class StratifiedRecognitionTests(unittest.TestCase):
    def test_faithfulness_equals_no_extra_stacked_rank(self):
        E = matrix([[1, 0], [0, 1]])
        Pi = matrix([[1, 1]])
        self.assertTrue(faithful(E, Pi))
        self.assertEqual(blind_dimension(E, Pi), 0)

    def test_blind_dimension_is_exact(self):
        E = matrix([[1, 0, 0]])
        Pi = matrix([[0, 1, 0], [0, 0, 1]])
        self.assertFalse(faithful(E, Pi))
        self.assertEqual(blind_dimension(E, Pi), 2)

    def test_truncation_of_target_relevant_stratum_is_blind(self):
        E = truncation_observer(4, 3)
        Pi = identity(4)
        self.assertFalse(faithful(E, Pi))
        self.assertEqual(blind_dimension(E, Pi), 1)

    def test_one_channel_repairs_one_missing_stratum(self):
        E = truncation_observer(4, 3)
        G = matrix([[0, 0, 0, 1]])
        self.assertTrue(faithful(append_observer(E, G), identity(4)))

    def test_truncation_is_lawful_if_target_ignores_omitted_stratum(self):
        E = truncation_observer(4, 3)
        Pi = truncation_observer(4, 3)
        self.assertTrue(faithful(E, Pi))

    def test_differential_target_has_two_missing_channels(self):
        D = matrix([[1, -1, 0], [0, 1, -1]])
        E = matrix([[1, 0, 0]])
        self.assertFalse(faithful(E, D))
        self.assertEqual(blind_dimension(E, D), 2)
        G = matrix([[0, 1, 0], [0, 0, 1]])
        self.assertTrue(faithful(append_observer(E, G), D))

    def test_scalar_cancellation_is_not_typed_closure(self):
        packet = (Fraction(3), Fraction(-3))
        self.assertTrue(scalar_sum_zero(packet))
        self.assertFalse(typed_zero(packet))

    def test_full_calibration(self):
        self.assertEqual(
            run_calibration()["status"],
            "PASS_STRATIFIED_RECOGNITION_CALIBRATION",
        )


if __name__ == "__main__":
    unittest.main()
