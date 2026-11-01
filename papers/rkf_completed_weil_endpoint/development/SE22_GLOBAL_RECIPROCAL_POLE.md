# SE22: global reciprocal-pole certificate below 0.57

12 October 2026. Owner: Monty. Complete-source numerical development.

The new executed result is
\[
 \boxed{S_b+\frac{227}{400}I_X\succeq
        \frac1{1476000}I_X.}                       \tag{SE22.1}
\]
It holds for every complex odd state of the corrected native carrier,
not only SE21's sixteen observed directions. Thus the sufficient global
nonnegative shift improves from 10883/18450 to
\[
 \boxed{\eta_{\rm sufficient}=\frac{837629}{1476000}
        =0.56749932249\ldots <0.57.}               \tag{SE22.2}
\]
This remains a positive shift. Global eta=0, critical full-source
recovery, historical five-label attachment, K0 and RH are still open.
SE21's finite eta-zero certificate is preserved unchanged.

## 1. Source and observer contract

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the admitted T35/T40 graph representation. This stage
uses SE19's source and its already proved reciprocal target theorem.
It adds its first executed smaller-eta instance, not a renamed general
Schur, Cauchy--Schwarz or Birman--Schwinger theorem.

Use h=sqrt(2)f on the positive half-line, z=e^(-x/2), and retain
\[
 v(x)=\tfrac12(e^{-x}-e^{-2x}),\quad
 F[f]=4|\langle v,h\rangle|^2,\quad
 W_{\eta,\alpha}(z)=\eta(1+z^6)
           +(1-\eta)L_\Gamma(z)-V_\alpha(z).     \tag{SE22.3}
\]
L_Gamma is the exact sixteen-mode SE17 potential. The two weights are
q_Gamma(x)=e^(-x/2)(1-e^(-2x)) for x>0 and
q_alpha(x)=e^(-|x|/2)(1-alpha e^(-3|x|)) on the whole line. SE19
extends their source identity to every 0<=alpha<1; the new choice is
\[
 \eta=227/400,\qquad\alpha=103/200,\qquad
 w=1/1000,\qquad B=199/200.                       \tag{SE22.4}
\]
The native metric, actual pole target, prime translations and Gamma
energies are unchanged. In particular SE19.2 gives exactly
\[
 s[f]+\eta\|f\|_X^2
 =\int W|h|^2-4|\langle v,h\rangle|^2
   +(1-\eta)D_\Gamma[h]+D_{P,\alpha}[f]
   +\mathcal E_\eta[f],\qquad
 \mathcal E_\eta[f]\ge2\eta E_+[f].             \tag{SE22.5}
\]
Both D terms are the retained nonnegative complete squared differences.
No finite residual observation is used in this certificate (SE19's
n=0 case). Therefore no assertion about an unknown finite-observation
Schur complement is needed to obtain this positive-shift bound.

When W>=w, the exact pole observer on the seed-energy input is
\[
 \mathcal O_W u=2\langle W^{-1/2}v,u\rangle,
 \quad \mathcal O_W(W^{1/2}h)=2\langle v,h\rangle,
 \quad\|\mathcal O_W\|^2=\beta_0
 =2\int_0^1\frac{z^3(1-z^2)^2}{W(z)}dz.          \tag{SE22.6}
\]
This is a bounded source-specific observation on the admitted energy
space, not a new primitive Hilbert pairing. It keeps the complete
complex pole correlation. Replacing that square by independently
charged pointwise targets would lose the improvement below.

## 2. Whole-source theorem and exact native reserve

**Theorem 1 (certified global source sign at 227/400).** For the data
in (SE22.4),
\[
 W(z)\ge1/1000\quad(0<z\le1),\qquad
 \beta_0\le0.994999857226\ldots <199/200<1.        \tag{SE22.7}
\]
Consequently (SE22.1)--(SE22.2) hold for all f in X. The negative
count and nullity vanish at every eta>=227/400. At the smaller shift
in (SE22.2) only nonnegativity, not a strict native gap, is asserted.

**Proof after the numerical bounds in sections 3--4.** Weighted
Cauchy--Schwarz, with the actual single pole functional, gives
4|<v,h>|^2<=beta_0 int W|h|^2. Insert this in (SE22.5) to obtain
\[
 s[f]+\eta\|f\|_X^2
 \ge(1-B)w\|f\|_2^2+2\eta E_+[f].              \tag{SE22.8}
\]
The unchanged native graph comparison from SE16--SE19 is
||f||_X^2<=(2+g_c)||f||_2^2+2E_+[f], where g_c=269/50.
Here (1-B)w/(2+g_c)=1/1476000<eta. This proves (SE22.1) on X,
including its unobserved infinite directions. Subtracting its native
floor gives (SE22.2). Larger eta adds a positive native multiple.
QED, with the fully specified interval certificate below.

The exact target matters: for a fixed positive W, beta_0 is both
sufficient and necessary for positivity of M_W-4 v tensor v on the
admitted half-line. Its extremal response is W^-1 v. This sharp
comparison fact is SE19 Theorem 1; it is not necessity for the full
source, whose other square energies can supply more reserve.

## 3. Complete spatial and prime bounds

