# SE45: variable jya, resolved curvature and a moving source

13 October 2026 (Asia/Kolkata). Author: Monty.

SE44 defines counting lines, native theta, the fixed-turn jya law and
fixed-source sine correction. This continuation allows the turn and the
source to change. It derives the extra readings needed to distinguish
angular sampling, observer calibration and a two-path curvature return.
It also supplies a finite refinement rule that recovers a lifted scalar
curvature flux even when the coarse terminal return is the identity.

The carrier is unchanged: typed Cut, derived cut scalars, the constant
marked unit Lambda, lawful counting translations and response lifts,
then the derived positive radial completion where angles are evaluated.
Write C(t), S(t) for SE44's native cosine and sine,
E(t)=C(t)I+S(t)J, and q=Pi_Sigma/2. The compass basis is (T,V), with
J T=V and J V=-T. An index n orders acquisitions; it is not physical time.
The algebraic and analytic mechanisms are standard identities proved here
on this native carrier, with no claim of external mathematical priority.

## 1. Theorem 1: variable-turn jya and its exact blind cases

Let x_n=(k_n,j_n)^T have fixed squared radius rho^2, with rho positive, and let

\[
x_{n+1}=Q_nx_n,\qquad
Q_n=c_nI+s_nJ=E(\alpha_n),\qquad c_n^2+s_n^2=1.
\tag{45.1}
\]

Then the two-channel rule and its division-free scalar consequence are

\[
\begin{aligned}
k_{n+1}&=c_nk_n-s_nj_n, & j_{n+1}&=s_nk_n+c_nj_n,\\
\boxed{s_{n-1}j_{n+1}
 -(s_{n-1}c_n+s_nc_{n-1})j_n+s_nj_{n-1}}&\boxed{=0}.
\end{aligned}
\tag{45.2}
\]

When s_(n-1) is nonneutral, two successive jya readings recover the
missing complementary response and predict the next reading:

\[
k_n=\frac{c_{n-1}j_n-j_{n-1}}{s_{n-1}}.
\tag{45.3}
\]

On the full two-channel response module this decoder exists precisely
when s_(n-1) is nonneutral. At a neutral s_(n-1), adding the complementary
reading k_n restores the response without dividing by that quantity.
Even on a fixed-radius circle, the two jya readings can be ambiguous.

**Proof.** Multiply (45.1). Its inverse gives
j_(n-1)=-s_(n-1)k_n+c_(n-1)j_n. Multiply the forward jya equation by
s_(n-1) and eliminate its k term to obtain (45.2). The two jya readings
are the rows (-s_(n-1),c_(n-1)) and (0,1) acting on x_n; their determinant
is -s_(n-1). This proves (45.3) and the exact rank statement. If the
previous turn is I, the states rho T and -rho T have the same two neutral
jya readings; a next turn J gives opposite jya readings. The row (1,0)
separates them. Norm multiplicativity preserves rho^2. QED.

For equal turns with s nonneutral, (45.2) reduces to SE44's jya law.
SE44 also proves that equal-turn law directly when s is neutral; dividing
(45.2) by s in that case would be invalid. In a moving calibrated frame
h_n, the local state is h_n^(-1)x_n, the step is
h_(n+1)^(-1)Q_n h_n, and both reading covectors are transported by h_n.
The same acquired numbers satisfy (45.2). Keeping a coordinate row fixed
after changing the frame instead changes the sensor.

## 2. Theorem 2: a chain can hide in frames; paired paths retain a return

For any sequence of invertible response steps A_n:E_n->E_(n+1), a
response-frame change h_n gives

\[
A_n^h=h_{n+1}^{-1}A_nh_n.
\tag{45.4}
\]

On an open chain, choose any initial frame and set h_(n+1)=A_nh_n.
Every transformed step is I. Thus an open chain modulo unrestricted
vertex frames has no nonidentity return obstruction. A known calibration
record can still recover its steps; the statement concerns the quotient
that forgets that record. It does not say that every physical change is
unobservable.

