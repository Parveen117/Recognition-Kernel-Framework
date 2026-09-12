"""Exact controls for SC-14/SC-15 triple normal-crossing compatibility."""
from __future__ import annotations


def pairwise_junctions_from_seam_tables(
    beta1: tuple[tuple[int, int], tuple[int, int]],
    beta2: tuple[tuple[int, int], tuple[int, int]],
    beta3: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Return (J12[e3], J13[e2], J23[e1]).

    Indexing:
      beta1[e2][e3] lives on Sigma_1,
      beta2[e1][e3] lives on Sigma_2,
      beta3[e1][e2] lives on Sigma_3.
    """
    j12 = tuple(
        (beta2[1][e3] - beta2[0][e3])
        - (beta1[1][e3] - beta1[0][e3])
        for e3 in (0, 1)
    )
    j13 = tuple(
        (beta3[1][e2] - beta3[0][e2])
        - (beta1[e2][1] - beta1[e2][0])
        for e2 in (0, 1)
    )
    j23 = tuple(
        (beta3[e1][1] - beta3[e1][0])
        - (beta2[e1][1] - beta2[e1][0])
        for e1 in (0, 1)
    )
    return j12, j13, j23


def triple_obstruction(
    j12: tuple[int, int],
    j13: tuple[int, int],
    j23: tuple[int, int],
) -> int:
    """T123 = Delta1 J23 - Delta2 J13 + Delta3 J12."""
    delta1_j23 = j23[1] - j23[0]
    delta2_j13 = j13[1] - j13[0]
    delta3_j12 = j12[1] - j12[0]
    return delta1_j23 - delta2_j13 + delta3_j12


def wrong_sign_triple_expression(
    j12: tuple[int, int],
    j13: tuple[int, int],
    j23: tuple[int, int],
) -> int:
    """Negative control: replaces the structural middle minus by plus."""
    delta1_j23 = j23[1] - j23[0]
    delta2_j13 = j13[1] - j13[0]
    delta3_j12 = j12[1] - j12[0]
    return delta1_j23 + delta2_j13 + delta3_j12


def calibration_tables() -> tuple[
    tuple[tuple[int, int], tuple[int, int]],
    tuple[tuple[int, int], tuple[int, int]],
    tuple[tuple[int, int], tuple[int, int]],
]:
    beta1 = ((2, 7), (5, 11))
    beta2 = ((3, 17), (13, 19))
    beta3 = ((23, 29), (31, 37))
    return beta1, beta2, beta3


def run_triple_calibration() -> dict[str, object]:
    beta1, beta2, beta3 = calibration_tables()
    j12, j13, j23 = pairwise_junctions_from_seam_tables(beta1, beta2, beta3)

    compatible_nontrivial_ok = (
        j12 == (7, -2)
        and j13 == (3, 2)
        and j23 == (-8, 0)
        and any(value != 0 for pair in (j12, j13, j23) for value in pair)
        and triple_obstruction(j12, j13, j23) == 0
    )

    wrong_sign_rejected_ok = wrong_sign_triple_expression(j12, j13, j23) == -2

    corrupted_j23 = (j23[0], j23[1] + 5)
    incompatible_declared_data_ok = triple_obstruction(j12, j13, corrupted_j23) == 5

    controls = {
        "derived_nonzero_pairwise_junctions_have_zero_T123": compatible_nontrivial_ok,
        "wrong_sign_alternating_law_rejected": wrong_sign_rejected_ok,
        "independent_triple_obstruction_detected": incompatible_declared_data_ok,
    }
    status = all(controls.values())
    return {
        "status": (
            "PASS_TRIPLE_NORMAL_CROSSING_CALIBRATION"
            if status
            else "FAIL_TRIPLE_NORMAL_CROSSING_CALIBRATION"
        ),
        "j12": j12,
        "j13": j13,
        "j23": j23,
        "T123": triple_obstruction(j12, j13, j23),
        **controls,
    }


if __name__ == "__main__":
    import json

    result = run_triple_calibration()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"].startswith("PASS") else 1)
