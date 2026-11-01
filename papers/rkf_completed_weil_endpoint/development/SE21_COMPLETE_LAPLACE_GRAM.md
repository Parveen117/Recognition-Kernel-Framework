# SE21: complete-source Laplace Gram at zero shift

12 October 2026. Owner: Monty. Written proof and executed finite certificate.

This continues SE20's complete signed-cancellation route. It evaluates
the unchanged source at eta=0 on functions with unbounded spatial
support. The prime series is summed with a proved infinite remainder;
no prime cutoff, zero-location assumption or Gamma truncation is used.
The executed result proves strict positivity on the sixteen-dimensional
complex span specified below. It does **not** prove positivity on its
unobserved complement or on the whole native carrier. The requested
global eta-zero endpoint remains unfinished.

## 1. Source contract and admissible observations

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the admitted T35/T40 representation. Retain precisely
SE4/SE20's native odd carrier X, graph norm, multiplier m and source:
\[
 m(x)=e^{-3|x|/2},\qquad s[f]=\Gamma[f]-P[f]-F[f],
 \qquad h(x)=\sqrt2 f(x)\quad(x>0).                 \tag{SE21.1}
\]
For real r>0 let h_r(x)=e^{-rx} and let f_r be its faithful odd lift
f_r(x)=sgn(x)e^{-r|x|}/sqrt(2). Values at the single point zero are
irrelevant. Define a=r+3/2 and z=r+2=a+1/2. For another rate q>0 use
b=q+3/2 and w=q+2. The Fourier convention is the inherited positive
exponent; the transformed lift of m f_r is sqrt(2)i xi/(a^2+xi^2).
Its product with the conjugate transform of m f_q is
2xi^2/((a^2+xi^2)(b^2+xi^2)).

These lifts belong to X even though an individual lift has a jump at
zero. Indeed the SE16 digamma series, split at beta_k comparable to
|xi|, gives |G(xi)|=O(1+log(2+|xi|)). The squared transform is O(xi^-2)
at infinity, so the native graph integral converges. Odd smoothing and
cutoff approximate these piecewise smooth, exponentially decaying lifts
in H^sigma for 0<sigma<1/2, hence in this logarithmically weighted graph.
This agrees with the inherited completion of the odd smooth core.

An observation family is a finite list of these actual source states.
Its Gram is formed with the source pairing, including every mixed
entry; it is not a replacement primitive pairing or an asserted
finite-dimensional reduction of the whole operator.

## 2. Exact complete-source response

