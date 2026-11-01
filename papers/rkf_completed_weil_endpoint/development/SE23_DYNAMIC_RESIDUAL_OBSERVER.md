# SE23: a source-attached residual observer and its moving obstruction count

12 October 2026. Owner: Monty.

The new complete-source certificate is
\[
 \boxed{S_b+\frac{113}{200}I_X\succeq\frac1{1476000}I_X.}
 \tag{SE23.1}
\]
It improves the sufficient nonnegative shift from SE22's
837629/1476000 to 833939/1476000, approximately 0.56499932249.
Every complex odd native input, complete prime/Gamma contribution,
the pole and the infinite spatial exterior are covered. Global eta=0
remains open.

This executes an actual residual observation from SE19. The same
diagonal-only pole test is rigorously above 1.0364, while the new
source-attached observer has a certified budget below 0.995. A continuous
activation of this observation has one explicitly proved positive
crossing. The count belongs to the improving comparison; the underlying
source is unchanged. It is not an assertion that an invariant alone
forces a missing positivity inequality.

## 1. Native carrier and unchanged source

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede representations. The auxiliary carrier H=L2(0,infinity)
is the already admitted T35/T40 adapter: J h is the odd lift h/sqrt(2).
We preserve the native graph norm X and SE4's corrected source.
No arbitrary measurement, metric or physical clock is introduced as
a native primitive.

Use all definitions and complete tails of SE17, SE19 and SE22, with
\[
 \eta=113/200,\quad \alpha=513/1000,\quad z=e^{-x/2},
 \quad q=z-z^5,\quad v=(z^2-z^4)/2,
\]
\[
 W=\eta(1+z^6)+(1-\eta)L_\Gamma-V_\alpha,\qquad
 D=D_\Gamma=\sum_{k=0}^{15}D_k,\quad
 D_k=M_{(K_kq)/q}-K_k.                         \tag{SE23.2}
\]
Here K_k has the exact odd kernel
\[
 e^{-3(x+y)/2}\big(e^{-\beta_k|x-y|}-e^{-\beta_k(x+y)}\big),
 \qquad\beta_k=2k+1/2.
\]
SE17 proves the removable boundary and boundedness of D_k. Its
weighted difference representation gives D_k>=0. Let T_G be the
unscaled sixteen-sheet Gamma event analysis, so D=T_G^dagger T_G;
SE19.7 with the factor sqrt(1-eta) removed is its explicit formula.
The exact identity is
\[
 s[Jh]+\eta\|Jh\|_X^2
 =\langle h,M_Wh\rangle+(1-\eta)\langle h,Dh\rangle
   +D_{P,\alpha}[Jh]-4|\langle v,h\rangle|^2+\mathcal E_\eta[Jh],
 \quad \mathcal E_\eta\ge2\eta E_+.           \tag{SE23.3}
\]
The unbounded graph energy stays on X. All other displayed operators
are bounded on H. The certificate below establishes W>=w=1/1000
on the entire half-line; this hypothesis is checked, not inferred
from adding observations.

## 2. A rational observation of the actual Gamma events

**Theorem 1 (exact residual coordinate).** For u in H with
E=<u,Du>>0, set d=Du and psi=T_G u/sqrt(E). Then ||psi||=1 and
\[
 |\langle\psi,T_Gh\rangle|^2=|\langle d,h\rangle|^2/E,
 \qquad D\succeq(d\otimes d)/E.               \tag{SE23.4}
\]
Thus retaining this coordinate is an orthogonal event projection,
and the unobserved residual remains positive, including for complex h.

**Proof.** The norm identity follows from D=T_G^dagger T_G. Orthogonal
projection onto psi decomposes ||T_Gh||^2 into the displayed square
and its nonnegative orthogonal remainder. QED.

