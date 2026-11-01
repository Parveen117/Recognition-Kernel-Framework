# SE2: put the observer in the endpoint operator equation

Owner: Monty Dabas. Date: 11 October 2026, Asia/Kolkata.
Parent: SE1, RKF commit `b6a3d4e641e81ff16d3e0798d8c168ac2076b739`.
Status: written operator theorems under stated hypotheses; an actual RH
contractive observer has not been constructed.

The owner's direction is to connect local operator descriptions along the
observer's route, match their diagonals with the pairing retained, and avoid
making either endpoint an absolute reference. This note implements that
direction on the existing endpoint problem.

The main change is to eliminate the **finite observed block first**. Debt
and boundary then become one joint target in a recovery equation. Source
positivity and inverse-half regularity follow from that equation and its
contraction bound; they are not assumed before this certificate is tested.

## 1. Reuse the native and Yang–Mills results

Begin with the full typed operator/lambda carrier: cut scalars, derived
iota, admissible composition, dagger, source labels, complementary channels
and ordered memory. A selected path is a sequence of admissible arrows in
this carrier. Its parameter is not automatically physical time or eta.
“Circles” here describe connected local presentations; no new geometric
circle or fixed centre is assumed.

The following results are reused rather than re-proved as new discoveries:

| Input | Role in SE2 |
| --- | --- |
| RKF N03 and N06 | Observer descent and the complementary return omitted by a bare compression |
| RKF N09--N11 | Ordered memory, bounded target recovery and the admitted positive pairing |
| RKF WC5 | Source-preserving Schur elimination and legitimate changes of pivot order |
| EMK-C1 | Connection covariance and target-faithful observation |
| YM YC57 | Observer motion inside the equation; connection and hidden-source terms |
| YM YC58 | Two-endpoint transport of full source records; route alignment and holonomy |
| RKF T36 and SE1 | Prime--Gamma mismatch/debt accounting and the unresolved RH source attachment |

The [YM source record](SE2_YM_SOURCE_RECORD.md) gives exact local Git
revisions and reading scope. These YM packets were read from existing
local Git history; their remote availability is not asserted. This work
changes only Recognition.

The algebraic block and composition identities below apply in the declared
dagger algebra whenever their products and inverses exist. Positivity,
square roots, norm completion and the unbounded-operator statements use
the admitted Hilbert representation. This representation is a downstream
adapter, not the primitive framework.

## 2. One joint source equation

At any reference v let:

- \(H_v\) be the native state carrier in its admitted positive representation;
- \(Y_v\) be the complete mismatch-event carrier;
- \(E_v\) be the finite source-label carrier, of dimension five for the
  declared endpoint instance;
- \(A_v:\operatorname{Dom}A_v\subset H_v\to Y_v\) be closed and densely defined;
- \(D_v\ge0\) be a bounded self-adjoint debt operator;
- \(W_v:E_v\to H_v\) be bounded and \(G_v>0\) on \(E_v\).

The dimension five is the existing application contract. It is not derived
from the appearance of a five-by-five matrix; T31's source-rank and
faithfulness conditions remain separate.

Omit v temporarily. Define the closed semibounded source form
\(S=A^\dagger A-D\), with form domain \(\operatorname{Dom}A\).
Do **not** assume \(S\ge0\). Consider the full Hermitian block form

\[
 \mathfrak C=
 \begin{pmatrix}S&W\\W^\dagger&G\end{pmatrix}
 \quad\text{on }\operatorname{Dom}A\oplus E,
 \qquad
 \mathcal L f=
 \binom{D^{1/2}f}{G^{-1/2}W^\dagger f}.                    \tag{SE2.1}
\]

For the T36 source, \(A\) is the actual prime--Gamma mismatch analysis and
\(D\) is its actual diagonal debt in the same native metric. If the
endpoint uses a Feshbach complement, all of \(A,D,W,G\) must first be
identified on that complement. An unnormalized Fourier identity term is
not silently substituted for the native \(D\).

### Joint observer theorem