For real z>2 set
\[
 L(z)=-\frac{\zeta'(z)}{\zeta(z)}
     =\sum_{n\ge2}\frac{\Lambda(n)}{n^z},\qquad
 Q(z)=\frac{\xi'(z)}{\xi(z)}
 =\frac1z+\frac1{z-1}-\frac{\log\pi}{2}
   +\frac12\psi(z/2)-L(z).                       \tag{SE21.2}
\]
Here xi(z)=z(z-1)pi^(-z/2)Gamma(z/2)zeta(z)/2 is only a compact
notation for absolutely convergent positive-real data. The certificate
uses this right-hand expression. No zeros, continuation into the
critical strip, or RH premise enter the computation.

**Theorem 1 (complete Laplace source matrix).** For r,q>0,
\[
 \boxed{s(f_r,f_q)=
 \frac{2\{aQ(z)-bQ(w)\}}{a^2-b^2}\quad(r\ne q),
 \qquad s[f_r]=Q'(z)+\frac{Q(z)}a.}              \tag{SE21.3}
\]
This is a real symmetric kernel and gives the full Hermitian form on
arbitrary complex linear combinations by polarization.

**Proof.** SE20's exact event folding gives the polarized response
\[
 C_{r,q}(t)=\frac{e^{-rt}+e^{-qt}}{r+q+3}
       -\frac{e^{-rt}-e^{-qt}}{q-r},\quad
 C_{r,r}(t)=e^{-rt}\left(\frac2{2r+3}-t\right). \tag{SE21.4}
\]
The divided difference is its continuous diagonal limit. Integrating
against u^-2 dpsi(u), t=log u, retains all prime powers and gives
\[
 P_{r,q}=\frac{L(z)+L(w)}{a+b}
             +\frac{L(z)-L(w)}{z-w},\quad
 P_{r,r}=\frac{L(z)}a+L'(z).                     \tag{SE21.5}
\]
Both series and their needed derivatives converge absolutely.

Direct integration of the retained odd Gamma kernel yields
\[
 \langle h_r,K^-_\beta h_q\rangle
       =\frac{2\beta}{(a+b)(a+\beta)(b+\beta)}.
                                                               \tag{SE21.6}
\]
Insert this in the complete digamma series with beta_k=2k+1/2.
The constant term is -m_Gamma/(a+b), and its kth remaining term is
(2/beta_k-2beta_k/((a+beta_k)(b+beta_k)))/(a+b). Summing by the
digamma difference identity gives
\[
 \Gamma_{r,q}=
 \frac{a\psi(z/2)-b\psi(w/2)-(a-b)\log\pi}{(a-b)(a+b)},
 \quad
 \Gamma_{r,r}=\frac{\psi(z/2)+(a/2)\psi'(z/2)-\log\pi}{2a}.
                                                               \tag{SE21.7}
\]
The full pole entry, from SE20.2, is
F_{r,q}=1/(z(z-1)w(w-1)). Substitute (SE21.2) in Gamma-P.
The prime terms combine exactly into aQ(z)-bQ(w). The remaining
rational contribution equals the pole, since
\[
 a\left(\frac1z+\frac1{z-1}\right)
       =2+\frac1{2z(z-1)},\qquad
 -\frac{1/(z(z-1))-1/(w(w-1))}{(z-w)(z+w-1)}=F_{r,q}.
                                                               \tag{SE21.8}
\]
Subtract F, leaving (SE21.3); its diagonal follows by differentiation.
All evaluations are of the same bounded native source. QED.

Equivalently put t=a^2 and Phi(t)=sqrt(t)Q(1/2+sqrt(t)). Then
\[
 s(f_r,f_q)=2\frac{\Phi(t)-\Phi(u)}{t-u},\qquad
 s[f_r]=2\Phi'(t),\quad t,u>9/4.                 \tag{SE21.9}
\]
This is the usual divided-difference, or Loewner, kernel. The equation
is an exact source identity, not a theorem asserting that Phi is
operator monotone. Scalar increase would be insufficient: Phi(t)=t^3
has positive derivative, but its divided-difference matrix at 1,2 is
[[3,7],[7,12]], of determinant -13. Mixed readings are indispensable.

## 3. The integer-rate observations form a native dense family

Let V_N=span_C{f_1,...,f_N} and let M_N=(s(f_j,f_k))_(1<=j,k<=N).
Distinct exponentials are linearly independent, so V_N has dimension N.

**Theorem 2 (all-order criterion, with no finite stopping inference).**
\[
 \overline{\bigcup_N V_N}^{\,X}=X,\qquad
 S_b\succeq0\ \Longleftrightarrow\ M_N\succeq0
                      \text{ for every positive integer }N.    \tag{SE21.10}
\]

**Proof.** Start with a compactly supported smooth odd native core
state, and its smooth half-line h, with h(0)=0. Write t=e^-x and
H(t)=h(-log t). Since h is zero for large x, H is zero near t=0.
At t=1 the zero of h makes
U(t)=H(t)/(t(1-t)) extend smoothly (C1 suffices) to [0,1]. Approximate
U in C1 by polynomials p_N: approximate U' uniformly by a polynomial
and integrate, matching U(0). Then
\[
 h_N(x)=e^{-x}(1-e^{-x})p_N(e^{-x})              \tag{SE21.11}
\]
is a finite combination of positive integer-rate exponentials.
If ||p_N-U||_(C1)<=epsilon, both the L2(dx) error and its first
derivative are bounded by a fixed constant times epsilon, using
dx=-dt/t and the common t factor. Each error has trace zero at x=0,
so its odd lift has the same H1 convergence. Multiplication by m
preserves that convergence. SE4's bound
|G(xi)|<=m_Gamma+(131/8)xi^2 therefore gives convergence in X.
The inherited core is dense in X, proving the first assertion.
Positivity passes to X because s is a bounded form there; the converse
is restriction. This proves the equivalence without asserting any of
its unverified signs. QED.

The theorem does not identify a fixed N with the full source. A
positive M_N cannot bound the next Schur complement by itself. In an
admitted native orthogonal splitting X=V_N plus V_N^perp, a full proof
from this stage would require
S_complement-S_cross^dagger S_observed^(-1) S_cross >=0 on the whole
complement, or an independent all-order proof of (SE21.10). Neither
has been established. Coordinate changes within a fixed V_N give
congruent Grams and preserve its inertia; they do not erase that
complement condition.

## 4. Certified arithmetic retaining the entire prime series

Write E(z)=(1-2^(1-z))zeta(z), reserving eta for the spectral shift.
For real integer z>=2 and integer K>=1 use
\[
 E_K(z)=\sum_{k=0}^{K-1}2^{-k-1}
       \sum_{j=0}^k(-1)^j\binom{k}{j}(j+1)^{-z}.
                                                               \tag{SE21.12}
\]
Its first two derivatives are computed by multiplying each summand
by (-log(j+1))^d. This is an Euler transform with a complete analytic
remainder; its term count is not a prime cutoff.

**Theorem 3 (entire-series derivative remainder).** For d=0,1,2,
\[
 |E^{(d)}(z)-E_K^{(d)}(z)|
            \le d!\,2^d\,2^{1-K}\quad(z\ge2).                \tag{SE21.13}
\]

**Proof.** The Mellin integral for (j+1)^(-z) and the finite binomial
sum give an exact remainder, analytic for Re z>0:
\[
 R_K(z)=\frac1{\Gamma(z)}\int_0^\infty
   v^{z-1}\frac{e^{-v}}{1+e^{-v}}
         \left(\frac{1-e^{-v}}2\right)^Kdv.       \tag{SE21.14}
\]
For z=sigma+i tau, its absolute value is at most
2^-K Gamma(sigma)/|Gamma(z)|. On |z-z_0|<=1/2 with real z_0>=2,
sigma>=3/2 and |tau|<=1/2. The Gamma product gives
\[
 \frac{\Gamma(\sigma)}{|\Gamma(\sigma+i\tau)|}
 =\prod_{n\ge0}\sqrt{1+\tau^2/(\sigma+n)^2}
 \le\exp\!\left[\frac{\tau^2}2
                 (\sigma^{-2}+\sigma^{-1})\right]
 \le e^{5/36}<2.                                \tag{SE21.15}
\]
Cauchy's derivative bound on this disk gives (SE21.13), including
both the factorial and the radius factor. This proves an error bound
for the derivatives of the remainder, not the invalid operation of
differentiating a scalar error estimate. QED.

With D=1-2^(1-z), the ordinary derivative jets are reconstructed by
zeta=E/D, zeta'=(E'-D'zeta)/D,
zeta''=(E''-2D'zeta'-D''zeta)/D. D is strictly positive here.
The logarithmic derivative and its derivative then give Q and Q'.
Euler's product in Re z>1 identifies these with all prime powers.

For integer/half-integer z/2, exact digamma/trigamma recurrences reduce
the Gamma readings to Euler's constant, log2 and pi. The implementation
encloses Euler's constant by
\[
 \gamma=H_M-\log M-\frac1{2M}
       +\sum_{k=1}^p\frac{B_{2k}}{2kM^{2k}}+R,
 \qquad |R|\le\frac{|B_{2p}|}{2pM^{2p}},
 \quad M=1024,\ p=32.                            \tag{SE21.16}
\]
This conservative last-term bound follows from the periodic-Bernoulli
Euler--Maclaurin remainder, using
|B_(2p)({x})|<=|B_(2p)| and integrating x^(-2p-1).
The inherited Machin arctangent and positive-logarithm series retain
their proved tails. No library black-box zeta evaluation is evidence.

## 5. Executed eta-zero result and its boundary

**Theorem 4 (certified sixteen-direction sign).** In the unchanged
source normalization,
\[
 s\!\left[\sum_{j=1}^{16}c_j f_j\right]>0
       \quad\text{for every }c\in\mathbb C^{16}\setminus\{0\}.
                                                               \tag{SE21.17}
\]

**Certificate proof.** The standard-library replay uses K=320 and
90-digit outward-rounded interval operations inherited unchanged from
SE7. It encloses zeta,zeta',zeta'' at z=3,...,18, constructs all 256
source entries by (SE21.3), and checks them against the separately
assembled Gamma-prime-pole formulas. Interval LDL produces sixteen
strictly positive pivots. The minimum pivot lower endpoint is
greater than 1.6005027 times 10^-42. Interval induction encloses the
actual LDL factors; positive pivots prove the real symmetric matrix
positive definite and hence its complex Hermitian form positive.
This number is a pivot bound in this basis, not a native spectral gap.
The [result](../../../proof_lab/ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json)
records every entry, jet, remainder and pivot. QED, subject to the
declared executable arithmetic and written analytic bounds.

The initial K=256 sixteen-direction attempt was inconclusive: pivot
16's interval straddled zero. Increasing the proved Euler remainder
accuracy to K=320 resolved that arithmetic ambiguity. It was neither
a negative source witness nor a reason to replace a pin with a PASS.
Independent controls compare even zeta values, ordinary Dirichlet
derivative tails, complete Gamma-mode tails, and exact SE20 reference
cancellations. Fault controls reject erased signs, omitted mixed
information, and uncertified pivots.

This proves eta=0 **on V_16 only**, including its unbounded spatial
tails and all complex mixtures. The universal inequality in SE20.17,
the complement in section 3, global critical recovery, historical
five-label attachment, K0 and RH are still open. The previous global
shift 10883/18450 and local radius 21/25 are unchanged. No all-N
induction, formal proof-assistant check, external review or global
engine PASS is asserted. See [scope](SE21_SCOPE.md),
[source record](SE21_SOURCE_RECORD.md) and [pins](SE21_SOURCE_PINS.json).
