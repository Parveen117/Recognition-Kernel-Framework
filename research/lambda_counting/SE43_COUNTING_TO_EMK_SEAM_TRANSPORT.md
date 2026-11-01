# SE43: counting-to-EMK movement and ordered seam memory

13 October 2026 (Asia/Kolkata). Author: Monty.

This stage consumes existing curvature and helical-memory results instead
of deriving the same curvature a second time. SE42 constructs a counting
instance of the connection calculus already present in EMK-C1. EMK-G3
already separates local flatness from global sheet return. The additional
task here is an explicit movement adapter: which counting translations,
response lifts and seam identifications can be composed without losing
the ordered response? The result is algebraic. A topological or physical
realization is a further admitted presentation, not a premise.

## 1. What is reused, and what the circle dictionary requires

The [source comparison](SE43_SOURCE_RECORD.md) binds the public sources.

| Existing object | Status in this development |
| --- | --- |
| EMK-C1 connection curvature and frame covariance | Reused mechanism; SE42 is its counting-carrier instance with commuting derivations |
| EMK-G1 metric curvature | Different target, requiring its declared metric; no identification with SE42 is made |
| EMK-G2/G3 quotient, monodromy and retained sheet | Reused global distinction; local flatness does not erase a seam return |
| MR-03 cocycle-lifted path memory | Reused extension theorem; the integer example below is a concrete instance |
| Counting movement across a matrix-valued seam | The explicit adapter developed here |

The proposed point/circle dictionary has the following precise *conditional*
realization. If an admitted presentation retains an independent circle
fibre and uses product gluing, its projection pi:B x S^1 -> B gives:

| Object in the base presentation | Its full inverse image |
| --- | --- |
| One point | S^1 |
| A line R | R x S^1, a cylinder |
| A circle S^1 | S^1 x S^1, a torus |

These statements concern inverse images under a specified map. They do
not identify an arbitrary TVSP point with a classical circle. A quotient
or twisted seam can change the total object and its movement rules.
EMK-G3 retains phase, scale and integer sheet sectors; dropping those
extra sectors to draw a torus need not be faithful. Neither the product
table nor this chapter proves the complete TVSP/double-helical adapter.
The checked sources establish a helical mapping-torus model, not that
every object named a torus has the same transition law.

## 2. Theorem 1: the lawful counting translation is not raw x-translation

Use SE42's algebra B over Q_Sigma[Lambda], with constant marked unit,
formula product p_alpha bullet p_beta=p_(alpha+beta), and derived lowering
D_i p_alpha=alpha_i p_(alpha-e_i). Its faithful coefficient chart is
U(y^alpha)=p_alpha(x). Let L be a cut-rational constant. Define

\[
\tau_{i,L}=U\,[f(y)\mapsto f(y+Le_i)]\,U^{-1}.
                                                        \tag{43.1}
\]

Then tau_(i,L) is an automorphism for bullet, commutes with every D_j,
has inverse tau_(i,-L), and

\[
\tau_{i,L}=\sum_{n\geq0}\frac{L^nD_i^n}{n!},\qquad
\tau_{i,L}\tau_{i,M}=\tau_{i,L+M}.             \tag{43.2}
\]

The sum is finite on each polynomial. Translations in different slots
commute. This requires no numerical exponential of a response connection.

**Proof.** Apply the binomial formula to each y^alpha and transport it
through U. Ordinary translation preserves products in that coefficient
chart and commutes with the coordinate derivatives. SE42's intertwining
identities transfer each assertion to bullet and D. Local nilpotence of
D_i on finite counting polynomials makes (43.2) an exact finite sum. QED.

In one slot p_1=x and p_2=x^2-Lambda x. Raw x-translation R_L, in
contrast, satisfies

\[
R_L(p_1\bullet p_1)-(R_Lp_1)\bullet(R_Lp_1)
 =-\Lambda L.                                        \tag{43.3}
\]

