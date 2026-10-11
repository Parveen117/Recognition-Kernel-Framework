"""Exact scalar replay for SE6; not a test of all-aperture Weil positivity.

Uses only Python 3.11/3.12 standard-library rational arithmetic.
Run with --write to create the new stage result, or --check to replay it.
The analytic input and all-function implications are in the SE6 proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path


RESULT = Path(__file__).with_name("ENDPOINT_PAIRED_APERTURE_RESULT.json")


def ratio(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def gamma_difference_lower(frequency: int, count: int = 128) -> F:
    v2 = F(frequency * frequency, 4)
    return sum(
        (v2 / (F(4 * k + 1, 4) * (F(4 * k + 1, 4) ** 2 + v2))
         for k in range(count)),
        F(0),
    )


def exp_lower(x: F, degree: int) -> F:
    return sum((x**k / factorial(k) for k in range(degree + 1)), F(0))


def exp_upper(x: F, degree: int) -> F:
    """Positive x; bound the omitted series by a geometric majorant."""
    tail_ratio = x / (degree + 2)
    if x < 0 or tail_ratio >= 1:
        raise ValueError("Positive-series tail assumptions failed")
    first = x ** (degree + 1) / factorial(degree + 1)
    return exp_lower(x, degree) + first / (1 - tail_ratio)


def replay() -> dict:
    checks: list[dict] = []

    def check(name: str, passed: bool) -> None:
        if not passed:
            raise AssertionError(name)
        checks.append({"name": name, "status": "PASS"})

    # External analytic constants are reduced to these exact comparisons.
    log2_lower = sum((2 * F(1, 3) ** (2*k + 1) / (2*k + 1)
                      for k in range(3)), F(0))
    h32 = sum((F(1, k) for k in range(1, 33)), F(0))
    check("three_term_log2_lower_exceeds_693_over_1000",
          log2_lower > F(693, 1000))
    check("harmonic_gamma_upper_below_three_fifths",
          h32 - 5 * log2_lower < F(3, 5))
    check("exp_seven_tenths_exceeds_two", exp_lower(F(7, 10), 3) > 2)
    check("exp_six_fifths_exceeds_pi_upper",
          exp_lower(F(6, 5), 4) > F(22, 7))
    mg_upper = F(3, 5) + F(11, 7) + F(21, 10) + F(6, 5)
    check("gamma_ground_upper_below_eleven_halves", mg_upper < F(11, 2))

    g16_sum = gamma_difference_lower(16)
    g24_sum = gamma_difference_lower(24)
    check("128_positive_gamma_terms_at_16_exceed_63_over_10",
          g16_sum > F(63, 10))
    check("128_positive_gamma_terms_at_24_exceed_67_over_10",
          g24_sum > F(67, 10))
    check("exp_three_sixteenths_below_two", F(1)/(1-F(3, 16)) < 2)
    check("exp_three_halves_below_five", exp_upper(F(3, 2), 8) < 5)
    check("exp_one_below_three", exp_upper(F(1), 6) < 3)
    check("small_aperture_diameter_below_first_prime",
          log2_lower > F(1, 8))
    check("prime_two_cross_cost_below_one",
          F(7, 5)**2 < 2 and 2*F(7, 10)/F(7, 5) == 1)
    check("cosh_half_geometric_upper_below_three_halves",
          F(1)/(1-F(1, 4)) < F(3, 2))

    # Full small aperture: only the automatic zeroth odd moment is used.
    small_gamma = F(4, 5) - (F(4, 5) + F(11, 2)) * F(2, 27)
    small_boundary = F(1, 16)**3 * 2 / 3
    small_q = small_gamma - small_boundary
    small_sigma = small_q / (small_q + 2 + 12 + small_boundary)
    small_reserve = 2 * small_sigma / 11
    check("small_gamma_floor_one_third", small_gamma == F(1, 3))
    check("small_boundary_upper_one_over_6144",
          small_boundary == F(1, 6144))
    check("small_native_source_floor", small_sigma == F(2047, 88064))
    check("small_joint_observer_reserve",
          small_reserve == F(2047, 484352))

    # Prime-active aperture: moments 1,3,...,29, plus automatic even moments.
    alpha_upper = F(2 * 12**61, 3 * 61**2 * factorial(30)**2)
    check("thirty_moment_low_frequency_mass_below_one_over_500",
          alpha_upper < F(1, 500))
    big_q = F(6, 5) - F(67, 10)*F(1, 500) - 1 - F(1, 16)
    check("prime_active_physical_reserve",
          big_q == F(1241, 10000) and big_q > F(1, 10))
    big_sigma = F(1, 10) / (F(1, 10) + 5 + 12 + 1 + F(1, 16))
    big_reserve = 2 * big_sigma / 11
    check("prime_active_native_complement_floor", big_sigma == F(8, 1453))
    check("prime_active_observer_reserve", big_reserve == F(16, 15983))
    check("prime_active_inverse_bound", 1/big_sigma == F(1453, 8))
    moments = list(range(1, 30, 2))
    check("fifteen_odd_moment_labels",
          len(moments) == 15 and set(moments) | set(range(0, 30, 2))
          == set(range(30)))

    # A missing mixed block must not be mistaken for a positive Schur form.
    # [[1,2],[2,1]] has positive diagonals but Schur value 1-4=-3.
    check("mixed_block_promotion_is_rejected", F(1) - F(2)**2/F(1) < 0)
    # Dropping the moment restriction invalidates the small low-band budget.
    blindless_alpha = 2*F(1, 2)**3 * 24**3 / 27
    blindless_margin = F(6, 5) - F(67, 10)*blindless_alpha - 1 - F(1, 16)
    check("using_only_oddness_for_big_aperture_budget_is_rejected",
          blindless_margin < 0)

    return {
        "schema": "rkf.endpoint-paired-aperture-budget.v1",
        "date": "2026-10-11",
        "arithmetic": "Python Fraction; no floating point, quadrature or eigenvalue sampling",
        "check_count": len(checks),
        "checks": checks,
        "small_aperture": {
            "radius": "1/16",
            "scope": "All states of the odd native aperture completion",
            "physical_source_floor": ratio(small_q),
            "native_source_floor": ratio(small_sigma),
            "relative_joint_reserve": ratio(small_reserve),
            "active_prime_powers": [],
        },
        "prime_active_complement": {
            "radius": "1/2",
            "active_prime_powers": [2],
            "moment_exponents": moments,
            "codimension": 15,
            "physical_source_floor_used": "1/10",
            "native_source_floor": ratio(big_sigma),
            "relative_joint_reserve": ratio(big_reserve),
            "inverse_norm_upper": ratio(1/big_sigma),
            "remaining_schur_matrix_dimension": 15,
            "schur_matrix_evaluated": False,
            "schur_matrix_sign_certified": False,
        },
        "analytic_inputs": [
            "SE4 corrected central-Gamma source and exact odd boundary",
            "SE6 support rule, moment mass inequality and native norm transport",
            "Positive digamma difference series and 3 < pi < 22/7",
            "SE4 full mismatch norm squared < 11/2",
        ],
        "not_certified": [
            "Full sign on the prime-active aperture",
            "Unbounded-aperture limit or global norm-one observer",
            "Historical five-label endpoint identification or K0",
            "Riemann hypothesis",
            "Proof-assistant verification or external mathematical review",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = replay()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.check:
        recorded = json.loads(RESULT.read_text(encoding="utf-8"))
        if recorded != result:
            raise SystemExit("SE6 result mismatch; inspect changes instead of repinning.")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
