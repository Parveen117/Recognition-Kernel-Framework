"""SE44 exact native-angle/jya witnesses and detached observer readings.

Python 3.12. Existing rational and polynomial adapters are reused.
Transcendental values are enclosed by proved rational series remainders.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from proof_lab.endpoint_observer_index_certificate import add, eye, inv, mat, mul, scale, tr
from proof_lab.ordered_return_feedback import (
    acquire, cayley, decode, encode, poly_add, poly_inverse_unit,
    poly_mul, poly_unit, power, zero,
)
from proof_lab.counting_emk_seam import translate
from proof_lab import counting_curvature as cc

ROOT = Path(__file__).resolve().parents[1]
RESULT = Path(__file__).with_name("TVSP_NATIVE_JYA_RESULT.json")
PINS = ROOT / "research/lambda_counting/SE44_SOURCE_PINS.json"
J = mat([[0, -1], [1, 0]])  # Ordered basis (T,V), clockwise on the compass.


def qturn(r):
    return cayley(scale(F(r), J))


def dot(u, v, metric=None):
    metric = eye(len(u)) if metric is None else metric
    return mul(mul(tr(u), metric), v)[0][0]


def angle_interval(r, order):
    """Integral of 2/(1+t^2), enclosed by a geometric remainder."""
    r = F(r)
    if not 0 <= r <= 1:
        raise ValueError("native first-quarter calibration requires 0<=r<=1")
    value = sum((2*(-1)**k*r**(2*k+1)/F(2*k+1) for k in range(order+1)), F(0))
    next_term = 2*(-1)**(order+1)*r**(2*order+3)/F(2*order+3)
    return min(value, value+next_term), max(value, value+next_term)


def sine_interval(t, order=10):
    t = F(t)
    if not 0 <= t <= 1:
        raise ValueError("this finite sine enclosure has domain [0,1]")
    value = sum(((-1)**k*t**(2*k+1)/factorial(2*k+1) for k in range(order+1)), F(0))
    next_term = (-1)**(order+1)*t**(2*order+3)/factorial(2*order+3)
    return min(value, value+next_term), max(value, value+next_term)


def floor_dyadic(x, bits=128):
    return F((x.numerator*(1 << bits))//x.denominator, 1 << bits)


def ceil_dyadic(x, bits=128):
    return -floor_dyadic(-x, bits)


def feedback_interval(interval):
    lo, hi = interval
    # e-Sin(e) is increasing on this branch, so evaluate the endpoints.
    low = lo-sine_interval(lo)[1]
    high = hi-sine_interval(hi)[0]
    return max(F(0), floor_dyadic(low)), ceil_dyadic(high)


def horizontal_series(connection, depth):
    n = len(connection[0])
    out = [eye(n)]
    for degree in range(depth):
        rhs = zero(n)
        for k in range(min(degree+1, len(connection))):
            rhs = add(rhs, mul(connection[k], out[degree-k]))
        out.append(scale(-F(1, degree+1), rhs))
    return out


def pad_series(items, length):
    return items+[zero(len(items[0])) for _ in range(length-len(items))]


def formal_exp(generator, depth):
    return [scale(F(1, factorial(n)), power(generator, n)) for n in range(depth+1)]


def phase_packet(turn, frame, label, quarter_word=None):
    local = mul(mul(inv(frame), turn), frame)
    p = mat([[1, 0], [0, 0]])
    local_p = mul(mul(inv(frame), p), frame)
    packet = acquire(local, local_p, label, ["phase-reading"], frame)
    if quarter_word is not None:
        packet["oriented_quarter_word"] = quarter_word
    return packet


def decode_phase(packet):
    local = decode(packet)
    frame = mat(packet["frame"])
    turn = mul(mul(frame, local), inv(frame))
    if len(turn) != 2 or any(len(row) != 2 for row in turn):
        raise ValueError("not a two-channel scalar-turn sector")
    c, s = turn[0][0], turn[1][0]
    if turn != mat([[c, -s], [s, c]]) or c*c+s*s != 1:
        raise ValueError("not the declared circular J sector")
    answer = {"cosine": c, "sine": s}
    if "oriented_quarter_word" in packet:
        word = packet["oriented_quarter_word"]
        if any(type(k) is not int or k not in (-1, 1) for k in word):
            raise ValueError("invalid oriented quarter-step record")
        quarters = sum(word)
        residue, winding = quarters % 4, quarters // 4
        if turn != power(J, residue):
            raise ValueError("quarter record does not match terminal phase")
        answer.update({"lifted_quarters": quarters, "principal_quarters": residue,
                       "full_turn_memory": winding})
    return answer


def build():
    checks, phase_readings = [], []

    def check(name, truth, negative=False):
        if not truth:
            raise ArithmeticError(name)
        checks.append({"name": name, "kind": "negative" if negative else "positive",
                       "status": "PASS"})

    eT, eV = mat([[1], [0]]), mat([[0], [1]])
    check("the actual clockwise TVSP order is T V S P",
          mul(J, eT) == eV and mul(J, eV) == scale(-1, eT)
          and power(J, 4) == eye(2) and power(J, 2) == scale(-1, eye(2)))

    x, y, lam = cc.variable(1), cc.variable(2), cc.variable(0)
    f = cc.add(cc.power(x, 3), cc.mul(lam, x, y), cc.power(y, 2))
    v = (F(2), F(-1), F(0))
    tv, sv = tuple(F(3)*k for k in v), tuple(F(2)*k for k in v)
    check("counting lines compose their lawful translation parameter",
          translate(translate(f, tv), sv) == translate(f, tuple(a+b for a, b in zip(tv, sv))))
    check("the derivative along a count line is its declared lowering direction",
          translate(cc.add(cc.scale(2, cc.derivative(f, 1)), cc.scale(-1, cc.derivative(f, 2))), tv)
          == cc.add(cc.scale(2, cc.derivative(translate(f, tv), 1)),
                    cc.scale(-1, cc.derivative(translate(f, tv), 2))))

    depth = 6
    along = pad_series([zero(2), J], depth+1)
    transport = horizontal_series(along, depth)
    expected = [eye(2), zero(2), scale(-F(1, 2), J), zero(2),
                scale(-F(1, 8), eye(2)), zero(2), scale(F(1, 48), J)]
    check("line response coefficients solve the ordered formal transport equation",
          transport == expected and poly_mul(transport, poly_inverse_unit(transport)) == poly_unit(transport))
    n12 = mat([[0, 1], [0, 0]])
    h = pad_series([eye(2), n12], depth+1)
    hi = pad_series([eye(2), scale(-1, n12)], depth+1)
    hd = pad_series([n12], depth+1)
    changed_along = poly_add(poly_mul(hi, hd), poly_mul(poly_mul(hi, along), h))
    check("formal line transport carries both endpoint frames",
          horizontal_series(changed_along, depth) == poly_mul(hi, transport))

    turn = qturn(F(1, 3))
    cosine, sine = F(4, 5), F(3, 5)
    check("the exact rational turn supplies its oriented cosine and sine",
          turn == mat([[cosine, -sine], [sine, cosine]])
          and mul(tr(turn), turn) == eye(2))
    r = cc.variable(1)
    jpoly, identpoly = cc.matrix([[0, -1], [1, 0]]), cc.eye(2)
    num = cc.ma(cc.ms(cc.add(cc.c(1), cc.scale(-1, cc.power(r, 2))), identpoly),
                cc.ms(cc.scale(2, r), jpoly))
    den = cc.add(cc.c(1), cc.power(r, 2))
    derivative_residue = cc.ma(cc.ms(den, cc.md(num, 1)),
                               cc.ms(cc.scale(-2, r), num),
                               cc.ms(cc.c(-2), cc.mm(jpoly, num)))
    check("the cleared Cayley derivative derives the native angular speed",
          derivative_residue == cc.zeros(2))
    check("two strictly smaller native angles compose to the quarter turn",
          mul(qturn(F(1, 2)), qturn(F(1, 3))) == J
          and qturn(1) == J and inv(qturn(F(1, 3))) == qturn(-F(1, 3)))
    bounds_half, bounds_third = angle_interval(F(1, 2), 28), angle_interval(F(1, 3), 28)
    q_bounds = tuple(a+b for a, b in zip(bounds_half, bounds_third))
    pi_bounds = tuple(2*x for x in q_bounds)
    check("native half-turn normalization has a strict rational enclosure",
          F(3) < pi_bounds[0] < pi_bounds[1] < F(22, 7)
          and pi_bounds[1]-pi_bounds[0] < F(1, 10**17))
    frame = mat([[1, 2], [0, 1]])
    met = mul(tr(frame), frame)
    ju = mul(mul(inv(frame), J), frame)
    u, w = mul(inv(frame), eT), mul(inv(frame), mul(turn, eT))
    check("angle readings survive a nonorthogonal moving frame with its pairing",
          dot(u, u, met) == dot(w, w, met) == 1
          and dot(u, w, met) == cosine and dot(mul(ju, u), w, met) == sine)
    check("using an untransported coordinate dot product changes the angle",
          dot(u, w)**2/(dot(u, u)*dot(w, w)) != cosine*cosine, True)
    phase = phase_packet(turn, frame, "SE44-moving-angle-frame")
    phase_readings.append(phase)
    check("the detached complementary phase bank recovers the full oriented turn",
          decode_phase(json.loads(json.dumps(phase))) == {"cosine": cosine, "sine": sine})
    check("an unoriented line cut loses its half-turn direction",
          mul(eT, tr(eT)) == mul(scale(-1, eT), tr(scale(-1, eT)))
          and mul(power(J, 2), eT) != eT, True)

    rho = F(3438)
    orbit = [power(turn, n) for n in range(13)]
    jya = [rho*u[1][0] for u in orbit]
    kappa = 2*(1-cosine)
    check("every exact jya table row preserves the native circle invariant",
          all(u[0][0]**2+u[1][0]**2 == 1 for u in orbit))
    check("the exact second difference uses the turn-derived coefficient",
          all(jya[n+1]-2*jya[n]+jya[n-1] == -kappa*jya[n] for n in range(1, 12))
          and kappa == 4*F(1, 3)**2/(1+F(1, 3)**2))
    check("the cumulative sine-table rule independently reproduces the orbit",
          all(jya[n+1] == jya[n]+jya[1]-kappa*sum(jya[1:n+1]) for n in range(1, 12)))
    check("a universal historical divisor cannot replace the measured turn coefficient",
          jya[2] != jya[1]+jya[1]-F(1, 225)*jya[1], True)
    check("fixed quarter-turn repetition is periodic rather than convergent calibration",
          [power(J, n)[1][0] for n in range(5)] == [0, 1, 0, -1, 0], True)

    frames = [mat([[1, n], [0, 1]]) for n in range(7)]
    state_matrices = [mul(inv(g), power(turn, n)) for n, g in enumerate(frames)]
    orbit_packets = [acquire(state, mat([[1, 0], [0, 0]]), "SE44-moving-jya-orbit",
                             ["repeat-same-turn", n], g)
                     for n, (state, g) in enumerate(zip(state_matrices, frames))]
    detached = json.loads(json.dumps(orbit_packets))
    decoded = [decode(p) for p in detached]
    recorded_frames = [mat(p["frame"]) for p in detached]
    recovered_turn = mul(mul(recorded_frames[1], decoded[1]), inv(mul(recorded_frames[0], decoded[0])))
    C = scale(F(1, 2), add(recovered_turn, inv(recovered_turn)))
    covariant_ok, raw_fail = True, False
    for n in range(1, 6):
        pn = mul(inv(recorded_frames[n+1]), recorded_frames[n])
        pp = mul(inv(recorded_frames[n]), recorded_frames[n-1])
        cn = mul(mul(inv(recorded_frames[n]), C), recorded_frames[n])
        delta = add(decoded[n], mul(pp, decoded[n-1]), -1)
        predicted_delta = mul(pn, add(delta, mul(scale(2, add(eye(2), cn, -1)), decoded[n]), -1))
        observed_delta = add(decoded[n+1], mul(pn, decoded[n]), -1)
        covariant_ok &= observed_delta == predicted_delta
        raw_fail |= add(add(decoded[n+1], scale(2, mul(C, decoded[n])), -1), decoded[n-1]) != zero(2)
    check("moving-frame jya recurrence is decoded from its recorded initial pair",
          recovered_turn == turn and covariant_ok)
    check("omitting frame transport gives a false jya mismatch", raw_fail, True)

    A = mat([[1, 1], [0, 1]])
    B = mat([[1, 0], [1, 1]])
    ab, ba = mul(A, B), mul(B, A)
    ca, cb = scale(F(1, 2), add(ab, inv(ab))), scale(F(1, 2), add(ba, inv(ba)))
    check("equal recurrence coefficients can hide distinct ordered initial turns",
          ca == cb and ab != ba and power(ab, 2) != power(ba, 2), True)
    varying = [A, B, A]
    z = [eye(2)]
    for operator in varying:
        z.append(mul(operator, z[-1]))
    residuals = []
    for n in (1, 2):
        observed = add(add(z[n+1], scale(2, mul(ca, z[n])), -1), z[n-1])
        expected_res = mul(add(add(varying[n], ab, -1), add(inv(varying[n-1]), inv(ab), -1)), z[n])
        residuals.append(observed)
        if observed != expected_res:
            raise ArithmeticError("varying-step residual identity")
    check("varying noncommuting steps have the stated forward/backward residual",
          any(x != zero(2) for x in residuals))
    memory = mat([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
    cmem = scale(F(1, 2), add(memory, inv(memory)))
    check("the operator law retains growing central sheet memory at C equal identity",
          cmem == eye(3) and power(memory, 5)[0][2] == 5
          and add(add(power(memory, 3), scale(2, power(memory, 2)), -1), memory) == zero(3), True)
    hyperbolic = mat([[2, 0], [0, F(1, 2)]])
    rejected = False
    try:
        decode_phase(phase_packet(hyperbolic, eye(2), "SE44-hyperbolic-control"))
    except ValueError:
        rejected = True
    check("a noncircular return is not decoded as a scalar compass angle", rejected, True)

    f_unit = cc.power(lam, 2)
    connection = [cc.zeros(2), cc.ms(cc.mul(f_unit, x), jpoly), cc.zeros(2)]
    field = cc.curvature(connection, 0, 1)
    loop = cc.loop(connection, 0, 1, cc.eye(2), depth=3)
    area = cc.mul(cc.variable(4), cc.variable(5), f_unit)
    expected_loop = cc.ma(cc.eye(2), cc.ms(area, jpoly),
                          cc.ms(cc.scale(-F(1, 2), cc.power(area, 2)), cc.eye(2)),
                          cc.ms(cc.scale(-F(1, 6), cc.power(area, 3)), jpoly))
    check("the native square has the stated rotational curvature and loop reading",
          field == cc.ms(f_unit, jpoly) and loop == expected_loop)
    check("the mixed jya coefficient recovers the actual curvature coefficient",
          cc.mixed(loop) == field and cc.step_coefficient(loop[1][0], 1, 1) == f_unit)
    check("shallow unit observation misses a retained curvature turn",
          cc.mr(field, 1) == cc.zeros(2) and cc.mr(field, 2) == field, True)
    antipode = phase_packet(scale(-1, eye(2)), eye(2), "SE44-antipodal-sine-silence", [1, 1])
    stationary = phase_packet(eye(2), eye(2), "SE44-no-turn", [])
    fullturn = phase_packet(eye(2), eye(2), "SE44-one-full-turn", [1, 1, 1, 1])
    phase_readings.extend([antipode, stationary, fullturn])
    check("the cosine response rejects nonidentity antipodal sine silence",
          decode_phase(antipode)["sine"] == 0 and decode_phase(antipode)["cosine"] == -1, True)
    check("oriented crossing memory repairs a terminal full-turn collision",
          decode(stationary) == decode(fullturn)
          and decode_phase(stationary)["full_turn_memory"] == 0
          and decode_phase(fullturn)["full_turn_memory"] == 1, True)

    feedback = [(F(1), F(1))]
    for _ in range(4):
        feedback.append(feedback_interval(feedback[-1]))
    check("literal native sine feedback has outward decreasing error enclosures",
          all(0 <= nxt[0] <= nxt[1] < prev[1] for prev, nxt in zip(feedback, feedback[1:]))
          and feedback[-1][1] < F(1, 10**30))
    check("finite feedback enclosures obey the proved cubic bound with outward rounding",
          all(nxt[1] <= prev[1]**3/6+F(1, 2**128) for prev, nxt in zip(feedback, feedback[1:])))
    depth = 8
    sine_reading = F(4, 5)
    forward = formal_exp(scale(sine_reading, J), depth)
    reverse = formal_exp(scale(-sine_reading, J), depth)
    relative = qturn(F(1, 2))
    source_before = mul(turn, relative)
    calibration = [mul(turn, a) for a in forward]
    remaining = [mul(a, relative) for a in reverse]
    check("observer sine feedback retains the exact source in formal response coefficients",
          poly_mul(calibration, remaining) == pad_series([source_before], depth+1))

    return encode({"stage": "SE44", "author": "Monty",
                   "scope": "Native counting/angle proofs with exact supplied observer instances and outward rational analytic enclosures; no universal physical geometry or RH sign.",
                   "quarter_turn_basis": ["T", "V"],
                   "quarter_angle_bounds": q_bounds, "native_half_turn_bounds": pi_bounds,
                   "angle_enclosure_orders": {"half": 28, "third": 28},
                   "phase_readings": phase_readings,
                   "jya_table": [{"n": n, "cosine": u[0][0], "sine": u[1][0], "jya": jya[n]}
                                 for n, u in enumerate(orbit)],
                   "jya_radius": rho, "jya_kappa": kappa,
                   "moving_orbit_readings": orbit_packets,
                   "varying_step_residuals": residuals,
                   "formal_line_transport": transport,
                   "curvature_loop_through_step_degree_3": cc.em(loop),
                   "curvature_coefficient": cc.em(field),
                   "feedback_error_intervals": feedback,
                   "feedback_rounding_bits": 128, "sine_series_order": 10,
                   "source_preserving_feedback_through_formal_degree": depth,
                   "checks": checks, "check_count": len(checks),
                   "negative_control_count": sum(x["kind"] == "negative" for x in checks)})


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
            if hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() != pin["sha256"]:
                raise ArithmeticError("source pin mismatch: "+pin["path"])
        archived = json.loads(RESULT.read_text())
        if result != archived:
            raise ArithmeticError("saved jya readings differ from exact replay")
        for packet in archived["phase_readings"]:
            decode_phase(packet)
        for packet in archived["moving_orbit_readings"]:
            decode(packet)
    print(f"PASS SE44: {result['check_count']} exact controls; "
          f"{result['negative_control_count']} negative controls; "
          f"archive={'matched' if args.check else 'written' if args.write else 'not requested'}")


if __name__ == "__main__":
    main()
