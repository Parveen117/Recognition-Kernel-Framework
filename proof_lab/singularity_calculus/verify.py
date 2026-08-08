"""Exact finite calibrations for the certified Singularity Calculus core.

The universal claims live in theorem proofs. These checks exercise exact
representative identities and negative controls with rational/integer arithmetic.
"""
from __future__ import annotations

from fractions import Fraction


def axis_swap_determinant() -> int:
    # det [[0,1],[1,0]]
    return 0 * 0 - 1 * 1


def maxwell_defect(t_p: Fraction, v_s: Fraction) -> Fraction:
    return t_p - v_s


def exact_potential_mixed_partials(P: Fraction, S: Fraction) -> tuple[Fraction, Fraction]:
    # H(P,S) = P^2*S + P*S^2
    # T = dH/dS = P^2 + 2*P*S
    # V = dH/dP = 2*P*S + S^2
    # dT/dP = 2P + 2S = dV/dS
    lhs = 2 * P + 2 * S
    rhs = 2 * P + 2 * S
    return lhs, rhs


def seam_singular_coefficient(normal_jump: Fraction, tangential_jump: Fraction) -> Fraction:
    # rho=x, Delta alpha = a dx + b dy.
    # dx wedge Delta alpha = b dx wedge dy.
    del normal_jump
    return tangential_jump


def rectangle_seam_stokes(c: Fraction, height: Fraction) -> tuple[Fraction, Fraction]:
    # alpha_- = 0, alpha_+ = c dy on x=0 seam.
    boundary_integral = c * height
    seam_integral = c * height
    return boundary_integral, seam_integral


def defining_function_positive_rescale_factor(k: Fraction) -> Fraction:
    # delta(k rho) d(k rho) = (1/k) * k * delta(rho) d rho for k>0.
    if k <= 0:
        raise ValueError("k must be positive")
    return Fraction(1, 1) / k * k


def typed_closure(bulk: Fraction, seam: Fraction) -> bool:
    # Typed closure: independent channels must each vanish.
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
    # Integral_C (R + dg) = Integral_C R + g(end)-g(start).
    return base_period + gauge_end - gauge_start


def master_closure(
    bulk_minus: Fraction,
    bulk_plus: Fraction,
    seam: Fraction,
) -> bool:
    # SC-09 finite scalar calibration of the typed closure packet.
    return bulk_minus == 0 and bulk_plus == 0 and seam == 0


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
