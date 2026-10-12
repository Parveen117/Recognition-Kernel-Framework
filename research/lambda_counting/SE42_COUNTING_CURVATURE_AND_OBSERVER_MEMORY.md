# SE42: curvature from counting paths and retained observer memory

13 October 2026 (Asia/Kolkata). Author: Monty.

This completes the curvature construction deferred by SE30--SE38. It
starts with their marked counting unit, formula product, lowering actions,
lawful composition and labelled memory cuts. No thermodynamic connection,
Riemannian metric, Hilbert space or physical time is a premise. A connection
here means a specified rule for transporting a response along counting
directions; the rule is part of the target, not determined by the numbers
alone. Curvature is the retained difference between two such ordered paths.

The result is algebraic connection curvature on the declared counting
module. The underlying connection, commutator, gauge and Bianchi identities
are standard mathematics; the derivations below establish them from this
chapter's actual counting operations. No external priority is claimed.

## 1. Counting carrier and the response transport to be compared

Take d independent positive-count slots, the tensor product of the SE30
carrier, over the exact characteristic-zero cut scalars Q_Sigma[Lambda].
Lambda is central and constant. For a multi-index alpha let p_alpha be
the product of the slotwise falling-count bases. The SE30/SE33 formula
product and lowering operators are

\[
p_\alpha\bullet p_\beta=p_{\alpha+\beta},\qquad
D_i p_\alpha=\alpha_i p_{\alpha-e_i},\qquad
X_i p_\alpha=p_{\alpha+e_i}.                       \tag{42.1}
\]

Terms with alpha_i=0 in the lowering action are additive-neutral. This
extends the already derived one-slot laws; it does not impose new Weyl
relations as unexplained axioms. The product is commutative and
associative, D_i is a derivation for bullet, and

\[
[D_i,D_j]=[X_i,X_j]=0,\qquad [D_i,X_j]=\delta_{ij}I.
                                                               \tag{42.2}
\]

Every identity follows by applying the two sides to p_alpha. Write B for
this counting formula algebra and E=B^r for a finite free response module.
The identity I_E, the additive-neutral endomorphism and the primitive
typed Cut are different objects. No dagger or positive pairing is needed.

The faithful coefficient chart U(y^alpha)=p_alpha takes ordinary
polynomial multiplication to bullet and partial_y_i to D_i. It is an
adapter for computation, not a replacement primitive. In the original
x-chart, ordinary multiplication is generally not bullet: x bullet x is
x^2-Lambda x. The ordinary-product difference rule of SE30 is not silently
replaced by a derivation rule.

A response lift along slot i is a Q_Sigma[Lambda]-linear map nabla_i
satisfying the counting Leibniz rule

\[
\nabla_i(f\bullet s)=(D_i f)\bullet s+f\bullet\nabla_i s.
                                                               \tag{42.3}
\]

The coefficients of the transport are its readings on the constant
response basis: A_i e_a=nabla_i e_a. Matrix products below multiply
entries with bullet, in their stated matrix order.

## 2. Theorem 1: curvature is the coefficient of ordered path mismatch

Every lift (42.3) has a unique expression nabla_i=D_i+A_i with
A_i in Mat_r(B), acting by left bullet multiplication. Its curvature is
the B-linear response operator

\[
\boxed{\mathcal F_{ij}:=[\nabla_i,\nabla_j]
       =D_i A_j-D_j A_i+A_i\bullet A_j-A_j\bullet A_i.}
                                                               \tag{42.4}
\]

Thus F_ij=-F_ji. It is not the commutator of arbitrary unrelated
operators: the compared lifts have the commuting counting directions
(42.2) and the same source/target module.

For central formal step labels a,b define the return

\[
\mathcal H_{ij}(a,b)
=e^{a\nabla_i}e^{b\nabla_j}e^{-a\nabla_i}e^{-b\nabla_j}.
                                                               \tag{42.5}
\]

Later applications act on the left; the displayed word fixes orientation.
The exponentials are formal series in the step labels. Each coefficient
is a finite composition on E, with no assertion of numerical convergence.
The return is B-linear and invertible over B[[a,b]], and

