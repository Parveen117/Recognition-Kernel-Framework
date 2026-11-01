# SP1: cyclic return with transported Smriti

Author: Monty. 1 November 2026.

Mathematical status: **PROVED UNDER THE STATED HYPOTHESES** by the arguments
below. Direct exact examples, source integrity, formal verification and
external review have separate statuses in [VALIDATION.md](VALIDATION.md).

## 1. Native construction and scope

Start with a supplied full lambda operator carrier: typed native objects,
cut scalars, admitted arrows and their lawful ordered composition. Lambda
names that carrier, not a scalar, elapsed time, derivative order or coupling.
The following is an admitted affine memory extension of that datum; it is
not a derivation of all possible dynamics from an invariant.

Fix a unital commutative rational algebra A in the central cut scalars. At
each protocol node i admit a source module E_i and a Smriti module M_i over A.
For each allowed edge a:i->j specify

\[
F_a:E_i\to E_j,\quad T_a:M_i\to M_j,\quad c_a\in M_j.
\tag{1}
\]

F_a and T_a are A-linear. The source does not receive feedback from memory
in this stage; the edge catalogue, its increments and the repeated protocol
are supplied. Each action on the unit sector u=1 is

\[
\mathcal U_a=
\begin{pmatrix}F_a&0&0\\0&T_a&c_a\\0&0&1\end{pmatrix}
:E_i\oplus M_i\oplus A\longrightarrow E_j\oplus M_j\oplus A.
\tag{2}
\]

Thus `(x,m,1)` becomes `(F_a x,T_a m+c_a,1)` by a native linear operator on
the augmented carrier. The unit sector is declared; an affine translation is
not mislabeled linear on M_i itself. Modules of different types are never
silently added. No Hilbert space, metric or physical clock is primitive.
Any previously admitted cut P_i retains its complement I-P_i on E_i;
no source quotient is taken here. Pairing data, when supplied, travel with
their modules. The argument does not assume that T_a preserves a positive
pairing, nor does a coordinate transpose define a native dagger.

Retain the edge word and source labels in provenance. Equality of an evaluated
source/Smriti state below does not mean equality of literal append-only words.
The model's memory may distinguish fewer histories than their complete words;
it must not be called universally history-complete.

A zero-specialization consists of compatible maps on scalars and all modules:

\[
\sigma_0:A\to A_0,\quad
\pi_E F_a=F_{a,0}\pi_E,\quad
\pi_M T_a=T_{a,0}\pi_M,\quad
\pi_M c_a=c_{a,0}.
\tag{3}
\]

The source/target versions of each pi have their own types. They preserve
addition and the scalar action through sigma_0. Admitted cuts, complements
and any pairing used by an application must satisfy their corresponding
compatibilities. The results below prove recovery for this domain, not the
existence of such an adapter for every lambda carrier.

## 2. SP1.1 — Ordered composition and zero recovery

For a chronological composable word gamma=a_1...a_k, later actions multiply
on the left. Its source return, memory transport and accumulated increment are

\[
F_\gamma=F_{a_k}\cdots F_{a_1},\qquad
H_\gamma=T_{a_k}\cdots T_{a_1},
\]
\[
b_\gamma=\sum_{j=1}^k
T_{a_k}\cdots T_{a_{j+1}}c_{a_j},
\tag{4}
\]

where the empty product has the identity of the appropriate module. For
gamma followed by eta,

\[
(H_\eta,b_\eta)\circ(H_\gamma,b_\gamma)
=(H_\eta H_\gamma,\ b_\eta+H_\eta b_\gamma).
\tag{5}
\]

This composition is associative and intertwines with (3).

**Proof.** Multiplying two blocks (2) gives (5). For three memory actions the
increment in either parenthesization is
`b_3 + H_3 b_2 + H_3 H_2 b_1`, and the linear part is `H_3 H_2 H_1`.
Induction proves (4), including its order. Applying pi to each finite sum
and product, using (3), gives

\[
\pi_0(\mathcal U_\gamma z)
=\mathcal U_{\gamma,0}\pi_0(z).
\tag{6}
\]

No commutation of different edges was used. QED.

This is a transported affine one-cocycle law on protocol words. It does not
replace MR-03's central two-cocycle law or impose equality on two different
words solely because their projected source operators agree. A further
quotient by word relations requires the whole lifted operators to respect
those relations.

## 3. SP1.2 — Exact reset obstruction and finite-period criterion

Choose a closed protocol at i with a supplied source state x_* such that
`F_gamma x_*=x_*`. Write M=M_i, H=H_gamma, b=b_gamma. At cycle boundaries,
the retained memory map is `f(m)=Hm+b`. Define

\[
C_H=M/\operatorname{im}(I-H),\quad q_H:M\to C_H,
\quad \delta=q_H(b).
\tag{7}
\]

The quotient is a *diagnostic for removable translation*. It is not declared
a sufficient replacement for all memory, source or observation targets.

The following are equivalent:

1. delta=0;
2. there is m_* with f(m_*)=m_*;
3. there is m and an integer p>=1 with f^p(m)=m.

For every n>=0,

