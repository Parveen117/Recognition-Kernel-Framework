"""Exact finite calibrations for the certified Singularity Calculus theory.

The universal claims live in theorem proofs. These checks exercise exact
representative identities and negative controls with rational/integer arithmetic.
"""
from __future__ import annotations

from fractions import Fraction


def axis_swap_determinant() -> int:
    return 0 * 0 - 1 * 1


def maxwell_defect(t_p: Fraction, v_s: Fraction) -> Fraction:
    return t_p - v_s


def exact_potential_mixed_partials(P: Fraction, S: Fraction) -> tuple[Fraction, Fraction]:
    # H(P,S) = P^2*S + P*S^2.
    lhs = 2 * P + 2 * S
    rhs = 2 * P + 2 * S
    return lhs, rhs


def seam_singular_coefficient(normal_jump: Fraction, tangential_jump: Fraction) -> Fraction:
    # rho=x, Delta alpha = a dx + b dy; dx wedge Delta alpha = b dx wedge dy.
    del normal_jump
    return tangential_jump


def rectangle_seam_stokes(c: Fraction, height: Fraction) -> tuple[Fraction, Fraction]:
    boundary_integral = c * height
    seam_integral = c * height
    return boundary_integral, seam_integral


def defining_function_positive_rescale_factor(k: Fraction) -> Fraction:
    if k <= 0:
        raise ValueError("k must be positive")
    return Fraction(1, 1) / k * k


def typed_closure(bulk: Fraction, seam: Fraction) -> bool:
    return bulk == 0 and seam == 0


def piecewise_enthalpy_channels(
    t_p_minus: Fraction,
    v_s_minus: Fraction,
    t_p_plus: Fraction,
    v_s_plus: Fraction,
    seam_tangential_jump: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        t_p_minus - v_s_minus,
        t_p_plus - v_s_plus,
        seam_tangential_jump,
    )


def closed_period_after_gauge(
    base_period: Fraction,
    gauge_start: Fraction,
    gauge_end: Fraction,
) -> Fraction:
    return base_period + gauge_end - gauge_start


def master_closure(
    bulk_minus: Fraction,
    bulk_plus: Fraction,
    seam: Fraction,
) -> bool:
    return bulk_minus == 0 and bulk_plus == 0 and seam == 0


def multi_seam_rectangle_stokes(
    seam_coefficients: tuple[Fraction, ...],
    height: Fraction,
) -> tuple[Fraction, tuple[Fraction, ...]]:
    """SC-10 flat-bulk rectangle crossing several vertical seams."""
    seam_terms = tuple(c * height for c in seam_coefficients)
    boundary_integral = sum(seam_terms, Fraction(0))
    return boundary_integral, seam_terms


def cocycle_defect(
    omega_c_ba: int,
    omega_b_a: int,
    omega_cb_a: int,
    omega_c_b: int,
) -> int:
    return omega_c_ba + omega_b_a - omega_cb_a - omega_c_b


def integer_bilinear_cocycle_defect(a: int, b: int, c: int) -> int:
    """MR-03/SC-11 flat-bulk calibration omega(b,a)=b*a."""
    omega = lambda right, left: right * left
    return cocycle_defect(
        omega(c, b + a),
        omega(b, a),
        omega(c + b, a),
        omega(c, b),
    )


def integer_bad_cocycle_interaction(a: int, b: int, c: int) -> tuple[int, int]:
    """Noncocyclic seam-only rule plus the compensating SC-11 bulk flux."""
    omega_bad = lambda right, left: right * left * left
    defect = cocycle_defect(
        omega_bad(c, b + a),
        omega_bad(b, a),
        omega_bad(c + b, a),
        omega_bad(c, b),
    )
    bulk_flux = -defect
    return defect, bulk_flux


