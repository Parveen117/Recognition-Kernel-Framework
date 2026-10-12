# SE36 development: restricted probes, action closure and finite unit-memory observers

12 October 2026. Owner: Monty.

**Development draft; certification remains deferred.** This stage
contains derivations and examples, with no new certificate packet,
executable replay, source-pin manifest or verification PASS.

[SE35](SE35_ACTIVE_READINGS_AND_SINGULAR_CUT_REPAIR.md) allowed a
declared full translation bank. Here the observer has only a supplied
catalogue of perturbations or actions. We derive its actual available
observations, retain the remaining nonlinear fibres, and construct a
finite bank determining every future allowed reading in two classes:
affine actions, and polynomial actions with affine cut at fixed
retained unit depth.

The observer equation is derived on its own response coordinates.
An unavailable probe or inverse action is never silently added.
Lambda remains the central marked unit. Zero-as-cut retains its
operator type; coordinate nulls below are derived additive neutrals.

## 1. Restricted translation has a different blind object

Work in a known finite counting sector V=Q^n, with finite output
sector W and a supplied polynomial F:V->W of degree at most d>=1.
Coordinates are the existing counting-basis coordinates. Let H be
the supplied subspace of allowed perturbation directions, with
basis h_1,...,h_k. The calibration state c is known but arbitrary.

The available translated observation is

\[
 {\cal A}_{H,c}(x;t)
 =F\!\left(x+\sum_{i=1}^k t_i h_i\right)
  -F\!\left(c+\sum_{i=1}^k t_i h_i\right).
 \tag{SE36.1}
\]

Rational perturbation amplitudes are part of this protocol. For
a restricted discrete catalogue, use the action construction
below instead of assuming every amplitude is available.

### Theorem 1: finite restricted signature and its exact fibres

As a polynomial in t, (SE36.1) has degree at most d-1. Consequently
its values on t in {0,...,d-1}^k determine its complete coefficient
signature J_HF(x;c). For k=0 this is the single unperturbed
difference F(x)-F(c).

Two inputs are indistinguishable by every allowed translation
exactly when

\[
 J_HF(x;c)=J_HF(z;c).
 \tag{SE36.2}
\]

These fibres are generally polynomial sets depending on the
observed input. They need not be cosets of a fixed linear subspace.

**Derivation.** The leading degree-d term in the perturbation
cancels between the two responses, as in SE35. Coordinatewise
finite interpolation reconstructs the remaining polynomial.
Equality of its coefficient vector is therefore equivalent to
equality for every allowed perturbation. Its coefficients are
polynomials in the unknown input, giving the stated fibres.

For example, let

\[
 F(u,v)=u^2+v^2,\qquad H=\operatorname{span}\{(1,0)\}.
\]

The available readings are

\[
 F(u+t,v)=u^2+v^2+2ut+t^2.
\]

They determine u and v^2. The residual fibre is

\[
 \{(u,v),(u,-v)\},
 \tag{SE36.3}
\]

with the two points merging when v=0. There is no nonzero fixed
linear subspace whose cosets are these two-point fibres. Thus
SE35's full-translation subspace K_F cannot be reused as the
complete blind object after restricting the probes.

For any specified target, exact set-theoretic recovery is
equivalent to its being constant on these fibres. A polynomial
or linear decoder is a stronger, separate conclusion.

## 2. Available actions act on response functions

Let the available experiment be

\[
 x\longmapsto F(w(x)),
 \tag{SE36.4}
\]

where w is a finite ordered word in supplied maps g_1,...,g_s.
The empty word is allowed. Experiments used to form one bank
start from the same unknown source, or a repeatably prepared copy.
An irreversible single trajectory does not automatically supply
every branching experiment in this catalogue.

First suppose each action is affine:

\[
 g_i(x)=A_i x+b_i.
 \tag{SE36.5}
\]

It need not be invertible. Let E_d be the finite vector space
of scalar polynomials on V of total degree at most d:

\[
 \dim E_d=\binom{n+d}{d}.
 \tag{SE36.6}
\]

An action induces the linear operation on response functions

\[
 K_i f=f\circ g_i.
 \tag{SE36.7}
\]

Linearity here is in the response function f. It does not say
that the nonlinear response F is a linear function of the state.

Take only readings already supplied by F:

\[
 {\cal W}_0=\operatorname{span}_{\mathbb Q}\{1,F_1,\ldots,F_m\},
 \qquad
 {\cal W}_{r+1}={\cal W}_r+\sum_i K_i{\cal W}_r.
 \tag{SE36.8}
\]

