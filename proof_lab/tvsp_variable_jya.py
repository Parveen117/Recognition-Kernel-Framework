"""SE45 variable-turn, paired-path and moving-source observer readings.

Python 3.12. Reuses SE41--SE44 exact finite adapters, without a second
operator engine. Tracking uses rational outward analytic enclosures.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from proof_lab.endpoint_observer_index_certificate import add, eye, inv, mat, mul, scale
from proof_lab.ordered_return_feedback import acquire, decode, encode, power, zero
from proof_lab.tvsp_native_jya import (
    J, qturn, phase_packet, decode_phase, sine_interval, floor_dyadic, ceil_dyadic,
)
from proof_lab import counting_curvature as cc

ROOT = Path(__file__).resolve().parents[1]
RESULT = Path(__file__).with_name("TVSP_VARIABLE_JYA_RESULT.json")
PINS = ROOT / "research/lambda_counting/SE45_SOURCE_PINS.json"


def recover_complement(previous_jya, jya, cosine, sine):
    if not sine:
        raise ValueError("two jya readings do not recover this complementary channel")
    return (cosine*jya-previous_jya)/sine


def transport_packet(response, initial_frame, final_frame, label):
    local = mul(mul(inv(final_frame), response), initial_frame)
    p = mat([[1, 0], [0, 0]])
    cut = mul(mul(inv(final_frame), p), final_frame)
    packet = acquire(local, cut, label, ["acquired-path"], final_frame)
    packet["initial_frame"] = encode(initial_frame)
    return packet


def decode_transport(packet):
    return mul(mul(mat(packet["frame"]), decode(packet)), inv(mat(packet["initial_frame"])))


def primitive(poly, slot):
    out = {}
    for key, value in poly.items():
        shifted = list(key)
        shifted[slot] += 1
        out[tuple(shifted)] = value/F(shifted[slot])
    return out


def integrate_step(poly, slot, step):
    antiderivative = primitive(poly, slot)
    return cc.add(cc.shift(antiderivative, slot, step), cc.scale(-1, antiderivative))


def circular_series(angle, depth):
    # Every angle monomial has step_b degree at least one; truncation is exact.
    if any(key[5] < 1 for key in angle):
        raise ValueError("the supplied loop/edge series must have positive step_b order")
    out = cc.eye(2)
    for n in range(1, depth+1):
        out = cc.ma(out, cc.ms(cc.scale(F(1, factorial(n)), cc.power(angle, n)),
                              cc.matrix(power(J, n))))
    return cc.mr(out, steps=depth)


def decode_quarter_cells(packet):
    """Declared bound is in the already proved native quarter-angle unit."""
    total, terminal = 0, eye(2)
    for cell in packet["cells"]:
        bound = F(cell["angle_bound_in_quarters"])
        if not 0 <= bound < 2:
            raise ValueError("short-angle uniqueness is not supplied by this cell bound")
        reading = decode_phase(cell["phase"])
        phase = (reading["cosine"], reading["sine"])
        allowed = {(F(1), F(0)): 0, (F(0), F(1)): 1, (F(0), F(-1)): -1}
        if phase not in allowed:
            raise ValueError("this finite decoder covers only the recorded quarter-sector fixture")
        quarter = allowed[phase]
        if abs(quarter) > bound:
            raise ValueError("reading contradicts the declared cell bound")
        total += quarter
        terminal = mul(power(J, quarter % 4), terminal)
    return {"lifted_quarters": total, "principal_quarters": total % 4,
            "full_turn_memory": total // 4, "terminal": terminal}


def tracking_interval(interval, disturbance):
    lo, hi = interval
    if not 0 <= lo <= hi <= 1 or disturbance < 0:
        raise ValueError("this replay's analytic enclosure uses nonnegative errors and drift")
    lower = lo-sine_interval(lo)[1]+disturbance
    upper = hi-sine_interval(hi)[0]+disturbance
    return max(F(0), floor_dyadic(lower)), ceil_dyadic(upper)


def sine_root_interval(delta, iterations=90):
    lo, hi = delta, 2*delta
    if not 0 < lo < hi <= 1:
        raise ValueError("fixture root bracket outside the declared sine enclosure")
    if not sine_interval(lo)[1] <= delta <= sine_interval(hi)[0]:
        raise ArithmeticError("root bracket not certified")
    for _ in range(iterations):
        middle = (lo+hi)/2
        low, high = sine_interval(middle)
        if high < delta:
            lo = middle
        elif low > delta:
            hi = middle
        else:
            raise ArithmeticError("increase analytic precision before claiming a smaller bracket")
    return lo, hi


def build():
    checks = []

    def check(name, truth, negative=False):
        if not truth:
            raise ArithmeticError(name)
        checks.append({"name": name, "kind": "negative" if negative else "positive", "status": "PASS"})

    turns = [qturn(F(1, 3)), eye(2), scale(-1, eye(2)), qturn(-F(1, 2)), J, qturn(F(1, 4))]
    orbit = [eye(2)]
    for turn in turns:
        orbit.append(mul(turn, orbit[-1]))
    k = [w[0][0] for w in orbit]
    j = [w[1][0] for w in orbit]
    c = [w[0][0] for w in turns]
    s = [w[1][0] for w in turns]
    check("variable circular steps preserve the two-channel radius",
          all(a*a+b*b == 1 for a, b in zip(k, j)))
    check("the division-free jya law holds for unequal and silent turns",
          all(s[n-1]*j[n+1]-(s[n-1]*c[n]+s[n]*c[n-1])*j[n]+s[n]*j[n-1] == 0
              for n in range(1, len(turns))))
    check("two jya readings recover precisely the nonsilent complementary cases",
          all(recover_complement(j[n-1], j[n], c[n-1], s[n-1]) == k[n]
              for n in range(1, len(orbit)) if s[n-1]))
    refused = False
    try:
        recover_complement(F(0), F(0), F(1), F(0))
    except ValueError:
        refused = True
    check("a silent previous turn cannot be divided out", refused, True)
    plus, minus = mat([[1], [0]]), mat([[-1], [0]])
    check("equal two-jya records can have opposite next readings",
          plus[1] == minus[1] and mul(J, plus)[1][0] == 1 and mul(J, minus)[1][0] == -1, True)
    check("the complementary channel repairs the silent-step ambiguity",
          plus[0][0] != minus[0][0] and mul(J, plus) != mul(J, minus))
    check("reusing one fixed-turn coefficient fails on the changing-turn orbit",
          any(j[n+1]-2*c[0]*j[n]+j[n-1] != 0 for n in range(1, len(turns))), True)

    frames = [mat([[1, 0], [n, 1]]) for n in range(len(orbit))]
    packets = [transport_packet(w, eye(2), h, "SE45-variable-orbit-"+str(n))
               for n, (w, h) in enumerate(zip(orbit, frames))]
    detached = json.loads(json.dumps(packets))
    read_orbit = [decode_transport(p) for p in detached]
    decoded_steps = [mul(read_orbit[n+1], inv(read_orbit[n])) for n in range(len(turns))]
    check("complete detached orbit readings recover each changing operator", decoded_steps == turns)
    check("the transported jya covector reads the same scalar in every frame",
          all(mul(mat([[F(n), 1]]), decode(p))[0][0] == j[n] for n, p in enumerate(detached)))
    check("keeping the untransported sensor row gives different jya readings",
          any(decode(p)[1][0] != j[n] for n, p in enumerate(detached)), True)

    A, B = mat([[1, 1], [0, 1]]), mat([[1, 0], [1, 1]])
    D = mat([[2, 0], [0, F(1, 2)]])
    noncommuting = [A, B, D, inv(A)]
    chain = [eye(2)]
    for v in noncommuting:
        chain.append(mul(v, chain[-1]))
    check("varying noncommuting steps obey the full second-order identity",
          all(add(add(chain[n+1], mul(add(noncommuting[n], inv(noncommuting[n-1])), chain[n]), -1),
                  chain[n-1]) == zero(2) for n in range(1, len(noncommuting))))
    check("one freely framed open chain has identity local steps",
          all(mul(mul(inv(chain[n+1]), v), chain[n]) == eye(2)
              for n, v in enumerate(noncommuting)) and chain[-1] != eye(2))
    P, Q = mul(B, A), mul(A, B)
    ha, hb = mat([[1, 2], [0, 1]]), mat([[1, 0], [3, 1]])
    paired = [transport_packet(P, ha, hb, "SE45-path-TV"), transport_packet(Q, ha, hb, "SE45-path-VT")]
    localP, localQ = [decode(p) for p in json.loads(json.dumps(paired))]
    H = mul(inv(Q), P)
    localH = mul(inv(localQ), localP)
    check("the shared terminal frame cancels from the acquired paired return",
          localH == mul(mul(inv(ha), H), ha) and H != eye(2))
    check("complete path readings recover the ordered source defect",
          add(decode_transport(paired[0]), decode_transport(paired[1]), -1) == add(P, Q, -1))
    check("a nonidentity paired return prevents simultaneous path trivialization",
          mul(inv(P), Q) != eye(2), True)
    mismatchP = decode(transport_packet(P, ha, hb, "SE45-same-path-frame-one"))
    mismatchQ = decode(transport_packet(P, ha, eye(2), "SE45-same-path-frame-two"))
    check("unmatched endpoint frames create a spurious path discrepancy",
          mul(inv(mismatchQ), mismatchP) != eye(2), True)

    lam, x, y, a, b = [cc.variable(i) for i in (0, 1, 2, 4, 5)]
    g = cc.add(cc.mul(cc.power(lam, 2), cc.add(cc.power(x, 2), cc.mul(x, y))),
               cc.mul(cc.power(lam, 3), x))
    f = cc.derivative(g, 1)
    K = integrate_step(g, 2, b)
    omega = cc.add(K, cc.scale(-1, cc.shift(K, 1, a)))
    expected = cc.scale(-1, cc.mul(a, b, cc.add(
        cc.mul(cc.power(lam, 2), cc.add(cc.scale(2, x), a, y, cc.scale(F(1, 2), b))),
        cc.power(lam, 3))))
    check("the inhomogeneous count connection has its exact polynomial flux",
          omega == expected and omega == cc.scale(-1, integrate_step(integrate_step(f, 2, b), 1, a)))
    jp = cc.matrix(J)
    connection = [cc.zeros(2), cc.ms(g, jp), cc.zeros(2)]
    field = cc.curvature(connection, 0, 1)
    check("the connection curvature is the native count derivative of its coefficient",
          field == cc.ms(f, jp))
    depth = 3
    forwardP = circular_series(cc.scale(-1, cc.shift(K, 1, a)), depth)
    inverseQ = circular_series(K, depth)
    rectangle = cc.mr(cc.mm(inverseQ, forwardP), steps=depth)
    expected_rectangle = circular_series(omega, depth)
    check("horizontal paired transport gives the complete declared flux return",
          rectangle == expected_rectangle)
    check("the forward-path mixed jya reading has the stated negative curvature sign",
          cc.mixed(rectangle) == cc.ms(cc.c(-1), field)
          and cc.step_coefficient(rectangle[1][0], 1, 1) == cc.scale(-1, f))
    check("copying the positive-flow orientation gives the wrong signed reading",
          cc.mixed(rectangle) != field, True)
    check("the degree-one unit cut misses the retained inhomogeneous curvature",
          cc.mr(field, 1) == cc.zeros(2) and cc.mr(field, 3) == field, True)
    curvature_bank = cc.acquire(connection, 0, 1, cc.matrix([[1, 0], [0, 0]]), 3,
                                "SE45-inhomogeneous-counting-source")
    check("detached count-response readings recover the full polynomial curvature",
          cc.decode_bank(json.loads(json.dumps(curvature_bank))) == field)
    half_a, half_b = cc.scale(F(1, 2), a), cc.scale(F(1, 2), b)
    subflux = cc.scale(-1, integrate_step(integrate_step(f, 2, half_b), 1, half_a))
    summed = cc.add(subflux, cc.shift(subflux, 1, half_a), cc.shift(subflux, 2, half_b),
                    cc.shift(cc.shift(subflux, 1, half_a), 2, half_b))
    check("refined inhomogeneous cell fluxes retain the entire coarse lift", summed == omega)

    refined = {"source": "constant f equals the native quarter-angle q; four unit cells",
               "cells": [{"angle_bound_in_quarters": "1",
                          "phase": phase_packet(scale(-1, J), frames[n], "SE45-refined-cell-"+str(n))}
                         for n in range(4)]}
    flat = {"source": "flat comparison on the same four unit cells",
            "cells": [{"angle_bound_in_quarters": "0",
                       "phase": phase_packet(eye(2), frames[n], "SE45-flat-cell-"+str(n))}
                      for n in range(4)]}
    recovered, flat_read = [decode_quarter_cells(json.loads(json.dumps(p))) for p in (refined, flat)]
    check("bounded refined phase readings recover the lost negative full-turn memory",
          recovered["lifted_quarters"] == -4 and recovered["full_turn_memory"] == -1
          and recovered["terminal"] == eye(2))
    check("flat and curved sources collide only after their refined data are discarded",
          recovered["terminal"] == flat_read["terminal"]
          and recovered["lifted_quarters"] != flat_read["lifted_quarters"], True)
    failures = []
    for phase, bound in ((scale(-1, eye(2)), "2"), (eye(2), "4")):
        bad = {"cells": [{"angle_bound_in_quarters": bound,
                          "phase": phase_packet(phase, eye(2), "SE45-unresolved-cell")}]}
        try:
            decode_quarter_cells(bad)
            failures.append(False)
        except ValueError:
            failures.append(True)
    check("half-turn equality and unbounded full-turn aliases remain undecoded", all(failures), True)

    calibration, relative, correction = A, B, qturn(F(1, 3))
    source = mul(calibration, relative)
    next_calibration = mul(calibration, correction)
    next_relative = mul(mul(mul(mul(inv(correction), inv(calibration)), D), calibration), relative)
    check("the noncommuting tracking update reconstructs the actual changing source",
          mul(next_calibration, next_relative) == mul(D, source))
    wrong_relative = mul(mul(inv(correction), D), relative)
    check("omitting the calibration conjugation corrupts a moving source",
          mul(next_calibration, wrong_relative) != mul(D, source), True)
    fixed_relative = mul(inv(correction), relative)
    check("fixed-source feedback alone does not account for a source advance",
          mul(next_calibration, fixed_relative) == source
          and source != mul(D, source), True)

    delta = F(1, 100)
    constant = [(F(1), F(1))]
    for _ in range(12):
        constant.append(tracking_interval(constant[-1], delta))
    root = sine_root_interval(delta)
    check("the chosen drift obeys the native branch invariance bound",
          delta <= sine_interval(F(1))[0] and all(0 <= lo <= hi <= 1 for lo, hi in constant))
    check("persistent source drift has a certified nonneutral tracking floor",
          delta < root[0] < root[1] and constant[-1][0] > delta
          and constant[-1][1]-root[0] < F(1, 10**27))
    check("zero tracking error is not fixed under uncancelled nonzero drift",
          tracking_interval((F(0), F(0)), delta) == (floor_dyadic(delta), ceil_dyadic(delta)), True)
    check("tracking enclosures obey cubic correction plus the actual disturbance",
          all(nxt[1] <= prev[1]**3/6+delta+F(1, 2**128)
              for prev, nxt in zip(constant, constant[1:])))
    vanishing, envelope = [(F(1), F(1))], F(1)
    envelope_ok = True
    for n in range(32):
        drift = delta/2**n
        vanishing.append(tracking_interval(vanishing[-1], drift))
        envelope = envelope/2+drift+F(1, 2**128)
        envelope_ok &= vanishing[-1][1] <= envelope
    check("vanishing drift obeys the transported contraction envelope",
          envelope_ok and vanishing[-1][1] < F(1, 10**10))
    predicted = [(F(1), F(1))]
    for _ in range(4):
        predicted.append(tracking_interval(predicted[-1], F(0)))
    check("exact source-advance prediction recovers the fixed-source cubic rate",
          predicted[-1][1] < F(1, 10**30))

    return encode({
        "stage": "SE45", "author": "Monty",
        "scope": "Exact supplied variable-turn and paired-path readings; formal count flux; quarter-sector refinement witness under declared bounds; outward scalar tracking enclosures. No universal physical geometry or RH sign.",
        "variable_turns": turns, "variable_orbit_readings": packets,
        "jya_rows": [{"n": n, "complement": k[n], "jya": j[n]} for n in range(len(orbit))],
        "paired_path_readings": paired, "paired_return": H,
        "inhomogeneous_curvature_readings": curvature_bank,
        "inhomogeneous_flux": cc.encode(omega), "horizontal_return_step_depth": depth,
        "horizontal_return": cc.em(rectangle),
        "refined_curved_source": refined, "refined_flat_source": flat,
        "refined_decoded": recovered,
        "noncommuting_tracking": {"calibration": calibration, "relative": relative, "source_advance": D,
                                  "correction": correction, "next_calibration": next_calibration,
                                  "next_relative": next_relative, "next_source": mul(D, source)},
        "constant_disturbance": delta, "constant_tracking_intervals": constant,
        "sharp_floor_interval": root, "root_bisections": 90,
        "vanishing_disturbance_rule": "(1/100)/2^n", "vanishing_tracking_intervals": vanishing,
        "exact_prediction_error_intervals": predicted, "outward_dyadic_bits": 128,
        "checks": checks, "check_count": len(checks),
        "negative_control_count": sum(x["kind"] == "negative" for x in checks),
    })


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+"\n")
    if args.check:
        for pin in json.loads(PINS.read_text())["local_files"]:
            if hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest() != pin["sha256"]:
                raise ArithmeticError("source pin mismatch: "+pin["path"])
        archive = json.loads(RESULT.read_text())
        if archive != result:
            raise ArithmeticError("saved variable-jya readings differ from replay")
        for packet in archive["variable_orbit_readings"]+archive["paired_path_readings"]:
            decode_transport(packet)
        cc.decode_bank(archive["inhomogeneous_curvature_readings"])
        decode_quarter_cells(archive["refined_curved_source"])
        decode_quarter_cells(archive["refined_flat_source"])
    print(f"PASS SE45: {result['check_count']} exact controls; "
          f"{result['negative_control_count']} negative controls; "
          f"archive={'matched' if args.check else 'written' if args.write else 'not requested'}")


if __name__ == "__main__":
    main()
