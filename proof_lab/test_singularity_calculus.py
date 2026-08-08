from __future__ import annotations

from fractions import Fraction
import unittest

from proof_lab.singularity_calculus.verify import (
    axis_swap_determinant,
    closed_period_after_gauge,
    defining_function_positive_rescale_factor,
    exact_potential_mixed_partials,
    master_closure,
    maxwell_defect,
    piecewise_enthalpy_channels,
    rectangle_seam_stokes,
    run_calibration,
    seam_singular_coefficient,
    typed_closure,
)


class SingularityCalculusTests(unittest.TestCase):
    def test_axis_swap_is_orientation_reversing_not_singular(self):
        self.assertEqual(axis_swap_determinant(), -1)

    def test_smooth_exact_potential_has_zero_d_squared(self):
        lhs, rhs = exact_potential_mixed_partials(Fraction(7, 3), Fraction(5, 4))
        self.assertEqual(lhs, rhs)

    def test_maxwell_defect_coefficient(self):
        self.assertEqual(maxwell_defect(Fraction(2), Fraction(7)), Fraction(-5))

    def test_tangential_jump_is_the_singular_coefficient(self):
        self.assertEqual(
            seam_singular_coefficient(Fraction(9, 5), Fraction(7, 11)),
            Fraction(7, 11),
        )

    def test_normal_only_jump_is_removable_for_curvature(self):
        self.assertEqual(
            seam_singular_coefficient(Fraction(9, 5), Fraction(0)),
            Fraction(0),
        )

    def test_exact_seam_stokes_rectangle(self):
        boundary, seam = rectangle_seam_stokes(Fraction(7, 3), Fraction(5, 2))
        self.assertEqual(boundary, Fraction(35, 6))
        self.assertEqual(boundary, seam)

    def test_positive_defining_function_rescale_is_invariant(self):
        for k in (Fraction(1, 7), Fraction(2), Fraction(13, 5)):
            self.assertEqual(defining_function_positive_rescale_factor(k), 1)

    def test_regular_and_singular_channels_do_not_scalar_cancel(self):
        self.assertFalse(typed_closure(Fraction(3), Fraction(-3)))
        self.assertTrue(typed_closure(Fraction(0), Fraction(0)))

    def test_flat_bulk_can_retain_seam_defect(self):
        self.assertEqual(
            piecewise_enthalpy_channels(
                Fraction(5), Fraction(5), Fraction(9), Fraction(9), Fraction(4, 3)
            ),
            (Fraction(0), Fraction(0), Fraction(4, 3)),
        )

    def test_closed_cycle_period_is_gauge_invariant(self):
        self.assertEqual(
            closed_period_after_gauge(
                Fraction(17, 5), Fraction(9, 7), Fraction(9, 7)
            ),
            Fraction(17, 5),
        )

    def test_master_closure_requires_all_channels(self):
        self.assertTrue(master_closure(Fraction(0), Fraction(0), Fraction(0)))
        self.assertFalse(master_closure(Fraction(3), Fraction(0), Fraction(-3)))
        self.assertFalse(master_closure(Fraction(0), Fraction(2), Fraction(0)))
        self.assertFalse(master_closure(Fraction(0), Fraction(0), Fraction(5)))

    def test_full_calibration(self):
        self.assertEqual(
            run_calibration()["status"],
            "PASS_SINGULARITY_CALCULUS_CALIBRATION",
        )


if __name__ == "__main__":
    unittest.main()
