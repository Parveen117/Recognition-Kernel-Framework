# SR-02 — Stratum-Truncation Blindness and Minimum Repair Theorem

## 1. Typed stratified carrier

Let

\[
V
=
\bigoplus_{k=0}^{n}V^{(k)}
\]

be a finite-dimensional stratified carrier. Degree \(k\) may represent bulk,
seam, pairwise junction, triple compatibility, or any higher declared stratum.

For \(0\le r<n\), define the lower-stratum truncation observer

\[
\boxed{
P_{\le r}:V\to\bigoplus_{k=0}^{r}V^{(k)}
}
\]

and the omitted higher-stratum carrier

\[
\boxed{
V_{>r}
=
\bigoplus_{k=r+1}^{n}V^{(k)}.
}
\]

Then

\[
\boxed{
\ker P_{\le r}=V_{>r}.
}
\]

Let

\[
\Pi:V\to T
\]

be a declared linear target.

## Theorem 1.1 — Exact truncation-faithfulness criterion

The lower-stratum observer \(P_{\le r}\) is target-faithful if and only if the
target ignores every omitted higher-stratum direction:

\[
\boxed{
P_{\le r}\text{ is }\Pi\text{-faithful}
\iff
\Pi|_{V_{>r}}=0.
}
\]

### Proof

By SR-01/MR-02, faithfulness is

\[
\ker P_{\le r}\subseteq\ker\Pi.
\]

Since \(\ker P_{\le r}=V_{>r}\), this is exactly

\[
V_{>r}\subseteq\ker\Pi,
\]

which is equivalent to \(\Pi|_{V_{>r}}=0\). ∎

## Corollary 1.2 — Higher-stratum witness

If there exists

\[
h\in V_{>r}
\]

with

\[
\Pi h\neq0,
\]

then

\[
P_{\le r}h=0
\]

while the target remains nonzero. Hence \(h\) is an explicit observer-blind
higher-stratum witness.

In particular, lower-stratum closure does not imply complete target closure when
the target cares about an omitted stratum.

## 2. Full typed target

Suppose the target itself retains every stratum through the identity packet

\[
\Pi_{\rm full}(v^{(0)},\ldots,v^{(n)})
=
(v^{(0)},\ldots,v^{(n)}).
\]

Then

\[
\boxed{
P_{\le r}\text{ is faithful to }\Pi_{\rm full}
\iff
V_{>r}=\{0\}.
}
\]

Thus a nonzero omitted junction or higher obstruction cannot be declared closed
merely because every recorded lower channel vanishes.

## Theorem 2.1 — Minimum repair after truncation

Let

\[
G:V\to\mathbb F^m
\]

be supplemental scalar channels. The minimum number needed to repair the
truncation observer for target \(\Pi\) is

\[
\boxed{
m_{\min}
=
\operatorname{rank}(\Pi|_{V_{>r}}).
}
\]

### Proof

Apply SR-01 Theorem 3.1 to \(E=P_{\le r}\) and use
\(\ker E=V_{>r}\). ∎

## Corollary 2.2 — Independent typed strata

If

\[
V=\bigoplus_{k=0}^{n}V^{(k)}
\]

and the target is a block-direct sum

\[
\Pi=\bigoplus_{k=0}^{n}\Pi_k,
\qquad
\Pi_k:V^{(k)}\to T_k,
\]

then

\[
\boxed{
m_{\min}
=
\sum_{k=r+1}^{n}\operatorname{rank}\Pi_k.
}
\]

### Proof

On \(V_{>r}\), the target is the direct sum of the independent maps \(\Pi_k\).
The rank of a block-direct-sum map is the sum of the block ranks. ∎

## 3. Singularity Calculus specialization

For the v5 normal-crossing carrier

\[
\mathfrak C_{\rm strat}
=
\bigoplus_{k=0}^{n}\mathfrak C^{(k)},
\]

an observer that retains only codimensions \(0,\ldots,r\) is complete only if
every omitted codimension is irrelevant to the declared Recognition target.

Therefore:

```text
bulk closure does not certify seam closure;
seam closure does not certify junction closure;
junction closure does not certify omitted higher-stratum closure.
```

The statement is conditional on the declared target, not on rhetoric about which
strata "ought" to matter.

## 4. Challenge interpretation

A public red-team track may deliberately expose \(P_{\le r}\) while declaring a
target with

\[
\Pi|_{V_{>r}}\neq0.
\]

Then a blind direction is mathematically guaranteed. After discovery, the exact
minimum repair burden is

\[
\operatorname{rank}(\Pi|_{V_{>r}}).
\]

This is a genuine falsifiable observer challenge rather than an unreachable win
predicate.

## Claim boundary

This theorem does not assert that every real system has nonzero higher-stratum
data. It states exactly when omitting such data is faithful to a declared target.

## Status

```text
LOWER-STRATUM TRUNCATION KERNEL             PROVED
TRUNCATION FAITHFULNESS CRITERION           PROVED
HIGHER-STRATUM BLIND WITNESS                PROVED
MINIMUM REPAIR RANK                         PROVED
BLOCK-DIRECT-SUM REPAIR FORMULA             PROVED
REAL-WORLD STRATUM RELEVANCE                TARGET/DOMAIN SPECIFIC
```