The unchanged M=4096 catalogue contains 604 prime powers. Both full
masses at exponents 5/2 and 11/2 retain their proved all-integer tails
from SE16--SE17. On each rational cell [a,b] in [1/64,1], the inherited
Gamma polynomial is evaluated by outward interval arithmetic, and the
complete prime row is bounded using SE17.14--SE17.15. Define
\[
 \ell_{a,b}=\operatorname{lower}\!\left[
  \eta(1+z^6)+(1-\eta)L_\Gamma(z)
     -U_\alpha(a,b)\right],\quad z\in[a,b].     \tag{SE22.9}
\]
The prime events straddling a cell's breakpoints are counted with the
inherited whole-cell bounds. A lower endpoint of this expression is
a lower bound on W everywhere in the cell. No sampled row minimum
is used as evidence.

For z in [0,1/64], use the existing entire exterior majorant
\[
 B_M=\frac{(16/15)\log M+4/9}{\sqrt M}
        +\frac{2\log M}{M\sqrt M}+\frac{p_{5/2}^{\rm up}}{M^3},
 \quad V_\alpha(z)\le\frac{B_M}{1-\alpha/M^3}.    \tag{SE22.10}
\]
If A(z)=sum a_j z^j is the SE17 Gamma polynomial numerator, then
|L_Gamma(z)|<=sum |a_j|64^(-j), since its denominator is at least one.
Thus on the complete unbounded physical exterior
\[
 W(z)\ge w_{\rm ext}:=\eta-(1-\eta)
          \sum_j|a_j|64^{-j}-\frac{B_M}{1-\alpha/M^3}>w.
                                                               \tag{SE22.11}
\]
All constants and tails are enclosed, including log M. The catalogue
cutoff does not truncate the actual source or its prime returns.

Starting with [1/64,1], the replay bisects until the entire seed cover
has ell_(a,b)>=w. This takes 75 initial cells. Later refinement may
inherit the larger of a child's new lower bound and its parent's
proved lower bound; both apply throughout the child.

## 4. Complete reciprocal integral, without quadrature samples

The exact nonnegative numerator mass on each rational cell is
\[
 J(a,b)=\int_a^b2z^3(1-z^2)^2dz
 =\left[\frac{z^4}{2}-\frac{2z^6}{3}+\frac{z^8}{4}\right]_a^b,
 \qquad J(0,1)=\frac1{12}.                       \tag{SE22.12}
\]
Consequently any certified positive seed cover gives
\[
 \boxed{\beta_0\le
      \frac{J(0,1/64)}{w_{\rm ext}}
       +\sum_{[a,b]}\frac{J(a,b)}{\ell_{a,b}}.}  \tag{SE22.13}
\]
Each numerator is integrated exactly; each reciprocal uses a positive
whole-cell lower bound. The exterior numerator is included as well.
The replay refines cells until this proved upper sum is strictly below
B. Its midpoint calculations only select which cell to refine. They
do not bound the integral, authorize acceptance or enter its upper sum.
A deliberate false-midpoint control checks this distinction.

The final 6,738 cells form an adjacent, complete partition, with maximum
bisection depth 14. The minimum certified seed lower endpoint exceeds
0.0011923621546793. Their exact masses plus the exterior equal 1/12.
The outward upper sum is
\[
 \beta_0\le0.99499985722595977134082550845520979256285062353848\ldots
                  <199/200.                    \tag{SE22.14}
\]
The [result](../../../proof_lab/ENDPOINT_RECIPROCAL_POLE_RESULT.json)
records the outward interval, full-tail data, cover statistics and
SHA-256 of every ordered cell, lower bound and contribution. The
[read-only replay](../../../proof_lab/endpoint_reciprocal_pole_certificate.py)
reconstructs and verifies the entire partition and checks its source
pins. The nine named replay checks and independent controls are scoped
in [SE22_SCOPE.md](SE22_SCOPE.md).

## 5. Why the earlier pointwise pole allocation misses this sign

Keep the same new eta and alpha, but restore the old fixed pole
allocation tau_c=(1/10)(1-z^6). Its comparison is Q=W-tau_c.
A complete two-sided row enclosure at the exact rational point z=3/4
gives
\[
 -0.029855760<Q(3/4)<-0.029806564<-29/1000.        \tag{SE22.15}
\]
This supplies an upper bound with a strictly negative sign; it is
not the invalid inference from a negative lower bound corrected in
the SE19 audit. Thus the older sufficient pointwise comparison fails
with these exact same weights and eta, while the whole reciprocal
target budget proves the source sign. No negative actual-source
witness is asserted. The gain comes from evaluating the actual pole
functional against its total seed energy.

## 6. Relationship to zero shift and next open condition

SE21's complete-source matrix signs on V_16 remain valid, and its
dense-family theorem still requires every order or a controlled
infinite complement. This stage does not extend that finite zero-shift
certificate to the full carrier. Instead, it improves the genuine
global positive-shift bound by executing an unused earlier theorem.

SE20's obstruction at eta<=1/14 still applies to this fixed-Gamma
diagonal seed. Hence repeating this n=0 budget or merely tuning alpha
is not an established path to eta=0. The selected direct endpoint
problem remains the complete signed arithmetic inequality of SE20,
equivalently the all-order SE21 source matrices. SE19's positive
residual observations remain available for improvements while their
seed hypothesis is certified. No convergence rate to zero is claimed.

No new local aperture, historical five-label closure, proof-assistant
verification or external review is asserted. The required unchanged
operator-engine pin check still fails as documented in the
[scope](SE22_SCOPE.md). Earlier results and pins are preserved; see
the [source record](SE22_SOURCE_RECORD.md) and [new pins](SE22_SOURCE_PINS.json).
