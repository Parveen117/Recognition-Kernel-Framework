# SE44: TVSP counting lines, native angle and the retained jya law

13 October 2026 (Asia/Kolkata). Author: Monty.

SE42 supplies counting curvature and SE43 supplies lawful movement across
seams. This chapter now defines counting lines, constructs their angle
unit from the native quarter-turn, and derives the sine-difference law
with its observer and seam memory. It also proves the literal sine
correction proposed in the supplied notes, on its correct attraction
branches and with the original source retained.

The existing F00-E factorial construction already supplies native Euler,
sine and cosine. Its fundamental period was explicitly deferred. Theorem 2
below closes that particular normalization step in its completed radial
field. The methods are standard translation, Cayley, integral and recurrence
identities derived here on the declared native carriers; no external
mathematical priority is claimed.

## 1. The carrier and the orientation actually used

Use the established completed ordered radial field R_Sigma, its cut-complex
field C_Sigma and derived iota^2=-1. Extend SE42's counting formula algebra
to R_Sigma[Lambda], keeping Lambda central and constant. Its independent
lowering actions are D_T,D_V. The compass direction module has basis
e_T,e_V, with e_S=-e_T and e_P=-e_V. Define the represented quarter-turn by

\[
J e_T=e_V,\quad J e_V=-e_T,\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}_{(T,V)}.
                                                        \tag{44.1}
\]

It sends T -> V -> S -> P -> T, clockwise in the supplied compass.
The ordered basis here is (T,V), not the drawing's (horizontal,vertical)
basis. The quarter-turn action and scalar iota have distinct types.

The map a e_T+b e_V -> a+iota b transfers the already derived native
cut norm to this direction module:

\[
\langle u,v\rangle=u_Tv_T+u_Vv_V,
\qquad \omega(u,v)=\langle Ju,v\rangle
                  =u_Tv_V-u_Vv_T.                    \tag{44.2}
\]

These are dimensionless counting directions carrying compass labels;
raw temperature and volume are not added as if they shared physical
units. The calibration is transported with a moving frame. The primitive
typed Cut, a neutral angle coordinate, an additive-neutral operator and
an identity map remain different objects.

## 2. Theorem 1: counting lines and their response lifts

For v=a e_T+b e_V, with a,b in R_Sigma, set D_v=aD_T+bD_V and let tau_(tv) be SE43's
product-preserving translation exp(tD_v). On each counting polynomial the
sum is finite. A counting point is an R_Sigma[Lambda]-algebra character
chi from the formula algebra to R_Sigma[Lambda]. The line through it,
with parameter t in R_Sigma and direction v, is the orbit

\[
\boxed{\ell_{\chi,v}(t)(f)=\chi(\tau_{tv}f).}         \tag{44.3}
\]

For the characters chi_q(p_alpha)=q^alpha this reads q -> q+tv in the
faithful normal-count chart. It is not a claim that raw x-translation
preserves the falling-count product. Nonzero v gives a nonconstant line,
and tau_(sv)tau_(tv)=tau_((s+t)v). Rescaling v changes parametrization;
the unparametrized line does not retain the orientation v versus -v.

A supplied counting connection nabla_i=D_i+A_i determines the unique
formal response transport P(t) along this line by

\[
P'(t)=-\ell_{\chi,v}(t)(aA_T+bA_V)P(t),\qquad P(0)=I.
                                                        \tag{44.4}
\]

For a coefficient series A_v(t)=sum A_n t^n, its constructive rule is

\[
(n+1)P_{n+1}=-\sum_{k=0}^n A_kP_{n-k},\qquad P_0=I.
                                                        \tag{44.5}
\]

It is invertible as a formal series. Under a response-frame change h,
with h(t)=ell_(chi,v)(t)(h), it transforms as

\[
P^h(t)=h(t)^{-1}P(t)h(0).                             \tag{44.6}
\]

**Proof.** The translation laws follow from SE43's binomial derivation,
and applying the character to the degree-one count basis gives q+tv.
This is nonconstant when v is nonneutral. Comparing formal coefficients
in (44.4) gives (44.5) and uniqueness. A formal inverse exists since
P_0=I, or is recursively obtained from Q'=Q A_v and Q(0)=I.
Differentiate the right side of (44.6), using the full SE42 connection
transformation, to obtain (44.4) in the new frame. Its initial value is I,
so uniqueness proves the formula. QED.

