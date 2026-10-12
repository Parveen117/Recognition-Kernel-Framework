# SE10: Prime-power crossing and completeness of the local certificate family

12 October 2026. Owner: Monty.

The corrected full odd source is now certified through the prime-power
event 4=2^2. In the radius-1/2 reference chart the endpoint is c=7/5;
its physical radius is 7/10. The executed bounds are
\[
 \boxed{s[f]\ge\frac1{20000000000}\|Rf\|_2^2,
 \qquad s[f]\ge\frac1{466500000001}\|f\|_X^2,
 \quad f\in X_{7/10}.}                             \tag{SE10.1}
\]
The exact local joint observer has squared reserve 2/5131500000011.
Every smaller aperture is covered by inclusion. Prime 5, at c=log 5,
is the next event outside the certified range.

The structural result concerns the certificate itself: for a fixed
finite aperture, increasing the frequency cutoff recovers the true
lower source edge up to the chosen positive cap. In particular, a
strictly positive source has a finite positive certificate in this
family once frequency, modes and arithmetic accuracy are sufficiently
refined. This rules out permanent blindness of the whole certificate
family to a strict local margin. It gives no positivity theorem for
uncertified apertures and no uniform bound on the work required.

## 1. What is retained and what is added

[SE4](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md) fixes the source;
[SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md) supplies graph bounds
and finite certification for an already bounded compact perturbation;
[SE6](SE6_PAIRED_APERTURE_AND_MOMENT_SCHUR.md) supplies native return;
[SE7](SE7_FULL_PRIME_ACTIVE_APERTURE.md) supplies the frequency minorant;
[SE8](SE8_MOVING_OBSERVER_AND_SIGNED_TRANSPORT.md) supplies actual
dilation and its native metric; and
[SE9](SE9_PRIME_EVENT_AND_NATIVE_CONTINUITY.md) supplies the fixed
catalogue and native event-continuity bound.

MP Gold 06's same-projection discipline and SE2/T28's observer joining
and cofinal principles remain in force. Their generic compact-block
argument is reused below, not counted as a new theorem. The additional
link here is convergence from the unbounded local source to its bounded
frequency comparisons, followed by an executed prime-power crossing.

The typed-cut, cut-scalar, derived-iota, composition, target and Smriti
order is unchanged. All Fourier and Hilbert statements below belong to
the explicitly admitted T35 logarithmic representation. L2 is not a
replacement for the native metric or its dagger.

## 2. A fixed local source and its complete form domain

Fix a positive rational scale c. The analytic edge limit below also
holds for arbitrary finite positive c; rational scales make the
effective certificate statement unambiguous. Work in H, the complex
odd L2 carrier supported in [-1/2,1/2].
Put
\[
 \begin{split}
 \Psi_c(t)&=G(t/c)-\sum_{\log n\le c}
                  \frac{2\Lambda(n)}{\sqrt n}\cos(t\log n/c),\\
 h_c(y)&=\sqrt c\sinh(cy/2),\qquad
 q_c[g]=\int\Psi_c(t)|\widehat g(t)|^2\frac{dt}{2\pi}
                  -2|\langle h_c,g\rangle|^2.
 \end{split}                                         \tag{SE10.2}
\]
The sum is finite. A larger finite catalogue is equally valid if its
extra correlations vanish by support, as proved in SE9. The Gamma
function and Fourier normalization are exactly those of SE4.

Let the form domain \(\mathcal D_c\) consist of the g in H with
\[
 \int(1+|G(t/c)|)|\widehat g(t)|^2\frac{dt}{2\pi}<\infty.
                                                        \tag{SE10.3}
\]
This is precisely the supported graph-form domain used by the native
aperture, after the R and dilation adapters. There is no hidden extra
boundary condition. To check the core identification, SE8's estimate
|G(t/r)-G(t)|<=(5/2)|log r| gives locally uniform bounds for dilation
in the weighted Fourier norm. Dilation is strongly continuous there:
verify it first on compactly supported frequency functions and then
use their density and those uniform bounds. For any supported g in
(SE10.3), an inward dilation with r<1 leaves a positive distance to the
two endpoints and converges to g as r increases to one. Convolution
with an even smooth compactly supported approximate identity then
produces odd smooth test functions with interior support. Its Fourier
multiplier is bounded by one and converges pointwise to one, so dominated
convergence applies in the same graph norm. On this finite interval
the additional native weight e^(3|x|) is bounded. This proves the stated
graph-core density; the scale c does not change the domain, by SE8.