Indeed the first term is (x+L)^2-Lambda(x+L), whereas the second is
x^2-Lambda x+2Lx+L^2. Thus raw translation fails the required product
law when Lambda L is nonneutral. The discrepancy disappears in the
degree-zero unit quotient, which is not equality before that quotient.
An EMK base displacement u -> u+L can be attached to (43.1) through the
normal counting coordinate y_i; identifying u with raw x instead changes
the movement rule. This is the first explicit adapter obligation.

## 3. Theorem 2: compatible seam lifts and moving response frames

Let E=B^r, let nabla_i=D_i+A_i be the SE42 response lifts, and let
tau_j be supplied commuting translations of (43.1). A seam lift is

\[
T_j s=g_j\bullet\tau_j(s),\qquad g_j\in GL_r(B).
                                                        \tag{43.4}
\]

Thus T_j is semilinear: T_j(f bullet s)=tau_j(f) bullet T_j(s).
It is invertible, with inverse tau_j^(-1)(g_j^(-1)) tau_j^(-1).
It intertwines every specified connection direction precisely when

\[
\boxed{D_i g_j+A_i\bullet g_j
       =g_j\bullet\tau_j(A_i).}                       \tag{43.5}
\]

Under this condition the curvature coefficients also intertwine:

\[
F_{ik}\bullet g_j=g_j\bullet\tau_j(F_{ik}).           \tag{43.6}
\]

For an invertible moving response frame h the simultaneous transport is

\[
A_i^h=h^{-1}\bullet D_i h+h^{-1}\bullet A_i\bullet h,
\qquad g_j^h=h^{-1}\bullet g_j\bullet\tau_j(h).
                                                        \tag{43.7}
\]

Compatibility (43.5) is preserved. Changing A without changing the seam,
or conjugating g without its shifted endpoint frame, need not preserve it.

**Proof.** Expand nabla_i(g_j tau_j s) by the counting Leibniz law.
Since D_i tau_j=tau_j D_i, the terms differentiating s cancel against
T_j nabla_i s. The remaining multiplication coefficient is the difference
of the two sides of (43.5). Its vanishing is necessary as well as sufficient
by evaluating it on each constant basis vector. Commuting T_j with the
two lifted directions gives (43.6). Finally h^(-1) nabla_i h and
h^(-1) T_j h give (43.7); conjugation preserves the intertwining identity.
Direct composition verifies the stated inverse. QED.

For a single seam the powers T^n, n in Z, are always defined. Writing
T^n=g_n tau^n gives the ordered cocycle

\[
g_{n+m}=g_n\bullet\tau^n(g_m).                         \tag{43.8}
\]

This is obtained by composing the two semilinear maps. It supplies a
matrix-valued cyclic lift; a one-generator monodromy group is not thereby
non-Abelian. In an admitted continuous cover, a constant g=H corresponds
to section condition H s(u+L)=s(u), equivalently the mapping-torus deck
action (u,f)->(u+L,H^(-1)f). A positive base circuit then has fibre return
H. The deck action and that positive return have opposite fibre signs.

## 4. Theorem 3: two seam orders decide descent, not local flatness alone

For two commuting scalar translations write

\[
a=g_1\bullet\tau_1(g_2),\qquad
b=g_2\bullet\tau_2(g_1),\qquad
\Delta=a-b,\qquad R=a\bullet b^{-1}.                  \tag{43.9}
\]

The displayed operator order is fixed: T_1T_2 applies T_2 first. Both
orders have the same scalar displacement tau_1 tau_2. Consequently

\[
T_1T_2-T_2T_1=M_\Delta\tau_1\tau_2,
\qquad
T_1T_2(T_2T_1)^{-1}=M_R.                              \tag{43.10}
\]

The following are equivalent: Delta is additive-neutral; R=I; the seam
lifts commute; the assigned lifts extend to an action of Z^2 with these
two generators. When (43.5) also holds, the connection respects this
action. This is the algebraic descent test for the two declared periods.
It does not by itself provide a topology or a complete space of analytic
sections. In particular F=0 alone is not that test.

Under (43.7),