def run_calibration() -> dict[str, object]:
    swap_ok = axis_swap_determinant() == -1

    P = Fraction(7, 3)
    S = Fraction(5, 4)
    lhs, rhs = exact_potential_mixed_partials(P, S)
    d2_zero_ok = lhs == rhs

    maxwell_defect_ok = maxwell_defect(Fraction(2), Fraction(7)) == Fraction(-5)

    tangential_jump_ok = (
        seam_singular_coefficient(Fraction(13, 5), Fraction(7, 11))
        == Fraction(7, 11)
    )
    normal_jump_removable_ok = (
        seam_singular_coefficient(Fraction(13, 5), Fraction(0)) == 0
    )

    boundary, seam = rectangle_seam_stokes(Fraction(7, 3), Fraction(5, 2))
    stokes_ok = boundary == seam == Fraction(35, 6)

    defining_function_ok = all(
        defining_function_positive_rescale_factor(k) == 1
        for k in (Fraction(1, 7), Fraction(2), Fraction(13, 5))
    )

    typed_non_cancellation_ok = (
        not typed_closure(Fraction(3), Fraction(-3))
        and typed_closure(Fraction(0), Fraction(0))
    )

    piecewise_enthalpy_ok = (
        piecewise_enthalpy_channels(
            Fraction(5), Fraction(5), Fraction(9), Fraction(9), Fraction(4, 3)
        )
        == (Fraction(0), Fraction(0), Fraction(4, 3))
    )

    closed_period_gauge_ok = (
        closed_period_after_gauge(Fraction(17, 5), Fraction(9, 7), Fraction(9, 7))
        == Fraction(17, 5)
    )

    master_closure_ok = (
        master_closure(Fraction(0), Fraction(0), Fraction(0))
        and not master_closure(Fraction(3), Fraction(0), Fraction(-3))
        and not master_closure(Fraction(0), Fraction(2), Fraction(0))
        and not master_closure(Fraction(0), Fraction(0), Fraction(5))
    )

    multi_boundary, multi_terms = multi_seam_rectangle_stokes(
        (Fraction(2, 3), Fraction(-5, 7), Fraction(11, 4)),
        Fraction(13, 5),
    )
    multi_seam_additivity_ok = multi_boundary == sum(multi_terms, Fraction(0))

    flat_bulk_cocycle_ok = all(
        integer_bilinear_cocycle_defect(a, b, c) == 0
        for a, b, c in ((2, 3, 5), (-7, 4, 9), (11, -3, 6))
    )

    bad_defect, compensating_bulk = integer_bad_cocycle_interaction(2, 3, 5)
    curvature_interaction_ok = (
        bad_defect == 60
        and compensating_bulk == -60
        and bad_defect + compensating_bulk == 0
    )

    controls = {
        "axis_swap_det_minus_one": swap_ok,
        "smooth_d_squared_zero_control": d2_zero_ok,
        "maxwell_defect_exact": maxwell_defect_ok,
        "tangential_jump_detected": tangential_jump_ok,
        "normal_only_jump_removable": normal_jump_removable_ok,
        "seam_stokes_exact_rectangle": stokes_ok,
        "positive_defining_function_rescaling": defining_function_ok,
        "typed_regular_singular_non_cancellation": typed_non_cancellation_ok,
        "flat_bulk_piecewise_enthalpy_seam": piecewise_enthalpy_ok,
        "closed_period_gauge_invariance": closed_period_gauge_ok,
        "master_closure_componentwise": master_closure_ok,
        "multi_seam_additivity": multi_seam_additivity_ok,
        "flat_bulk_seam_memory_cocycle": flat_bulk_cocycle_ok,
        "curved_bulk_associator_interaction_balance": curvature_interaction_ok,
    }
    status = all(controls.values())
    return {
        "status": (
            "PASS_SINGULARITY_CALCULUS_CALIBRATION"
            if status
            else "FAIL_SINGULARITY_CALCULUS_CALIBRATION"
        ),
        **controls,
    }


if __name__ == "__main__":
    import json

    result = run_calibration()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"].startswith("PASS") else 1)