The prime multiplier and pole are bounded on H. Since G is bounded
below, q_c is a semibounded closed form on \(\mathcal D_c\). Define its lower edge
\[
 \lambda_c=\inf_{g\in\mathcal D_c,\ \|g\|_2=1}q_c[g]. \tag{SE10.4}
\]
This is the actual finite-aperture source edge: the map
g->R^(-1)D_c g sends the form domain onto X_(c/2), where D_c is SE8's
L2-unitary dilation. No sign of lambda_c is assumed in the convergence
theorem below.

## 3. The frequency comparisons recover the local lower edge

Choose b>0. The positive Gamma series proves G(t)->infinity, so the
finite prime catalogue permits T_0 with Psi_c(t)>=b for |t|>=T_0.
For T>=T_0 put
\[
 K_{c,T}=bI+F_T^*M_{\Psi_c-b}F_T-2h_c\otimes h_c,
 \qquad \ell_{c,T}=\inf_{\|g\|_2=1}\langle g,K_{c,T}g\rangle.
                                                        \tag{SE10.5}
\]
Here F_T restricts the Fourier transform to [-T,T], with measure
dt/(2pi), and the displayed star is the L2 adjoint. The fixed-support
band transform is Hilbert--Schmidt, so K_(c,T)=bI+C_(c,T) with C_(c,T)
compact and self-adjoint. The same-projection compact machinery applies
at each fixed T.

For T_2>=T_1>=T_0,
\[
 K_{c,T_2}-K_{c,T_1}
 =F_{T_2\setminus T_1}^*M_{\Psi_c-b}F_{T_2\setminus T_1}
 \succeq0.                                          \tag{SE10.6}
\]
Its quadratic forms increase to q_c, interpreted as +infinity off \(\mathcal D_c\).
The tail integrand is nonnegative; bounded prime and pole terms do
not change this domain assertion. Also ell_(c,T)<=lambda_c by
domination, and ell_(c,T)<=b: along an orthonormal Legendre sequence
the compact correction has quadratic readings tending to zero.

**Local edge recovery theorem.**
\[
 \boxed{\ell_{c,T}\ \uparrow\ \min(b,\lambda_c)
                       \quad\text{as }T\to\infty.} \tag{SE10.7}
\]

**Proof.** Suppose the monotone limit were below min(b,lambda_c), and
choose a real number a strictly between them. There would be T_j->infinity
and unit vectors g_j with <g_j,K_(c,T_j)g_j><=a. Passing to a subsequence
g_j converges weakly to some g with ||g||<=1. This subsequence can also
be constructed by diagonal extraction of coefficients in the complete
Legendre basis, followed by the unit-ball bound.

For any fixed U>=T_0, monotonicity gives <g_j,K_(c,U)g_j><=a for
all sufficiently large j. Compactness of C_(c,U) gives
\[
 b+\langle g,C_{c,U}g\rangle\le a,
 \quad\text{or}\quad
 \langle g,K_{c,U}g\rangle+b(1-\|g\|^2)\le a.
                                                        \tag{SE10.8}
\]
Let U increase to infinity. The bounded right side forces g into \(\mathcal D_c\)
by monotone convergence and the domain identification above. Hence
\[
 b+(\lambda_c-b)\|g\|^2\le a<\min(b,\lambda_c),       \tag{SE10.9}
\]
which is impossible for 0<=||g||^2<=1. The reverse bound was already
proved. This establishes (SE10.7), including when lambda_c is zero
or negative. The retained term b(1-||g||^2) is what prevents a weakly
escaping unit vector from being silently replaced by zero. QED.

## 4. What completeness does, and does not, guarantee

Let P_N project onto the first N odd Legendre modes. At fixed c,T,
compactness gives
\[
 \tau_N:=\|C_{c,T}-P_NC_{c,T}P_N\|\longrightarrow0.
                                                        \tag{SE10.10}
\]
This is the fixed-compact-operator step already used in SE5 and MP
Gold 06. The leading block A_N=P_N K_(c,T) P_N and the scalar b on
its complement give the same-projection estimate
\[
 \ell_{c,T}\ge\min(b,\lambda_{\min}(A_N))-\tau_N.     \tag{SE10.11}
\]
The explicit Legendre tail/coupling bounds of SE7--SE9 make tau_N
effectively small: at fixed T their factorial decay dominates the
growing head norm. Matrix quadrature, constant enclosures and arithmetic
precision can each be refined arbitrarily. A strict rational gap then
permits finite outward enclosures and a positive interval LDL test.

