"""SE41 detached native-return readings in an exact finite representation.

Python 3.12. This reuses the existing rational adapter; it is not a new
native algebra engine, a physical measurement, or an RH certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from proof_lab.endpoint_observer_index_certificate import (
    add, diag, eye, inertia, inv, mat, mul, rank, scale, tr,
)

RESULT = Path(__file__).with_name("ORDERED_RETURN_FEEDBACK_RESULT.json")
ROOT = Path(__file__).resolve().parents[1]
PINS = ROOT / "research/lambda_counting/SE41_SOURCE_PINS.json"


def zero(n):
    return scale(F(0), eye(n))


def power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mul(out, a)
    return out


def conjugate(a, g):
    return mul(mul(inv(g), a), g)


def realify(a, b):
    """Real representation of a+iota*b, with central iota retained."""
    n = len(a)
    return [a[i] + [-x for x in b[i]] for i in range(n)] + [
        b[i] + a[i] for i in range(n)
    ]


def cayley(t):
    return mul(add(eye(len(t)), t), inv(add(eye(len(t)), t, -1)))


def chart(w):
    return mul(add(w, eye(len(w)), -1), inv(add(w, eye(len(w)))))


def odd(w):
    return scale(F(1, 2), add(w, inv(w), -1))


def correction(e):
    ident = eye(len(e))
    return mul(inv(add(ident, scale(F(1, 2), e))),
               add(ident, scale(F(-1, 2), e)))


def psi(t):
    return mul(scale(F(-1), power(t, 3)),
               inv(add(eye(len(t)), scale(F(-2), power(t, 2)))))


def psd(a):
    return a == tr(a) and inertia(a)[0] == 0


def unitary(a):
    return mul(tr(a), a) == eye(len(a))


def squared_norm_at_most(a, bound):
    return psd(add(scale(bound * bound, eye(len(a))), mul(tr(a), a), -1))


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def acquire(w, p, source_id, word, frame):
    """Finite fixture sensor: accepted and complementary output per probe."""
    q = add(eye(len(p)), p, -1)
    accepted, complement = mul(p, w), mul(q, w)
    rows = [{"probe": j, "accepted": [r[j] for r in accepted],
             "complement": [r[j] for r in complement]}
            for j in range(len(w))]
    packet = {"source_id": source_id, "ordered_word": word,
              "frame": frame, "cut": p, "readings": rows}
    return json.loads(json.dumps(encode(packet)))


def decode(packet):
    """Consumes only detached readings and sensor calibration metadata."""
    p = mat(packet["cut"])
    n = len(p)
    if len(packet["readings"]) != n:
        raise ValueError("incomplete probe bank")
    q, out = add(eye(n), p, -1), zero(n)
    labels = set()
    for reading in packet["readings"]:
        j = reading["probe"]
        if j in labels or j not in range(n) or "complement" not in reading:
            raise ValueError("missing complementary reading or probe label")
        labels.add(j)
        a = [[F(x)] for x in reading["accepted"]]
        b = [[F(x)] for x in reading["complement"]]
        if mul(p, a) != a or mul(q, b) != b:
            raise ValueError("reading does not lie in its declared channel")
        for i in range(n):
            out[i][j] = a[i][0] + b[i][0]
    return out


def central_rechart(w, central_iota):
    """For a complex d-carrier represented on 2d real coordinates."""
    assert mul(w, central_iota) == mul(central_iota, w)
    d, ranks = len(w) // 2, []
    for j in range(d + 1):
        phase = cayley(scale(F(j), central_iota))
        candidate = add(w, phase)
        ranks.append(rank(candidate))
        if ranks[-1] == len(w):
            return phase, mul(inv(phase), w), j, ranks
    raise ArithmeticError("finite branch-repair theorem violated")


def poly_mul(a, b):
    """Independent, finite truncated coefficient witness, not engine code."""
    n, d = len(a), len(a[0])
    out = [zero(d) for _ in range(n)]
    for k in range(n):
        for j in range(k + 1):
            out[k] = add(out[k], mul(a[j], b[k-j]))
    return out


def poly_add(a, b, sign=1):
    return [add(x, y, sign) for x, y in zip(a, b)]


def poly_scale(c, a):
    return [scale(c, x) for x in a]


def poly_unit(a):
    return [eye(len(a[0]))] + [zero(len(a[0])) for _ in a[1:]]


def poly_inverse_unit(a):
    assert a[0] == eye(len(a[0]))
    ident = poly_unit(a)
    residue = poly_add(ident, a, -1)
    out, term = ident, ident
    for _ in range(1, len(a)):
        term = poly_mul(term, residue)
        out = poly_add(out, term)
    return out


def poly_order(a):
    return next((j for j, coefficient in enumerate(a)
                 if coefficient != zero(len(coefficient))), None)


def build():
    checks, packets = [], []

    def check(name, condition, negative=False):
        if not condition:
            raise ArithmeticError(name)
        checks.append({"name": name, "status": "PASS",
                       "kind": "negative" if negative else "positive"})

    r2, k2 = mat([[0, -1], [1, 0]]), diag([1, -1])
    r = realify(r2, zero(2))
    k = realify(k2, zero(2))
    ik = realify(zero(2), k2)
    central_iota = realify(zero(2), eye(2))
    ident, p = eye(4), diag([1, 0, 1, 0])
    check("EMK relations and the distinct central iota are represented exactly",
          power(r, 2) == scale(-1, ident) and power(k, 2) == ident
          and mul(r, k) == scale(-1, mul(k, r))
          and mul(central_iota, r) == mul(r, central_iota)
          and mul(central_iota, k) == mul(k, central_iota))

    a, b = cayley(scale(F(1, 2), r)), cayley(scale(F(1, 3), ik))
    word = ["R_step", "iotaK_step", "R_step_inverse", "iotaK_step_inverse"]
    source = ident
    for segment in [a, b, inv(a), inv(b)]:
        source = mul(segment, source)
    check("noncommuting native arrows yield a nontrivial unitary ordered return",
          mul(a, b) != mul(b, a) and source != ident and unitary(source))
    reversed_source = inv(source)
    check("same spectral power traces do not recover ordered loop direction",
          source != reversed_source and all(
              sum(power(source, j)[i][i] for i in range(4)) ==
              sum(power(reversed_source, j)[i][i] for i in range(4))
              for j in range(1, 5)), True)

    packet = acquire(source, p, "SE41-native-ordered-return", word, ident)
    packets.append(packet)
    decoded = decode(packet)
    check("detached accepted and complementary readings recover the actual return",
          decoded == source)
    incomplete = json.loads(json.dumps(packet))
    for row in incomplete["readings"]:
        del row["complement"]
    try:
        decode(incomplete)
        refused = False
    except ValueError:
        refused = True
    check("missing complement is refused rather than filled from the target", refused, True)

    wp, wm = cayley(scale(F(1, 2), r)), cayley(scale(F(-1, 2), r))
    q = add(ident, p, -1)
    check("opposite turns collide on accepted compression but separate on complement",
          mul(mul(p, wp), p) == mul(mul(p, wm), p)
          and mul(mul(q, wp), p) != mul(mul(q, wm), p)
          and mul(mul(p, odd(wp)), p) == zero(4), True)

    antipode = scale(-1, ident)
    check("antipodal sine silence has the wrong symmetric reading and singular chart",
          odd(antipode) == zero(4)
          and scale(F(1, 2), add(antipode, inv(antipode))) == antipode
          and rank(add(antipode, ident)) == 0, True)
    phase, w, chosen, ranks = central_rechart(antipode, central_iota)
    check("central phase repairs the antipode and preserves the original source",
          chosen == 1 and mul(phase, w) == antipode and unitary(w))
    hard = realify(diag([-1, 0]), diag([0, -1]))
    hard_packet = acquire(hard, p, "SE41-two-forbidden-charts", [], ident)
    phase_h, w_h, chosen_h, ranks_h = central_rechart(decode(hard_packet), central_iota)
    check("two forbidden phase charts require the third candidate on a rank-two carrier",
          chosen_h == 2 and ranks_h[:2] == [2, 2] and ranks_h[2] == 4
          and mul(phase_h, w_h) == hard)

    first_t = chart(decoded)
    first_q = correction(odd(decoded))
    first_w = mul(first_q, decoded)
    check("independent return update gives the cubic operator Cayley identity",
          chart(first_w) == psi(first_t) and unitary(first_q)
          and tr(first_t) == scale(-1, first_t))

    # The exact target is held fixed; only calibration and its frame move.
    frames = [ident, a, mul(b, a), mul(a, b)]
    cuts = [p, conjugate(p, b), conjugate(p, a), conjugate(p, mul(a, b))]
    calibration, w_current = ident, decoded
    bound = max(sum(abs(x) for x in row) for row in first_t)
    history = []
    good_identity = good_bounds = good_frames = True
    for n in range(3):
        frame, next_frame = frames[n], frames[n+1]
        observed_cut = conjugate(cuts[n], frame)
        observed_w = conjugate(w_current, frame)
        data = acquire(observed_w, observed_cut, packet["source_id"], word, frame)
        packets.append(data)
        observed_w = decode(data)
        t = chart(observed_w)
        cq = correction(odd(observed_w))
        change = mul(inv(frame), next_frame)
        observed_calibration = conjugate(calibration, frame)
        next_w = conjugate(mul(cq, observed_w), change)
        next_calibration = conjugate(mul(observed_calibration, inv(cq)), change)
        next_t = chart(next_w)
        good_identity &= mul(next_calibration, next_w) == conjugate(source, next_frame)
        good_frames &= next_t == conjugate(psi(t), change)
        bound = bound**3 / (1 + 2 * bound**2)
        good_bounds &= squared_norm_at_most(next_t, bound)
        good_bounds &= squared_norm_at_most(add(conjugate(source, next_frame),
                                                  next_calibration, -1), 2*bound)
        history.append({"step": n+1, "cayley_norm_upper": bound,
                        "reconstruction_error_upper": 2*bound,
                        "calibration": next_calibration, "residue": next_w})
        calibration = conjugate(next_calibration, inv(next_frame))
        w_current = conjugate(next_w, inv(next_frame))
    check("every moving-cut reading predicts the next transported residue", good_frames)
    check("every moving calibration retains the same fixed ordered source", good_identity)
    check("exact inertia verifies contraction and reconstruction-error bounds", good_bounds)
    check("corrected near-identity residue retains a nonidentity source in calibration",
          source != ident and calibration != ident
          and mul(calibration, w_current) == source)
    check("dropping the between-frame transport changes the predicted next reading",
          psi(first_t) != conjugate(psi(first_t), a), True)
    check("wrong calibration multiplier fails source reconstruction",
          mul(first_q, first_w) != source, True)

    # Frame covariance includes a non-orthonormal representation with its metric.
    g = diag([2, 3, 2, 3])
    h = mul(tr(g), g)
    moved = conjugate(source, g)
    moved_t = conjugate(first_t, g)
    check("nonorthonormal frame retains metric unitarity and feedback covariance",
          mul(mul(tr(moved), h), moved) == h
          and psi(moved_t) == conjugate(psi(first_t), g))

    # NT-6: compression has a hidden complement-return correction.
    l = mul(r, k)
    raw = add(mul(r, l), mul(l, r), -1)
    compressed_raw = mul(mul(p, raw), p)
    hidden = add(mul(mul(mul(mul(p, l), q), r), p),
                 mul(mul(mul(mul(p, r), q), l), p), -1)
    check("NT-6 hidden return cancels compressed curvature while full curvature survives",
          raw == scale(-2, k) and compressed_raw == scale(-2, p)
          and add(compressed_raw, hidden) == zero(4), True)

    # Noise in a noncommuting skew channel; correct order is Qhat W.
    epsilon = F(1, 20)
    e = odd(decoded)
    ehat = add(e, scale(epsilon, r))
    qhat = correction(ehat)
    noisy_w = mul(qhat, decoded)
    check("noisy skew readout keeps the actual calibration identity in the correct order",
          unitary(qhat) and mul(inv(qhat), noisy_w) == source
          and mul(inv(qhat), mul(decoded, qhat)) != source)
    check("measured skew error controls the next actual return",
          squared_norm_at_most(add(noisy_w, first_w, -1), epsilon))
    margin = F(1, 2)
    plus = add(first_w, ident)
    margin_valid = psd(add(mul(tr(plus), plus), scale(margin**2, ident), -1))
    noise_bound = 2*epsilon / (margin*(margin-epsilon))
    check("a verified chart margin controls the noisy Cayley coordinate",
          margin_valid and epsilon < margin
          and squared_norm_at_most(add(chart(noisy_w), chart(first_w), -1), noise_bound))

    hyper = scale(F(2, 3), k)
    check("the hyperbolic sector rejects a universal convergence claim",
          psi(hyper) == scale(F(-8, 3), k) and not unitary(cayley(hyper)), True)

    scalar_history, scalar = [], F(1)
    for _ in range(4):
        scalar_history.append(scalar)
        check_t = scale(scalar, r)
        expected = scalar**3/(1+2*scalar**2)
        assert psi(check_t) == scale(expected, r)
        scalar = expected
    check("the pure rotational sector has the stated exact scalar sequence",
          scalar_history == [F(1), F(1, 3), F(1, 33), F(1, 36003)])

    # Noncommuting coefficient memory through Lambda^10.
    t = [zero(4) for _ in range(11)]
    t[1], t[2] = r, ik
    unit = poly_unit(t)
    poly_w = poly_mul(poly_add(unit, t), poly_inverse_unit(poly_add(unit, t, -1)))
    target, estimate, orders = poly_w, unit, [poly_order(t)]
    memory_ok = True
    for _ in range(3):
        inverse_w = poly_mul(poly_add(unit, t, -1), poly_inverse_unit(poly_add(unit, t)))
        pe = poly_scale(F(1, 2), poly_add(poly_w, inverse_w, -1))
        pq = poly_mul(poly_inverse_unit(poly_add(unit, poly_scale(F(1, 2), pe))),
                      poly_add(unit, poly_scale(F(-1, 2), pe)))
        estimate = poly_mul(estimate, poly_inverse_unit(pq))
        poly_w = poly_mul(pq, poly_w)
        t3 = poly_mul(poly_mul(t, t), t)
        tnext = poly_mul(poly_scale(F(-1), t3),
                         poly_inverse_unit(poly_add(unit, poly_scale(F(-2), poly_mul(t, t)))))
        actual_t = poly_mul(poly_add(poly_w, unit, -1),
                            poly_inverse_unit(poly_scale(F(1, 2), poly_add(poly_w, unit))))
        actual_t = poly_scale(F(1, 2), actual_t)
        memory_ok &= actual_t == tnext and poly_mul(estimate, poly_w) == target
        t = tnext
        orders.append(poly_order(t))
    check("noncommuting coefficient memory has orders 1, 3, 9, then vanishes at depth ten",
          mul(r, ik) != mul(ik, r) and orders == [1, 3, 9, None])
    check("formal feedback retains all source coefficients and recovers the depth-ten target",
          memory_ok and estimate == target)

    loop = power(r, 4)
    check("endpoint identity does not distinguish a full turn from the empty word",
          loop == ident and ["R", "R", "R", "R"] != [], True)

    return encode({
        "stage": "SE41", "owner": "Monty",
        "scope": "Detached readings of supplied finite native return models; no physical acquisition, RH or universal curvature-flatness claim.",
        "source": {"word": word, "return": source, "reverse_return": reversed_source},
        "reading_packets": packets, "feedback_history": history,
        "branch_repair": {"antipode_candidate": chosen, "antipode_ranks": ranks,
                          "hard_packet": hard_packet, "chosen_candidate": chosen_h,
                          "candidate_ranks": ranks_h, "phase": phase_h,
                          "residue": w_h},
        "noise": {"epsilon": epsilon, "chart_margin_lower": margin,
                  "coordinate_error_upper": noise_bound},
        "scalar_sequence": scalar_history, "unit_orders": orders,
        "checks": checks, "check_count": len(checks),
        "negative_control_count": sum(c["kind"] == "negative" for c in checks),
    })


def main():
    parser = argparse.ArgumentParser()
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument("--write", action="store_true")
    choice.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2) + "\n")
    if args.check:
        for pin in json.loads(PINS.read_text())["local_files"]:
            actual = hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest()
            if actual != pin["sha256"]:
                raise ArithmeticError("source pin mismatch: " + pin["path"])
        if json.loads(RESULT.read_text()) != result:
            raise ArithmeticError("saved observer readings do not match replay")
    print(f"PASS SE41: {result['check_count']} exact controls; "
          f"{result['negative_control_count']} negative controls; "
          f"archive={'matched' if args.check else 'written' if args.write else 'not requested'}")


if __name__ == "__main__":
    main()
