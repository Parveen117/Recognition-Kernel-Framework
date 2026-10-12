# SE19: recover the pole from retained Gamma and prime observations

12 October 2026. Owner: Monty. Written development; numerical
certification remains deferred under the theory-first instruction.

The next comparison uses the positive square residuals already present
in SE17. It tests the full pole functional against their joint energy,
instead of assigning the pole a fixed pointwise cost. A finite matrix
retains all correlations between the selected observations. Adding an
independent observation decreases the pole burden by an exact amount;
an observation blind to the remaining pole response gives no decrease.

This is a source-specific application of the existing SE2 recovery and
SE13 positive-reference machinery, not a new general Schur or
Birman--Schwinger principle. The [SE18 audit](SE19_SE18_AUDIT.md)
corrects its interval-floor inference and its local-to-global gluing.
The SE18 files remain unchanged as historical records.

The strongest executed global result remains SE17.1: at eta=59/100
the native floor is 1/7380, implying nonnegativity at 10883/18450.
The positive local radius remains 21/25. No smaller numerical anchor,
eta-zero sign, historical five-label identification, K0 or RH is proved.

## 1. The same source, with the pole left exact

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede representations. We use the admitted T35 graph adapter
and the corrected T40 odd source of SE4, with the native graph norm
retained as in SE17.2. This does not posit a Hilbert metric as a native
primitive or identify an arbitrary measurement with a faithful chart.

Fix 0<eta<1 and one alpha in [0,1). Use SE17's exact
L_Gamma and V_alpha, including every prime power. The row algebra
extends to this alpha range because (1-alpha)q_0<=q_alpha<=q_0;
the already executed anchor is used only on [21/40,53/100]. On the auxiliary
half-line carrier H=L2((0,infinity)), write h=sqrt(2) f for x>0;
J h is its odd extension divided by sqrt(2). J is an L2 isometry.
Its graph-domain pullback J^(-1)X is dense in H, not all of H.
Put
\[
 z=e^{-x/2},\quad u=z^6,\quad
 v(x)=\tfrac12(e^{-x}-e^{-2x}),\qquad
 F[f]=4|\langle v,h\rangle_H|^2,
\]
\[
 W_{\eta,\alpha}(z)=\eta(1+z^6)+(1-\eta)L_\Gamma(z)-V_\alpha(z)
                  =Q_{\eta,\alpha}(z)+\tfrac1{10}(1-z^6).
                                                               \tag{SE19.1}
\]
Let delta_G=g_c-m_Gamma>0. Cancelling the pole comparison and its
residual in SE17.11 gives the exact identity
\[
 \begin{split}
 s[f]+\eta\|f\|_X^2
 &=\langle h,M_W h\rangle+(1-\eta)D_\Gamma[h]
       +D_{P,\alpha}[Jh]-4|\langle v,h\rangle|^2+\mathcal E_\eta[f],\\
 \mathcal E_\eta[f]
 &=2\eta E_+[f]+(1-\eta)\{E_{16}[f]+\delta_G\|mf\|_2^2\}\ge0.
 \end{split}                                                   \tag{SE19.2}
\]
No source term, sign, prime tail or native norm has changed. The
unbounded graph energies stay in the nonnegative form E_eta on X.

**Standing hypothesis for Sections 2--6:** the chosen comparison has
\[
                 W_{\eta,\alpha}\ge w>0\quad\text{almost everywhere}.
                                                               \tag{SE19.3}
\]
W is bounded by SE17.6 and SE17.9. Its positivity is a hypothesis to
establish at each new eta; observation monotonicity does not establish it.
At the existing eta=59/100 this hypothesis follows from SE17's already
proved Q>=1/1000, uniformly throughout the certified alpha interval.

## 2. Optimal pole budget for the fixed diagonal energy

**Theorem 1 (diagonal pole test).** Under (SE19.3), define
\[
 \begin{split}
 \beta_0&=4\langle v,M_W^{-1}v\rangle
       =4\int_0^\infty\frac{v(x)^2}{W(e^{-x/2})}\,dx\\
       &=2\int_0^1\frac{z^3(1-z^2)^2}{W(z)}\,dz.
 \end{split}                                                   \tag{SE19.4}
\]
Then M_W-4 v tensor v>=0 on H iff beta_0<=1. Equivalently, some
positive measurable density tau<=W pays the pole on H iff beta_0<=1.
The choice tau=W works whenever that condition holds.

