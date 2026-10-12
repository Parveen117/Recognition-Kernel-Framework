"""SE7: outward-rounded certificate for the full odd aperture |x| <= 1/2.

Standard library only. Decimal operations use separate floor/ceiling contexts;
all analytic remainders are explicit. No floating-point eigenvalue is evidence.
See SE7_FULL_PRIME_ACTIVE_APERTURE.md for the infinite-dimensional implication.
"""
from __future__ import annotations

import argparse
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt, prod
from pathlib import Path

PRECISION = 90
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING)
N = 40
T = 48
RESULT = Path(__file__).with_name("ENDPOINT_FULL_APERTURE_RESULT.json")
MATRIX = Path(__file__).with_name("ENDPOINT_FULL_APERTURE_MATRIX.json")


def dec(x, ctx):
    if isinstance(x, F):
        return ctx.divide(Decimal(x.numerator), Decimal(x.denominator))
    return Decimal(x)


class I:
    """Closed real interval; arithmetic is rounded outward at every operation."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo=0, hi=None):
        self.lo = dec(lo, DOWN)
        self.hi = dec(lo if hi is None else hi, UP)
        if self.lo > self.hi:
            raise ValueError("Reversed interval")

    def __add__(self, other):
        other = box(other)
        return I(DOWN.add(self.lo, other.lo), UP.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) - self

    def __mul__(self, other):
        other = box(other)
        if self.lo >= 0 and other.lo >= 0:
            return I(DOWN.multiply(self.lo, other.lo), UP.multiply(self.hi, other.hi))
        vals = [(x, y) for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(DOWN.multiply(x, y) for x, y in vals),
                 max(UP.multiply(x, y) for x, y in vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("Interval contains zero")
        return self * I(DOWN.divide(Decimal(1), other.hi),
                        UP.divide(Decimal(1), other.lo))

    def __rtruediv__(self, other):
        return box(other) / self

    def __pow__(self, n):
        if n < 0:
            return 1 / (self ** (-n))
        out, base = I(1), self
        while n:
            if n & 1:
                out = out * base
            n //= 2
            if n:
                base = base * base
        return out

    def abs_upper(self):
        return max(self.lo.copy_abs(), self.hi.copy_abs())

    def midpoint(self):
        # The rounded midpoint is merely a rational candidate, not an enclosure.
        return DOWN.divide(DOWN.add(self.lo, self.hi), Decimal(2))

    def record(self):
        return [str(self.lo), str(self.hi)]


def box(x):
    return x if isinstance(x, I) else I(x)


def sqrt_integer(n):
    scale = 10 ** 100
    k = isqrt(n * scale * scale)
    return I(F(k, scale), F(k + 1, scale))


def atan_reciprocal(q, count=160):
    value = sum(((-1) ** k * F(1, (2*k+1) * q**(2*k+1))
                 for k in range(count)), F(0))
    error = F(1, (2*count+1) * q**(2*count+1))
    return I(value - error, value + error)


def log_positive(x, count=200):
    x = box(x)
    if x.lo < 1:
        raise ValueError("This logarithm enclosure expects x >= 1")
    z = (x - 1) / (x + 1)
    z2, power, total = z*z, z, I(0)
    for k in range(count):
        total = total + power / (2*k+1)
        power = power * z2
    tail = 2 * power / ((2*count+1) * (1-z2))
    return 2*total + I(0, tail.hi)


def constants():
    pi = 16*atan_reciprocal(5) - 4*atan_reciprocal(239)
    log2 = log_positive(2)
    k = 1024
    h = sum((F(1, j) for j in range(1, k+1)), F(0))
    gamma = I(h) - 10*log2 - F(1, 2*k) + F(1, 12*k*k)
    err = F(1, 120*k**4)
    gamma = gamma + I(-err, err)
    mg = gamma + pi/2 + 3*log2 + log_positive(pi)
    return pi, log2, mg


BERNOULLI = [F(1,6), F(-1,30), F(1,42), F(-1,30), F(5,66), F(-691,2730)]


def hurwitz_power(p, a=F(513,4)):
    """Euler--Maclaurin through B12, with a last-term absolute remainder."""
    val = a**(1-p)/F(p-1) + a**(-p)/2
    last = F(0)
    for j, b in enumerate(BERNOULLI, 1):
        last = b/F(factorial(2*j)) * prod(range(p, p+2*j-1)) * a**(-p-2*j+1)
        val += last
    return I(val-abs(last), val+abs(last))


def gamma_symbol(t, mg, zeta):
    y2 = (t/2)**2
    total = I(0)
    for k in range(128):
        s = F(4*k+1,4)
        total = total + y2 / (s * (s*s+y2))
    power = y2
    for r in range(1, 11):
        total = total + ((-1)**(r-1)) * power * zeta[r-1]
        power = power*y2
    # The first omitted term is positive; the pointwise geometric ratio < 1.
    omitted = power*zeta[10]
    return total + I(0, omitted.hi) - mg


def cosine(x, pi):
    integer = int(DOWN.divide(DOWN.add(x.midpoint(), pi.midpoint()),
                              DOWN.multiply(Decimal(2), pi.midpoint())))
    x = x - (2*integer)*pi
    if x.abs_upper() >= 4:
        raise AssertionError("Cosine range-reduction bound")
    x2, term, total = x*x, I(1), I(1)
    for k in range(1, 51):
        term = -term*x2/((2*k-1)*(2*k))
        total = total + term
    error = F(4**102, factorial(102))
    return total + I(-error, error)


def odd_bessel(z):
    """j_1,j_3,...,j_79. Enclosed high orders seed an exact recurrence."""
    seeds = []
    for n in (80,81):
        term = z**n / prod(range(1, 2*n+2, 2))
        total = term
        for k in range(1, 91):
            term = -term*z*z/(2*k*(2*n+2*k+1))
            total = total + term
        next_term = -term*z*z/(182*(2*n+183))
        err = next_term.abs_upper()
        seeds.append(total + I(-err, err))
    values = {80: seeds[0], 81: seeds[1]}
    for n in range(80, 1, -1):
        values[n-1] = (2*n+1)*values[n]/z - values[n+1]
    return [values[n] for n in range(1,80,2)]


def pole_coefficients(roots):
    out = []
    z = F(1,4)
    for n, root in zip(range(1,80,2), roots):
        term = I(z**n / prod(range(1,2*n+2,2)))
        total = term
        for k in range(1,41):
            term = term*z*z/(2*k*(2*n+2*k+1))
            total = total + term
        nxt = term*z*z/(82*(2*n+83))
        ratio = F(1,16)/(84*(2*n+85))
        total = total + I(0, (nxt/(1-ratio)).hi)
        out.append(root*total)
    return out


def p8(x):
    x2=x*x
    return ((((6435*x2-12012)*x2+6930)*x2-1260)*x2+35)/128


def gauss8():
    positive = []
    for left, right in [(18,19),(52,53),(79,80),(96,97)]:
        lo, hi = F(left,100), F(right,100)
        sign = p8(lo)
        assert sign*p8(hi) < 0
        for _ in range(260):
            mid = (lo+hi)/2
            if p8(mid)*sign > 0:
                lo = mid
            else:
                hi = mid
        positive.append(I(lo,hi))
    nodes = [-x for x in reversed(positive)] + positive
    weights=[]
    for x in nodes:
        derivative = (51480*x**7-72072*x**5+27720*x**3-2520*x)/128
        weights.append(2/((1-x*x)*derivative*derivative))
    return nodes,weights


def analytic_budgets():
    low = 10*sum((F(1,1)/F(4*k+1,2) for k in range(50)),F(0))
    b = F(201,2)
    high = F(8,3)*49**2*(b**(-3)+F(1,4)*b**(-2))
    # On the radius-1/4 complex disks: |G| plus comb plus beta.
    symbol_bound = F(11,2)+low+high+2+F(1,5)
    assert symbol_bound < 100
    assert symbol_bound*F(4,9) < 100  # |F_m F_n| < 4/3, pi > 3.
    eps_entry = F(4*T*100, 1) * F(1,7)**16 / (1-F(1,7))
    # Chebyshev coefficient bound 2*M*rho^-k and quadrature functional norm 4.
    n=81
    d = F(24**n, prod(range(1,2*n,2)))
    r = F(24**2,(2*n+1)*(2*n+3))
    tail_f = d/(1-r)
    e = 2*F(1,4)**n / prod(range(1,2*n,2))
    rp = F(1,16)/((2*n+1)*(2*n+3))
    tail_h = e/(1-rp)
    tail_d = 1600*tail_f**2 + 2*tail_h**2
    coupling = 11200*tail_f + 2*tail_h
    assert N*eps_entry < F(1,1000000)
    assert tail_d < F(1,10**20) and coupling < F(1,10**20)
    return eps_entry,tail_d,coupling,symbol_bound


def assemble(progress=False):
    pi,log2,mg=constants()
    zeta=[hurwitz_power(2*r+1) for r in range(1,12)]
    roots=[sqrt_integer(2*n+1) for n in range(1,80,2)]
    poles=pole_coefficients(roots)
    nodes,weights=gauss8()
    matrix=[[I(0) for _ in range(N)] for _ in range(N)]
    for panel in range(384):
        center=F(2*panel+1,16)
        for node,weight in zip(nodes,weights):
            t=center+node/16
            assert 0 < t.lo <= t.hi < T
            sym=gamma_symbol(t,mg,zeta)-sqrt_integer(2)*log2*cosine(t*log2,pi)-F(1,5)
            bessel=odd_bessel(t/2)
            vec=[root*j*((-1)**k) for k,(root,j) in enumerate(zip(roots,bessel))]
            measure=weight*sym/(16*pi)
            for i in range(N):
                scaled=measure*vec[i]
                for j in range(i+1):
                    matrix[i][j]=matrix[i][j]+scaled*vec[j]
        if progress and panel%64==63:
            print(f"enclosed panels {panel+1}/384",flush=True)
    for i in range(N):
        for j in range(i+1):
            val=matrix[i][j]-2*poles[i]*poles[j]
            if i==j:
                val=val+F(1,5)
            matrix[i][j]=val
            matrix[j][i]=val
    return matrix,mg


def interval_ldl(candidate, shift):
    lower=[[I(0) for _ in range(N)] for _ in range(N)]
    pivots=[]
    for i in range(N):
        lower[i][i]=I(1)
        pivot=I(candidate[i][i])-shift
        for k in range(i):
            pivot=pivot-lower[i][k]*lower[i][k]*pivots[k]
        if pivot.lo <= 0:
            raise AssertionError(f"Uncertified LDL pivot {i}: {pivot.record()}")
        pivots.append(pivot)
        for j in range(i+1,N):
            value=I(candidate[j][i])
            for k in range(i):
                value=value-lower[j][k]*lower[i][k]*pivots[k]
            lower[j][i]=value/pivot
    return pivots


def replay(progress=False):
    eps_entry,tail_d,coupling,symbol_bound=analytic_budgets()
    matrix,mg=assemble(progress)
    candidate=[[value.midpoint() for value in row] for row in matrix]
    radius=Decimal(0)
    for row,midrow in zip(matrix,candidate):
        rowsum=Decimal(0)
        for val,mid in zip(row,midrow):
            error=max(UP.subtract(mid,val.lo),UP.subtract(val.hi,mid))
            rowsum=UP.add(rowsum,error)
        radius=max(radius,rowsum)
    assert radius < Decimal("1e-10")
    total_error=I(radius)+N*eps_entry
    assert total_error.hi < Decimal("0.000001")
    # Candidate - 51/10^6 I > 0; exact integral block is >= 1/20000 I.
    pivots=interval_ldl(candidate,F(51,1000000))
    whole_floor=F(1,25000)
    assert min(F(1,20000),F(1,5)-tail_d)-coupling > whole_floor
    native=whole_floor/(whole_floor+F(289,16))
    reserve=2*native/11
    archived={"schema":"rkf.endpoint-full-aperture-matrix.v1",
              "basis":"L2-normalized odd Legendre orders 1,3,...,79 on [-1/2,1/2]",
              "matrix":[[str(x) for x in row] for row in candidate]}
    encoded=json.dumps(archived,indent=2)+"\n"
    def rat(x): return f"{x.numerator}/{x.denominator}"
    result={
        "schema":"rkf.endpoint-full-aperture-certificate.v1", "date":"2026-10-12",
        "status":"PASS", "arithmetic":"90-digit outward-rounded Decimal; exact Fraction budgets",
        "aperture_radius":"1/2", "active_prime_powers":[2], "odd_complex_carrier":True,
        "frequency_split":T, "high_frequency_floor":"1/5", "legendre_dimension":N,
        "gauss_order":8, "panel_count":384, "complex_ellipse_parameter":7,
        "analytic_integrand_bound":100, "analytic_symbol_bound":rat(symbol_bound),
        "quadrature_error_per_entry":rat(eps_entry),
        "point_evaluation_matrix_norm_error_upper":str(radius),
        "total_leading_matrix_error_upper":str(total_error.hi),
        "candidate_ldl_shift":"51/1000000", "positive_ldl_pivots":len(pivots),
        "ldl_pivot_enclosures":[p.record() for p in pivots],
        "certified_leading_matrix_floor":"1/20000",
        "infinite_tail_deviation_upper":rat(tail_d), "infinite_coupling_upper":rat(coupling),
        "physical_source_floor":rat(whole_floor), "native_source_floor":rat(native),
        "relative_joint_observer_reserve":rat(reserve),
        "SE6_F15_sign_certified_by_domination":True, "SE6_F15_entries_computed":False,
        "gamma_ground_enclosure":mg.record(),
        "matrix_sha256":hashlib.sha256(encoded.encode()).hexdigest(),
        "not_certified":["unbounded-aperture positivity", "global norm-one observer", "Riemann hypothesis",
                         "historical five-label endpoint or K0", "formal proof-assistant checking", "external review"]}
    return result,encoded


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument("--write",action="store_true")
    mode.add_argument("--check",action="store_true")
    args=parser.parse_args()
    result,matrix=replay(progress=True)
    if args.write:
        MATRIX.write_text(matrix,encoding="utf-8")
        RESULT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    if args.check:
        if json.loads(RESULT.read_text(encoding="utf-8")) != result or MATRIX.read_text(encoding="utf-8") != matrix:
            raise SystemExit("SE7 replay differs from the stored certificate; inspect, do not repin.")
    print(json.dumps({k:result[k] for k in ["status","positive_ldl_pivots","total_leading_matrix_error_upper",
         "physical_source_floor","native_source_floor","relative_joint_observer_reserve","matrix_sha256"]},indent=2))


if __name__=="__main__":
    main()
