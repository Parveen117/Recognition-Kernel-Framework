from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.cut_graded_lambda_jacobian_tower import (
    bigrade_matrix,
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    quadratic_lambda,
    quadratic_lambda_jacobian,
    rank_fraction,
    run_connection_curvature_fixture,
    run_jacobian_bigrading_fixture,
    run_rank_change_cut_fixture,
    run_recursive_tower_fixture,
    run_tower_observer_fixture,
    vector,
)
from proof_lab.cut_graded_universal_generator import (
    diagonal,
    identity,
    is_zero,
    matmul,
    scale,
    transpose,
    zero,
)


class CutGradedLambdaJacobianTowerTests(unittest.TestCase):
    def test_recursive_tower_and_cut_covariance(self) -> None:
        packet = run_recursive_tower_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_lambda_value_and_jacobian_covariance_at_another_point(self) -> None:
        j = diagonal((1, 1, -1, -1))
        x = vector((1, 2, -3, 5))
        jx = tuple(j[i][i] * x[i] for i in range(4))
        self.assertEqual(
            quadratic_lambda(jx),
            tuple(j[i][i] * quadratic_lambda(x)[i] for i in range(4)),
        )
        self.assertEqual(
            quadratic_lambda_jacobian(jx),
            matmul(matmul(j, quadratic_lambda_jacobian(x)), j),
        )

    def test_jacobian_bigrading_reconstructs_and_types_every_sector(self) -> None:
        packet = run_jacobian_bigrading_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_antisymmetry_is_not_automatic(self) -> None:
        j = diagonal((1, 1, -1, -1))
        a = quadratic_lambda_jacobian(vector((2, -1, 3, 4)))
        sectors = bigrade_matrix(a, j)
        self.assertNotEqual(transpose(a), scale(-1, a))
        self.assertTrue(
            not is_zero(sectors["cut_even_symmetric"])
            or not is_zero(sectors["cut_odd_symmetric"])
        )

    def test_connection_curvature_matches_cut_loop_coefficient(self) -> None:
        packet = run_connection_curvature_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_higher_layer_repairs_first_order_target_blindness(self) -> None:
        packet = run_tower_observer_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["burden"], "1/4")

    def test_rank_change_cut_and_repair(self) -> None:
        packet = run_rank_change_cut_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_rank_function_negative_controls(self) -> None:
        self.assertEqual(rank_fraction(zero(3, 3)), 0)
        self.assertEqual(rank_fraction(identity(3)), 3)
        self.assertEqual(rank_fraction(diagonal((1, 1, 0))), 2)

    def test_certificate_is_deterministic(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertEqual(
            first["status"],
            "PASS_CUT_GRADED_LAMBDA_JACOBIAN_TOWER_CANDIDATE",
        )
        self.assertTrue(all(first["checks"].values()))

    def test_certificate_hash_matches_pin(self) -> None:
        payload = build_certificate()
        expected_path = Path(__file__).with_name(
            "CUT_GRADED_LAMBDA_JACOBIAN_TOWER_EXPECTED.sha256"
        )
        expected = expected_path.read_text(encoding="ascii").strip()
        self.assertEqual(certificate_sha256(payload), expected)
        self.assertEqual(hashlib.sha256(canonical_bytes(payload)).hexdigest(), expected)


if __name__ == "__main__":
    unittest.main()
