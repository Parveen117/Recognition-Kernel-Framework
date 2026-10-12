"""Independent analytic controls and fault rejection for the SE21 certificate."""
from fractions import Fraction as F
import json
import unittest

from proof_lab.endpoint_full_aperture_certificate import I
from proof_lab.endpoint_global_eta_certificate import integer_log
from proof_lab.endpoint_precision_frontier_certificate import refined_constants
from proof_lab.endpoint_zero_shift_laplace_certificate import (
    RESULT, bernoulli_numbers, euler_tail, interval_ldl, overlap,
    precise_constants, psi_pair, zeta_jet,
)


class ZeroShiftLaplaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cc = precise_constants()
        cls.logs = [I(0)]+[integer_log(n, cls.cc['log2']) for n in range(1, 161)]

    def test_accelerated_complete_series_against_even_zeta_values(self):
        # Analytically independent values detect signs, normalizers and lost tails.
        for s, exact in ((2, self.cc['pi']**2/6), (4, self.cc['pi']**4/90)):
            actual = zeta_jet(s, self.logs, self.cc['log2'], 160)[0]
            self.assertTrue(overlap(actual, exact))
            self.assertLess(actual.lo, exact.hi)
            self.assertGreater(actual.hi, exact.lo)

    def test_ordinary_derivative_jets_against_complete_dirichlet_tails(self):
        s, n = 3, 128
        actual = zeta_jet(s, self.logs, self.cc['log2'], 160)
        ell, a = self.logs[n], s-1
        tails = [I(F(1, a*n**a)),
                 (ell/a+F(1, a*a))/n**a,
                 (ell**2/a+2*ell/(a*a)+F(2, a**3))/n**a]
        for j in range(3):
            head = sum((self.logs[k]**j/F(k**s) for k in range(1,n+1)), I(0))
            bound = head+I(0,tails[j].hi)
            if j % 2:
                bound = -bound
            self.assertLessEqual(bound.lo,actual[j].lo)
            self.assertGreaterEqual(bound.hi,actual[j].hi)
        self.assertLess(actual[1].hi,0)
        self.assertGreater(actual[2].lo,0)

    def test_euler_maclaurin_constants_against_independent_older_enclosure(self):
        self.assertEqual(bernoulli_numbers(8)[2::2], [F(1,6),F(-1,30),F(1,42),F(-1,30)])
        _,_,older = refined_constants()
        newer = self.cc['gamma']+self.cc['pi']/2+3*self.cc['log2']+self.cc['logpi']
        self.assertLess(older.lo,newer.lo)
        self.assertGreater(older.hi,newer.hi)
        self.assertGreater(self.cc['gamma_error'],0)

    def test_gamma_formula_against_positive_full_mode_remainder(self):
        mg = self.cc['gamma']+self.cc['pi']/2+3*self.cc['log2']+self.cc['logpi']
        for s,t in ((3,3),(3,7),(6,12)):
            a,b = F(2*s-1,2), F(2*t-1,2)
            ps,tri = psi_pair(s,self.cc)
            pt,_ = psi_pair(t,self.cc)
            if s==t:
                closed = (ps+a*tri/2-self.cc['logpi'])/(2*a)
            else:
                closed = ((a*ps-b*pt)/(a-b)-self.cc['logpi'])/(a+b)
            modes = 128
            head = sum((2/F(4*k+1,2)-2*F(4*k+1,2)/
                ((a+F(4*k+1,2))*(b+F(4*k+1,2))) for k in range(modes)),F(0))
            beta = F(4*modes+1,2)
            # Sum of decreasing beta^-p <= its first term plus its integral.
            tail = 2*(beta**-2+1/(2*beta))+2*a*b/(a+b)*(beta**-3+1/(4*beta**2))
            lower = (head-mg)/(a+b)
            bound = lower+I(0,tail)
            self.assertLessEqual(bound.lo,closed.lo)
            self.assertGreaterEqual(bound.hi,closed.hi)

    def test_se20_complete_reference_and_pole_cancellation_exactly(self):
        for r,s in ((1,1),(1,4),(3,7),(12,16)):
            r,s=F(r),F(s)
            a,b=r+F(3,2),s+F(3,2)
            pole=1/((r+1)*(r+2)*(s+1)*(s+2))
            continuous=(1/(r+1)+1/(s+1))/(r+s+3)-1/((r+1)*(s+1))
            kernel=1/((a+b)*(a+F(1,2))*(b+F(1,2)))
            self.assertEqual(continuous+pole,-kernel)
            self.assertNotEqual(continuous-pole,-kernel)
            self.assertNotEqual(continuous+pole,kernel)
            for density_power in (1,3,5):
                beta=F(2*density_power-1,2)
                actual=(1/(r+density_power+1)+1/(s+density_power+1))/(r+s+3)-1/(
                    (r+density_power+1)*(s+density_power+1))
                exact=2*beta/((a+b)*(a+beta)*(b+beta))
                self.assertEqual(actual,exact)

    def test_pole_cancels_rational_xi_normalization_exactly(self):
        for s,t in ((3,4),(3,9),(6,13)):
            a,b=F(2*s-1,2),F(2*t-1,2)
            rs=a*(F(1,s)+F(1,s-1))
            rt=b*(F(1,t)+F(1,t-1))
            pole=F(1,s*(s-1)*t*(t-1))
            self.assertEqual(-2*(rs-rt)/(a*a-b*b),pole)

    def test_cauchy_derivatives_keep_factorial_and_radius(self):
        self.assertEqual([euler_tail(20,j) for j in range(3)],
                         [F(2,2**20),F(4,2**20),F(16,2**20)])
        with self.assertRaises(ValueError):
            euler_tail(0,0)

    def test_positive_diagonal_does_not_certify_mixed_or_next_directions(self):
        interval_ldl([[I(1)]])
        with self.assertRaises(AssertionError):
            interval_ldl([[I(1),I(2)],[I(2),I(1)]])
        with self.assertRaises(AssertionError):
            interval_ldl([[I(1),I(0)],[I(0),I(-1)]])
        # phi(t)=t^3 is increasing but its Loewner matrix at 1,2 is indefinite.
        with self.assertRaises(AssertionError):
            interval_ldl([[I(3),I(7)],[I(7),I(12)]])

    def test_interval_ldl_refuses_uncertainty_crossing_zero(self):
        with self.assertRaises(AssertionError):
            interval_ldl([[I(-F(1,100),F(1,100))]])
        with self.assertRaises(ValueError):
            interval_ldl([[I(1),I(0)],[I(1),I(1)]])

    def test_checked_result_keeps_global_and_finite_claims_distinct(self):
        result=json.loads(RESULT.read_text())
        self.assertEqual(result['eta'],'0/1')
        self.assertTrue(result['all_prime_powers_included'])
        self.assertTrue(result['all_gamma_modes_included'])
        self.assertFalse(result['unobserved_complement_certified'])
        self.assertFalse(result['global_eta_zero_certified'])
        self.assertFalse(result['rh_proved'])
        self.assertEqual(len(result['pivots']),result['dimension'])


if __name__=='__main__':
    unittest.main()