Consequently the complete family, allowing all these refinements, obeys
\[
 \boxed{\lambda_c>0
 \quad\Longleftrightarrow\quad
 \text{some finite, error-enclosed comparison certifies a positive floor}.}
                                                        \tag{SE10.12}
\]
For the forward direction choose 0<r<min(b,lambda_c). Equation
(SE10.7) gives a finite T with ell_(c,T)>r. Choose N so that the
complete tail error is smaller than the remaining gap, then enclose
the finitely many entries closely enough. For the reverse direction
use K_(c,T)<=q_c. This proves an equivalence, not an assumption that
lambda_c is positive for every c.

A fixed T can fail forever under mode refinement if its lower
comparison is nonpositive. A fixed arithmetic precision can also
exhaust its available error margin. Thus the theorem requires
frequency, modes and numerical accuracy to be adjustable together.
The present replay is one fixed finite certificate, not an implemented
unbounded search or a stopping-time estimate for arbitrary c. At a
true zero edge it gives no eventual strict-positive certificate.
No uniform strict global reserve is asserted; SE4 rules that out.

## 5. The actual prime-power-4 source

Take C=7/5 and use SE9's common catalogue {2,3,4} on 1<=c<=C. The
replay verifies log 4<C<log 5. The exact symbol is
\[
 \Psi_c(t)=G(t/c)-\sqrt2\log2\cos(t\log2/c)
 -\frac{2\log3}{\sqrt3}\cos(t\log3/c)
 -\log2\cos(2t\log2/c).                            \tag{SE10.13}
\]
The final coefficient uses Lambda(4)=log 2, not log 4. The prime power
is one event in the same source, without doubling its arithmetic weight.
The negative pole remains -2c|integral g(y)sinh(cy/2)dy|^2.

Set b=1/10 and T=192. Interval logarithms and square roots give total
prime weight p<59/20 and m_Gamma<269/50. With y=480/7, the first
512 positive Gamma summands give the exact rational lower estimate
\[
 G(T/C)\ge\sum_{k=0}^{511}
 \frac{y^2}{(k+1/4)((k+1/4)^2+y^2)}-\frac{269}{50}
 >\frac{153}{50}.                                  \tag{SE10.14}
\]
Thus Psi_c(t)>11/100>b for |t|>=192 and every 1<=c<=C. This is a
valid complete-catalogue envelope. The comparison K_(C,192) therefore
dominates the source from below on the entire reference carrier.

## 6. The finer certificate and every error term

The [new replay](../../../proof_lab/endpoint_prime_power_certificate.py)
retains 88 odd Legendre orders 1,3,...,175. In the SE7 normalization,
\[
 v_n(t)=(-1)^{(n-1)/2}\sqrt{2n+1}\,j_n(t/2),\qquad
 q_n=\sqrt{C(2n+1)}\,i_n(C/4),
\]
and the exact leading block is
\[
 A_{nm}=b\delta_{nm}+\frac1\pi\int_0^{192}
       (\Psi_C(t)-b)v_n(t)v_m(t)\,dt-2q_nq_m.         \tag{SE10.15}
\]
All mixed entries are included. This comparison is not the historical
five-label Feshbach matrix or SE6's native F_15.

The old interval class, constants, cosine, power-sum enclosures and
dimension-aware LDL are imported unchanged. The following resolution
changes are confined to the new stage:

