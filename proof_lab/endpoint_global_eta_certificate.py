"""SE15: a global positive-eta certificate and effective aperture obligations.

The global eta bound is proved for the complete corrected odd source.
Smaller-eta rows are conditional local obligations, not executed source signs.
Only standard-library arithmetic and immutable earlier interval routines are used.
"""
from __future__ import annotations

import argparse
from decimal import localcontext
from fractions import Fraction as F
import json
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import I, log_positive
    from proof_lab.endpoint_precision_frontier_certificate import refined_constants
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I, log_positive
    from endpoint_precision_frontier_certificate import refined_constants

RESULT = Path(__file__).with_name('ENDPOINT_GLOBAL_ETA_RESULT.json')
MG_CAP, PRIME_CAP, BOUNDARY_CAP = F(269, 50), F(57, 100), F(1, 10)
ETA = (MG_CAP+2*PRIME_CAP)/(MG_CAP+2)
SERIES_TERMS = 1024


def rational(x):
    x = F(x)
    return f'{x.numerator}/{x.denominator}'


def integer_log(n, log2):
    """Binary reduction keeps the inherited positive-log series well conditioned."""
    if not isinstance(n, int) or n < 1:
        raise ValueError('A positive integer is required')
    exponent = n.bit_length()-1
    return exponent*log2+log_positive(F(n, 2**exponent))


def prime_mass_enclosure(count=SERIES_TERMS):
    """Enclose sum Lambda(n)/n^2 by two complete alternating Dirichlet series.

    E=sum (-1)^(n-1)/n^2 and D=sum (-1)^(n-1)*log(n)/n^2.
    Absolute convergence at s=2 and the Euler product give p=log(2)+D/E.
    For an even cutoff both omitted alternating tails are nonnegative.
    """
    if count < 2 or count % 2:
        raise ValueError('An even cutoff at least two is required')
    log2 = log_positive(2)
    e = sum((F((-1)**(n-1), n*n) for n in range(1, count+1)), F(0))
    d = I(0)
    for n in range(2, count+1):
        d = d+F((-1)**(n-1), n*n)*integer_log(n, log2)
    e_box = I(e, e+F(1, (count+1)**2))
    d_tail = integer_log(count+1, log2)/(count+1)**2
    d_box = d+I(0, d_tail.hi)
    assert e_box.lo > 0
    return dict(mass=log2+d_box/e_box, denominator=e_box,
                logarithmic_sum=d_box, log2=log2)


def localization_budget(m, logm):
    """Whole-source upper budgets for R=log(m), transition width one.

    Every expression is a rational outward enclosure once log(m) is enclosed.
    The signed localization identity and geometric support bounds are proved
    in SE15; these scalars never stand in for the local sign obligation.
    """
    if not isinstance(m, int) or m < 2:
        raise ValueError('An integer m >= 2 is required')
    gamma = I(F(41, m*m)+F(1, m-1))
    prime = (3*logm+2)/m+logm/(m*m)
    boundary = I(F(1, 2*m)+F(1, 2*m*m))
    error = gamma+prime+boundary
    exterior = I((MG_CAP+2*PRIME_CAP)/m**3)+(4*logm+F(5, 2))/m**2
    total = error+exterior
    return dict(gamma=gamma, prime=prime, boundary=boundary,
                error=error, exterior=exterior, zero_local_total=total)


def obligation(target, log2):
    """Choose a rational aperture and local tolerance for a desired global eta.

    This returns an obligation only. No local certificate for it is asserted.
    """
    target = F(target)
    if target <= 0:
        raise ValueError('The target eta must be positive')
    k = 1
    # A written all-k majorant provides an entirely rational stopping rule.
    while F(4*k+29, 2**k) > target/2:
        k += 1
    m, local_tolerance = 2**k, target/2
    budget = localization_budget(m, k*log2)
    exterior_upper = F(budget['exterior'].hi)
    total_upper = F(budget['error'].hi)+max(local_tolerance, exterior_upper)
    assert total_upper <= target
    return dict(status='CONDITIONAL_LOCAL_OBLIGATION', target_eta=rational(target),
                m=m, logarithmic_inner_radius=(k*log2).record(),
                aperture_radius=rational(1+F(7*k, 10)),
                required_physical_source_lower_floor=rational(-local_tolerance),
                local_certificate_executed=False,
                localization_error_upper=str(budget['error'].hi),
                exterior_negative_allowance_upper=str(budget['exterior'].hi),
                conditional_global_allowance_upper=rational(total_upper),
                rational_schedule_majorant=rational(F(4*k+29, 2**k)))