The following are equivalent:

1. \(\mathfrak C\ge0\) as a form.
2. \(\|\mathcal L f\|^2\le\|Af\|^2\) for every \(f\in\operatorname{Dom}A\).
3. There is a contraction \(\mathcal O:Y\to H\oplus E\) such that

\[
 \boxed{\mathcal O A=\mathcal L
       =\binom{D^{1/2}}{G^{-1/2}W^\dagger},
       \qquad \mathcal O^\dagger\mathcal O\preceq I_Y.}       \tag{SE2.2}
\]

4. There is a contraction \(C:H\oplus E\to Y\) with
   \(\operatorname{Ran}C\subset\operatorname{Dom}A^\dagger\) and

\[
 A^\dagger C=[D^{1/2},\,WG^{-1/2}].                        \tag{SE2.3}
\]

The map \(\mathcal O\) is the observer in the certificate equation. It
recovers the combined debt/boundary target from the actual mismatch
analysis. It need not recover every state or every operator.

**Proof.** Eliminate the already positive finite block \(G\), retaining
every cross term:

\[
 \begin{split}
 \mathfrak c(f,z)
 &=\|Af\|^2-\langle f,Df\rangle
       +2\operatorname{Re}\langle f,Wz\rangle+\langle z,Gz\rangle\\
 &=\|Af\|^2-\|\mathcal Lf\|^2
       +\|G^{1/2}z+G^{-1/2}W^\dagger f\|^2.                \tag{SE2.4}
 \end{split}
\]

The last square can be set to zero for each \(f\). This proves 1 iff 2
without inverting \(S\).

Under 2 define \(\mathcal O_0(Af)=\mathcal Lf\). If \(Af=0\), the
inequality gives \(\mathcal Lf=0\), so the map is well-defined.
It is contractive on \(\operatorname{Ran}A\), extends to its closure,
and can be set to zero on the orthogonal complement. This proves 3.
Conversely 3 implies 2 immediately.

Taking the adjoint in the weak identity proves 4 with \(C=\mathcal O^\dagger\).
Explicitly, for each u the functional
\(\langle Af,Cu\rangle=\langle\mathcal L f,u\rangle\) is bounded in
\(\|f\|\), because \(\mathcal L\) is bounded. This puts
\(Cu\) in \(\operatorname{Dom}A^\dagger\) and proves (SE2.3).
Taking adjoints again proves the converse. This also justifies the
unbounded-A domain statement. QED.

The associated positive factorization is

\[
 \boxed{\mathfrak c(f,z)
 =\|(I-\mathcal O^\dagger\mathcal O)^{1/2}Af\|^2
   +\|G^{1/2}z+G^{-1/2}W^\dagger f\|^2.}                  \tag{SE2.5}
\]

The first term is the retained operator reserve. A strict scalar source
floor is not required. The factorization/majorization mechanism is
classical Douglas recovery, consumed here through native N10 and with
the actual debt and boundary combined; no new general priority is claimed.

### Endpoint consequences

Equation (SE2.4) implies \(S\ge WG^{-1}W^\dagger\ge0\).
Applying the same bounded-recovery proof to \(S^{1/2}\) and
\(G^{-1/2}W^\dagger\) produces a contraction \(T:E\to H\), on positive
support, with

\[
 S^{1/2}T=WG^{-1/2},\qquad
 T=S^{\dagger/2}WG^{-1/2}.
\]

Thus \(W E\perp\ker S\), the required inverse-half columns exist, and

\[
 \boxed{K_0
 =G-W^\dagger S^\dagger W
 :=G-(S^{\dagger/2}W)^\dagger(S^{\dagger/2}W)
 =G^{1/2}(I-T^\dagger T)G^{1/2}\succeq0.}                 \tag{SE2.6}
\]

The middle notation is a form Gram, not an assertion that \(S^\dagger W\)
exists as an H-valued operator. Conversely these support/domain conditions
and \(K_0\ge0\) imply \(\mathfrak C\ge0\) by completing the square with
\(S^{1/2}f\) and \(S^{\dagger/2}Wz\).

