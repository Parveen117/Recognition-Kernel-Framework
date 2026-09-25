"""Exact negative controls for the 2026-09-25 corrections.

Finite controls complement the written proofs; they do not certify arbitrary
operators, infinite limits, or physical identifications.
"""
from fractions import Fraction as F
import itertools
import unittest
from proof_lab.native_seam_gap_odd_covariance import (
    flow_face, mat, sc, mass, kron, face_hypotheses, t5_mixed_tensor_control,
)
from proof_lab.infinite_face_recognition_completion import word_mass

# Formal noncommuting polynomials through degree three. A word's length is
# its step degree, so coefficients are checked before choosing matrices.
def add(*polys):
    out = {}
    for p in polys:
        for w, c in p.items(): out[w] = out.get(w, F(0)) + c
    return {w: c for w, c in out.items() if c}

def scale(c, p): return {w: c * x for w, x in p.items() if c * x}

def mul(p, q):
    out = {}
    for w, a in p.items():
        for v, b in q.items():
            if len(w + v) <= 3: out[w + v] = out.get(w + v, F(0)) + a*b
    return {w: c for w, c in out.items() if c}

def log_near_identity(p):
    y = add(p, {(): F(-1)})
    return add(y, scale(F(-1,2), mul(y,y)), scale(F(1,3), mul(mul(y,y),y)))

def degree(p, n): return {w:c for w,c in p.items() if len(w)==n}

class CorrectionRegressions(unittest.TestCase):
    def test_repeated_mixed_face_refutes_mass_equality_preserves_gap(self):
        self.assertTrue(all(t5_mixed_tensor_control()['checks'].values()))

    def test_face_hypotheses_require_positive_floor_and_subunit_ratio(self):
        d=mat([[0,sc(1,1)],[0,0]])
        for f0,rho in [(F(0),F(1,2)),(F(-1),F(1,2)),(F(1),F(1)),(F(1),F(-1))]:
            fc=flow_face(f0,F(0),d,F(1))
            self.assertFalse(face_hypotheses(fc,rho)['H2_mass_contraction'])

    def test_t54_word_product_is_only_an_upper_bound(self):
        fc=flow_face(F(1),F(1,8),mat([[0,sc(1,1)],[0,0]]),F(1))
        fc['mu']=mass(fc['B'])
        self.assertEqual(word_mass([fc,fc],(-1,-1)),F(1,4))
        self.assertEqual(mass(kron(fc['B'],fc['B'])),F(7,32))

    def test_twisted_trace_uses_successive_prefixes(self):
        # Additive arrows, t(a)=a^2/2 and normalized cocycle omega(b,a)=ba.
        trace=lambda a:F(a*a,2)
        omega=lambda b,a:F(b*a)
        for a,b,c in itertools.product(range(-2,3),repeat=3):
            self.assertEqual(omega(c,b)+omega(c+b,a),omega(b,a)+omega(c,b+a))
        for word in itertools.product(range(-2,3),repeat=4):
            total=sum(trace(x) for x in word)
            total+=sum(omega(word[k],sum(word[:k])) for k in range(1,len(word)))
            self.assertEqual(total,trace(sum(word)))
        old=3*trace(1)+omega(2,1)+omega(1,2)
        self.assertEqual(old,F(11,2))
        self.assertNotEqual(old,trace(3))

    def test_euler_and_symmetric_generator_defects(self):
        I={():F(1)}; A={('A',):F(1)}; B={('B',):F(1)}
        C1=add(I,A); C2=add(I,B)
        ordinary=log_near_identity(mul(C1,C2))
        expected={('A','B'):F(1,2),('B','A'):F(-1,2),('A','A'):F(-1,2),('B','B'):F(-1,2)}
        self.assertEqual(degree(ordinary,2),expected)
        root=add(I,scale(F(1,2),A),scale(F(-1,8),mul(A,A)),scale(F(1,16),mul(mul(A,A),A)))
        sym=log_near_identity(mul(mul(root,C2),root))
        self.assertEqual(degree(sym,2),{('A','A'):F(-1,2),('B','B'):F(-1,2)})
        inverse=lambda X:add(I,scale(-1,X),mul(X,X),scale(-1,mul(mul(X,X),X)))
        loop=mul(mul(mul(C1,C2),inverse(A)),inverse(B))
        self.assertEqual(degree(loop,1),{})
        self.assertEqual(degree(loop,2),{('A','B'):F(1),('B','A'):F(-1)})

    def test_torus_zero_mode_has_nonzero_coefficient(self):
        # Squared coefficient modulus is 1+(k.Omega)^2, including k=0.
        self.assertEqual(1+F(0)**2,1)
        for x in (F(-3),F(-1,7),F(0),F(5,2)): self.assertGreater(1+x*x,0)

    def test_irreducibility_does_not_make_shannon_entropy_monotone(self):
        K=((F(3,4),F(1,4)),)*2
        p=(F(1,2),F(1,2))
        out=tuple(sum(p[i]*K[i][j] for i in range(2)) for j in range(2))
        self.assertEqual(out,(F(3,4),F(1,4)))
        # exp(4 S(out))=4^4/3^3 < exp(4 S(p))=16; log is increasing.
        self.assertLess(F(4**4,3**3),16)

if __name__=='__main__': unittest.main()