Thus a counting line and the transport of a response along it are
different defined objects. Equation (44.4) is a formal local construction;
it does not assert convergence of every polynomial-connection flow.
No Riemannian geodesic is assumed in defining (44.3).

## 3. Theorem 2: native theta and the quarter-turn period

For r in the native radial field define the rational turn

\[
Q(r)=(I+rJ)(I-rJ)^{-1}
     =\frac{1-r^2}{1+r^2}I+\frac{2r}{1+r^2}J.
                                                        \tag{44.7}
\]

Its inverse is Q(-r), it preserves (44.2), and Q(1)=J. Define, initially
for 0<=r<=1,

\[
\vartheta(r)=\int_0^r\frac{2\,dt}{1+t^2},\qquad
q_\Sigma=\vartheta(1),\qquad
\Pi_\Sigma=2q_\Sigma.                                \tag{44.8}
\]

The integral is the limit of finite native cut-rational partition sums,
extended to radial endpoints in the completed field. It does not import
a prior circle, pi or arctangent. Then

\[
\boxed{Q(r)=\operatorname{Cos}_\Sigma(\vartheta(r))I
                   +\operatorname{Sin}_\Sigma(\vartheta(r))J.}
                                                        \tag{44.9}
\]

The native Euler turn has least positive period 4q_Sigma=2Pi_Sigma.
It parametrizes every unit pair (c,s), c^2+s^2=1. In particular its
quarter, half and full turns are J,-I,I. Under the classical real chart
Pi_Sigma has the ordinary value pi; that chart is a conclusion, not the
input used to normalize the turn.

For nonzero directions u,v set

\[
c(u,v)=\frac{\langle u,v\rangle}{\|u\|\|v\|},\qquad
s(u,v)=\frac{\omega(u,v)}{\|u\|\|v\|}.               \tag{44.10}
\]

Their native angle theta is the unique class modulo 2Pi_Sigma satisfying
(c,s)=(Cos_Sigma(theta),Sin_Sigma(theta)). A path-resolved angle retains
the extra integer m:

\[
\Theta=\theta_{\rm pr}+2\Pi_\Sigma m,\qquad
0\leq\theta_{\rm pr}<2\Pi_\Sigma.                    \tag{44.11}
\]

The integer is acquired from the oriented path/crossing record, not
inferred from the terminal phase. An unoriented line loses an additional
half-turn: its direction angle is only a class modulo Pi_Sigma.

**Proof.** Multiplication by I+rJ proves (44.7); J^2=-I proves its inverse
and norm identity. For w(t)=2/(1+t^2), the exact difference formula and
2|t|<=1+t^2 imply |w(t)-w(s)|<=2|t-s|. Upper and lower sums on an
interval of length L therefore differ by at most 2L times the mesh.
Refining finite partitions gives a native Cauchy sequence; the completed
field supplies the integral. The same bound on a short increment proves
vartheta'=w. Also 1<=w<=2 on [0,1], so vartheta is strictly increasing
and maps [0,1] onto [0,q_Sigma].

Direct rational differentiation gives Q'=w JQ. F00-E gives the derivative
of E_J(t)=Cos_Sigma(t)I+Sin_Sigma(t)J and E_J(-t)E_J(t)=I.
Consequently d[E_J(-vartheta(r))Q(r)]/dr=0, and its value at r=0 is I.
This proves (44.9) using the native completed-field calculus. At r=1
it gives E_J(q_Sigma)=J, hence E_J(4q_Sigma)=I by F00-E's addition law.

The rational pair in (44.7) maps [0,1] bijectively to the closed first
quarter of the unit circle: the inverse is r=s/(1+c). Multiplication
by J covers the other three quarters. Strict increase of vartheta and
the distinct interiors of these four quarters show that no t strictly
between 0 and 4q_Sigma has E_J(t)=I. Translating by whole periods proves
the exact period kernel and the asserted angle classification.
The two-dimensional determinant identity proves c^2+s^2=1 in (44.10).
The period kernel gives (44.11); v and -v differ by the half-turn.
QED.

For an invertible frame h put u'=h^(-1)u, v'=h^(-1)v, J'=h^(-1)Jh and
G'=h^T h. Using G' for the transported pairing makes both c and s in
(44.10) unchanged. Thus theta is independent of the response-frame
coordinates when the pairing and orientation travel with them. Keeping
the Euclidean coordinate dot product after a nonorthogonal frame change
would instead change the measurement.

