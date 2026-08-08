# Typed Residue Non-Cancellation and Aggregator Faithfulness Theorem

## 1. Purpose

Recognition closure is often implemented by combining several logically distinct
obligations into one displayed score, one endpoint flag, or one aggregate
residual. That operation is safe only when the aggregation is faithful on the
residual sector that matters.

The primitive object of this note is therefore not a scalar pass/fail score. It
is a typed residual packet

\[
\mathbf r(a)=(r_i(a))_{i\in I},
\]

attached to an admissible morphism \(a:x\to y\).

The theorem below isolates the exact algebraic condition under which global
closure is equivalent to factorwise closure and proves why a lossy aggregation
can hide an open factor by cancellation or projection.

This theorem is domain independent. It contains no AI, blockchain, zeta,
physics, or RH assumption.

---

## 2. Typed residual system

Let \(I\) be a finite index set and, for each \(i\in I\), let \(A_i\) be an
abelian group. Define the typed residual carrier

\[
A:=\bigoplus_{i\in I} A_i.
\]

For an admissible morphism \(a\), let

\[
r_i(a)\in A_i
\]

be the residual of the \(i\)-th mandatory recognition obligation, and define

\[
\boxed{
\mathbf r(a):=\bigoplus_{i\in I}r_i(a)\in A.
}
\]

Examples of factor types may include recognition, authority, provenance,
lineage, target faithfulness, numerical enclosure, ledger coherence, or any
other independently declared obligation. The theorem does not depend on their
interpretation.

### Definition 2.1 (Factorwise closure)

The morphism \(a\) is factorwise closed when

\[
r_i(a)=0
\qquad\text{for every }i\in I.
\]

### Definition 2.2 (Typed global closure)

The morphism \(a\) is typed-globally closed when

\[
\mathbf r(a)=0
\qquad\text{in }A.
\]

---

## 3. Non-cancellation theorem

### Theorem 3.1 (Typed Residue Non-Cancellation)

For every admissible morphism \(a\),

\[
\boxed{
\mathbf r(a)=0
\iff
r_i(a)=0\text{ for every }i\in I.
}
\]

Hence no nonzero residual in one mandatory type can be cancelled by a residual
in another mandatory type when the global residual is represented in the
external direct sum.

### Proof

The zero element of the direct sum is

\[
0_A=\bigoplus_{i\in I}0_{A_i}.
\]

Equality

\[
\bigoplus_i r_i(a)=\bigoplus_i0_{A_i}
\]

holds if and only if each coordinate agrees, so

\[
r_i(a)=0_{A_i}
\]

for every \(i\). The converse is immediate. ∎

### Corollary 3.2 (No local override)

Suppose one factor \(j\) is open:

\[
r_j(a)\ne0.
\]

Then the morphism is not typed-globally closed regardless of the values of the
other factors.

In particular, a local admission factor cannot override a failed global,
lineage, or integrity factor merely because another coordinate closes.

---

## 4. Aggregated shadows

Let \(B\) be an abelian group and let

\[
Q:A\to B
\]

be a homomorphism representing a displayed score, scalar summary, endpoint
projection, compressed certificate, or other aggregate shadow.

Let \(M\le A\) be the declared adverse residual submodule: the set of residual
packets that are considered possible/relevant for the theorem or application.

### Definition 4.1 (Aggregator faithfulness on the adverse sector)

The aggregator \(Q\) is faithful on \(M\) when

\[
\boxed{
\ker(Q|_M)=\{0\}.
}
\]

### Theorem 4.2 (Aggregator Faithfulness Criterion)

The implication

\[
Q\mathbf r=0
\Longrightarrow
\mathbf r=0
\qquad(\mathbf r\in M)
\]

holds if and only if \(Q\) is faithful on \(M\).

Equivalently,

\[
\boxed{
\text{aggregate closure is sound on }M
\iff
\ker(Q|_M)=\{0\}.
}
\]

### Proof

If \(\ker(Q|_M)=\{0\}\) and \(Q\mathbf r=0\) with \(\mathbf r\in M\), then
\(\mathbf r\in\ker(Q|_M)\), hence \(\mathbf r=0\).

Conversely, if \(\ker(Q|_M)\ne\{0\}\), choose nonzero
\(v\in\ker(Q|_M)\). Then

\[
v\ne0,
\qquad
Qv=0.
\]

Thus the aggregate declares closure while a nonzero typed residual survives.
∎

### Corollary 4.3 (Exact hidden-residual witness)

A lossy aggregate \(Q\) has a recognition-blind residual witness exactly when

\[
\ker(Q|_M)\ne\{0\}.
\]

Every nonzero vector in this kernel is an explicit false-closure direction for
an endpoint- or score-only verifier based solely on \(Q\).

---

## 5. Cancellation is a representation defect

A common special case takes all factor residuals in one abelian group \(G\) and
uses the sum

\[
Q(r_1,\ldots,r_n)=\sum_{i=1}^n r_i.
\]

Then

\[
(r,-r,0,\ldots,0)\in\ker Q
\]

for every nonzero \(r\in G\). Therefore

\[
\sum_i r_i=0
\]

does not imply factorwise closure.

The failure is not mysterious cancellation in the native system. It is loss of
type information under the chosen representation.

### Corollary 5.1 (Endpoint/global cancellation warning)

If the verifier collapses independently mandatory residues into a non-faithful
common channel before the commitment decision, then a globally displayed zero
may coexist with an open mandatory factor.

The repair is not to assign signs more carefully. The repair is to retain a
faithful typed carrier or prove faithfulness of the chosen aggregate on the
adverse sector.

---

## 6. Stable version

Assume now that \(A\) and \(B\) are normed vector spaces and \(M\subseteq A\)
is a linear subspace.

### Theorem 6.1 (Quantitative Aggregator Stability)

If there exists \(c>0\) such that

\[
\boxed{
\|Qv\|_B\ge c\|v\|_A
\qquad(v\in M),
}
\]

then \(Q\) is faithful on \(M\), and every observed aggregate residual controls
the full typed residual by

\[
\boxed{
\|v\|_A\le c^{-1}\|Qv\|_B.
}
\]

### Proof

If \(Qv=0\), then

\[
0\ge c\|v\|_A.
\]

Since \(c>0\), \(v=0\). Rearranging the lower bound gives the residual estimate.
∎

This is the stable form of factorwise recognition: exact injectivity prevents
false closure, while a positive lower margin prevents near-blind amplification.

---

## 7. Relation to Recognition-Seam Calculus

The clock-free Recognition-Seam chain law already proves that compositional
residues and cut-corner cross terms are generated structurally. This theorem
adds a separate logical requirement:

```text
generated residues may compose in their native fibers;
mandatory obligation types must not be silently collapsed before closure.
```

Thus the Recognition-Kernel commitment rule should be represented by a typed
residual packet, not by an unproved scalar aggregation.

The result also explains the earlier implementation pattern

```text
local gate      ADMIT
global closure  FAILED
execution       true
```

without referring to any application: one coordinate was allowed to control a
commitment that mathematically belonged to the full direct-sum residual.

---

## 8. Claim boundary

```text
typed direct-sum non-cancellation              PROVED
aggregator faithfulness criterion              PROVED
existence of hidden residual for nonfaithful Q PROVED
quantitative lower-bound stability             PROVED

novelty relative to all category/cohomology
or verification literature                     NOT CLAIMED HERE
application-specific completeness               NOT CLAIMED HERE
```

The mathematical contribution at this stage is a clean framework theorem and a
non-circular closure rule. Novelty claims require a separate literature audit.