from fractions import Fraction
import unittest

from proof_lab.recognition_topology.verify import (
    exact_gauge_boundary_increment,
    lifted_phase,
    linear_interpolation_seam_witness,
    principal_turn_class,
    rectangle_boundary_integral,
    rectangle_flux,
    run_calibration,
    signed_phase_crossings,
)


class RecognitionTopologyTests(unittest.TestCase):
    def test_rectangle_stokes_exact(self):
        for width in [Fraction(1, 11), Fraction(3, 8), Fraction(13, 5)]:
            self.assertEqual(rectangle_boundary_integral(width), rectangle_flux(width))

    def test_exact_gauge_increment_vanishes_on_closed_rectangle(self):
        for width in [Fraction(1, 9), Fraction(4, 7), Fraction(5, 2)]:
            self.assertEqual(exact_gauge_boundary_increment(width), 0)

    def test_principal_holonomy_forgets_integer_lifts(self):
        base = Fraction(3, 10)
        for n in range(-20, 21):
            self.assertEqual(principal_turn_class(base + n), base)

    def test_branch_integer_repairs_scalar_lift(self):
        base = Fraction(3, 10)
        for n in range(-20, 21):
            self.assertEqual(
                lifted_phase(principal_turn_class(base + n), n),
                base + n,
            )

    def test_phase_crossing_count_equals_winding(self):
        for n in range(-20, 21):
            self.assertEqual(signed_phase_crossings(n), n)

    def test_degree_change_linear_interpolation_hits_seam(self):
        self.assertEqual(linear_interpolation_seam_witness(), 0)

    def test_full_calibration(self):
        self.assertEqual(
            run_calibration()["status"],
            "PASS_RECOGNITION_TOPOLOGY_CALIBRATION",
        )


if __name__ == "__main__":
    unittest.main()