**Proof.** Weighted Cauchy--Schwarz gives
4|<v,h>|^2<=beta_0 <h,M_W h>. Conversely take h=M_W^(-1)v,
which belongs to H since W>=w; the inequality forces beta_0<=1.
The same criterion applies if the inequality is first known on
J^(-1)X: both forms are H-continuous and that domain is dense.
If tau<=W pays the pole, W also pays it. Conversely beta_0<=1
allows tau=W. Finally dx=-2 dz/z and v=(z^2-z^4)/2 give the last
integral. QED.

This optimizes all diagonal pole budgets below this fixed W. It does
not optimize the Gamma/prime weights or the actual source. In particular,
beta_0>1 only rejects this diagonal comparison; the positive residuals
in (SE19.2) may repair it.

**Theorem 2 (the existing anchor enters this test).** At eta=59/100,
for every alpha in SE17's interval,
\[
 W\ge\tfrac1{1000}+\tau_c\ge\tfrac{101}{100}\tau_c,
 \quad \tau_c=\tfrac1{10}(1-z^6),\qquad
 \beta_0\le\frac{1000}{101}(\log3-1)<\frac{100}{101}<1.
                                                               \tag{SE19.5}
\]
**Proof.** The first inequality is SE17's existing spatial floor.
Since tau_c<=1/10, 1/1000>=tau_c/100. SE15.5 gives
4 int v^2/tau_c=10(log3-1)<1. Integrate the reciprocal comparison;
the endpoint where tau_c vanishes is a null set. QED.

Thus the new construction has a proved nonempty application range on
the actual source. This deduction reuses the old certificate; it is
not a fresh numerical certificate or an improvement of its eta anchor.

## 3. Turn the actual residuals into observations

**Theorem 3 (bounded residual analysis).** There is a bounded analysis
T:H->Y into a separable event Hilbert space such that
\[
             \|Th\|_Y^2=(1-\eta)D_\Gamma[h]+D_{P,\alpha}[Jh].
                                                               \tag{SE19.6}
\]
It can use the actual squared differences, rather than an unrelated
positive operator. For k=0,...,15, beta_k=2k+1/2, set
\[
 (T_\Gamma h)_k(x,y)=
 \sqrt{\frac{1-\eta}{2}k_{\beta_k}^-(x,y)q_\Gamma(x)q_\Gamma(y)}
 \left(\frac{h(x)}{q_\Gamma(x)}-\frac{h(y)}{q_\Gamma(y)}\right),
                                                               \tag{SE19.7}
\]
and, with f=Jh, a_n=Lambda(n)/sqrt(n), lambda_n=log n,
\[
 (T_P h)_n(x)=
 \sqrt{a_n m(x)m(x-\lambda_n)q_\alpha(x)q_\alpha(x-\lambda_n)}
 \left(\frac{f(x)}{q_\alpha(x)}
             -\frac{f(x-\lambda_n)}{q_\alpha(x-\lambda_n)}\right).
                                                               \tag{SE19.8}
\]
Take Y to be the direct sum of the sixteen L2(dx dy) spaces and
the countable prime-event L2(dx) spaces, and T=(T_Gamma,T_P).

**Proof.** SE17.7 and SE16.11 identify the two squared norms exactly,
including their factors 1/2 and the complete prime sum. The bounded
rows make both nonnegative residual forms bounded on H; for example
the squared-difference inequality bounds each by twice its diagonal
row form. The apparent q_Gamma boundary zero is already removed in
SE17.5--SE17.7. Truncation and monotone convergence therefore extend
T to a bounded operator on H. The indicated L2 direct sum is separable.
QED.

An observation here is an integrated event coordinate <psi,Th>_Y.
Point evaluation on L2 is not automatically a bounded observation.
One admissible dense dictionary consists of simple functions on
bounded rational rectangles for Gamma and bounded rational intervals
on finitely many prime-event sheets, followed by orthonormalization.
No numerical dictionary or source Gram is evaluated in this stage.