For two acquired paths P,Q:E_a->E_b with the same endpoints, define

\[
\Delta=P-Q,\qquad H=Q^{-1}P.
\tag{45.5}
\]

Then

\[
\Delta^h=h_b^{-1}\Delta h_a,\qquad
H^h=h_a^{-1}Hh_a,\qquad
\boxed{\Delta=0\ \Longleftrightarrow\ H=I}.
\tag{45.6}
\]

Complete cut/complement readings on a basis at the common input recover
P and Q in their recorded endpoint frames, hence H. Its identity verdict
does not depend on those frames. If H is nonidentity, the two paths cannot
both be made identity by one consistent choice of their endpoint frames.

**Proof.** The recursion for h proves the chain assertion. Substitution of
P^h=h_b^(-1)P h_a and Q^h=h_b^(-1)Q h_a gives (45.6); the common terminal
frame cancels in (Q^h)^(-1)P^h. Invertibility of Q gives the equivalence.
Adding accepted and complementary outputs recovers every response column,
which is the existing SE41 observation contract. QED.

For a calibrated general orbit Z_(n+1)=V_n Z_n, invertible matrix readings
recover V_n=Z_(n+1)Z_n^(-1). The exact second-order identity is

\[
Z_{n+1}-(V_n+V_{n-1}^{-1})Z_n+Z_{n-1}=0.
\tag{45.7}
\]

This is a variable-step identity, not by itself a curvature diagnosis.
A single probe need not recover an operator. Nor does one identity-valued
finite loop prove local flatness: its terminal response may have lost a
full turn. The next two theorems supply a specified curvature target and
a faithful way to retain its scalar lift.

## 3. Theorem 3: inhomogeneous counting curvature has an exact jya flux

Use the existing counting formula product. In its faithful normal-count
chart write x,y for the T,V count coordinates. For any counting polynomial
g(x,y;Lambda), specify the response lifts

\[
\nabla_T=D_T,\qquad \nabla_V=D_V+gJ,
\qquad F_{TV}=fJ,\quad f=D_Tg.
\tag{45.8}
\]

Take a rectangle with initial count coordinates (x,y) and positive side
lengths a,b. Use SE44's horizontal response convention P'=-A(path)P.
Let P travel first in T then V, and Q first in V then T. Horizontal T
transport is I; vertical transport at T=u is E(-K(u)), where

\[
K(u)=\int_y^{y+b}g(u,v;\Lambda)\,dv.
\]

The paired return at the initial corner is exactly

\[
\boxed{H=Q^{-1}P=E(\Omega),\qquad
\Omega=-\int_x^{x+a}\int_y^{y+b}f(u,v;\Lambda)\,dv\,du.}
\tag{45.9}
\]

Consequently its acquired circular responses are C(Omega), S(Omega),
and the labelled first mixed reading satisfies

\[
\boxed{[ab]S(\Omega)=-f(x,y;\Lambda).}
\tag{45.10}
\]

The minus sign belongs to the stated forward horizontal transport and
P/Q orientation. SE42's displayed positive-flow commutator uses a
different convention and has mixed coefficient +F. These are not silently
identified. Reversing the compared paths inverts H.

**Proof.** SE42 gives F=(D_Tg)J. Along a vertical segment, all coefficient
matrices are multiples of the same J; native Euler differentiation gives
the unique transport E(-K). Thus P=E(-K(x+a)), Q=E(-K(x)). The native
addition law yields Omega=-(K(x+a)-K(x)). Counting antiderivatives are
obtained by raising each count exponent and dividing by that positive
integer. The fundamental difference identity gives (45.9) coefficientwise.
Omega has no term of degree below ab and its ab coefficient is -f;
S(Omega)=Omega-Omega^3/3!+... proves (45.10). QED.

This proof works formally in the step labels. For radial evaluations of
the polynomial coefficients, the displayed scalar integrals are finite
polynomial integrals and F00-E evaluates the Euler turns. No convergence
of an arbitrary noncommuting connection flow is inferred.

A concrete inhomogeneous family is