This replaces the separate source-positivity and chart-decoder obligations
by one equivalent joint operator target. It is not a proof that the actual
RH observer in (SE2.2) has been found.

### Recover the five-column certificate after transporting the debt

The joint observer need not have rank five: its debt target can be
infinite-dimensional. It is a full-operator formulation. If the debt
observer is already supplied, the remaining decision returns to five
columns without discarding that target.

Suppose a contraction \(\mathcal O_d:Y\to H\) satisfies
\(\mathcal O_dA=D^{1/2}\). Define
\[
 J_d=I-\mathcal O_d^\dagger\mathcal O_d,\qquad
 \Xi=J_d^{1/2}A.
\]
Then \(\|\Xi f\|^2=\|Af\|^2-\|D^{1/2}f\|^2\), so
\(\Xi^\dagger\Xi=S\) in form sense. The operator \(\Xi\), on
\(\operatorname{Dom}A\), is closed: if \(f_n\) and \(\Xi f_n\) converge,
the displayed norm identity and boundedness of D make \(Af_n\) Cauchy;
closedness of A gives the required limit.

The remaining joint certificate is equivalent to finding a bounded
\(Z:E\to Y\) with columns in \(\operatorname{Dom}\Xi^\dagger\) such that
\[
 \boxed{\Xi^\dagger Z=WG^{-1/2},\qquad Z^\dagger Z\preceq I_E.}
                                                               \tag{SE2.6a}
\]
For sufficiency set \(\mathcal O_b=Z^\dagger J_d^{1/2}\).
Its recovery equation is exact and
\(\mathcal O_b^\dagger\mathcal O_b\preceq J_d\).
For necessity, (SE2.4) gives
\(\|G^{-1/2}W^\dagger f\|\le\|\Xi f\|\); the same range-extension
argument constructs \(Z^\dagger\) with norm at most one.

This is the existing source-flux recovery mechanism, now obtained inside
the transported joint-debt construction. The comparison \(Z^\dagger Z\)
is five-by-five for the endpoint E. The recovery identity still concerns
the actual full source; five sampled diagonals do not verify it.
Neither the needed actual debt observer nor these boundary columns is
newly constructed by this corollary.

## 3. Why operator directions can unblock a scalar ledger

Write \(\mathcal O=(\mathcal O_d,\mathcal O_b)^{\mathsf T}\).
The exact bound is

\[
 \mathcal O_d^\dagger\mathcal O_d+
 \mathcal O_b^\dagger\mathcal O_b\preceq I_Y.               \tag{SE2.7}
\]

The two summands need not act in the same direction. Replacing (SE2.7)
by \(\|\mathcal O_d\|^2+\|\mathcal O_b\|^2\le1\) is sufficient but can
discard the available reserve.

An exact two-direction example takes \(A=I_2,\ E=\mathbb C,\ G=1\),

\[
 D=\operatorname{diag}(9/16,0),\qquad W=(0,3/4)^{\mathsf T}.
\]

Here \(\mathcal O=\mathcal L\), both component norms squared are \(9/16\),
and their scalar sum is \(9/8>1\). Nevertheless
\(\mathcal O^\dagger\mathcal O=(9/16)I_2\). The true reserve is
\((7/16)I_2\), \(S=\operatorname{diag}(7/16,1)\), and \(K_0=7/16\).
The scalar sufficient test fails while the exact operator certificate
succeeds. This is an illustrative supplied model, not RH data.

The reverse error is also possible. Let \(A=\sqrt2\), \(D=3/2\),
\(W=\sqrt3/2\), \(G=1\). The individual squared recovery norms are
\(3/4\) and \(3/8\), each below one, but their joint norm squared is
\(9/8>1\). The completed source is \(S=1/2\), and \(K_0=-1/2\).
Two separate PASS values do not certify their combined target.

