# SE5: Stable exact observer and compact critical defect

11 October 2026. Owner: Monty Dabas.

This continues the corrected central-Gamma source of
[SE4](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md). It proves that its
positive mismatch Gram has a uniform native lower bound. Consequently
the joint debt/boundary observer exists as a bounded exact operator and
its regularized approximations converge in operator norm.

Its norm being at most one is still unproved. The lower bound is for
the mismatch Gram, not for the source after debt or boundary subtraction.
The latter retains the zero-reserve escape found in SE4.

## 1. Fixed source, native metric and notation

Typed cuts, source/target arrows and Smriti precede the representation.
Here the admitted representation is precisely the T35 graph used in SE4,
on the odd carrier X. Every dagger below is the adjoint for its stated
native domain and target metrics. No alternate engine or source is chosen.

Let a=3/2, m(x)=exp(-a|x|), Rf=mf, and let F denote the unitary Fourier
map from L2(dx) to L2(dmu), dmu=dxi/(2pi), with positive exponent.
Write
\[
 G(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi,\qquad
 g_0=G+m_\Gamma,\qquad G_-=\max(-G,0).
\]
The native graph norm and its two bounded coordinate maps satisfy
\[
 \|f\|_X^2=\|f\|_2^2+
       \int(1+|G|)|\mathcal F Rf|^2d\mu,\quad
 \iota:X\longrightarrow L^2,\quad
 E=\iota^\dagger\iota,\quad C^\dagger C=I_X-E.
                                                        \tag{SE5.1}
\]
Thus 0<=E<=I_X. E is not the identity and is not assumed compact.
The Fourier normalization in C agrees with SE4.

Retain the exact SE4 arrows A_*, B, J and L_d. In particular
\[
 Bf=\sqrt{1+m^4}\,f,\quad
 m_p=\sum_{n\ge2}\frac{\Lambda(n)}{n^2}>0,\quad
 D_*=m_\Gamma R^\dagger R+m_pB^\dagger B,\quad
 N_*=A_*^\dagger A_*.
\]
For a supplied bounded finite-column map W from a finite-dimensional
label space and a positive definite metric G_E, set
\[
 F_b=WG_E^{-1}W^\dagger,\quad
 \mathcal L_*=\begin{pmatrix}
    \sqrt{m_\Gamma}R\\ \sqrt{m_p}B\\G_E^{-1/2}W^\dagger
 \end{pmatrix},\quad
 S_b=N_*-\mathcal L_*^\dagger\mathcal L_*
     =N_*-D_*-F_b.                                    \tag{SE5.2}
\]
For the actual full odd form, W=r_partial and G_E=1. General W in this
note is supplied data; it does not manufacture the other four Feshbach
columns. X-adjoints automatically include the T35 graph metric.

## 2. The central input is compact, with an explicit approximation

**Lemma.** R:X->L2 is compact.

The SE4 digamma series gives, with s_k=k+1/4,
\[
 g_0(\xi)=\sum_{k\ge0}
       \frac{(\xi/2)^2}{s_k(s_k^2+(\xi/2)^2)}.
\]
It is increasing in |xi| and tends to infinity. Indeed, for
|xi|>=2(K+1/4), its first K+1 terms are at least
one half of the divergent sum of 1/s_k. Hence G tends to positive
infinity. This conclusion uses the series, not an assumed asymptotic.

Let Q_L be multiplication by 1_{[-L,L]} on L2(dx), and let P_T be
the Fourier projection onto [-T,T]. Choose T with G(T)>=0 and put
w_T=1+G(T). From (SE5.1),
\[
 \|(I-P_T)R\|\le w_T^{-1/2},\qquad
 \|(I-Q_L)R\|\le e^{-aL}.
\]
Therefore
\[
 \|R-P_TQ_LR\|\le w_T^{-1/2}+e^{-aL}.                 \tag{SE5.3}
\]
P_T Q_L has Hilbert--Schmidt norm squared 2LT/pi. Its composition
with R is compact. Letting L,T tend to infinity proves the lemma.
The restriction to the odd subspace causes no change.

There is also a finite-rank version, needed for quantitative tail work.
For an integer d>=1 define R_d=R_{L,T,d} by
\[
 (\mathcal F R_df)(\xi)=
  {\bf1}_{|\xi|\le T}\sum_{k=0}^{d-1}\frac{(i\xi)^k}{k!}
                  \int_{-L}^L x^km(x)f(x)\,dx .
                                                        \tag{SE5.4}
\]
This has rank at most d. Taylor's integral remainder on the real axis
gives |exp(it)-sum_{k<d}(it)^k/k!|<=|t|^d/d!.
The corresponding integral-kernel bound, including dmu, proves
\[
 \boxed{\|R-R_d\|\le
 \rho(L,T,d):=e^{-aL}+w_T^{-1/2}
             +\sqrt{\frac{2LT}{\pi}}\,\frac{(LT)^d}{d!}.}
                                                        \tag{SE5.5}
\]
First choose L,T to make the first two terms small, then d to control
the last. No claim that fixed d works as L,T increase is made.
Certified finite lower sums for g_0(T), together with an upper enclosure
for m_Gamma, can replace w_T by any verified positive lower bound.
The finite-rank approximation is an analysis tool, not a new source.

## 3. The complete prime cross-operator is compact

Let P be the bounded self-adjoint native operator of the exact prime
cross-form:
\[
 \langle f,Pf\rangle_X=P_{1/2}[Rf],\qquad
 P_M=R^\dagger H_{p,M}R,\quad
 H_{p,M}=\sum_{2\le n\le M}\frac{\Lambda(n)}{\sqrt n}
                  (T_{\log n}+T_{-\log n}).
                                                        \tag{SE5.6}
\]
Here (T_lambda g)(x)=g(x-lambda). The finite operators P_M are compact
by Section 2. On the exact Hardy pair, the omitted multiplier has norm
at most
\[
 t_M=\sum_{n>M}\frac{\Lambda(n)}{n^2}
       \le\frac{\log M+1}{M}\qquad(M\ge2).
\]
Since ||J||<=sqrt(2), the SE4 pullback identity gives
\[
 \boxed{\|P-P_M\|\le2t_M.}                            \tag{SE5.7}
\]
Thus P is compact, as a norm limit of compact operators. The integral
tail uses only Lambda(n)<=log n. No prime-density theorem is needed.
The nonsummable-looking coefficients Lambda(n)/sqrt(n) are used only
in a finite core; the infinite tail is controlled in its actual Hardy
input metric. Replacing that tail by a formal L2 convolution norm
would not prove this assertion.

## 4. Uniform stability of the positive mismatch

Set
\[
 H=I_X+(m_p-1)E,\qquad h=\min(1,m_p)>0.
\]
Then H>=hI_X. The exact identities
\[
 B^\dagger B=E+R^\dagger M_{m^2}R,\qquad
 (\Gamma_0\mathcal F R)^\dagger(\Gamma_0\mathcal F R)
 =I_X-E+
 R^\dagger\mathcal F^{-1}M_{m_\Gamma-1-2G_-}\mathcal F R
\]
and the prime mismatch identity imply
\[
 \boxed{N_*=H+K_N,\quad
 K_N=R^\dagger\!
 \left[\mathcal F^{-1}M_{m_\Gamma-1-2G_-}\mathcal F
                    +m_pM_{m^2}\right]\!R-P.}
                                                        \tag{SE5.8}
\]
K_N is compact and self-adjoint. The bracket is bounded:
0<=G_-<=m_Gamma, so its norm is at most m_Gamma+1+m_p.

**Stable-mismatch theorem.** For these corrected actual source data
there is a constant c_*>0 such that
\[
 \boxed{N_*\succeq c_*I_X.}                           \tag{SE5.9}
\]

Proof. N_* is positive. Its kernel is zero because its Gamma summand
vanishes only when F(Rf) vanishes almost everywhere: g_0 is strictly
positive except at xi=0, a null set, and R is injective.
If (SE5.9) failed, choose ||f_j||_X=1 with
<f_j,N_*f_j>_X tending to zero. Bounded positivity implies N_*f_j->0.
Pass to a weakly convergent subsequence f_j->f. Then N_*f=0, so f=0.
Compactness gives K_N f_j->0. But
\[
 \langle f_j,N_*f_j\rangle_X
 =\langle f_j,Hf_j\rangle_X+\langle f_j,K_Nf_j\rangle_X
 \ge h+o(1),
\]
a contradiction. This proves a uniform lower bound, not just
injectivity. QED.

In particular A_* has closed range. The theorem also holds for its
restriction to any closed native subspace, with the same lower bound.
It does not identify a requested Feshbach subspace or its source columns.
No value for c_* is numerically certified in this note.

## 5. A finite route to certifying the mismatch floor

The compact remainder has an explicit finite-rank enclosure. Put
\[
 V_{N,M}=\mathcal F^{-1}M_{m_\Gamma-1-2G_-}\mathcal F
                  +m_pM_{m^2}-H_{p,M},\qquad
 K_{N,d,M}=R_d^\dagger V_{N,M}R_d.
\]
With
\[
 v_{N,M}=m_\Gamma+1+m_p+
                   2\sum_{2\le n\le M}\frac{\Lambda(n)}{\sqrt n},
\]
(SE5.5)--(SE5.7) imply
\[
 \boxed{\|K_N-K_{N,d,M}\|
       \le v_{N,M}\rho(2+\rho)+2t_M=:\tau_N.}         \tag{SE5.10}
\]
Indeed ||R||<=1 and ||R_d||<=1+rho; replacing both factors of R
costs at most v_{N,M}rho(2+rho). Choose M first and then choose
L,T,d to control rho. Increasing M with a fixed rho is not a valid
convergence argument.

Define F_N=H^{-1/2}K_NH^{-1/2}. It is compact. For a finite orthogonal
native projection Pi, suppose one has verified
\[
 \|F_N-\Pi F_N\Pi\|\le\tau,\quad
 \lambda_{\min}(I_{\Pi X}+\Pi F_N\Pi)\ge\ell,\quad
 \delta:=\min(1,\ell)-\tau>0.
\]
Then
\[
 \boxed{N_*\succeq h\delta I_X.}                     \tag{SE5.11}
\]
Proof: I+Pi F_N Pi equals the displayed finite block on Pi X and
the identity on its orthogonal complement. Subtract its norm error,
then conjugate by H^{1/2}. QED.

This is a sufficient computable floor certificate. Along cofinal
orthogonal projections, compactness makes the compression tail vanish;
the positivity proved in Section 4 ensures an exact-data certificate
eventually succeeds. It still requires actual matrix and tail
enclosures to report a numerical c_*.

For instance (SE5.10) gives
||F_N-H^{-1/2}K_{N,d,M}H^{-1/2}||<=tau_N/h.
If Pi contains the range of this finite self-adjoint approximation,
then ||F_N-Pi F_N Pi||<=2tau_N/h. Approximation and solve errors in
forming that range must be included in the same bound.
This reuses the same-projection discipline of MP Gold 06.

## 6. Exact bounded observer and operator-norm convergence

Because N_* is now boundedly invertible, define
\[
 \boxed{O_{*,0}=\mathcal L_*N_*^{-1}A_*^\dagger,\qquad
        O_{*,0}A_*=\mathcal L_*.}                    \tag{SE5.12}
\]
This is a bounded exact observer of all declared debt and boundary
channels. It is zero on Ran(A_*) perpendicular, and every exact observer
agrees with it on Ran(A_*). Consequently it has the least possible
operator norm among bounded exact observers, although minimizing
extensions on the perpendicular space need not be unique.

Write A_*=U N_*^{1/2}, where U is an isometry onto its closed range.
For the SE4 regularization,
\[
 O_{*,\epsilon}=\mathcal L_*(N_*+\epsilon I)^{-1}A_*^\dagger,
\]
functional calculus gives the explicit bounds
\[
 \boxed{\begin{aligned}
 \|O_{*,\epsilon}-O_{*,0}\|
 &\le\frac{\epsilon\|\mathcal L_*\|}
                  {\sqrt{c_*}(c_*+\epsilon)},\\
 \|\mathcal L_*-O_{*,\epsilon}A_*\|
 &\le\frac{\epsilon\|\mathcal L_*\|}{c_*+\epsilon}.
 \end{aligned}}                                      \tag{SE5.13}
\]
The full observer, including its infinite debt component, therefore
converges in operator norm. This strengthens SE4's strong convergence
statement; it is not limited to the finite boundary row.

Its limiting target Gram and monotone approximations obey
\[
 K_{*,0}=\mathcal L_*N_*^{-1}\mathcal L_*^\dagger,\quad
 0\preceq K_{*,0}-K_{*,\epsilon}
 \preceq\frac{2\epsilon\|\mathcal L_*\|^2}{c_*^2}I,
                                                        \tag{SE5.14}
\]
where K_{*,epsilon}=O_{*,epsilon}O_{*,epsilon}^\dagger.
For a scalar x>=c_*, the difference is
1/x-x/(x+epsilon)^2<=2epsilon/c_*^2, which proves the estimate.

The remaining exact criterion is
\[
 \boxed{\begin{aligned}
 S_b\succeq0
 &\ \Longleftrightarrow\
 T_*:=N_*^{-1/2}\mathcal L_*^\dagger\mathcal L_*N_*^{-1/2}
       \preceq I_X\\
 &\ \Longleftrightarrow\ \|O_{*,0}\|\le1 .
 \end{aligned}}                                      \tag{SE5.15}
\]
SE4's escaping packets show
1<=||O_{*,0}||<=||L_*||/sqrt(c_*)<infinity.
More precisely, ||O_{*,0}||^2=||T_*||=||K_{*,0}||.
Thus bounded exact recovery is proved, while contractive exact recovery
remains the unresolved sign problem. In particular a finite value for
the boundary Gram relative to N_* is not a bound relative to S_*.

## 7. Compact critical defect and what can still escape

The completed operator has another exact decomposition:
\[
 \boxed{S_b=T_0-V,\quad T_0=I_X-E=C^\dagger C\succeq0,\quad
 V=R^\dagger\mathcal F^{-1}M_{1+2G_-}\mathcal F R+P+F_b.}
                                                        \tag{SE5.16}
\]
V is compact and self-adjoint, but need not be positive. Therefore
for every eta>0 the spectral subspace of S_b below -eta is finite
dimensional. To see this directly, an orthonormal sequence in that
subspace would have <f_j,S_b f_j><=-eta, whereas compactness of V and
positivity of T_0 would give <f_j,S_b f_j>>=o(1), a contradiction.
The negative part of S_b is compact. Any negative eigenvalues have
finite multiplicity and can accumulate only at zero.

The zero threshold is real, not removable by this compactness argument.
SE4 supplies unit-normalized weakly escaping f_j with ||Cf_j||->0.
Consequently T_0 f_j->0 and V f_j->0, so S_b f_j->0. Thus zero remains
in the essential spectrum on the full odd carrier, and on every fixed
finite-codimensional native restriction.

Similarly I_X-T_* is a positive operator minus a compact operator,
by conjugating (SE5.16) with N_*^{-1/2}. Every spectral subspace of T_*
above 1+delta, delta>0, is finite dimensional. Its positive excess
(T_*-I_X)_+ is compact. Moreover
z_j=N_*^{1/2}f_j/||A_*f_j|| is a unit weakly null sequence with
(I_X-T_*)z_j->0. Hence 1 is an essential threshold for T_*.
A violation ||O_{*,0}||>1 would be witnessed by an eigenvalue of T_*
above one; infinitely many smaller violations could still accumulate
at one. Compactness alone does not exclude them.

For a concrete finite-margin certificate, use the already established
MP Gold 06 machinery on the compact self-adjoint operator
\[
 \mathcal B_\eta=(T_0+\eta I)^{-1/2}V(T_0+\eta I)^{-1/2}.
\]
For each eta>0,
\[
 \boxed{S_b\succeq-\eta I_X
      \ \Longleftrightarrow\ \mathcal B_\eta\preceq I_X.}
                                                        \tag{SE5.17}
\]
This follows by factoring S_b+eta I, so it requires no inverse of S_b.
With
\[
 V_{d,M}=R_d^\dagger
       [\mathcal F^{-1}M_{1+2G_-}\mathcal F+H_{p,M}]R_d+F_b,\quad
 v_{V,M}=1+2m_\Gamma+
                  2\sum_{2\le n\le M}\frac{\Lambda(n)}{\sqrt n},
\]
the same argument as (SE5.10) yields
\[
 \boxed{\|V-V_{d,M}\|\le
       v_{V,M}\rho(2+\rho)+2t_M=:\tau_V,\quad
 \|\mathcal B_\eta-\mathcal B_{\eta,d,M}\|\le\tau_V/\eta.}
                                                        \tag{SE5.18}
\]
The supplied finite boundary term is retained exactly in this formula.
Errors in its numerical data must be added if it is only approximately
known. Every block and tail in a Gold 06 certificate must use the same
projection; neither a small boundary norm nor sampled eigenvalues
replace that requirement.

## 8. The two zero limits and the remaining endpoint task

| Limit or assertion | SE5 result |
| --- | --- |
| Inverting N_*+epsilon I as epsilon tends to zero | Bounded exact inverse exists; full observer converges in norm |
| Numerical conditioning constant c_* | Positive existence proved; value not yet enclosed |
| S_b at its zero spectral threshold | Zero remains essential; nonnegativity not proved |
| Contractive observer | Exact bounded candidate constructed; its norm <=1 remains open |
| Compact sign-defect approximation | Explicit native core and full prime-tail bounds supplied |
| Fixed positive eta certificate | Can reuse the existing same-projection Gold 06 route |
| Passage from those certificates to eta=0 | Needs certificates for a cofinal eta sequence, or another uniform sign proof |
| Actual five-label endpoint | Complement, four further columns and their metric still need identification |

The bound tau_V/eta explicitly shows why resolving the mismatch inverse
does not resolve the completed-source zero cut. A norm approximation
whose absolute error is fixed cannot be promoted through eta->0.
If S_b>=-eta_j I were certified for every member of a sequence
eta_j->0, then S_b>=0 would follow; a finite list does not do this.

The next sign computation should therefore use the corrected source,
the now stable inverse N_* and the compact defect V with its stated
tails. A strict global reserve is not the goal: SE4 already rules it
out. No completed-source sign, K0 positivity or RH proof is claimed.

See the [source record](SE5_SOURCE_RECORD.md),
[pins](SE5_SOURCE_PINS.json) and [verification scope](SE5_SCOPE.md).
