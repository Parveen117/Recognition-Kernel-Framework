# SE7: Full prime-active aperture and the sign of the fifteen-moment Schur form

12 October 2026. Owner: Monty Dabas.

The whole odd aperture of radius 1/2 now has a certified positive
source floor. No vanishing-moment condition is imposed. The written
reduction and the outward-rounded finite calculation below prove
\[
 \boxed{s[f]\ge\frac1{25000}\|Rf\|_2^2,\qquad
 s[f]\ge\frac{2}{903127}\|f\|_X^2,\qquad f\in X_{1/2}.}
                                                        \tag{SE7.1}
\]
Section 6 derives the native bound using s itself in the graph-norm
estimate; it does not identify the L2 and native norms.

Consequently the remaining SE6 fifteen-dimensional Schur form is
strictly positive. Its entries are not computed: its sign follows by
domination from a separately certified forty-dimensional comparison.
This is a finite-aperture result, not the unbounded-aperture sign or RH.

The frequency-split and Legendre-tail method has prior art. See the
[source record](SE7_SOURCE_RECORD.md). The certificate here is recomputed
for the corrected SE4 odd source, with its negative completion pole,
and transported through the existing native metric. No published
numerical certificate is assumed correct or imported as an axiom.

## 1. Source and representation contract

Retain the typed cuts, cut scalars, derived iota, lawful composition,
targets and Smriti before the admitted T35 logarithmic representation.
Keep the native dagger and graph metric from
[SE4](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md) and
[SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md).
Let g=Rf=e^{-3|x|/2}f, with Fourier transform
hat g(t)=int g(x)exp(itx)dx and measure dt/(2pi).
The source is S=N_*-L_*^dagger L_*, where L_* includes both debts
and the actual odd boundary. On X_{1/2}, the exact support rule of
[SE6](SE6_PAIRED_APERTURE_AND_MOMENT_SCHUR.md) leaves prime 2 only:
\[
 \begin{split}
 s[f]&=\int_{\mathbb R}\Psi(t)|\widehat g(t)|^2\frac{dt}{2\pi}
             -2\left|\int_{-1/2}^{1/2}g(x)\sinh(x/2)dx\right|^2,\\
 \Psi(t)&=G(t)-\sqrt2\log2\cos(t\log2),\qquad
 G(t)=\Re\psi(1/4+it/2)-\log\pi.
 \end{split}                                           \tag{SE7.2}
\]
These signs and factors also hold for complex odd g. No prime or pole
tail has been omitted on this aperture.

SE6 proves G(24)>6/5, monotonicity in |t|, and sqrt(2)log2<1.
Thus Psi(t)>b:=1/5 for |t|>=48. Parseval gives the bounded minorant
on the full odd L2 interval:
\[
 s[f]\ge r[g]:=b\|g\|_2^2+
 \frac1\pi\int_0^{48}(\Psi(t)-b)|\widehat g(t)|^2dt
       -2|\langle g,\sinh(x/2)\rangle|^2.              \tag{SE7.3}
\]
The discarded high-frequency excess is nonnegative. This is not a
finite sampling assumption on g. The bounded form r is defined on
all odd L2 functions; the source comparison is used on its graph domain.

## 2. The finite comparison and every discarded mode

For odd n define the orthonormal Legendre basis
phi_n(x)=sqrt(2n+1)P_n(2x), -1/2<x<1/2. Put
\[
 v_n(t)=(-1)^{(n-1)/2}\sqrt{2n+1}\,j_n(t/2),\qquad
 h_n=\sqrt{2n+1}\,i_n(1/4),                           \tag{SE7.4}
\]
where j_n is the spherical Bessel function and i_n its modified
version. Then hat phi_n=i v_n and h_n=int phi_n(x)sinh(x/2)dx.
The odd parity makes the same real symmetric matrix act on real and
imaginary coefficient vectors. For n,m=1,3,...,79 its leading block is
\[
 A_{nm}=b\delta_{nm}+\frac1\pi\int_0^{48}
                  (\Psi(t)-b)v_n(t)v_m(t)dt-2h_nh_m.  \tag{SE7.5}
\]
The minus sign in the last term is essential.

