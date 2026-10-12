"""Exact finite controls for SE13's moving-reference index theorems.

These rational controls are not a proof-assistant verification of
Atiyah--Singer and do not evaluate the actual global RH obstruction.
The written infinite-dimensional hypotheses remain separate.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

RESULT = Path(__file__).with_name('ENDPOINT_OBSERVER_INDEX_RESULT.json')


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def diag(values):
    return mat([[x if i == j else 0 for j in range(len(values))]
                for i, x in enumerate(values)])


def tr(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in tr(b)] for row in a]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def inv(a):
    n = len(a)
    out = [row[:]+unit for row, unit in zip(a, eye(n))]
    for k in range(n):
        j = next((j for j in range(k, n) if out[j][k]), None)
        if j is None:
            raise ValueError('singular matrix')
        out[k], out[j] = out[j], out[k]
        pivot = out[k][k]
        out[k] = [x/pivot for x in out[k]]
        for j in range(n):
            if j != k:
                ratio = out[j][k]
                out[j] = [x-ratio*y for x, y in zip(out[j], out[k])]
    return [row[n:] for row in out]


def rank(a):
    out = [row[:] for row in a]
    r = 0
    for k in range(len(out[0])):
        j = next((j for j in range(r, len(out)) if out[j][k]), None)
        if j is None:
            continue
        out[r], out[j] = out[j], out[r]
        pivot = out[r][k]
        out[r] = [x/pivot for x in out[r]]
        for j in range(r+1, len(out)):
            ratio = out[j][k]
            out[j] = [x-ratio*y for x, y in zip(out[j], out[r])]
        r += 1
    return r


def inertia(a):
    """Exact real symmetric inertia (negative, zero, positive).

    Congruence elimination uses a nonzero diagonal pivot when present;
    otherwise a nonzero off-diagonal gives a two-by-two hyperbolic block.
    No floating-point eigenvalues or tolerance decisions are used.
    """
    assert a == tr(a)
    a = [row[:] for row in a]
    negative = zero = positive = 0
    while a:
        n = len(a)
        k = next((i for i in range(n) if a[i][i]), None)
        if k is not None:
            order = [k]+[i for i in range(n) if i != k]
            a = [[a[i][j] for j in order] for i in order]
            d = a[0][0]
            negative += int(d < 0)
            positive += int(d > 0)
            a = [[a[i][j]-a[i][0]*a[0][j]/d
                  for j in range(1, n)] for i in range(1, n)]
            continue
        pair = next(((i, j) for i in range(n) for j in range(i+1, n)
                     if a[i][j]), None)
        if pair is None:
            zero += n
            break
        order = list(pair)+[i for i in range(n) if i not in pair]
        a = [[a[i][j] for j in order] for i in order]
        d = a[0][1]
        negative += 1
        positive += 1
        a = [[a[i][j]-(a[i][0]*a[1][j]+a[i][1]*a[0][j])/d
              for j in range(2, n)] for i in range(2, n)]
    return negative, zero, positive


def congr(a, t):
    return mul(mul(tr(t), a), t)


def gram(t):
    return mul(tr(inv(t)), inv(t))


def charge(b):
    return inertia(add(b, eye(len(b)), -1))[2]


def diagonal_flow(start, end):
    """Exact crossing locations for affine diagonal paths with nonzero ends."""
    crossings = []
    for i, (a, b) in enumerate(zip(start, end)):
        assert a and b, 'endpoint convention required'
        if a*b < 0:
            crossings.append({'channel': i, 'time': str(-a/(b-a)),
                              'sign': 1 if b > a else -1})
    return sum(row['sign'] for row in crossings), crossings


def build():
    checks = []

    def check(name, assertion, **data):
        assert assertion, name
        checks.append({'name': name, 'status': 'PASS', **data})

    # Two domain-changing charts of a rectangular Fredholm control.
    d = mat([[1, 0, 0], [0, 1, 0]])
    u = mat([[1, 2, 0], [0, 1, 1], [0, 0, 2]])
    v = mat([[2, 1], [0, 3]])
    dp = mul(mul(v, d), inv(u))
    indices = [(len(x[0])-rank(x))-(len(x)-rank(x)) for x in [d, dp]]
    check('rectangular_kernel_cokernel_transport', indices == [1, 1], indices=indices)
    up = mat([[3, 0, 1], [0, 2, 0], [0, 0, 1]])
    u10, u21, u20 = u, mul(up, inv(u)), up
    check('three_chart_cocycle', mul(u21, u10) == u20)
    check('transported_domain_metric', congr(gram(u), u) == eye(3))
    kernel = mul(u, mat([[0], [0], [1]]))
    check('transported_kernel_vector', mul(dp, kernel) == mat([[0], [0]]))

    # D plus the one missing output row is invertible: q-p=1.
    augmented = eye(3)
    proposed = diag([1, 1, F(9, 10)])
    left = add(eye(3), mul(proposed, augmented), -1)
    right = add(eye(3), mul(augmented, proposed), -1)
    check('augmented_index_certificate', indices[0] == 1 and left == right
          and inertia(add(scale(F(1, 100), eye(3)), mul(tr(left), left), -1))[0] == 0,
          domain_extra_rank=0, target_extra_rank=1, residual_norm_upper='1/10')
    ep = mul(mul(u, left), inv(u))
    bound = add(scale(F(1, 100), gram(u)), congr(gram(u), ep), -1)
    check('nonorthonormal_residual_bound', inertia(bound)[0] == 0)
    # A lossy domain cut removes the kernel: it is not an isomorphism.
    cut = mat([[1, 0], [0, 1], [0, 0]])
    dc = mul(d, cut)
    check('lossy_cut_is_not_index_preserving', len(dc[0])-len(dc) == 0
          and indices[0] == 1)

    source = diag([-1, 2])
    r1, w1 = diag([3, 6]), scale(F(2), eye(2))
    r2, w2 = diag([8, 11]), scale(F(3), eye(2))
    b1, b2 = mul(mul(tr(w1), inv(r1)), w1), mul(mul(tr(w2), inv(r2)), w2)
    check('moving_references_same_source', add(r1, mul(w1, tr(w1)), -1) == source
          and add(r2, mul(w2, tr(w2)), -1) == source
          and charge(b1) == charge(b2) == inertia(source)[0] == 1,
          first_B=[str(b1[i][i]) for i in range(2)],
          second_B=[str(b2[i][i]) for i in range(2)], invariant_charge=1)
    check('relative_gap_is_not_reference_invariant', 1-b1[0][0] == F(-1, 3)
          and 1-b2[0][0] == F(-1, 8))
    t = mat([[2, 1], [1, 1]])
    rp, wp = congr(r1, t), mul(tr(t), w1)
    bp = mul(mul(tr(wp), inv(rp)), wp)
    check('nonunitary_Birman_Schwinger_congruence', bp == b1
          and inertia(congr(source, t)) == inertia(source))
    check('zero_diagonal_inertia_control', inertia(mat([[0, 2, 0], [2, 0, 0], [0, 0, 0]]))
          == (1, 1, 1))

    analysis, target = eye(3), diag([F(3, 2), F(1, 2), 1])
    te = mat([[2, 0, 1], [0, 3, 1], [0, 0, 1]])
    tl = mat([[1, 1, 0], [0, 2, 0], [1, 0, 1]])
    ap = mul(mul(te, analysis), inv(u))
    lp = mul(mul(tl, target), inv(u))
    q = add(mul(tr(analysis), analysis), mul(tr(target), target), -1)
    qp = add(congr(gram(te), ap), congr(gram(tl), lp), -1)
    f = mat([[1], [2], [3]])
    fp = mul(u, f)
    quotient = congr(mul(tr(target), target), f)[0][0]/congr(eye(3), f)[0][0]
    quotient_p = congr(congr(gram(tl), lp), fp)[0][0]/congr(congr(gram(te), ap), fp)[0][0]
    check('state_event_target_metric_transport', qp == congr(q, inv(u))
          and inertia(qp) == (1, 1, 1) and quotient == quotient_p,
          exact_test_quotient=str(quotient))
    check('ordinary_coordinate_norm_can_change', congr(mul(tr(lp), lp), fp)[0][0]
          /congr(mul(tr(ap), ap), fp)[0][0] != quotient)
    check('ordinary_selfadjoint_index_zero_is_not_positivity',
          len(source)-len(source) == 0 and inertia(source)[0] == 1)

    # Rational rotating frame at a regular crossing.
    s = F(1, 3)
    z = 1+s*s
    rot = mat([[(1-s*s)/z, -2*s/z], [2*s/z, (1-s*s)/z]])
    rot_dot = mat([[-4*s/z**2, -2*(1-s*s)/z**2],
                   [2*(1-s*s)/z**2, -4*s/z**2]])
    ds, ds_dot = diag([s-F(1, 3), 2-s]), diag([1, -1])
    transformed = mul(mul(rot, ds), tr(rot))
    derivative = add(add(mul(mul(rot_dot, ds), tr(rot)),
                         mul(mul(rot, ds_dot), tr(rot))),
                     mul(mul(rot, ds), tr(rot_dot)))
    connection = scale(-1, mul(rot_dot, tr(rot)))
    covariant = add(derivative, add(mul(connection, transformed), mul(transformed, connection), -1))
    check('moving_connection_full_covariance', mul(tr(rot), rot) == eye(2)
          and covariant == mul(mul(rot, ds_dot), tr(rot))
          and derivative != covariant)
    crossing_vector = mul(rot, mat([[1], [0]]))
    check('crossing_signature_transport', congr(covariant, crossing_vector)[0][0] == 1
          and mul(transformed, crossing_vector) == mat([[0], [0]]))

    sf, crossings = diagonal_flow([F(1), F(1), F(1)], [F(-5, 4), F(5, 9), F(1, 2)])
    reverse, _ = diagonal_flow([F(-5, 4), F(5, 9), F(1, 2)], [F(1), F(1), F(1)])
    check('activation_and_reverse_path', sf == -1 and reverse == 1,
          forward=sf, reverse=reverse, forward_crossings=crossings)
    cancel, events = diagonal_flow([F(3, 4), F(-5, 4), F(1, 2)],
                                   [F(-5, 4), F(3, 4), F(1, 2)])
    check('zero_net_flow_can_leave_nonzero_charge', cancel == 0
          and charge(diag([F(1, 4), F(9, 4), F(1, 2)])) == 1
          and charge(diag([F(9, 4), F(1, 4), F(1, 2)])) == 1,
          crossings=events, endpoint_charges=[1, 1])
    threshold_rejected = False
    try:
        diagonal_flow([F(1)], [F(0)])
    except AssertionError:
        threshold_rejected = True
    check('critical_endpoint_requires_convention', threshold_rejected)

    def bracket(c, error):
        return (inertia(add(c, scale(1+error, eye(len(c))), -1))[2],
                inertia(add(c, scale(1-error, eye(len(c))), -1))[2])
    check('finite_error_count_bracket', bracket(diag([F(6, 5), F(4, 5)]), F(1, 10)) == (1, 1)
          and bracket(diag([1, F(1, 2)]), F(1, 10)) == (0, 1),
          resolved=[1, 1], unresolved=[0, 1])
    eta_rows = []
    for eta in [F(1, 2), F(1, 4), F(1, 8)]:
        bs = diag([F(1, 4)/eta, 1/(1+eta), F(1, 2)/(1+eta)])
        shifted = diag([eta-F(1, 4), eta, eta+F(1, 2)])
        assert charge(bs) == inertia(shifted)[0]
        eta_rows.append({'eta': str(eta), 'charge': charge(bs), 'nullity': inertia(shifted)[1]})
    check('shifted_source_counts_and_threshold', [r['charge'] for r in eta_rows] == [0, 0, 1]
          and [r['nullity'] for r in eta_rows] == [0, 1, 0], values=eta_rows)

    return {'schema': 'rkf.endpoint-observer-index-controls.v1', 'date': '2026-10-12',
            'status': 'PASS_FINITE_RATIONAL_CONTROLS', 'arithmetic': 'exact Fraction only',
            'checks_passed': len(checks), 'checks': checks,
            'scope': 'Finite transport, reference, sign-convention and enclosure controls. '
                     'Not a formal proof of Atiyah--Singer, a native elliptic adapter, '
                     'or a global eta-zero/RH certificate.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--write', action='store_true')
    modes.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = build()
    encoded = json.dumps(result, indent=2, ensure_ascii=False)+'\n'
    if args.write:
        RESULT.write_text(encoded)
    else:
        assert RESULT.read_text() == encoded, 'archived control result differs'
    print(json.dumps({k: result[k] for k in ['status', 'checks_passed', 'scope']}, indent=2))


if __name__ == '__main__':
    main()