For the executed observation choose
\[
 u=q\phi,\qquad
 \phi(z)=-\frac7{25}z^2+\frac{1137}{50}z^4
              -\frac{4103}{100}z^6+\frac{516}{25}z^8.          \tag{SE23.5}
\]
This is one event coordinate formed from all sixteen Gamma sheets,
not four independent coordinates whose overlapping energies are added.
The polynomial's mixed terms are retained exactly. Since u/q=phi,
\[
 d=\sum_{k=0}^{15}\{\phi K_kq-K_k(q\phi)\}.                  \tag{SE23.6}
\]
All coefficients are rational. For a nonresonant monomial z^p,
\[
 K_k z^p=\frac{2\beta_k}{((p+3)/2)^2-\beta_k^2}
                \big(z^{4k+4}-z^{p+6}\big).                 \tag{SE23.7}
\]
**Proof.** Split the kernel integral at y=x and integrate both
exponentials; the reflected term enforces the zero boundary at x=0.
Equivalently, after removing the external factor exp(-3x/2), this
is the unique decaying Dirichlet solution of
(-partial_x^2+beta_k^2)y=2 beta_k exp(-(p+3)x/2).
The exponents in q and q phi are odd, so none resonates with
2 beta_k=4k+1. QED.

For polynomial coefficients u_i,d_j the event energy is the exact
positive rational number
\[
 E=\sum_{i,j}\frac{2u_i d_j}{i+j}
   =0.00448837106175764888956396267309\ldots.                  \tag{SE23.8}
\]
The full rational and every coefficient of d appear in the result
file. The response has d(1)=0; r=v-d has degree 72 and vanishes
at z=0. The trial was selected by exploratory arithmetic; the final
certificate consumes only the rational polynomial (SE23.5).

## 3. Certify the remaining target, without inverting a sampled matrix

**Theorem 2 (residual-target certificate).** Suppose W>=w>0 and
E>0 as above. Define
\[
 C(u)=4\int_0^\infty\frac{|v-d|^2}{W}\,dx+\frac{4E}{1-\eta},
 \qquad A=M_W+(1-\eta)(d\otimes d)/E.                        \tag{SE23.9}
\]
Then 4|<v,h>|^2<=C(u)<h,Ah>. In particular C(u)<=B<1 implies
\[
 S_b+\eta I_X\succeq
 \min\{\eta,(1-B)w/(2+g_c)\}\,I_X,\qquad g_c=269/50.         \tag{SE23.10}
\]

**Proof.** Use the faithful augmented observation
\[
 \mathcal A h=(W^{1/2}h,\sqrt{1-\eta}\langle d,h\rangle/\sqrt E).
\]
The target v is recovered by pairing this vector with
(W^(-1/2)(v-d),sqrt(E/(1-eta))). The squared norm of this
recovery vector is C(u)/4. Cauchy--Schwarz proves the bound.
Theorem 1 and (SE23.3) keep every remaining source term nonnegative.
Retain 2 eta E_+ and use the unchanged native inequality
||Jh||_X^2<=(2+g_c)||h||^2+2E_+ to obtain (SE23.10). QED.

This is a certified recovery vector, not a claim that it minimizes
the target norm. The exact optimal retained burden is
4<v,A^(-1)v><=C(u); SE19's Schur formula is available but unnecessary
for accepting this rational witness. The cost 4E/(1-eta) is included;
the extra observation is not free positive energy.

## 4. Complete interval certificate

The unchanged inherited row algebra, complete prime-power head
(604 events through M=4096) and analytic tails establish the seed
W>=1/1000. On z in [0,1/64], use the full SE22.10--SE22.11 exterior
bound with the new eta and alpha. On [1/64,1], use SE22.9, the full
sixteen-mode Gamma polynomial and the shaped prime upper row.
There are 88 initial seed cells. Every accepted lower bound applies
throughout its cell, with valid inherited parent bounds on refinements.