The Rodrigues integral for j_n, or integration by parts in the Legendre
Fourier integral, gives
\[
 |v_n(t)|\le d_n:=\frac{24^n}{(2n-1)!!},\quad
 |h_n|\le e_n:=\frac{2(1/4)^n}{(2n-1)!!},
 \quad 0\le t\le48.                                  \tag{SE7.6}
\]
For the first discarded n=81, let
\[
 a_f=\frac{d_{81}}{1-576/(163\cdot165)},\qquad
 a_h=\frac{e_{81}}{1-1/(16\cdot163\cdot165)}.
                                                        \tag{SE7.7}
\]
Successive odd-order ratios decrease, so these bound the l1, hence
l2, norms of the complete discarded vectors. On the real axis each
|v_n|<=1 by Cauchy--Schwarz, so the leading vector norm is less than 7.
The leading pole vector norm is at most ||sinh(x/2)||_2<1.
Using |Psi-b|<100 and pi>3, the infinite block D and coupling B obey
\[
 D\ge(b-\tau_D)I,\quad \|B\|\le\tau_B,\qquad
 \tau_D=1600a_f^2+2a_h^2,\quad
 \tau_B=11200a_f+2a_h.                                \tag{SE7.8}
\]
Both rational quantities are less than 10^{-20}; their exact values
are recorded. The two-block inequality therefore gives
\[
 r[g]\ge[\min(\lambda_{\min}(A),b-\tau_D)-\tau_B]\|g\|_2^2.
                                                        \tag{SE7.9}
\]
In particular, certifying the finite block alone is not the theorem:
both complete infinite-tail bounds are used.

## 3. A uniform analytic quadrature error

