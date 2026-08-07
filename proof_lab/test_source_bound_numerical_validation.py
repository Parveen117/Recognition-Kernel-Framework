import unittest
from fractions import Fraction

from proof_lab.source_bound_numerical_validation import (
    STATUS,
    Interval,
    add,
    build_certificate,
    div,
    exp_rational_upper,
    geometric_tail,
    implementation_manifest_hash,
    mul,
    strict_upper_decision,
    t43_tail_upper,
    verify_trace,
)


class SourceBoundNumericalValidationTests(unittest.TestCase):
    def test_exact_interval_add(self):
        self.assertEqual(
            add(Interval.exact(Fraction(1, 3)), Interval.exact(Fraction(1, 6))),
            Interval.exact(Fraction(1, 2)),
        )

    def test_interval_multiplication(self):
        self.assertEqual(
            mul(Interval(Fraction(-2), Fraction(3)), Interval(Fraction(4), Fraction(5))),
            Interval(Fraction(-10), Fraction(15)),
        )

    def test_division_by_zero_interval_rejected(self):
        with self.assertRaises(ZeroDivisionError):
            div(Interval.exact(1), Interval(Fraction(-1), Fraction(1)))

    def test_valid_trace_derives_radius(self):
        nodes = [
            {"id": "a", "kind": "exact_contract", "value": Fraction(1, 3), "interval": (Fraction(1, 3), Fraction(1, 3))},
            {"id": "b", "kind": "exact_contract", "value": Fraction(1, 6), "interval": (Fraction(1, 6), Fraction(1, 6))},
            {"id": "s", "kind": "op", "op": "add", "deps": ["a", "b"], "interval": (Fraction(49, 100), Fraction(51, 100))},
        ]
        result = verify_trace(nodes, "s")
        self.assertEqual(result.status, "PASS")
        self.assertEqual(result.root.radius, Fraction(1, 100))

    def test_forged_narrow_trace_fails(self):
        nodes = [
            {"id": "a", "kind": "exact_contract", "value": Fraction(1, 3), "interval": (Fraction(1, 3), Fraction(1, 3))},
            {"id": "b", "kind": "exact_contract", "value": Fraction(1, 6), "interval": (Fraction(1, 6), Fraction(1, 6))},
            {"id": "s", "kind": "op", "op": "add", "deps": ["a", "b"], "interval": (Fraction(49, 100), Fraction(49, 100))},
        ]
        self.assertEqual(verify_trace(nodes, "s").status, "FAIL")

    def test_duplicate_node_id_invalid(self):
        nodes = [
            {"id": "a", "kind": "exact_contract", "value": 1, "interval": (1, 1)},
            {"id": "a", "kind": "exact_contract", "value": 2, "interval": (2, 2)},
        ]
        self.assertEqual(verify_trace(nodes, "a").status, "INVALID")

    def test_forward_dependency_or_cycle_invalid(self):
        nodes = [
            {"id": "a", "kind": "op", "op": "neg", "deps": ["b"], "interval": (-1, 1)},
            {"id": "b", "kind": "op", "op": "neg", "deps": ["a"], "interval": (-1, 1)},
        ]
        self.assertEqual(verify_trace(nodes, "a").status, "INVALID")

    def test_unsupported_source_is_open(self):
        nodes = [{"id": "x", "kind": "backend_claim", "interval": (1, 1)}]
        self.assertEqual(verify_trace(nodes, "x").status, "OPEN")

    def test_source_completeness_is_required(self):
        nodes = [{"id": "x", "kind": "exact_contract", "value": 1, "interval": (1, 1)}]
        self.assertEqual(verify_trace(nodes, "x", source_complete=False).status, "OPEN")

    def test_geometric_tail(self):
        self.assertEqual(geometric_tail(Fraction(1, 8), Fraction(1, 2)), Fraction(1, 4))

    def test_geometric_tail_ratio_one_rejected(self):
        with self.assertRaises(ValueError):
            geometric_tail(Fraction(1, 8), Fraction(1))

    def test_exp_rational_upper_pinned(self):
        self.assertEqual(exp_rational_upper(Fraction(1, 2), 2), Fraction(277, 168))

    def test_exp_order_too_small_rejected(self):
        with self.assertRaises(ValueError):
            exp_rational_upper(Fraction(5), 0)

    def test_t43_tail_is_exact_positive_fraction(self):
        value = t43_tail_upper(Fraction(1, 2), Fraction(2), Fraction(1, 3), 2, 2)
        self.assertIsInstance(value, Fraction)
        self.assertGreater(value, 0)

    def test_exact_strict_boundary_fails(self):
        self.assertEqual(strict_upper_decision(Interval.exact(Fraction(4, 5)), Fraction(4, 5)), "FAIL")

    def test_uncertain_touching_boundary_is_incomplete(self):
        self.assertEqual(
            strict_upper_decision(Interval(Fraction(79, 100), Fraction(4, 5)), Fraction(4, 5)),
            "INCOMPLETE",
        )

    def test_interval_strictly_below_passes(self):
        self.assertEqual(
            strict_upper_decision(Interval(Fraction(7, 10), Fraction(79, 100)), Fraction(4, 5)),
            "PASS",
        )

    def test_manifest_hash_is_stable_shape(self):
        digest = implementation_manifest_hash()
        self.assertEqual(len(digest), 64)
        int(digest, 16)

    def test_certificate_passes(self):
        result = build_certificate()
        self.assertEqual(result["status"], STATUS)
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["pinned_examples"]["root_radius"], "1/100")
        self.assertEqual(result["pinned_examples"]["geometric_tail"], "1/4")
        self.assertEqual(result["pinned_examples"]["exp_upper_x_half_order_2"], "277/168")


if __name__ == "__main__":
    unittest.main()
