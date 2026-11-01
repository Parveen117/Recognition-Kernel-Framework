"""Independent controls for SE13's recalibrated aperture certificate."""
import itertools
import unittest
from decimal import localcontext
from fractions import Fraction as F
from math import factorial

from proof_lab.endpoint_full_aperture_certificate import I, cosine
from proof_lab.endpoint_aperture_convergence_certificate import (
    B, FIXED_GRID, SCALE, _fixed, _fadd, _fneg, _fmul, _fdivint,
    budgets, gamma_symbol, marked_symbol, odd_bessel, interval_ldl,
)
from proof_lab.test_endpoint_precision_frontier_certificate import shifted_gamma


def trig_control(z, terms=900):
    """Exact rational Taylor sums and alternating remainders, no Decimal trig."""
    sine = sum(((-1)**k*z**(2*k+1)/factorial(2*k+1)
                for k in range(terms)), F(0))
    cosine_ = sum(((-1)**k*z**(2*k)/factorial(2*k)
                   for k in range(terms)), F(0))
    return (sine, cosine_, z**(2*terms+1)/F(factorial(2*terms+1)),
            z**(2*terms)/F(factorial(2*terms)))


class ApertureConvergenceTests(unittest.TestCase):
    def test_refined_ldl_against_exact_nearly_singular_rank_one_pivots(self):
        epsilon = F(1, 10**45)
        vector = list(range(1, 13))
        matrix = [[F(a*b)+(epsilon if i == j else 0)
                   for j, b in enumerate(vector)] for i, a in enumerate(vector)]
        shift = epsilon/2
        pivots = interval_ldl(matrix, shift)
        diagonal, norm_squared = epsilon-shift, F(0)
        for i, (pivot, value) in enumerate(zip(pivots, vector)):
            exact = diagonal+value*value if i == 0 else diagonal*(diagonal+norm_squared+value*value)/(diagonal+norm_squared)
            self.assertLessEqual(F(pivot.lo), exact)
            self.assertGreaterEqual(F(pivot.hi), exact)
            self.assertGreater(pivot.lo, 0)
            norm_squared += value*value
        with self.assertRaises(AssertionError):
            interval_ldl(matrix, 2*epsilon)

    def test_fixed_integer_intervals_enclose_signed_rational_arithmetic(self):
        values = [F(-1234567, 13), F(-1, 10**260), F(0), F(1, 7), F(193)]
        def encloses(interval, value):
            self.assertLessEqual(F(interval[0], FIXED_GRID), value)
            self.assertGreaterEqual(F(interval[1], FIXED_GRID), value)
        for a in values:
            encloses(_fixed(a), a)
            encloses(_fneg(_fixed(a)), -a)
            encloses(_fdivint(_fixed(a), 37), a/37)
        for a, b in itertools.product(values, repeat=2):
            encloses(_fadd(_fixed(a), _fixed(b)), a+b)
            encloses(_fmul(_fixed(a), _fixed(b)), a*b)

    def test_gamma_encloses_independent_large_shift_through_far_tail(self):
        with localcontext() as context:
            context.prec = 90
            budget = budgets()
            for t in [F(0), F(32), F(512)/SCALE, F(78769, 100)/SCALE, F(2048)/SCALE]:
                actual = gamma_symbol(I(t), budget)
                control = shifted_gamma(t, budget['pi'], budget['log2'])
                self.assertLessEqual(actual.lo, control.lo, str(t))
                self.assertGreaterEqual(actual.hi, control.hi, str(t))
                self.assertLess(F(actual.hi)-F(actual.lo), F(3, 10**27))

    def test_normalized_bessel_against_low_order_trigonometric_formulas(self):
        with localcontext() as context:
            context.prec = 90
            for z in [F(1, 64), F(1), F(128), F(256)]:
                sine, cosine_, sine_error, cosine_error = trig_control(z, 600)
                got = odd_bessel(I(z))
                for index, (s, c) in enumerate([
                    (1/z**2, -1/z), (15/z**4-6/z**2, 1/z-15/z**3),
                ]):
                    expected = s*sine+c*cosine_
                    error = abs(s)*sine_error+abs(c)*cosine_error
                    self.assertLessEqual(F(got[index].lo), expected+error)
                    self.assertGreaterEqual(F(got[index].hi), expected-error)
                    self.assertLess(F(got[index].hi)-F(got[index].lo), F(1, 10**80))
            # A deliberately wide node interval exercises the independent
            # derivative enclosure, rather than only point recurrence.
            radius = F(1, 10**8)
            wide = odd_bessel(I(1-radius, 1+radius))[0]
            for z in [1-radius, 1+radius]:
                sine, cosine_, se, ce = trig_control(z, 50)
                expected, error = sine/z**2-cosine_/z, se/z**2+ce/z
                self.assertLessEqual(F(wide.lo), expected-error)
                self.assertGreaterEqual(F(wide.hi), expected+error)

    def test_all_retained_bessel_orders_against_odd_parseval_identity(self):
        with localcontext() as context:
            context.prec = 90
            tail_squared = budgets()['tail_f']**2
            for z in [F(1), F(128), F(256)]:
                readings = odd_bessel(I(z))
                head = sum(((4*k+3)*v*v for k, v in enumerate(readings)), I(0))
                sine, _, error, _ = trig_control(2*z, 1100)
                exact, radius = (1-sine/(2*z))/2, error/(4*z)
                self.assertLessEqual(F(head.lo), exact+radius)
                self.assertGreaterEqual(F(head.hi)+tail_squared, exact-radius)
                self.assertLess(F(head.hi)-F(head.lo), F(1, 10**75))

    def test_previous_marker_fails_and_recalibration_recovers_selected_cap(self):
        with localcontext() as context:
            context.prec = 90
            budget = budgets()
            t = I(F(78769, 100))
            marked = marked_symbol(t, budget)
            unmarked = marked+cosine(t, budget['pi'])/10
            previous = unmarked+cosine(t, budget['pi'])
            self.assertLess(unmarked.hi, I(B).lo)
            self.assertLess(previous.hi, 0)
            self.assertGreater(marked.lo, I(B).hi)
            self.assertGreater(t.lo, 512)
            self.assertLess(budget['logs'][-1].hi, I(SCALE).lo)


if __name__ == '__main__':
    unittest.main()
