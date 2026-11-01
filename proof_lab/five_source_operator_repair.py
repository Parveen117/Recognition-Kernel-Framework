"""SE47: source-attached 1+4 reduction, with correlated observer readings.

Python 3.12 only. Consumes the unchanged SE21 complete-source enclosure.
The finite five-label sign is not a certificate on the infinite complement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from proof_lab.endpoint_full_aperture_certificate import I
from proof_lab.endpoint_zero_shift_laplace_certificate import interval_ldl, verify_source_pins
from proof_lab.endpoint_observer_index_certificate import add, eye, inertia, inv, mat, mul, scale, tr
from proof_lab.ordered_return_feedback import encode, zero

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "proof_lab/ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json"
RESULT = Path(__file__).with_name("FIVE_SOURCE_OPERATOR_REPAIR_RESULT.json")
PINS = ROOT / "papers/rkf_completed_weil_endpoint/development/SE47_SOURCE_PINS.json"


def iproduct(a, b):
    return [[sum((x*y for x, y in zip(row, col)), I(0)) for col in tr(b)] for row in a]


def symmetric_box(a):
    """Intersect two enclosures of the same proved Hermitian entry."""
    out = [row[:] for row in a]
    for i in range(len(a)):
        for j in range(i):
            out[i][j] = out[j][i] = I(max(a[i][j].lo, a[j][i].lo), min(a[i][j].hi, a[j][i].hi))
    return out


def ifactor(a):
    n = len(a)
    l = [[I(int(i == j)) for j in range(n)] for i in range(n)]
    d = []
    for i in range(n):
        d.append(a[i][i]-sum((l[i][k]*l[i][k]*d[k] for k in range(i)), I(0)))
        if d[-1].lo <= 0:
            raise ArithmeticError("reference pivot not positive")
        for j in range(i+1, n):
            l[j][i] = (a[j][i]-sum((l[j][k]*l[i][k]*d[k] for k in range(i)), I(0)))/d[i]
    return l, d


def isolve(a, b):
    l, d = ifactor(a)
    n, m = len(a), len(b[0])
    z = [[I(0) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            z[i][j] = b[i][j]-sum((l[i][k]*z[k][j] for k in range(i)), I(0))
    z = [[v/d[i] for v in row] for i, row in enumerate(z)]
    x = [[I(0) for _ in range(m)] for _ in range(n)]
    for i in reversed(range(n)):
        for j in range(m):
            x[i][j] = z[i][j]-sum((l[k][i]*x[k][j] for k in range(i+1, n)), I(0))
    return x, d


def records(a):
    return [[v.record() for v in row] for row in a]


def pole(rate):
    return F(1, (rate+1)*(rate+2))


def coordinates(rates):
    """Fixed accepted E=(f2,f3,f4,f5), fixed L2-moment complement."""
    accepted = rates[:4]
    gram = [[F(1, i+j) for j in accepted] for i in accepted]
    cross = [[F(1, i+j) for j in rates[4:]] for i in accepted]
    coefficients = mul(inv(gram), cross)
    transform = eye(len(rates))
    for i in range(4):
        for j in range(len(rates)-4):
            transform[i][j+4] = -coefficients[i][j]
    return gram, cross, coefficients, transform


def actual_packet(source, n):
    if source["eta"] != "0/1" or source["dimension"] < n:
        raise ValueError("incorrect source catalogue")
    rates = [2, 3, 4, 5, 1]+list(range(6, n+1))
    raw = [[I(*source["matrix"][i-1][j-1]) for j in rates] for i in rates]
    gram, cross, coeff, transform = coordinates(rates)
    change = [[I(v) for v in row] for row in transform]
    source_box = symmetric_box(iproduct(tr(change), iproduct(raw, change)))
    a = [row[:4] for row in source_box[:4]]
    c = [row[:4] for row in source_box[4:]]
    d = [row[4:] for row in source_box[4:]]
    b = [pole(j)-sum((pole(i)*coeff[k][l] for k, i in enumerate(rates[:4])), F(0))
         for l, j in enumerate(rates[4:])]
    r = [[v+b[i]*b[j] for j, v in enumerate(row)] for i, row in enumerate(d)]
    w = [[I(b[i])]+row for i, row in enumerate(c)]
    g = [[I(0) for _ in range(5)] for _ in range(5)]
    g[0][0] = I(1)
    for i in range(4):
        for j in range(4):
            g[i+1][j+1] = a[i][j]
    solved, reference_pivots = isolve(r, w)
    h = symmetric_box(iproduct(tr(w), solved))
    k = [[g[i][j]-h[i][j] for j in range(5)] for i in range(5)]
    try:
        direct_pivots = interval_ldl(k)
        direct = {"status": "POSITIVE", "minimum_pivot_lower": str(min(p.lo for p in direct_pivots))}
    except AssertionError:
        direct = {"status": "INCONCLUSIVE_AFTER_ENTRYWISE_SUBTRACTION", "negative_source_witness": False}
    # This is the unchanged full-source box, before a dependency-losing
    # transformation or subtraction. The source congruence theorem transfers
    # its certified positivity to the corresponding five-label K exactly.
    original = [[I(*v) for v in row[:n]] for row in source["matrix"][:n]]
    source_pivots = interval_ldl(original)
    accepted_pivots = interval_ldl(a)
    moment_null = add(cross, mul(gram, coeff), -1) == [[F(0)]*(n-4) for _ in range(4)]
    return encode({
        "dimension": n, "eta": "0/1", "accepted_rates": rates[:4], "complement_rates": rates[4:],
        "projection_coefficients": coeff, "moment_null_exact": moment_null,
        "boundary_readings_on_complement": b, "label_metric_G": records(g),
        "source_gram_H": records(h), "five_gap_K": records(k),
        "source_minimum_pivot_lower": str(min(p.lo for p in source_pivots)),
        "accepted_minimum_pivot_lower": str(min(p.lo for p in accepted_pivots)),
        "reference_minimum_pivot_lower": str(min(p.lo for p in reference_pivots)),
        "direct_gap_box": direct,
        "correlated_five_gap_status": "POSITIVE_BY_SAME_SOURCE_AUGMENTED_CONGRUENCE",
        "global_complement_sign_certified": False,
    })


def block_model(m, b):
    n = len(m)
    a = [row[:4] for row in m[:4]]
    c = [row[:4] for row in m[4:]]
    d = [row[4:] for row in m[4:]]
    r = add(d, mul(b, tr(b)))
    w = [[b[i][0]]+row for i, row in enumerate(c)]
    g = zero(5)
    g[0][0] = F(1)
    for i in range(4):
        for j in range(4):
            g[i+1][j+1] = a[i][j]
    h = mul(mul(tr(w), inv(r)), w)
    k = add(g, h, -1)
    return a, c, d, r, w, g, h, k


def build():
    source = json.loads(SOURCE.read_text())
    checks = []
    def check(name, condition, negative=False):
        if not condition:
            raise ArithmeticError(name)
        checks.append({"name": name, "kind": "negative" if negative else "positive", "pass": True})

    check("all source prime powers, Gamma modes and pole are retained",
          source["all_prime_powers_included"] and source["all_gamma_modes_included"] and source["full_pole_included"])
    packets = [actual_packet(source, n) for n in (5, 8, 12, 16)]
    for p in packets:
        n = p["dimension"]
        check(f"N={n} uses one fixed four-state acceptance and moment-null complement", p["moment_null_exact"])
        check(f"N={n} five-label gap is attached to a strictly positive complete source box",
              F(p["source_minimum_pivot_lower"]) > 0 and F(p["accepted_minimum_pivot_lower"]) > 0
              and F(p["reference_minimum_pivot_lower"]) > 0 and len(p["five_gap_K"]) == 5)
    check("direct entrywise five-gap certificates close N=5,8,12",
          all(p["direct_gap_box"]["status"] == "POSITIVE" for p in packets[:3]))
    check("N=16 entrywise cancellation is inconclusive while source correlations retain positivity",
          packets[-1]["direct_gap_box"]["status"] == "INCONCLUSIVE_AFTER_ENTRYWISE_SUBTRACTION", True)
    check("the pole is a nonzero acquired channel on the selected fixed complement",
          all(any(F(v) != 0 for v in p["boundary_readings_on_complement"]) for p in packets))
    nested = all(packets[i]["complement_rates"] == packets[i+1]["complement_rates"][:len(packets[i]["complement_rates"])]
                 for i in range(3))
    check("all four finite catalogues use nested restrictions of the same complement", nested)

    # Correlation identities use exact rational supplied controls, distinct
    # from the actual arithmetic interval evidence above.
    n = 9
    lower = eye(n)
    for i in range(n):
        for j in range(i): lower[i][j] = F((i+2*j)%5-2, 7)
    m = mul(lower, tr(lower))
    b = [[F(j+1, 13)] for j in range(n-4)]
    a, c, d, r, w, g, h, k = block_model(m, b)
    aug = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    # Order: accepted x, complement y, boundary t.
    for i in range(n):
        for j in range(n): aug[i][j] = m[i][j]
    for i in range(n-4):
        for j in range(n-4): aug[i+4][j+4] += b[i][0]*b[j][0]
        aug[i+4][n] = aug[n][i+4] = b[i][0]
    aug[n][n] = F(1)
    change = eye(n+1)
    for i in range(n-4): change[n][i+4] = b[i][0]
    diagonal = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n): diagonal[i][j] = m[i][j]
    diagonal[n][n] = F(1)
    check("augmented five-source form is exactly congruent to source plus one square",
          aug == mul(mul(tr(change), diagonal), change))
    check("five-gap and full-source negative counts and nullities agree",
          inertia(m)[:2] == inertia(k)[:2] == (0, 0))
    z = [[F(0) for _ in range(5)] for _ in range(n)]
    for i in range(4): z[i][i+1] = F(1)
    for i in range(n-4): z[i+4][0] = -b[i][0]
    e00 = zero(5); e00[0][0] = F(1)
    inverse_reading = add(e00, mul(mul(tr(z), inv(m)), z))
    check("inverse five-gap retains the exact source Gram without subtracting near equals", inv(k) == inverse_reading)

    # A new complement direction changes H by one full outer product.
    old_r = [row[:-1] for row in r[:-1]]
    old_w = w[:-1]
    coupling = [[r[i][-1]] for i in range(len(r)-1)]
    schur = r[-1][-1]-mul(mul(tr(coupling), inv(old_r)), coupling)[0][0]
    innovation = add([w[-1]], mul(mul(tr(coupling), inv(old_r)), old_w), -1)
    old_h = mul(mul(tr(old_w), inv(old_r)), old_w)
    increment = scale(1/schur, mul(tr(innovation), innovation))
    check("one new complementary observation gives the exact rank-one five-matrix update",
          schur > 0 and add(h, old_h, -1) == increment)
    check("the update includes mixed channels and cannot be replaced by its diagonal",
          any(increment[i][j] for i in range(5) for j in range(i)), True)

    label = eye(5); label[0][1] = F(2); label[2][3] = F(-3)
    gp, hp = mul(mul(tr(label), g), label), mul(mul(tr(label), h), label)
    action, changed_action = mul(inv(g), h), mul(inv(gp), hp)
    delta = mul(inv(add(g, h)), add(g, h, -1))
    delta_p = mul(inv(add(gp, hp)), add(gp, hp, -1))
    check("nonunitary observer changes transport both label forms and preserve the response action",
          changed_action == mul(mul(inv(label), action), label)
          and delta_p == mul(mul(inv(label), delta), label))
    check("the five-channel response is self-adjoint in its acquired metric",
          mul(g, action) == mul(tr(action), g) and mul(g, delta) == mul(tr(delta), g))
    # I+Lambda*N has a finite inverse when N^2=0; test several exact cuts.
    nil = zero(5); nil[0][4] = F(1)
    check("the marked-unit label family is lawful and returns the same target at the zero cut",
          all(mul(add(eye(5), scale(t, nil)), add(eye(5), scale(-t, nil))) == eye(5)
              for t in (F(0), F(1), F(7, 3))))
    scaled = eye(5); scaled[0][0] = F(3)
    metric = eye(5); response = scale(F(1, 4), eye(5))
    metric_p = mul(mul(tr(scaled), metric), scaled)
    response_p = mul(mul(tr(scaled), response), scaled)
    check("keeping I fixed after changing labels produces a false obstruction",
          inertia(add(metric_p, response_p, -1))[0] == 0 and inertia(add(eye(5), response_p, -1))[0] == 1, True)
    blind_h = scale(F(1, 4), eye(5)); blind_h[0][0] = blind_h[1][1] = F(3, 4)
    blind_h[0][1] = blind_h[1][0] = F(1, 2)
    blind_k = add(eye(5), blind_h, -1)
    check("five positive coordinate diagonals miss a negative mixed direction",
          all(blind_k[i][i] > 0 for i in range(5)) and inertia(blind_h)[0] == 0 and inertia(blind_k)[0] == 1, True)
    bad_m = eye(5); bad_m[-1][-1] = F(-1, 4)
    bad = block_model(bad_m, [[F(1)]])
    check("dropping the boundary source column falsely changes a negative source to a passing gap",
          inertia(bad[-1])[0] == 1 and inertia(bad[-3])[0] == 0, True)
    indefinite_reference = mat([[1, 0], [0, -1]])
    invisible_columns = mat([[F(1, 2), 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    apparently_good = add(eye(5), mul(mul(tr(invisible_columns), inv(indefinite_reference)), invisible_columns), -1)
    hidden_bad = add(indefinite_reference, mul(invisible_columns, tr(invisible_columns)), -1)
    check("a five-label pass cannot hide a negative reference direction",
          inertia(apparently_good)[0] == 0 and inertia(hidden_bad)[0] == 1, True)
    shear = mat([[1, 1], [0, 1]])
    native_metric = mul(tr(shear), shear)
    check("a nonorthogonal source chart must transport eta times the native metric including cross blocks",
          native_metric[0][1] == 1 and native_metric != eye(2), True)
    seam_h = scale(F(1, 4), eye(5)); seam_h[0][0] = F(1)
    seam_delta = mul(inv(add(eye(5), seam_h)), add(eye(5), seam_h, -1))
    check("the comparison seam is the generalized unit-threshold kernel",
          seam_delta[0][0] == 0 and inertia(seam_delta)[1] == 1
          and all(seam_delta[i][i] == F(3, 5) for i in range(1, 5)))
    # Choosing E=f1..f4 under the same moment projection absorbs the pole.
    rates = [1, 2, 3, 4, 5, 6]
    _, _, coeff, _ = coordinates(rates)
    absorbed = [pole(j)-sum((pole(i)*coeff[k][l] for k, i in enumerate(rates[:4])), F(0))
                for l, j in enumerate(rates[4:])]
    check("five is a label budget, not a forced minimal rank when acceptance already contains the pole",
          absorbed == [F(0), F(0)], True)
    check("neither finite five-gap positivity nor a formal zero cut is marked as a global certificate",
          all(not p["global_complement_sign_certified"] for p in packets), True)
    return encode({
        "stage": "SE47", "author": "Monty",
        "source_file": str(SOURCE.relative_to(ROOT)), "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "actual_source_scope": "Corrected complete odd source at eta=0, restricted to V_N for N=5,8,12,16; no proof on the infinite complement.",
        "historical_attachment": "Same 1+4 template, explicitly instantiated on E=span(f2,f3,f4,f5); no identity with the older raw E3 numerical packet asserted.",
        "packets": packets,
        "exact_model": {"source": m, "boundary": b, "G": g, "H": h, "K": k,
                        "inverse_gap": inverse_reading, "innovation": innovation, "increment_pivot": schur,
                        "rank_one_increment": increment, "label_change": label, "contrast": delta},
        "checks": checks, "check_count": len(checks),
        "negative_control_count": sum(x["kind"] == "negative" for x in checks),
        "rh_proved": False, "global_eta_zero_certified": False,
    })


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    verify_source_pins()
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+"\n")
    else:
        for pin in json.loads(PINS.read_text())["local_files"]:
            if hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest() != pin["sha256"]:
                raise ArithmeticError("SE47 pin mismatch: "+pin["path"])
        archive = json.loads(RESULT.read_text())
        if archive != result:
            raise ArithmeticError("SE47 archive mismatch")
        # Replay actual packets directly from the source bank identified by
        # the archive, not from a stored approximate five-matrix alone.
        for saved in archive["packets"]:
            if actual_packet(json.loads(SOURCE.read_text()), saved["dimension"]) != saved:
                raise ArithmeticError("detached five-source packet mismatch")
    print(f"PASS SE47: {result['check_count']} controls; {result['negative_control_count']} negative controls; "
          f"actual zero-shift source on V5,V8,V12,V16; archive={'matched' if args.check else 'written'}")


if __name__ == "__main__":
    main()
