"""SE43 finite counting/EMK movement and retained seam observer fixtures.

Python 3.12; exact rational coefficient readings. Reuses SE42's finite
polynomial evaluator without changing the canonical operator engine.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from proof_lab.counting_curvature import (
    LABELS, add, c, curvature, derivative, dm, em, eye, ma, matrix,
    md, mm, mr, ms, mul, power, scale, shift, to_raw, transformed,
    variable, zeros,
)

ROOT = Path(__file__).resolve().parents[1]
RESULT = Path(__file__).with_name("COUNTING_EMK_SEAM_RESULT.json")
PINS = ROOT / "research/lambda_counting/SE43_SOURCE_PINS.json"


def translate(poly, steps):
    for slot, step in enumerate(steps, 1):
        poly = shift(poly, slot, c(step))
    return poly


def tm(a, steps):
    return [[translate(p, steps) for p in row] for row in a]


def compose(left, right):
    g, steps = left
    k, next_steps = right
    return mm(g, tm(k, steps)), tuple(a+b for a, b in zip(steps, next_steps))


def inverse(lift, coefficient_inverse):
    g, steps = lift
    assert mm(g, coefficient_inverse) == mm(coefficient_inverse, g) == eye(len(g))
    back = tuple(-x for x in steps)
    return tm(coefficient_inverse, back), back


def act(lift, state):
    return mm(lift[0], tm(state, lift[1]))


def compatibility(connection, lift):
    g, steps = lift
    return [ma(md(g, i+1), mm(a, g), ms(c(-1), mm(g, tm(a, steps))))
            for i, a in enumerate(connection)]


def change_frame(lift, h, hi):
    g, steps = lift
    return mm(mm(hi, g), tm(h, steps)), steps


def defect(left, right):
    a, steps_a = compose(left, right)
    b, steps_b = compose(right, left)
    assert steps_a == steps_b
    return ma(a, ms(c(-1), b))


def acquire(left, right, cut, unit_depth, name):
    n = len(cut)
    complement = ma(eye(n), ms(c(-1), cut))
    assert mm(cut, cut) == cut
    orders = {"12": compose(left, right), "21": compose(right, left)}
    assert orders["12"][1] == orders["21"][1]
    readings = []
    for k in range(n):
        probe = [[c(j == k)] for j in range(n)]
        row = {"probe": k}
        for label, lift in orders.items():
            response = act(lift, probe)
            row[label] = {
                "accepted": em(mr(mm(cut, response), unit_depth)),
                "complement": em(mr(mm(complement, response), unit_depth)),
            }
        readings.append(row)
    return {"source": name, "labels": LABELS, "rank": n,
            "unit_depth": unit_depth, "cut": em(mr(cut, unit_depth)),
            "common_translation": [str(x) for x in orders["12"][1]],
            "word_convention": "12 = T1 T2; T2 acts first",
            "readings": readings}


def decode_bank(packet):
    """Decoder takes detached responses, without connection/seam matrices."""
    if packet["labels"] != LABELS:
        raise ValueError("counting labels differ")
    n, depth = packet["rank"], packet["unit_depth"]
    if packet["word_convention"] != "12 = T1 T2; T2 acts first":
        raise ValueError("unknown word orientation")
    if sorted(row["probe"] for row in packet["readings"]) != list(range(n)):
        raise ValueError("incomplete or repeated probe bank")
    if depth is not None and (type(depth) is not int or depth < 0):
        raise ValueError("invalid memory depth")
    if len(packet["common_translation"]) != 3:
        raise ValueError("missing scalar displacement")
    tuple(F(x) for x in packet["common_translation"])
    cut = dm(packet["cut"])
    if len(cut) != n or any(len(row) != n for row in cut):
        raise ValueError("invalid cut shape")
    if mr(mm(cut, cut), depth) != cut:
        raise ValueError("not an idempotent memory cut")
    out = zeros(n)
    for row in packet["readings"]:
        full = {}
        for order in ("12", "21"):
            accepted = dm(row[order]["accepted"])
            complement = dm(row[order]["complement"])
            if any(len(a) != n or any(len(r) != 1 for r in a)
                   for a in (accepted, complement)):
                raise ValueError("invalid response shape")
            total = ma(accepted, complement)
            if mr(total, depth) != total:
                raise ValueError("response exceeds labelled depth")
            if mr(mm(cut, total), depth) != accepted:
                raise ValueError("reading does not respect the supplied cut")
            full[order] = total
        delta = ma(full["12"], ms(c(-1), full["21"]))
        for i in range(n):
            out[i][row["probe"]] = delta[i][0]
    return out


def heisenberg(a, b, d):
    return matrix([[1, a, d], [0, 1, b], [0, 0, 1]])


def acquire_integer(a):
    return {"e2": em(mm(a, matrix([[0], [1], [0]]))),
            "e3": em(mm(a, matrix([[0], [0], [1]])))}


def decode_integer(packet):
    e2, e3 = dm(packet["e2"]), dm(packet["e3"])
    if (e2[1:] != matrix([[1], [0]]) or e3[2:] != matrix([[1]])):
        raise ValueError("not the declared integer path sector")
    polynomials = [e2[0][0], e3[1][0], e3[0][0]]
    ans = []
    for p in polynomials:
        coeff = p.get((0,)*6, F(0))
        if p != c(coeff) or coeff.denominator != 1:
            raise ValueError("not a constant integer reading")
        ans.append(int(coeff))
    return tuple(ans)


def build():
    checks, packets = [], []

    def check(name, truth, negative=False):
        if not truth:
            raise ArithmeticError(name)
        checks.append({"name": name, "kind": "negative" if negative else "positive",
                       "status": "PASS"})

    lam, x, y = variable(0), variable(1), variable(2)
    l1, l2, neutral = (F(2), F(0), F(0)), (F(0), F(3), F(0)), (F(0),)*3
    f = add(power(x, 4), mul(lam, x, y), scale(F(2, 3), power(y, 2)))
    k = add(power(x, 2), y, lam)
    check("native translation preserves the counting formula product",
          translate(mul(f, k), l1) == mul(translate(f, l1), translate(k, l1)))
    check("count translations commute and have their exact inverse",
          translate(translate(f, l1), l2) == translate(translate(f, l2), l1)
          and translate(translate(f, l1), tuple(-a for a in l1)) == f)
    check("count derivatives intertwine each seam displacement",
          all(derivative(translate(f, l1), i) == translate(derivative(f, i), l1)
              for i in (1, 2, 3)))
    term, expansion = f, {}
    for n in range(5):
        expansion = add(expansion, scale(F(2)**n / factorial(n), term))
        term = derivative(term, 1)
    check("the finite lowering exponential is exactly the native translation",
          expansion == translate(f, l1))
    raw_difference = add(shift(to_raw(power(x, 2)), 1, c(2)),
                         scale(-1, to_raw(power(add(x, c(2)), 2))))
    check("raw x translation fails the native product law by minus Lambda L",
          raw_difference == scale(-2, lam) and raw_difference != {}, True)

    n = matrix([[0, 1], [0, 0]])
    m = matrix([[0, 0], [1, 0]])
    identity = eye(2)
    h, hi = ma(identity, ms(x, m)), ma(identity, ms(scale(-1, x), m))
    H, Hi = ma(identity, n), ma(identity, ms(c(-1), n))
    base = [zeros(2) for _ in range(3)]
    moving_connection = transformed(base, h, hi)
    original = (H, l1)
    moving = change_frame(original, h, hi)
    # Inverse of hi H tau(h), as a coefficient matrix at the same base point.
    moving_inv_g = mm(mm(tm(hi, l1), Hi), h)
    check("moving seam coefficients have a two-sided polynomial inverse",
          mm(moving[0], moving_inv_g) == mm(moving_inv_g, moving[0]) == identity)
    check("the actual endpoint-frame seam intertwines the moving connection",
          compatibility(moving_connection, moving) == [zeros(2)]*3)
    check("the moving count connection is flat while the seam H is not identity",
          all(curvature(moving_connection, i, j) == zeros(2)
              for i, j in ((0, 1), (0, 2), (1, 2))) and H != identity, True)
    s = [[f], [k]]
    check("simultaneous frame transport preserves the full semilinear action",
          act(moving, s) == mm(hi, act(original, mm(h, s))))
    wrong_endpoint = (mm(mm(hi, H), h), l1)
    check("omitting the translated endpoint frame changes the actual reading",
          act(wrong_endpoint, s) != mm(hi, act(original, mm(h, s))), True)
    check("omitting the connection derivative term breaks compatibility",
          compatibility(base, moving) != [zeros(2)]*3, True)
    backward = inverse(moving, moving_inv_g)
    check("the semilinear inverse reverses scalar displacement as well as fibre",
          compose(moving, backward) == compose(backward, moving) == (identity, neutral))
    squared = compose(moving, moving)
    cubed = compose(squared, moving)
    check("ordered seam cocycles compose without resetting intermediate frames",
          cubed == compose(moving, squared)
          and act(cubed, s) == act(moving, act(moving, act(moving, s))))
    wrong_inverse = (moving_inv_g, tuple(-a for a in l1))
    check("unshifted coefficient inversion is not a semilinear inverse",
          compose(moving, wrong_inverse) != (identity, neutral), True)
    scalar_connection = [zeros(1), [[x]], zeros(1)]
    check("an identity seam does not descend a nonperiodic connection",
          compatibility(scalar_connection, (eye(1), l1)) != [zeros(1)]*3, True)

    G1, G2 = heisenberg(1, 0, 0), heisenberg(0, 1, 0)
    G1i, G2i = heisenberg(-1, 0, 0), heisenberg(0, -1, 0)
    first, second = (G1, l1), (G2, l2)
    unit3, z3 = eye(3), zeros(3)
    e13 = matrix([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
    zero_connection = [z3]*3
    delta = defect(first, second)
    relative = mm(mm(mm(G1, G2), G1i), G2i)
    check("each constant seam separately respects every flat count direction",
          compatibility(zero_connection, first) == compatibility(zero_connection, second) == [z3]*3)
    check("flat local lifts can fail the two-period relation exactly",
          delta == e13 and relative == ma(unit3, e13) and relative != unit3, True)
    commuting = (heisenberg(0, 0, 2), l2)
    check("commuting retained seam generators pass the two-period relation",
          defect(first, commuting) == z3)
    h3 = ma(unit3, ms(add(x, y), matrix([[0, 0, 0], [0, 0, 0], [1, 0, 0]])))
    hi3 = ma(unit3, ms(scale(-1, add(x, y)), matrix([[0, 0, 0], [0, 0, 0], [1, 0, 0]])))
    moved1, moved2 = change_frame(first, h3, hi3), change_frame(second, h3, hi3)
    common = tuple(a+b for a, b in zip(l1, l2))
    moved_delta = defect(moved1, moved2)
    check("the open-order residue retains both endpoint frames",
          moved_delta == mm(mm(hi3, delta), tm(h3, common)))
    moved_b_inv = mm(mm(tm(hi3, common), mm(G1i, G2i)), h3)
    moved_relative = mm(compose(moved1, moved2)[0], moved_b_inv)
    check("the closed seam return transforms by one-frame conjugation",
          moved_relative == mm(mm(hi3, relative), h3))
    check("open residue is generally not a same-frame conjugate",
          moved_delta != mm(mm(hi3, delta), h3), True)

    # An independent symbolic multiplication check for the integer carrier,
    # using all six existing polynomial labels as the six scalar entries.
    aa, bb, cc, ap, bp, cp = [variable(i) for i in range(6)]
    left = [[c(1), aa, cc], [{}, c(1), bb], [{}, {}, c(1)]]
    right = [[c(1), ap, cp], [{}, c(1), bp], [{}, {}, c(1)]]
    expected = [[c(1), add(aa, ap), add(cc, cp, mul(aa, bp))],
                [{}, c(1), add(bb, bp)], [{}, {}, c(1)]]
    check("the retained integer multiplication has the ordered a b-prime cocycle",
          mm(left, right) == expected)
    integer_target = mm(mm(heisenberg(2, 0, 0), heisenberg(0, -3, 0)), relative)
    integer_packet = json.loads(json.dumps(acquire_integer(integer_target)))
    check("two complete labelled integer responses recover the path labels",
          decode_integer(integer_packet) == (2, -3, -5)
          and mm(integer_target, heisenberg(-2, 3, -1)) == unit3)
    loop_packet = json.loads(json.dumps(acquire_integer(relative)))
    check("the projected identity retains central integer memory one",
          decode_integer(loop_packet) == (0, 0, 1), True)
    cut = matrix([[0, 0, 0], [0, 1, 0], [0, 0, 1]])
    full_packet = acquire(first, second, cut, None, "SE43-flat-counting-noncommuting-seams")
    packets.append(full_packet)
    check("complete seam observer responses reconstruct the order residue",
          decode_bank(json.loads(json.dumps(full_packet))) == delta)
    check("accepted-only reading loses the retained central seam response",
          all(row["12"]["accepted"] == row["21"]["accepted"]
              for row in full_packet["readings"]) and delta != z3, True)
    moved_cut = mm(mm(hi3, cut), h3)
    moved_packet = acquire(moved1, moved2, moved_cut, None, "SE43-moving-frame-and-cut")
    packets.append(moved_packet)
    check("a moving observation cut still decodes both ordered endpoint frames",
          decode_bank(json.loads(json.dumps(moved_packet))) == moved_delta)

    e12 = matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    e23 = matrix([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
    deep1 = (ma(unit3, ms(power(lam, 2), e12)), l1)
    deep2 = (ma(unit3, ms(power(lam, 2), e23)), l2)
    deep_defect = defect(deep1, deep2)
    deep_packets = [acquire(deep1, deep2, cut, q, "SE43-unit-degree-two-seams") for q in (0, 3, 4)]
    packets.extend(deep_packets)
    check("the twice-coefficient-degree memory bound is sharp for the seam defect",
          deep_defect == ms(power(lam, 4), e13)
          and decode_bank(deep_packets[0]) == decode_bank(deep_packets[1]) == z3
          and decode_bank(deep_packets[2]) == deep_defect, True)
    check("labelled unit cuts commute with ordered composition and acquisition",
          all(mr(compose(deep1, deep2)[0], q) ==
              mr(compose((mr(deep1[0], q), l1), (mr(deep2[0], q), l2))[0], q)
              for q in range(5)))

    # These are the public G3 T1 deck constants. The compensator is tested
    # against that deck, not the different forward-lift map used in its T2.
    L, alpha, beta, sheet = F(5), F(3), F(2, 5), 2
    start = (F(1, 3), F(2), F(3, 7), 4)

    def deck(v, power_):
        u, phi, sigma, k_ = v
        return u+power_*L, phi-power_*alpha, sigma-power_*beta, k_-power_*sheet

    def compensated(v, sign):
        u, phi, sigma, _ = v
        return phi+sign*alpha*u/L, sigma+sign*beta*u/L

    check("plus compensators are invariant under the declared negative-fibre deck",
          all(compensated(deck(start, j), 1) == compensated(start, 1)
              for j in (-3, -1, 0, 1, 4)))
    bad_scale = compensated(deck(start, 1), -1)[1]-compensated(start, -1)[1]
    check("public G3 minus-compensator claim fails on its actual deck map",
          bad_scale == -F(4, 5), True)
    forward = (start[0]+L, start[1]+alpha, start[2]+beta, start[3]+sheet)
    check("the source minus compensator belongs to the different forward lift",
          compensated(forward, -1) == compensated(start, -1))

    return {"stage": "SE43", "author": "Monty", "labels": LABELS,
            "scope": "Exact supplied counting/seam coefficient readings. No universal TVSP double-helix identification, physical measurement or RH sign.",
            "raw_translation_product_defect": em([[raw_difference]]),
            "moving_connection": [em(a) for a in moving_connection],
            "moving_seam": em(moving[0]), "moving_seam_inverse": em(moving_inv_g),
            "flat_seam_order_defect": em(delta), "flat_seam_relative_return": em(relative),
            "integer_readings": {"general_word": integer_packet, "central_word": loop_packet},
            "reading_packets": packets,
            "deck_audit": {"L": str(L), "alpha": str(alpha), "beta": str(beta),
                           "q": sheet, "wrong_compensator_scale_change": str(bad_scale),
                           "correct_compensator_scale_change": "0"},
            "checks": checks, "check_count": len(checks),
            "negative_control_count": sum(x["kind"] == "negative" for x in checks)}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+"\n")
    if args.check:
        for pin in json.loads(PINS.read_text())["local_files"]:
            if hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() != pin["sha256"]:
                raise ArithmeticError("source pin mismatch: "+pin["path"])
        archived = json.loads(RESULT.read_text())
        if result != archived:
            raise ArithmeticError("saved seam readings differ from exact replay")
        for packet in archived["reading_packets"]:
            decode_bank(packet)
    print(f"PASS SE43: {result['check_count']} exact controls; "
          f"{result['negative_control_count']} negative controls; "
          f"archive={'matched' if args.check else 'written' if args.write else 'not requested'}")


if __name__ == "__main__":
    main()