Choose increasing finite-rank orthogonal projections Pi_n in Y,
Pi_0=0, with Pi_n->I strongly. Define
\[
 B_n=\Pi_nT,\quad A_n=M_W+B_n^\dagger B_n,\quad
 R_n=(I-\Pi_n)T,\quad A_\infty=M_W+T^\dagger T.
                                                               \tag{SE19.9}
\]
Then the exact source identity becomes
\[
 s[f]+\eta\|f\|_X^2
 =\langle h,A_n h\rangle-4|\langle v,h\rangle|^2
       +\|R_nh\|^2+\mathcal E_\eta[f].             \tag{SE19.10}
\]
The unobserved event energy is retained with its proved positive sign.
Repeated or overlapping observations may not be counted twice: the
orthogonal projection, or an equivalent correctly normalized Gram,
is essential to this identity.

## 4. A finite full-Gram pole certificate

**Theorem 4 (recovered pole test).** Under (SE19.3), identify ran Pi_n
with its orthonormal finite coordinate space and put
\[
 G_n=B_nM_W^{-1}B_n^\dagger,\quad b_n=B_nM_W^{-1}v,\qquad
 \beta_n=\beta_0-4b_n^\dagger(I+G_n)^{-1}b_n
        =4\langle v,A_n^{-1}v\rangle\ge0.
                                                               \tag{SE19.11}
\]
Then A_n-4 v tensor v>=0 iff beta_n<=1. In that case the complete
source obeys S_b+eta I_X>=0 and kappa_eta=0. If beta_n<1, then
\[
 S_b+\eta I_X\succeq c_n I_X,\qquad
 c_n=\min\left\{\eta,\frac{(1-\beta_n)w}{2+g_c}\right\}>0,
                                                               \tag{SE19.12}
\]
so the shifted nullity also vanishes.

**Proof.** Multiplication verifies the inverse identity
\[
 A_n^{-1}=M_W^{-1}-M_W^{-1}B_n^\dagger
                   (I+G_n)^{-1}B_nM_W^{-1}.
                                                               \tag{SE19.13}
\]
All inverses exist since W>=w and G_n>=0. Sandwich with v to obtain
(SE19.11). Weighted Cauchy--Schwarz in the A_n energy gives
4|<v,h>|^2<=beta_n <h,A_nh>; testing h=A_n^(-1)v proves necessity
for the retained comparison. Equation (SE19.10) proves the source
implication, with the remaining terms still nonnegative.

For strict beta_n<1 retain the 2 eta E_+ part of E_eta. The result
is at least (1-beta_n)w ||f||_2^2+2 eta E_+[f]. The native inequality
||f||_X^2<=(2+g_c)||f||_2^2+2E_+[f], already used in SE16--SE17,
gives (SE19.12). QED.

Every mixed observation entry of G_n is used. Replacing G_n by its
diagonal, testing separate observations in isolation, or declaring
the remaining cross terms zero is not this theorem. The test is
necessary and sufficient for its retained comparison; it is only
sufficient for the full source because R_n and E_eta may help further.
Its finite dimension is the number of selected residual observations,
not the historical five-label endpoint rank.

## 5. Exact gain, blindness and convergence at fixed eta

**Theorem 5 (one refinement and its blind directions).** Let C consist
of additional orthogonal residual coordinates, so A_{n+1}=A_n+C^dagger C.
Write d=C A_n^(-1)v. Then
\[
 \beta_n-\beta_{n+1}
   =4d^\dagger(I+C A_n^{-1}C^\dagger)^{-1}d\ge0,
 \qquad \beta_{n+1}=\beta_n\iff C A_n^{-1}v=0.
                                                               \tag{SE19.14}
\]
Moreover, for a complete increasing sequence of event projections,
\[
 \beta_n\downarrow\beta_\infty
       :=4\langle v,(M_W+T^\dagger T)^{-1}v\rangle.
                                                               \tag{SE19.15}
\]
If beta_infinity<1, some finite n has beta_n<1. If beta_infinity=1,
finite strict passage need not occur.

**Proof.** Apply (SE19.13) with A_n in place of M_W and C in place
of B_n. The middle inverse is strictly positive, proving both the
gain and its equality condition. Increasing Pi_n gives A_n increasing
to A_infinity strongly. The uniform floor w implies
A_n^(-1)->A_infinity^(-1) strongly: apply
A_n^(-1)-A_infinity^(-1)=A_n^(-1)(A_infinity-A_n)A_infinity^(-1)
to each fixed vector. Inverse order and the scalar limit give
(SE19.15). The strict finite-passage assertion follows from scalar
convergence. QED.