### Constructive angle readings without a transcendental oracle

Finite geometric division inside (44.8) gives, for 0<=r<=1,

\[
\vartheta(r)=2\sum_{k=0}^{N}\frac{(-1)^k r^{2k+1}}{2k+1}
             +\epsilon_N,
\quad |\epsilon_N|\leq\frac{2r^{2N+3}}{2N+3},
\quad (-1)^{N+1}\epsilon_N\geq0.                     \tag{44.12}
\]

Indeed the remaining integrand is 2(-1)^(N+1)t^(2N+2)/(1+t^2).
The Cayley addition rule gives Q(1/2)Q(1/3)=J. Both corresponding angles
are in (0,q_Sigma), so their sum is q_Sigma, not another period lift.
Equation (44.12) at 1/2 and 1/3 therefore encloses q_Sigma efficiently.
These rational enclosures are used by the replay.

## 4. Theorem 3: the native jya table and its difference rule

Let Q=cI+sJ be one retained, fixed turn with c^2+s^2=1. Repetition defines

\[
Q^n=c_n I+s_nJ,\qquad c_0=1,\ s_0=0.
\]

Multiplication gives the exact count rule

\[
\binom{c_{n+1}}{s_{n+1}}
 =\begin{pmatrix}c&-s\\s&c\end{pmatrix}
  \binom{c_n}{s_n},\qquad c_n^2+s_n^2=1.              \tag{44.13}
\]

For a positive jya calibration rho define j_n=rho s_n and
d_n=j_n-j_(n-1). Then

\[
\boxed{j_{n+1}-2j_n+j_{n-1}=-\kappa j_n,\qquad
       d_{n+1}=d_n-\kappa j_n,\quad \kappa=2(1-c).}   \tag{44.14}
\]

Equivalently,

\[
\boxed{j_{n+1}=j_n+j_1-\kappa\sum_{m=1}^n j_m.}     \tag{44.15}
\]

For Q=Q(r), all table entries are exact cut-rational values when r and
rho are cut-rational, and

\[
\kappa=\frac{4r^2}{1+r^2}.                           \tag{44.16}
\]

In the angle chart, c_n=Cos_Sigma(n theta) and s_n=Sin_Sigma(n theta).

**Proof.** Expand Q(c_n I+s_nJ), using J^2=-I, for (44.13). Norm
multiplicativity gives its invariant. Since Q+Q^(-1)=2cI, multiplication
by Q^n gives Q^(n+1)-2cQ^n+Q^(n-1)=0. The J coefficient, multiplied
by rho, gives (44.14). Summing its difference identity from 1 to n
gives (44.15). Substituting (44.7) gives (44.16); the angle statement is
F00-E's addition law. QED.

This is the native counterpart of the sine-table difference mechanism
in the historical Surya Siddhanta passage. Its coefficient is derived
from the actual turn, not imposed as a universal numerical divisor.
The nonlinear correction theta -> theta+Sin(theta) is a different
operation, treated in Theorem 6. Repeating a fixed turn does not normally
stabilize: the table records an orbit, while a feedback rule changes a
relative reading.

## 5. Theorem 4: the same law for operator returns and moving observers

Let U be any supplied invertible native response operator, including a
closed ordered loop acquired by SE42 or SE43. Define

\[
C_U=(U+U^{-1})/2,\qquad E_U=(U-U^{-1})/2.
                                                        \tag{44.17}
\]

These commute with U and with one another; C_U^2-E_U^2=I. For
Y_n=U^nY_0, and also for the reversal-odd sequence
E_n=(U^n-U^(-n))/2, the exact operator difference rule is

\[
Y_{n+1}-2C_UY_n+Y_{n-1}=0,\qquad
D_{n+1}=D_n-2(I-C_U)Y_n.                              \tag{44.18}
\]

Here D_n=Y_n-Y_(n-1). The reversal-odd name refers to path inversion;
it does not identify this split with the separate EMK cut grading.
For U=cI+sJ the operator law reduces to (44.14). A general U need not
have one scalar theta or a circular orbit.

Now let G_n:mathcal E_n->mathcal E_* be declared invertible observer calibrations and
write y_n=G_n^(-1)U^n y_*. Set

