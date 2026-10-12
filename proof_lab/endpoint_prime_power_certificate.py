"""SE10: a complete odd-source certificate across the prime-power-4 event.

Scale 7/5, physical radius 7/10, catalogue {2,3,4}. The tighter quadrature
and Gamma/Bessel enclosures resolve the small positive margin. Earlier
stage files are imported unchanged and every infinite tail is retained.
"""
from __future__ import annotations

import argparse
from decimal import Context, Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import factorial, prod
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import (
        I, UP, constants, log_positive, sqrt_integer, hurwitz_power, cosine,
    )
    from proof_lab.endpoint_prime_event_certificate import interval_ldl
    from proof_lab.endpoint_paired_aperture_budget import exp_upper
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import (
        I, UP, constants, log_positive, sqrt_integer, hurwitz_power, cosine,
    )
    from endpoint_prime_event_certificate import interval_ldl
    from endpoint_paired_aperture_budget import exp_upper

SCALE = F(7, 5)
N, T, PANELS = 88, 192, 384
ORDER, GAMMA_TERMS, BESSEL_TERMS = 20, 32, 160
B, RHO = F(1, 10), F(7, 2)
INTEGRAND_BOUND = 256
CANDIDATE_CONTEXT = Context(prec=40, rounding=ROUND_HALF_EVEN)
RESULT = Path(__file__).with_name("ENDPOINT_PRIME_POWER_RESULT.json")
MATRIX = Path(__file__).with_name("ENDPOINT_PRIME_POWER_MATRIX.json")