Equivalently, \(C^\dagger C\) for \(C=\mathcal O^\dagger=[C_d,C_b]\)
contains both cross blocks \(C_d^\dagger C_b\) and \(C_b^\dagger C_d\).
They are retained in the joint contraction; no phase is erased by treating
the two channels as independent scalar costs.

## 4. Nonzero recovery errors can fit inside the operator reserve

Take a bounded candidate \(\mathcal O\). Let its actual recovery residual
be \(\mathcal E=\mathcal L-\mathcal O A\) on \(\operatorname{Dom}A\).
Suppose a bounded correction \(N:Y\to H\oplus E\) satisfies
\(\mathcal E=NA\). Then the true observer is \(\mathcal O+N\).
The following comparison is sufficient:

\[
 \boxed{
 \mathcal O^\dagger N+N^\dagger\mathcal O+N^\dagger N
 \preceq I-\mathcal O^\dagger\mathcal O.}                  \tag{SE2.8}
\]

Indeed (SE2.8) is exactly
\((\mathcal O+N)^\dagger(\mathcal O+N)\preceq I\); apply the joint
observer theorem. The correction need not be zero. Its signed cross terms
must be kept or enclosed in the correct order.

A relative estimate \(\|\mathcal E f\|\le\epsilon\|Af\|\) constructs
such an \(N\) with \(\|N\|\le\epsilon\), by the proof of Section 2.
This does not require a global lower bound for A. A plain small residual
in \(\|f\|\), without a relative bound or an explicit factor, is not enough
when the mismatch analysis has small singular directions.

This is the operator counterpart of SE1's nonzero residual/reserve
comparison. It is a sufficient route, not a requirement that every possible
proof use this particular observer or correction.

## 5. A moving graph observer and its exact endpoint equation

For trial columns \(X:E\to\operatorname{Dom}S\) define the full invertible
lift and its block form

\[
 T_X=\begin{pmatrix}I&-X\\0&I\end{pmatrix},\qquad
 T_X^\dagger\mathfrak C T_X
 =\begin{pmatrix}S&R_X\\R_X^\dagger&H_X\end{pmatrix},       \tag{SE2.9}
\]
\[
 R_X=W-SX,\qquad
 H_X=G-W^\dagger X-X^\dagger W+X^\dagger SX.
\]

These are the SE1 residual and finite reserve, now inside the full
operator certificate. Multiplying the three blocks proves the identity
in the native order. Since the lift is invertible and preserves the
form domain, it preserves form positivity. It does not discard the
hidden H-channel.

For a change of observer \(X\mapsto X+Y\),

\[
 \boxed{
 R_{X+Y}=R_X-SY,\qquad
 H_{X+Y}=H_X-R_X^\dagger Y-Y^\dagger R_X+Y^\dagger SY.}    \tag{SE2.10}
\]

The same operation transports the off-diagonal residual and both
diagonal forms. Matching only \(H_X\) while dropping \(R_X\) changes
the problem.

For fixed bounded S,W,G and a norm-C1 observer path,

\[
 \dot R_X=-S\dot X,\qquad
 \boxed{\dot H_X=-R_X^\dagger\dot X-\dot X^\dagger R_X.}   \tag{SE2.11}
\]

This puts observer motion in the reserve equation. For unbounded S the
same differentiation requires X to be C1 in its operator graph norm.
For a moving physical S,W,G, their product-derivative terms must also
be retained. Section 7 gives the covariant full-operator version.

Sine spaces remain useful trial modules for X. This construction does
not make an uncontrolled sine tail vanish, and it does not assume that
a full inverse source solve exists at eta zero.

## 6. Connect references without privileging either endpoint

At each vertex v keep the whole \(\mathfrak C_v\) and its typed carrier
\(\mathscr H_v=H_v\oplus E_v\). For an admitted edge \(e:v\to w\), let
\(T_e:\mathscr H_v\to\mathscr H_w\) be bounded and invertible, transporting
the form domains bijectively. Define its **signed operator defect**

\[
 \Delta_e=T_e^\dagger\mathfrak C_wT_e-\mathfrak C_v.       \tag{SE2.12}
\]

