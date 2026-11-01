# SE15: effective localization and a global positive-eta certificate

12 October 2026. Owner: Monty.

The complete corrected odd source has an executed global certificate
at eta=326/369, including zero negative count and zero nullity. An
explicit localization theorem also turns each smaller positive eta
into a finite-aperture source obligation. Those larger-aperture signs
have not been executed. The positive local frontier remains 21/25;
the eta-zero sign, global contractivity and RH remain open.

## 1. Native source, representations and the invariant

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede representations. This note retains the corrected T40
source in the admitted T35 graph adapter of SE4--SE5. It does not
replace the native pairing by an unexplained classical metric.
In that adapter, on the complex odd carrier X, write
\[
 m(x)=e^{-3|x|/2},\quad Rf=mf=g,\quad d\mu=d\xi/(2\pi),
 \quad \|f\|_X^2=\|f\|_2^2+\int(1+|G|)|\widehat g|^2d\mu,
 \qquad G(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi.       \tag{SE15.1}
\]
The native inclusion into the displayed L2 representation is iota.
The same complete source, with its actual pole and prime signs, is
\[
 s[f]=\langle f,S_bf\rangle_X
 =\int G|\widehat g|^2d\mu
  -2\Re\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                   \langle g,T_{\log n}g\rangle_2
  -2\left|\int g(x)\sinh(x/2)dx\right|^2.          \tag{SE15.2}
\]
Here T_t g(x)=g(x-t). Oddness identifies the last expression with
SE6's completion term. It is not an additional boundary assumption.
Set m_Gamma=-G(0) and p=sum Lambda(n)/n^2. The prime mismatch
factorization of SE4 gives, with P denoting the paired prime term,
\[
 G\ge-m_\Gamma,\qquad
 |P[f]|\le p\|Bf\|_2^2
          =p\int(1+m^4)|f|^2dx.                   \tag{SE15.3}
\]
Indeed the self-adjoint two-sheet prime operator has norm at most p,
and Bf=sqrt(2 cosh(3x)) mf. This bound includes every prime power.

Use SE13's actual invariant kappa_eta=N_-(S_b+eta I_X), finite for
eta>0 by SE5. Negative count means the maximal dimension of a strictly
negative subspace, with multiplicities. It is not the ordinary index
of a self-adjoint operator. All comparisons below are on this source.

## 2. Two complete scalar bounds

**Theorem (weighted pole bound).** For every f in X, with u=m^2,
\[
 2\left|\int mf\sinh(x/2)dx\right|^2
 \le (\log3-1)\int(1-u)|f|^2dx,
 \qquad 0<\log3-1<1/10.                           \tag{SE15.4}
\]
Proof. Put v=m sinh(x/2). Weighted Cauchy--Schwarz applies because
v/sqrt(1-u) is square integrable; the value at x=0 is immaterial.
Its full constant, with z=e^{-x} on the positive half-line, is
\[
 2\int_{\mathbb R}\frac{|v|^2}{1-u}dx
 =4\int_0^\infty\frac{e^{-3x}\sinh^2(x/2)}{1-e^{-3x}}dx
 =\int_0^1\frac{z(1-z)}{1+z+z^2}dz
 =\log3-1.                                       \tag{SE15.5}
\]
The last integrand is -1+(2z+1)/(1+z+z^2). The rational outward
logarithm enclosure proves the stated strict upper bound. QED.

**Theorem (complete prime-mass enclosure).** The independently
replayed scalar certificate gives
\[
 0<p<57/100,\qquad m_\Gamma<269/50.               \tag{SE15.6}
\]
Proof. The Gamma bound is the unchanged SE11 refined constant.
For the prime mass, absolute convergence at s=2 permits the Euler
product and differentiation of the alternating Dirichlet series.
With E=sum (-1)^(n-1)/n^2 and D=sum (-1)^(n-1)log(n)/n^2,
\[
 E=\tfrac12\zeta(2)>0,\qquad
 p=-\frac{\zeta'(2)}{\zeta(2)}=\log2+\frac DE.     \tag{SE15.7}
\]
For an even N, E lies between E_N and E_N+1/(N+1)^2. Likewise D lies
between D_N and D_N+log(N+1)/(N+1)^2, since log(x)/x^2 decreases for
x>=2. At N=1024, outward interval sums and division yield a complete
enclosure strictly below 57/100. Binary reduction n=2^k y, 1<=y<2,
uses only the pinned positive-logarithm series. No zero locations or
analytic continuation are inputs. QED.

## 3. A global count that is actually certified

**Theorem (global positive-eta zero obstruction).** Let
\[
 g_c=269/50,\quad p_c=57/100,\quad b_c=1/10,
 \qquad \eta_*:=\frac{g_c+2p_c}{g_c+2}
                    =\frac{326}{369}.             \tag{SE15.8}
\]
Then, on the entire complex odd native carrier,
\[
 S_b+\eta_* I_X\succeq
 \frac{7877}{36900}\,\iota^\dagger M_{1-m^2}\iota\succeq0.
 \quad \kappa_\eta=0,\quad\ker(S_b+\eta I_X)=\{0\}
 \quad(\eta\ge\eta_*).                            \tag{SE15.9}
\]
Proof. For 0<eta<1 the scalar inequality
G+eta(1+|G|)>=eta-(1-eta)g_c+(1+eta)G_+ holds pointwise.
Use (SE15.3)--(SE15.6), Parseval, and discard only the nonnegative
G_+ integral. At eta=eta_* the remaining multiplier is exactly
\[
 \begin{split}
 s[f]+\eta_*\|f\|_X^2
 &\ge\int\{\eta_*+[\eta_*-(1-\eta_*)g_c]u
                 -p_c(1+u^2)-b_c(1-u)\}|f|^2dx\\
 &=\int(1-u)(\eta_*-p_c-b_c+p_cu)|f|^2dx.
 \end{split}                                      \tag{SE15.10}
\]
The factorization uses 2 eta_*-(1-eta_*)g_c-2p_c=0. Its remaining
coefficient eta_*-p_c-b_c=7877/36900 is positive. Since 1-u>0 almost
everywhere and iota is injective, every nonzero f gives a strictly
positive right side. This proves both count and nullity assertions
at eta_*. Increasing eta preserves them. QED.

This proves S_b>=-(326/369)I_X, not S_b>=0. The displayed weighted
reserve is not asserted to dominate a fixed positive multiple of I_X.
Eta is a native spectral shift; it is not an aperture radius or a
percentage of progress. A sufficiently large positive shift alone is
not the cofinal eta-zero condition required by SE13.

## 4. An exact source localization identity

**Theorem (Gamma jump representation).** With
w(t)=e^{-t/2}/(1-e^{-2t}), t>0,
\[
 G(\xi)+m_\Gamma
 =2\int_0^\infty w(t)(1-\cos(\xi t))dt,
 \quad \int(G+m_\Gamma)|\widehat g|^2d\mu
 =\int_0^\infty w(t)\|g-T_tg\|_2^2dt.             \tag{SE15.11}
\]
Proof. In SE5's digamma series put beta_k=2k+1/2. Each summand is
2[1/beta_k-beta_k/(beta_k^2+xi^2)], the Laplace integral of
2e^{-beta_k t}(1-cos(xi t)). Sum nonnegative integrands, then use
Parseval and Tonelli. QED.

Let M>=2 be an integer and rho=log M. Define an even angle phi to be
zero for |x|<=rho, pi(|x|-rho)/2 for rho<|x|<rho+1, and pi/2 beyond.
Write chi=cos(phi), theta=sin(phi), U=(chi,theta). Then
\[
 \chi^2+\theta^2=1,\quad
 D(x,y):=|U(x)-U(y)|^2
 \le\min\{(\pi/2)^2|x-y|^2,2\}.                 \tag{SE15.12}
\]
The two functions are even, real and nonnegative, so they preserve
oddness and complex linearity. D=0 when both points are in |x|<=rho.
Chi f belongs to X_(rho+1); theta f is supported in |x|>=rho.

For completeness these are bounded native-domain maps. For any bounded
Lipschitz multiplier h, expanding h g-T_t(h g) bounds its squared
jump norm by twice the original jump energy times ||h||_infinity^2
plus 2||g||_2^2 integral w(t) min(L^2 t^2,4||h||_infinity^2)dt.
This integral is finite. The jump graph is equivalent to the graph
in (SE15.1), since G is bounded below. SE10's full local-domain/core
theorem therefore places the compactly supported chi f in X_(rho+1).
No native isometry of this partition is assumed: only its L2 identity
||chi f||_2^2+||theta f||_2^2=||f||_2^2 is used below.

**Theorem (complete signed localization).** For every f in X,
\[
 s[f]=s[\chi f]+s[\theta f]-\mathcal R_M[f],
 \qquad\mathcal R_M=\mathcal R_\Gamma+\mathcal R_P+\mathcal R_F,
                                                               \tag{SE15.13}
\]
where, using v=m sinh(x/2),
\[
 \begin{split}
 \mathcal R_\Gamma[f]
 &=\int_0^\infty w(t)\int D(x,x-t)
                   \Re(\overline{g(x)}g(x-t))dxdt,\\
 \mathcal R_P[f]
 &=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
        \int D(x,x-\log n)\Re(\overline{g(x)}g(x-\log n))dx,\\
 \mathcal R_F[f]
 &=\iint v(x)v(y)D(x,y)\Re(\overline{f(x)}f(y))dxdy.
 \end{split}                                                    \tag{SE15.14}
\]
Proof. For each pair x,y the sum of localized squared jumps equals
the original squared jump plus D(x,y)Re(conj(g(x))g(y)). The local
L2 term -m_Gamma||g||^2 splits exactly. In the prime term the
localized overlap has factor U(x) dot U(y)=1-D(x,y)/2, so its full
coefficient -2 leaves precisely -R_P. Expanding the full squared
pole functional gives -R_F, including both orders of x,y. The bounds
below prove absolute integrability of every remainder and continuity
in ||f||_2. First prove on the core, then extend in X. QED.

This is a source-specific IMS-type identity. The individual remainders
are signed; cross terms have not been declared positive or discarded.
The general localization method is classical, as recorded in the
source note. Its fractional-Laplacian formula is not substituted for
the actual Gamma, prime or pole operators here.

## 5. Complete and explicit remainder estimates

**Theorem (localization error).** With rho=log M,
\[
 |\mathcal R_M[f]|\le E_M\|f\|_2^2,\qquad
 E_M=\frac{83/2+\rho}{M^2}
            +\frac{3\rho+5/2}{M}+\frac1{M-1}.     \tag{SE15.15}
\]
Proof. If D(x,y) is nonzero, max(|x|,|y|)>rho. For t=|x-y|,
\[
 |x|+|y|\ge\max\{t,2\rho-t\},\qquad
 m(x)m(y)\le e^{-(3/2)\max\{t,2\rho-t\}}.        \tag{SE15.16}
\]
Also integral |f(x)f(x-t)|dx<=||f||_2^2.
For the Gamma remainder split t at rho/2. Below it the weight product
is at most e^{-9rho/4}, and D<=(pi/2)^2 t^2. Above it use D<=2
and the product bound e^{-3t/2}. Termwise integration and a decreasing
sum remainder give
\[
 \int_0^\infty t^2w(t)dt
 =\sum_{k\ge0}\frac2{(2k+1/2)^3}
 \le16+16/125+2/25=2026/125,
 \qquad (2026/125)(11/7)^2<41.                    \tag{SE15.17}
\]
Here 2/25 is the integral from k=1 to infinity bounding the terms
with integer k>=2. Since pi<22/7, M^(-9/4)<=M^(-2), and
2 integral_(rho/2)^infinity e^(-2t)/(1-e^(-2t))dt
=-log(1-1/M)<=1/(M-1), the Gamma budget is 41/M^2+1/(M-1).

For the primes, split at n=M in (SE15.16). The complete bound is
\[
 |\mathcal R_P[f]|/\|f\|_2^2
 \le2M^{-3}\sum_{n\le M}\Lambda(n)n
       +2\sum_{n>M}\frac{\Lambda(n)}{n^2}
 \le\frac{3\rho+2}{M}+\frac\rho{M^2}.             \tag{SE15.18}
\]
Indeed Lambda(n)<=log n, sum_(n<=M)n<=M(M+1)/2, and the complete
tail is at most (log M+1)/M by the decreasing integral test for M>=2.

For the pole put B_0=2||v||^2 and B_rho=2||1_(|x|>=rho)v||^2.
Exact integration gives
\[
 B_0=1/12,\qquad
 B_\rho=\tfrac12 M^{-2}-\tfrac23 M^{-3}+\tfrac14 M^{-4}
           \le\tfrac12 M^{-2}.                    \tag{SE15.19}
\]
Write F=2v tensor v. The difference F-chi F chi is the sum of two
rank-one terms using v-chi v, whose squared norm is at most B_rho/2.
Moreover ||theta v||^2<=B_rho/2. Consequently
||F-chi F chi-theta F theta||<=2 sqrt(B_0 B_rho)+B_rho
<=1/(2M)+1/(2M^2), because 1/sqrt(6)<1/2. Adding the three budgets
gives (SE15.15). QED.

**Theorem (exterior source bound).** Every h in X supported in
|x|>=rho obeys
\[
 s[h]\ge-d_M\|h\|_2^2,\qquad
 d_M=\frac{163}{25M^3}+\frac{4\rho+5/2}{M^2}.       \tag{SE15.20}
\]
Proof. The Gamma negative part is bounded by g_c M^(-3)||h||_2^2.
For a shift 0<=t<=2rho, two exterior points with opposite signs
cannot overlap except at a measure-zero endpoint. Points on the same
side satisfy |x|+|x-t|>=2rho+t. Thus the weighted exterior shift norm
is at most M^(-3)e^(-3t/2). For t>2rho use e^(-3t/2).
Splitting the actual prime sum at n=M^2 bounds its absolute value by
[2p_c M^(-3)+2(2rho+1)/M^2]||h||_2^2. The entire pole is bounded
by B_rho||h||_2^2<=||h||_2^2/(2M^2). Now g_c+2p_c=163/25. QED.

Neither theorem cuts off prime powers or frequencies without a bound.
The pole tail here is a full rank-one functional norm, not a list
of sampled observations.

## 6. Effective local-to-global inertia transfer

For finite A and r>=0 define the auxiliary local negative count
\[
 \nu_r(A)=N_-\bigl(s[h]+r\|Rh\|_2^2;\ h\in X_A\bigr).
                                                               \tag{SE15.21}
\]
This is a physical-source tolerance, represented natively by
r R^dagger R. It is not kappa_r(A), whose shift is r I_(X_A).
At fixed A the count is finite: in the physical g chart the prime
and pole terms are L2-bounded, with only finitely many active prime
shifts. Unit vectors in a negative subspace have uniformly bounded
positive Gamma energy. As G(xi) tends to infinity, their frequency
tails vanish uniformly. Fixed support and compactness of a bounded
band transform then make these vectors L2-precompact, excluding an
infinite orthonormal family. This is the SE10 local compactness argument.

**Theorem (effective invariant bracket).** If A>=log M+1 and
eta>=E_M+max(r,d_M), then
\[
 \kappa_\eta(A)\le\kappa_\eta\le\nu_r(A).
                                                               \tag{SE15.22}
\]
In particular a certificate s[h]>=-r||Rh||_2^2 on X_A proves
\[
 S_b\succeq-[E_M+\max(r,d_M)]I_X,
 \qquad\kappa_\eta=0
 \quad\text{for }\eta\ge E_M+\max(r,d_M).         \tag{SE15.23}
\]
Proof. The lower count inequality is restriction to the native
subspace, as in SE13. For the upper one use (SE15.13), (SE15.15),
(SE15.20), and the exact L2 partition identity. Writing
||Cf||^2=||f||_X^2-||f||_2^2, which is nonnegative, gives
\[
 \begin{split}
 s[f]+\eta\|f\|_X^2
 &\ge s[\chi f]+(\eta-E_M)\|\chi f\|_2^2
              +(\eta-E_M-d_M)\|\theta f\|_2^2+\eta\|Cf\|^2\\
 &\ge s[\chi f]+r\|R\chi f\|_2^2.
 \end{split}                                                    \tag{SE15.24}
\]
Here ||R chi f||<=||chi f|| and all omitted terms are nonnegative.
On any strictly negative subspace of S_b+eta I, multiplication by
chi is injective: a zero image would contradict (SE15.24). Its image
is a negative subspace of the local form. This proves the upper
inertia bound. If that local form is nonnegative, (SE15.24) proves
the global lower bound and zero negative count. No zero-nullity claim
follows from this non-strict local hypothesis alone. QED.

The cut is a proof device that supplies an injection, not a frozen
physical observer. Under a faithful change of observer coordinates
the source, cut maps, Gram metric and tolerance form are transported
together. Their counts and form inequalities persist. Moving the
physical center without transporting the source is not asserted to
be a symmetry. Changing a local sign convention cannot remove any
of the signed remainders in (SE15.14).

## 7. An explicit schedule toward eta zero

**Theorem (rational aperture schedule).** For every desired eta>0,
choose the first integer k>=1 satisfying
\[
 \frac{4k+29}{2^k}\le\frac\eta2,
 \qquad M=2^k,\quad \widehat A=1+7k/10,\quad r=\eta/2.
                                                               \tag{SE15.25}
\]
A full local certificate s[h]>=-(eta/2)||Rh||_2^2 on X_(Ahat)
then proves kappa_eta=0 on the entire native source.

Proof. Adding the error and exterior budgets gives
\[
 \varepsilon_M:=E_M+d_M
 =\frac{163}{25M^3}+\frac{44+5\log M}{M^2}
       +\frac{3\log M+5/2}{M}+\frac1{M-1}
 \le\frac{4k+29}{2^k}\quad(M=2^k,k\ge1).          \tag{SE15.26}
\]
To verify the last inequality, use log2<7/10 and multiply by M.
The four terms are bounded respectively by 163/100, 22+7k/4,
21k/10+5/2 and 2. Their sum is 28.13+3.85k<29+4k.
The majorant tends to zero, so the first k exists. Also
Ahat>=log M+1 and E_M+max(r,d_M)<=epsilon_M+r<=eta.
Apply (SE15.23). QED.

For any sequence eta_j decreasing to zero, supplying every scheduled
local certificate proves S_b>=0 by passage to the limit in its bounded
quadratic form. Conversely S_b>=0 makes each scheduled local form
strictly positive in its physical metric after adding eta_j/2; SE10's
local comparison completeness then supplies a finite certificate for
each one. This equivalence gives neither their signs in advance nor
a uniform bound on the numerical work to certify them.

The executable record prints schedules for eta=1/2, 1/4, 1/10, 1/100
and 1/1000. Every row is labelled CONDITIONAL_LOCAL_OBLIGATION and
local_certificate_executed=false. They are not five additional global
zero counts. The table's tail computations pass independently of the
missing local source signs. The currently executed positive-aperture
certificate remains SE14's radius 21/25, which is much smaller than
the apertures required by this conservative schedule.

## 8. What is established and what remains

The executed result is a whole-source positive-eta bound with a
nonzero weighted reserve. The new written results supply an exact
localization identity and a computable sufficient aperture and local
tolerance for any smaller positive eta. They quantify one route from
local source certificates to the global invariant; they do not prove
that the required local signs hold.

SE5's essential spectrum at zero and SE13's non-Fredholm zero-threshold
boundary remain intact. The native global critical observer inequality,
historical five-label endpoint, K0 and RH are not closed. No new
Atiyah--Singer elliptic adapter, universal marker optimizer, formal
proof-assistant verification or external review is asserted.

See the [replay](../../../proof_lab/endpoint_global_eta_certificate.py),
[result](../../../proof_lab/ENDPOINT_GLOBAL_ETA_RESULT.json),
[independent controls](../../../proof_lab/test_endpoint_global_eta_certificate.py),
[sources](SE15_SOURCE_RECORD.md), [audit](SE15_SCOPE.md), and
[source pins](SE15_SOURCE_PINS.json).
