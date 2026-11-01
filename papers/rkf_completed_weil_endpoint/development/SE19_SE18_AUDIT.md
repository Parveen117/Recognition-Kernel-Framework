# SE19 audit: corrections to SE18 before further endpoint development

12 October 2026. The reviewed SE18 commit is
`2d2809ae9fcc5c6463ff499dfaa52d63f34533e9` on
`agent/rh-source-energy-tail`. Its three development files remain
unchanged. This later note controls the corrected claims. No SE17
certificate, archive, source pin or earlier source identity is changed.

SE18's useful contribution is to separate the pole budget from the
Gamma/prime weights and identify the artificial constant-pole cost at
infinity. Its proposed hybrid proof and inferred numerical route floor
cannot be consumed as written. The next stage uses its pole idea with
the exact SE17 residuals; see the [SE19 theorem](SE19_RETAINED_RESIDUAL_POLE_RECOVERY.md).

## 1. Interval lower bounds do not prove anchor tightness

Write D(z)=1+z^6-L_Gamma(z) and eta_0=59/100. Whenever D>0,
\[
 \Phi(z)=\eta_0-\frac{Q_{\eta_0}(z)}{D(z)}.
                                                               \tag{SE19.A1}
\]
If Q>=l>=0 and D<=d on an entire cell, then
Phi<=eta_0-l/d on that cell. This is an **upper** enclosure of Phi,
not the lower enclosure asserted in SE18.3. An interval lower bound
can be small solely because of enclosure loss. It does not establish
a point where the true Q is small.

Consequently SE18's eta_pw>=0.58938, its claimed tightness within
0.0007, its reported maximizing locations, and its conclusion that
every further anchor needs new weights are withdrawn. No contrary
numerical value of the exact route floor is asserted here. A valid
lower floor needs a pointwise upper enclosure of Q (and compatible
enclosures of D), or a direct lower enclosure of Phi at a point.
SE17's original complete lower bounds on Q remain valid and untouched.

**Theorem A1 (the affine criterion has an elementary valid slope).**
For the actual sixteen-mode SE17 comparison,
\[
 C_{16}=\sum_{k=0}^{15}\frac4{4k+1}
       =\frac{168623511779891008}{24142663793423175}<7,
 \quad L_\Gamma\le(C_{16}-g_c)z^6\le\frac{81}{50}z^6,
 \quad D(z)\ge\frac{19}{50}>0.                  \tag{SE19.A2}
\]
**Proof.** Every H_beta^* is a row of a nonnegative kernel, hence is
nonnegative. Use SE17.6, g_c=269/50, the displayed exact rational sum,
and 0<=z<=1. In particular D>=1-(31/50)z^6>=19/50. QED.

Solving Q_eta=eta D+L_Gamma-V_alpha-b_c(1-z^6)>=0 therefore proves
SE18's affine half-line criterion for these weights, without a sampled
claim that L_Gamma attains its maximum at z=1. The supremum is to be
intersected with the stated 0<eta<1 range. The continuum maximum and
sign of L_Gamma are not certified by 1,000 sampled points.

## 2. Correct the auxiliary-row limit and the pole polynomial

SE18 Theorem 2 claims V_(7/2)->0. This is false. At t=n=2^k,
one term of SE17.8 alone gives
\[
 V_{7/2}(t^{-1/2})\ge t^{-3}\Lambda(n)n^{9/2}
                      =(\log2)n^{3/2}\longrightarrow\infty.
                                                               \tag{SE19.A3}
\]
SE17 explicitly allows that auxiliary row to be unbounded. The
correct argument uses positivity and the combined-weight estimate
0<=V_alpha<=V_(1/2)/(1-alpha). SE16.19 proves V_(1/2)->0; SE17.6
gives L_Gamma->0. Thus Q_eta(0)=eta-b_c is still valid for this
declared family. It is not asserted for every possible Gamma weight.

For the q_0 pole row tau_0=(4/15)(z-z^3), direct subtraction gives
\[
 30\{\tau_0-\tfrac1{10}(1-z^6)\}
                     =3z^6-8z^3+8z-3.          \tag{SE19.A4}
\]
The row exceeds the constant density where this polynomial is
**positive**, not negative as printed in SE18.9 and its direct-check
record. The correct algebraic inequality is the controlling statement;
the printed decimal roots and maximum are not needed or newly certified.

SE18.7's proof also needs int tau_q q^2=4<v,q>^2, not int tau_q q.
The reciprocal budget itself is correct on the full weighted L2 form
domain. When its necessity is claimed only from f in X, an appropriate
density hypothesis is needed; positive continuous tau, locally bounded
above and away from zero on (0,infinity), suffices by approximation on
compact subintervals and monotone exhaustion. The actual tau_0 and
constant-pole densities have that property. SE19 instead uses bounded
W>=w, for which domain density and continuity are explicit.

The factor 2 in SE18's translate-charging argument uses evenness of q.
Retain the positive **even** weight hypothesis from its Theorem 4 in
the subsequent statement as well. Its proof is then valid. No such
factor for an arbitrary non-even weight is inferred.

## 3. Preserve exterior decay with proved constants and monotonicity