A desired target is not inserted as if it were an acquired
reading. Whether it can be recovered is determined afterwards.

### Theorem 2: finite complete observation for the affine catalogue

The spaces (SE36.8) stabilize after at most

\[
 \binom{n+d}{d}-\dim{\cal W}_0
 \tag{SE36.9}
\]

strict increases. One subsequent equality establishes closure.
Their stable value is exactly

\[
 {\cal W}_\infty=
 \operatorname{span}_{\mathbb Q}
 \{1,\ F_j\circ w:\ w\hbox{ an allowed finite word}\}.
 \tag{SE36.10}
\]

It is the smallest response-function subspace containing the
given readings and closed under every supplied action.

Choose a basis psi_0=1,psi_1,...,psi_(ell-1) from this spanning
family. Each nonconstant basis element comes with an actual
output-channel label and a protocol word. Put

\[
 Y(x)=(\psi_0(x),\ldots,\psi_{\ell-1}(x))^T.
\]

Then:

1. Equality of Y(x) and Y(z) is equivalent to equality of every
   future allowed F reading.
2. Each action has an exactly descended response matrix M_i:
   \[
     \boxed{Y(g_i x)=M_iY(x).}
     \tag{SE36.11}
   \]
3. Equality of observations is preserved under every action.
   The observer therefore has an autonomous update on its image.
4. A finite bank of the recorded basis protocols determines all
   future allowed readings, regardless of their word length.

**Derivation.** Affine substitution preserves degree, so K_i
maps E_d into itself. Induction shows W_r is the span of the
constant and all readings whose protocol word length is at
most r. A strict step increases dimension; the bound follows
from (SE36.6). If equality occurs once, the space is invariant
under every K_i and contains all longer words, proving (SE36.10).

Each psi_a composed with g_i is a unique linear combination
of the basis, defining the corresponding row of M_i. This
proves (SE36.11). It also proves that any future reading is
determined by Y. Conversely basis coordinates are themselves
available protocol readings, so equality of all such readings
implies equality of Y.

The ordinary constant coordinate requires no measurement.
A W-valued protocol can provide several scalar channels at once;
ell is a response-space dimension, not automatically the number
of physical executions. The image Y(V) can satisfy nonlinear
relations and is not silently treated as an arbitrary free
state space.

The construction extends the canonical N03/WB4 observer closure
from linear state readouts to a declared finite polynomial
response space. Its termination follows from this constructed
space, not from empirical flattening of a numerical rank curve.

### Three different meanings of recovery

For a scalar target tau:

- A linear decoder of the completed response vector exists
  exactly when tau belongs to W_infinity.
- A polynomial decoder exists exactly when tau belongs to the
  polynomial algebra generated by its basis response functions.
- A set-theoretic decoder exists exactly when tau is constant
  on the fibres of Y.

These are different conditions. For F(u,v)=u^3+v with available
unit shifts in u, the closure contains 1,u,u^2,u^3+v. It does
not contain v as a linear combination, but the polynomial
decoder v=F-u^3 recovers it.

For the passive scalar bank (x^2,x^3), x is uniquely determined:
use x^3/x^2 when x^2 is nonzero, and x=0 otherwise. But no
polynomial in x^2 and x^3 equals x, since every nonconstant
monomial in those generators has degree at least two. Thus
unique recoverability alone does not supply the polynomial
decoder required by SE34's polynomial lifting construction.

## 3. The next useful protocol can be selected from a blind pair

The closure calculation can retain a witness word with every
new independent response. Start with actual F components and,
at each step, compose retained witness functions with each
available action. Retain a candidate exactly when its polynomial
coefficient vector is independent of the current span. The
retained vectors need not be replaced by row-reduced mixtures;
row reduction can be used only to decide independence.

### Corollary: shortest separating word for supplied candidates

Suppose x and z are two candidate inputs. Find the first stage r
for which some retained function satisfies

\[
 \psi(x)\ne\psi(z).
 \tag{SE36.12}
\]

Its witness gives a separating output and a protocol of length
at most r. If every earlier stage agreed, r is the shortest
possible separating word length. If the stable bank agrees,
no word in this catalogue separates that pair.

**Derivation.** W_r spans all readings through word length r.
Evaluation difference f->f(x)-f(z) is a linear functional on it.
It vanishes on the whole span exactly when it vanishes on its
basis. The first nonvanishing stage therefore supplies both
a witness and the word-length conclusion.

