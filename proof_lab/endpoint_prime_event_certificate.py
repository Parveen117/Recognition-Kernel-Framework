"""SE9: full odd source certificate beyond the prime-3 activation event.

The fixed reference aperture is 1/2, the physical scale is 9/8, and the
common prime catalogue is {2,3}. All tails and rounding errors are retained.
SE7 supplies immutable interval primitives; this is not another engine.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import prod
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import (
        I, UP, constants, log_positive, sqrt_integer, hurwitz_power,
        gamma_symbol, cosine, gauss8,
    )
    from proof_lab.endpoint_paired_aperture_budget import exp_upper
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import (
        I, UP, constants, log_positive, sqrt_integer, hurwitz_power,
        gamma_symbol, cosine, gauss8,
    )
    from endpoint_paired_aperture_budget import exp_upper

SCALE = F(9, 8)
N, T, PANELS = 52, 96, 768
B = F(1, 5)
RESULT = Path(__file__).with_name("ENDPOINT_PRIME_EVENT_RESULT.json")
MATRIX = Path(__file__).with_name("ENDPOINT_PRIME_EVENT_MATRIX.json")


def odd_bessel(z):
    """j_1,...,j_103 for 0<z<=48, with enclosed seeds j_104,j_105."""
    assert z.lo > 0 and z.hi <= 48
    values = {}
    for n in (2*N, 2*N+1):
        term = z**n / prod(range(1, 2*n+2, 2))
        total = term
        for k in range(1, 91):
            term = -term*z*z/(2*k*(2*n+2*k+1))
            total = total + term
        # After the retained k=90 term, absolute term ratios decrease.
        assert F(48**2, 182*(2*n+183)) < 1
        next_term = -term*z*z/(182*(2*n+183))
        error = next_term.abs_upper()
        values[n] = total + I(error.copy_negate(), error)
    for n in range(2*N, 1, -1):
        values[n-1] = (2*n+1)*values[n]/z - values[n+1]
    return [values[n] for n in range(1, 2*N, 2)]


def pole_coefficients(roots):
    """Coefficients without sqrt(c); the Gram retains its exact factor c."""
    z = SCALE/4
    out = []
    for n, root in zip(range(1, 2*N, 2), roots):
        term = I(z**n/prod(range(1, 2*n+2, 2)))
        total = term
        for k in range(1, 41):
            term = term*z*z/(2*k*(2*n+2*k+1))
            total = total + term
        following = term*z*z/(82*(2*n+83))
        ratio = z*z/(84*(2*n+85))
        out.append(root*(total+I(0, (following/(1-ratio)).hi)))
    return out


def interval_ldl(candidate, shift):
    """Certify a symmetric rational candidate at its actual dimension."""
    size = len(candidate)
    assert all(len(row) == size for row in candidate)
    assert all(candidate[i][j] == candidate[j][i]
               for i in range(size) for j in range(i))
    lower = [[I(0) for _ in range(size)] for _ in range(size)]
    pivots = []
    for i in range(size):
        lower[i][i] = I(1)
        pivot = I(candidate[i][i])-shift
        for k in range(i):
            pivot = pivot-lower[i][k]*lower[i][k]*pivots[k]
        if pivot.lo <= 0:
            raise AssertionError(f"Uncertified LDL pivot {i}: {pivot.record()}")
        pivots.append(pivot)
        for j in range(i+1, size):
            value = I(candidate[j][i])
            for k in range(i):
                value = value-lower[j][k]*lower[i][k]*pivots[k]
            lower[j][i] = value/pivot
    return pivots


def budgets():
    pi, log2, mg = constants()
    log3 = log_positive(3)
    weight2 = sqrt_integer(2)*log2
    weight3 = 2*log3/sqrt_integer(3)
    prime_sum = weight2+weight3
    assert log2.hi < 1 < log3.lo
    assert log3.hi < I(SCALE).lo < (2*log2).lo
    assert prime_sum.hi < I(F(9, 4)).lo
    assert mg.hi < I(F(27, 5)).lo
    # Monotone G: the first 128 positive summands alone suffice beyond T/c.
    y = F(T, 2)/SCALE
    gamma_lower = sum((y*y/(F(4*k+1, 4)*(F(4*k+1, 4)**2+y*y))
                       for k in range(128)), F(0))-F(27, 5)
    assert gamma_lower > F(5, 2)
    assert F(5, 2)-F(9, 4) > B
    assert y < F(513, 4)  # Validates the imported alternating Gamma tail.
    # On each rho=7 ellipse for a width-1/8 panel: |z|<97, |Im z|<1/4.
    beta = F(401, 2)
    symbol_bound = (F(27, 5)
        + 10*sum((1/F(4*k+1, 2) for k in range(100)), F(0))
        + F(8, 3)*97**2*(beta**-3+F(1, 4)*beta**-2)+3+B)
    assert symbol_bound < 100
    assert symbol_bound*F(4, 9) < 100
    assert exp_upper(F(9, 32), 12) < F(4, 3)
    # Prime cosines have |Im(argument)|<9/32; their total modulus <3.
    epsilon = F(4*T*100)*F(1, 7)**16/(1-F(1, 7))
    n = 2*N+1
    first_f = F((T//2)**n, prod(range(1, 2*n, 2)))
    tail_f = first_f/(1-F((T//2)**2, (2*n+1)*(2*n+3)))
    # sqrt(c)<2, exp(c/4)<2, and sqrt(2n+1)/(2n+1)<=1.
    assert SCALE < 4 and exp_upper(SCALE/4, 12) < 2
    first_h = 4*(SCALE/4)**n/prod(range(1, 2*n, 2))
    tail_h = first_h/(1-(SCALE/4)**2/((2*n+1)*(2*n+3)))
    assert N < 64
    tau_d = F(T*100, 3)*tail_f**2+2*tail_h**2
    tau_b = F(T*100*8, 3)*tail_f+2*tail_h
    assert tau_d < F(1, 10**30) and tau_b < F(1, 10**16)
    aperture = SCALE/2
    # Exact odd-pole norm squared is sinh(A)-A, hence <1 on this range.
    boundary_upper = aperture**3/(3*(1-aperture**2/20))
    assert boundary_upper < F(1, 16)
    assert exp_upper(3*aperture, 20) < F(11, 2)
    native_budget = F(11, 2)+1+11+F(9, 4)+F(1, 16)
    assert native_budget == F(317, 16)
    return {
        'pi': pi, 'logs': [log2, log3], 'weights': [weight2, weight3], 'mg': mg,
        'prime_sum': prime_sum, 'gamma_lower': gamma_lower,
        'symbol_bound': symbol_bound, 'epsilon': epsilon, 'tail_f': tail_f,
        'tail_h': tail_h, 'tau_d': tau_d, 'tau_b': tau_b,
        'boundary_upper': boundary_upper, 'native_budget': native_budget,
    }


def assemble(budget, progress=False):
    zeta = [hurwitz_power(2*r+1) for r in range(1, 12)]
    roots = [sqrt_integer(2*n+1) for n in range(1, 2*N, 2)]
    poles = pole_coefficients(roots)
    nodes, weights = gauss8()
    matrix = [[I(0) for _ in range(N)] for _ in range(N)]
    for panel in range(PANELS):
        center = F(2*panel+1, 16)
        for node, weight in zip(nodes, weights):
            t = center+node/16
            assert 0 < t.lo <= t.hi < T
            physical_t = t/SCALE
            symbol = gamma_symbol(physical_t, budget['mg'], zeta)-B
            for logp, prime_weight in zip(budget['logs'], budget['weights']):
                symbol = symbol-prime_weight*cosine(physical_t*logp, budget['pi'])
            bessel = odd_bessel(t/2)
            vector = [root*j*((-1)**k) for k, (root, j) in enumerate(zip(roots, bessel))]
            measure = weight*symbol/(16*budget['pi'])
            for i in range(N):
                scaled = measure*vector[i]
                for j in range(i+1):
                    matrix[i][j] = matrix[i][j]+scaled*vector[j]
        if progress and panel % 64 == 63:
            print(f"prime-event panels {panel+1}/{PANELS}", flush=True)
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
    candidate = [[value.midpoint() for value in row] for row in enclosed]
    radius = Decimal(0)
    for row, midrow in zip(enclosed, candidate):
        total = Decimal(0)
        for value, mid in zip(row, midrow):
            total = UP.add(total, max(UP.subtract(mid, value.lo), UP.subtract(value.hi, mid)))
        radius = max(radius, total)
    error = I(radius)+N*budget['epsilon']
    shift, leading_floor, q = F(3, 10**6), F(1, 400000), F(1, 500000)
    assert error.hi < I(shift-leading_floor).lo
    pivots = interval_ldl(candidate, shift)
    assert min(leading_floor, B-budget['tau_d'])-budget['tau_b'] > q
    native = q/(q+budget['native_budget'])
    reserve = 2*native/11
    def rat(x):
        return f'{x.numerator}/{x.denominator}'
    archive = {
        'schema': 'rkf.endpoint-prime-event-matrix.v1',
        'reference_aperture': '1/2', 'physical_aperture': '9/16', 'scale': '9/8',
        'common_prime_catalogue': [2, 3],
        'basis': 'L2-normalized odd Legendre orders 1,3,...,103 on [-1/2,1/2]',
        'matrix': [[str(x) for x in row] for row in candidate],
    }
    encoded = json.dumps(archive, indent=2)+'\n'
    result = {
        'schema': 'rkf.endpoint-prime-event-certificate.v1', 'date': '2026-10-12',
        'status': 'PASS', 'arithmetic': '90-digit outward Decimal; exact Fraction budgets; guarded ambient precision 90',
        'scale': rat(SCALE), 'reference_aperture': '1/2', 'physical_aperture': '9/16',
        'all_intermediate_scales_by_native_inclusion': ['1', '9/8'],
        'crossed_prime_event': 3, 'event_scale_enclosure': budget['logs'][1].record(),
        'next_event': 'log(4)', 'active_prime_powers': [2, 3], 'common_prime_catalogue': [2, 3],
        'prime_weight_sum_enclosure': budget['prime_sum'].record(),
        'gamma_ground_enclosure': budget['mg'].record(),
        'finite_gamma_lower_at_split': rat(budget['gamma_lower']),
        'boundary_upper': rat(budget['boundary_upper']),
        'frequency_split_in_reference_coordinates': T, 'high_frequency_floor': rat(B),
        'matrix_dimension': N, 'quadrature_order': 8, 'panels': PANELS,
        'ellipse_parameter': 7, 'analytic_integrand_bound': 100,
        'analytic_symbol_bound': rat(budget['symbol_bound']),
        'quadrature_error_per_entry': rat(budget['epsilon']),
        'point_evaluation_matrix_norm_error_upper': str(radius),
        'total_leading_matrix_error_upper': str(error.hi),
        'ldl_shift': rat(shift), 'positive_ldl_pivots': len(pivots),
        'ldl_pivot_enclosures': [p.record() for p in pivots],
        'exact_leading_matrix_floor': rat(leading_floor),
        'first_discarded_odd_order': 2*N+1,
        'tail_deviation_upper': rat(budget['tau_d']), 'tail_coupling_upper': rat(budget['tau_b']),
        'physical_source_floor': rat(q), 'native_graph_budget': rat(budget['native_budget']),
        'native_source_floor': rat(native), 'relative_joint_reserve': rat(reserve),
        'matrix_sha256': hashlib.sha256(encoded.encode()).hexdigest(),
        'not_certified': ['positivity of every intermediate comparison K_c',
                          'all-prime-event sign-preserving rule', 'cofinal all-scale positivity',
                          'global eta=0 source sign', 'historical five-label endpoint or K0',
                          'Riemann hypothesis', 'proof-assistant verification or external review'],
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
            raise SystemExit('SE9 replay mismatch: inspect changes instead of repinning.')
    keys = ['status', 'scale', 'physical_aperture', 'crossed_prime_event',
            'positive_ldl_pivots', 'total_leading_matrix_error_upper', 'physical_source_floor',
            'native_source_floor', 'relative_joint_reserve', 'matrix_sha256']
    print(json.dumps({key: result[key] for key in keys}, indent=2))


if __name__ == '__main__':
    main()