\[
f^n(m)=H^n m+\sum_{j=0}^{n-1}H^j b,
\qquad
q_H(f^n(m))=q_H(m)+n\delta.
\tag{8}
\]

Consequently delta!=0 prevents every finite-period retained-memory state,
even when the source pose returns after each cycle. If delta=0, a reset
*exists*; an arbitrary initial memory need not reset or converge to one.

**Proof.** The fixed-point equation is `(I-H)m_*=b`, proving 1 iff 2;
2 implies 3. Induction gives the first identity (8). Since `q_H H=q_H`,
the second follows. If a p-periodic memory exists, (8) gives p delta=0.
Multiplication by p is invertible in every A-module because A is a rational
algebra. Thus delta=0. Equivalently, averaging the p points of the affine
orbit gives a fixed point. QED.

The rational-algebra assumption matters. Translation by 1 on the additive
field F_p has nonzero delta and period p. It is outside this theorem.
Even in characteristic zero, `b!=0` alone does not imply drift: `H=-I`
has `f^2=I` and fixed point b/2. Conversely, `H=2I,b=0` has delta=0 but
every nonzero initial memory is nonperiodic. Reset feasibility and the
actual trajectory are different questions.

## 4. SP1.3 — Frame independence and moving calibration

Use the same affine change of memory coordinates at the beginning and end
of the closed protocol: `m'=Gm+c`, with G an A-linear isomorphism. Then

\[
H'=GHG^{-1},\qquad b'=Gb+(I-H')c.
\tag{9}
\]

G induces an isomorphism C_H->C_H' carrying delta to delta'. In particular,
reset feasibility and its obstruction are independent of this frame and
memory-origin choice.

**Proof.** Substitute `m=G^{-1}(m'-c)` into `Gf(m)+c`, giving (9).
The identity `G(I-H)=(I-H')G` identifies the image submodules. The extra
term in b' belongs to the target image submodule, so its quotient class
vanishes. QED.

If the observer changes frame at *each* cycle, `r_n=G_n m_n+c_n`, the law is
instead

\[
r_{n+1}=G_{n+1}HG_n^{-1}(r_n-c_n)+G_{n+1}b+c_{n+1}.
\tag{10}
\]

Retaining calibration permits reconstruction `m_n=G_n^{-1}(r_n-c_n)`.
For `H=I`, choosing `G_n=I,c_n=-nb` makes r_n=m_0 constant even if
delta!=0. It records the drift in calibration rather than removing it.
Different endpoint frames cannot be treated as the single-frame conjugacy
(9). This is an affine companion to SE41's retained-source principle.

## 5. SP1.4 — Event count and observer access

For this section, M is finite-dimensional over a characteristic-zero cut
field K. A finite A-module which is also finite over K may use its complete
K-linear coefficient carrier; the scalar type of a reading must be declared.
Let E:M->K^s be the acquired linear observation, and let `row E` denote its
span in M*. Then:

1. delta!=0 iff there is ell in M* with `ell H=ell` and `ell b!=0`.
2. Such ell gives a dimensionless event count along the fixed protocol:

\[
\tau(m)=\frac{\ell m-\ell m_0}{\ell b},
\qquad \tau(f^n(m_0))=n.
\tag{11}
\]

3. A globally valid linear count of this form can be decoded from the current
   E-reading iff some such ell belongs to row E.

**Proof.** Functionals on C_H identify with the annihilator of im(I-H),
namely the ell satisfying `ell H=ell`. Finite-dimensional dual separation
detects a nonzero class delta, proving 1. Applying ell to f gives the
constant increment ell b, proving 2. A linear functional factors through E
iff it vanishes on ker E, equivalently iff it belongs to row E. This proves
3, allowing a fixed additive reference and nonzero scalar normalization.
QED.

Thus a cycle can carry an event count that the current observer cannot
read. If no suitable ell lies in row E but delta!=0, one extra acquired
scalar reading ell m is sufficient and necessary to enable a linear count
on the whole carrier, provided that reading is physically/operationally
available. This counts a chosen clock target, not all future memory.

If H and b are known and sequential probes are allowed, future readings
satisfy

\[
E f^j(m)-E\sum_{k=0}^{j-1}H^k b=EH^j m.
\tag{12}
\]

The known offsets can be removed. MR-04 then applies to the row closure
`W=span{row(EH^j):j>=0}`: an event count is recoverable from this future
bank exactly when W contains such an ell. For d=dim_K M, rows through
`j=d-rank(E)` suffice by MR-04. This is a reused observability result,
not a new minimization theorem: its proof uses only field operations,
closure under right multiplication by H and at most d-rank(E) strict
dimension increases, so the same argument applies over K. Unknown forcing,
noise and unavailable
probes require additional inference contracts.

The normalization in (11) is a unit per completed protocol. It is not a
duration in seconds, an entropy law or a unique universal time coordinate.

## 6. SP1.5 — Polynomial memory from transported increments

If H=I+N with N^r=0, then exactly for every integer n>=0,

\[
f^n(m_0)=
\sum_{k=0}^{r-1}\binom nk N^k m_0+
\sum_{k=0}^{r-1}\binom n{k+1}N^k b.
\tag{13}
\]

The convention is binomial(n,k)=0 for k>n. The forcing contribution has
degree at most r in the cycle index. Its degree-r coefficient is
`N^(r-1)b/r!`; when that vector is nonzero the degree is exactly r.

**Proof.** The finite binomial theorem expands H^n. Substitute the same
expansion in (8) and use
`sum_(j=0)^(n-1) binomial(j,k)=binomial(n,k+1)`.
The initial-memory term has degree at most r-1, so it cannot cancel a
nonzero degree-r forcing coefficient. QED.

This shows how transporting old increments generates higher-order records
even with the same increment each cycle. Polynomial accumulation alone is
not the reset obstruction: with `b=0,N m_0!=0`, memory can grow along that
initial orbit while delta=0 and a fixed memory still exists.

## 7. SP1.6 — Specialization preserves construction, may hide obstruction

For a compatible loop specialization (3), pi_M induces

\[
\overline\pi_0:C_H\longrightarrow C_{H_0},
\qquad \overline\pi_0(\delta)=\delta_0.
\tag{14}
\]

**Proof.** `pi_M((I-H)m)=(I-H_0)pi_M(m)`, so the quotient map is
well defined. Applying it to b proves the class identity. Equations
(4), (8), (9) for compatible invertible frames, and (13) specialize
term by term. QED.

In particular a full-family reset specializes to a zero-member reset.
The converse need not hold: the quotient map (14) can kill a nonzero class.
A field-valued clock need not descend through pi_M either; descent requires
its reading to be constant on the fibers of pi_M. Neither quotient
injectivity nor safe division by a disappearing coefficient is assumed.

## 8. Full-family example: source returns, memory records cycles

Choose the admitted coefficient algebra `A=K[epsilon]/(epsilon^3)`.
It is a finite-jet realization within the declared operator carrier;
epsilon is a central formal coefficient, not the meaning of lambda-space.
Use E=A^2, M=A^2, and the derived quarter-turn

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad J^2=-I,\quad J^4=I.
\]