def legendre_coefficients(n):
    coefficients = [F(0)]*(n+1)
    for k in range(n//2+1):
        coefficients[n-2*k] = F((-1)**k*factorial(2*n-2*k),
            2**n*factorial(k)*factorial(n-k)*factorial(n-2*k))
    return coefficients


def polynomial(coefficients, x):
    value = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        value = value*x+coefficient
    return value


def gauss20():
    """All P20 roots have disjoint exact sign brackets; weights are enclosed."""
    coefficients = legendre_coefficients(ORDER)
    derivative = [k*coefficients[k] for k in range(1, ORDER+1)]
    positive = []
    for start in [76, 227, 373, 510, 636, 746, 839, 912, 963, 993]:
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
    assert len(nodes) == ORDER
    weights = []
    for x in nodes:
        slope = polynomial(derivative, x)
        weight = 2/((1-x*x)*slope*slope)
        assert weight.lo > 0
        weights.append(weight)
    return nodes, weights


def gamma_symbol(t, mg, zeta):
    """128 direct terms, 32 alternating tail terms and a signed remainder."""
    assert 0 <= t.lo <= t.hi <= I(F(T)/SCALE).hi
    y2 = (t/2)**2
    total = I(0)
    for k in range(128):
        s = F(4*k+1, 4)
        total = total+y2/(s*(s*s+y2))
    power = y2
    for r in range(1, GAMMA_TERMS+1):
        total = total+((-1)**(r-1))*power*zeta[r-1]
        power = power*y2
    assert GAMMA_TERMS % 2 == 0
    remainder = power*zeta[GAMMA_TERMS]
    return total+I(0, remainder.hi)-mg


def odd_bessel(z):
    """j_1,...,j_175, seeded by j_176,j_177, for 0<z<=96."""
    assert z.lo > 0 and z.hi <= T//2
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


def pole_coefficients(roots):
    z, out = SCALE/4, []
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


def budgets():
    pi, log2, mg = constants()
    log3, log5 = log_positive(3), log_positive(5)
    logs = [log2, log3, 2*log2]
    # Lambda(4)=log(2), so its coefficient is log(2), not log(4).
    weights = [sqrt_integer(2)*log2, 2*log3/sqrt_integer(3), log2]
    prime_sum = sum(weights, I(0))
    assert (2*log2).hi < I(SCALE).lo < log5.lo
    assert prime_sum.hi < I(F(59, 20)).lo
    assert mg.hi < I(F(269, 50)).lo
    y = F(T, 2)/SCALE
    gamma_lower = sum((y*y/(F(4*k+1, 4)*(F(4*k+1, 4)**2+y*y))
                       for k in range(512)), F(0))-F(269, 50)
    assert gamma_lower > F(153, 50)
    assert F(153, 50)-F(59, 20) > B
    assert y < F(513, 4)
    # Panel half-width=1/4, ellipse rho=7/2; semimajor radius=53/112<1/2.
    ellipse_radius = (RHO+1/RHO)/8
    assert ellipse_radius == F(53, 112) < F(1, 2)
    assert F(1, 2)/SCALE < F(3, 8)
    beta = F(801, 2)
    symbol_bound = (F(269, 50)
        +34*sum((1/F(4*k+1, 2) for k in range(200)), F(0))
        +F(8, 3)*(T+1)**2*(beta**-3+F(1, 4)*beta**-2)+6+B)
    assert beta > 2*(T+1)
    assert symbol_bound < 200 < INTEGRAND_BOUND
    assert exp_upper(F(1, 2), 16) < 2
    assert symbol_bound*F(2, 3) < INTEGRAND_BOUND
    epsilon = 4*T*INTEGRAND_BOUND*RHO**(-2*ORDER)/(1-1/RHO)
    n = 2*N+1
    first_f = F((T//2)**n, prod(range(1, 2*n, 2)))
    tail_f = first_f/(1-F((T//2)**2, (2*n+1)*(2*n+3)))
    assert SCALE < 4 and exp_upper(SCALE/4, 12) < 2
    first_h = 4*(SCALE/4)**n/prod(range(1, 2*n, 2))
    tail_h = first_h/(1-(SCALE/4)**2/((2*n+1)*(2*n+3)))
    assert N < 100
    tau_d = F(T*INTEGRAND_BOUND, 3)*tail_f**2+2*tail_h**2
    tau_b = F(T*INTEGRAND_BOUND*10, 3)*tail_f+2*tail_h
    assert tau_d < F(1, 10**35) and tau_b < F(1, 10**17)
    aperture = SCALE/2
    boundary_upper = aperture**3/(3*(1-aperture**2/20))
    assert boundary_upper < F(1, 8)
    assert exp_upper(3*aperture, 20) < F(33, 4)
    native_budget = F(33, 4)+1+11+F(59, 20)+F(1, 8)
    assert native_budget == F(933, 40)
    return {
        'pi': pi, 'logs': logs, 'weights': weights, 'mg': mg, 'log5': log5,
        'prime_sum': prime_sum, 'gamma_lower': gamma_lower,
        'symbol_bound': symbol_bound, 'epsilon': epsilon, 'tail_f': tail_f,
        'tail_h': tail_h, 'tau_d': tau_d, 'tau_b': tau_b,
        'boundary_upper': boundary_upper, 'native_budget': native_budget,
    }


def assemble(budget, progress=False):
    zeta = [hurwitz_power(2*r+1) for r in range(1, GAMMA_TERMS+2)]
    roots = [sqrt_integer(2*n+1) for n in range(1, 2*N, 2)]
    poles = pole_coefficients(roots)
    nodes, weights = gauss20()
    matrix = [[I(0) for _ in range(N)] for _ in range(N)]
    for panel in range(PANELS):
        center = F(2*panel+1, 4)
        for node, weight in zip(nodes, weights):
            t = center+node/4
            assert 0 < t.lo <= t.hi < T
            physical_t = t/SCALE
            symbol = gamma_symbol(physical_t, budget['mg'], zeta)-B
            for logn, prime_weight in zip(budget['logs'], budget['weights']):
                symbol = symbol-prime_weight*cosine(physical_t*logn, budget['pi'])
            bessel = odd_bessel(t/2)
            vector = [root*j*((-1)**k) for k, (root, j) in enumerate(zip(roots, bessel))]
            measure = weight*symbol/(4*budget['pi'])
            for i in range(N):
                scaled = measure*vector[i]
                for j in range(i+1):
                    matrix[i][j] = matrix[i][j]+scaled*vector[j]
        if progress and panel % 32 == 31:
            print(f"prime-power panels {panel+1}/{PANELS}", flush=True)
    for i in range(N):
        for j in range(i+1):
            value = matrix[i][j]-2*SCALE*poles[i]*poles[j]
            if i == j:
                value = value+B
            matrix[i][j] = matrix[j][i] = value
    return matrix


def _replay(progress=False):
    budget = budgets()
    enclosed = assemble(budget, progress)
    candidate = [[CANDIDATE_CONTEXT.plus(value.midpoint()) for value in row]
                 for row in enclosed]
    radius = Decimal(0)
    for row, midrow in zip(enclosed, candidate):
        total = Decimal(0)
        for value, mid in zip(row, midrow):
            total = UP.add(total, max(UP.subtract(mid, value.lo), UP.subtract(value.hi, mid)))
        radius = max(radius, total)
    error = I(radius)+N*budget['epsilon']
    shift = F(1, 10_000_000_000)
    leading_floor, q = F(1, 12_500_000_000), F(1, 20_000_000_000)
    assert error.hi < I(shift-leading_floor).lo
    pivots = interval_ldl(candidate, shift)
    assert min(leading_floor, B-budget['tau_d'])-budget['tau_b'] > q
    native, reserve = q/(q+budget['native_budget']), 2*q/(11*(q+budget['native_budget']))
    def rat(x):
        return f'{x.numerator}/{x.denominator}'
    archive = {
        'schema': 'rkf.endpoint-prime-power-matrix.v1',
        'reference_aperture': '1/2', 'physical_aperture': '7/10', 'scale': '7/5',
        'common_prime_power_catalogue': [2, 3, 4], 'candidate_significant_digits': 40,
        'basis': 'L2-normalized odd Legendre orders 1,3,...,175 on [-1/2,1/2]',
        'matrix': [[str(x) for x in row] for row in candidate],
    }
    encoded = json.dumps(archive, indent=2)+'\n'
    result = {
        'schema': 'rkf.endpoint-prime-power-certificate.v1', 'date': '2026-10-12',
        'status': 'PASS', 'arithmetic': '90-digit outward Decimal; exact Fraction budgets; guarded ambient precision 90',
        'candidate_significant_digits': 40,
        'scale': rat(SCALE), 'reference_aperture': '1/2', 'physical_aperture': '7/10',
        'all_intermediate_scales_by_native_inclusion': ['1', '7/5'],
        'crossed_prime_power_event': 4, 'event_scale_enclosure': budget['logs'][2].record(),
        'next_event': 'log(5)', 'active_prime_powers': [2, 3, 4],
        'prime_power_4_weight': 'log(2)', 'prime_weight_sum_enclosure': budget['prime_sum'].record(),
        'gamma_ground_enclosure': budget['mg'].record(),
        'finite_gamma_lower_at_split': rat(budget['gamma_lower']),
        'boundary_upper': rat(budget['boundary_upper']),
        'frequency_split_in_reference_coordinates': T, 'high_frequency_floor': rat(B),
        'matrix_dimension': N, 'quadrature_order': ORDER, 'panels': PANELS,
        'gamma_alternating_terms': GAMMA_TERMS, 'bessel_correction_terms': BESSEL_TERMS,
        'ellipse_parameter': rat(RHO), 'analytic_integrand_bound': INTEGRAND_BOUND,
        'analytic_symbol_bound': rat(budget['symbol_bound']),
        'quadrature_error_per_entry': rat(budget['epsilon']),
        'point_evaluation_and_candidate_rounding_norm_error_upper': str(radius),
        'total_leading_matrix_error_upper': str(error.hi),
        'ldl_shift': rat(shift), 'positive_ldl_pivots': len(pivots),
        'ldl_pivot_enclosures': [p.record() for p in pivots],
        'exact_leading_matrix_floor': rat(leading_floor), 'first_discarded_odd_order': 2*N+1,
        'tail_deviation_upper': rat(budget['tau_d']), 'tail_coupling_upper': rat(budget['tau_b']),
        'physical_source_floor': rat(q), 'native_graph_budget': rat(budget['native_budget']),
        'native_source_floor': rat(native), 'relative_joint_reserve': rat(reserve),
        'matrix_sha256': hashlib.sha256(encoded.encode()).hexdigest(),
        'not_certified': ['positivity of every intermediate comparison K_c',
                          'all-prime-event sign-preserving rule', 'a numerical cost bound for arbitrary apertures',
                          'cofinal all-scale positivity', 'global eta=0 source sign',
                          'historical five-label endpoint or K0', 'Riemann hypothesis',
                          'proof-assistant verification or external review'],
    }
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
            raise SystemExit('SE10 replay mismatch: inspect changes instead of repinning.')
    keys = ['status', 'scale', 'physical_aperture', 'crossed_prime_power_event',
            'positive_ldl_pivots', 'total_leading_matrix_error_upper', 'physical_source_floor',
            'native_source_floor', 'relative_joint_reserve', 'matrix_sha256']
    print(json.dumps({key: result[key] for key in keys}, indent=2))


if __name__ == '__main__':
    main()