In the unbounded case this is a difference of forms on the transported
common domain. Operator-norm bounds below require that the difference
extend to a bounded operator, or must be replaced by explicit form bounds.

For \(e:v\to w,\ f:w\to u\), associativity proves

\[
 \boxed{\Delta_{fe}=\Delta_e+T_e^\dagger\Delta_fT_e.}       \tag{SE2.13}
\]

For a path \(p=(e_1,\ldots,e_n)\), set
\(P_0=I,\ P_j=T_{e_j}\cdots T_{e_1}\). Repeated use gives

\[
 \boxed{P_n^\dagger\mathfrak C_{v_n}P_n
 =\mathfrak C_{v_0}
   +\sum_{j=1}^nP_{j-1}^\dagger\Delta_{e_j}P_{j-1}.}      \tag{SE2.14}
\]

There is no absolute reference vertex. Any adjacent pair or subpath can
be used. Reversal obeys

\[
 \Delta_{e^{-1}}=-T_e^{-\dagger}\Delta_eT_e^{-1}.          \tag{SE2.15}
\]

Positivity of the right side of (SE2.14) is equivalent to positivity at
the final vertex. No individual defect has to vanish or be positive.
Actual signed cancellations may be used after transport. If only
enclosures \(-B_e\preceq\Delta_e\preceq B_e\) are known, carry the
operator sum of \(P^\dagger B_eP\); scalar norm addition is a further
weakening, not the defining certificate.

For example, take all arrows to be I and defects \(F,-F\), where
\(F=(3/4)\operatorname{diag}(1,-1)\), starting from \(\mathfrak C=I_2\).
Both intermediate and final forms are positive and the net defect is
zero. A sum of the two defect norms is \(3/2\), larger than the initial
unit reserve. The exact signed path calculation retains what that scalar
estimate loses.

The endpoints of a requested comparison must still denote identified
typed data. “No preferred endpoint” does not mean changing the physical
target after observing its sign.

### Loops retain memory

For a loop \(\ell:v\to v\),
\(\Delta_\ell=T_\ell^\dagger\mathfrak C_vT_\ell-\mathfrak C_v\).
If every edge is exact, the loop preserves this form, but \(T_\ell\)
need not be I. For instance any nonidentity unitary preserves
\(\mathfrak C_v=I\). Equal endpoint forms therefore do not erase path
holonomy or establish equality of all future source histories.

For that stronger target, use YC58's complete ordered records and N03
descent, transporting sources, ports, pairings and hidden returns.
If an edge is a lossy projection rather than an invertible full lift,
(SE2.14) proves a compression statement only. Complementary memory or
a target-faithful recovery theorem is needed for a full-carrier claim.

### Local joins: construct the observer from connected modules

The edge law retains already supplied operators. There is also a finite
construction of the recovery observer on each joined source module.
Let \(Z_i:F_i\to\operatorname{Dom}A\) be finite-column input syntheses,
with \(F_i\) finite-dimensional. Put \(a_i=AZ_i,\ l_i=\mathcal LZ_i\).
The local diagonal reserve and the cross-pairing defect are
\[
 P_i=a_i^\dagger a_i-l_i^\dagger l_i,\qquad
 C_{12}=a_1^\dagger a_2-l_1^\dagger l_2.
\]

On the joined module use the **entire** matrix
\[
 \boxed{\mathcal P_{12}=
 \begin{pmatrix}P_1&C_{12}\\C_{12}^\dagger&P_2\end{pmatrix}\succeq0.}
                                                               \tag{SE2.J1}
\]
This is equivalent to existence of a contractive observer sending
\(a_1x+a_2y\) to \(l_1x+l_2y\). Indeed (SE2.J1) says exactly that the
squared output norm is at most the squared input norm for every
coefficient pair. It also makes the assignment well-defined on overlap
and on redundant or source-null columns. Extend it by zero on the
orthogonal complement of the joined event range.