Here the matrix is an exact cut-scalar realization of the admitted native
quarter-turn; it does not import physical rotation or a Hilbert metric.
P=diag(1,0) and Q=I-P retain both source channels. A four-edge protocol
has source action J at every edge. Its first three memory actions are the
identity; the fourth has

\[
H=I+\varepsilon N,\quad
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
b=\varepsilon e_2.
\tag{15}
\]

These are supplied attachment choices; no verse fixes their coefficients
or forces this catalogue. The extended operators (2), word and cuts define
the full family before any specialization. A compatible declared source
pairing may be retained, but the memory shear is not assumed unitary in it.

Every completed protocol returns the source: `J^4 x=x`. Starting at m_0=0,
equation (13) gives

\[
\boxed{m_n=\binom n2\varepsilon^2e_1+n\varepsilon e_2.}
\tag{16}
\]

The image of I-H is `epsilon A e_1`, so b is outside that image and
delta!=0. No retained-memory state has a finite period. The first five
coefficient pairs, displayed as `([epsilon^2]m_1,[epsilon]m_2)`, are

| completed cycles n | quadratic record | event count |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 3 | 3 |
| 4 | 6 | 4 |

Let `ell(m)=[epsilon]m_2`. This is a K-linear coefficient reading on the
complete six-dimensional K-carrier, not an A-linear division by epsilon.
It satisfies `ell H=ell` and `ell b=1`, and reads n directly. Epsilon is
not invertible in A. The naive formula `m_2/epsilon` is not a defined
unique A-valued clock.

An observer acquiring only `y=[epsilon^2]m_1` sees y_0=y_1=0, then y_2=1.
The missing clock row appears in one future reading: for arbitrary memory,

\[
y(f(m))-y(m)=[\varepsilon]m_2.
\tag{17}
\]

Thus the two-reading bank recovers a count that one reading cannot recover
on the whole carrier. Along (16), `y_(n+1)-y_n=n`. This uses the calibrated
update (15); it is not a claim to infer an unknown law from two data points.

The zero-specialization epsilon->0 gives H_0=I,b_0=0,m_(n,0)=0, while
leaving J and the source return intact. All construction squares commute,
yet the memory obstruction and count disappear at that reading. The
witness `m=epsilon e_2` has pi_M(m)=0 but ell(m)=1, proving that this clock
cannot descend to zero-member memory alone. Retained coefficients repair
that blindness; specializing first cannot recover them.

## 9. Meaning of the development

The closed item is an exact decision criterion for the stated affine cycle
family, plus its observer-access and zero-specialization consequences.
The contribution to this repository is this combined attachment and the
full-family witness. Fixed-point/coboundary equivalence, cyclic
coinvariants, finite observability and binomial summation have established
mathematical lineage, recorded in [SOURCES.md](SOURCES.md).

The philosophical sources motivated the questions. They are not premises
of the proof and are not asserted to encode these equations. Choosing the
actual source operators, transported increments, feedback law, empirical
readings and physical time adapter remains application-specific work.