* Gauss-20 replaces Gauss-8, with 384 panels of width 1/2. All roots
  of P_20 have disjoint rational sign brackets, refined by 260 exact
  bisections. Weights are enclosed by 2/((1-x^2)P'_20(x)^2). The
  degree-39 exactness and positive weights are the standard Gauss
  rule, also checked independently against all forty rational moments.
* Gamma uses its first 128 positive summands and 32 alternating
  power-sum terms. With y=t/(2C), y<=480/7<513/4, the omitted tail
  is between zero and y^66 zeta(67,513/4). SE7's periodic-Bernoulli
  bound encloses each power sum. The number of terms is increased
  explicitly; the old ten-term error is not reused at this larger T.
* Enclosed j_176,j_177 seed the Bessel downward recurrence for z<=96.
  There are 160 series corrections; the first omitted term bounds
  the decreasing alternating tail. Pole coefficients use their
  positive series and geometric remainder, with the exact factor C.
* Point intervals still use 90-digit outward Decimal arithmetic.
  The archived candidate is rounded to forty significant decimal
  digits; every such rounding enters the same row-sum error bound.
  These stored decimals are exact rational candidates for interval LDL.

For quadrature take rho=7/2. A panel ellipse has semimajor radius
53/112<1/2, so |Im t|<1/2 and |t|<193. At the certified endpoint
|Im(t/C)|<3/8. With beta_k=2k+1/2, the Gamma-series argument gives
\[
 M_s=\frac{269}{50}+34\sum_{k<200}\frac1{\beta_k}
 +\frac83\,193^2[(801/2)^{-3}+\tfrac14(801/2)^{-2}]
 +6+\frac1{10}<200.                                \tag{SE10.16}
\]
Indeed the first terms have modulus at most 34/beta_k; the remaining
beta_k exceed twice 193. The three prime terms contribute less than
3 exp(1/2)<6, since log 4<C. Also |v_n v_m|<exp(1/2)<2 and pi>3.
Thus M=256 bounds every analytic matrix integrand. SE7's Chebyshev
remainder proof, now using exactness through degree 39, gives
\[
 \epsilon_Q=4\cdot192\cdot256\,
       \frac{(7/2)^{-40}}{1-2/7},\qquad
 88\epsilon_Q<4.184\cdot10^{-15}.                   \tag{SE10.17}
\]
All point-evaluation and Gauss node/weight uncertainties are additional
enclosed terms, not numerical resolution comparisons.

The discarded basis begins at n=177. Define
\[
 a_f=\frac{96^{177}/353!!}{1-96^2/(355\cdot357)},\quad
 a_h=\frac{4(C/4)^{177}/353!!}{1-(C/4)^2/(355\cdot357)}.
                                                        \tag{SE10.18}
\]
They bound the complete discarded Fourier and pole vectors by the
Rodrigues estimate and decreasing odd-order ratios. The Fourier head
norm is below 10, and the pole head norm below one. With the same
projection as the leading block,
\[
 D\ge(b-\tau_D)I,\quad \|B_{\rm mix}\|\le\tau_B,
 \quad\tau_D=16384a_f^2+2a_h^2<10^{-35},\quad
 \tau_B=163840a_f+2a_h<10^{-17}.                    \tag{SE10.19}
\]

The [archived rational matrix](../../../proof_lab/ENDPOINT_PRIME_POWER_MATRIX.json)
A_tilde satisfies, after every rounding and quadrature term,
\[
 \|A-A_{\rm tilde}\|<1.148\cdot10^{-13}.
                                                        \tag{SE10.20}
\]
The executed interval LDL finds 88 strictly positive pivots of
A_tilde-10^(-10)I. Hence
\[
 A\succeq8\cdot10^{-11}I,\qquad
 K_{C,192}\succeq
 [\min(8\cdot10^{-11},b-\tau_D)-\tau_B]I
 \succ5\cdot10^{-11}I.                             \tag{SE10.21}
\]
The [result](../../../proof_lab/ENDPOINT_PRIME_POWER_RESULT.json)
records every pivot, rational budget and matrix hash. The physical
dilation bijection and its L2 unitarity give the first bound in
(SE10.1) on all complex odd states in the aperture.

## 7. Native observer return and what remains

At physical radius A=7/10 the exact rational checks give
\[
 e^{3A}<33/4,\quad m_\Gamma<11/2,\quad p_A<59/20,
 \quad2(\sinh A-A)\le\frac{A^3}{3(1-A^2/20)}<1/8.
                                                        \tag{SE10.22}
\]
SE6's graph estimate therefore yields
\[
 \|f\|_X^2\le s[f]+\frac{933}{40}\|Rf\|_2^2
                 \le466500000001\,s[f].             \tag{SE10.23}
\]
With N_*<=11I/2 this proves
\[
 \|\mathcal L_*f\|^2
 \le\left(1-\frac2{5131500000011}\right)\|A_*f\|^2,
 \qquad f\in X_{7/10}.                              \tag{SE10.24}
\]
As in SE9, the exact map A_*f->L_*f extends by zero off the closed
local event range. Its restrictions to the nested smaller ranges
agree on every shared event vector. This covers all intermediate
physical apertures, including log 4/2. No positivity interpolation
between sampled comparison matrices is used or needed.

The smaller-aperture SE7--SE9 bounds remain valid. The current lower
floor is smaller because it certifies a larger space; the certificate
constants are not measurements of the true lower edge. The completeness
theorem shows what sufficient refinement can detect at a fixed c.
It does not prove lambda_c>0 at every c, bound the necessary resources,
or supply the cofinal source sign required by SE2/T28. Prime 5 is the
next unverified event. The global eta=0 sign, historical five-label
closure, K0 and RH remain open.

See [sources](SE10_SOURCE_RECORD.md), [audit](SE10_SCOPE.md) and
[pins](SE10_SOURCE_PINS.json).