This is a selection rule for a supplied unresolved candidate
pair, not a claim to enumerate arbitrary nonlinear fibres or
to minimize a global experimental budget.

Adding an admissible proposed action a opens a new linear response direction
exactly when its action on the current completed span fails to
remain in that span. Even then, separation of the particular
target-relevant fibre must be checked: a larger linear span can
contain functions already polynomially determined by old readings.

## 4. Theorem 3: construct new probe directions by lawful action words

Suppose in addition that a group of supplied linear actions is
reversible in the available catalogue. Their inverses must be
explicitly available; invertibility on paper does not grant an
unavailable operation. Let H_0 be the initial allowed translation
subspace. This subsection allows a supplied parameterized translation
family together with finitely many reversible linear actions.
With T_h(x)=x+h, composition gives

\[
 \boxed{A\,T_h\,A^{-1}=T_{Ah}.}
 \tag{SE36.13}
\]

The whole word implements a translation whose direction may
not belong to H_0, while restoring the original linear frame.

Define

\[
 H_{r+1}=H_r+\sum_i A_iH_r+\sum_i A_i^{-1}H_r.
 \tag{SE36.14}
\]

**Theorem.** The stable space H_* is the span of all transported
directions A_w h, with h in H_0 and A_w an available group word.
It stabilizes after at most n-dim H_0 strict increases. Every
direction in H_* is implemented by a finite composition of
conjugated translations with supplied rational amplitudes.

**Derivation.** Equation (SE36.13) follows by applying its three
maps to x. Induction gives the stated span, and finite dimension
gives termination. Translations add their directions and their
rational amplitudes can be supplied, proving implementability.
Conversely conjugated translations produce exactly the
directions in that invariant span.

If K_F is SE35's full-translation blind subspace, then

\[
 H_*+K_F=V
 \tag{SE36.15}
\]

is sufficient for these constructed translations to reproduce
every full-translation reading: write a direction as h+k,
and F ignores k. SE35's quotient decoder then applies. For
full state recovery, K_F null and H_*=V are sufficient.

This is not a necessary condition for all possible recovery.
For example u^3+v is already recoverable using only u shifts.
Nor does H_* classify all action-word readings: some actions
reveal new information without synthesizing a translation.
The complete classification for the affine catalogue is
Theorem 2's response bank.

### Example: the order of a swap and a probe opens the missing branch

Let F(u,v)=u^2+v^2, let T(u,v)=(u+1,v), and supply the reversible
swap J(u,v)=(v,u), with J^2=I. Initially T alone leaves the v
branch in (SE36.3) unresolved. The swap alone leaves F unchanged.

But order matters:

\[
 \begin{aligned}
 F(JT(u,v))&=F(u,v)+2u+1,\\
 F(TJ(u,v))&=F(u,v)+2v+1.
 \end{aligned}
 \tag{SE36.16}
\]

Thus the readings F(x), F(Tx) and F(TJx) recover

\[
 u=\frac{F(Tx)-F(x)-1}{2},\qquad
 v=\frac{F(TJx)-F(x)-1}{2}.
 \tag{SE36.17}
\]

Equivalently, JTJ is the previously unavailable vertical
translation. The path through the operators creates the useful
probe; declaring an extra independent detector was unnecessary
for this supplied action catalogue.

This is an algebraic two-coordinate counting example. It does
not identify its labels with physical thermodynamic quadrants.

## 5. Theorem 4: nonlinear actions have finite observation closure at fixed unit depth

The affine hypothesis in Theorem 2 can be replaced by an affine
cut plus retained nonlinear unit memory.

Fix q>=0 and the coefficient ring

\[
 R_q=\mathbb Q[\Lambda]/(\Lambda^{q+1}).
\]

Let the supplied actions on R_q^n be

\[
 g_{i,\Lambda}(x)=A_i x+b_i+
                    \sum_{r=1}^{q}\Lambda^r B_{i,r}(x),
 \qquad \deg B_{i,r}\leq b,\quad b\geq1.
 \tag{SE36.18}
\]

Only their cut members need be affine. No assumption that the
nonlinear coefficients are numerically small is used.

Choose d>=0 so the recorded scalar observables lie in

\[
 {\cal E}_{d,q,b}
 =\bigoplus_{r=0}^{q}
   \Lambda^r\mathbb Q[V]_{\leq d+r(b-1)}.
 \tag{SE36.19}
\]

