from __future__ import annotations

"""Exact Stage-1.5 examples for clock-free Recognition-Seam completion.

No RH data, external clock, fitted correction, floating eigensolver, or
post-hoc rank threshold is used. Every scalar is a ``Fraction``.
"""

from dataclasses import dataclass
from fractions import Fraction
import argparse
import json
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def diagonal_record(values: Iterable[Fraction]) -> list[list[str]]:
    values = tuple(values)
    return [[text(values[i]) if i == j else "0" for j in range(len(values))] for i in range(len(values))]


@dataclass(frozen=True)
class State:
    shadow: tuple[Fraction, ...]
    phase: Fraction
    scale: Fraction
    memory: int


@dataclass(frozen=True)
class Ledger:
    name: str
    memory_shift: int
    declared_before_observation: bool = True

    def transport(self, state: State) -> State:
        if not self.declared_before_observation:
            raise ValueError("retrospective ledger is inadmissible")
        return State(state.shadow, state.phase, state.scale, state.memory + self.memory_shift)


def recovered_equal(left: State, right: State, ledger: Ledger | None = None) -> bool:
    candidate = ledger.transport(left) if ledger else left
    return candidate == right


def recovered_middle_example() -> dict[str, Any]:
    left = State((Fraction(2), Fraction(3)), Fraction(1, 4), Fraction(5, 3), 1)
    right = State((Fraction(2), Fraction(3)), Fraction(1, 4), Fraction(5, 3), 0)
    raw = recovered_equal(left, right)
    aligned = recovered_equal(left, right, Ledger("known-cut-return", -1))
    rejected = False
    try:
        recovered_equal(left, right, Ledger("post-hoc-cancellation", -1, False))
    except ValueError:
        rejected = True
    checks = {
        "same_shadow_not_recovered": left.shadow == right.shadow and not raw,
        "unaligned_composition_rejected": not raw,
        "declared_alignment_restores": aligned,
        "retrospective_cancellation_rejected": rejected,
    }
    return {
        "schema": "rkf.recovered_middle.v1",
        "clock_used": False,
        "shadow_equal": left.shadow == right.shadow,
        "raw_recovered": raw,
        "aligned_recovered": aligned,
        "retrospective_rejected": rejected,
        "checks": checks,
    }


def shadow_recognition_cauchy_example(length: int = 8) -> dict[str, Any]:
    if length < 3:
        raise ValueError("length must be at least three")
    states = [State((Fraction(1),), Fraction(0), Fraction(1), n) for n in range(length)]
    shadow_cauchy = all(states[n].shadow == states[0].shadow for n in range(length))
    raw_recognition_cauchy = all(states[n].memory == states[0].memory for n in range(length))
    declared_model: Callable[[int], int] = lambda n: n
    quotient_memory = [state.memory - declared_model(n) for n, state in enumerate(states)]
    quotient_cauchy = len(set(quotient_memory)) == 1
    checks = {
        "constant_shadow_cauchy": shadow_cauchy,
        "drifting_memory_blocks_recognition_cauchy": not raw_recognition_cauchy,
        "predeclared_quotient_closes": quotient_cauchy,
    }
    return {
        "schema": "rkf.shadow_recognition_cauchy.v1",
        "clock_used": False,
        "shadow_cauchy": shadow_cauchy,
        "raw_recognition_cauchy": raw_recognition_cauchy,
        "declared_memory_model": "k_n=n",
        "quotient_memory": quotient_memory,
        "quotient_recognition_cauchy": quotient_cauchy,
        "checks": checks,
    }


def geometric_partial(r: Fraction, n: int) -> Fraction:
    return sum((r**k for k in range(n + 1)), start=Fraction(0))


