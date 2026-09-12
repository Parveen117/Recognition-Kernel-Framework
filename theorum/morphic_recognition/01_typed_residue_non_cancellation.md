# MR-01 — Typed Residue Non-Cancellation and Aggregator Faithfulness

## 1. Purpose

Recognition closure may involve several logically distinct obligations. Replacing those obligations by one scalar score or one untyped sum can create false closure by cancellation or projection.

The native global residual is therefore a **typed packet**, not a scalar.

This theorem is algebraic and domain independent.

---

## 2. Typed residual datum

Let `I` be a finite index set. For each `i in I`, let `A_i` be an abelian group and define the external direct sum

\[
A:=\bigoplus_{i\in I}A_i.
\]

For a declared morphism

\[
a:x\to y,
\]

let

\[
r_i(a)\in A_i
\]

be the residual of mandatory obligation `i`. Define

\[
\boxed{
\mathbf r(a):=\bigoplus_{i\in I}r_i(a)\in A.
}
\]

Examples of types may later be recognition, authority, provenance, lineage, target faithfulness, ledger coherence, or numerical enclosure. Their interpretation is irrelevant to the theorem.

### Definition 2.1 — Factorwise closure

`a` is factorwise closed when

\[
r_i(a)=0_{A_i}\qquad\forall i\in I.
\]

### Definition 2.2 — Typed global closure

`a` is typed-globally closed when

\[
\mathbf r(a)=0_A.
\]

---

## 3. Typed Residue Non-Cancellation Theorem

### Theorem 3.1

For every declared morphism `a`,

\[
\boxed{
\mathbf r(a)=0_A
\iff
r_i(a)=0_{A_i}\quad\forall i\in I.
}
\]

Hence a nonzero residual in one mandatory type cannot be cancelled by a residual in another type inside the native direct-sum carrier.

### Proof

By definition,

\[
0_A=\bigoplus_{i\in I}0_{A_i}.
\]

Equality in an external direct sum is coordinatewise. Therefore

\[
\bigoplus_i r_i(a)=\bigoplus_i0_{A_i}
\]

holds if and only if

\[
r_i(a)=0_{A_i}
\]

for every `i`. The converse is immediate. ∎

### Corollary 3.2 — No local override

If one mandatory factor is open,

\[
r_j(a)\neq0,
\]

then `a` is not typed-globally closed regardless of all other residuals.

This is the theorem-level form of the rule:

```text
no local closure may override an open mandatory global factor.
```

---

## 4. Aggregated shadows

Let `B` be an abelian group and

\[
Q:A\to B
\]

be a homomorphism representing a displayed score, compressed certificate, endpoint summary, or other aggregate shadow.

Let

\[
M\le A
\]

be the declared adverse residual submodule.

### Definition 4.1 — Aggregator faithfulness

`Q` is faithful on `M` when

\[
\boxed{
\ker(Q|_M)=\{0\}.
}
\]

### Theorem 4.2 — Aggregator Faithfulness Criterion

For residuals restricted to `M`,

\[
\boxed{
Q\mathbf r=0\Longrightarrow\mathbf r=0
\quad\text{for all }\mathbf r\in M
}
\]

if and only if

\[
\boxed{
\ker(Q|_M)=\{0\}.
}
\]

### Proof

If the restricted kernel is trivial and `Q r = 0`, then `r` belongs to that kernel and must vanish.

Conversely, if the restricted kernel is nontrivial, choose

\[
0\neq v\in\ker(Q|_M).
\]

Then

\[
v\neq0,
\qquad
Qv=0,
\]

so the aggregate reports closure while a nonzero typed residual survives. ∎

### Corollary 4.3 — Exact hidden-residual witness

A lossy aggregate has a false-closure direction exactly when

\[
\ker(Q|_M)\neq\{0\}.
\]

Every nonzero vector in this kernel is an explicit adversarial witness.

---

## 5. Cancellation example

Take

\[
A_1=A_2=\mathbb Z,
\qquad
A=\mathbb Z\oplus\mathbb Z,
\]

and define

\[
Q(u,v)=u+v.
\]

Then

\[
(1,-1)\neq(0,0),
\]

but

\[
Q(1,-1)=0.
\]

Thus scalar summation can erase an open typed residual. The defect is not in the residuals; it is the non-faithful representation `Q`.

---

## 6. Positive norm shadow

If each `A_i` is instead a normed vector space and all weights `w_i` are strictly positive, define

\[
\rho(\mathbf r)^2
:=
\sum_{i\in I}w_i\|r_i\|^2.
\]

Then

\[
\boxed{
\rho(\mathbf r)=0
\iff
r_i=0\quad\forall i.
}
\]

This scalarization is closure-faithful because positivity forbids cross-factor cancellation. It remains a representation of the typed packet, not the primitive residual itself.

---

## 7. Relation to Recognition-Seam composition

Theorem 24 already shows that cut-corner composition creates typed cross terms such as

\[
\mathsf J_\delta\mathsf C_\gamma
\quad\text{and}\quad
\mathsf C_\delta\mathsf J_\gamma.
\]

MR-01 adds the global admission rule: mandatory residue species must retain their type until a faithful compression theorem has been proved.

Endpoint equality, a scalar score, or an untyped sum is not sufficient by itself.

---

## 8. RNKE proof contract

The RNKE-style proof contract for MR-01 contains these obligations:

```text
MR01-O1  direct-sum zero is coordinatewise zero
MR01-O2  one open factor forbids typed global closure
MR01-O3  aggregate closure is sound iff the restricted kernel is trivial
MR01-N1  non-faithful sum aggregator admits the exact witness (1,-1)
MR01-N2  faithful identity aggregator rejects every tested nonzero residual
```

The universal theorem is proved algebraically above. Executable checks are calibration/negative-control evidence and must not be relabeled as the proof itself.

## 9. Status

```text
GENERAL ALGEBRAIC PROOF                    PROVED
DEPENDENCE ON DOMAIN SEMANTICS             NONE
DEPENDENCE ON CLOCK                        NONE
RNKE PROOF-CONTRACT CALIBRATION             SEE proof_lab/morphic_recognition
FORMAL PROOF-ASSISTANT CERTIFICATE          NOT CLAIMED
```