\[
\boxed{[ab](\mathcal H_{ij}-I)=\mathcal F_{ij}.}     \tag{42.6}
\]

Equivalently, the difference between the two open orders has coefficient

\[
[ab](e^{a\nabla_i}e^{b\nabla_j}-e^{b\nabla_j}e^{a\nabla_i})
=\mathcal F_{ij}.
\]

These open orders have the same scalar counting displacement. Their
mixed reading is therefore a comparison on a common target.

**Proof.** Expand s=sum_a f_a bullet e_a in (42.3); this gives the
classification and uniqueness. Expand both compositions of D_i+A_i.
The terms differentiating s once cancel, as do D_iD_j s and D_jD_i s,
leaving (42.4). The exponential Leibniz formula, obtained by induction
and binomial expansion, is

\[
e^{a\nabla_i}(f\bullet s)
 =(e^{aD_i}f)\bullet(e^{a\nabla_i}s).
\]

Its scalar shifts e^{aD_i} commute. Around (42.5) they cancel, so the
closed return is B-linear. Its formal inverse reverses the four factors.
Multiplying through mixed step degree ab gives (42.6). The open-order
version follows from the same coefficient multiplication. QED.

In particular, the curvature is an acquired mixed response, not a norm
assigned to a diagram or a scalar logarithm of a preselected function.

## 3. Theorem 2: formal flatness, complete return and the first native example

The following conditions are equivalent for the specified lifts:

1. F_ij is additive-neutral for every pair.
2. Every elementary formal return (42.5) equals I.
3. Every word in these formal flows depends only on the total step in
   each counting direction; a word with all such totals neutral is I.

This is path independence for this formal additive protocol. It does not
erase additional global identifications, topological winding or path
labels of a separately supplied space.

If C=[nabla_i,nabla_j] commutes with both lifts, then the complete return
has the exact stronger form

\[
\boxed{\mathcal H_{ij}(a,b)=e^{abC}.}              \tag{42.7}
\]

**Proof.** Neutral F means the lifts commute. Their formal exponentials
then commute coefficientwise and combine steps of the same generator.
This proves 1=>3=>2. Extracting ab proves 2=>1. In the central case,
formal differentiation of e^{a nabla_i} nabla_j e^{-a nabla_i} gives C,
so this conjugate is nabla_j+aC. Exponentiating in b and using the two
commutations yields (42.7). QED.

### Curvature built from the counting operators themselves

On two count slots and one response channel, select the lawful lifts

\[
\nabla_1=D_1,\qquad \nabla_2=D_2+c(\Lambda)X_1,
\quad c(\Lambda)\in\mathbb Q_\Sigma[\Lambda].
\]

Here X_1 is bullet multiplication by p_(1,0), already derived in SE30.
Equations (42.2), (42.4) and (42.7) give

\[
\boxed{\mathcal F_{12}=c(\Lambda)I,\qquad
       \mathcal H_{12}=e^{ab c(\Lambda)}I.}        \tag{42.8}
\]

For c=1 this is the SE31 central ordered-return factor promoted to a
two-direction response connection. It remains nonneutral at the unit
cut. For c=Lambda^m, m>=1, the degree-zero cut sees flatness while the
first retained nonneutral layer is exactly m. These are different
transport choices. Counting alone does not select one or force flatness
at the cut.

For noncentral F, (42.6) does not justify (42.7). In a two-channel native
path module let N=e_12, M=e_21, A_1=N, A_2=M be constant, so N^2=M^2=0.
Then F_12=diag(1,-1), but the exact return is

\[
\mathcal H_{12}=
\begin{pmatrix}1+ab+a^2b^2&-a^2b\\ab^2&1-ab\end{pmatrix}.
                                                               \tag{42.9}
\]

Its higher mixed readings retain order information beyond F. In
particular tr(F)=0 does not mean F=0. Conversely a noncommuting pair
of coefficients A_i can have neutral total F when its derivative
terms cancel their commutator; pure frame changes below provide examples.

## 4. Theorem 3: moving frames, moving directions and compatibility

Let g be invertible in Mat_r(B), or in its separated unit completion
when all operations are continuous in the unit filtration. A moving
response frame changes the whole lift by nabla_i^g=g^{-1} nabla_i g.
Consequently