Thus a new coordinate helps precisely when it sees the remaining
response A_n^(-1)v. A coordinate can be nonzero on many states and
still be blind to this target. This is target-relative blindness in
the stated energy, not a claim that the source itself loses a state.
The theorem holds at fixed eta, alpha and W. It does not prove
monotonicity when the comparison weights or eta are changed, and it
does not prove convergence of eta to zero.

**Theorem 6 (best next observation in a declared residual space).**
In the unobserved space Y_n=(I-Pi_n)Y set
\[
 d_n=R_n A_n^{-1}v,\qquad K_n=R_n A_n^{-1}R_n^\dagger\ge0.
\]
For one unit coordinate psi in Y_n the pole gain is
\[
 \Delta(\psi)=
 \frac{4|\langle\psi,d_n\rangle|^2}
      {1+\langle\psi,K_n\psi\rangle}.
 \qquad
 \sup_{\|\psi\|=1}\Delta(\psi)
       =4\langle d_n,(I+K_n)^{-1}d_n\rangle
       =\beta_n-\beta_\infty.                    \tag{SE19.16}
\]
When d_n!=0 the maximum is attained by the normalized vector
(I+K_n)^(-1)d_n. On a declared finite candidate subspace, compress
d_n and K_n to that subspace: the analogous maximum equals the gain
from retaining that whole candidate subspace, which may be smaller
than beta_n-beta_infinity for all remaining events.

**Proof.** Take C h=<psi,R_nh> in (SE19.14). For unit psi the
denominator equals <psi,(I+K_n)psi>. Cauchy--Schwarz in this positive
energy proves the maximum and its equality direction. The bounded
inverse identity with C=R_n identifies that maximum with
beta_n-beta_infinity. A positive scalar rescaling of the maximizing
vector is removed by unit normalization. QED.

One target-adapted coordinate can therefore capture the remaining
inverse-energy improvement for this rank-one pole target. Computing
that coordinate requires the full residual response; its existence
does not provide its arithmetic enclosure or a finite-support recipe.
For actual development, the finite candidate-space version gives a
well-defined next-observation choice without asserting that ideal
infinite calculation has been performed.

## 6. Direct algebra controls and transport boundary

These exact examples check the mechanisms on finite auxiliary
matrices, not on the RH source. Take W=I_2 and v=(1,1)^T/2. Then
beta_0=2. With B=(1,1), A=I+B^dagger B has eigenvalue 3 along v,
beta_1=2/3, and A-4v v^dagger=I_2. Thus retained observation energy
can succeed where every diagonal pole density below W fails.
With B=(1,-1), instead Bv=0 and beta_1=2: that coordinate is blind
to this response and the negative direction remains.

Under faithful changes of state and event coordinates with transported
pairings, A_n, v, T and Pi_n transform together. The variational scalar
4 sup_(h!=0)|<v,h>|^2/<h,A_nh> and hence beta_n are unchanged.
Changing alpha, dropping an event, or changing the target is a change
of comparison, not such a coordinate transport. The intrinsic source
count remains kappa_eta; beta_n is the burden of a declared comparison.
No measurement-free invariant or identification of Euler e with a
cut invariant is inferred.

## 7. Concrete next obligation

At a proposed smaller positive eta, establish a valid positive seed
W>=w, assemble the complete pole integral and the full finite Gram
for an admitted residual dictionary, and prove beta_n<=1 with all
tails accounted for. Theorem 6 specifies which further candidate
observation gives the largest decrease. If W lacks a positive floor,
this particular inverse construction is not applicable: one must
first supply another positive operator seed with its full coupling
contract, as in SE2/SE13. Substituting zero into the inverse is invalid.

This stage supplies that written mechanism and the exact blindness
test. It does not execute the smaller-eta inequalities. SE5's essential
zero threshold, SE13's cofinal condition and the historical K0/RH
attachment obligations remain in force. See the
[audit](SE19_SE18_AUDIT.md), [scope](SE19_SCOPE.md), and
[source record](SE19_SOURCE_RECORD.md).
