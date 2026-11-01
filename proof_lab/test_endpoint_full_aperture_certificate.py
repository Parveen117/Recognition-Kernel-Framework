"""Independent arithmetic controls for the SE7 enclosure implementation."""
import unittest
from fractions import Fraction as F
from math import factorial

from proof_lab.endpoint_full_aperture_certificate import I, N, gauss8, interval_ldl, odd_bessel


def contains(interval, rational):
    return F(interval.lo) <= rational <= F(interval.hi)


class EnclosureTests(unittest.TestCase):
    def test_interval_operations_against_exact_endpoint_rationals(self):
        cases=[(F(-7,3),F(-2,7)),(F(-2,9),F(3,11)),(F(1,7),F(8,3))]
        for a,b in cases:
            for c,d in cases:
                x,y=I(a,b),I(c,d)
                for p in (a,b):
                    for q in (c,d):
                        self.assertTrue(contains(x+y,p+q))
                        self.assertTrue(contains(x-y,p-q))
                        self.assertTrue(contains(x*y,p*q))
                        if not c <= 0 <= d:
                            self.assertTrue(contains(x/y,p/q))
        with self.assertRaises(ZeroDivisionError):
            _=I(1)/I(-1,1)

    def test_gauss_nodes_enclose_all_degree_fifteen_moments(self):
        nodes,weights=gauss8()
        self.assertTrue(all(w.lo>0 for w in weights))
        for k in range(16):
            moment=sum((w*x**k for x,w in zip(nodes,weights)),I(0))
            exact=F(0) if k%2 else F(2,k+1)
            self.assertTrue(contains(moment,exact),f"degree {k}")

    def test_downward_bessel_against_exact_trigonometric_j1(self):
        for z in [F(1,64),F(1),F(12),F(24)]:
            # Direct sin/cos Taylor formulas are independent of the high-order seeds.
            sin=sum(((-1)**k*z**(2*k+1)/factorial(2*k+1) for k in range(160)),F(0))
            cos=sum(((-1)**k*z**(2*k)/factorial(2*k) for k in range(160)),F(0))
            err=z**321/F(factorial(321))/z**2+z**320/F(factorial(320))/z
            exact=sin/z**2-cos/z
            got=odd_bessel(I(z))[0]
            self.assertLessEqual(F(got.lo),exact+err)
            self.assertGreaterEqual(F(got.hi),exact-err)
            self.assertLess(F(got.hi)-F(got.lo),F(1,10**60))

    def test_ldl_rejects_positive_diagonals_with_bad_coupling(self):
        matrix=[[1 if i==j else 0 for j in range(N)] for i in range(N)]
        matrix[0][1]=matrix[1][0]=2
        with self.assertRaises(AssertionError):
            interval_ldl(matrix,F(0))


if __name__=="__main__":
    unittest.main()