Write r(z)=sum r_i z^i. Its nonnegative whole-cell target mass is
\[
 J_r(a,b)=\int_a^b\frac{8r(z)^2}{z}\,dz
       =\sum_{i,j}\frac{8r_i r_j}{i+j}
                         (b^{i+j}-a^{i+j}).                  \tag{SE23.11}
\]
The polynomial is constructed exactly; the primitive is evaluated
with outward 90-digit intervals. Cancellation in its coefficients
is enclosed at every arithmetic operation. Positivity permits
clipping a negative lower rounding endpoint to zero, never lowering
an upper bound. For each whole cell let ell_(a,b)>0 be its certified
W lower bound. Then
\[
 C(u)\le\frac{4E}{1-\eta}
       +\frac{J_r(0,1/64)^{\rm up}}{w_{\rm ext}}
       +\sum_{[a,b]}\frac{J_r(a,b)^{\rm up}}{\ell_{a,b}}.
                                                               \tag{SE23.12}
\]
The exterior numerator is included. Midpoints only prioritize work;
they never authorize an integral bound. All contributions are summed
as exact Fractions of outward upper endpoints. The replay checks
complete cell adjacency, all positive seed floors, and enclosure of
the exact total numerator mass by the summed cell mass intervals.

The final 4,495 cells, maximum depth 14, have minimum seed lower
bound greater than 0.00109824821382245. The result is
\[
 C(u)\le0.99499934919474752598869545372520\ldots<199/200.
                                                               \tag{SE23.13}
\]
The observation cost is enclosed at 0.04127237757938067944...,
and the entire outer target burden is below 7.106*10^(-8).
Taking B=199/200 in Theorem 2 gives the native floor 1/1476000
and proves (SE23.1). Negative count and nullity vanish for
eta>=113/200. Only nonnegativity, not a strict gap or zero nullity,
is asserted at the implied smaller shift 833939/1476000.

For the separate failure control, bound W from above on the same
cells. Put n_-=floor(b^(-2)), n_+=floor(a^(-2)). The complete base
row lower bound is
\[
 V_{1/2}\ge a^6(A_{1/2,n_-}+p_{5/2}^{lo})
 +b^{-2}T_{1/2,n_+}^{head,lo}
 +\sum_{n_-<n\le n_+}\min\{\Lambda(n)n^{3/2}a^6,
                         \Lambda(n)n^{-5/2}b^{-2}\}.          \tag{SE23.14}
\]
The auxiliary upper bound uses b^6(A_(7/2,n_-)+p_(11/2)^up),
the complete suffix at a^(-14), and the exact maximum
Lambda(n)n^(3/2) for every straddled auxiliary event. Consequently
V_alpha is bounded below by the larger of zero and
(V_(1/2)^lo-alpha b^6 V_(7/2)^up)/(1-alpha a^6).
Insert this in W for a whole-cell upper bound W^up. Then
\[
 \beta_0=4\int v^2/W\,dx
 \ge\sum_{[a,b]}J_v(a,b)/W_{a,b}^{up}
 >1.03640844707971711809>103/100>1.             \tag{SE23.15}
\]
The omitted exterior is nonnegative, so omission is lawful only in
this lower failure control. Thus the diagonal comparison really
fails at the new parameters; a negative lower enclosure is not
being misread as a negative witness. This does not assert a negative
direction of the actual source.

## 5. A moving observer with an explicit obstruction count

**Theorem 3 (source-attached activation and one crossing).** Keep
the certified eta, alpha, W, u and d. For t in [0,1] set
\[
 A_t=M_W+t(1-\eta)(d\otimes d)/E,\qquad Q_t=A_t-4v\otimes v.
                                                               \tag{SE23.16}
\]
This is a norm-continuous bounded self-adjoint Fredholm path, with
essential spectrum bounded below by w. If
b=<d,W^(-1)v> and g=<d,W^(-1)d>, its target budget is
\[
 \beta(t)=4\langle v,A_t^{-1}v\rangle
 =\beta_0-\frac{4t(1-\eta)|b|^2}{E+t(1-\eta)g}.              \tag{SE23.17}
\]
The negative count and nullity of Q_t are exactly
\[
 n_-(Q_t)=\mathbf1_{\{\beta(t)>1\}},\qquad
 \dim\ker Q_t=\mathbf1_{\{\beta(t)=1\}}.                     \tag{SE23.18}
\]
There is exactly one t_* in (0,1) at which the one-dimensional
kernel crosses in the positive direction. With negative-to-positive
crossings counted positively, the spectral flow is +1.

