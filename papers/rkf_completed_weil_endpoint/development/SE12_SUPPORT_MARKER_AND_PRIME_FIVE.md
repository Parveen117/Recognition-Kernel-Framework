# SE12: Support calibration and a complete prime-5 crossing

12 October 2026. Owner: Monty.

An exact support identity improves the input to the finite observer.
The corrected full odd source is certified through the prime-5 event,
on physical radius A=161/200=0.805. The reference scale is C=161/100,
strictly greater than log 5. The full-carrier bounds are
\[
 \boxed{s[f]\ge\frac1{500000000000000}\|Rf\|_2^2,
 \qquad s[f]\ge\frac1{13925000000000001}\|f\|_X^2,
 \quad f\in X_{161/200}.}                           \tag{SE12.1}
\]
The squared local joint-observer reserve is
2/153175000000000011. Every smaller aperture is covered by native
inclusion. This settles the next event left open by SE11, not the
cofinal all-scale source sign or RH.

## 1. Native premise order and the specific recovery step

Typed cuts, cut scalars, derived iota, composition, declared target
and Smriti remain prior to representations. The following Fourier
calculations use the admitted T35/T40 logarithmic graph chart.
Neither its coordinate adjoint nor L2 dilation is silently identified
with the native dagger or a native unitary.

[SE4](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md) fixes the full source;
[SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md) and
[MP Gold 06](../../../mp_gold/06_unified_seam_block_krylov.md) supply
same-projection compact certification; SE6 supplies native return;
SE7 supplies the frequency comparison; SE8 supplies dilation; SE9
supplies support cancellation and event continuity; SE10 supplies
local certificate completeness; and
[SE11](SE11_PRECISION_FRONTIER_AND_CUTOFF_OBSTRUCTION.md) supplies
exact signed-Gram arithmetic and a proved fixed-comparison obstruction.
These are reused results.

The [path-blindness theorem](../../../theorum/morphic_recognition/02_path_blindness_minimal_memory_repair.md)
requires extra readings to separate the declared target's blind fibre.
The [bilateral-jet theorem](../../../theorum/43_bilateral_jet_flow_recognition_capstone_theorem.md)
distinguishes removal of blindness from a quantitative unit-norm decoder.
NSB1/NSB2, cited at exact versions in the
[source record](SE12_SOURCE_RECORD.md), likewise distinguish a repeated
spectral response from an independently calibrated response.

Here the added information is a known support constraint, not a new
unknown measurement. It calibrates a comparison which previously lost
full-band cancellation. The result is this particular complete source
certificate. No universal self-correction or reduced complexity theorem
is inferred from the metaphor of connecting observation circles.
No prime-distribution interpretation of a circle, torus or double helix
is used, and no geometric adapter is assumed.

## 2. Exact source-preserving support markers

Let H be the complex odd L2 carrier supported in [-1/2,1/2], with
Fourier transform g-hat(t)=integral g(y) exp(ity) dy and measure
dmu=dt/(2pi). Translation and Parseval give, for every a>=1,
\[
 \int\cos(at)|\widehat g(t)|^2\,d\mu
       =\operatorname{Re}\langle g,T_a g\rangle=0,
 \qquad g\in H.                                    \tag{SE12.2}
\]
At a=1 the supports meet only at one point, a null set. The integral
is absolutely convergent because g-hat is square integrable. Complex
polarization shows that the compressed self-adjoint cosine multiplier
is the zero operator on H, not just zero on a list of trial states.

For any finite list a_j>=1 and real alpha_j, put
\[
 m_\alpha(t)=\sum_j\alpha_j\cos(a_jt),\qquad
 \Xi_{c,\alpha}(t)=\Psi_c(t)+m_\alpha(t).             \tag{SE12.3}
\]
The complete source q_c from SE10.2 is unchanged when Psi_c is
replaced by Xi_(c,alpha), and its form domain is unchanged because
m_alpha is bounded. Such a marker cannot be used with an arbitrary
shift below one: the two supports would overlap.