\[
P_n=G_{n+1}^{-1}G_n,\qquad C_n=G_n^{-1}C_UG_n,
\qquad \delta_n=y_n-P_{n-1}y_{n-1}.
\]

The frame-correct form of the jya difference mechanism is

\[
\boxed{\delta_{n+1}
       =P_n\bigl[\delta_n-2(I-C_n)y_n\bigr].}        \tag{44.19}
\]

With the initial pair y_0=G_0^(-1)y_* and
y_1=G_1^(-1)UG_0y_0 this recurrence uniquely reconstructs the entire
constant-return orbit. The construction concerns calibrations along the
specified acquisition path; it does not erase the loop's global seam
memory by asserting a trivialization over every path.

For actual varying steps z_(n+1)=V_n z_n in the common reference,
z_n=G_n y_n, the residual in the second-order version of (44.19) is

\[
\begin{aligned}
\mathcal R_n
 &=y_{n+1}-2P_nC_ny_n+P_nP_{n-1}y_{n-1}\\
 &=G_{n+1}^{-1}
 \bigl[(V_n-U)+(V_{n-1}^{-1}-U^{-1})\bigr]z_n.        \tag{44.20}
\end{aligned}
\]

Thus a mismatch is a specific reading of changed forward and backward
steps. It is not automatically the curvature two-form or a uniquely
identified physical error.

**Proof.** All identities in (44.17)--(44.18) follow by multiplying
U+U^(-1) by its powers; no commutation between the factors originally
used to construct U is needed. Transport the second-order identity by
G_(n+1)^(-1), insert G_n G_n^(-1) and G_(n-1)G_(n-1)^(-1), and collect
the two covariant differences to obtain (44.19). Its forward coefficient
is I, so the given two initial readings determine every later reading.
For (44.20), substitute z_(n+1)=V_n z_n and
z_(n-1)=V_(n-1)^(-1)z_n before subtracting U+U^(-1). QED.

For example, SE43's central integer return U=I+E_13 has C_U=I and
U^n=I+nE_13. It satisfies the operator recurrence while its retained
integer memory grows. Labelling this a stabilized circular sine table
would lose exactly the sector that the observer must retain.

## 6. Theorem 5: attaching the jya to actual counting curvature

On a two-channel counting response module choose the existing quarter-turn
J and the lawful counting lifts

\[
\nabla_T=D_T,\qquad
\nabla_V=D_V+f(\Lambda)X_TJ,
\qquad f(\Lambda)\in R_\Sigma[\Lambda].
\]

SE42's derived commutator [D_T,X_T]=I and its central-return theorem give

\[
F_{TV}=f(\Lambda)J,\qquad
\mathcal H(a,b)=\operatorname{Exp}(ab f(\Lambda)J).
                                                        \tag{44.21}
\]

For the specified orientation of the SE42 word the lifted loop angle is
Theta_loop=ab f(Lambda). Hence its acquired two response coordinates are

\[
c_{\rm loop}=\operatorname{Cos}(ab f(\Lambda)),\quad
s_{\rm loop}=\operatorname{Sin}(ab f(\Lambda)),\quad
\boxed{[ab]s_{\rm loop}=f(\Lambda).}                 \tag{44.22}
\]

Formal coefficients make these identities meaningful before numerical
evaluation. On evaluating the scalar parameters in the completed radial
field, F00-E evaluates the displayed matrix return. No general numerical
connection-flow convergence is inferred. Repetitions of this very return
obey (44.14); the curvature-to-jya attachment is now explicit for this
family, rather than an identification by analogy.

**Proof.** The two lift commutator is fJ. It commutes with both lifts,
because J is constant and the remaining response coefficient is a scalar
multiple of J. SE42 therefore gives the exact formal exponential in
(44.21). Separate its even and odd powers to get (44.22). The term
linear in ab is ab f, proving the coefficient claim. Theorem 3 applies
to the resulting fixed return. QED.

Complete accepted and complementary readings of H e_T recover c_loop
and s_loop in the calibrated (T,V) frame. The sine alone is not a
faithful detector: at Theta_loop=Pi_Sigma, s_loop=0 but H=-I. Both phase
coordinates still miss full turns at Theta_loop=2Pi_Sigma m. The
path/branch integer in (44.11), or the labelled mixed coefficient in
(44.22) for the curvature target, must be retained. For f=Lambda^h,
depths below h miss the first nonneutral curvature reading. Counting
memory and integer winding are separate retained labels.

