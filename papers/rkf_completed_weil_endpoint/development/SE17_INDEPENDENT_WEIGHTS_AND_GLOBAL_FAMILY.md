# SE17: independent comparison weights and a global certified family

12 October 2026. Owner: Monty.

The entire corrected complex odd source satisfies
\[
 S_b+\frac{59}{100}I_X\succeq\frac1{7380}I_X.
                                                               \tag{SE17.1}
\]
The sufficient global anchor improves from SE16's 0.69 to 0.59.
The proof uses sixteen retained odd Gamma modes, a boundary-adapted
Gamma weight, and a distinct positive prime weight. An entire closed
interval of prime weights certifies the same bound. Their parameters
may change between replays without converging to a fixed calibration.

The positive local aperture remains 21/25. Eta zero, the unshifted
critical observer, the historical five-label endpoint, K0 and RH
remain open. The new reserve belongs to the shifted source.

## 1. Same native source; separate weights are allowed

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the representations. Use the admitted T35 graph and
the SE4 corrected T40 source, exactly as in SE15--SE16:
\[
 \begin{gathered}
 m(x)=e^{-3|x|/2},\quad g=mf,\quad u=m^2,\quad d\mu=d\xi/(2\pi),\\
 \|f\|_X^2=\|f\|_2^2+\int(1+|G|)|\widehat g|^2d\mu,\qquad
 s[f]=\Gamma[f]-P[f]-F[f].
 \end{gathered}                                                  \tag{SE17.2}
\]
Here G is SE16's central digamma symbol, Gamma its Fourier form,
P the complete paired prime translations, and F the full odd pole.
The inherited bounds are m_Gamma=-G(0)<g_c=269/50 and
F[f]<=b_c integral (1-u)|f|^2, b_c=1/10.
Write E_+=integral G_+|g-hat|^2 dmu and
D_F=b_c integral (1-u)|f|^2-F[f]>=0.

The exact weighted-square identity SE16.7 can be applied separately
to each positive kernel. It imposes no equality between their test
weights. Choose
\[
 \begin{split}
 q_\Gamma(x)&=e^{-x/2}(1-e^{-2x}),\quad x>0,\\
 q_\alpha(x)&=e^{-|x|/2}(1-\alpha e^{-3|x|}),\quad x\in\mathbb R,
 \qquad \frac{21}{40}\le\alpha\le\frac{53}{100}.
 \end{split}                                                    \tag{SE17.3}
\]
The first is positive on the open half-line. Its zero at the single
boundary point is handled by an exact removable limit below.
The second is strictly positive everywhere. Neither weight changes
the source, its odd carrier, or its native pairing.

## 2. Boundary-adapted odd Gamma reading

**Theorem (sixteen-mode identity with a regular boundary).** Let
beta_k=2k+1/2, 0<=k<16, and C_16=sum_(k<16) 2/beta_k. On the faithful
odd chart h(x)=sqrt(2)f(x), x>0, use the same positive kernels
\[
 k_\beta^-(x,y)=m(x)m(y)
   \{e^{-\beta|x-y|}-e^{-\beta(x+y)}\}.
 \qquad
 \Gamma[f]=(C_{16}-m_\Gamma)\|g\|_2^2
       -\sum_{k<16}\langle h,K_{\beta_k}^-h\rangle+E_{16}[f],
 \quad E_{16}\ge0.                              \tag{SE17.4}
\]
E_16 is the complete integral of the omitted nonnegative digamma
terms, not an unknown error. This is SE16.4--SE16.6 with a longer
finite head; monotone convergence supplies the remaining series.

Put z=exp(-x/2), c_beta=2 beta/(4-beta^2), and
d_beta=2 beta/(16-beta^2). Splitting each exponential integral at
y=x and retaining the reflected term gives the exact row
\[
 H_\beta^*(z)=
 \frac{c_\beta(z^{2\beta+2}-z^6)
       -d_\beta(z^{2\beta+2}-z^{10})}{1-z^4},
 \qquad H_\beta^*(1)=\frac{2\beta}{(\beta+2)(\beta+4)}.
                                                               \tag{SE17.5}
\]
For a direct derivation, integrate the kernel against exp(-a y)
with a=2 and a=4. The three pieces are
(exp(-beta x)-exp(-a x))/(a-beta), exp(-a x)/(a+beta), and
-exp(-beta x)/(a+beta). Subtract the a=4 expression from the a=2
expression and multiply by m(x)/q_Gamma(x). This yields (SE17.5).
Differentiation at x=0 gives its stated limit. All denominators
a-beta are nonzero for these half-integer beta values. QED.

