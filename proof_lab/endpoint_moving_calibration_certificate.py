"""SE14: radius-21/25 certificate with three source-null markers.

The complete source is unchanged. All frequencies, all modes and every
arithmetic error are enclosed; finite aperture growth is not a global limit.
"""
from __future__ import annotations

import argparse
from decimal import Context, Decimal, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import prod
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import (
        BERNOULLI, I, log_positive, sqrt_integer, cosine,
    )
    from proof_lab.endpoint_precision_frontier_certificate import (
        GRID, gauss24, node_error, refined_constants,
    )
    from proof_lab.endpoint_paired_aperture_budget import exp_upper
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import (
        BERNOULLI, I, log_positive, sqrt_integer, cosine,
    )
    from endpoint_precision_frontier_certificate import (
        GRID, gauss24, node_error, refined_constants,
    )
    from endpoint_paired_aperture_budget import exp_upper

SCALE = F(42, 25)
N, T, PANELS = 208, 512, 1024
B, RHO = F(1, 10), F(5)
MARKERS = ((1, F(-1, 3)), (2, F(1, 9)), (3, F(-1, 8)))
ORDER, INTEGRAND_BOUND = 24, 256
BESSEL_TERMS, FIXED_GRID = 480, 10**240
TAIL_END, TAIL_LIPSCHITZ = 2048, F(5)
CANDIDATE_CONTEXT = Context(prec=40)
LDL_PRECISION = 512
RESULT = Path(__file__).with_name('ENDPOINT_MOVING_CALIBRATION_RESULT.json')
MATRIX = Path(__file__).with_name('ENDPOINT_MOVING_CALIBRATION_MATRIX.json')


