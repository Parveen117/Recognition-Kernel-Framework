# SR-01 — Stratified Target-Faithfulness and Decoder Theorem

## 1. Purpose

Morphic Recognition MR-02 proves the exact blindness and minimum-repair theorem
for a finite-dimensional path target. Singularity Calculus v5 supplies a typed
stratified obstruction carrier across bulk, seam, junction, and higher normal-
crossing degrees.

SR-01 combines those structures without changing either theorem.

## 2. Linear stratified carrier

Let \(V\) be a finite-dimensional vector space over \(\mathbb F\), and let

\[
\Pi_\lambda:V\to T_\lambda,
\qquad \lambda\in\Lambda,
\]

be finitely many declared linear target channels. Define the typed target packet

\[
\boxed{
\Pi_*=(\Pi_\lambda)_{\lambda\in\Lambda}:
V\to
T_*:=\bigoplus_{\lambda\in\Lambda}T_\lambda.
}
\]

The labels may represent path memory, bulk curvature, seam residue, junction
obstruction, higher-stratum compatibility, or any other separately typed linear
target.

Let

\[
E:V\to Y
\]

be the observer/representation available to the verifier.

### Definition 2.1 — Stratified target-faithfulness

\[
\boxed{
E\text{ is }\Pi_*\text{-faithful}
\iff
\ker E\subseteq\ker\Pi_*.
}
\]

Because the codomain is a direct sum,

\[
\boxed{
\ker\Pi_*
=
\bigcap_{\lambda\in\Lambda}\ker\Pi_\lambda.
}
\]

Thus combined faithfulness means no observer-invisible direction may alter any
declared target channel.

## Theorem 2.2 — Faithfulness equals decodability

The following are equivalent:

1. \(\ker E\subseteq\ker\Pi_*\);
2. there exists a unique linear decoder
   \[
   L:\operatorname{ran}E\to T_*
   \]
   such that
   \[
   \boxed{\Pi_*=LE;}
   \]
3. the stratified blind quotient
   \[
   \boxed{
   \mathcal B_{\rm strat}(E,\Pi_*)
   =
   \ker E/(\ker E\cap\ker\Pi_*)
   }
   \]
   is zero.

### Proof

If \(\Pi_*=LE\), then \(Ev=0\) implies \(\Pi_*v=L0=0\), hence
\(\ker E\subseteq\ker\Pi_*\).

Conversely assume the kernel inclusion. Define

\[
L(Ev):=\Pi_*v.
\]

If \(Ev=Ew\), then \(v-w\in\ker E\subseteq\ker\Pi_*\), so
\(\Pi_*v=\Pi_*w\). Thus \(L\) is well defined. Linearity is immediate and the
value of \(L\) is forced on \(\operatorname{ran}E\), giving uniqueness.

The blind quotient is zero exactly when

\[
\ker E=\ker E\cap\ker\Pi_*,
\]

which is the same kernel inclusion. ∎

## Corollary 2.3 — Componentwise equivalence

The combined observer is faithful to \(\Pi_*\) if and only if it is faithful to
every component target:

\[
\boxed{
\ker E\subseteq\ker\Pi_*
\iff
\ker E\subseteq\ker\Pi_\lambda
\quad\forall\lambda.
}
\]

Thus one failed typed target is enough to make the combined representation
unfaithful.

## 3. Exact blindness dimension

The map

\[
[v]\mapsto\Pi_*v
\]

identifies

\[
\mathcal B_{\rm strat}(E,\Pi_*)
\cong
\Pi_*(\ker E).
\]

Therefore

\[
\boxed{
b(E,\Pi_*)
:=
\dim\mathcal B_{\rm strat}(E,\Pi_*)
=
\operatorname{rank}(\Pi_*|_{\ker E}).
}
\]

In matrix form,

\[
\boxed{
b(E,\Pi_*)
=
\operatorname{rank}
\begin{pmatrix}E\\\Pi_*\end{pmatrix}
-
\operatorname{rank}E.
}
\]

### Proof of the matrix formula

The common kernel of \(E\) and \(\Pi_*\) is the kernel of the stacked map.
Rank-nullity gives

\[
\begin{aligned}
b(E,\Pi_*)
&=
\dim\ker E-
\dim(\ker E\cap\ker\Pi_*)\\
&=(\dim V-\operatorname{rank}E)
-(\dim V-\operatorname{rank}(E,\Pi_*))\\
&=
\operatorname{rank}(E,\Pi_*)-
\operatorname{rank}E.
\end{aligned}
\]

∎

## Theorem 3.1 — Minimum stratified repair

Let

\[
G:V\to\mathbb F^m
\]

be added scalar observer channels. The minimum \(m\) for which

\[
\ker(E,G)\subseteq\ker\Pi_*
\]

is

\[
\boxed{
m_{\min}=b(E,\Pi_*)
=
\operatorname{rank}(\Pi_*|_{\ker E}).
}
\]

### Proof

This is MR-02 Theorem 6.1 applied to the combined target \(\Pi_*\). The proof is
unchanged: restrict the repair to \(\ker E\), obtain the rank lower bound, then
use coordinates on

\[
\ker E/(\ker E\cap\ker\Pi_*)
\]

to attain it. ∎

## Recognition interpretation

A typed target packet cannot be replaced by a scalar total merely because some
components numerically cancel. The observer is complete only when every
observer-invisible direction is irrelevant to every declared target channel.

```text
observer equality
+ target-faithful decoder
=> target equality.
```

## Claim boundary

This theorem is finite-dimensional and linear. It does not claim:

- that every physical/topological target has a linear encoding;
- infinite-dimensional minimum-rank results without topology/continuity
  hypotheses;
- computational hardness or cryptographic security;
- novelty of the underlying factorization theorem.

## Status

```text
STRATIFIED TARGET PACKET                     DEFINED
FAITHFULNESS = DECODABILITY                  PROVED
BLIND QUOTIENT / STACKED-RANK FORMULA        PROVED
MINIMUM REPAIR RANK                          PROVED VIA MR-02
TYPED COMPONENTWISE FAITHFULNESS             PROVED
FINITE-DIMENSIONAL LINEAR SCOPE              EXPLICIT
```