The displayed equality (5/4)^(5/2)=1.746 in SE18.13 is not an outward
upper bound: (5/4)^5=3125/1024 > (873/500)^2. The continuum claim
L_Gamma<=0 on (0,1/2] also needs more than samples. Rather than rely
on those steps, the following sufficient exterior bound uses the
already proved denominator floor (SE19.A2).

**Theorem A2 (corrected exterior bound).** Let
\[
 C_\Gamma=\sum_{j\ge3}|a_j|2^{-(j-3)},\qquad
 L_\Gamma=A(z)/S_3(z),\quad A(z)=\sum_{j\ge3}a_jz^j.
\]
This is a finite exact rational constant from SE17.6. For A>=2 and
z_A=exp(-A/2), define
\[
 \begin{split}
 \Psi(z_A)=\frac{50}{19}\bigg[\frac{100}{47}
  \left\{\frac{32}{15}z_A\log(1/z_A)+\frac49z_A
          +4z_A^3\log(1/z_A)+\frac{29}{100}z_A^6\right\}
       +\frac4{15}z_A+C_\Gamma z_A^3\bigg].
 \end{split}                                                   \tag{SE19.A5}
\]
Using the admissible pole density tau_0, every f in X supported in
|x|>=A satisfies s[f]+eta||f||_X^2>=0 whenever
0<eta<1 and eta>=Psi(z_A). Moreover Psi(exp(-A/2))=O(A exp(-A/2)).

**Proof.** The integral-test proof of SE16.19 applies for t>=2:
sum_(n<=t)n^(3/2)<=(2/5)t^(5/2)+t^(3/2), and the decreasing tail
log(y)y^(-5/2) is bounded by its endpoint plus its integral.
Set t=z^(-2) and use p_(5/2)<29/100 from the existing certificate.
This bounds V_(1/2) by the expression in braces in (SE19.A5).
Also V_alpha<=100 V_(1/2)/47, tau_0<=4z/15 and
|L_Gamma|<=C_Gamma z^3 for z<=1/2. Divide the resulting nonnegative
numerator upper bound by D>=19/50.

All the displayed majorant terms increase with z on 0<z<=exp(-1):
the logarithmic derivatives are log(1/z)-1 and
z^2(3log(1/z)-1), respectively. Thus their supremum on z<=z_A is
their value at z_A. For eta>=Psi, eta D+L_Gamma-V_alpha-tau_0>=0
on the entire exterior. The SE17 identity with the exact admissible
pole residual proves the asserted form sign. The rate follows from
the explicit expression. QED.

This is a support-restricted native-shift estimate. It does not
supply the missing mixed terms of a local-to-global decomposition.
SE15 already provides a stronger-decaying exterior L2 estimate for
its own localization scheme; there is no reason to discard that result.

## 4. Local and exterior signs need their coupling budget

SE18 Theorem 6(i) does not follow from SE15. Two nonnegative diagonal
blocks can have a negative joined operator: the matrix
[[1,2],[2,1]] has eigenvalues 3 and -1. A maximum of the separate
thresholds does not bound their mixed block.

For SE15's actual smooth partition chi^2+theta^2=1, retain
\[
 s[f]=s[\chi f]+s[\theta f]-\mathcal R_M[f],\qquad
 |\mathcal R_M[f]|\le E_M\|f\|_2^2,              \tag{SE19.A6}
\]
where R_M contains the Gamma, prime and pole cross terms. The valid
already-proved conclusion is
\[
 A\ge\log M+1,\quad s[h]\ge-r\|Rh\|_2^2\ (h\in X_A),
 \quad\eta\ge E_M+\max\{r,d_M\}
 \quad\Longrightarrow\quad S_b+\eta I_X\succeq0. \tag{SE19.A7}
\]
E_M and d_M are the full expressions in SE15.15 and SE15.20. Its
local tolerance r R^dagger R is not the local native shift r I.
Its partition is an L2 identity, not a native graph isometry. If
native local shifts are used on both parts, their norm defect
||chi f||_X^2+||theta f||_X^2-||f||_X^2 must also be handled.
Neither defect is paid by substituting the exterior Phi into a max.

Accordingly SE18's per-aperture global conclusion is withdrawn and
replaced by (SE19.A7). SE15's rational schedule remains a valid
conditional construction, with its larger-aperture signs still open.

There is a useful separate qualitative fact behind SE18's discussion.
If A_j tends to infinity, eta_j>=0 tends to zero and
s[h]+eta_j||h||_X^2>=0 on every X_(A_j), then s>=0 globally. Indeed
each compactly supported native-core vector lies in all sufficiently
large apertures; first let j tend to infinity, then use core density
and continuity of s on X. The converse at the level of true local
signs is immediate. This limit argument does not prove a global sign
at any one finite j, nor construct executed local certificates.

## 5. Status of the continuation

SE19 uses a global event projection in a single exact source identity.
The full finite observation Gram retains the correlations and the
unobserved square energy remains positive. It therefore does not need
the invalid SE18 max-only gluing step. The comparison's uniform seed
and eventual pole budget are still real hypotheses, not supplied by
calling the condition invariant. See [scope](SE19_SCOPE.md).