When \(P_1,P_2\succeq0\), the exact join condition can be written
\[
 \boxed{C_{12}=P_1^{1/2}V_{12}P_2^{1/2},
          \qquad \|V_{12}\|\le1.}                         \tag{SE2.J2}
\]
No strict reserve floor is required. To prove necessity, apply positivity
of (SE2.J1) to \((x,ty)\), varying the complex scalar t. The discriminant
gives
\[
 |\langle x,C_{12}y\rangle|^2
 \le\langle x,P_1x\rangle\langle y,P_2y\rangle .
\]
It also forces \(C_{12}\ker P_2=0\) and
\(\operatorname{Ran}C_{12}\subset(\ker P_1)^\perp\).
On these finite positive supports,
\(V_{12}=P_1^{\dagger/2}C_{12}P_2^{\dagger/2}\) is a contraction
by the displayed inequality and gives the factorization. Conversely,
(SE2.J2) bounds the mixed term by
\(2\|P_1^{1/2}x\|\|P_2^{1/2}y\|\); completing the scalar square proves
(SE2.J1). This is the standard positive block-matrix criterion in the
native join interface.

At a saturated local direction there is no reserve to pay a cross
defect; the required null-space matching is a consequence of the joint
form, not a rule that every error everywhere must vanish.
Agreement on an intersection alone is weaker. For example the local
maps \(e_1\mapsto3/4\) and \(e_2\mapsto3/4\) are individually contractive
and have a trivial overlap. Their joint row \((3/4,3/4)\) has squared
norm \(9/8>1\). The mixed block exposes the failure.

For multiple modules, merge the whole accumulated Gram with the next
module. Testing isolated pairs alone does not establish positivity of
the full multi-module Gram.

### Cofinal paths and the five-channel limit

For \(Z_n\) synthesizing a nested finite input module, set
\(a_n=AZ_n,\ l_n=\mathcal LZ_n\). If its full joined reserve is
nonnegative, the canonical finite observer is
\[
 \boxed{\mathcal O_n=l_n a_n^+.}                           \tag{SE2.J3}
\]
Here \(a_n^+\) denotes the Moore--Penrose inverse, distinct
from the native dagger used elsewhere. The input and output spaces of
\(a_n\) carry their declared positive metrics. Positivity supplies
\(\ker a_n\subseteq\ker l_n\), so the formula recovers every column.
It is the prescribed map on \(\operatorname{Ran}a_n\), zero on its
orthogonal complement, with norm at most one.

Assume that the union of the input modules is an A-graph core and that
every accumulated join passes. The observers agree on all common event
vectors, since each reads \(\mathcal O_n(Af)=\mathcal Lf\).
Their bounded union extends to the unique contraction \(\mathcal O\)
on \(\overline{\operatorname{Ran}A}\), taken zero off that range.
Graph-core approximation extends recovery to every
\(f\in\operatorname{Dom}A\). This constructs (SE2.2).

Let \(P_n^Y\) project onto \(\operatorname{Ran}a_n\). Then
\(\mathcal O_n=\mathcal O P_n^Y\) and \(\mathcal O_n\to\mathcal O\)
strongly. For the boundary component \(\mathcal O_b:Y\to E\), finite
dimensionality of E improves this to operator-norm convergence:
\[
 \|\mathcal O_b-\mathcal O_bP_n^Y\|
 =\|(I-P_n^Y)\mathcal O_b^\dagger\|\longrightarrow0.
\]
To see it directly, sum the squared residual norms of the finitely many
columns \(\mathcal O_b^\dagger e_j\); each tends to zero by strong
projection convergence. No norm convergence of the infinite-dimensional
debt component is asserted.

Any cofinal ordering of compatible modules gives the same recovered
observer because its value on every \(Af\) is prescribed. Neither the
first module nor an arbitrarily chosen terminal chart is an invariant.
Native sine modules can be used when they meet the stated graph-core
condition; Hilbert-space density alone is insufficient for unbounded A.
This is the observer-space version of the finite-column convergence
mechanism already used in SE1, joined to the full debt/source criterion.

