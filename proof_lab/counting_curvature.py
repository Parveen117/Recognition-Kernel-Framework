"""SE42 exact observer fixtures in the admitted counting-coefficient chart.

Python 3.12 only; standard-library rational polynomials. The small fixed
six-label arithmetic below evaluates finite witnesses, not a replacement
native operator engine. No numerical spectral or exponential routine is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = Path(__file__).with_name("COUNTING_CURVATURE_RESULT.json")
PINS = ROOT / "research/lambda_counting/SE42_SOURCE_PINS.json"
LABELS = ["Lambda", "count_1", "count_2", "count_3", "step_a", "step_b"]
ZERO_KEY = (0,) * 6


def c(value):
    value = F(value)
    return {ZERO_KEY: value} if value else {}


def variable(i):
    key = [0] * 6
    key[i] = 1
    return {tuple(key): F(1)}


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(value, poly):
    return {key: F(value) * coeff for key, coeff in poly.items()
            if value * coeff}


def mul(*polys):
    out = c(1)
    for poly in polys:
        nxt = {}
        for left, av in out.items():
            for right, bv in poly.items():
                key = tuple(a + b for a, b in zip(left, right))
                nxt[key] = nxt.get(key, F(0)) + av * bv
        out = {key: value for key, value in nxt.items() if value}
    return out


def power(poly, n):
    out = c(1)
    for _ in range(n):
        out = mul(out, poly)
    return out


def derivative(poly, i):
    out = {}
    for key, value in poly.items():
        if key[i]:
            changed = list(key)
            changed[i] -= 1
            out[tuple(changed)] = value * key[i]
    return out


def retain(poly, unit=None, steps=None):
    return {key: value for key, value in poly.items()
            if (unit is None or key[0] <= unit)
            and (steps is None or (key[4] <= steps and key[5] <= steps))}


def shift(poly, i, displacement):
    out = {}
    for key, value in poly.items():
        rest = list(key)
        exponent, rest[i] = rest[i], 0
        for k in range(exponent + 1):
            term = mul({tuple(rest): value * comb(exponent, k)},
                       power(variable(i), k), power(displacement, exponent-k))
            out = add(out, term)
    return out


def to_raw(poly):
    """U: normal count powers to actual falling-count x polynomials."""
    out, unit = {}, variable(0)
    for key, value in poly.items():
        rest = list(key)
        rest[1:4] = [0, 0, 0]
        term = {tuple(rest): value}
        for i in range(1, 4):
            for j in range(key[i]):
                term = mul(term, add(variable(i), scale(-j, unit)))
        out = add(out, term)
    return out


def raw_lower(poly, i):
    difference = add(shift(poly, i, variable(0)), scale(-1, poly))
    assert all(key[0] >= 1 for key in difference)
    return {tuple([key[0]-1] + list(key[1:])): value
            for key, value in difference.items()}


def zeros(rows, cols=None):
    return [[{} for _ in range(rows if cols is None else cols)] for _ in range(rows)]


def eye(n):
    return [[c(i == j) for j in range(n)] for i in range(n)]


def matrix(rows):
    return [[c(x) for x in row] for row in rows]


def ma(*matrices):
    return [[add(*(a[i][j] for a in matrices)) for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def ms(poly, a):
    return [[mul(poly, x) for x in row] for row in a]


def mm(a, b):
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def md(a, i):
    return [[derivative(x, i) for x in row] for row in a]


def mr(a, unit=None, steps=None):
    return [[retain(x, unit, steps) for x in row] for row in a]


def bracket(a, b):
    return ma(mm(a, b), ms(c(-1), mm(b, a)))


def nabla(a, i, state):
    return ma(md(state, i+1), mm(a[i], state))


def curvature(a, i, j):
    return ma(md(a[j], i+1), ms(c(-1), md(a[i], j+1)), bracket(a[i], a[j]))


def covariant(a, i, field):
    return ma(md(field, i+1), bracket(a[i], field))


def transformed(a, g, gi):
    return [ma(mm(gi, md(g, i+1)), mm(mm(gi, a[i]), g)) for i in range(len(a))]


def flow(a, i, state, parameter, sign=1, depth=2):
    out, term = state, state
    for n in range(1, depth+1):
        term = nabla(a, i, term)
        coeff = scale(F(sign**n, factorial(n)), power(variable(parameter), n))
        out = ma(out, ms(coeff, term))
    return mr(out, steps=depth)


def loop(a, i, j, state, depth=2):
    state = flow(a, j, state, 5, -1, depth)
    state = flow(a, i, state, 4, -1, depth)
    state = flow(a, j, state, 5, 1, depth)
    return flow(a, i, state, 4, 1, depth)


def step_coefficient(poly, a, b):
    out = {}
    for key, value in poly.items():
        if key[4:] == (a, b):
            out[key[:4] + (0, 0)] = value
    return out


def mixed(a):
    return [[step_coefficient(x, 1, 1) for x in row] for row in a]


def encode(poly):
    return [{"powers": list(key), "coefficient": str(value)}
            for key, value in sorted(poly.items())]


def decode(poly):
    out = {}
    for term in poly:
        key = tuple(term["powers"])
        if len(key) != 6 or any(type(k) is not int or k < 0 for k in key) or key in out:
            raise ValueError("invalid or duplicate count label")
        out[key] = F(term["coefficient"])
    return {key: value for key, value in out.items() if value}


def em(a):
    return [[encode(x) for x in row] for row in a]


def dm(a):
    return [[decode(x) for x in row] for row in a]


def acquire(a, i, j, p, unit_depth, source):
    n, q = len(p), ma(eye(len(p)), ms(c(-1), p))
    rows = []
    for index in range(n):
        probe = [[c(k == index)] for k in range(n)]
        u, v = nabla(a, i, nabla(a, j, probe)), nabla(a, j, nabla(a, i, probe))
        rows.append({"probe": index,
                     "ij": {"accepted": em(mr(mm(p, u), unit_depth)),
                            "complement": em(mr(mm(q, u), unit_depth))},
                     "ji": {"accepted": em(mr(mm(p, v), unit_depth)),
                            "complement": em(mr(mm(q, v), unit_depth))}})
    return {"source": source, "labels": LABELS, "directions": [i+1, j+1],
            "cut": em(mr(p, unit_depth)), "unit_depth": unit_depth, "readings": rows}


def decode_bank(packet):
    """Read only the detached two-path responses and their metadata."""
    p, depth = dm(packet["cut"]), packet["unit_depth"]
    n, labels, out = len(p), set(), zeros(len(p))
    q = ma(eye(n), ms(c(-1), p))
    if mr(mm(p, p), depth) != p or len(packet["readings"]) != n:
        raise ValueError("invalid cut or incomplete bank")
    for row in packet["readings"]:
        index = row["probe"]
        if index not in range(n) or index in labels:
            raise ValueError("missing or duplicate probe")
        labels.add(index)
        paths = []
        for order in ["ij", "ji"]:
            if "complement" not in row[order]:
                raise ValueError("missing complementary path response")
            accepted, complement = dm(row[order]["accepted"]), dm(row[order]["complement"])
            if mr(mm(p, accepted), depth) != accepted or mr(mm(q, complement), depth) != complement:
                raise ValueError("response does not belong to its labelled channel")
            paths.append(ma(accepted, complement))
        difference = ma(paths[0], ms(c(-1), paths[1]))
        for k in range(n):
            out[k][index] = difference[k][0]
    return out


def build():
    checks, packets = [], []

    def check(name, condition, negative=False):
        if not condition:
            raise ArithmeticError(name)
        checks.append({"name": name, "status": "PASS",
                       "kind": "negative" if negative else "positive"})

    lam, x, y, z, a, b = [variable(i) for i in range(6)]
    one, ident = c(1), eye(2)
    n, m = matrix([[0, 1], [0, 0]]), matrix([[0, 0], [1, 0]])
    k, p = matrix([[1, 0], [0, -1]]), matrix([[1, 0], [0, 0]])
    f, h = add(power(x, 3), mul(lam, x, y), power(z, 2)), add(power(y, 2), x)
    check("tensor counting chart intertwines all three actual lowering actions",
          all(to_raw(derivative(f, i)) == raw_lower(to_raw(f), i) for i in range(1, 4)))
    check("counting formula multiplication has its derived Leibniz rule",
          all(derivative(mul(f, h), i) == add(mul(derivative(f, i), h), mul(f, derivative(h, i)))
              for i in range(1, 4)))
    check("ordinary x multiplication cannot replace the counting formula product",
          to_raw(power(x, 2)) == add(power(x, 2), scale(-1, mul(lam, x)))
          and to_raw(power(x, 2)) != mul(to_raw(x), to_raw(x)), True)

    connection = [ma(ms(y, n), ms(mul(lam, z), m)),
                  ma(ms(power(x, 2), m), ms(mul(lam, x), n)),
                  ma(ms(mul(y, z), k), ms(mul(power(lam, 2), x), m))]
    state = [[add(power(x, 2), mul(y, z))], [add(x, mul(lam, power(y, 2)))]]
    field = curvature(connection, 0, 1)
    direct = ma(nabla(connection, 0, nabla(connection, 1, state)),
                ms(c(-1), nabla(connection, 1, nabla(connection, 0, state))))
    check("nonlinear counting coefficients give the stated full path-curvature action",
          direct == mm(field, state) and field != zeros(2))
    ret = loop(connection, 0, 1, ident)
    check("independent formal loop action has the actual curvature as its mixed reading",
          mixed(ret) == field)
    check("closed formal return is linear over the counting formula algebra",
          loop(connection, 0, 1, ms(f, ident)) == ms(f, ret))

    central = [zeros(1), [[x]], zeros(1)]
    central_return = loop(central, 0, 1, eye(1), depth=3)
    expected = add(*(scale(F(1, factorial(j)), mul(power(a, j), power(b, j))) for j in range(4)))
    check("the derived D1 and D2-plus-X1 connection has unit curvature and central return",
          curvature(central, 0, 1) == eye(1) and central_return == [[expected]])
    hidden = [zeros(1), [[mul(power(lam, 3), x)]], zeros(1)]
    hidden_field = curvature(hidden, 0, 1)
    hidden_packets = [acquire(hidden, 0, 1, eye(1), q, "SE42-hidden-unit-layer") for q in (0, 2, 3)]
    packets.extend(hidden_packets)
    check("a flat shallow reading does not annihilate the full counting curvature",
          hidden_field == [[power(lam, 3)]] and decode_bank(hidden_packets[0]) == zeros(1)
          and decode_bank(hidden_packets[1]) == zeros(1), True)
    check("the first retained third unit layer recovers the hidden curvature",
          decode_bank(hidden_packets[2]) == hidden_field)
    check("the unit cut does not force the c-equals-one connection to be flat",
          mr(curvature(central, 0, 1), 0) == eye(1), True)

    constants = [n, m, zeros(2)]
    ab = mul(a, b)
    noncentral_expected = [[add(one, ab, power(ab, 2)), scale(-1, mul(power(a, 2), b))],
                           [mul(a, power(b, 2)), add(one, scale(-1, ab))]]
    noncentral_return = loop(constants, 0, 1, ident)
    check("noncentral native path generators retain the complete higher ordered return",
          noncentral_return == noncentral_expected and curvature(constants, 0, 1) == k)
    naive = ma(ident, ms(ab, k), ms(scale(F(1, 2), power(ab, 2)), ident))
    check("central exponential and trace-only shortcuts lose noncentral curvature data",
          noncentral_return != naive and add(k[0][0], k[1][1]) == {} and k != zeros(2), True)

    frame_coeff = add(mul(x, y), mul(lam, z))
    g, gi = ma(ident, ms(frame_coeff, n)), ma(ident, ms(scale(-1, frame_coeff), n))
    moved = transformed(connection, g, gi)
    check("a counting-dependent observer frame retains the conjugate curvature",
          mm(g, gi) == ident and curvature(moved, 0, 1) == mm(mm(gi, field), g))
    wrong = [mm(mm(gi, item), g) for item in connection]
    check("omitting the frame derivative gives the wrong transported curvature",
          curvature(wrong, 0, 1) != mm(mm(gi, field), g), True)
    moved_simple = transformed(constants, g, gi)
    check("full loop readings transport in a moving response frame",
          loop(moved_simple, 0, 1, ident) == mm(mm(gi, noncentral_return), g))

    pg = mm(ma(ident, ms(x, n)), ma(ident, ms(y, m)))
    pgi = mm(ma(ident, ms(scale(-1, y), m)), ma(ident, ms(scale(-1, x), n)))
    pure = transformed([zeros(2)] * 3, pg, pgi)
    check("a pure moving frame is flat with identity formal return",
          curvature(pure, 0, 1) == zeros(2) and loop(pure, 0, 1, ident) == ident)
    check("noncommuting coefficient matrices alone do not establish curvature",
          bracket(pure[0], pure[1]) != zeros(2) and curvature(pure, 0, 1) == zeros(2), True)

    def v1(s):
        return ma(nabla(connection, 0, s), ms(y, nabla(connection, 1, s)))

    raw_direction = ma(v1(nabla(connection, 1, state)),
                       ms(c(-1), nabla(connection, 1, v1(state))))
    corrected = ma(raw_direction, nabla(connection, 1, state))
    check("moving counting directions recover curvature after their bracket is subtracted",
          corrected == mm(field, state) and raw_direction != corrected)
    cyclic = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    bianchi = ma(*(covariant(connection, i, curvature(connection, j, t)) for i, j, t in cyclic))
    bare = ma(*(md(curvature(connection, j, t), i+1) for i, j, t in cyclic))
    check("ordered counting curvature satisfies its covariant Bianchi identity", bianchi == zeros(2))
    check("dropping response commutators breaks the same Bianchi reading", bare != zeros(2), True)

    moving_p = mm(mm(gi, p), g)
    kp = [covariant(moved_simple, i, moving_p) for i in range(2)]
    moved_field = curvature(moved_simple, 0, 1)
    projected = mm(mm(moving_p, moved_field), moving_p)
    correction = mm(mm(moving_p, bracket(kp[0], kp[1])), moving_p)
    check("moving-cut complement returns cancel compression without erasing full curvature",
          projected != zeros(2) and ma(projected, correction) == zeros(2)
          and moved_field != zeros(2), True)
    retained_state = mm(moving_p, state)

    def compressed(i, s):
        return mm(moving_p, nabla(moved_simple, i, s))

    compressed_action = ma(compressed(0, compressed(1, retained_state)),
                           ms(c(-1), compressed(1, compressed(0, retained_state))))
    check("the compressed-lift action matches the derived moving-cut formula",
          compressed_action == mm(ma(projected, correction), retained_state))
    packet = acquire(moved_simple, 0, 1, moving_p, 4, "SE42-moving-counting-frame")
    packets.append(packet)
    check("detached accepted and complement path readings decode every curvature column",
          decode_bank(json.loads(json.dumps(packet))) == moved_field)
    missing = json.loads(json.dumps(packet))
    del missing["readings"][0]["ij"]["complement"]
    try:
        decode_bank(missing)
        refused = False
    except ValueError:
        refused = True
    check("the decoder refuses an absent complement instead of assuming it neutral", refused, True)

    memory_ok = all(mr(field, q) == mr(curvature([mr(item, q) for item in connection], 0, 1), q)
                    for q in range(5))
    check("retained unit cuts commute with curvature in their convolution quotient", memory_ok)
    check("retained unit cuts commute with the independent formal loop computation",
          all(mr(loop(hidden, 0, 1, eye(1)), q)
              == mr(loop([mr(t, q) for t in hidden], 0, 1, eye(1)), q)
              for q in (0, 2, 3, 6))
          and mr(loop(hidden, 0, 1, eye(1)), 2) == eye(1))
    deep = [ms(power(lam, 2), n), ms(power(lam, 2), m), zeros(2)]
    deep_field = curvature(deep, 0, 1)
    check("the twice-coefficient-degree curvature memory bound is attained",
          deep_field == ms(power(lam, 4), k) and mr(deep_field, 3) == zeros(2)
          and mr(deep_field, 4) == deep_field)
    packet_nl = acquire(connection, 0, 1, p, 4, "SE42-polynomial-count-response")
    packets.append(packet_nl)
    check("the bounded unit-depth nonlinear-coefficient bank recovers the full curvature",
          decode_bank(packet_nl) == field)

    top, level = power(x, 3), 3
    clip = lambda poly: {key: val for key, val in poly.items() if key[1] <= level}
    lower = lambda poly: derivative(poly, 1)
    raise_ = lambda poly: mul(x, poly)
    compressed_commutator = add(clip(lower(clip(raise_(top)))), scale(-1, clip(raise_(clip(lower(top))))))
    check("finite counting windows retain their actual top-boundary defect",
          compressed_commutator == scale(-level, top)
          and add(compressed_commutator, scale(level+1, top)) == top, True)
    interior = power(x, 2)
    check("a count window with the required intermediate-state guard reads unit curvature",
          add(clip(lower(clip(raise_(interior)))), scale(-1, clip(raise_(clip(lower(interior)))))) == interior)

    return {"stage": "SE42", "author": "Monty", "labels": LABELS,
            "scope": "Exact supplied counting-coordinate observer readings; formal step coefficients only. No physical acquisition, RH sign or numerical exponential convergence.",
            "central_return_through_step_degree_3": em(central_return),
            "noncentral_return": em(noncentral_return),
            "polynomial_connection": [em(item) for item in connection],
            "polynomial_curvature": em(field), "frame": em(g), "frame_inverse": em(gi),
            "moving_cut": em(moving_p), "retained_curvature": em(projected),
            "complement_correction": em(correction), "reading_packets": packets,
            "sharp_unit_depth": {"connection_degree": 2, "required_curvature_degree": 4,
                                  "curvature": em(deep_field)},
            "checks": checks, "check_count": len(checks),
            "negative_control_count": sum(item["kind"] == "negative" for item in checks)}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2) + "\n")
    if args.check:
        for pin in json.loads(PINS.read_text())["local_files"]:
            if hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() != pin["sha256"]:
                raise ArithmeticError("source pin mismatch: " + pin["path"])
        if result != json.loads(RESULT.read_text()):
            raise ArithmeticError("saved observer readings differ from exact replay")
    print(f"PASS SE42: {result['check_count']} exact controls; "
          f"{result['negative_control_count']} negative controls; "
          f"archive={'matched' if args.check else 'written' if args.write else 'not requested'}")


if __name__ == "__main__":
    main()