If Xi_(c,alpha)(t)>=b outside [-T,T], the bounded operator
\[
 K_{c,T}^{\alpha,b}
 =bI+F_T^*M_{\Xi_{c,\alpha}-b}F_T-2h_c\otimes h_c
 \preceq q_c,
 \qquad h_c(y)=\sqrt c\sinh(cy/2),                 \tag{SE12.4}
\]
is a full-carrier lower comparison. Indeed its difference from q_c
is exactly the nonnegative integral of (Xi-b)|g-hat|^2 outside
the band. The pole and every active prime coefficient are retained.

For two choices at the same c and T,
\[
 K^{\alpha,b}-K^{\alpha',b'}
 =(b-b')(I-F_T^*F_T)
   +F_T^*M_{m_\alpha-m_{\alpha'}}F_T.                \tag{SE12.5}
\]
The full source has not changed, although the finite comparisons
can have different signs. The second term need not be positive.
Neither adding a marker nor raising the cap is an automatic repair:
the entire tail condition and head/complement bounds must be proved
again. SE11's negative witness concerned its particular unmarked
T=256 comparison; it remains valid.

## 3. The selected input and its complete high-frequency condition

Use the exact parameters
\[
 C=161/100,\quad A=C/2=161/200,\quad
 m(t)=\cos t,\quad b=3/5,\quad T=384.               \tag{SE12.6}
\]
Since log 5<C<log 7, the active catalogue is {2,3,4,5}, with
\[
 \Psi_C(t)=G(t/C)-\sum_{n\in\{2,3,4,5\}}w_n
            \cos(t\log n/C),\quad
 (w_2,w_3,w_4,w_5)=
 (\sqrt2\log2,2\log3/\sqrt3,\log2,2\log5/\sqrt5).
                                                        \tag{SE12.7}
\]
Here G(u)=Re psi(1/4+iu/2)-log pi. In particular Lambda(4)=log 2.
The marker shift is exactly one in the reference chart, independently
of prime 5's now active shift log(5)/C<1. It does not remove prime 5.

There are two parts to the high-frequency proof. For the finite
corridor [384,4096], SE8's |u G'(u)|<=5/2 gives
\[
 |\Xi'(t)|\le\frac5{2\cdot384}
       +\sum_n w_n\frac{\log n}{C}+1<5.             \tag{SE12.8}
\]
The [replay](../../../proof_lab/endpoint_support_marker_certificate.py)
starts with every closed unit interval in the corridor. A cell with
midpoint x and radius r is accepted only when its outward reading
satisfies Xi(x)_lower-5r>3/5; otherwise it is bisected. Thus each
accepted reading proves the inequality on its whole cell. The exact
sum of covered lengths must equal 3712. The result records the cell
count, deepest subdivision, minimum lower bound and a deterministic
partition hash. This is an interval covering proof, not a sampled plot.
The executed covering uses 4236 cells, maximum depth six, and has
minimum lower bound greater than 0.6011227473.

Beyond the corridor, the replay encloses
\[
 G(4096/C)>6,\qquad p=\sum_nw_n<22/5.
                                                        \tag{SE12.9}
\]
Monotonicity of G implies Xi(t)>=G(4096/C)-p-1>3/5
for t>=4096. Evenness covers negative frequencies. Together these
arguments establish the full hypothesis of (SE12.4).
The executed far-frequency floor is greater than 0.6221563585.

An independent diagnostic in the same replay fixes t_*=24837/50,
which lies outside the band, and certifies
\[
 \Psi_C(t_*)<0<3/5<\Xi_C(t_*).                     \tag{SE12.10}
\]
Removing the marker therefore invalidates this chosen positive cap
at T=384. This demonstrates a concrete benefit of the known support
information at fixed cutoff. It does not establish that no other
unmarked comparison could work. Relative to SE11 the cutoff and
mode count also increase; no isolated speedup is claimed.

## 4. Enclosing Gamma and every Fourier reading

For nonnegative u, shift z=1/4+iu/2 by 128, writing
Z=513/4+iu/2. The evaluator uses
\[
 \begin{split}
 G(u)={}&\operatorname{Re}\left[
 \log Z-\frac1{2Z}-\sum_{k=1}^6\frac{B_{2k}}{2kZ^{2k}}
 -\sum_{j=0}^{127}\frac1{j+1/4+iu/2}\right]-\log\pi+r,\\
 |r|\le{}&\frac{|B_{12}|}{12(513/4)^{12}}.
 \end{split}                                       \tag{SE12.11}
\]
The error follows from the complex periodic-Bernoulli remainder:
bound its periodic numerator by |B_12| and integrate
(Re Z+x)^(-13). It is uniform in u and does not apply a
positive-real-only remainder rule to a complex argument. Binary
reduction makes the real logarithm use the inherited convergent
series. A separate shift-2048 computation tests values from zero
through 4096/C. No old evaluator or source pin is modified.

Retain N=168 normalized odd Legendre modes, orders 1,3,...,335,
with v_n(t)=(-1)^((n-1)/2) sqrt(2n+1) j_n(t/2). To avoid numerical
loss in an unnormalized downward recurrence, set
\[
 S_n(z)=\frac{(2n+1)!!}{z^n}j_n(z),\qquad
 S_{n-1}(z)=S_n(z)
       -\frac{z^2}{(2n+1)(2n+3)}S_{n+1}(z).         \tag{SE12.12}
\]
The two seeds S_336,S_337 are enclosed by their power series with
360 corrections. The next-term ratio is below one for z<=192 and
all subsequent ratios decrease, so the first omitted magnitude
bounds the alternating remainder. Every operation in this recurrence
uses signed integer intervals on the exact grid 10^(-180), with
outward floor/ceiling division. The factor z^n/(2n+1)!! is restored
using the inherited arbitrary-exponent intervals.

Evaluation is at a rational point associated with each node enclosure.
The spherical-Bessel integral and |P_n(x)|<=1 imply
\[
 |j_n'(z)|\le\frac12\int_{-1}^1|x|\,dx=\frac12,
 \qquad z\in\mathbb R.                            \tag{SE12.13}
\]
Half the node displacement therefore encloses the point-to-node
change. Independent controls use direct j_1,j_3 trigonometric
formulas through z=192, a deliberately wide node interval, and
the whole-vector identity
\[
 \sum_{n\ {m odd}}(2n+1)j_n(z)^2
           =\frac12\left(1-\frac{\sin(2z)}{2z}\right).
                                                        \tag{SE12.14}
\]
Its unretained terms are bounded by the same complete factorial
tail below. Exact rational Taylor remainders enclose the independent
sines and cosines; no library eigensolver or special function is trusted.

## 5. Quadrature, the finite sign and the entire infinite complement

Use Gauss-24 on 768 width-half panels. The inherited root brackets
and all degree-47 moments are checked. For rho=4 each ellipse has
semimajor 17/32 and semiminor 15/32. Thus |Im(t/C)|<3/8 and |t|<385.
The analytic continuation of G is the symmetric digamma sum from
SE7. With beta_k=2k+1/2, its inherited majorant gives
\[
 M_s=\frac{269}{50}+34\sum_{k<400}\frac1{\beta_k}
 +\frac83\,385^2[(1601/2)^{-3}+\tfrac14(1601/2)^{-2}]
 +11+\frac35<200.                                  \tag{SE12.15}
\]
For the final term before b, all cosine frequencies are at most one;
their total modulus is below (22/5+1)exp(15/32)<11. The marker is
included in this bound. As |v_n v_m|<2 and pi>3, M=256 bounds the
matrix integrands after division by pi. The SE7 Chebyshev remainder
argument therefore supplies, per entry,
\[
 \epsilon_Q=4\cdot384\cdot256\frac{4^{-48}}{1-1/4}
           =\frac1{151115727451828646838272}.         \tag{SE12.16}
\]
Signed node measures are assembled with SE11's exact integer sums
and its dimension-independent rank-one operator error. Pole
intervals and forty-significant-digit archive rounding receive a
separate symmetric row-sum bound. Total leading-matrix error is
below 1.112e-21, including node error below 1.303e-25 and
pole/archive error below 1.265e-39. This is less than 10^(-15).

For the same head projection, the first discarded odd order is 337.
Rodrigues' bound and the geometric ratio of consecutive odd orders give
\[
 a_f=\frac{192^{337}/673!!}{1-192^2/(675\cdot677)},
 \qquad
 a_h=\frac{4(C/4)^{337}/673!!}{1-(C/4)^2/(675\cdot677)}.
                                                        \tag{SE12.17}
\]
The first bounds the full discarded Fourier vector; the second
bounds the full discarded pole vector, including its scale factor.
Use the sufficient head bound sqrt(168)<13 and pole norm below one.
For the infinite diagonal and mixed blocks,
\[
 \begin{split}
 D&\succeq(b-\tau_D)I,
 &\tau_D&=\frac{384\cdot256}{3}a_f^2+2a_h^2<10^{-60},\\
 \|B_{\rm mix}\|&\le\tau_B,
 &\tau_B&=\frac{384\cdot256\cdot13}{3}a_f+2a_h<10^{-28}.
 \end{split}                                       \tag{SE12.18}
\]
These deliberately conservative bounds retain every discarded mode
and the full coupling, using the same projection as the finite head.

All 168 pivots of the archived rational candidate minus
4*10^(-15)I are certified by outward interval LDL. Subtracting the
total leading error yields A>=3*10^(-15)I. The complete comparison
therefore satisfies
\[
 K_{C,384}^{1,3/5}\succeq
 [\min(3\cdot10^{-15},b-\tau_D)-\tau_B]I
 \succ2\cdot10^{-15}I.                             \tag{SE12.19}
\]
Equations (SE12.2), (SE12.4) and the all-frequency condition now
transfer this sign to the unchanged full source. See the
[matrix](../../../proof_lab/ENDPOINT_SUPPORT_MARKER_MATRIX.json),
[complete result](../../../proof_lab/ENDPOINT_SUPPORT_MARKER_RESULT.json)
and [audit](SE12_SCOPE.md) for the enclosed errors and all pivots.

## 6. Native observer return and what remains open

At A=161/200 the replay verifies
\[
 e^{3A}<45/4,\quad2m_\Gamma<11,\quad p_A<22/5,
 \quad2(\sinh A-A)<1/5,
 \quad C_A<557/20.                                 \tag{SE12.20}
\]
SE6's native graph return consequently gives
\[
 \|f\|_X^2\le s[f]+(557/20)\|Rf\|_2^2
       \le13925000000000001\,s[f].                 \tag{SE12.21}
\]
The inherited N_*<=11I/2 and actual joint target then imply
\[
 \|\mathcal L_*f\|^2\le
 \left(1-\frac2{153175000000000011}\right)
       \|A_*f\|^2,\qquad f\in X_{161/200}.          \tag{SE12.22}
\]
The exact local observer A_*f -> L_*f is well defined and extends
as in SE9. Native inclusion covers every smaller aperture, including
the prime-5 activation itself; no interpolation of sampled matrix
signs is used. On shared vectors the local observers have the same
prescribed target.

The certificate reaches radius 0.805. The next event is prime 7 at
radius log(7)/2. Neither this finite extension nor the smaller
sufficient lower floor measures the distance to global stabilization.
No monotone improvement for arbitrary markers, automatic selection
rule or universal termination bound is proved. Cofinal source signs,
the global eta=0 sign, historical five-label endpoint, K0 and RH remain
open. SE4's obstruction to a strict uniform global reserve still holds.
Formal proof-assistant verification and external review are not claimed.

See [sources and novelty boundary](SE12_SOURCE_RECORD.md),
[verification scope](SE12_SCOPE.md) and [pins](SE12_SOURCE_PINS.json).