\[
g=\Lambda^2(x^2+xy)+\Lambda^3x,\qquad
f=\Lambda^2(2x+y)+\Lambda^3,
\]
\[
\boxed{\Omega=-ab\left[\Lambda^2(2x+a+y+b/2)+\Lambda^3\right].}
\tag{45.11}
\]

The symbols x^2,xy here denote the faithful normal-count presentation
of the formula product, not raw ordinary multiplication of falling-count
x variables. The Lambda^2 layer is invisible below unit depth two, even
though the full source curvature is nonneutral.

## 4. Theorem 4: finite subdivision repairs scalar full-turn blindness

After a radial evaluation, suppose a proved bound |f|<=M is available on
the rectangle. Partition it into finitely many axis-aligned cells R_k,
each with

\[
M\,\operatorname{area}(R_k)<\Pi_\Sigma.
\tag{45.12}
\]

Read the complete circular return of each cell, retaining its orientation
and transported J/pairing. There is a unique angle
omega_k in (-Pi_Sigma,Pi_Sigma) for that reading, and

\[
\boxed{\omega_k=-\int_{R_k}f,\qquad
\Omega=\sum_k\omega_k.}
\tag{45.13}
\]

Thus these refined readings determine the entire lifted scalar curvature
flux, including full turns invisible to the coarse H. Every further
partition satisfying (45.12) gives the same lifted sum. Such a finite
partition always exists for finite M and rectangle area: divide into N
equal strips with N>M area/Pi_Sigma. If M is neutral, Omega is neutral
directly. For a polynomial on a bounded box a finite M can be constructed
by bounding each coefficient times its coordinate powers.

**Proof.** Theorem 3 bounds each true cell angle in magnitude by M area.
SE44 proves that E is injective on the open interval (-Pi,Pi), so its
unique short angle is that true integral. Finite additivity of the
polynomial integral gives the sum and refinement independence. All cell
returns lie in one common J sector after their declared transport, so
the native addition law also gives H=product_k E(omega_k). The integer
part is obtained from the retained sum, not the final product. QED.

For example take f=q on a 2 by 2 count rectangle. Its coarse angle is
-4q=-2Pi, hence H=I. Four unit cells each have angle -q and return -J;
each bound q<Pi is strict. The four readings recover the nonneutral
lift -2Pi. A flat source also gives coarse H=I, but gives identity on
each of those cells. This is a finite observer distinction between two
sources with the same coarse terminal signal.

Without a bound excluding unobserved full turns within each cell, those
cell endpoints alone still have integer ambiguity. At equality in
(45.12), +Pi and -Pi already collide. This is an information requirement,
not a claim that every larger cell is impossible to decode with other
memory. The additive scalar theorem does not apply to arbitrary
noncommuting response sectors or unrecorded singular seams.

## 5. Theorem 5: exact source retention when the source itself changes

In any of the declared unital response algebras, let B_n, W_n and D_n
be invertible, set S_n=B_n W_n, and let the actual next source be
S_(n+1)=D_n S_n.
For any chosen invertible calibration correction R_n set

\[
\boxed{B_{n+1}=B_nR_n,\qquad
W_{n+1}=R_n^{-1}B_n^{-1}D_nB_nW_n.}
\tag{45.14}
\]

Then B_(n+1)W_(n+1)=S_(n+1) exactly, without any commutation assumption.
All factors must be expressed in their common transported response
algebra. Complete source readings determine D_n=S_(n+1)S_n^(-1);
an unmeasured future D_n is not thereby predicted.

**Proof.** Multiply the two expressions in (45.14) and cancel the adjacent
inverse pairs in their given order. This yields D_n B_n W_n. Omitting
B_n^(-1)D_nB_n in favor of D_n need not preserve the source. QED.

This extends the fixed-source identity used in SE41/SE44. It is an exact
accounting law for noncommuting returns, not a convergence assertion for
every matrix feedback. The next theorem gives a convergence and tracking
statement in the already defined scalar circular sector.

## 6. Theorem 6: sine tracking, drift bounds and the residual floor