def _replay():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name, status='PASS'))

    pi, log2, mg = refined_constants()
    mass = prime_mass_enclosure()
    beta = log_positive(3)-1
    check('complete_prime_mass_positive', mass['mass'].lo > 0)
    check('complete_prime_mass_below_57_over_100', mass['mass'].hi < I(PRIME_CAP).lo)
    check('gamma_ground_below_269_over_50', mg.hi < I(MG_CAP).lo)
    check('exact_weighted_boundary_constant_below_one_tenth', 0 < beta.lo and beta.hi < I(BOUNDARY_CAP).lo)
    check('global_eta_exact_value', ETA == F(326, 369))
    check('global_polynomial_endpoint_matches', 2*ETA-(1-ETA)*MG_CAP-2*PRIME_CAP == 0)
    reserve = ETA-PRIME_CAP-BOUNDARY_CAP
    check('remaining_weighted_reserve_positive', reserve > 0)
    check('shift_below_one', ETA < 1)

    # Integrate the geometric Gamma kernel termwise. The decreasing remainder
    # after k=1 is bounded by the integral beginning at one.
    gamma_second_moment = F(16)+F(16, 125)+F(2, 25)
    check('gamma_jump_second_moment_below_seventeen', gamma_second_moment < 17)
    check('pi_bound_for_transition', pi.hi < I(F(22, 7)).lo)
    check('gamma_localization_integer_coefficient', gamma_second_moment*F(121, 49) < 41)
    check('boundary_unweighted_norm', F(1, 2)-F(2, 3)+F(1, 4) == F(1, 12))
    check('boundary_square_root_majorant', F(1, 6) < F(1, 4))
    check('log_two_rational_radius_majorant', log2.hi < I(F(7, 10)).lo)
    check('outer_source_coefficient', MG_CAP+2*PRIME_CAP == F(163, 25))

    budgets = []
    for k in (1, 2, 4, 5, 6, 8, 10, 16, 24):
        m = 2**k
        b = localization_budget(m, k*log2)
        direct = (I(F(163, 25*m**3))+(44+5*k*log2)/m**2
                  +(3*k*log2+F(5, 2))/m+F(1, m-1))
        check(f'combined_localization_identity_k_{k}',
              b['zero_local_total'].lo <= direct.hi and direct.lo <= b['zero_local_total'].hi)
        check(f'all_k_rational_majorant_at_k_{k}', b['zero_local_total'].hi < I(F(4*k+29, m)).lo)
        budgets.append(dict(m=m, inner_radius=(k*log2).record(),
                            zero_local_global_allowance=b['zero_local_total'].record(),
                            status='BUDGET_ONLY_LOCAL_SIGN_NOT_EVALUATED'))

    schedule = [obligation(x, log2) for x in (F(1, 2), F(1, 4), F(1, 10), F(1, 100), F(1, 1000))]
    for row in schedule:
        check('scheduled_budget_eta_'+row['target_eta'],
              F(row['conditional_global_allowance_upper']) <= F(row['target_eta']))
    check('no_scheduled_local_sign_promotion', all(not row['local_certificate_executed'] for row in schedule))

    return dict(schema='rkf.endpoint-global-eta-certificate.v1', date='2026-10-12',
                status='PASS_GLOBAL_POSITIVE_ETA_AND_LOCALIZATION_BUDGETS',
                arithmetic='90-digit outward Decimal intervals and exact Fraction inequalities',
                check_count=len(checks), checks=checks,
                global_source=dict(eta=rational(ETA), invariant_negative_count=0,
                    nullity=0, scope='Entire corrected complex odd native source; every eta >= the certified threshold',
                    lower_bound='S_b >= -(326/369) I_X',
                    remaining_weighted_reserve=rational(reserve),
                    weighted_reserve_operator='iota-dagger M_(1-exp(-3*abs(x))) iota',
                    eta_zero_certified=False),
                gamma_ground_enclosure=mg.record(),
                prime_mass=dict(method='Absolutely convergent Euler/alternating Dirichlet identity at s=2',
                    terms=SERIES_TERMS, complete_enclosure=mass['mass'].record(),
                    alternating_denominator=mass['denominator'].record(),
                    alternating_logarithmic_sum=mass['logarithmic_sum'].record(),
                    rational_upper=rational(PRIME_CAP)),
                weighted_boundary=dict(exact_constant='log(3)-1', enclosure=beta.record(),
                    rational_upper=rational(BOUNDARY_CAP)),
                localization=dict(transition_width='1', gamma_coefficient='41',
                    all_prime_and_boundary_tails_included=True,
                    gamma_second_moment_upper=rational(gamma_second_moment), budgets=budgets),
                smaller_eta_schedule=schedule,
                prior_local_frontier=dict(radius='21/25', stage='SE14', unchanged=True),
                not_certified=['any smaller eta in the conditional schedule', 'new larger-aperture source sign',
                    'cofinal eta-zero limit', 'global contractive observer', 'historical five-label endpoint or K0',
                    'RH', 'formal proof-assistant verification or external review'])


def replay():
    with localcontext() as context:
        context.prec = 90
        return _replay()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = replay()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    if args.check and json.loads(RESULT.read_text()) != result:
        raise SystemExit('SE15 replay mismatch: inspect changes instead of repinning.')
    print(json.dumps({key: result[key] for key in ('status', 'check_count', 'global_source')}, indent=2))


if __name__ == '__main__':
    main()
