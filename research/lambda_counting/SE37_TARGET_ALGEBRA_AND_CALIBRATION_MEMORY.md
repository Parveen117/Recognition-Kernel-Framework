# SE37: target algebra, nonlinear reduction and calibration memory

12 October 2026. Owner: Monty.

**Certified observer readings.** Four theorem groups below have written
derivations and worked examples. The [observer certificate](SE37_SCOPE.md)
decodes recorded readings for their stated targets and passes 22 exact
checks, including 7 negative controls, against 150 source pins.

[SE36](SE36_RESTRICTED_PROBES_AND_ACTION_CLOSURE.md) constructs a finite
bank determining every future allowed sensor reading. This stage asks
what can be retained when only a specified target and its future readings
are required. It derives the least such polynomial observation algebra,
explains when response entries can be removed, and keeps the calibration
inside the equation after nonlinear reduction.

The resulting construction includes a whole unit-scaled action family
whose relative observer uses the same two coordinates at every retained
unit depth. Increasing depth still increases the coefficients carried
by those coordinates; it is not a claim of finite information at infinite
depth.

Lambda is the central marked unit. Zero-as-cut is the typed operation
already constructed in SE30--SE34. Coordinate additive neutrals below
retain their distinct algebraic type. RH and curvature remain deferred.

## 1. Available bank, target and lawful relations

Use a known finite counting sector with coefficient ring

\[
 R=\mathbb Q\quad\hbox{or}\quad
 R=R_q=\mathbb Q[\Lambda]/(\Lambda^{q+1}).
 \tag{SE37.1}
\]

The retained unit quotient is the existing counting construction, not
a numerical substitution for Lambda. Let x have n counting coordinates.
Suppose the actual available protocol bank has been completed to

\[
 Y(x)=(Y_1(x),\ldots,Y_m(x)),\qquad
 Y(g_i x)=M_iY(x)+a_i,
 \tag{SE37.2}
\]

where the Y_j lie in R[x], the supplied catalogue consists of the g_i,
and M_i,a_i have entries in R. A constant bank coordinate can absorb a_i.
This is the finite affine response law furnished by SE36; the source
actions g_i themselves need not be affine at positive unit depth.

Every retained entry must already be obtainable from the allowed
readings. The original access to a common source or repeatably prepared
copy remains whatever SE36 required; compression does not supply it.

The target is supplied with a polynomial decoder from that bank:

\[
 \tau(x)=P(Y(x)),\qquad P=(P_1,\ldots,P_t)\in R[y]^t.
 \tag{SE37.3}
\]

Adding an unavailable target as an independent sensor would change this
premise. Here the target is computed from acquired information.

Define the algebra of available polynomial readings and its relation
ideal by

\[
 A_Y=R[Y_1,\ldots,Y_m]\subseteq R[x],\qquad
 I_Y=\{H\in R[y]:H(Y(x))=0\text{ in }R[x]\}.
 \tag{SE37.4}
\]

All equalities in this stage are polynomial identities on the declared
carrier, including its retained unit relations. Consequently
A_Y is represented by R[y]/I_Y. No arbitrary tuple in R^m is assumed to
be an attainable reading. In particular, over R_q the ideal must retain
nilpotent information: replacing it by its radical can erase unit memory.

For example, if Y=Lambda x at q=1, then Y^2=0 as a polynomial identity,
while Y itself need not vanish. Replacing the relation y^2=0 by y=0
would discard a lawful nonzero reading.

Substitution h_i(y)=M_i y+a_i preserves I_Y: H(Y)=0 implies
H(Y(g_i x))=0. Thus each action acts on the available reading algebra.
This is an algebra of scalar response functions. It is not a claim that
an invisible subspace of a noncommutative operator algebra is a two-sided
ideal; the distinction in canonical N03--N05 remains in force.

## 2. Theorem 1: exact polynomial reduction on the observation image

Choose proposed retained coordinates Z=C(Y), with C in R[y]^k.
They preserve the target with a polynomial decoder and have polynomial
updates under every supplied action exactly when there are polynomials
D and Phi_i satisfying