This special family does not turn every SE42/SE43 return into one scalar
angle. For a general matrix return the full operator law (44.18) remains
available. Neither a trace, a sine nor a principal phase is substituted
for all of its response channels.

## 7. Theorem 6: native sine correction with branch and source retained

For a relative angular error e_0 with |e_0|<Pi_Sigma define

\[
\boxed{e_{n+1}=e_n-\operatorname{Sin}_\Sigma(e_n).}    \tag{44.23}
\]

The errors keep their sign, decrease in magnitude to the neutral error,
and satisfy the global-on-this-branch cubic bound

\[
\boxed{|e_{n+1}|\leq |e_n|^3/6.}                    \tag{44.24}
\]

For a fixed lifted source angle Phi, let beta_n=Phi-e_n,
B_n=E_J(beta_n) and W_n=E_J(e_n). The correction can be executed on its
acquired sine reading s_n=Sin_Sigma(e_n):

\[
B_{n+1}=B_nE_J(s_n),\qquad
W_{n+1}=E_J(-s_n)W_n,\qquad
\boxed{B_nW_n=E_J(\Phi)\text{ for every }n.}         \tag{44.25}
\]

With the chosen lift retained, beta_n -> Phi. Thus the observer's
calibration converges while the source return remains reconstructed.
It does not make the original connection flat or remove its integer
seam history.

For the supplied-note update theta_+=theta+Sin_Sigma(theta), each open
interval (2m Pi_Sigma,2(m+1)Pi_Sigma) converges to its odd-half-turn
(2m+1)Pi_Sigma. The even-half-turn endpoints are fixed but repelling
from within these intervals. At e=+/-Pi_Sigma the relative-error rule
(44.23) is fixed at a nonidentity antipode; sine silence alone must not
be accepted as successful calibration.

**Proof.** Theorem 2 gives Sin_Sigma(t)>0 for 0<t<Pi_Sigma. The circular
differential identities give

\[
e-\operatorname{Sin}_\Sigma(e)
 =\int_0^e[1-\operatorname{Cos}_\Sigma(t)]dt.
\]

For positive e on that interval this lies strictly between 0 and e.
The positive errors decrease to a limit l>=0 by native order completeness.
Continuity gives Sin_Sigma(l)=0, and l<=e_0<Pi_Sigma forces l=0.
Oddness proves the negative-error case. On this branch Sin(t)<=t,
so 1-Cos(t)=integral_0^t Sin(u)du<=t^2/2. Integration yields (44.24).
The source identity and update in (44.25) follow from F00-E's addition
law in the fixed J subalgebra. Finally put
theta=(2m+1)Pi_Sigma+e and use E_J(Pi_Sigma)=-I: the note update is
exactly (44.23) in e. Its even-half-turn derivative is 1+Cos(0)=2,
whereas the odd-half-turn derivative is neutral. QED.

The literal sine feedback above was not proved by merely comparing its
cubic Taylor coefficient with SE41. It now has a defined native angle,
a proved branch domain, convergence and retained source identity.
SE41's rational Cayley feedback remains a distinct, already available
implementation; its proof and certificates are unchanged.

## 8. Observer and publication boundary

The [saved readings](../../proof_lab/TVSP_NATIVE_JYA_RESULT.json) include
exact rational direction/phase banks, table entries, a changing-frame
operator orbit, a noncircular integer-memory orbit, formal curvature
coefficients, and outward rational enclosures for the literal sine
feedback. The decoder uses acquired responses and declared calibration
metadata. A numerical principal angle does not reconstruct unrecorded
winding or a hidden operator channel.

The new development supplies a precise counting-line and angular
construction on the stated TVSP-labelled carrier. It does not prove
that arbitrary thermodynamic or double-helical motion has this constant
turn law. The two-form curvature, its integrated return, the jya reading
and the calibration error are typed, connected quantities, not one
quantity under four names. Scalar d(df/f) remains neutral where defined;
it is not used as a nonzero operator curvature.

The historical sine-difference mechanism motivates the name; the exact
operator extension and observer feedback are the constructions proved
here. Atomic quantization, the periodic table, RH positivity and a
Yang--Mills gap are not consequences of these proofs. The actual RH eta
remains 1079/2000, with floor 1/492000, and the universal sign remains open.
