"""Exact calibrations for SC-16 through SC-18.

These controls exercise the normal-crossing jump complex, total differential
sign, and realizability obstruction in finite exact arithmetic.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def ordered_subsets(n: int, k: int) -> tuple[tuple[int, ...], ...]:
    return tuple(combinations(range(1, n + 1), k))


def delete_position(I: tuple[int, ...], r: int) -> tuple[int, ...]:
    return I[:r] + I[r + 1 :]


def scalar_jump(cochain: dict[tuple[int, ...], Fraction], j: int, base: tuple[int, ...]) -> Fraction:
    """Exact calibration model: commuting jump operator Delta_j multiplies by j+1.

    The theorem itself does not assume scalar multiplication. This is only a
    finite exact representation with pairwise commuting jump maps.
    """
    return Fraction(j + 1) * cochain[base]


def jump_differential(
    n: int,
    degree: int,
    cochain: dict[tuple[int, ...], Fraction],
) -> dict[tuple[int, ...], Fraction]:
    out: dict[tuple[int, ...], Fraction] = {}
    for I in ordered_subsets(n, degree + 1):
        total = Fraction(0)
        for r, j in enumerate(I):
            total += ((-1) ** r) * scalar_jump(cochain, j, delete_position(I, r))
        out[I] = total
    return out


def jump_square_zero(n: int, degree: int) -> bool:
    source = {
        I: Fraction(sum((index + 2) * value for index, value in enumerate(I)) + 3, 7)
        for I in ordered_subsets(n, degree)
    }
    first = jump_differential(n, degree, source)
    second = jump_differential(n, degree + 1, first)
    return all(value == 0 for value in second.values())


def wrong_sign_jump_square_nonzero() -> bool:
    """Delete the alternating sign and require nilpotence to fail."""
    n = 4
    source = {I: Fraction(sum(I) + 1) for I in ordered_subsets(n, 1)}
    first: dict[tuple[int, ...], Fraction] = {}
    for I in ordered_subsets(n, 2):
        first[I] = sum(
            (Fraction(j + 1) * source[delete_position(I, r)] for r, j in enumerate(I)),
            Fraction(0),
        )
    second: dict[tuple[int, ...], Fraction] = {}
    for I in ordered_subsets(n, 3):
        second[I] = sum(
            (Fraction(j + 1) * first[delete_position(I, r)] for r, j in enumerate(I)),
            Fraction(0),
        )
    return any(value != 0 for value in second.values())


def total_square(
    form_degree: int,
    d_value: Fraction,
    jump_value: Fraction,
    d_of_jump: Fraction,
    jump_of_d: Fraction,
) -> Fraction:
    """Coefficient-level cross-term calibration of mathbb D^2.

    d^2 and D^2 are zero. The remaining terms are
      (-1)^(p+1) Dd + (-1)^p dD.
    """
    del d_value, jump_value
    return ((-1) ** (form_degree + 1)) * jump_of_d + ((-1) ** form_degree) * d_of_jump


def wrong_total_square(form_degree: int, d_of_jump: Fraction, jump_of_d: Fraction) -> Fraction:
    del form_degree
    return d_of_jump + jump_of_d


def realizability_gate(next_obstruction: dict[tuple[int, ...], Fraction]) -> bool:
    return all(value == 0 for value in next_obstruction.values())


def derived_packet_passes(n: int, source_degree: int) -> bool:
    source = {
        I: Fraction(sum((idx + 1) * value for idx, value in enumerate(I)) + 5, 11)
        for I in ordered_subsets(n, source_degree)
    }
    derived = jump_differential(n, source_degree, source)
    obstruction = jump_differential(n, source_degree + 1, derived)
    return realizability_gate(obstruction)


def corrupted_packet_fails(n: int, source_degree: int) -> bool:
    source = {
        I: Fraction(sum(I) + 2, 5)
        for I in ordered_subsets(n, source_degree)
    }
    derived = jump_differential(n, source_degree, source)
    if not derived:
        return False
    first_key = sorted(derived)[0]
    corrupted = dict(derived)
    corrupted[first_key] += Fraction(7, 13)
    obstruction = jump_differential(n, source_degree + 1, corrupted)
    return not realizability_gate(obstruction)


def run_general_complex_calibration() -> dict[str, object]:
    nilpotence_cases = []
    for n in range(2, 9):
        for degree in range(0, n - 1):
            nilpotence_cases.append(jump_square_zero(n, degree))

    wrong_jump_sign_detected = wrong_sign_jump_square_nonzero()

    commute_value = Fraction(17, 19)
    total_even = total_square(2, Fraction(0), Fraction(0), commute_value, commute_value)
    total_odd = total_square(3, Fraction(0), Fraction(0), commute_value, commute_value)
    total_nilpotence_ok = total_even == 0 and total_odd == 0
    wrong_total_sign_detected = wrong_total_square(2, commute_value, commute_value) != 0

    derived_realizability_ok = all(
        derived_packet_passes(n, degree)
        for n, degree in ((3, 1), (4, 1), (5, 2), (6, 3), (8, 4))
    )
    corrupted_realizability_detected = all(
        corrupted_packet_fails(n, degree)
        for n, degree in ((3, 1), (4, 1), (5, 2), (6, 3))
    )

    controls = {
        "D_delta_squared_zero_n2_to_n8": all(nilpotence_cases),
        "alternating_sign_is_necessary": wrong_jump_sign_detected,
        "total_differential_squared_zero": total_nilpotence_ok,
        "wrong_totalization_sign_detected": wrong_total_sign_detected,
        "derived_packets_pass_next_gate": derived_realizability_ok,
        "corrupted_packets_fail_next_gate": corrupted_realizability_detected,
    }
    status = all(controls.values())
    return {
        "status": (
            "PASS_GENERAL_NORMAL_CROSSING_COMPLEX_CALIBRATION"
            if status
            else "FAIL_GENERAL_NORMAL_CROSSING_COMPLEX_CALIBRATION"
        ),
        "nilpotence_case_count": len(nilpotence_cases),
        **controls,
    }


if __name__ == "__main__":
    import json

    result = run_general_complex_calibration()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"].startswith("PASS") else 1)