\[
\Delta^h=h^{-1}\bullet\Delta\bullet\tau_1\tau_2(h),
\qquad R^h=h^{-1}\bullet R\bullet h.                  \tag{43.11}
\]

Hence failure or success of the descent relation is frame-independent.
The entries of the open-order difference have two endpoint frames;
only the closed return transforms by conjugation at one frame.

**Proof.** Multiply (43.4) in each order to obtain a tau_1 tau_2 and
b tau_1 tau_2. Their common scalar translation cancels in the relative
return, yielding (43.10). Invertibility of b proves Delta=0 iff R=I.
Commuting invertible generators give T_(m,n)=T_1^m T_2^n and every
Z^2 relation; conversely such an action must respect its commuting
generators. Inserting (43.7) in a and b cancels their intermediate
frames and gives a^h=h^(-1)a tau_1 tau_2(h) and the corresponding formula
for b. Subtraction and multiplication by its inverse give (43.11). QED.

## 5. Theorem 4: explicit flat lifts with retained matrix and integer memory

First take two response channels, N=E_12, M=E_21, h=I+y_1 M and
h^(-1)=I-y_1 M in the normal count chart. Let H=I+N and select

\[
A_i=h^{-1}D_i h,\qquad
g=h^{-1}H\tau_{1,L}(h).                               \tag{43.12}
\]

This polynomial seam is invertible, the connection is flat, and (43.5)
holds. It is the moving-frame presentation of A_i=0 and the constant
seam H. In particular local flatness retains the nonidentity return H;
a frame change does not set H to identity. The derivative/endpoint terms
of (43.7) are necessary in this explicit counting example.

Next take three channels with flat lifts nabla_i=D_i, constant seams
G_1=I+E_12 and G_2=I+E_23, and the two scalar count translations.
Every compatibility identity (43.5) holds, yet

\[
\Delta=E_{13},\qquad
R=G_1G_2G_1^{-1}G_2^{-1}=I+E_{13}\ne I.               \tag{43.13}
\]

Thus these are not commuting period lifts on an ordinary torus. A lawful
alternative is to retain a central integer path sector, using the
existing MR-03 extension with the concrete faithful matrices

