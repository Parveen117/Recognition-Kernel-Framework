"""SE11: complete radius-4/5 certificate with exact signed-Gram accumulation.

The inherited interval primitives remain immutable. Integer sums assemble the
candidate; a separate rank-one operator bound encloses every node error.
"""
from __future__ import annotations

import argparse
from decimal import Context, Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import prod
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import (
        BERNOULLI, I, constants, log_positive, sqrt_integer, hurwitz_power, cosine,
    )
    from proof_lab.endpoint_prime_event_certificate import interval_ldl
    from proof_lab.endpoint_prime_power_certificate import legendre_coefficients, polynomial
    from proof_lab.endpoint_paired_aperture_budget import exp_upper
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import (
        BERNOULLI, I, constants, log_positive, sqrt_integer, hurwitz_power, cosine,
    )
    from endpoint_prime_event_certificate import interval_ldl
    from endpoint_prime_power_certificate import legendre_coefficients, polynomial
    from endpoint_paired_aperture_budget import exp_upper

SCALE = F(8, 5)
N, T, PANELS = 116, 256, 512
ORDER, GAMMA_TERMS, BESSEL_TERMS = 24, 64, 240
B, RHO = F(1, 10), F(4)
INTEGRAND_BOUND = 256
GRID = 10**50
CANDIDATE_CONTEXT = Context(prec=40, rounding=ROUND_HALF_EVEN)
RESULT = Path(__file__).with_name('ENDPOINT_PRECISION_FRONTIER_RESULT.json')
MATRIX = Path(__file__).with_name('ENDPOINT_PRECISION_FRONTIER_MATRIX.json')


def refined_constants():
    """Euler--Maclaurin through B12; absolute last-term remainder is retained."""
    pi, log2, _ = constants()
    k = 1024
    harmonic = sum((F(1, j) for j in range(1, k+1)), F(0))
    corrections = sum((b/F(2*j*k**(2*j))
                       for j, b in enumerate(BERNOULLI, 1)), F(0))
    error = abs(BERNOULLI[-1])/F(12*k**12)
    gamma = I(harmonic-F(1, 2*k)+corrections)-10*log2+I(-error, error)
    return pi, log2, gamma+pi/2+3*log2+log_positive(pi)


def gauss24():
    coefficients = legendre_coefficients(ORDER)
    derivative = [k*coefficients[k] for k in range(1, ORDER+1)]
    positive = []
    for start in [64, 191, 315, 433, 545, 648, 740, 820, 886, 938, 974, 995]:
        lo, hi = F(start, 1000), F(start+1, 1000)
        sign = polynomial(coefficients, lo)
        assert sign*polynomial(coefficients, hi) < 0
        for _ in range(260):
            mid = (lo+hi)/2
            if polynomial(coefficients, mid)*sign > 0:
                lo = mid
            else:
                hi = mid
        positive.append(I(lo, hi))
    nodes = [-x for x in reversed(positive)]+positive
    weights = [2/((1-x*x)*polynomial(derivative, x)**2) for x in nodes]
    assert len(nodes) == ORDER and all(w.lo > 0 for w in weights)
    return nodes, weights


def gamma_symbol(t, mg, zeta):
    assert 0 <= t.lo <= t.hi <= I(F(T)/SCALE).hi
    y2, total = (t/2)**2, I(0)
    for k in range(128):
        s = F(4*k+1, 4)
        total = total+y2/(s*(s*s+y2))
    power = y2
    for r in range(1, GAMMA_TERMS+1):
        total = total+((-1)**(r-1))*power*zeta[r-1]
        power = power*y2
    remainder = power*zeta[GAMMA_TERMS]
    return total+I(0, remainder.hi)-mg