For a supplied finite polynomial response family, a sufficiently
large d always includes its retained coefficients. The dimension
of this space over Q is

\[
 \boxed{
 N_{d,q,b}=\sum_{r=0}^{q}
   \binom{n+d+r(b-1)}{d+r(b-1)}.}
 \tag{SE36.20}
\]

**Theorem.** Polynomial substitution by every g_(i,Lambda)
preserves E_(d,q,b). Multiplication by Lambda also preserves it.
Consequently the smallest Q-linear subspace containing the
supplied observables and the coefficient constants, and closed
under these operations, is finite.

It is exactly the span of the available protocol observations
and their retained unit multiples. A basis provides a finite
bank determining all future catalogue readings modulo
Lambda^(q+1), even though the underlying actions are nonlinear.
Their response updates are exact finite matrices on this
Q-linear response space.

**Derivation of the degree bound.** Consider an input monomial
Lambda^r x^alpha with k=|alpha|<=d+r(b-1). In substituting an
action, choose nonlinear terms in j of its k variable factors.
Those choices add at least j unit powers; affine choices have
input degree at most one and nonlinear choices degree at most b.
The resulting state degree is at most

\[
 k+j(b-1).
\]

If the total resulting unit degree is t, then j<=t-r. Hence

\[
 k+j(b-1)
 \leq d+r(b-1)+(t-r)(b-1)
 =d+t(b-1).
 \tag{SE36.21}
\]

Terms with t>q are discarded by the declared cut. This proves
substitution invariance. Multiplication by Lambda increases
the allowed degree bound or leaves it unchanged, proving its
invariance too.

For the closure algorithm, start with the Q-span of all unit
multiples of the acquired response components and 1. Since
substitution commutes with multiplication by Lambda, each
successive action-closure stage remains closed under Lambda.
A strict step increases dimension inside the space (SE36.19),
so there are at most N_(d,q,b)-dim W_0 strict increases.

Induction identifies the stable span with
Lambda^a F_j composed with available words, together with
coefficient constants. A unit multiple is obtained from the
same recorded reading, not a new experimental capability.
The proof of Theorem 2 then supplies exact descended action
matrices and equivalence of the finite bank with all future
retained readings.

The matrices may be represented with a Q-basis of the
function space. An alternative generating tuple over R_q can
have relations because Lambda is nilpotent. It must not be
called a free R_q basis merely because its displayed entries
look different.

### Explicit nonlinear example through unit degree two

Let

\[
 g_\Lambda(x)=x+\Lambda x^2,\qquad F(x)=x,\qquad q=2.
\]

The observable tuple

\[
 Y(x)=
 \begin{pmatrix}x\\\Lambda x^2\\\Lambda^2x^3\end{pmatrix}
\]

has the exact update

\[
 \boxed{
 Y(g_\Lambda x)=
 \begin{pmatrix}
 1&1&0\\
 0&1&2\\
 0&0&1
 \end{pmatrix}Y(x)
 \quad\bmod\Lambda^3.}
 \tag{SE36.22}
\]

Indeed g=x+Lambda x^2,
Lambda g^2=Lambda x^2+2Lambda^2x^3, and
Lambda^2g^3=Lambda^2x^3 at this cut.

These response coordinates are themselves obtained from
allowed readings:

\[
 \begin{aligned}
 Y_1&=F(x),\\
 Y_2&=F(gx)-F(x),\\
 Y_3&=\tfrac12\{F(g^2x)-2F(gx)+F(x)\}.
 \end{aligned}
 \tag{SE36.23}
\]

Finite matrix multiplication therefore determines every
future iterate. For every nonnegative integer N,

\[
 F(g_\Lambda^N x)=
 x+N\Lambda x^2+N(N-1)\Lambda^2x^3
 \quad\bmod\Lambda^3.
 \tag{SE36.24}
\]

N counts protocol repetitions, not physical time. Exactness is
at the declared unit cut, with no numerical large-N error
bound or assertion after setting Lambda to a nonzero number.

### A later unit reading can separate an earlier sign branch

For the same action but sensor F(x)=x^2, restrict this example
to an unknown constant input a in Q. The cut reading is a^2.
The first transformed reading is

\[
 F(g_\Lambda a)=
 a^2+2\Lambda a^3+\Lambda^2a^4.
 \tag{SE36.25}
\]

The next unit coefficient supplies 2a^3. If a^2 is nonzero,
their ratio gives a; if a^2=0, the constant rational input
is already a=0. Thus a branch invisible to the initial sensor
is separated by an allowed action and a retained memory layer.