\[
\boxed{A_i^g=g^{-1}\bullet(D_i g)+g^{-1}\bullet A_i\bullet g,}
\qquad
\boxed{\mathcal F_{ij}^g=g^{-1}\bullet\mathcal F_{ij}\bullet g.}
                                                               \tag{42.10}
\]

The return similarly obeys H_ij^g=g^{-1} H_ij g. The entries of F are
frame readings; its vanishing, B-linear kernel and image up to the
transported isomorphism are invariant properties. No metric norm is
silently called invariant under arbitrary invertible g.

The direction frame may move too. For derivations V=sum_i v^i D_i and
W=sum_i w^i D_i, set nabla_V=sum_i v^i nabla_i. Then

\[
\boxed{[\nabla_V,\nabla_W]-\nabla_{[V,W]}
       =\sum_{i,j}v^i\bullet w^j\bullet\mathcal F_{ij}.}
                                                               \tag{42.11}
\]

Thus a noncommuting direction frame requires its bracket subtraction.
For V_1=D_1+p_{e_2} D_2 and V_2=D_2, [V_1,V_2]=-V_2; omitting that term
would report false curvature even for the flat lifts D_i.

Finally define the response action on matrices by
mathcal D_i T=D_i T+[A_i,T]_bullet. The compatibility identity is

\[
\boxed{\mathcal D_i\mathcal F_{jk}
      +\mathcal D_j\mathcal F_{ki}
      +\mathcal D_k\mathcal F_{ij}=0.}            \tag{42.12}
\]

**Proof.** Apply g^{-1} nabla_i g to f bullet s and use the derived
Leibniz rule to obtain the first identity. Conjugating the commutator
and each formal exponential gives the next identities. Expand the two
variable-direction products in (42.11): terms differentiating v,w
are exactly nabla_[V,W]; the remaining terms are the displayed sum.
The associative commutator satisfies Jacobi by cancellation of its six
ordered products. Applying it to the three lifts gives (42.12), because
[nabla_i,T] acts by the matrix mathcal D_i T. QED.

These calculations give covariance without a fixed observer position.
They also show precisely why a bare coefficient commutator or a bare
noncoordinate-direction commutator can give the wrong curvature.

## 5. Theorem 4: moving observation cuts and a complete curvature reading

Let P in Mat_r(B) be any idempotent observation cut, P bullet P=P;
Q=I-P. This is a declared algebraic projector, not an assumed orthogonal
projection in a primitive metric. It may vary in the counting slots.
Define K_i=[nabla_i,P]=D_iP+[A_i,P]_bullet. The induced response lift
on the retained module PE is nabla_i^P s=P nabla_i s. Its curvature is

\[
\boxed{\mathcal F^P_{ij}
 =P\mathcal F_{ij}P+P[K_i,K_j]P\quad\hbox{on }PE.} \tag{42.13}
\]

Products are ordered bullet products. In particular a constant P has
the complement-return correction

\[
-PA_i Q A_j P+PA_j Q A_i P.                       \tag{42.14}
\]

For each constant response basis e_a, acquire the two ordered second
responses u_a=nabla_i nabla_j e_a and v_a=nabla_j nabla_i e_a, with
both accepted and complementary outputs. The bank

\[
(P u_a,Q u_a,P v_a,Q v_a)_{a=1}^r                \tag{42.15}
\]

decodes every column of F_ij by

\[
\boxed{\mathcal F_{ij} e_a
       =P u_a+Q u_a-P v_a-Q v_a.}                 \tag{42.16}
\]

These are whole labelled counting-polynomial readings, not r scalar
samples. A separately proved faithful reduced bank may replace them;
no universal minimum number of physical sensors is claimed. Decoder
existence does not supply readings that were never acquired.

**Proof.** The commutator of two compressed lifts expands as
P[nabla_i,nabla_j]P-P nabla_i Q nabla_j P+P nabla_j Q nabla_i P.
Differentiating P^2=P in commutator form gives P K_i P=Q K_i Q=0.
Substitution makes the last two terms P[K_i,K_j]P, proving (42.13).
Constant P gives (42.14). Adding the complementary readings gives u_a
and v_a, whose difference is F_ij e_a by Theorem 1. Their columns
determine the B-linear matrix. QED.