A finite run of successful joins is not the all-joins hypothesis and
gives no automatic tail rate. An actual RH proof needs a theorem for
the remaining joins or a proved operator error allowance such as
(SE2.8). This stage does not certify those actual joins.

## 7. Observer inside the differential equation

In a norm-C1 bounded adapter, let the full transport velocity satisfy
\(\dot T(s)=\mathcal V(s)T(s)\), and put

\[
 \mathcal D_{\mathcal V}\mathfrak C
 =\dot{\mathfrak C}+\mathcal V^\dagger\mathfrak C+\mathfrak C\mathcal V.
\]

Product differentiation gives the two-endpoint law

\[
 \boxed{
 T(b,a)^\dagger\mathfrak C(b)T(b,a)-\mathfrak C(a)
 =\int_a^bT(s,a)^\dagger
       \mathcal D_{\mathcal V}\mathfrak C(s)T(s,a)\,ds.}   \tag{SE2.16}
\]

Neither a nor b is a distinguished invariant point. Moving either one
changes the transported comparison according to the same law.
For an unbounded family a common transported form domain and justified
form differentiation/integration are additional hypotheses; this bounded
identity alone does not construct them.

For the recovery equation itself choose metric-compatible connections on
the state, event and joint-target carriers. For an arrow \(B:V\to U\)
write \(\nabla B=\dot B+\Gamma_U B-B\Gamma_V\). Then

\[
 \boxed{(\nabla\mathcal O)A+\mathcal O(\nabla A)
       =\nabla\mathcal L}                                \tag{SE2.17}
\]

is the derivative of \(\mathcal O A=\mathcal L\). Its exact residual form is
\(\nabla\mathcal E=\nabla\mathcal L-(\nabla\mathcal O)A-\mathcal O\nabla A\).
This connection convention makes a parallel state satisfy
\(\dot x+\Gamma_Hx=0\); thus \(\Gamma_H=-\mathcal V\) when it describes
the preceding state transport. The transport velocity and connection
coefficient must not be assigned the same sign.
The observer reserve evolves as

\[
 \boxed{\nabla(I-\mathcal O^\dagger\mathcal O)
 =-(\nabla\mathcal O)^\dagger\mathcal O
   -\mathcal O^\dagger\nabla\mathcal O.}                  \tag{SE2.18}
\]

Equations (SE2.17)--(SE2.18) specify what a selected observer path must
transport and pay for. They do not prove that an arbitrary desired
observer velocity is compatible with a supplied physical A and L.
Solving the covariant derivative constraint with one matching datum
preserves recovery along its existence interval; contraction must also
be controlled by (SE2.18) or a direct operator bound.

Under simultaneous unitary frame changes U on H, V on E and R on Y,

\[
 A'=RAU^\dagger,\quad D'=UDU^\dagger,\quad
 W'=UWV^\dagger,\quad G'=VGV^\dagger,\quad
 \mathcal O'=(U\oplus V)\mathcal O R^\dagger.              \tag{SE2.19}
\]

The joint equation is unchanged after transport and its reserve is
conjugated by R. Norm-C1 changes include the usual derivative connection,
as in YC57 and EMK-C1. A physical change of observer range with the
physical operator fixed is a different operation and carries its actual
recovery defect. Nonunitary coordinates require the transported pairing;
coordinate transpose must not replace the native dagger.

## 8. What “matching diagonals” means

The native balance diagonal in this construction is the moving set
\[
 \mathscr D_v=\{f:\|A_vf\|^2=\|\mathcal L_vf\|^2\}.
\]
It is determined by the two transported operator readings, not by an
absolute endpoint or a preselected coordinate angle. Equation (SE2.19)
carries this set to \(U\mathscr D_v\). The sign certificate says that no
admitted direction has combined lost/debt reading larger than its mismatch
reading. The balance set alone does not determine which side all the
other directions occupy.

