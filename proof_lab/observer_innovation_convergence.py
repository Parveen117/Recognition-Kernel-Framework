"""SE49: actual-source innovations and quantitative response convergence.

Python 3.12, standard library only. Midpoint whitening only proposes an
invertible coordinate change; outward congruence and LDL certify the sign.
All-order positivity and global eta zero are not outputs of this replay.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from math import prod

from proof_lab.endpoint_full_aperture_certificate import I
from proof_lab.endpoint_global_eta_certificate import integer_log
from proof_lab.endpoint_zero_shift_laplace_certificate import (
    precise_constants, zeta_jet, response, source_entry, separate_entry,
    interval_ldl, overlap, verify_source_pins, euler_tail,
)
from proof_lab.endpoint_observer_index_certificate import add, inv, mul, scale, tr, inertia
from proof_lab.five_source_operator_repair import iproduct, symmetric_box, isolve
from proof_lab.diagonal_spectral_pencil import model_pencil
from proof_lab.ordered_return_feedback import encode

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'proof_lab/ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json'
RESULT = Path(__file__).with_name('OBSERVER_INNOVATION_CONVERGENCE_RESULT.json')
PINS = ROOT / 'papers/rkf_completed_weil_endpoint/development/SE49_SOURCE_PINS.json'
DIMENSION = 24
COUNT = 320


def whitening_candidate(a):
    """Untrusted rational upper-triangular candidate, not a sign certificate."""
    n = len(a)
    with localcontext() as ctx:
        ctx.prec = 120
        midpoint = [[(v.lo+v.hi)/2 for v in row] for row in a]
        lower = [[Decimal(int(i == j)) for j in range(n)] for i in range(n)]
        pivots = []
        for i in range(n):
            pivots.append(midpoint[i][i]-sum(lower[i][k]**2*pivots[k] for k in range(i)))
            if pivots[-1] <= 0:
                raise ArithmeticError('no positive midpoint whitening candidate')
            for j in range(i+1, n):
                lower[j][i] = (midpoint[j][i]-sum(lower[j][k]*lower[i][k]*pivots[k]
                                                  for k in range(i)))/pivots[i]
        out = [[Decimal(0) for _ in range(n)] for _ in range(n)]
        for k in range(n):
            for i in reversed(range(k+1)):
                out[i][k] = ((1/pivots[k].sqrt() if i == k else Decimal(0))
                             -sum(lower[j][i]*out[j][k] for j in range(i+1, k+1)))
        return [[F(v) for v in row] for row in out]


def certify_form(a):
    change = whitening_candidate(a)
    n = len(a)
    if any(change[i][i] == 0 for i in range(n)) or any(change[i][j] for i in range(n) for j in range(i)):
        raise ArithmeticError('candidate is not invertible upper triangular')
    change_box = [[I(v) for v in row] for row in change]
    normalized = symmetric_box(iproduct(tr(change_box), iproduct(a, change_box)))
    # These calculations, not the midpoint factorization, establish the sign.
    pivots = interval_ldl(normalized)
    rows = [normalized[i][i]-sum((I(v.abs_upper()) for j, v in enumerate(row) if i != j), I(0))
            for i, row in enumerate(normalized)]
    if any(v.lo <= 0 for v in rows):
        raise ArithmeticError('outward Gershgorin margin failed')
    original = [pivots[i]/I(change[i][i])**2 for i in range(n)]
    digest = hashlib.sha256(json.dumps(encode(change), sort_keys=True).encode()).hexdigest()
    return change_box, normalized, original, {
        'candidate_sha256': digest,
        'candidate_arithmetic': '120-digit Decimal proposal, converted exactly to Fraction',
        'certificate_arithmetic': 'unchanged 90-digit outward Decimal intervals',
        'normalized_minimum_row_lower': str(min(v.lo for v in rows)),
        'normalized_pivots': [v.record() for v in pivots],
        'original_innovation_pivots': [v.record() for v in original],
        'minimum_original_pivot_lower': str(min(v.lo for v in original)),
    }


def source_bank():
    old = json.loads(SOURCE.read_text())
    cc = precise_constants()
    logs = [I(0)]+[integer_log(n, cc['log2']) for n in range(1, COUNT+1)]
    responses = {int(s): [I(*v) for v in row] for s, row in old['responses'].items()}
    jets = {int(s): [I(*v) for v in row] for s, row in old['zeta_jets'].items()}
    new = {}
    # s=27 is an independent held-out reading, not an interpolation node.
    for s in range(19, DIMENSION+4):
        jets[s] = zeta_jet(s, logs, cc['log2'], COUNT)
        responses[s] = response(s, jets[s], cc)
        new[str(s)] = {'zeta_jet': [v.record() for v in jets[s]],
                       'Q_and_derivative': [v.record() for v in responses[s]]}
    n = DIMENSION
    roots = [F(2*i+5, 2) for i in range(n)]
    nodes = [w*w for w in roots]
    values = [responses[i+3][0]/(2*roots[i]) for i in range(n)]
    derivatives = [(responses[i+3][1]-responses[i+3][0]/roots[i])/(4*nodes[i]) for i in range(n)]
    ell = [[-derivatives[i] if i == j else (values[j]-values[i])/(nodes[i]-nodes[j])
            for j in range(n)] for i in range(n)]
    source = [[source_entry(i+3, j+3, responses) for j in range(n)] for i in range(n)]
    jj = [[v/4 for v in row] for row in source]
    return old, cc, responses, jets, new, roots, nodes, values, derivatives, ell, jj, source


def product_squared(real, imag, n, boundary=F(0)):
    """Exact modulus squared of the finite half-plane Blaschke product."""
    return prod((((real-F(2*i+3, 2))**2+imag**2)
                 /((real+F(2*i+3, 2)-2*boundary)**2+imag**2)
                 for i in range(1, n+1)), start=F(1))


def actual_response_bound(w, n):
    if w <= 1:
        raise ValueError('unconditional actual-response bound requires real w>1')
    return (w+F(5, 2))**2/w*product_squared(w, F(0), n, F(1))


def rational_innovations(nodes, values, derivatives, x, r, derivative):
    ell, jj = model_pencil(nodes, values, derivatives)
    l = [[(u-r)/(x-t)] for t, u in zip(nodes, values)]
    j = [[(x*r-t*u)/(x-t)] for t, u in zip(nodes, values)]
    lp = mul(mul(tr(l), inv(ell)), l)[0][0]
    jp = mul(mul(tr(j), inv(jj)), j)[0][0]
    return ell, jj, l, j, -derivative-lp, r+x*derivative-jp, lp, jp


def rational_controls(check):
    atoms = [F(1), F(4), F(9), F(16), F(25)]
    weights = [F(1), F(2), F(1), F(3), F(2)]
    value = lambda t: sum((w/(t+a) for a, w in zip(atoms, weights)), F(0))
    derivative = lambda t: -sum((w/(t+a)**2 for a, w in zip(atoms, weights)), F(0))
    nodes = list(map(F, [3, 4, 5]))
    values = [value(t) for t in nodes]; derivatives = [derivative(t) for t in nodes]
    x = F(7); r = value(x); d = derivative(x)
    ell, jj, l, j, alpha, beta, lp, jp = rational_innovations(nodes, values, derivatives, x, r, d)
    check('two positive scalar innovations admit the new actual model reading', alpha > 0 and beta > 0)
    check('derivative lies in its exact simultaneous admissibility window', (jp-r)/x < d < -lp)
    bad_upper = -lp + min(lp/2, F(1, 1000))
    bad_lower = (jp-r)/x-min((r-jp)/(2*x), F(1, 1000))
    for label, bad, which in [('L', bad_upper, 0), ('J', bad_lower, 1)]:
        a, b = model_pencil(nodes+[x], values+[r], derivatives+[bad])
        check('positive diagonal readings do not replace the '+label+' innovation',
              all(a[i][i] > 0 and b[i][i] > 0 for i in range(4))
              and inertia([a, b][which])[0] > 0, negative=True)
    full_l, full_j = model_pencil(nodes+[x], values+[r], derivatives+[d])
    u = [[v] for v in values]
    for z in [F(1), F(6), F(20)]:
        p = add(jj, scale(z, ell)); k = add(j, scale(z, l)); solved = mul(inv(p), u)
        delta = r+(x-z)*d-mul(mul(tr(k), inv(p)), k)[0][0]
        residue = r-mul(tr(k), solved)[0][0]
        q0 = mul(tr(u), solved)[0][0]
        uf = u+[[r]]
        q1 = mul(mul(tr(uf), inv(add(full_j, scale(z, full_l)))), uf)[0][0]
        check('exact response innovation at z='+str(z), q1-q0 == residue**2/delta and delta >= beta+z*alpha > 0)
    change = [[F(2), F(1), F(0)], [F(0), F(3), F(1)], [F(0), F(0), F(1)]]
    p = add(jj, scale(F(6), ell)); old = mul(mul(tr(u), inv(p)), u)[0][0]
    transported = mul(mul(tr(change), p), change); moved = mul(tr(change), u)
    check('response transports the probe with the acquired pairing', mul(mul(tr(moved), inv(transported)), moved)[0][0] == old)
    check('moving the operator without its probe is detected', mul(mul(tr(u), inv(transported)), u)[0][0] != old, negative=True)
    one_factor = F(1, 5)  # w=3, one value-only zero at w=2.
    check('value-only interpolation does not justify a squared factor', one_factor > one_factor**2, negative=True)
    check('the diagonal boundary has no product decay', product_squared(F(0), F(14), 24) == 1, negative=True)
    sparse = prod(((F(2)**j-F(1, 8))/(F(2)**j+F(1, 8)))**2 for j in range(1, 33))
    check('an unbounded sparse bank need not force convergence', sparse > F(1, 2), negative=True)
    try:
        actual_response_bound(F(1), 16)
    except ValueError:
        check('right-half-plane bound refuses its excluded boundary', True, negative=True)
    else:
        raise AssertionError('missing half-plane guard')
    try:
        interval_ldl([[I(1), I(0)], [I(0), I(-1)]])
    except AssertionError:
        check('the outward sign gate rejects a planted negative direction', True, negative=True)
    else:
        raise AssertionError('negative direction accepted')


def build():
    checks = []
    def check(name, condition, negative=False):
        if not condition:
            raise AssertionError(name)
        checks.append({'name': name, 'status': 'PASS', 'negative_control': negative})
    rational_controls(check)
    old, cc, rr, jets, new, roots, nodes, values, derivatives, ell, jj, source = source_bank()
    check('all old sixteen source entries remain byte-identical',
          [[v.record() for v in row[:16]] for row in source[:16]] == old['matrix'])
    check('new complete zeta denominators and prime masses retain their signs',
          all(jets[s][0].lo > 1 and jets[s][1].hi < 0 for s in range(19, 28)))
    check('all new source entries agree with separate Gamma prime and pole assembly',
          all(overlap(source[i][j], separate_entry(i+3, j+3, jets, cc))
              for i in range(24) for j in range(24) if max(i, j) >= 16))
    check('actual normalization is strictly between zero and one half', 0 < values[0].lo and values[0].hi < F(1, 2))
    check('the elementary actual-response majorant is below one half', F(41, 8)/F(49, 4)+F(1, 14) < F(1, 2))
    check('digamma constants satisfy the declared majorant premises',
          0 < cc['gamma'].lo and cc['gamma'].hi < 1 and 0 < cc['logpi'].lo and cc['logpi'].hi < 2)
    displacement = [[jj[i][j]+nodes[j]*ell[i][j]-values[i] for j in range(24)] for i in range(24)]
    check('all actual source displacement readings enclose zero', all(v.lo <= 0 <= v.hi for row in displacement for v in row))
    forms = {}; pivots = {}; raw = {}
    for name, a in [('L', ell), ('J', jj)]:
        try:
            interval_ldl(a)
            raw[name] = 'PASS'
        except AssertionError as error:
            raw[name] = str(error)
        _, _, pivots[name], forms[name] = certify_form(a)
        check('outward transformed '+name+' is strictly positive on all 24 directions', all(v.lo > 0 for v in pivots[name]))
    check('raw interval uncertainty is not a negative-source witness',
          raw['L'].startswith('Uncertified pivot 17:') and raw['J'].startswith('Uncertified pivot 18:'), negative=True)
    innovations = []
    for i in range(24):
        alpha, beta, d, x = pivots['L'][i], pivots['J'][i], derivatives[i], nodes[i]
        # Correlated identities: lower=d-beta/x, upper=d+alpha.
        lower = d-beta/x; upper = d+alpha
        innovations.append({'dimension': i+1, 'node': x, 'alpha': alpha.record(), 'beta': beta.record(),
                            'actual_derivative': d.record(), 'admissible_derivative_lower': lower.record(),
                            'admissible_derivative_upper': upper.record(),
                            'strict_window_certified': lower.hi < d.lo and d.hi < upper.lo})
    check('all 24 actual derivatives lie strictly inside both-form windows', all(r['strict_window_certified'] for r in innovations))
    held_s = 27; held_w = F(53, 2); held_value = rr[held_s][0]/(2*held_w)
    readings = []
    for n in [5, 8, 12, 16, 20, 24]:
        p = [[jj[i][j]+held_w**2*ell[i][j] for j in range(n)] for i in range(n)]
        change, normal, _, _ = certify_form(p)
        moved = iproduct(tr(change), [[v] for v in values[:n]])
        solved, _ = isolve(normal, moved)
        rational_value = iproduct(tr(moved), solved)[0][0]
        difference = held_value-rational_value
        bound = actual_response_bound(held_w, n)
        check('independent actual response agrees with the analytic bound at N='+str(n), F(difference.abs_upper()) < bound)
        readings.append({'dimension': n, 'held_out_s': held_s, 'held_out_w': held_w,
                         'actual_q': held_value.record(), 'finite_q': rational_value.record(),
                         'actual_minus_finite_q': difference.record(),
                         'absolute_error_enclosure_upper': F(difference.abs_upper()),
                         'analytic_error_bound': bound,
                         'analytic_bound_decimal_enclosure': I(bound).record()})
    check('certified analytic bounds strictly decrease along the actual bank',
          all(readings[i+1]['analytic_error_bound'] < readings[i]['analytic_error_bound'] for i in range(5)))
    return encode({
        'schema': 'rkf.se49.observer-innovation-convergence.v1', 'author': 'Monty',
        'status': 'PASS_FINITE_SOURCE_AND_SCOPED_CONVERGENCE_CONTRACT',
        'eta_on_V24': F(0), 'dimension': DIMENSION,
        'five_label_gap_positive_by_SE47_finite_congruence': True,
        'five_label_gap_independently_boxed': False,
        'global_eta_zero_certified': False, 'all_order_positivity_certified': False, 'rh_proved': False,
        'global_shift_frontier_unchanged': F(1079, 2000), 'global_shift_floor': F(1, 492000),
        'old_source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'new_integer_s_readings': new, 'euler_terms': COUNT,
        'euler_remainders': [euler_tail(COUNT, j) for j in range(3)],
        'nodes': nodes, 'values': [v.record() for v in values],
        'L': [[v.record() for v in row] for row in ell],
        'J': [[v.record() for v in row] for row in jj],
        'raw_interval_ldl_outcomes': raw, 'congruence_certificates': forms,
        'actual_scalar_innovations': innovations, 'held_out_response_readings': readings,
        'check_count': len(checks), 'negative_control_count': sum(c['negative_control'] for c in checks),
        'checks': checks,
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write', action='store_true'); group.add_argument('--check', action='store_true')
    args = parser.parse_args()
    verify_source_pins()
    if args.check:
        for pin in json.loads(PINS.read_text())['local_files']:
            if hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest() != pin['sha256']:
                raise ArithmeticError('SE49 source pin mismatch: '+pin['path'])
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+'\n')
    elif result != json.loads(RESULT.read_text()):
        raise ArithmeticError('SE49 archive mismatch')
    print(f"PASS SE49: {result['check_count']} controls; {result['negative_control_count']} negative; "
          f"24 source directions, 48 positive innovations, six held-out response bounds; "
          f"global RH remains open; archive={'matched' if args.check else 'written'}")


if __name__ == '__main__':
    main()