**Proof.** A_t>=wI, and Q_t differs from M_W by finite rank.
Multiplication verifies its rank-one inverse update and hence
(SE23.17). Congruence by A_t^(-1/2) gives I-4a_t tensor a_t with
a_t=A_t^(-1/2)v, proving (SE23.18) and Fredholmness. The endpoints
satisfy beta(0)>1.03 and beta(1)<=C(u)<0.995. Hence b is nonzero
and beta'(t)=-4(1-eta)E|b|^2/(E+t(1-eta)g)^2<0. A unique
crossing follows. At its kernel vector A_t^(-1)v the quadratic
crossing derivative is (1-eta)|<d,A_t^(-1)v>|^2/E>0. QED.

For the standard indefinite-component presentation of spectral flow,
one may stabilize Q_t to Q_t direct-sum (-I) on H direct-sum l2.
The extra summand has no zero crossings. This fits the path and local
spectral-projection setting of Phillips [1]. The elementary count
above proves the asserted value without an elliptic-manifold model
or an invocation of the Atiyah--Singer index theorem.

The observation is dynamic in an exact sense: use
mathcal A_t h=(W^(1/2)h,sqrt(t(1-eta)/E)<d,h>). At each t, the
unchanged source is Q_t plus the nonnegative residual
(1-eta)(D-t d tensor d/E), D_P and E_eta. Activating a coordinate
transfers already present energy into the observed comparison;
it does not add a term to the original equation.

Under a faithful unitary change of admitted chart U_t, transport
W, d and v together and replace Q_t by U_t Q_t U_t^dagger. The
counts at each t remain the same; for a norm-continuous transported
path so do its crossings. Changing the event coordinate's phase,
with the recovery coefficient transported as well, leaves its
rank-one energy and the certificate unchanged. A general
discarding measurement is not such a faithful transport.

The count is invariant under these representation changes; it is
not constant as new energy is resolved. Reversing the path reverses
the spectral-flow sign. An endpoint may move inside an invertible
region without creating an endpoint crossing, but arbitrary endpoint
motion is not authorized by homotopy invariance. The Fredholm index
of each self-adjoint Q_t is itself zero and does not prove positivity.
No orientation-free spectral flow or unrestricted Atiyah--Singer
extension is claimed.

## 6. Remaining endpoint obligation

The construction gives a strict complete-source certificate at a
smaller positive eta and executes the first actual residual coordinate
of SE19. It proves neither a rate to eta=0 nor an all-order stopping
rule for SE21. SE20's fixed-Gamma positive-seed obstruction remains;
the universal signed arithmetic inequality or a genuinely controlled
infinite complement is still required for the endpoint. SE21's V_16
zero-shift signs and the radius-21/25 support result are unchanged.

See the [replay](../../../proof_lab/endpoint_residual_observer_certificate.py),
[result](../../../proof_lab/ENDPOINT_RESIDUAL_OBSERVER_RESULT.json),
[controls](../../../proof_lab/test_endpoint_residual_observer_certificate.py),
[scope](SE23_SCOPE.md), [source record](SE23_SOURCE_RECORD.md)
and [pins](SE23_SOURCE_PINS.json). The unchanged required engine
gate still fails its pre-existing pin mismatch. No formal verification,
external review, global eta-zero sign, K0 or RH completion is asserted.

[1] John Phillips, *Self-Adjoint Fredholm Operators and Spectral Flow*,
Canadian Mathematical Bulletin 39(4), 460--467 (1996),
[doi:10.4153/CMB-1996-054-4](https://doi.org/10.4153/CMB-1996-054-4).
Used for the spectral-flow path convention and scope, not for an
unproved source positivity implication.