\[
H(a,b,c)=I+aE_{12}+bE_{23}+cE_{13},\quad a,b,c\in Z,
\]
\[
H(a,b,c)H(a',b',c')
 =H(a+a',b+b',c+c'+ab').                              \tag{43.14}
\]

The inverse has labels (-a,-b,-c+ab). The projection onto (a,b) forgets
c. The relation word in (43.13) projects to (0,0) but retains c=1.
It is not an identity in the lifted group. For integer words, one full
response to e_3 reads (c,b,1), and a response to e_2 reads (a,1,0), so
the three retained labels have an explicit decoder. Reading only the
bottom two response components loses the central word in (43.13).

**Proof.** Equation (43.12) is precisely (43.7) applied to the compatible
flat pair (0,H); SE42's curvature covariance gives flatness. All factors
and their inverses are polynomial because M^2=N^2=0. For (43.13)--(43.14)
use E_12 E_23=E_13, with the reversed product and every product with
E_13 equal to zero within this strictly upper-triangular algebra. Matrix
multiplication gives each formula. The additional term ab' obeys the
MR-03 cocycle identity, since both associations of three factors give
c+c'+c''+ab'+ab''+a'b''. The stated columns prove faithfulness and the
decoder. QED.

This is the familiar integer Heisenberg extension used as a counting/seam
example, not a new group or a claimed unique EMK/TVSP geometry. The
extension changes the declared path carrier to retain its memory. It
does not repair a failed torus relation by calling its nonidentity word
the identity. Non-Abelian seam laws must be checked before making that
quotient.

## 6. Theorem 5: the observer reads the seam defect and its unit depth

For each constant response basis vector e_k, acquire both ordered paths
T_1T_2e_k and T_2T_1e_k. Retain the accepted and complementary parts under
one supplied idempotent P, with Q=I-P, at their common output frame.
The sum of the two channels for each path, followed by subtraction of
the two orders, gives exactly the kth column of Delta. This complete
bank determines the descent verdict without inspecting a hidden seam
matrix. It also determines the whole semilinear order difference on E
when the declared common scalar translation is retained.

These statements commute with labelled memory cuts
M_q:B->B/(Lambda^(q+1)). All depths together separate the full formal
defect in the separated unit completion. When each g_j has unit degree
at most h and the scalar shifts are cut-rational constants, Delta has
degree at most 2h. Depth 2h therefore suffices, and the worst-case bound
is sharp for h>=1:

\[
g_1=I+\Lambda^h E_{12},\quad g_2=I+\Lambda^h E_{23}
\quad\Longrightarrow\quad
\Delta=\Lambda^{2h}E_{13}.                            \tag{43.15}
\]

The local counting connection remains flat at every unit depth in this
example. A lower-depth observer can still miss its global order residue.
The finite degree bound is for Delta, not an unrestricted inverse or
relative-return series. No common finite depth detects all formal data.

**Proof.** Since each tau fixes e_k, the two acquired columns are a e_k
and b e_k. P+Q=I reconstructs each before subtraction, yielding Delta
e_k. The known translation then gives (43.10) on an arbitrary state.
The memory cut preserves sums and bullet products in its quotient;
constant translations preserve each power of Lambda. Thus acquisition,
composition and decoding commute with M_q. Separation of the formal
unit completion makes equality at all depths equivalent to equality
of every coefficient. Products of two degree-h matrices have degree
at most 2h. Equation (43.15), by the multiplication in (43.13), attains
that degree and is invisible at every smaller retained depth. QED.

For P=diag(0,1,1), P Delta=0 in (43.15): the accepted bank alone is blind.
Its complementary row reads the missing Lambda^(2h) coefficient. These
are full labelled polynomial responses, not finitely many point samples.
Their exact executable instances are in the
[saved readings](../../proof_lab/COUNTING_EMK_SEAM_RESULT.json).

## 7. Source orientation audit: deck step versus forward helical step

The public EMK-G3 certificate declares rho(phi,sigma,k)=
(phi+alpha,sigma+beta,k+q) and its deck step

\[
d(u,\phi,\sigma,k)=(u+L,\phi-\alpha,\sigma-\beta,k-q),
                                                        \tag{43.16}
\]

with phase optionally reduced modulo its period. For this deck action
the invariant compensated coordinates are

\[
\widehat\phi=\phi+(\alpha/L)u,\qquad
\widehat\sigma=\sigma+(\beta/L)u.                    \tag{43.17}
\]

Substitution proves invariance for every integer power of d. Conversely,
the minus-compensated coordinates belong to the distinct forward lift
(u+L,phi+alpha,sigma+beta,k+q). The public `certify_T2` tests that forward
lift but labels the test deck invariance. Its claim does not follow for
the `deck` function in the same file.

At the source values L=5, beta=2/5, the change of the minus-compensated
scale under the actual deck step is -2 beta=-4/5, not neutral. The plus
compensator gives no change. This exact negative control distinguishes
the two maps without relying on the phase projection, which can itself
hide signs. This chapter adopts (43.16)--(43.17), preserving the mapping
torus's original deck convention and positive-circuit monodromy. It does
not rewrite the older source or withdraw unrelated EMK-G3 statements.

## 8. Development boundary

The mathematical mechanisms here are standard semilinear descent,
connection covariance, cocycles and retained coefficient memory. The
development is their explicit counting/EMK interface, source comparison,
orientation correction and observer replay. It does not claim novelty
for those general mechanisms or a stronger replacement for every EMK
geometry.

Zero continues to name the typed Cut. Neutral Delta is a response-module
condition; it is not a redefinition of the Cut. Neither the product-fibre
picture nor the matrix seam selects a physical TVSP motion law. A full
double-helical model still needs its exact carrier, generators, seam
relations and faithful presentation. The shared engine, earlier pins
and RH source are unchanged. No eta improvement, RH proof, Yang--Mills
gap, numerical flow convergence or empirical geometry is inferred.