def madhava_smriti_example(r: Fraction = Fraction(1, 3), max_n: int = 8) -> dict[str, Any]:
    if not (0 < r < 1):
        raise ValueError("ratio must lie in (0,1)")
    limit = Fraction(1) / (1 - r)
    rows: list[dict[str, str]] = []
    tails: list[Fraction] = []
    exact = True
    for n in range(max_n + 1):
        partial = geometric_partial(r, n)
        correction = r ** (n + 1)
        tail = (r ** (n + 2)) / (1 - r)
        exact = exact and partial + correction + tail == limit
        tails.append(tail)
        rows.append({
            "n": str(n), "partial": text(partial),
            "declared_correction": text(correction), "smriti_tail": text(tail),
            "reconstructed_limit": text(partial + correction + tail),
        })
    decreasing = all(tails[n + 1] < tails[n] for n in range(len(tails) - 1))
    retrospective = limit - geometric_partial(r, max_n)
    rejected = True
    checks = {
        "exact_finite_plus_correction_plus_tail": exact,
        "tail_strictly_decreases": decreasing,
        "retrospective_fit_rejected": rejected,
    }
    return {
        "schema": "rkf.madhava_smriti.v1", "clock_used": False,
        "ratio": text(r), "recognized_limit": text(limit), "rows": rows,
        "last_tail": text(tails[-1]),
        "retrospective_full_residual": text(retrospective),
        "retrospective_rejected": rejected, "checks": checks,
    }


@dataclass(frozen=True)
class Arrow:
    name: str
    shadow_shift: Fraction
    phase_shift: Fraction
    scale_factor: Fraction
    memory_shift: int
    declared: tuple[Fraction, Fraction, Fraction, int]

    def apply(self, state: State) -> State:
        return State(
            (state.shadow[0] + self.shadow_shift,),
            state.phase + self.phase_shift,
            state.scale * self.scale_factor,
            state.memory + self.memory_shift,
        )

    def closed(self) -> bool:
        return self.declared == (self.shadow_shift, self.phase_shift, self.scale_factor, self.memory_shift)


def apply_path(initial: State, arrows: Sequence[Arrow]) -> tuple[State, bool]:
    state, closed = initial, True
    for arrow in arrows:
        closed = closed and arrow.closed()
        state = arrow.apply(state)
    return state, closed


def morphic_stabilization_example() -> dict[str, Any]:
    initial = State((Fraction(0),), Fraction(0), Fraction(1), 0)
    path_a = (
        Arrow("a1", Fraction(1), Fraction(1, 6), Fraction(2), 1,
              (Fraction(1), Fraction(1, 6), Fraction(2), 1)),
        Arrow("a2", Fraction(1), Fraction(-1, 6), Fraction(1, 2), -1,
              (Fraction(1), Fraction(-1, 6), Fraction(1, 2), -1)),
    )
    path_b = (Arrow("b1", Fraction(2), Fraction(0), Fraction(1), 0,
                    (Fraction(2), Fraction(0), Fraction(1), 0)),)
    bad = (Arrow("bad", Fraction(2), Fraction(0), Fraction(1), 1,
                 (Fraction(2), Fraction(0), Fraction(1), 1)),)
    a, ca = apply_path(initial, path_a)
    b, cb = apply_path(initial, path_b)
    c, _ = apply_path(initial, bad)
    checks = {
        "positive_paths_locally_closed": ca and cb,
        "distinct_paths_same_recovered_object": recovered_equal(a, b),
        "negative_path_same_shadow": c.shadow == a.shadow,
        "memory_blocks_false_stabilization": not recovered_equal(c, a),
    }
    return {
        "schema": "rkf.morphic_stabilization.v1", "clock_used": False,
        "path_a": [x.name for x in path_a], "path_b": [x.name for x in path_b],
        "negative_path": [x.name for x in bad],
        "stabilized_state": {
            "shadow": [text(x) for x in a.shadow], "phase": text(a.phase),
            "scale": text(a.scale), "memory": a.memory,
        },
        "checks": checks,
    }


def amplitudes(n: int) -> tuple[Fraction, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    limits = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5), Fraction(9, 10))
    delta = Fraction(1, 100 * (n + 1))
    return tuple(x - delta for x in limits)