No interval division through zero is used. Define the exact
polynomials D_(a,b)(z)=(z^a-z^b)/(1-z), using a finite geometric sum,
and S_3(z)=1+z+z^2+z^3. The Gamma lower potential is
\[
 \begin{split}
 L_\Gamma(z)&=(C_{16}-g_c)z^6-\sum_{k<16}H_{\beta_k}^*(z)
              =\frac{A(z)}{S_3(z)},\\
 A(z)&=(C_{16}-g_c)z^6S_3(z)
 -\sum_{k<16}\{c_{\beta_k}D_{(4k+3,6)}(z)
                  -d_{\beta_k}D_{(4k+3,10)}(z)\}.
 \end{split}                                                    \tag{SE17.6}
\]
A has rational coefficients and degree 62. S_3>=1 on [0,1].
This proves boundedness of the row through the boundary and provides
a rational interval evaluation of the exact expression.

By the weighted-square identity,
\[
 D_\Gamma[h]:=\sum_{k<16}\frac12\iint k_{\beta_k}^-(x,y)
 q_\Gamma(x)q_\Gamma(y)
 \left|\frac{h(x)}{q_\Gamma(x)}-\frac{h(y)}{q_\Gamma(y)}\right|^2dxdy
 \ge0.                                                         \tag{SE17.7}
\]
The diagonal rows are bounded, so these integrals extend from
truncated data to every L2 reading. No pointwise trace of h at zero
is required. Odd folding retains the full complementary reading.

## 3. Shaped prime reading with every event retained

**Theorem (exact two-exponential prime row).** For r=1/2 or 7/2 set
t=exp(|x|), z=t^(-1/2), N=floor(t), and
\[
 \begin{gathered}
 p_{2+r}=\sum_{n\ge2}\Lambda(n)n^{-(2+r)},\quad
 A_{r,N}=\sum_{2\le n\le N}\Lambda(n)n^{1+r},\quad
 T_{r,N}=\sum_{n>N}\Lambda(n)n^{-(2+r)},\\
 V_r(z)=z^6(A_{r,N}+p_{2+r})+z^{-4r}T_{r,N}.
 \end{gathered}                                                  \tag{SE17.8}
\]
This is the positive prime kernel applied to exp(-r|x|), divided by
that weight: split x-log n by its sign in the two exact translations.
Linearity before division therefore gives
\[
 V_\alpha(z)=\frac{V_{1/2}(z)-\alpha z^6V_{7/2}(z)}{1-\alpha z^6},
 \qquad
 P[f]=\int V_\alpha(e^{-|x|/2})|f(x)|^2dx-D_{P,\alpha}[f],
 \quad D_{P,\alpha}\ge0.                        \tag{SE17.9}
\]
D_(P,alpha) is exactly SE16.11 with q replaced by q_alpha.
Expanding its squared difference recovers both complex cross terms.
Although V_(7/2) alone need not be globally bounded, the combined
row obeys V_alpha<=V_(1/2)/(1-alpha) and is bounded. This follows
directly from (1-alpha)q_0<=q_alpha<=q_0 and positivity of the prime
kernel, where q_0=exp(-|x|/2). Complete row integrability and monotone
convergence justify every prime power in (SE17.9). QED.

## 4. Full source and the convex family theorem

**Theorem (independent-weight source identity).** For 0<eta<1 put
\[
 d_\eta(z)=\eta-b_c+(\eta+b_c)z^6+(1-\eta)L_\Gamma(z),
 \qquad Q_{\eta,\alpha}(z)=d_\eta(z)-V_\alpha(z).
                                                               \tag{SE17.10}
\]
Then, with the full native graph pairing retained,
\[
 \begin{split}
 s[f]+\eta\|f\|_X^2
 &=\int Q_{\eta,\alpha}(e^{-|x|/2})|f|^2dx+2\eta E_+[f]\\
 &\quad +(1-\eta)\{D_\Gamma[h]+E_{16}[f]
                   +(g_c-m_\Gamma)\|g\|_2^2\}
          +D_{P,\alpha}[f]+D_F[f].
 \end{split}                                                    \tag{SE17.11}
\]
Proof. Use G+eta|G|=(1-eta)G+2eta G_+ and substitute the exact Gamma,
prime and pole decompositions. Distinct weights simply give distinct
nonnegative residuals. Every term matches the original source.
Bounded rows and the established graph forms extend the core identity
to X. QED.