Use 384 panels of length 1/8 and eight-point Gauss--Legendre quadrature
on each panel. Its nodes are exact roots of
\[
 P_8(u)=(6435u^8-12012u^6+6930u^4-1260u^2+35)/128.
                                                        \tag{SE7.10}
\]
Rational sign brackets and 260 bisections enclose all eight roots.
Weights are enclosed from 2/((1-u^2)P'_8(u)^2). All node and weight
uncertainties enter the evaluation intervals, rather than being
treated as exact decimals.

For each panel take the Bernstein ellipse of parameter rho=7.
Its semimajor radius in the t-plane is 25/112<1/4. Thus every point
has |Im t|<1/4 and |t|<49, with no digamma pole in the ellipse.
Extend G analytically by the half-sum of the two digamma functions,
or, equivalently, by the normally convergent series
\[
 G(z)=-m_\Gamma+\sum_{k\ge0}
       \left(\frac2{\beta_k}-\frac{2\beta_k}{\beta_k^2+z^2}\right),
 \qquad \beta_k=2k+1/2.                               \tag{SE7.11}
\]
The first fifty summands have absolute sum at most
10 sum_{k<50}1/beta_k, since |beta_k +/- iz|>=beta_k-1/4.
For k>=50 the sum is at most
(8/3)49^2[(201/2)^(-3)+(1/4)(201/2)^(-2)].
Add m_Gamma<11/2, the comb bound 2 and b=1/5. The resulting exact
rational bound is below 100. This also proves the real-axis symbol
bound used in (SE7.8).

The Legendre Fourier integral and its L2 normalization give
|v_n(z)|<=exp(|Im z|/2), hence |v_n(z)v_m(z)|<4/3.
The rational budget verifies that the analytic integrand
(Psi-b)v_n v_m/pi has absolute value less than M=100 on every ellipse,
uniformly in the forty retained orders.

For an analytic function bounded by M on the rho ellipse, its
Chebyshev coefficients have magnitude at most 2M rho^{-k}.
Gauss quadrature is exact through degree 15. The integral-minus-rule
functional on [-1,1] has norm at most 4 because the weights are
positive and sum to 2. Summing the Chebyshev remainder and all panels
therefore gives the following error for each matrix entry:
\[
 \epsilon_Q=4\cdot48\cdot100\,
              \frac{7^{-16}}{1-1/7}.                 \tag{SE7.12}
\]
No comparison of two numerical quadrature resolutions is substituted
for this analytic estimate.

## 4. Enclosed point evaluations and finite positivity

The standard-library
[program](../../../proof_lab/endpoint_full_aperture_certificate.py)
uses separate 90-digit Decimal floor and ceiling contexts for every
interval addition, product and division. Integers and rational
constants are converted outward. Integer square roots enclose the
normalizing factors. There are no scipy, numpy or float eigenvalue
dependencies in the certificate.

The implementation uses the following independently bounded series.

* Machin's arctangent identity encloses pi; the positive atanh series
  encloses logarithms, with geometric remainder. Euler--Maclaurin at
  1024 encloses gamma by
  H_1024-log(1024)-1/(2048)+1/(12*1024^2), with absolute error at most
  1/(120*1024^4). This determines m_Gamma.
* The first 128 positive digamma-difference summands are evaluated
  directly. With y=t/2 and a=513/4, the remaining sum is
  sum_{r=1}^{10}(-1)^{r-1}y^{2r} zeta(2r+1,a), with remainder between
  zero and y^22 zeta(23,a). Here y/a<1. The positive power sums are
  enclosed by Euler--Maclaurin through B_12. The periodic-Bernoulli
  remainder has absolute value at most the last included term:
  |B_12| (p)_11 a^(-p-11)/12!. This follows by bounding the periodic
  Bernoulli function by |B_12| and integrating (x+a)^(-p-12).
* The cosine is reduced by an enclosed multiple of 2pi to |x|<4.
  Its degree-100 Taylor polynomial has error at most 4^102/102!.
* Enclosed power series for j_80 and j_81 seed the exact downward
  recurrence j_{n-1}=(2n+1)j_n/z-j_{n+1}. Ninety correction terms are
  included; the omitted alternating tail is bounded by its first
  term, since the subsequent ratios are below one. Modified Bessel
  pole coefficients use forty positive correction terms and a
  geometric upper tail. The pole is not quadrature-sampled.

Let A_tilde be the rational decimal midpoint matrix in the
[matrix archive](../../../proof_lab/ENDPOINT_FULL_APERTURE_MATRIX.json).
The maximum row sum of all point-evaluation interval radii, plus
40 epsilon_Q, bounds ||A-A_tilde||. The recorded upper bound is
less than 2.697*10^(-8), and in particular less than 10^(-6).

Interval LDL elimination, applied to the rational matrix
A_tilde-(51/10^6)I, encloses forty strictly positive pivots.
Thus it proves positivity of that exact rational matrix, not merely
success of a floating-point factorization. It follows that
\[
 \boxed{A\ge\frac1{20000}I.}                         \tag{SE7.13}
\]
Combining (SE7.8)--(SE7.9) yields r[g]>=||g||^2/25000 and then
the physical source floor. The
[result](../../../proof_lab/ENDPOINT_FULL_APERTURE_RESULT.json)
contains all pivot intervals, error budgets and the matrix SHA-256.
The finite calculation is reproducible, not proof-assistant formalized.

## 5. The SE6 Schur sign is now settled on this aperture

Keep the exact native moment projection Pi and Q=I-Pi of SE6.
The pivot D_Q remains the already proved coercive operator on the
fifteen-moment blind complement; its inverse is not approximated here.
For p in ran Pi the exact Schur identity is
\[
 \langle p,F_{15}p\rangle_X
       =\inf_{y\in\operatorname{ran}Q}s[p+y].         \tag{SE7.14}
\]
Once the native bound in Section 6 is applied, native orthogonality
gives
\[
 \boxed{F_{15}\ge\frac2{903127}I_{\operatorname{ran}\Pi}.}
                                                        \tag{SE7.15}
\]
The mixed block and exact inverse in F_15 are retained by the infimum.
The forty Legendre coordinates are a certificate for a lower comparison
form; they do not replace the fifteen native moments, or relabel them
as the historical five-source matrix.

## 6. Native observer consequence and remaining limit

SE6's graph estimate, with e^(3/2)<5, m_Gamma<11/2, p_A<1 and
beta_A<1/16, gives
\[
 \|f\|_X^2\le s[f]+\frac{289}{16}\|g\|_2^2
       \le\left(1+\frac{289\cdot25000}{16}\right)s[f].
                                                        \tag{SE7.16}
\]
This proves the native bound 2/903127. Since N_*<=11I/2, the joint
target and mismatch satisfy on the entire X_{1/2}
\[
 \boxed{\|\mathcal L_*f\|^2
 \le\left(1-\frac4{9934397}\right)\|A_*f\|^2.}       \tag{SE7.17}
\]
Injectivity and the native floor make the local exact observer
A_*f -> L_*f bounded on the closed range A_*(X_{1/2}); extending it
by zero on the orthogonal complement gives an exact local contraction.
This does not bound the already constructed global observer by one.

The same constants hold on smaller odd apertures by inclusion. The
full graph carrier has escape states from SE4, so the local strict
reserve cannot simply be carried unchanged to infinite aperture.
Every larger support range needs its actual primes, pole, finite
comparison and complete tail estimates. Neither that exhaustion nor
the global eta=0 sign has been proved here.

See [verification scope](SE7_SCOPE.md) and
[source pins](SE7_SOURCE_PINS.json). Earlier stages remain historical
records: their statements that the full radius-1/2 sign was open are
superseded only by this later, explicitly scoped certificate.
