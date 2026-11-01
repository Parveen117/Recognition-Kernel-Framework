"""Independent controls for SE24's three-weight certificate with an exact pole row."""
from fractions import Fraction as F
from decimal import localcontext
import itertools
from math import isqrt
import unittest

from proof_lab.endpoint_full_aperture_certificate import I, log_positive
from proof_lab.endpoint_signed_return_certificate import MG_CAP, POLE_CAP, prime_catalogue
from proof_lab.endpoint_three_weight_certificate import (
    ETA, FLOOR, GAMMA_CONSTANT, GAMMA_WEIGHT, POLE_PAIRING, POLE_WEIGHT, PRIME_WEIGHT,
    UncertifiedCell, comparison_cell, extend_catalogue, gamma_lower, gamma_numerator, pole_budget,
    pole_pairing, pole_upper, poly_eval, prime_upper, row_lower, row_upper, se17_cut_point_control,
    weight_lower_slope, weight_polynomial,
)


def finite_catalogue():
    """Independent rational catalogue at three square prime-power positions, all exponents."""
    limit = 64
    entries = {4: F(1), 16: F(2), 64: F(3)}
    weights = [I(entries.get(n, 0)) for n in range(limit+1)]
    prefix, suffix, peaks = [], [], []
    for n in range(limit+1):
        prefix.append(I(sum((w*j*isqrt(j) for j, w in entries.items() if j <= n), F(0))))
        suffix.append(I(sum((w/F(j*j*isqrt(j)) for j, w in entries.items() if j > n), F(0))))
        peaks.append(I(entries.get(n, F(0))/F(n*isqrt(n)) if n in entries else 0))
    cat = dict(limit=limit, prefix=prefix, suffix=suffix, peaks=peaks, weights=weights,
               mass=suffix[0], tail=I(0), log_limit=log_positive(limit))
    cat = extend_catalogue(cat)
    for k in cat['rows']:
        cat['rows'][k]['tail'] = I(0)
        cat['rows'][k]['mass'] = cat['rows'][k]['suffix'][0]
        cat['rows'][k]['mass_lower'] = cat['rows'][k]['suffix'][0].lo
    return cat, entries


class ThreeWeightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = localcontext()
        cls.ctx = cls.context.__enter__()
        cls.ctx.prec = 90
        cls.cat = extend_catalogue(prime_catalogue(4096))   # local controls only; the exterior split needs 512^2

    @classmethod
    def tearDownClass(cls):
        cls.context.__exit__(None, None, None)

    def test_pole_pairing_against_direct_exponential_integrals(self):
        # <v, e^{-kx/2}> with v=(e^{-x}-e^{-2x})/2: (1/2)[1/(k/2+1)-1/(k/2+2)] = 1/(k+2)-1/(k+4).
        for k in (1, 3, 5, 7):
            self.assertEqual(pole_pairing(((F(1), k),)), F(1, k+2)-F(1, k+4))
        self.assertEqual(POLE_PAIRING, F(2, 15)+F(1, 4)*(F(1, 5)-F(1, 7)))

    def test_pole_budget_law_saturated_and_violations_detected(self):
        self.assertEqual(pole_budget(), 1)
        self.assertGreater(pole_budget(scale=F(1, 2)), 1)      # halving the density breaks 4 int v^2/tau <= 1
        self.assertLess(pole_budget(scale=F(2)), 1)            # doubling it wastes budget but stays admissible
        with self.assertRaises(ValueError):
            pole_budget(((F(-1), 1),))

    def test_pole_row_matches_rank_one_cauchy_schwarz_at_sample_points(self):
        # tau_q(z)=4 v(x)<v,q>/q(x) with v=(z^2-z^4)/2, q=z+z^3/4: at z=1/2, 2(1/4-1/16)(31/210)/(1/2+1/32).
        self.assertEqual(pole_upper(F(1, 2)), 2*(F(1, 4)-F(1, 16))*F(31, 210)/(F(1, 2)+F(1, 32)))
        self.assertEqual(pole_upper(F(0)), 0)
        self.assertEqual(pole_upper(F(1)), 0)
        # SE18.8: with q_F=z the row is (4/15)(z-z^3).
        pairing_q0 = pole_pairing(((F(1), 1),))
        z = F(1, 3)
        self.assertEqual(2*(z**2-z**4)*pairing_q0/z, F(4, 15)*(z-z**3))

    def test_gamma_numerator_against_separately_integrated_exponentials(self):
        # For weight sum_j g_j e^{-s_j x}, a_j=s_j+3/2, each mode integrates to c(z^{2beta}-z^{2a}).
        for modes, z in itertools.product((1, 2, 4, 16), (F(1, 2), F(1, 4), F(3, 4))):
            row = F(0)
            for k in range(modes):
                beta = F(4*k+1, 2)
                for g, kz in GAMMA_WEIGHT:
                    a = F(kz, 2)+F(3, 2)
                    eb, ea = z**int(2*beta), z**int(2*a)
                    left = (eb-ea)/(a-beta)
                    right = ea/(a+beta)
                    reflected = eb/(a+beta)
                    row += g*(left+right-reflected)
            q = poly_eval(weight_polynomial(GAMMA_WEIGHT), z)
            expected = (sum((F(4, 4*k+1) for k in range(modes)), F(0))-MG_CAP)*z**6-z**3*row/q
            numerator = gamma_numerator(GAMMA_WEIGHT, modes)
            self.assertEqual((sum((F(4, 4*k+1) for k in range(modes)), F(0))-MG_CAP)*z**6-z**3*poly_eval(numerator, z)/q, expected)

    def test_gamma_row_vanishes_at_the_cut_point_for_a_nonvanishing_weight(self):
        # The odd reflected kernel is zero at x=0, so L_Gamma(1)=C_16-g_c when q_Gamma(0)>0.
        self.assertEqual(gamma_lower(F(1)), GAMMA_CONSTANT-MG_CAP)

    def test_rows_against_direct_translated_positive_weight(self):
        # Each event: the -log n translate gives min(n^{(k+2)/2} z^{k+6}, n^{-(k+4)/2} z^{-k}); the +log n
        # translate gives the constant n^{-(k+4)/2} times z^{k+6} (SE17.8). n is a perfect square here.
        cat, entries = finite_catalogue()
        for k in (1, 3, 5, 7):
            for z in (F(1, 8), F(1, 5), F(1, 3), F(1, 2), F(7, 8)):
                direct = F(0)
                for n, w in entries.items():
                    root = F(isqrt(n))
                    direct += w*(min(root**(k+2)*z**(k+6), 1/(root**(k+4)*z**k))+z**(k+6)/root**(k+4))
                upper = row_upper(z, z, cat, k)
                lower = row_lower(z, z, cat, k)
                self.assertLessEqual(I(lower).lo, I(direct).hi)
                self.assertGreaterEqual(upper.hi, I(direct).lo)

    def test_higher_rows_never_exceed_the_base_row(self):
        # W_k <= W_1 on (0,1] for k>=1 (SE24 lemma used for the exterior).
        for z in (F(1, 50), F(1, 8), F(1, 3), F(2, 3), F(1)):
            base = row_upper(z, z, self.cat, 1).hi
            for k in (3, 5, 7):
                self.assertLessEqual(row_lower(z, z, self.cat, k), base)

    def test_weight_positivity_slopes(self):
        self.assertEqual(weight_lower_slope(GAMMA_WEIGHT), F(9, 10))
        self.assertEqual(weight_lower_slope(POLE_WEIGHT), 1)
        with self.assertRaises(ValueError):
            weight_lower_slope(PRIME_WEIGHT)                       # not provable by the z-term on all of (0,1]
        self.assertGreater(weight_lower_slope(PRIME_WEIGHT, F(1, 512)), F(1, 13))
        # On the interior the cells certify positivity themselves; a cell too wide is refused, not accepted.
        with self.assertRaises(UncertifiedCell):
            prime_upper(F(1, 64), F(1), self.cat)

    def test_prime_shape_against_direct_translated_weight_at_a_point(self):
        # At z=1 every row equals 2 p_{(k+4)/2}; V_P(1) = sum c_k 2p / q_P(1).
        num = sum((c*2*self.cat['rows'][k]['mass'] for c, k in PRIME_WEIGHT), I(0))
        q1 = poly_eval(weight_polynomial(PRIME_WEIGHT), F(1))
        self.assertEqual(q1, F(1, 12))
        enclosure = prime_upper(F(1), F(1), self.cat)
        self.assertLessEqual((I(enclosure.lo)*I(F(999, 1000))).lo, (num/q1).hi)
        self.assertGreaterEqual(enclosure.hi, (num/q1).lo)

    def test_planted_lower_anchor_fails_at_the_binding_cell(self):
        # SE24 certifies 14/25. Bisect near x=0.325 until a cell passes at 14/25; the same cell fails at 11/20.
        left, right = F(217, 256), F(218, 256)
        for _ in range(14):
            try:
                if F(comparison_cell(left, right, self.cat, ETA).lo) >= FLOOR:
                    break
            except UncertifiedCell:
                pass
            right = (left+right)/2
        self.assertGreaterEqual(F(comparison_cell(left, right, self.cat, ETA).lo), FLOOR)
        self.assertLess(F(comparison_cell(left, right, self.cat, F(11, 20)).lo), FLOOR)

    def test_se17_weights_fail_at_the_cut_point_at_this_eta(self):
        control = se17_cut_point_control(self.cat, ETA)
        self.assertLess(control.hi, 0)
        self.assertGreater(se17_cut_point_control(self.cat, F(59, 100)).lo, 0)

    def test_constant_pole_bound_has_the_exterior_floor(self):
        # SE18 Theorem 2: with the constant pole bound the exterior value is eta-b_c; the row gives eta.
        self.assertEqual(ETA-POLE_CAP, F(14, 25)-F(1, 10))
        self.assertEqual(pole_upper(F(0)), 0)

    def test_native_shift_uses_the_graph_conversion(self):
        self.assertEqual(FLOOR/(2+MG_CAP), F(1, 7380))


if __name__ == '__main__':
    unittest.main()
