"""SE11: a certified failure of the T=256 lower comparison before prime 5.

This is not a negative full-source witness. A support-invisible prime changes
the finite-band reading, but its modified comparison has no certified tail.
"""
from __future__ import annotations

import argparse
from decimal import localcontext
from fractions import Fraction as F
import json
from pathlib import Path

try:
    from proof_lab.endpoint_precision_frontier_certificate import (
        I, B, N, T, GAMMA_TERMS, gauss24, gamma_symbol, odd_bessel,
        pole_coefficients, refined_constants, hurwitz_power, sqrt_integer,
        log_positive, cosine, exp_upper,
    )
except ModuleNotFoundError:
    from endpoint_precision_frontier_certificate import (
        I, B, N, T, GAMMA_TERMS, gauss24, gamma_symbol, odd_bessel,
        pole_coefficients, refined_constants, hurwitz_power, sqrt_integer,
        log_positive, cosine, exp_upper,
    )

SCALE = F(8047, 5000)
RESULT = Path(__file__).with_name('ENDPOINT_CUTOFF_OBSTRUCTION_RESULT.json')
COEFFICIENTS = [
    '0.546187410393', '0.247528700041', '-0.361393055325', '-0.427619294080',
    '0.212507655294', '0.373577780532', '-0.349098677830', '0.134379293716',
    '-0.026002037648', '0.029631881487', '-0.011695136050', '0.020511654944',
    '0.000323718217', '0.009901773091', '0.002949399051', '0.003229988034',
    '0.001405214696', '-0.001695211686', '-0.002752846585', '-0.003574561520',
    '-0.002586682997', '-0.002372029562', '-0.000882612681', '0.002431903143',
    '0.001782729406', '0.002822997278', '0.000729404442', '-0.000422751116',
    '-0.001396681848', '-0.002953686802', '-0.001365235256', '-0.000747832746',
]


def _replay(progress=False):
    pi, log2, mg = refined_constants()
    log3, log5 = log_positive(3), log_positive(5)
    assert (2*log2).hi < I(SCALE).lo < log5.lo
    logs = [log2, log3, 2*log2]
    weights = [sqrt_integer(2)*log2, 2*log3/sqrt_integer(3), log2]
    weight5 = 2*log5/sqrt_integer(5)
    assert sum(weights, I(0)).hi < I(F(59, 20)).lo
    assert (sum(weights, I(0))+weight5).hi < I(F(22, 5)).lo
    y = F(T, 2)/SCALE
    gamma_lower = sum((y*y/(F(4*k+1, 4)*(F(4*k+1, 4)**2+y*y))
                       for k in range(512)), F(0))-F(269, 50)
    assert gamma_lower > F(16, 5) and F(16, 5)-F(59, 20) > B
    # Width-one panels, rho=2: semimajor 5/8, semiminor 3/8.
    assert F(3, 8)/SCALE < F(1, 4)
    beta = F(1201, 2)
    symbol_bound = (F(269, 50)
        +10*sum((1/F(4*k+1, 2) for k in range(300)), F(0))
        +F(8, 3)*(T+1)**2*(beta**-3+F(1, 4)*beta**-2)+9+B)
    assert symbol_bound < 100 and (F(3, 8)*log5/SCALE).hi < I(F(1, 2)).lo
    assert exp_upper(F(1, 2), 16) < 2 and exp_upper(F(3, 8), 16) < 2
    coefficients = [F(x) for x in COEFFICIENTS]
    norm = sum((x*x for x in coefficients), F(0))
    assert F(99, 100) < norm < F(101, 100) < 2
    assert 100*F(4, 3) < 256  # |g-hat|^2 <= norm*exp(3/8)<4; pi>3.
    epsilon = F(4*T*256)*F(1, 2)**48/(1-F(1, 2))
    roots = [sqrt_integer(2*n+1) for n in range(1, 2*N, 2)]
    poles = pole_coefficients(roots, SCALE)
    pole = sum((a*q for a, q in zip(coefficients, poles)), I(0))
    zeta = [hurwitz_power(2*r+1) for r in range(1, GAMMA_TERMS+2)]
    nodes, quadrature_weights = gauss24()
    old, extra = I(0), I(0)
    for panel in range(T):
        for node, weight in zip(nodes, quadrature_weights):
            t = F(2*panel+1, 2)+node/2
            physical_t = t/SCALE
            symbol = gamma_symbol(physical_t, mg, zeta)-B
            for logn, prime_weight in zip(logs, weights):
                symbol = symbol-prime_weight*cosine(physical_t*logn, pi)
            bessel = odd_bessel(t/2)
            value = sum((a*root*j*((-1)**k)
                         for k, (a, root, j) in enumerate(zip(coefficients, roots, bessel))), I(0))
            measure = weight*value*value/(2*pi)
            old = old+measure*symbol
            extra = extra-measure*weight5*cosine(physical_t*log5, pi)
        if progress and panel % 64 == 63:
            print(f'cutoff-witness panels {panel+1}/{T}', flush=True)
    base = B*norm-2*SCALE*pole*pole
    old_reading = base+old+I(-epsilon, epsilon)
    modified_reading = base+old+extra+I(-epsilon, epsilon)
    assert old_reading.hi < I(F(-3, 100000)).lo
    assert modified_reading.lo > I(F(1, 10000)).hi
    quotient = old_reading/norm
    assert quotient.hi < I(F(-3, 100000)).lo
    return dict(
        schema='rkf.endpoint-cutoff-obstruction.v1', date='2026-10-12', status='PASS',
        scale='8047/5000', physical_aperture='8047/10000',
        frequency_split=T, high_frequency_floor='1/10', active_catalogue=[2, 3, 4],
        inactive_prime=5, inactive_shift_enclosure=(log5/SCALE).record(),
        witness_basis='first 32 L2-normalized odd Legendre modes on [-1/2,1/2]',
        witness_coefficients=COEFFICIENTS, witness_norm_squared=str(norm),
        valid_original_comparison_rayleigh_enclosure=quotient.record(),
        original_comparison_reading=old_reading.record(),
        dormant_prime_modified_reading=modified_reading.record(),
        quadrature_order=24, panels=T, ellipse_parameter='2',
        analytic_integrand_bound=256, analytic_symbol_bound=str(symbol_bound),
        quadrature_error_per_reading=str(epsilon),
        finite_gamma_lower_at_split_enclosure=I(gamma_lower).record(),
        conclusion='At this scale, T=256 with catalogue {2,3,4} fails regardless of mode or precision refinement.',
        modified_comparison_scope='Only this trial reading is positive. Its high-frequency minorant condition is not certified.',
        not_certified=['a negative full-source value', 'positivity of the modified comparison',
                       'prime-5 crossing', 'global eta=0 source sign', 'RH'])


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
    result = replay(progress=True)
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    if args.check and json.loads(RESULT.read_text()) != result:
        raise SystemExit('SE11 cutoff witness replay mismatch; do not repin.')
    print(json.dumps({k: result[k] for k in ['status', 'scale',
          'valid_original_comparison_rayleigh_enclosure', 'dormant_prime_modified_reading']}, indent=2))


if __name__ == '__main__':
    main()