For a Hermitian form, matching its quadratic diagonal
\(q(x)=\langle x,\mathfrak Cx\rangle\) for **all** x matches the full
sesquilinear form by polarization. Matching only the entries
\(\mathfrak C_{ii}\) in one basis does not.

For a five-dimensional Hermitian operator H in a declared orthonormal
source chart, the 25 real readings

\[
 q(e_i),\quad q(e_i+e_j),\quad q(e_i+\iota e_j)
 \quad (i<j)
\]

recover all its entries. With the pairing conjugate-linear in its first
slot,

\[
 \operatorname{Re}H_{ij}
  =\tfrac12[q(e_i+e_j)-q(e_i)-q(e_j)],\qquad
 \operatorname{Im}H_{ij}
  =-\tfrac12[q(e_i+\iota e_j)-q(e_i)-q(e_j)].              \tag{SE2.20}
\]

These are complete finite-form readings, not 25 tests of the infinite
source. In a nonorthonormal chart carry its Gram. The matrices
\(I_2\) and \(\begin{pmatrix}1&2\\2&1\end{pmatrix}\) have identical
basis diagonals but the second has a negative direction. This explains
why transported mixed pairings are part of the certificate.

## 9. Full-family construction and zero reading

The construction is the family of typed data
\((A_v,D_v,W_v,G_v,\mathcal O_v,T_e,\Delta_e)\), with its admitted
relations, domains, pairings and ordered words. A scalar s selects a
path through that family; it does not define the full lambda carrier.

For a supplied typed specialization \(\pi_0\) require preservation of
addition, composition, dagger, pairing and the displayed recovery maps.
Inverses and positive square roots require their compatible functional
calculus; alternatively specialize their supplied factor identities.
On this declared domain,

\[
 \pi_0(\mathcal O A)=\pi_0(\mathcal O)\pi_0(A)=\pi_0(\mathcal L),
 \qquad
 \pi_0(\Delta_{fe})
 =\pi_0(\Delta_e)+
   \pi_0(T_e)^\dagger\pi_0(\Delta_f)\pi_0(T_e).            \tag{SE2.21}
\]

If positivity is preserved by the admitted representation, the joint
certificate specializes as well. The zero-reading is constructed from
the specialized full data. It does not reset hidden memory, remove
holonomy, identify s=0 with eta=0, or assert that every curvature vanishes.
Infinite limits require their own uniform domain and convergence controls.

## 10. Concrete change to the RH work

SE1 improved the conditional Fourier chart allowance. SE2 supplies an
alternative actual-source target:

\[
 \mathcal O\,\mathcal A_{\rm mis}
 =\binom{D^{1/2}}{G^{-1/2}W^\dagger},
 \qquad I-\mathcal O^\dagger\mathcal O\succeq0,
\]

or the nonzero-error version (SE2.8). This target includes the diagonal
debt from the start and does not invert the unknown completed source.
It can therefore be pursued directly on native prime--Gamma events
instead of making the particular T21 scalar chart a mandatory route.

The next construction is an actual event-space recovery map for the
declared five-label endpoint, transported with its sources and pairing.
A sine/Galerkin trial can propose graph columns; an event-space correction
must then establish the full joint operator inequality. The seed
two-direction examples above show why orientation can help, but do not
supply that map for RH.

No new numerical bound, completed RH observer, eta-zero sign certificate,
mass gap, or universal representation theorem is claimed. This is a
written successor using the operator-first YM route. The scalar chart
result in SE1 remains valid within its original conditional scope.

Primary mathematical lineage: R. G. Douglas, *On majorization,
factorization, and range inclusion of operators on Hilbert space*,
Proc. AMS 17 (1966), 413--415
([original paper](https://galaxy.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf)).
Its bounded factorization theorem is the standard mechanism; the
unbounded-A statement used here is proved directly by the domain argument
in Section 2. Native source/observer transport and the application target
come from the pinned framework results, not from that citation alone.

See [source pins](SE2_SOURCE_PINS.json) and the
[written audit and validation scope](SE2_SCOPE.md).