\[
 \begin{aligned}
 P(y)-D(C(y))&\in I_Y^t,\\
 C(h_i(y))-\Phi_i(C(y))&\in I_Y^k
 \quad\text{for every }i.
 \end{aligned}
 \tag{SE37.5}
\]

Here membership is componentwise. Under these identities,

\[
 \boxed{\tau(x)=D(Z(x)),\qquad Z(g_i x)=\Phi_i(Z(x)).}
 \tag{SE37.6}
\]

Composing the descended updates recovers the target after every finite
allowed word, with its actual order retained.

**Derivation.** Substitute y=Y(x) into (SE37.5). The relation terms
vanish and give (SE37.6). Repeated substitution gives the assertion for
words. Conversely, (SE37.6) as polynomial identities says exactly that
the differences in (SE37.5) lie in the kernel defining I_Y. No assertion
outside the observation image is necessary.

Equivalently, the subalgebra R[Z] must contain the target components
and be preserved by every action pullback f -> f composed with g_i.
This criterion permits nonlinear updates even when Y had linear ones.

### Removing a redundant entry

If a bank entry has an explicit identity

\[
 Y_j=H(Y_1,\ldots,\widehat{Y_j},\ldots,Y_m),
 \tag{SE37.7}
\]

it may be deleted without changing A_Y. Substitute H into the old
update and decoder formulas to obtain the new ones. The hat denotes
the deleted entry. This gives a concrete reduction, including its
reconstruction map; a relation alone is insufficient.

For instance, the readings u=x^2 and v=x^3 satisfy v^2=u^3. Nevertheless
v is not a polynomial in u and u is not a polynomial in v. A polynomial
in x^2 contains only even powers, and a polynomial in x^3 contains only
powers divisible by three. Neither identity needed for deletion exists.
The pair even recovers x set-theoretically on Q, using v/u when u is
nonzero and a separate branch when u=0; that does not put x in Q[u,v].

The same example separates algebraic dependence, polynomial decoding
and a decoder with division. Compression here uses the stated polynomial
contract, not an unannounced change of decoder class.

### Three linear responses become one nonlinear coordinate

SE36's example at q=2 has

\[
 g(x)=x+\Lambda x^2,\qquad
 Y=(x,\Lambda x^2,\Lambda^2x^3),
 \qquad
 Y(gx)=
 \begin{pmatrix}1&1&0\\0&1&2\\0&0&1\end{pmatrix}Y(x).
 \tag{SE37.8}
\]

Both later entries are polynomial functions of the first. Retaining
z=x therefore preserves the entire bank, with exact nonlinear update