**Theorem (convex cone of certifying weights).** Fix eta and c.
Let K_P denote the positive complete prime kernel. If two positive
weights q_0 and q_1 obey (d_eta-c)q_j-K_P q_j>=0 pointwise, then
every positive constant linear combination has the same property:
\[
 \begin{split}
 q_\theta&=(1-\theta)q_0+\theta q_1,\quad 0\le\theta\le1,\\
 (d_\eta-c)q_\theta-K_Pq_\theta
 &=(1-\theta)\{(d_\eta-c)q_0-K_Pq_0\}
   +\theta\{(d_\eta-c)q_1-K_Pq_1\}\ge0.
 \end{split}                                                    \tag{SE17.12}
\]
Division by q_theta>0 gives Q>=c. Positive rescaling cancels from
the row. For (SE17.3), certifying the two alpha endpoints certifies
every alpha between them. This is linearity before division, not
an assumed convexity of the ratios. QED.

Consequently any sequence of parameters in this interval, convergent
or not, supplies the same certified source inequality. A parameter
chosen independently at each spatial point does not follow from
this theorem: K_P couples the whole weight. An exact finite negative
control in the tests demonstrates that distinction. Nor is this a
claim that arbitrary lossy measurements preserve the source invariant.

## 5. Complete arithmetic and spatial enclosure

Use M=4096=64^2 and the unchanged 604-entry prime-power catalogue.
SE16 supplies the complete exponent-5/2 head, tail and cell upper
bound U_(1/2)(a,b). The auxiliary exponent-11/2 mass has the enclosure
\[
 \sum_{n\le M}\frac{\Lambda(n)}{n^{11/2}}
 \le p_{11/2}\le
 \sum_{n\le M}\frac{\Lambda(n)}{n^{11/2}}+\tau_M^*,\qquad
 \tau_M^*=\frac{(2/9)\log M+4/81}{M^{9/2}}.
                                                               \tag{SE17.13}
\]
Proof: Lambda(n)<=log n and the decreasing integral test, integrating
log(t)t^(-11/2) exactly. The entire omitted mass is below 1.054e-16.

For a cell a<=z<=b in [1/64,1], put L=floor(b^(-2)), U=floor(a^(-2)).
Write p^lo for the finite positive mass through M. A complete lower
bound for the auxiliary row is
\[
 \begin{split}
 \ell_*(a,b)&=a^6(A_{7/2,L}+p^{\rm lo})
       +b^{-14}\sum_{U<n\le M}\frac{\Lambda(n)}{n^{11/2}}\\
 &\quad +\sum_{L<n\le U}\Lambda(n)
       \min\{n^{9/2}a^6,n^{-11/2}b^{-14}\}
 \le V_{7/2}(z).
 \end{split}                                                    \tag{SE17.14}
\]
Proof. Each event is min(n^(9/2)z^6,n^(-11/2)z^(-14)). Events outside
the breakpoint interval are monotone on the cell. Each straddled
event is bounded below by the smaller of its two endpoint branch
bounds. Omitted events are nonnegative and may be dropped in this
lower bound. No negative omitted contribution is discarded. QED.

Since the exact combined numerator is positive, (SE17.9) implies
\[
 V_\alpha(z)\le
 \frac{U_{1/2}(a,b)-\alpha a^6\ell_*(a,b)}{1-\alpha b^6}.
                                                               \tag{SE17.15}
\]
The implemented upper uses outward endpoint rounding throughout;
the denominator is at least 1-alpha>0. This is why the auxiliary
row needs a lower bound while the base row needs an upper bound.
Reversing those directions would be invalid.

