# SR-03 — Differential-Obstruction Faithfulness and False-Commit No-Go

## 1. Compatibility target

Let \(C\) and \(W\) be finite-dimensional vector spaces and let

\[
\partial:C\to W
\]

be a declared linear compatibility operator.

Two principal framework instances are:

\[
\partial=D_\Delta
\]

from Singularity Calculus SC-16, and

\[
\partial=\mathbb D
\]

from SC-17 on a finite-dimensional totalized model.

Let

\[
E:C\to Y
\]

be the observer/certificate surface exposed to the verifier.

### Definition 1.1 — Compatibility-faithful observer

\[
\boxed{
E\text{ is }\partial\text{-faithful}
\iff
\ker E\subseteq\ker\partial.
}
\]

Equivalently, the declared compatibility target is

\[
\Pi_\partial:=\partial.
\]

## Theorem 1.2 — False-commit no-go under target-faithfulness

If \(E\) is \(\partial\)-faithful, then

\[
\boxed{
Ev=0
\Longrightarrow
\partial v=0.
}
\]

Therefore a verifier that commits compatibility only after establishing both

1. \(Ev=0\), and
2. \(\ker E\subseteq\ker\partial\),

cannot produce a false compatibility commit inside the declared linear model.

### Proof

The implication is exactly the kernel inclusion. If \(Ev=0\), then
\(v\in\ker E\subseteq\ker\partial\), so \(\partial v=0\). ∎

This is a logical no-go statement, not a computational-hardness claim.

## Theorem 1.3 — Blind false-closure witness when faithfulness fails

If

\[
\ker E\not\subseteq\ker\partial,
\]

then there exists

\[
\boxed{v\in C}
\]

such that

\[
\boxed{
Ev=0,
\qquad
\partial v\neq0.
}
\]

Thus an observer-only rule that treats \(Ev=0\) as complete compatibility closure
admits a false-closure witness.

### Proof

Failure of the kernel inclusion means exactly that some
\(v\in\ker E\) lies outside \(\ker\partial\). ∎

## 2. Exact blindness and repair burden

Define

\[
\boxed{
b_\partial(E)
=
\operatorname{rank}(\partial|_{\ker E}).
}
\]

By SR-01/MR-02,

\[
\boxed{
b_\partial(E)
=
\operatorname{rank}
\begin{pmatrix}E\\\partial\end{pmatrix}
-
\operatorname{rank}E.
}
\]

## Theorem 2.1 — Minimum compatibility repair

Among all added scalar linear channels

\[
G:C\to\mathbb F^m,
\]

the minimum number required to make \((E,G)\) compatibility-faithful is

\[
\boxed{
m_{\min}=b_\partial(E).}
\]

### Proof

Apply SR-01 Theorem 3.1 with target \(\Pi_\partial=\partial\). ∎

## 3. Jump-complex specialization

For

\[
\partial=D_\Delta:C^k_\Delta\to C^{k+1}_\Delta,
\]

an observer \(E_k\) of codimension-\(k\) data is realizability-faithful exactly
when

\[
\boxed{
\ker E_k\subseteq\ker D_\Delta.
}
\]

If this fails, there is an observer-invisible packet \(c\) with

\[
D_\Delta c\neq0.
\]

By SC-18, such a packet cannot arise from compatible lower-stratum data. Hence the
observer has hidden a theorem-certified realizability obstruction.

The minimum repair burden is

\[
\boxed{
\operatorname{rank}(D_\Delta|_{\ker E_k}).
}
\]

## 4. Total-complex specialization

For

\[
\partial=\mathbb D,
\]

target-faithfulness requires

\[
\boxed{
\ker E\subseteq\ker\mathbb D.
}
\]

An observer-invisible vector with

\[
\mathbb D v\neq0
\]

is a combined within-stratum/between-stratum false-closure witness.

Again, \(\mathbb Dv=0\) is only a closure gate; SC-18 does not claim that every
closed total cochain is globally exact.

## 5. Typed combined target

Suppose the verifier cares simultaneously about several linear obligations, for
example

\[
\Pi_*
=
(\Pi_{\rm path},\partial,\Pi_{\rm source}).
\]

Then SR-01 gives

\[
\boxed{
\ker E
\subseteq
\ker\Pi_{\rm path}
\cap
\ker\partial
\cap
\ker\Pi_{\rm source}.
}
\]

No cancellation between these target channels can replace componentwise
faithfulness.

## 6. Red-team interpretation

A mathematically meaningful challenge is therefore:

\[
\boxed{
\text{find }v\in\ker E
\text{ such that }
\partial v\neq0.
}
\]

If such a witness exists, the public observer is not compatibility-faithful.
After discovery, the theorem predicts the minimum scalar repair rank exactly.

If no witness is found computationally, that alone does not prove faithfulness;
faithfulness is the kernel theorem, not the absence of a search hit.

## Claim boundary

This theorem proves a finite-dimensional linear implication. It does not prove:

- computational hardness of finding blind directions;
- security against implementation bugs;
- global exactness from \(\partial v=0\);
- faithfulness of a concrete physical sensor without an explicit linear adapter;
- nonlinear topological faithfulness without a separate target model.

## Status

```text
COMPATIBILITY TARGET partial                    DEFINED
FAITHFUL OBSERVER => NO FALSE CLOSURE           PROVED
UNFAITHFUL OBSERVER => BLIND WITNESS EXISTS     PROVED
EXACT BLIND DIMENSION                           PROVED
MINIMUM REPAIR RANK                             PROVED
D_DELTA / mathbb D SPECIALIZATIONS              PROVED
COMPUTATIONAL HARDNESS                          NOT CLAIMED
```