# SE20: exact prime--Gamma cancellation at zero shift

12 October 2026. Owner: Monty. Written development.

The selected endpoint route is to retain and cancel the complete prime
return, pole and Gamma contributions before estimating the arithmetic
fluctuation. It works directly with the unshifted source. The earlier
positive-eta certificates remain valid, but decreasing their decimal
anchors is no longer the main endpoint strategy.

This note proves two obstructions to shortcuts and an exact replacement
identity. The SE19 diagonal seed, with its fixed Gamma reading, cannot
remain nonnegative for eta<=1/14 for any admissible continuous even prime
weight. Also, every fixed prime cutoff with the full pole left in place
has a negative escaping packet. Neither obstruction is a negative
witness for the complete source.

The replacement cancels an explicit continuous prime reference and the
pole against Gamma kernels. At cancellation depth 16 the remaining
reference energy has a proved physical multiplier floor greater than
8/5, without adding eta I_X. The complete source is exactly this energy
minus a specified signed prime-fluctuation form. Bounding that form by
the reference energy would prove the eta-zero sign. **That last
arithmetic bound is not proved here. Eta zero and RH remain open.**

## 1. Same native source and faithful half-line reading

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the admitted representation. Use the corrected T40 source
and T35 native graph of SE4--SE19, unchanged:
\[
 s[f]=\Gamma[f]-P[f]-F[f],\quad g=mf,\quad m(x)=e^{-3|x|/2},
 \quad G(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi,
\]
\[
 \Gamma[f]=\int G|\widehat g|^2\,d\xi/(2\pi),\qquad
 \|f\|_X^2=\|f\|_2^2+\int(1+|G|)|\widehat g|^2\,d\xi/(2\pi).
                                                               \tag{SE20.1}
\]
For odd f put h(x)=sqrt(2)f(x), x>0. This is an L2 isometry, with
the native graph domain and pairing still attached. Set
\[
 a[h]=\int_0^\infty e^{-x}h(x)dx,\quad
 b[h]=\int_0^\infty e^{-2x}h(x)dx,\qquad
                         F[f]=|a[h]-b[h]|^2.     \tag{SE20.2}
\]
The symbols a[h], b[h] in this note denote two scalar functionals;
they are not the native source operator or the boundary-label space.
Let psi(u)=sum_(n<=u) Lambda(n). Its measure dpsi consists of all
prime-power atoms. No prime-density asymptotic is assumed below.

## 2. A proved floor for the old diagonal-seed route

**Theorem 1 (changing the prime weight cannot reach zero in that seed).**
Keep SE17's sixteen-mode L_Gamma. Let q be a positive continuous even
prime weight whose row V_q is finite and continuous near x=0 and
x=log2. If
\[
 \eta(1+e^{-3x})+(1-\eta)L_\Gamma(e^{-x/2})-V_q(x)\ge0
                                                               \tag{SE20.3}
\]
almost everywhere, with 0<=eta<1, then eta>1/14. In particular the
positive seed required by SE19 cannot be continued to zero with this
Gamma row merely by choosing better such prime weights.

**Proof.** The n=2 event and its return give
V_q(0)V_q(log2)>=2(log2)^2/2^4>(1/18), using log2>2/3.
This is SE18's translate-charging argument with evenness explicit.
The exact rational Gamma value is
L_Gamma(1)=1907/44850, between 0 and 1/20. By SE19.A2,
L_Gamma(z)<=(81/50)z^6. If eta<=1/14, the right-hand budgets at the
two points obey
\[
 d_0\le2\eta+\tfrac1{20}\le\tfrac{27}{140},\quad
 d_2\le\tfrac98\eta+\tfrac{81}{400}\le\tfrac{99}{350},\quad
 d_0d_2\le\tfrac{2673}{49000}<\tfrac1{18}.        \tag{SE20.4}
\]
Here the estimate for d_2 uses 0<=1-eta<=1 and the nonnegative
upper bound 81/400; it does not assume L_Gamma itself is positive.
Continuity turns the almost-everywhere inequality into the same
inequalities at the two points. Multiplication contradicts the event
lower bound. Finally log2=2 sum_(j>=0)(1/3)^(2j+1)/(2j+1)>2/3.
QED.

The rational 1/14 is a proved obstruction, not the optimal floor.
This theorem does not rule out other Gamma analyses or full nonlocal
operator seeds. It identifies why the selected diagonal route is an
unsuitable main strategy for the requested endpoint.

## 3. All prime events as one signed form

For a real signed measure nu on (1,infinity) with
int u^(-2)|dnu(u)|<infinity, define
\[
 \begin{split}
 H_h(t)&=\int_0^t\overline{h(x)}h(t-x)dx\in\mathbb R,\\
 C_h(t)&=2\Re\int_0^\infty e^{-3x}\overline{h(x+t)}h(x)dx-H_h(t),\\
 \mathcal P_\nu[h]&=\int_1^\infty u^{-2}C_h(\log u)\,d\nu(u).
 \end{split}                                                   \tag{SE20.5}
\]
H_h is real by interchanging x and t-x. Both integrals are continuous
in t for h in L2, using zero extension where necessary. Moreover
|C_h(t)|<=3||h||_2^2, so
\[
       |\mathcal P_\nu[h]|
       \le3\|h\|_2^2\int_1^\infty u^{-2}|d\nu(u)|.             \tag{SE20.6}
\]
This defines a bounded self-adjoint form on the half-line by
polarization; it need not be positive.

**Theorem 2 (complete same-side and return identity).** The actual
prime form is P[f]=P_(dpsi)[h].

**Proof.** For t>0 split the full odd pairing <g,T_t g> into x>t,
x<0 and 0<x<t. The first two pieces give the real same-side overlap.
The third is minus one half of the reflected overlap. Multiplying by
2 Lambda(n)/sqrt(n), and using m(x)m(x+t)=e^(-3x)n^(-3/2) and
m(x)m(t-x)=n^(-3/2), gives exactly Lambda(n)n^(-2)C_h(log n).
All atoms are included. Absolute convergence follows from
sum Lambda(n)/n^2<infinity and (SE20.6). QED.

The reflection is a signed cross-pairing. It must not be assigned a
positive sign just because its measure has positive atoms.

## 4. The continuous return cancels the complete pole

For beta>0 write K_beta^- for the SE16--SE17 half-line operator
with kernel
\[
 k_\beta^-(x,y)=m(x)m(y)
       \{e^{-\beta|x-y|}-e^{-\beta(x+y)}\}.        \tag{SE20.7}
\]

**Theorem 3 (pole--reference cancellation).** With du denoting
Lebesgue measure on (1,infinity),
\[
          \boxed{\mathcal P_{du}[h]+F[f]
                         =-\langle h,K_{1/2}^-h\rangle.}
                                                               \tag{SE20.8}
\]
Furthermore, for every s>1/2,
\[
       \mathcal P_{u^{-s}du}[h]
                         =\langle h,K_{s-1/2}^-h\rangle\ge0.
                                                               \tag{SE20.9}
\]

**Proof.** Substitute u=e^t in (SE20.5). The continuous same-side
kernel is e^(-max(x,y)-2min(x,y)), while its return kernel is
e^(-x-y). Add the pole kernel
(e^(-x)-e^(-2x))(e^(-y)-e^(-2y)). The sum is
-e^(-2max(x,y)-min(x,y))+e^(-2x-2y), which is -k_(1/2)^-.
For u^(-s)du the same-side kernel becomes
e^(-(s+1)max(x,y)+(s-2)min(x,y)), and the return kernel becomes
e^(-(s+1)(x+y)). Their difference is (SE20.7) with beta=s-1/2.

Positivity, including all complex cross terms, follows from
\[
 \langle h,K_\beta^-h\rangle
  =2\beta\int_0^\infty e^{2\beta t}
       \left|\int_t^\infty e^{-(3/2+\beta)x}h(x)dx\right|^2dt.
                                                               \tag{SE20.10}
\]
Expanding this square gives
2 beta int_0^min(x,y) exp(2 beta t)dt times
exp(-(3/2+beta)(x+y)), exactly the kernel above. Initially use
compact smooth h; bounded kernels and (SE20.6) extend the identities
to H. QED.

For beta=1/2 the positive term is
int_0^infinity e^t |int_t^infinity e^(-2x)h(x)dx|^2dt.
Thus the leading return and pole form one exact positive kernel after
the reference is included. No approximation psi(u)~u was used.

## 5. Match a finite set of Gamma modes before taking any bound

For an integer J>=1 put beta_k=2k+1/2,
C_J=sum_(k<J)2/beta_k and define the signed reference and remainder
measures
\[
 d\omega_J(u)=\left(1-\sum_{k=1}^{J-1}u^{-(2k+1)}\right)du,
 \qquad d\mu_J=d\psi-d\omega_J.                  \tag{SE20.11}
\]
These are explicit finite reference densities, not assumptions about
the distribution of primes. Their u^(-2)-weighted total variation is
finite. The actual all-prime measure is exactly dpsi=domega_J+dmu_J.

**Theorem 4 (positive reference energy at eta zero).** Set
\[
 \begin{split}
 \mathcal A_J[f]
   &=\Gamma[f]+\sum_{k<J}\langle h,K_{\beta_k}^-h\rangle\\
   &=\int a_J(\xi)|\widehat{mf}(\xi)|^2d\xi/(2\pi),\\
 a_J(\xi)
   &=G(\xi)+\sum_{k<J}\frac{2\beta_k}{\beta_k^2+\xi^2}
     =C_J-m_\Gamma+
       \sum_{k\ge J}\frac{2\xi^2}{\beta_k(\beta_k^2+\xi^2)}.
 \end{split}                                                   \tag{SE20.12}
\]
Then the complete unshifted source satisfies
\[
             \boxed{s[f]=\mathcal A_J[f]-\mathcal P_{\mu_J}[h].}
                                                               \tag{SE20.13}
\]
For J=4 and J=16 respectively, inherited exact constants give
\[
 a_4(\xi)>\frac{1007}{5850}>0,\qquad
 a_{16}(\xi)>\frac85>0.                         \tag{SE20.14}
\]
In particular A_16[f]>=(8/5)||mf||_2^2, and A_16[f]>0 for f!=0.
No positive multiple of the native identity I_X is asserted here.

**Proof.** Theorem 3 yields
P_(omega_J)[h]+F[f]=-sum_(k<J)<h,K_beta_k^-h>.
Insert P=P_(omega_J)+P_(mu_J) into the unchanged source. The
digamma series SE16.4 gives (SE20.12); its remaining terms are
nonnegative and converge in the inherited graph form. Now
C_4=3248/585 and C_4-269/50=1007/5850. The exact SE19.A2 value
of C_16 satisfies C_16-269/50>8/5, and m_Gamma<269/50. This proves
the floors. Rf=mf is injective, proving strict positivity of the
reference energy on nonzero f. Boundedness in X of every source and
finite kernel term extends the identity from the core to X. QED.

This is the replacement for the diagonal seed. Its positive reference
is a whole Fourier energy, with all the remaining Gamma modes retained.
The norm ||mf||_2 can tend to zero on native unit escaping packets,
so this physical floor does not contradict SE5's essential zero
threshold or supply a bounded inverse on X.

**Theorem 5 (reference depth moves both sides).**
\[
 \mathcal A_{J+1}-\mathcal A_J
   =\mathcal P_{\mu_{J+1}}-\mathcal P_{\mu_J}
   =\langle h,K_{\beta_J}^-h\rangle\ge0.          \tag{SE20.15}
\]
Thus the source and its invariant counts are unchanged when J moves.
For each nonzero vector with A_J[f]>0, the new ratio is
\[
 \frac{\mathcal P_{\mu_{J+1}}[h]}{\mathcal A_{J+1}[f]}
 =\frac{\mathcal A_J[f]}{\mathcal A_J[f]+k}
       \frac{\mathcal P_{\mu_J}[h]}{\mathcal A_J[f]}
   +\frac{k}{\mathcal A_J[f]+k},\quad
 k=\langle h,K_{\beta_J}^-h\rangle.              \tag{SE20.16}
\]
**Proof.** Subtract (SE20.11)--(SE20.12), apply (SE20.9), and divide
by the positive denominator. QED.

Increasing J can improve reference conditioning but cannot convert a
negative actual-source vector into a positive one: its ratio approaches
one from the same side. This keeps the comparison from manufacturing
progress by moving a reference without moving its target.

The endpoint obligation now has an exact arithmetic statement:
\[
 \boxed{S_b\succeq0\quad\Longleftrightarrow\quad
       \mathcal P_{\mu_{16}}[h]\le\mathcal A_{16}[f]
       \quad\text{for every odd }f\in X.}         \tag{SE20.17}
\]
It suffices to establish the inequality on the dense native core. This
equivalence is a consequence of the proved source identity, not proof
that its right side holds. Relative boundedness of the fluctuation in
the A_16 metric is not presumed, and no unbounded inverse is silently
treated as a bounded Birman--Schwinger operator.

## 6. Why a finite prime cutoff cannot finish the global zero sign

**Theorem 6 (negative escape for every uncompensated prime cutoff).**
Let P_M retain only n<=M, with M finite, while keeping the complete
Gamma and pole. Then s_M=Gamma-P_M-F has a negative odd smooth
compactly supported vector for every M. This is a statement about the
truncated source, not the actual complete source.

**Proof.** Choose a nonzero real nonnegative phi in C_c^infinity((0,ell)),
where 0<ell<log2, and set h_R(x)=phi(x-R), with f_R its odd extension
divided by sqrt(2). Choose 2R>log M. Same-side prime translations cannot
overlap because every log n>=log2>ell. Opposite-side returns require
log n in [2R,2R+2ell], absent from this cutoff. Thus P_M[f_R]=0.

Put alpha_phi=int e^(-y)phi(y)dy>0, beta_phi=int e^(-2y)phi(y)dy>0,
and rho(y)=e^(-3y/2)phi(y). Then
\[
 F[f_R]=(e^{-R}\alpha_\phi-e^{-2R}\beta_\phi)^2,
 \quad |\Gamma[f_R]|\le C_\phi e^{-3R},\quad
 C_\phi=m_\Gamma\|\rho\|_2^2+\tfrac{131}{8}\|\rho'\|_2^2.
                                                               \tag{SE20.18}
\]
The Gamma bound uses SE4.3: |G(xi)|<=m_Gamma+(131/8)xi^2, and
the two disjoint translated supports give the indicated L2 and
derivative norms exactly. For R large enough the pole is at least
(alpha_phi^2/4)e^(-2R), which exceeds C_phi e^(-3R). Hence
s_M[f_R]<0. QED.

This also applies if the continuous reference (SE20.11) is retained
exactly but the arithmetic atoms are cut off and the remaining signed
tail is set to zero: algebra then reconstructs exactly s_M. A valid
finite certificate therefore needs an analytic tail contract that
retains the return--pole cancellation; no number of fixed head primes
alone proves the unshifted global result.

## 7. A concrete arithmetic test at the escaping end

For the packets in Theorem 6 define
\[
 H_\phi(t)=\int\phi(y)\phi(t-y)dy,\quad
 \Delta_R=\int_1^\infty u^{-2}H_\phi(\log u-2R)
                                      (d\psi(u)-du).
                                                               \tag{SE20.19}
\]
Only prime powers in the moving interval [exp(2R),exp(2R+2ell)]
enter this integral. Its continuous part is exactly
exp(-2R) alpha_phi^2.

**Theorem 7 (exact return-deficit condition).** On this packet family,
\[
 s[f_R]=\Gamma[f_R]+\Delta_R
          +2e^{-3R}\alpha_\phi\beta_\phi-e^{-4R}\beta_\phi^2.
                                                               \tag{SE20.20}
\]
Consequently global source positivity requires the lower bound
Delta_R>=-Gamma[f_R]-2e^(-3R)alpha_phi beta_phi
+e^(-4R)beta_phi^2 for every R. Satisfying it on this family alone
would not prove positivity on all X.

**Proof.** All same-side prime terms vanish as above. The opposite
return is the prime integral in (SE20.19); its continuous part cancels
the leading term of (SE20.18). The remaining two pole terms give
(SE20.20). QED.

The scale of the unresolved arithmetic is visible without a numerical
experiment. Let E(u)=psi(u)-u. Integration by parts, whose endpoint
terms vanish for this compact packet, gives
\[
 \Delta_R=-\int_1^\infty E(u)u^{-3}
       \{H_\phi'(\log u-2R)-2H_\phi(\log u-2R)\}\,du.
                                                               \tag{SE20.21}
\]
If a supplied bound |E(u)|<=C u^theta holds over the moving interval,
then
\[
 |\Delta_R|\le C e^{-(4-2\theta)R}
       \int_0^{2\ell}e^{(\theta-2)t}|H_\phi'(t)-2H_\phi(t)|dt.
                                                               \tag{SE20.22}
\]
This is a conditional estimate, not an assertion of a new bound on psi.
The square-root exponent theta=1/2 aligns this magnitude estimate with
the e^(-3R) source scale, but does not by itself prove the required
sign or constants. A weaker o(u) error gives only o(e^(-2R)), which
does not settle that comparison. Signed smoothed cancellation could
be stronger than taking the absolute value in (SE20.22).

## 8. Decision and exact remaining work

The selected route is (SE20.13)--(SE20.17), with the complete signed
arithmetic fluctuation and the positive physical Gamma energy. It
removes the constant pole cost, the SE19 diagonal-seed floor, and the
temptation to read a finite prime head as the global zero source.
It keeps the observer's same-side and return readings connected.

The next mathematical obligation is an actual signed bound on
P_(mu_16), including the moving return intervals, or a source-faithful
recovery factorization that proves precisely the same inequality.
SE19's finite observation gains can be used inside such a construction
after its positive seed and event coupling are established. They are
not an automatic proof of the arithmetic condition.

No estimate establishing (SE20.17) for all f has been obtained in this
stage. The user's requested eta-zero result is therefore not complete.
The executed SE17 anchor 59/100 with floor 1/7380, its implied shift
10883/18450, and SE14's local radius 21/25 remain unchanged. Critical
global positivity, historical five-label attachment, K0 and RH stay
open. See [scope](SE20_SCOPE.md) and [sources](SE20_SOURCE_RECORD.md).