Retain a chosen lifted source angle Phi_n and observer calibration beta_n.
Let e_n=Phi_n-beta_n and d_n=Phi_(n+1)-Phi_n. Allow a recorded prediction
hat d_n and a sine-reading error nu_n in the update

\[
\beta_{n+1}=\beta_n+S(e_n)+\nu_n+\widehat d_n.
\]

The exact relative reading evolves by

\[
\boxed{e_{n+1}=e_n-S(e_n)+w_n,\qquad
w_n=d_n-\widehat d_n-\nu_n.}
\tag{45.15}
\]

Choose 0<r<q. If |e_0|<=r and |w_n|<=delta<=S(r), then |e_n|<=r
for all n. Set L=1-C(r), so 0<L<1. The quantitative bounds are

\[
\boxed{|e_{n+1}|\le |e_n|^3/6+|w_n|,}
\qquad
\boxed{|e_n|\le L^n|e_0|+\sum_{k=0}^{n-1}L^{n-1-k}|w_k|.}
\tag{45.16}
\]

If w_n tends to the neutral value, e_n does too. With only the uniform
bound delta, the sharper asymptotic statement is

\[
\boxed{\limsup_n|e_n|\le e_\delta,\qquad
e_\delta\in[0,r],\quad S(e_\delta)=\delta.}
\tag{45.17}
\]

The value e_delta is uniquely defined by the native monotonic sine on
[0,r]. The bound is attained by the constant disturbance w_n=delta
with e_0=e_delta. A persistent uncancelled angular advance therefore
need not converge to neutral tracking error. With exact prediction of
the advance and exact sine readings, w_n is neutral and SE44's cubic
correction is recovered even while the source keeps moving.

**Proof.** Subtract the two angle updates for (45.15). Write
F(t)=t-S(t). Native differentiation gives F'=1-C, whence F is odd,
nondecreasing and L-Lipschitz on [-r,r], with F(r)=r-S(r).
Thus |F(e)+w|<=F(r)+delta<=r, proving invariance. SE44's cubic estimate
gives the first bound in (45.16); |F(e)|<=L|e| and induction give the
second. For w_n->0, split the weighted sum at a large fixed index:
the finite initial terms decay, and the remaining terms are at most
sup_(k>=N)|w_k|/(1-L). This proves convergence to neutral error.

For (45.17), the scalar envelope t_0=r,
t_(n+1)=F(t_n)+delta bounds |e_n| by induction. It decreases from r
towards the unique fixed point e_delta, because S is strictly increasing
on [0,r]. Completeness and continuity give its limit and the equation
S(e_delta)=delta. Substitution verifies sharpness. QED.

Setting B_n=E(beta_n), W_n=E(e_n), D_n=E(d_n) and
R_n=E(S(e_n)+nu_n+hat d_n) in (45.14) retains E(Phi_n) at every step.
The lifted Phi/beta records retain the integer part as well. Bounds on
prediction and sensor error must come from their declared readings or
source bounds; closure alone does not measure them.

## 7. What the development now distinguishes

| Reading | Recoverable target and required retained data |
| --- | --- |
| Two successive jya values | Current two-channel state when the previous turn has nonneutral sine; otherwise add its complementary channel |
| One open chain modulo free frames | No return obstruction; retain calibration to recover its actual steps |
| Two paths with common endpoints | Full return up to base-frame conjugacy, from complete path-response columns |
| Refined circular cell returns | Lifted scalar curvature flux when the proved per-cell bound excludes a full-turn alias |
| Sine feedback on a moving source | Tracking error controlled by actual advance, prediction and reading error; exact source retained separately |

The [replay](../../proof_lab/tvsp_variable_jya.py) and
[saved readings](../../proof_lab/TVSP_VARIABLE_JYA_RESULT.json) provide
finite exact instances and outward rational tracking enclosures.
The [scope](SE45_SCOPE.md) records their limits separately from these
general written proofs. This construction selects no universal physical
TVSP connection and changes no RH source, eta certificate or mass gap.