The example (42.9) with P=diag(1,0) has PFP=P and F^P=0: the
complement-return term is -P. Replacing PFP by F^P would erase real
source curvature. Under a moving frame, P^g=g^{-1}Pg and K_i^g=g^{-1}K_i g;
the whole identity transports, including D_iP. No branch is discarded.

This is also why finite count windows must retain SE31's boundary
correction [D_N,X_N]=I-(N+1)E_N. A clipped top count reads -N instead of
the full curvature reading 1. Such windows are not faithful finite
representations of the infinite counting algebra.

## 6. Theorem 5: unit-cut curvature, exact memory depth and hidden layers

Express all objects in the counting basis, with central unit coefficients.
Let M_q retain labelled unit degrees through q and multiply them by
truncated convolution, as in SE31--SE38. It is an algebra quotient,
commutes with D_i, and therefore

\[
\boxed{M_q(\mathcal F(A))=\mathcal F(M_q A),\qquad
 M_q(\mathcal H(A))=\mathcal H(M_q A).}            \tag{42.17}
\]

The latter equality is coefficientwise in the independent step labels.
The same reduction commutes with the frame, moving-cut and decoder
identities whenever the frame inverse is defined in the stated carrier.
In the separated unit completion,

\[
\boxed{\mathcal F=0\quad\Longleftrightarrow\quad
       M_q\mathcal F=0\ \hbox{for every finite }q.} \tag{42.18}
\]

No single finite q replaces all q without additional information.
If the normal counting coefficients of every A_i have unit degree at
most h, then F has unit degree at most 2h. The bank (42.15), retained
through degree 2h, determines F exactly. For h>=1 this worst-case depth
is attained by A_1=Lambda^h N, A_2=Lambda^h M: F=Lambda^(2h)[N,M].

More locally, if A_i and A_j begin in unit orders w_i,w_j, then F_ij
has order at least min(w_i,w_j). If both cross derivatives D_i A_j
and D_j A_i vanish, its order is at least w_i+w_j. Cancellations may
raise either bound. The example (42.8) attains the first type; constant
N,M coefficients attain the second.

**Proof.** Each operation in (42.4) is a sum, product or coefficientwise
count derivative, all of which descend through the existing quotient.
The formal-flow coefficients use finite sums and rational factorials,
so they descend too. Separatedness says a formal unit series with every
coefficient neutral is neutral, proving (42.18). Derivatives preserve
unit degree/order and matrix multiplication adds it, yielding the bounds
and their examples. Theorem 4 reconstructs the retained coefficients.
No division by Lambda or identification of a missing layer with a
neutral full response is involved. QED.

The finite degree statement concerns curvature, not every coefficient
of its complete exponential return, which can have arbitrarily high
unit degree. Likewise a small numerical value of Lambda is not the
same operation as a retained labelled unit cut.

## 7. Result, scope and next attachment

The chapter now has an independently derived counting curvature:
lawful response lifts -> two ordered paths -> mixed return coefficient
-> frame/direction covariance -> moving-cut complement correction
-> observer decoder and retained unit-depth law. The example c=1 is
already nonflat in the counting algebra; c=Lambda^m demonstrates how
a cut can hide its first response layer without annihilating the source.

The construction classifies and compares specified linear response
lifts. Their coefficients may be nonlinear counting polynomials; this
does not make it a theorem for all nonlinear state maps. The canonical
unadorned lift D_i is flat. A response catalogue selects the A_i; no
unique physical connection or value of a physical constant is derived.

Definitions, five theorem groups and exact model readings have distinct
roles. The finite replay is not proof-assistant verification or an
independent external review. No numerical exponential convergence,
physical curvature identity, RH positivity or new eta bound is claimed.
SE29's attached curvature and SE41's calibration theorem remain separate
constructions. The current RH source and all its bounds are unchanged.

See [scope](SE42_SCOPE.md), [source record](SE42_SOURCE_RECORD.md),
[source pins](SE42_SOURCE_PINS.json),
[observer replay](../../proof_lab/counting_curvature.py) and
[saved readings](../../proof_lab/COUNTING_CURVATURE_RESULT.json).