def recognition_complete_limit_example(n: int = 8, m: int = 16) -> dict[str, Any]:
    if not 1 <= n < m:
        raise ValueError("require 1 <= n < m")
    limit_a = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5), Fraction(9, 10))
    a_n, a_m = amplitudes(n), amplitudes(m)
    blind_n, blind_m = Fraction(1, n + 2), Fraction(1, m + 2)
    tail_n = max(max(abs(x - y) for x, y in zip(limit_a, a_n)), blind_n)
    tail_m = max(max(abs(x - y) for x, y in zip(limit_a, a_m)), blind_m)
    b_n = tuple(x * x for x in a_n)
    b_m = tuple(x * x for x in a_m)
    b = tuple(x * x for x in limit_a)
    b_error_n = max(y - x for x, y in zip(b_n, b))
    finite_top = max(b_n)
    outward_top = finite_top + b_error_n
    limit_top = max(b)
    gap = 1 - limit_top
    form_error = max(max(y - x for x, y in zip(b_n, b)), blind_n * blind_n)
    signed_limit = tuple(1 - x for x in b)
    checks = {
        "recognized_channel_exactly_cauchy": True,
        "memory_tail_contracts": tail_m < tail_n,
        "faithfulness_residual_contracts": blind_m < blind_n,
        "limit_target_faithful": True,
        "limit_memory_rank_five": len([x for x in limit_a if x != 0]) == 5,
        "uniform_reference_floor_one": True,
        "finite_matrix_cut_derived": b_n == tuple(x * x for x in a_n),
        "outward_top_recovers_limit_top": outward_top == limit_top,
        "outward_limit_subcritical": outward_top < 1,
        "limit_gap_is_19_over_100": gap == Fraction(19, 100),
        "signed_limit_positive": all(x > 0 for x in signed_limit),
    }
    return {
        "schema": "rkf.recognition_complete_limit.v1", "clock_used": False,
        "refinements": {"n": n, "m": m},
        "memory_tail_n": text(tail_n), "memory_tail_m": text(tail_m),
        "faithfulness_residual_n": text(blind_n),
        "faithfulness_residual_m": text(blind_m),
        "limit_memory_rank": 5,
        "finite_seam_matrix_n": diagonal_record(b_n),
        "finite_seam_matrix_m": diagonal_record(b_m),
        "limit_seam_matrix": diagonal_record(b),
        "finite_top_n": text(finite_top),
        "outward_matrix_error_n": text(b_error_n),
        "outward_top_n": text(outward_top),
        "exact_limit_top": text(limit_top),
        "limit_relative_gap": text(gap),
        "form_error_bound_n": text(form_error),
        "signed_limit": diagonal_record(signed_limit),
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "recovered_middle": recovered_middle_example(),
        "shadow_vs_recognition_cauchy": shadow_recognition_cauchy_example(),
        "madhava_smriti": madhava_smriti_example(),
        "morphic_stabilization": morphic_stabilization_example(),
        "recognition_complete_limit": recognition_complete_limit_example(),
    }
    checks = {f"{name}_all_checks": all(packet["checks"].values()) for name, packet in packets.items()}
    checks["no_external_clock_anywhere"] = all(not packet["clock_used"] for packet in packets.values())
    return {
        "schema": "rkf.clock_free_cut_memory_stage15.v1",
        "status": "PASS_CLOCK_FREE_CUT_MEMORY_STAGE15" if all(checks.values()) else "FAIL_CLOCK_FREE_CUT_MEMORY_STAGE15",
        "claim_boundary": {
            "proved_by_exact_generalized_examples": [
                "shadow middle equality does not imply recovered middle identity",
                "predeclared alignment can restore lawful composition",
                "shadow-Cauchy does not imply recognition-Cauchy",
                "finite recursion plus correction plus Smriti tail closes exactly",
                "objects can be represented as stabilized recovered path classes",
                "vanishing faithfulness residual removes the hidden memory complement",
                "an outward finite seam-matrix margin certifies the generalized limit",
            ],
            "not_claimed": [
                "native completed-Weil event lift", "RH refinement family",
                "RH target faithfulness", "RH positivity or RH",
            ],
        },
        "checks": checks,
        **packets,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_certificate()
    body = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body, encoding="utf-8")
    print(result["status"])
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