\[
 \boxed{z'=z+\Lambda z^2\pmod{\Lambda^3}.}
 \tag{SE37.9}
\]

The number of displayed response coordinates falls from three to one.
The update becomes nonlinear. A coordinate in R_2 still carries three
rational unit coefficients; this is not three numerical measurements
being replaced by a scalar without memory.

## 3. Theorem 2: the least algebra preserving every future target

For a finite allowed word w, let g_w be its ordered source action,
including the empty word. Define

\[
 \boxed{A_\tau=R[\tau_j\circ g_w:
                   1\leq j\leq t,\ w\text{ allowed}].}
 \tag{SE37.10}
\]

Under (SE37.2)--(SE37.3), this algebra is finitely generated. It is the
unique least action-preserved R-subalgebra of A_Y containing the target.
It is therefore contained in the coordinate algebra of every polynomial
observer obtained from Y that recovers the target and has polynomial
updates for the catalogue.

There is a finite direct construction. Choose D bounding the degree of
the supplied P_j in bank variables, and put

\[
 E_D=\operatorname{span}_R\{Y^\alpha:|\alpha|\leq D\}.
 \tag{SE37.11}
\]

Treat E_D as a Q-vector space. Its dimension is at most

\[
 N_D=\begin{cases}
 \binom{m+D}{D},&R=\mathbb Q,\\
 (q+1)\binom{m+D}{D},&R=R_q.
 \end{cases}
 \tag{SE37.12}
\]

Relations among the entries can lower this bound. Start with the
Q-span L_0 of the coefficient constants and target components and,
over R_q, all their unit multiples. Iterate

\[
 L_{r+1}=L_r+\sum_i\{f\circ g_i:f\in L_r\}.
 \tag{SE37.13}
\]

The chain stabilizes after at most N_D-dim_Q L_0 strict increases.
If L_* is the stable space, then

\[
 \boxed{A_\tau=R[L_*].}
 \tag{SE37.14}
\]

A finite basis of L_* is a generating bank with linear action updates.
Any further polynomial generating tuple for the same algebra is a
possibly smaller observer with polynomial updates.

**Derivation.** The affine bank substitution h_i does not increase
degree in y, so it preserves E_D. The displayed bound counts its
spanning monomials and, for R_q, their retained unit coefficients.
The closure is therefore a finite increasing chain of Q-subspaces.
Equality at one step implies stability under every generator.

Induction in r shows that L_r is spanned by constants and target
observations at words of length at most r, with their retained unit
multiples. Its stable value consequently spans all future target
observations. Generating an R-algebra gives (SE37.14).

Pullback respects sums and products. Hence the algebra generated by
all future targets is action-preserved and contains the present target.
Any other such algebra contains each future target by induction on
word length and therefore contains A_tau. This proves leastness.

For any finite algebra generating tuple Z of A_tau, every Z_j composed
with g_i remains in A_tau and is thus a polynomial in Z. Every target
component is likewise a polynomial in Z. This supplies the descended
updates and decoder required by Theorem 1.

The construction never acquires the target as an extra instrument.
Every target word is a polynomial function of the original completed
bank Y, by (SE37.2)--(SE37.3). Finite-span calculations can retain these
word and decoder expressions as their provenance.

### What the minimum means

Leastness is inclusion of polynomial observation algebras. It is not
a minimum-coordinate-count theorem, a minimum cost of acquiring Y, or
a noise-conditioning result. Greedy deletion using (SE37.7) preserves
information when it succeeds; failure to delete another entry does not
prove a globally minimum generating tuple.

Finite generation here follows from the explicit finite invariant
space E_D. It is not inferred merely because A_tau is a subalgebra of
a finitely generated algebra. The original source functions can have
large degree while still having bounded degree in the bank variables.

Canonical N03 already proves minimum linear refinement by stable row
closure. The present construction applies that finite closure mechanism
to target polynomials in available responses, then distinguishes the
generated algebra from its linear presentation. It does not claim a
new priority for invariant-space closure.

### Two examples: discard an irrelevant coordinate, retain a future one

On the counting sector (u,v), supply the coordinate permutation
g(u,v)=(v,u), a full bank Y=(u,v), and target tau=u+v. Then tau composed
with g equals tau, so A_tau=Q[u+v]. A single coordinate z=u+v with
update z'=z preserves every future target. It deliberately does not
recover u and v separately. No geometric interpretation is required.

Instead supply g(u,v)=(u+v,v) and target tau=u. The next target reading
is u+v. Thus A_tau contains both u and (u+v)-u=v, and equals Q[u,v].
Keeping only u loses future target information: (u,v) and (u,w) agree
now but disagree after the action when v differs from w.

The distinction is decided by the allowed action and target together.
It cannot be settled by looking only at the present target reading.

## 4. Theorem 3: nonlinear compression retains calibration dependence

Let Z be a polynomial observer with descended update Phi_i. For source
x and an arbitrary known calibration c, put

\[
 b=Z(c),\qquad \Delta=Z(x)-Z(c).
 \tag{SE37.15}
\]

Transport both x and c by the same allowed action. Their exact joint
update is

\[
 \boxed{b'=\Phi_i(b),\qquad
 \Delta'=\Phi_i(b+\Delta)-\Phi_i(b).}
 \tag{SE37.16}
\]

If calibration c is held fixed instead, the second equation becomes
Delta'=Phi_i(b+Delta)-b, with b unchanged. No preferred calibration is
introduced by either choice.

For a polynomial map Phi on a free coordinate carrier over R, an
identity

\[
 \Phi(b+\Delta)-\Phi(b)=\Psi(\Delta)
 \quad\text{in }R[b,\Delta]
 \tag{SE37.17}
\]

exists if and only if Phi is affine. Thus an autonomous difference
law independent of the calibration is exactly the affine case on
this carrier.

**Derivation.** Subtract the update at c from the update at x to
obtain (SE37.16). Affine Phi plainly has property (SE37.17). For the
converse, differentiate the polynomial identity in Delta and set
Delta=0. It says that every entry of the polynomial derivative of
Phi at b is constant. Since all positive integers are invertible in
R, every coefficient of degree at least two in Phi must vanish.
This proof also works over the nonreduced ring R_q.

This converse is a formal identity on independent b and Delta. On a
proper observation image, only attainable pairs are tested and its
relations can alter the conclusion. A nonlinear formula can represent
an affine function after those relations are imposed. Theorem 1 is
the correct image-specific criterion.

### The exact part of calibration needed by one update

Expand the increment polynomial as

\[
 \Phi_i(b+\Delta)-\Phi_i(b)
 =\sum_{1\leq|\alpha|\leq e_i}
       R_{i,\alpha}(b)\Delta^\alpha.
 \tag{SE37.18}
\]

The coefficients are the finite response coefficients already used in
SE33; equivalently R_(i,alpha)=(partial^alpha Phi_i)/alpha!. Collect them
over the supplied actions into Gamma(b), omitting constant coefficients.
Two calibrations give the same increment polynomial in free Delta
exactly when they have equal Gamma readings. Coefficient uniqueness
proves both directions.

Therefore Gamma is precisely the one-step calibration information for
that polynomial increment contract. For restricted attainable Delta it
is sufficient and can retain more information than necessary. Nor does
one-step sufficiency imply that Gamma has a closed future update.
Such closure must be derived separately.

In the setting of Sections 1--3, it has a finite construction: each
entry of Gamma(C(Y(c))) is a polynomial in the affine-updating bank
Y(c). Apply Theorem 2 with these calibration coefficients as the target.
It supplies a finitely generated, action-preserved calibration algebra.
If B(c) is a generating tuple, both its next value and all coefficients
in (SE37.18) are polynomials in B(c). The pair (Delta,B(c)) consequently
has a closed polynomial update at this declared depth. An absolute
target decoder may need additional calibration functions; this
construction alone concerns transport of the relative reading.

This establishes finite calibration closure when the original finite
affine response bank exists. Its size may grow with retained unit depth.
The next theorem gives the same explicit calibration coordinate at
every depth for a declared unit-scaled family.

The smaller nonlinear observer can thus move information from repeated
response entries into calibration-dependent coefficients. Suppressing
those coefficients would change the observation law.

## 5. Theorem 4: a uniform relative observer for unit-scaled actions

Consider a finite catalogue of scalar counting actions

\[
 g_i(x)=x+\sum_{r=1}^{s_i}a_{i,r}\Lambda^r x^{r+1},
 \qquad a_{i,r}\in\mathbb Q.
 \tag{SE37.19}
\]

The coefficients and the catalogue are supplied. Work over Q[Lambda],
any retained quotient R_q, or its formal unit completion Q[[Lambda]].
For a moving calibration c define

\[
 \Delta=x-c,\qquad \gamma=\Lambda c.
 \tag{SE37.20}
\]

Both source and calibration undergo g_i. The same two-coordinate
observer (Delta,gamma) has the exact polynomial update

\[
 \boxed{\begin{aligned}
 \gamma'&=\gamma+
            \sum_{r=1}^{s_i}a_{i,r}\gamma^{r+1},\\
 \Delta'&=\Delta+
       \sum_{r=1}^{s_i}a_{i,r}
       \sum_{k=1}^{r+1}\binom{r+1}{k}
           \Lambda^{k-1}\gamma^{r+1-k}\Delta^k.
 \end{aligned}}
 \tag{SE37.21}
\]

No division by Lambda is used. These equations compose in the order
of any finite catalogue word. They commute with every reduction from
one retained unit depth to a shallower depth, and thus define the same
formal update throughout the compatible unit tower.

**Derivation.** Multiplying the calibration update by Lambda gives

\[
 \Lambda g_i(c)=\Lambda c+
   \sum_r a_{i,r}\Lambda^{r+1}c^{r+1}
 =\gamma+\sum_r a_{i,r}\gamma^{r+1}.
\]

For the relative reading expand (c+Delta)^(r+1)-c^(r+1). Its kth
term, after multiplication by Lambda^r, is

\[
 \binom{r+1}{k}\Lambda^r c^{r+1-k}\Delta^k
 =\binom{r+1}{k}\Lambda^{k-1}\gamma^{r+1-k}\Delta^k.
 \tag{SE37.22}
\]

Here k>=1, so every displayed unit power is nonnegative. These
polynomial identities prove (SE37.21) before any unit truncation.
Applying the quotient operations therefore preserves them, and finite
polynomial operations also preserve the compatible formal tower.

The lawful calibration coordinate lies in Lambda R. Its update
preserves that condition. At the unit cut both positive-unit changes
disappear; later unit layers retain the exact calibration effect.

### Quadratic action: explicit memory and necessity

For g(x)=x+Lambda x^2, the result reduces to

\[
 \boxed{\gamma'=\gamma+\gamma^2,\qquad
 \Delta'=(1+2\gamma)\Delta+\Lambda\Delta^2.}
 \tag{SE37.23}
\]

At q>=1, Delta alone cannot in general determine its next reading.
Pairs (x,c)=(1,0) and (2,1) both give Delta=1. Their next readings are
1+Lambda and 1+3Lambda, respectively. The missing information is
calibration, not a failure of the subtraction rule.

For this action, two calibrations have identical increment polynomials
in Delta exactly when Lambda c=Lambda d. The coefficient of Delta is
1+2Lambda c and the coefficient of Delta^2 is the fixed unit Lambda.
Thus gamma is precisely the one-step calibration signature of Theorem 3;
its closed update in (SE37.23) makes it sufficient for every future word.
This is a minimum equivalence of calibration information, not a claim
about the smallest arbitrary encoding of the entire observer state.

For q=2, write c=c_0+Lambda c_1+Lambda^2 c_2. Then gamma retains
Lambda c_0+Lambda^2 c_1; c_2 cannot affect any future relative reading
through this retained depth. The last calibration coefficient can be
discarded without declaring the entire calibration irrelevant.

Subtracting SE36's explicit N-repeat source formulas gives, modulo
Lambda^3 and with gamma in Lambda R_2,

\[
 \begin{aligned}
 \gamma_N&=\gamma+N\gamma^2,\\
 \Delta_N&=\Delta+
 N(2\gamma\Delta+\Lambda\Delta^2)\\
 &\quad+N(N-1)
 (3\gamma^2\Delta+3\Lambda\gamma\Delta^2+\Lambda^2\Delta^3).
 \end{aligned}
 \tag{SE37.24}
\]

N counts protocol repetitions. This is a finite algebraic identity
at the declared depth, not an estimate for numerical long-time error.

### A higher member of the same family

For g(x)=x+a Lambda x^2+b Lambda^2 x^3, the exact update before any
truncation is

\[
 \begin{aligned}
 \gamma'&=\gamma+a\gamma^2+b\gamma^3,\\
 \Delta'&=(1+2a\gamma+3b\gamma^2)\Delta
          +(a\Lambda+3b\Lambda\gamma)\Delta^2
          +b\Lambda^2\Delta^3.
 \end{aligned}
 \tag{SE37.25}
\]

The two retained coordinates are unchanged. The action coefficients
change the polynomial update. Composition can produce more source
powers, but the pair update remains closed without introducing a new
calibration coordinate for each power.

### Scope of the uniform construction

The matching of unit degree r with source degree r+1 in (SE37.19) is
what permits (SE37.22). Arbitrary polynomial actions need not close on
(Delta,Lambda c). For example, for g(x)=x+Lambda x^3 the coefficient
3Lambda c^2 of Delta cannot be a polynomial in Lambda and Lambda c:
each occurrence of c^2 in such a polynomial has at least unit degree
two, whereas this coefficient has unit degree one. Extra calibration
functions are required for that family.

Uniformity concerns the number and formula of formal coordinates.
At depth q, Delta can carry q+1 rational coefficients and gamma can
carry q. At infinite depth these are series with potentially infinitely
many coefficients. No finite numerical data packet is claimed to
contain all of them. Formal unit completion also does not justify
evaluation or convergence at an arbitrary nonzero numerical Lambda.

## 6. How the constructions fit together

The reduction can now be carried out in a declared order:

1. Assemble the available bank and its action law as in SE36.
2. Supply the polynomial decoder for the target already available from
   that bank; close its future response span as in Theorem 2.
3. Retain generators of the resulting target algebra. Remove an entry
   only with its reconstruction identity, and rewrite the update and
   target decoder on the retained tuple.
4. For moving relative readings, derive the calibration coefficients
   rather than dropping them. Retain their future closure, when it is
   available. The unit-scaled family supplies an explicit closed example.

If the original bank is presented relative to a known calibration,
Y(x)-Y(c), reconstruct Y(x) by adding the known Y(c) before applying a
nonlinear decoder. In general C(Y(x))-C(Y(c)) is not C(Y(x)-Y(c)).
This is another instance of the calibration dependence just derived.

The method reduces storage and update description after the declared
readings are available. Fewer physical probes, robustness to noisy
readings, and the cost of solving relation identities are separate
questions. These results do not assume those questions are settled.

## 7. Source lineage and development status

| Source read | Role in this development |
| --- | --- |
| [SE33](SE33_JOINT_READINGS_AND_NONLINEAR_COUNTING.md) | Polynomial response coefficients and finite expansion |
| [SE34](SE34_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY.md) | Retained unit quotients and compatible formal completion |
| [SE35](SE35_ACTIVE_READINGS_AND_SINGULAR_CUT_REPAIR.md) | Polynomial decoding on lawful readings, not arbitrary output tuples |
| [SE36](SE36_RESTRICTED_PROBES_AND_ACTION_CLOSURE.md) | Available action-word banks, affine response closure and the worked unit action |
| [Canonical N03--N05](../../operator_foundation/theory/01_NATIVE_ALGEBRA.md) | Existing minimum linear closure and the distinction between state observation and operator-algebra quotient |

The four derived theorem groups give: exact polynomial descent on the
observation image; the finite least future-target algebra; calibration
dependence after nonlinear compression; and a uniform two-coordinate
relative observer for the declared unit-scaled family. Polynomial
substitution, finite invariant-span closure and coefficient comparison
are established algebraic mechanisms; no priority claim is made.

This is an additive research derivation in the existing counting chapter.
The single shared operator engine remains in operator_foundation/;
no second runtime or competing engine is introduced. The observer
certificate is
[proof_lab/lambda_target_algebra.cjs](../../proof_lab/lambda_target_algebra.cjs)
with its read-only archive
[LAMBDA_TARGET_ALGEBRA_RESULT.json](../../proof_lab/LAMBDA_TARGET_ALGEBRA_RESULT.json),
[scope](SE37_SCOPE.md), [source record](SE37_SOURCE_RECORD.md) and
[pins](SE37_SOURCE_PINS.json). Existing certificates and their table
are unchanged. No RH, eta improvement, Yang--Mills, curvature or
general nonlinear recovery result is claimed here.

A next development can use the response-coefficient construction to
build calibration closure for broader unit-weighted actions, then
separate which memory is needed for the target from which memory is
needed only to transport the observer.
