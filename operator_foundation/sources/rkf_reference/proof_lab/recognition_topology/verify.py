"""Exact finite calibrations for the Recognition Topology theorem layer.

These checks do not replace the universal proofs in the theorem capsules.
They permanently exercise representative identities and negative controls.
"""
from __future__ import annotations

from fractions import Fraction
from math import floor


def principal_turn_class(turns: Fraction) -> Fraction:
    """Return a normalized principal U(1) phase in turns, in [0,1)."""
    return turns - floor(turns)


def lifted_phase(principal_turns: Fraction, branch: int) -> Fraction:
    """Recover a real lift measured in full turns."""
    if not (Fraction(0) <= principal_turns < Fraction(1)):
        raise ValueError("principal_turns must lie in [0,1)")
    if type(branch) is not int:
        raise TypeError("branch must be an integer")
    return principal_turns + branch


def rectangle_flux(width: Fraction, height: Fraction = Fraction(1)) -> Fraction:
    """For omega=x dy and Omega=dx wedge dy, flux through [0,width]x[0,height]."""
    return width * height


def rectangle_boundary_integral(
    width: Fraction, height: Fraction = Fraction(1)
) -> Fraction:
    """Exact integral of omega=x dy around the positively oriented rectangle."""
    # bottom: dy=0; right: x=width, y:0->height; top:dy=0; left:x=0.
    return width * height


def exact_gauge_boundary_increment(
    width: Fraction, height: Fraction = Fraction(1)
) -> Fraction:
    """Integral of d(xy) around the closed rectangle, evaluated by vertices."""
    chi00 = Fraction(0)
    chi_w0 = Fraction(0)
    chi_wh = width * height
    chi_0h = Fraction(0)
    return (
        (chi_w0 - chi00)
        + (chi_wh - chi_w0)
        + (chi_0h - chi_wh)
        + (chi00 - chi_0h)
    )


def signed_phase_crossings(winding: int, reference: Fraction = Fraction(1, 2)) -> int:
    """Signed crossings for the lift q(t)=winding*t through reference+Z.

    Endpoints are not at reference when reference is strictly between 0 and 1.
    """
    if type(winding) is not int:
        raise TypeError("winding must be int")
    if not (Fraction(0) < reference < Fraction(1)):
        raise ValueError("reference must lie strictly between 0 and 1")
    if winding == 0:
        return 0

    if winding > 0:
        # reference+k in (0,winding)
        count = sum(
            1
            for k in range(-1, winding + 1)
            if Fraction(0) < reference + k < winding
        )
        return count

    # q(t)=winding*t decreases from 0 to winding.
    lo = winding
    count = sum(
        1
        for k in range(winding - 1, 2)
        if lo < reference + k < 0
    )
    return -count


def linear_interpolation_seam_witness() -> complex:
    """F(1/2,-1) for F(t,z)=(1-t)z+t."""
    return (1 - Fraction(1, 2)) * (-1) + Fraction(1, 2)


def run_calibration() -> dict[str, object]:
    # RT-02 exact Stokes/transgression rectangle model.
    widths = [Fraction(1, 7), Fraction(2, 5), Fraction(9, 4)]
    rectangle_ok = all(
        rectangle_boundary_integral(w) == rectangle_flux(w) for w in widths
    )
    gauge_ok = all(exact_gauge_boundary_increment(w) == 0 for w in widths)

    # RT-03: different integer lifts have identical principal class.
    base = Fraction(2, 7)
    principal_blindness_ok = all(
        principal_turn_class(base + n) == base for n in range(-12, 13)
    )
    branch_repair_ok = all(
        lifted_phase(principal_turn_class(base + n), n) == base + n
        for n in range(-12, 13)
    )

    # RT-04: scalar unitary phase crossing count equals winding.
    crossing_ok = all(
        signed_phase_crossings(n) == n for n in range(-12, 13)
    )

    # RT-01 concrete negative control: an attempted degree-1 to degree-0
    # linear interpolation hits the forbidden zero.
    seam_witness_ok = linear_interpolation_seam_witness() == 0

    status = all(
        [
            rectangle_ok,
            gauge_ok,
            principal_blindness_ok,
            branch_repair_ok,
            crossing_ok,
            seam_witness_ok,
        ]
    )
    return {
        "status": "PASS_RECOGNITION_TOPOLOGY_CALIBRATION" if status else "FAIL",
        "rectangle_stokes": rectangle_ok,
        "exact_gauge_closed_loop": gauge_ok,
        "principal_holonomy_blindness": principal_blindness_ok,
        "scalar_branch_repair": branch_repair_ok,
        "phase_crossing_degree": crossing_ok,
        "explicit_seam_witness": seam_witness_ok,
    }


if __name__ == "__main__":
    import json

    result = run_calibration()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if str(result["status"]).startswith("PASS") else 1)