def interval_ldl(candidate, shift):
    """A separate directed-512-digit LDL; inherited interval contexts stay fixed.

    Only the rational candidate is factorized. The operator error between
    that candidate and the true head is subtracted independently.
    """
    down = Context(prec=LDL_PRECISION, rounding=ROUND_FLOOR)
    up = Context(prec=LDL_PRECISION, rounding=ROUND_CEILING)
    class LdlInterval:
        def __init__(self, value=0, high=None):
            if high is not None:
                self.lo, self.hi = value, high
            else:
                exact = F(value)
                a, b = Decimal(exact.numerator), Decimal(exact.denominator)
                self.lo, self.hi = down.divide(a, b), up.divide(a, b)
        def __sub__(self, other):
            if not isinstance(other, LdlInterval):
                other = LdlInterval(other)
            return LdlInterval(down.subtract(self.lo, other.hi), up.subtract(self.hi, other.lo))
        def __mul__(self, other):
            lows = [down.multiply(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
            highs = [up.multiply(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
            return LdlInterval(min(lows), max(highs))
        def __truediv__(self, other):
            assert other.lo > 0
            lows = [down.divide(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
            highs = [up.divide(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
            return LdlInterval(min(lows), max(highs))
        def record(self):
            return [str(self.lo), str(self.hi)]
    size = len(candidate)
    assert all(len(row) == size for row in candidate)
    assert all(candidate[i][j] == candidate[j][i]
               for i in range(size) for j in range(i))
    lower = [[None for _ in range(size)] for _ in range(size)]
    pivots = []
    for i in range(size):
        lower[i][i] = LdlInterval(1)
        pivot = LdlInterval(candidate[i][i])-shift
        for k in range(i):
            pivot = pivot-lower[i][k]*lower[i][k]*pivots[k]
        if pivot.lo <= 0:
            raise AssertionError(f'Uncertified refined LDL pivot {i}: {pivot.record()}')
        pivots.append(pivot)
        for j in range(i+1, size):
            value = LdlInterval(candidate[j][i])
            for k in range(i):
                value = value-lower[j][k]*lower[i][k]*pivots[k]
            lower[j][i] = value/pivot
    return pivots


def complex_product(left, right):
    a, b = left
    c, d = right
    return a*c-b*d, a*d+b*c


def reduced_log(x, log2):
    exponent = 0
    while x.lo >= 2:
        x = x/2
        exponent += 1
    assert x.lo >= 1 and x.hi < 3
    return log_positive(x)+exponent*log2


def gamma_symbol(t, budget):
    """Shifted complex digamma with an absolute periodic-Bernoulli tail."""
    assert t.lo >= 0
    a, y = F(513, 4), t/2
    denominator = a*a+y*y
    inverse = (a/denominator, -y/denominator)
    square = complex_product(inverse, inverse)
    power = (I(1), I(0))
    value = reduced_log(denominator, budget['log2'])/2-inverse[0]/2-budget['log_pi']
    for k, bernoulli in enumerate(BERNOULLI, 1):
        power = complex_product(power, square)
        value = value-bernoulli*power[0]/(2*k)
    for k in range(128):
        s = F(4*k+1, 4)
        value = value-s/(s*s+y*y)
    error = abs(BERNOULLI[-1])/(12*a**12)
    return value+I(-error, error)


def _fixed(x):
    x = F(x)*FIXED_GRID
    return x.numerator//x.denominator, -((-x.numerator)//x.denominator)


def _fadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def _fneg(x):
    return -x[1], -x[0]


def _fmul(x, y):
    products = [a*b for a in x for b in y]
    return min(products)//FIXED_GRID, -((-max(products))//FIXED_GRID)


def _fdivint(x, divisor):
    assert divisor > 0
    return x[0]//divisor, -((-x[1])//divisor)


def odd_bessel(z):
    """Point-normalized Bessel recurrence on an exact 240-place interval grid.

    S_n=j_n(z)*(2n+1)!!/z^n avoids small-argument underflow. Evaluate
    at a rational point, then bound node displacement with |j_n'|<=1/2.
    No inherited Decimal context or earlier replay is mutated.
    """
    assert 0 < z.lo <= z.hi <= T//2
    point = F(z.midpoint())
    displacement = (z-I(point)).abs_upper()
    z2 = _fixed(point*point)
    values = {}
    for n in (2*N, 2*N+1):
        term = total = _fixed(1)
        for k in range(1, BESSEL_TERMS+1):
            term = _fneg(_fdivint(_fmul(term, z2), 2*k*(2*n+2*k+1)))
            total = _fadd(total, term)
        k = BESSEL_TERMS+1
        assert F((T//2)**2, 2*k*(2*n+2*k+1)) < 1
        following = _fdivint(_fmul(term, z2), 2*k*(2*n+2*k+1))
        error = max(abs(following[0]), abs(following[1]))
        values[n] = total[0]-error, total[1]+error
    for n in range(2*N, 1, -1):
        correction = _fdivint(_fmul(z2, values[n+1]), (2*n+1)*(2*n+3))
        values[n-1] = _fadd(values[n], _fneg(correction))
    coefficient, out = I(point)/3, []
    shift = I(displacement)/2
    for n in range(1, 2*N, 2):
        lo, hi = values[n]
        value = coefficient*I(F(lo, FIXED_GRID), F(hi, FIXED_GRID))
        out.append(value+I(shift.hi.copy_negate(), shift.hi))
        coefficient = coefficient*point*point/((2*n+3)*(2*n+5))
    return out


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


def marker_symbol(t, budget):
    return sum((coefficient*cosine(shift*t, budget['pi'])
                for shift, coefficient in MARKERS), I(0))


def marked_symbol(t, budget):
    value = gamma_symbol(t/SCALE, budget)
    for logn, weight in zip(budget['logs'], budget['weights']):
        value = value-weight*cosine(t*logn/SCALE, budget['pi'])
    return value+marker_symbol(t, budget)


def budgets():
    pi, log2, mg = refined_constants()
    logs = [log2, log_positive(3), 2*log2, log_positive(5)]
    weights = [sqrt_integer(2)*log2, 2*logs[1]/sqrt_integer(3),
               log2, 2*logs[3]/sqrt_integer(5)]
    prime_sum = sum(weights, I(0))
    assert logs[3].hi < I(SCALE).lo < log_positive(7).lo
    assert prime_sum.hi < I(F(22, 5)).lo and mg.hi < I(F(269, 50)).lo
    marker_norm = sum((abs(a) for _, a in MARKERS), F(0))
    assert marker_norm == F(41, 72)
    derivative = F(5, 2*T)+sum((w*l/SCALE for w, l in zip(weights, logs)), I(0))+sum(k*abs(a) for k, a in MARKERS)
    assert derivative.hi < I(TAIL_LIPSCHITZ).lo
    # Width-half panel, rho=5. The actual semiminor is 3/5.
    ellipse_radius, ellipse_imaginary = F(13, 20), F(3, 5)
    assert ellipse_imaginary/SCALE < F(3, 8)
    beta = F(2081, 2)
    symbol_bound = (F(269, 50)
        +34*sum((1/F(4*k+1, 2) for k in range(520)), F(0))
        +F(8, 3)*(T+1)**2*(beta**-3+F(1, 4)*beta**-2)+10+B)
    assert beta > 2*(T+1) and symbol_bound < 200
    assert logs[3].hi < I(SCALE).lo and exp_upper(ellipse_imaginary, 18) < 2
    analytic_event_bound = F(22, 5)*exp_upper(ellipse_imaginary, 24)+sum(
        abs(a)*exp_upper(k*ellipse_imaginary, 24) for k, a in MARKERS)
    assert analytic_event_bound < 10
    assert exp_upper(ellipse_radius, 18) < 2
    assert symbol_bound*F(2, 3) < INTEGRAND_BOUND
    epsilon = 4*T*INTEGRAND_BOUND*RHO**(-2*ORDER)/(1-1/RHO)
    n = 2*N+1
    first_f = F((T//2)**n, prod(range(1, 2*n, 2)))
    tail_f = first_f/(1-F((T//2)**2, (2*n+1)*(2*n+3)))
    assert N < 225 and SCALE < 4 and exp_upper(SCALE/4, 12) < 2
    first_h = 4*(SCALE/4)**n/prod(range(1, 2*n, 2))
    tail_h = first_h/(1-(SCALE/4)**2/((2*n+1)*(2*n+3)))
    tau_d = F(T*INTEGRAND_BOUND, 3)*tail_f**2+2*tail_h**2
    tau_b = F(T*INTEGRAND_BOUND, 3)*tail_f+2*tail_h
    assert tau_d < F(1, 10**54) and tau_b < F(1, 10**27)
    aperture = SCALE/2
    boundary_upper = aperture**3/(3*(1-aperture**2/20))
    assert boundary_upper < F(1, 4) and exp_upper(3*aperture, 24) < 13
    native_budget = 13+1+11+F(22, 5)+F(1, 4)
    assert native_budget == F(593, 20)
    return dict(pi=pi, log2=log2, mg=mg, log_pi=log_positive(pi), logs=logs,
                weights=weights, prime_sum=prime_sum, derivative=derivative,
                symbol_bound=symbol_bound, epsilon=epsilon, tail_f=tail_f,
                tail_h=tail_h, tau_d=tau_d, tau_b=tau_b,
                boundary_upper=boundary_upper, native_budget=native_budget,
                marker_norm=marker_norm, analytic_event_bound=analytic_event_bound)


def certify_tail(budget, progress=False):
    """Cover every point of the finite corridor, then all remaining frequencies."""
    far_gamma = gamma_symbol(I(F(TAIL_END)/SCALE), budget)
    assert far_gamma.lo > I(F(21, 4)).hi and F(21, 4)-F(22, 5)-budget['marker_norm'] > B
    far_floor = far_gamma-budget['prime_sum']-budget['marker_norm']
    assert far_floor.lo > I(B).hi
    cells, largest_depth, smallest, covered = 0, 0, None, F(0)
    digest = hashlib.sha256()
    def visit(left, right, depth):
        nonlocal cells, largest_depth, smallest, covered
        center, radius = (left+right)/2, (right-left)/2
        reading = marked_symbol(I(center), budget)
        lower = (reading-TAIL_LIPSCHITZ*radius).lo
        if lower > I(B).hi:
            cells += 1
            largest_depth = max(largest_depth, depth)
            smallest = lower if smallest is None else min(smallest, lower)
            covered += right-left
            digest.update(f'{left}|{right}|{lower}\n'.encode())
            return
        assert depth < 12, f'Uncertified tail cell {left},{right}'
        visit(left, center, depth+1)
        visit(center, right, depth+1)
    for block in range(T, TAIL_END):
        visit(F(block), F(block+1), 0)
        if progress and (block+1-T) % 512 == 0:
            print(f'recalibrated tail corridor {block+1}/{TAIL_END}', flush=True)
    assert covered == TAIL_END-T and smallest > I(B).hi
    return dict(corridor=[T, TAIL_END], lipschitz_upper='5', unit_blocks=TAIL_END-T,
                accepted_dyadic_cells=cells, maximum_depth=largest_depth,
                certified_minimum_lower=str(smallest), exact_covered_length=str(covered),
                partition_sha256=digest.hexdigest(), far_gamma_enclosure=far_gamma.record(),
                all_remaining_frequencies_floor=far_floor.record())


def assemble(budget, progress=False):
    roots = [sqrt_integer(2*n+1) for n in range(1, 2*N, 2)]
    poles = pole_coefficients(roots)
    nodes, weights = gauss24()
    matrix = [[0 for _ in range(i+1)] for i in range(N)]
    point_error = I(0)
    for panel in range(PANELS):
        for node, weight in zip(nodes, weights):
            t = F(2*panel+1, 4)+node/4
            symbol = marked_symbol(t, budget)-B
            vector = [root*j*((-1)**k)
                      for k, (root, j) in enumerate(zip(roots, odd_bessel(t/2)))]
            integer_weight, integers, error = node_error(weight*symbol/(4*budget['pi']), vector)
            point_error = point_error+error
            active = [(i, value) for i, value in enumerate(integers) if value]
            for position, (i, value) in enumerate(active):
                scaled, row = integer_weight*value, matrix[i]
                for j, other in active[:position+1]:
                    row[j] += scaled*other
        if progress and panel % 32 == 31:
            print(f'moving-calibration panels {panel+1}/{PANELS}', flush=True)
    enclosed = [[I(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            value = I(F(matrix[i][j], GRID**3))-2*SCALE*poles[i]*poles[j]
            if i == j:
                value = value+B
            enclosed[i][j] = enclosed[j][i] = value
    return enclosed, point_error


def _replay(progress=False, candidate_checkpoint=None):
    budget = budgets()
    witness_frequency = F(51819, 100)
    marked_reading = marked_symbol(I(witness_frequency), budget)
    unmarked_reading = marked_reading-marker_symbol(I(witness_frequency), budget)
    assert unmarked_reading.hi < I(B).lo < marked_reading.lo
    previous_marker_reading = unmarked_reading-cosine(I(witness_frequency), budget['pi'])/10
    assert previous_marker_reading.hi < 0
    tail = certify_tail(budget, progress)
    enclosed, point_error = assemble(budget, progress)
    candidate = [[CANDIDATE_CONTEXT.plus(value.midpoint()) for value in row]
                 for row in enclosed]
    radius = I(0)
    for row, midrow in zip(enclosed, candidate):
        total = sum((I((value-I(mid)).abs_upper()) for value, mid in zip(row, midrow)), I(0))
        radius = I(max(radius.hi, total.hi))
    error = point_error+radius+N*budget['epsilon']
    if candidate_checkpoint is not None:
        Path(candidate_checkpoint).write_text(json.dumps(dict(
            status='UNCERTIFIED_CANDIDATE_ONLY',
            matrix=[[str(x) for x in row] for row in candidate],
            total_head_error_upper=str(error.hi)), indent=2)+'\n', encoding='utf-8')
    shift, leading_floor, q = F(3, 10**20), F(2, 10**20), F(1, 10**20)
    assert error.hi < I(shift-leading_floor).lo
    pivots = interval_ldl(candidate, shift)
    assert min(leading_floor, B-budget['tau_d'])-budget['tau_b'] > q
    native = q/(q+budget['native_budget'])
    def rat(x):
        return f'{x.numerator}/{x.denominator}'
    archive = dict(schema='rkf.endpoint-moving-calibration-matrix.v1',
                   reference_aperture='1/2', physical_aperture='21/25', scale='42/25',
                   active_prime_powers=[2, 3, 4, 5], support_zero_marker='-cos(t)/3+cos(2t)/9-cos(3t)/8',
                   candidate_significant_digits=40,
                   basis='L2-normalized odd Legendre orders 1,3,...,415 on [-1/2,1/2]',
                   matrix=[[str(x) for x in row] for row in candidate])
    encoded = json.dumps(archive, indent=2)+'\n'
    result = dict(
        schema='rkf.endpoint-moving-calibration-certificate.v1', date='2026-10-12', status='PASS',
        arithmetic='90-digit outward Decimal; exact 240-place normalized Bessel intervals; exact signed-Gram sums',
        scale=rat(SCALE), physical_aperture='21/25', reference_aperture='1/2',
        active_latest_prime_event=5, next_event='log(7)', active_prime_powers=[2, 3, 4, 5],
        prime5_event_enclosure=budget['logs'][3].record(),
        support_zero_markers=[dict(shift=str(k), coefficient=rat(a), full_quadratic_form='exactly zero') for k, a in MARKERS],
        total_marker_norm_upper=rat(budget['marker_norm']),
        high_frequency_floor=rat(B), frequency_split=T, tail_certificate=tail,
        marker_recalibration=dict(frequency=rat(witness_frequency),
            unmarked_symbol=unmarked_reading.record(), marked_symbol=marked_reading.record(),
            previous_marker_symbol=previous_marker_reading.record()),
        prime_weight_sum_enclosure=budget['prime_sum'].record(),
        gamma_ground_enclosure=budget['mg'].record(),
        matrix_dimension=N, quadrature_order=ORDER, panels=PANELS,
        ellipse_parameter=rat(RHO), analytic_integrand_bound=INTEGRAND_BOUND,
        analytic_symbol_bound=rat(budget['symbol_bound']), quadrature_error_per_entry=rat(budget['epsilon']),
        gamma_shift=128, gamma_complex_remainder='abs(B12)/(12*(513/4)^12)',
        bessel_correction_terms=BESSEL_TERMS, normalized_bessel_fixed_places=240,
        signed_gram_point_operator_error_upper=str(point_error.hi),
        final_candidate_and_pole_norm_error_upper=str(radius.hi),
        total_leading_matrix_error_upper=str(error.hi),
        ldl_shift=rat(shift), positive_ldl_pivots=len(pivots),
        ldl_arithmetic_precision=LDL_PRECISION,
        ldl_pivot_enclosures=[p.record() for p in pivots], exact_leading_matrix_floor=rat(leading_floor),
        first_discarded_odd_order=2*N+1, tail_deviation_upper=rat(budget['tau_d']),
        tail_coupling_upper=rat(budget['tau_b']), physical_source_floor=rat(q),
        native_graph_budget=rat(budget['native_budget']), native_source_floor=rat(native),
        relative_joint_reserve=rat(2*native/11), all_smaller_apertures_by_native_inclusion=True,
        comparison_negative_index=0, full_source_aperture_negative_index=0,
        full_source_aperture_nullity=0,
        matrix_sha256=hashlib.sha256(encoded.encode()).hexdigest(),
        not_certified=['cofinal aperture exhaustion or global observer limit certified by this finite run', 'prime-7 crossing',
                       'cofinal all-scale source signs', 'global eta=0 sign',
                       'historical five-label endpoint or K0', 'RH',
                       'proof-assistant verification or external review'])
    return result, encoded


def replay(progress=False, candidate_checkpoint=None):
    with localcontext() as context:
        context.prec = 90
        return _replay(progress, candidate_checkpoint)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    parser.add_argument('--candidate-checkpoint', help='Optional diagnostic proposal; never accepted as a certificate')
    args = parser.parse_args()
    result, matrix = replay(progress=True, candidate_checkpoint=args.candidate_checkpoint)
    if args.write:
        MATRIX.write_text(matrix, encoding='utf-8')
        RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    if args.check:
        if MATRIX.read_text(encoding='utf-8') != matrix or json.loads(RESULT.read_text()) != result:
            raise SystemExit('SE14 replay mismatch: inspect changes instead of repinning.')
    keys = ['status', 'scale', 'physical_aperture', 'active_latest_prime_event', 'positive_ldl_pivots',
            'total_leading_matrix_error_upper', 'physical_source_floor',
            'native_source_floor', 'relative_joint_reserve', 'matrix_sha256']
    print(json.dumps({key: result[key] for key in keys}, indent=2))


if __name__ == '__main__':
    main()
