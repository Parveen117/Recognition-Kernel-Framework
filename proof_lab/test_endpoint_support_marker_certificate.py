"""Independent controls for SE12's support-calibrated full-tail certificate."""
import itertools
import unittest
from decimal import localcontext
from fractions import Fraction as F
from math import factorial

from proof_lab.endpoint_full_aperture_certificate import I, cosine
from proof_lab.endpoint_support_marker_certificate import (
    B, FIXED_GRID, SCALE, _fixed, _fadd, _fneg, _fmul, _fdivint,
    budgets, gamma_symbol, marked_symbol, odd_bessel,
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


class SupportMarkerTests(unittest.TestCase):
    def test_fixed_integer_intervals_enclose_signed_rational_arithmetic(self):
        values = [F(-1234567, 13), F(-1, 10**200), F(0), F(1, 7), F(193)]
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
            for t in [F(0), F(32), F(384)/SCALE, F(24837, 50)/SCALE, F(4096)/SCALE]:
                actual = gamma_symbol(I(t), budget)
                control = shifted_gamma(t, budget['pi'], budget['log2'])
                self.assertLessEqual(actual.lo, control.lo, str(t))
                self.assertGreaterEqual(actual.hi, control.hi, str(t))
                self.assertLess(F(actual.hi)-F(actual.lo), F(3, 10**27))

    def test_normalized_bessel_against_low_order_trigonometric_formulas(self):
        with localcontext() as context:
            context.prec = 90
            for z in [F(1, 64), F(1), F(96), F(192)]:
                sine, cosine_, sine_error, cosine_error = trig_control(z, 500)
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
            for z in [F(1), F(96), F(192)]:
                readings = odd_bessel(I(z))
                head = sum(((4*k+3)*v*v for k, v in enumerate(readings)), I(0))
                sine, _, error, _ = trig_control(2*z)
                exact, radius = (1-sine/(2*z))/2, error/(4*z)
                self.assertLessEqual(F(head.lo), exact+radius)
                self.assertGreaterEqual(F(head.hi)+tail_squared, exact-radius)
                self.assertLess(F(head.hi)-F(head.lo), F(1, 10**75))

    def test_removing_marker_invalidates_selected_high_frequency_cap(self):
        with localcontext() as context:
            context.prec = 90
            budget = budgets()
            t = I(F(24837, 50))
            marked = marked_symbol(t, budget)
            unmarked = marked-cosine(t, budget['pi'])
            self.assertLess(unmarked.hi, 0)
            self.assertGreater(marked.lo, I(B).hi)
            self.assertGreater(t.lo, 384)
            self.assertLess(budget['logs'][-1].hi, I(SCALE).lo)


if __name__ == '__main__':
    unittest.main()