def odd_bessel(z):
    """Enclosed seeds j232,j233 followed by downward recurrence, z<=128."""
    assert 0 < z.lo <= z.hi <= T//2
    values = {}
    for n in (2*N, 2*N+1):
        term = z**n/prod(range(1, 2*n+2, 2))
        total = term
        for k in range(1, BESSEL_TERMS+1):
            term = -term*z*z/(2*k*(2*n+2*k+1))
            total = total+term
        k = BESSEL_TERMS+1
        assert F((T//2)**2, 2*k*(2*n+2*k+1)) < 1
        following = -term*z*z/(2*k*(2*n+2*k+1))
        error = following.abs_upper()
        values[n] = total+I(error.copy_negate(), error)
    for n in range(2*N, 1, -1):
        values[n-1] = (2*n+1)*values[n]/z-values[n+1]
    return [values[n] for n in range(1, 2*N, 2)]


def pole_coefficients(roots, scale=SCALE):
    z, out = scale/4, []
    for n, root in zip(range(1, 2*N, 2), roots):
        term = I(z**n/prod(range(1, 2*n+2, 2)))
        total = term
        for k in range(1, 41):
            term = term*z*z/(2*k*(2*n+2*k+1))
            total = total+term
        following = term*z*z/(82*(2*n+83))
        ratio = z*z/(84*(2*n+85))
        out.append(root*(total+I(0, (following/(1-ratio)).hi)))
    return out


def grid_point(value):
    """Any exact grid point is allowed; distance to the whole interval is kept."""
    integer = int(value.midpoint()*GRID)
    point = F(integer, GRID)
    return integer, (value-I(point)).abs_upper()


def node_error(measure, vector):
    """||M vv* - mu uu*|| <= delta + |mu| e(2+e), using ||v||<=1.

    Bessel's inequality gives the unit norm bound for the real Fourier
    readings in the normalized odd Legendre basis, independent of N.
    """
    weight, delta = grid_point(measure)
    pairs = [grid_point(value) for value in vector]
    e = sum((I(radius) for _, radius in pairs), I(0))
    error = I(delta)+abs(F(weight, GRID))*e*(2+e)
    return weight, [integer for integer, _ in pairs], error


def budgets():
    pi, log2, mg = refined_constants()
    log3, log5 = log_positive(3), log_positive(5)
    logs = [log2, log3, 2*log2]
    weights = [sqrt_integer(2)*log2, 2*log3/sqrt_integer(3), log2]
    prime_sum = sum(weights, I(0))
    assert (2*log2).hi < I(SCALE).lo < log5.lo
    assert prime_sum.hi < I(F(59, 20)).lo and mg.hi < I(F(269, 50)).lo
    assert F(mg.hi)-F(mg.lo) < F(1, 10**37)
    y = F(T, 2)/SCALE
    gamma_lower = sum((y*y/(F(4*k+1, 4)*(F(4*k+1, 4)**2+y*y))
                       for k in range(512)), F(0))-F(269, 50)
    assert gamma_lower > F(16, 5) and F(16, 5)-F(59, 20) > B
    assert y < F(513, 4)
    ellipse_radius = (RHO+1/RHO)/8
    assert ellipse_radius == F(17, 32) and ellipse_radius/SCALE < F(3, 8)
    beta = F(1201, 2)
    symbol_bound = (F(269, 50)
        +34*sum((1/F(4*k+1, 2) for k in range(300)), F(0))
        +F(8, 3)*(T+1)**2*(beta**-3+F(1, 4)*beta**-2)+6+B)
    assert beta > 2*(T+1) and symbol_bound < 200
    assert (ellipse_radius*logs[-1]/SCALE).hi < I(F(1, 2)).lo
    assert exp_upper(ellipse_radius, 18) < 2 and exp_upper(F(1, 2), 16) < 2
    assert symbol_bound*F(2, 3) < INTEGRAND_BOUND
    epsilon = 4*T*INTEGRAND_BOUND*RHO**(-2*ORDER)/(1-1/RHO)
    n = 2*N+1
    first_f = F((T//2)**n, prod(range(1, 2*n, 2)))
    tail_f = first_f/(1-F((T//2)**2, (2*n+1)*(2*n+3)))
    assert SCALE < 4 and exp_upper(SCALE/4, 12) < 2 and N < 144
    first_h = 4*(SCALE/4)**n/prod(range(1, 2*n, 2))
    tail_h = first_h/(1-(SCALE/4)**2/((2*n+1)*(2*n+3)))
    tau_d = F(T*INTEGRAND_BOUND, 3)*tail_f**2+2*tail_h**2
    tau_b = F(T*INTEGRAND_BOUND*12, 3)*tail_f+2*tail_h
    assert tau_d < F(1, 10**48) and tau_b < F(1, 10**24)
    aperture = SCALE/2
    boundary_upper = aperture**3/(3*(1-aperture**2/20))
    assert boundary_upper < F(1, 5) and exp_upper(3*aperture, 24) < F(45, 4)
    native_budget = F(45, 4)+1+11+F(59, 20)+F(1, 5)
    assert native_budget == F(132, 5)
    return dict(pi=pi, logs=logs, weights=weights, mg=mg, log5=log5,
                prime_sum=prime_sum, gamma_lower=gamma_lower,
                symbol_bound=symbol_bound, epsilon=epsilon, tail_f=tail_f,
                tail_h=tail_h, tau_d=tau_d, tau_b=tau_b,
                boundary_upper=boundary_upper, native_budget=native_budget)


def assemble(budget, progress=False):
    zeta = [hurwitz_power(2*r+1) for r in range(1, GAMMA_TERMS+2)]
    roots = [sqrt_integer(2*n+1) for n in range(1, 2*N, 2)]
    poles = pole_coefficients(roots)
    nodes, weights = gauss24()
    matrix = [[0 for _ in range(i+1)] for i in range(N)]
    point_error = I(0)
    for panel in range(PANELS):
        center = F(2*panel+1, 4)
        for node, weight in zip(nodes, weights):
            t = center+node/4
            physical_t = t/SCALE
            symbol = gamma_symbol(physical_t, budget['mg'], zeta)-B
            for logn, prime_weight in zip(budget['logs'], budget['weights']):
                symbol = symbol-prime_weight*cosine(physical_t*logn, budget['pi'])
            vector = [root*j*((-1)**k)
                      for k, (root, j) in enumerate(zip(roots, odd_bessel(t/2)))]
            measure = weight*symbol/(4*budget['pi'])
            integer_weight, integers, error = node_error(measure, vector)
            point_error = point_error+error
            for i, row in enumerate(matrix):
                scaled = integer_weight*integers[i]
                for j in range(i+1):
                    row[j] += scaled*integers[j]
        if progress and panel % 32 == 31:
            print(f'precision-frontier panels {panel+1}/{PANELS}', flush=True)
    enclosed = [[I(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            value = I(F(matrix[i][j], GRID**3))-2*SCALE*poles[i]*poles[j]
            if i == j:
                value = value+B
            enclosed[i][j] = enclosed[j][i] = value
    return enclosed, point_error


def _replay(progress=False):
    budget = budgets()
    enclosed, point_error = assemble(budget, progress)
    candidate = [[CANDIDATE_CONTEXT.plus(value.midpoint()) for value in row]
                 for row in enclosed]
    radius = I(0)
    for row, midrow in zip(enclosed, candidate):
        total = sum((I((value-I(mid)).abs_upper()) for value, mid in zip(row, midrow)), I(0))
        radius = I(max(radius.hi, total.hi))
    error = radius+point_error+N*budget['epsilon']
    shift, leading_floor, q = F(6, 10**15), F(5, 10**15), F(4, 10**15)
    assert error.hi < I(shift-leading_floor).lo
    pivots = interval_ldl(candidate, shift)
    assert min(leading_floor, B-budget['tau_d'])-budget['tau_b'] > q
    native = q/(q+budget['native_budget'])
    reserve = 2*native/11
    def rat(x):
        return f'{x.numerator}/{x.denominator}'
    archive = dict(schema='rkf.endpoint-precision-frontier-matrix.v1',
                   reference_aperture='1/2', physical_aperture='4/5', scale='8/5',
                   active_prime_powers=[2, 3, 4], candidate_significant_digits=40,
                   basis='L2-normalized odd Legendre orders 1,3,...,231 on [-1/2,1/2]',
                   matrix=[[str(x) for x in row] for row in candidate])
    encoded = json.dumps(archive, indent=2)+'\n'
    result = dict(
        schema='rkf.endpoint-precision-frontier-certificate.v1', date='2026-10-12', status='PASS',
        arithmetic='90-digit outward Decimal; exact rational budgets and integer signed-Gram sums',
        candidate_significant_digits=40, integer_grid_digits=50,
        scale=rat(SCALE), reference_aperture='1/2', physical_aperture='4/5',
        all_smaller_apertures_by_native_inclusion=True, active_prime_powers=[2, 3, 4],
        next_event='log(5)', next_event_scale_enclosure=budget['log5'].record(),
        prime_weight_sum_enclosure=budget['prime_sum'].record(),
        gamma_ground_enclosure=budget['mg'].record(),
        finite_gamma_lower_at_split=rat(budget['gamma_lower']),
        frequency_split_in_reference_coordinates=T, high_frequency_floor=rat(B),
        matrix_dimension=N, quadrature_order=ORDER, panels=PANELS,
        gamma_alternating_terms=GAMMA_TERMS, bessel_correction_terms=BESSEL_TERMS,
        ellipse_parameter=rat(RHO), analytic_integrand_bound=INTEGRAND_BOUND,
        analytic_symbol_bound=rat(budget['symbol_bound']),
        quadrature_error_per_entry=rat(budget['epsilon']),
        signed_gram_point_operator_error_upper=str(point_error.hi),
        final_candidate_and_pole_norm_error_upper=str(radius.hi),
        total_leading_matrix_error_upper=str(error.hi),
        ldl_shift=rat(shift), positive_ldl_pivots=len(pivots),
        ldl_pivot_enclosures=[p.record() for p in pivots],
        exact_leading_matrix_floor=rat(leading_floor), first_discarded_odd_order=2*N+1,
        tail_deviation_upper=rat(budget['tau_d']), tail_coupling_upper=rat(budget['tau_b']),
        physical_source_floor=rat(q), boundary_upper=rat(budget['boundary_upper']),
        native_graph_budget=rat(budget['native_budget']), native_source_floor=rat(native),
        relative_joint_reserve=rat(reserve),
        matrix_sha256=hashlib.sha256(encoded.encode()).hexdigest(),
        not_certified=['prime-5 crossing', 'all-scale source signs', 'global eta=0 source sign',
                       'historical five-label endpoint or K0', 'Riemann hypothesis',
                       'proof-assistant verification or external review'])
    return result, encoded


def replay(progress=False):
    with localcontext() as context:
        context.prec = 90
        return _replay(progress)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result, matrix = replay(progress=True)
    if args.write:
        MATRIX.write_text(matrix, encoding='utf-8')
        RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    if args.check:
        if MATRIX.read_text(encoding='utf-8') != matrix or json.loads(RESULT.read_text()) != result:
            raise SystemExit('SE11 replay mismatch: inspect changes instead of repinning.')
    keys = ['status', 'scale', 'physical_aperture', 'positive_ldl_pivots',
            'total_leading_matrix_error_upper', 'physical_source_floor',
            'native_source_floor', 'relative_joint_reserve', 'matrix_sha256']
    print(json.dumps({key: result[key] for key in keys}, indent=2))


if __name__ == '__main__':
    main()
