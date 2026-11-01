"""SE21: full-source eta=0 on a finite Laplace subspace, with entire tails.

No sampled eigenvalue, prime cutoff, zero list or RH assumption is used.
The inherited outward interval implementation is left unchanged.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import I, constants, log_positive
    from proof_lab.endpoint_global_eta_certificate import integer_log
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I, constants, log_positive
    from endpoint_global_eta_certificate import integer_log

DIMENSION = 16
EULER_TERMS = 320
RESULT = Path(__file__).with_name('ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json')
PINS = Path(__file__).resolve().parents[1]/'papers/rkf_completed_weil_endpoint/development/SE21_SOURCE_PINS.json'


def bernoulli_numbers(n):
    values = [F(1)]
    for m in range(1, n+1):
        values.append(-sum((comb(m+1, k)*values[k] for k in range(m)), F(0))/(m+1))
    return values


def precise_constants():
    pi, log2, _ = constants()
    m, order = 1024, 32
    bb = bernoulli_numbers(2*order)
    harmonic = sum((F(1, j) for j in range(1, m+1)), F(0))
    correction = sum((bb[2*k]/(2*k*m**(2*k)) for k in range(1, order+1)), F(0))
    error = abs(bb[2*order])/(2*order*m**(2*order))
    gamma = I(harmonic-F(1, 2*m)+correction)-10*log2+I(-error, error)
    return dict(pi=pi, log2=log2, logpi=log_positive(pi), gamma=gamma,
                gamma_error=error, bernoulli_order=2*order)


def euler_tail(count, derivative):
    """Cauchy bound on the analytic remainder, radius 1/2, real s>=2."""
    if count < 1 or derivative not in (0, 1, 2):
        raise ValueError('Positive Euler count and derivative 0, 1 or 2 required')
    return F(2*factorial(derivative)*2**derivative, 2**count)


def eta_jet(s, logs, count=EULER_TERMS):
    """Ordinary derivatives (not factorial-divided jets) through order two."""
    if not isinstance(s, int) or s < 2 or len(logs) < count+1:
        raise ValueError('Integer s>=2 and a complete logarithm table required')
    result = []
    for derivative in range(3):
        row = [(-logs[n])**derivative/F(n**s) for n in range(1, count+1)]
        total = I(0)
        for k in range(count):
            total = total+row[0]/2**(k+1)
            row = [row[j]-row[j+1] for j in range(len(row)-1)]
        error = euler_tail(count, derivative)
        result.append(total+I(-error, error))
    return result


def zeta_jet(s, logs, log2, count=EULER_TERMS):
    ee = eta_jet(s, logs, count)
    power = F(1, 2**(s-1))
    dd = [I(1-power), power*log2, -power*log2**2]
    zz = [ee[0]/dd[0]]
    zz.append((ee[1]-dd[1]*zz[0])/dd[0])
    zz.append((ee[2]-2*dd[1]*zz[1]-dd[2]*zz[0])/dd[0])
    return zz


def psi_pair(s, cc):
    """Exact integer/half-integer recurrences for psi(s/2), psi'(s/2)."""
    if not isinstance(s, int) or s < 2:
        raise ValueError('Integer s>=2 required')
    if s % 2 == 0:
        terms = [F(k) for k in range(1, s//2)]
        psi, trigamma = -cc['gamma'], cc['pi']**2/6
    else:
        terms = [F(2*k+1, 2) for k in range((s-1)//2)]
        psi = -cc['gamma']-2*cc['log2']
        trigamma = cc['pi']**2/2
    return (psi+sum((1/x for x in terms), F(0)),
            trigamma-sum((1/x**2 for x in terms), F(0)))


def response(s, zz, cc):
    psi, tri = psi_pair(s, cc)
    logarithmic = zz[1]/zz[0]
    q = F(1, s)+F(1, s-1)-cc['logpi']/2+psi/2+logarithmic
    dq = -F(1, s*s)-F(1, (s-1)**2)+tri/4+zz[2]/zz[0]-logarithmic**2
    return q, dq


def source_entry(s, t, responses):
    a, b = F(2*s-1, 2), F(2*t-1, 2)
    if s == t:
        q, dq = responses[s]
        return dq+q/a
    return 2*(a*responses[s][0]-b*responses[t][0])/(a*a-b*b)


def separate_entry(s, t, jets, cc):
    """Independently assemble Gamma, complete prime overlap, and full pole."""
    a, b = F(2*s-1, 2), F(2*t-1, 2)
    ps, ts = psi_pair(s, cc)
    pt, _ = psi_pair(t, cc)
    ls, lt = -jets[s][1]/jets[s][0], -jets[t][1]/jets[t][0]
    if s == t:
        gamma = (ps+a*ts/2-cc['logpi'])/(2*a)
        dl = -jets[s][2]/jets[s][0]+(jets[s][1]/jets[s][0])**2
        prime = ls/a+dl
    else:
        gamma = ((a*ps-b*pt)/(a-b)-cc['logpi'])/(a+b)
        prime = (ls+lt)/(a+b)+(ls-lt)/(s-t)
    pole = F(1, s*(s-1)*t*(t-1))
    return gamma-prime-pole


def interval_ldl(matrix):
    """Positive interval pivots certify every real symmetric member of the box."""
    size = len(matrix)
    if not size or any(len(row) != size for row in matrix):
        raise ValueError('A nonempty square interval matrix is required')
    if any(matrix[i][j].record() != matrix[j][i].record()
           for i in range(size) for j in range(i)):
        raise ValueError('Symmetric interval matrix required')
    lower = [[I(0) for _ in range(size)] for _ in range(size)]
    pivots = []
    for i in range(size):
        lower[i][i] = I(1)
        pivot = matrix[i][i]
        for k in range(i):
            pivot = pivot-lower[i][k]**2*pivots[k]
        if pivot.lo <= 0:
            raise AssertionError(f'Uncertified pivot {i+1}: {pivot.record()}')
        pivots.append(pivot)
        for j in range(i+1, size):
            value = matrix[j][i]
            for k in range(i):
                value = value-lower[j][k]*lower[i][k]*pivots[k]
            lower[j][i] = value/pivot
    return pivots


def overlap(x, y):
    return max(x.lo, y.lo) <= min(x.hi, y.hi)


def replay(dimension=DIMENSION, count=EULER_TERMS):
    if not isinstance(dimension, int) or dimension < 1:
        raise ValueError('A positive finite dimension is required')
    cc = precise_constants()
    logs = [I(0)]+[integer_log(n, cc['log2']) for n in range(1, count+1)]
    nodes = list(range(3, dimension+3))
    jets = {s: zeta_jet(s, logs, cc['log2'], count) for s in nodes}
    responses = {s: response(s, jets[s], cc) for s in nodes}
    matrix = [[source_entry(s, t, responses) for t in nodes] for s in nodes]
    pivots = interval_ldl(matrix)
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name, status='PASS'))
    check('all_euler_derivative_tails_positive', all(euler_tail(count, j)>0 for j in range(3)))
    check('all_zeta_denominators_strictly_positive', all(jets[s][0].lo > 1 for s in nodes))
    check('all_complete_prime_masses_positive', all(jets[s][1].hi < 0 for s in nodes))
    check('all_mixed_source_entries_match_separate_assembly', all(
        overlap(matrix[i][j], separate_entry(s, t, jets, cc))
        for i, s in enumerate(nodes) for j, t in enumerate(nodes)))
    check('every_interval_ldl_pivot_strictly_positive', all(p.lo > 0 for p in pivots))
    check('all_laplace_rates_strictly_positive_and_distinct',
          len(set(nodes)) == dimension and all(s>2 for s in nodes))
    encoded = [[v.record() for v in row] for row in matrix]
    digest = hashlib.sha256(json.dumps(encoded, sort_keys=True).encode()).hexdigest()
    return dict(schema='rkf.endpoint-zero-shift-laplace.v1', date='2026-10-12',
        status='PASS_ZERO_SHIFT_FINITE_SUBSPACE', arithmetic='Inherited 90-digit outward Decimal and exact Fraction',
        eta='0/1', dimension=dimension, half_line_basis='h_j(x)=exp(-j*x), 1<=j<=dimension',
        source='Corrected SE4/T40 odd source, f(x)=sgn(x)*h(abs(x))/sqrt(2)',
        spatial_support='Unbounded; no spatial truncation', all_complex_linear_combinations=True,
        all_prime_powers_included=True, all_gamma_modes_included=True, full_pole_included=True,
        unobserved_complement_certified=False, global_eta_zero_certified=False,
        global_shift_frontier_unchanged='10883/18450', rh_proved=False,
        euler_terms=count, euler_remainders=[str(euler_tail(count, j)) for j in range(3)],
        gamma_bernoulli_order=cc['bernoulli_order'], gamma_remainder=str(cc['gamma_error']),
        constants={k:v.record() for k,v in cc.items() if isinstance(v, I)},
        zeta_jets={str(s):[x.record() for x in jets[s]] for s in nodes},
        responses={str(s):[x.record() for x in responses[s]] for s in nodes},
        matrix=encoded, matrix_sha256=digest, pivots=[p.record() for p in pivots],
        minimum_pivot_lower=str(min(p.lo for p in pivots)), checks=checks, check_count=len(checks))


def verify_source_pins():
    root = Path(__file__).resolve().parents[1]
    pins = json.loads(PINS.read_text())
    for name, expected in pins['sha256'].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest() != expected:
            raise AssertionError('SE21 source pin mismatch: '+name)
    return len(pins['sha256'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Write this new stage result')
    parser.add_argument('--check', action='store_true', help='Read-only exact result comparison')
    args = parser.parse_args()
    if args.write and args.check:
        parser.error('Choose --write or --check')
    result = replay()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+'\n')
    if args.check:
        if json.loads(RESULT.read_text()) != result:
            raise AssertionError('SE21 result differs from checked-in evidence')
        print('Source pins checked:', verify_source_pins())
    print(json.dumps({k:result[k] for k in ('status', 'dimension', 'eta',
        'minimum_pivot_lower', 'check_count', 'global_eta_zero_certified')}, indent=2))


if __name__ == '__main__':
    main()