This is recovery of the stated constant input, not a claim
that the same two readings recover every coefficient of an
arbitrary unit-series input. The ratio decoder also has a
separate zero branch and is not silently promoted to a
polynomial global decoder.

### What is not implied by fixed-depth closure

For g(x)=x^2 at the cut and F(x)=x, the successive observations
x,x^2,x^4,x^8,... are linearly independent polynomials.
No finite response space contains them all. This action has
a nonlinear cut and lies outside (SE36.18).

Even for affine-cut families, the dimension bound can grow
with q. A finite exact observer at every fixed unit depth
does not establish one finite observer for the full infinite
unit tower. Reduction to a shallower unit cut commutes with
all underlying actions and readings; independently chosen
coordinate bases must be transported accordingly.

## 6. The moving observer satisfies an exact update equation

For any completed response tuple Y in Theorem 2 or Theorem 4,
retain the calibration in the observation:

\[
 {\cal O}(x,c)=Y(x)-Y(c).
\]

Transporting both source and calibration by the same allowed
action gives

\[
 \boxed{
 {\cal O}(g_i x,g_i c)=M_i{\cal O}(x,c).}
 \tag{SE36.26}
\]

If the calibration is deliberately held at c instead, the
correct equation has its known correction:

\[
 {\cal O}(g_i x,c)
 =M_i{\cal O}(x,c)+Y(g_i c)-Y(c).
 \tag{SE36.27}
\]

These follow by subtracting the two instances of the exact
response update. They show explicitly which part comes from
moving the observer and which from holding its calibration.
No preferred fixed c is needed.

Changing an independent response basis by an invertible matrix
S transports the update to S M_i S^(-1). Equality of readings,
the induced fibres and target recoverability remain the same.
The finite observer is a quotient by indistinguishability under
the supplied protocols, not an assertion that every original
state has been recovered.

## 7. Connection to the preceding nonlinear inverse construction

If the completed available cut bank C_0 has a supplied
polynomial left decoder D_0 with D_0 C_0=I, apply that decoder
to its deformed unit-reading bank:

\[
 Z_\Lambda=D_0 C_\Lambda=I+\Lambda E_\Lambda.
 \tag{SE36.28}
\]

SE35's construction and SE34's unit lifting then recover the
source by finite retained-depth corrections, including the
order-doubling update. The advance here is that C_0 must be
assembled from actual catalogue words rather than assumed
full-direction probes.

If the completed bank still has target-relevant blind fibres,
closure precisely records that limitation. It does not
invent the missing decoder. The pair-witness procedure
identifies the next useful available experiment when one
exists; expanding the action catalogue is a separate
mathematical input.

## 8. Construction order, sources and status

| Earlier source read | Actual role |
| --- | --- |
| SE33 multilinear and response calculus | Polynomial descriptions and finite coefficient response |
| SE34 unit-memory completion and lifting | Typed retained quotients and inverse continuation after a regular cut |
| SE35 active readings and singular-cut repair | Full-translation comparison, polynomial left decoding and identity-cut completion |
| Canonical 01_NATIVE_ALGEBRA.md, N03 | Existing invariant response-space closure and minimum linear refinement |
| Canonical AUTOMATIC_REGULAR_MODEL.md, WB4 | Keeping an action catalogue explicit when constructing future-complete observation |
| Canonical native primitive order and chapter navigation | Counting carriers, lawful composition and calibrated targets precede interpretations |

The added derivations establish: the actual restricted signature;
finite catalogue closure on polynomial responses; witness protocols
for separating candidates; synthesis of transported translations;
and a finite polynomial response space for nonlinear actions with
affine cut at each retained unit depth. The observer then has an
exact update with its calibration included.

Polynomial pullbacks, invariant-span closure and conjugation of
translations are established algebraic mechanisms. Their priority
is not claimed. The degree-versus-unit-order bound is derived
above for this specified class. No Hilbert metric, physical
clock or unrestricted perturbation source is a primitive input.

Certification, software implementation, archived reading packets,
new pins and verification runs remain deferred. Existing
certificates and their table are unchanged. No RH, Yang--Mills,
curvature, arbitrary nonlinear finite-closure or noisy-data
recovery claim is made.

A natural next development is to reduce the retained response
space for a specified target and its future protocol reads,
using the polynomial relations on the observation image.
Its dimension bound above is finite and explicit, but is
not claimed to be the smallest possible nonlinear observer.