For the entire exterior t>=M, let B_M be SE16.19 evaluated at M,
using its complete prime-mass upper bound. Write A(z)=sum a_j z^j.
All powers of A are nonnegative integer powers, and S_3>=1, so
\[
 Q_{59/100,\alpha}(z)\ge
 \frac{59}{100}-\frac1{10}
 -\frac{41}{100}\sum_j|a_j|64^{-j}
 -\frac{B_M}{1-(53/100)M^{-3}}
 >0.34436233708.
                                                               \tag{SE17.16}
\]
The prime exterior estimate decreases beyond M, as proved in SE16.
Dropping the positive auxiliary subtraction only enlarges this upper
bound, and the displayed denominator is a uniform lower bound.
The discarded diagonal term (eta+b_c)z^6 is positive. This covers
every exterior position, including the limiting value at infinity.

The replay evaluates the rational Gamma potential and (SE17.15)
over whole cells, for both endpoint weights. Its 485 dyadic cells
cover [1/64,1] with exactly matching rational endpoints and maximum
depth 13. All 970 endpoint-weight cell inequalities exceed 1/1000;
the smallest enclosed lower value is above 0.00100621309.
(SE17.12) then covers the whole continuous weight family. These
cells and the analytic exterior prove Q>=1/1000 everywhere; sampled
eigenvalues or a spatial scan are not proof inputs.

## 6. Global invariant and the retained-shape control

**Theorem (executed global family certificate).** Equations
(SE17.11)--(SE17.16) give, for the entire complex odd source,
\[
 \begin{gathered}
 s[f]+\frac{59}{100}\|f\|_X^2
 \ge\frac1{1000}\|f\|_2^2+\frac{118}{100}E_+[f],\\
 \|f\|_X^2\le(2+g_c)\|f\|_2^2+2E_+[f],\qquad
 \frac{1/1000}{2+269/50}=\frac1{7380}.
 \end{gathered}                                                  \tag{SE17.17}
\]
Since 59/100>1/7380, this proves (SE17.1). In particular
\[
 \kappa_\eta=N_-(S_b+\eta I_X)=0,\quad
 \ker(S_b+\eta I_X)=\{0\}\quad(\eta\ge59/100),\qquad
 S_b\succeq-\frac{10883}{18450}I_X.
                                                               \tag{SE17.18}
\]
The last inequality also gives zero negative count at its implied
nonnegative shift. The positive native floor and nullity statement
are recorded at the simple anchor 0.59, not at that smaller shift.
Neither number is asserted to be the exact spectral edge.

**Theorem (the prime shape matters to this comparison).** Keep the
same sixteen-mode Gamma weight but replace q_alpha by q_0. At
x=log 3 the exact complete point enclosure gives
\[
 Q_{59/100,0}(1/\sqrt3)<-0.10164567760<0.
                                                               \tag{SE17.19}
\]
Proof. Use N=3 in (SE17.8), the complete exponent-5/2 mass enclosure,
and the exact rational Gamma potential (SE17.6). The negative upper
bound is recorded in the replay. This is a failure of the unshaped
comparison at the same eta, not a negative value of the source. QED.

## 7. What is and is not released

The Gamma and prime kernels no longer share one imposed comparison
weight. The certified prime weight belongs to a full convex family,
and need not settle at one reference between refinements. Changes
in the scalar reading are balanced by changes in its exact squared
residual. The invariant belongs to the complete source identity.
Faithful observer transport still carries the source, odd relation,
weights, domains and pairing together, as in SE13--SE16.

This is a sufficient positive-eta certificate. It establishes neither
eta=1/2 nor a sequence of certified shifts tending to zero. The
unshifted essential zero threshold, global critical contractivity,
historical endpoint and RH boundary are unchanged. No convergence
rate to eta zero or optimality of these weights follows from the
finite sequence of improved anchors.

General weighted Schur testing is established prior art. The new
content here is the source-specific pair of weights, exact regular
boundary calculation, complete family enclosure and improved global
anchor. Written proofs, interval execution, provenance, formalization
and external review remain separate evidence categories.

See the [replay](../../../proof_lab/endpoint_weight_family_certificate.py),
[result](../../../proof_lab/ENDPOINT_WEIGHT_FAMILY_RESULT.json),
[controls](../../../proof_lab/test_endpoint_weight_family_certificate.py),
[sources](SE17_SOURCE_RECORD.md), [audit](SE17_SCOPE.md) and
[pins](SE17_SOURCE_PINS.json).
