# Stratified Recognition Status

```text
STATUS: RNKE_VERIFIED_STRATIFIED_RECOGNITION_LINEAR_CORE
```

This layer integrates the verified finite-dimensional Morphic Recognition
faithfulness theorem with the typed obstruction carrier supplied by Singularity
Calculus v5.

## Certified results

### SR-01 — Stratified target-faithfulness

For a typed linear target packet

\[
\Pi_*:V\to\bigoplus_\lambda T_\lambda
\]

and observer \(E:V\to Y\),

\[
\boxed{
\ker E\subseteq\ker\Pi_*
}
\]

is equivalent to existence of a unique decoder on \(\operatorname{ran}E\):

\[
\boxed{\Pi_*=LE.}
\]

The exact blind dimension is

\[
\boxed{
b(E,\Pi_*)
=\operatorname{rank}(\Pi_*|_{\ker E})
=\operatorname{rank}\begin{pmatrix}E\\\Pi_*\end{pmatrix}-\operatorname{rank}E.}
\]

The minimum number of added scalar linear channels is exactly \(b(E,\Pi_*)\).

### SR-02 — Stratum truncation

For a stratified carrier

\[
V=\bigoplus_{k=0}^{n}V^{(k)}
\]

and lower-stratum observer \(P_{\le r}\),

\[
\boxed{
P_{\le r}\text{ is target-faithful}
\iff
\Pi|_{V_{>r}}=0.
}
\]

Thus omitting a higher stratum is lawful exactly when the declared target truly
ignores it. If not, a blind witness is guaranteed and the minimum repair rank is
\(\operatorname{rank}(\Pi|_{V_{>r}})\).

### SR-03 — Differential obstruction false-commit no-go

For a compatibility target \(\partial\), including \(D_\Delta\) or finite-model
\(\mathbb D\),

\[
\boxed{
\ker E\subseteq\ker\partial
}
\]

implies

\[
\boxed{Ev=0\Rightarrow\partial v=0.}
\]

If the kernel inclusion fails, there exists a guaranteed blind false-closure
witness

\[
\boxed{Ev=0,\qquad\partial v\neq0.}
\]

The exact minimum compatibility repair is

\[
\boxed{
\operatorname{rank}(\partial|_{\ker E}).
}
\]

## Verification

Validated theorem/proof head:

```text
7915fc739611370a0ef4befa63dcab0da9dcb23f
```

GitHub Actions run:

```text
31262853402
```

Results:

```text
Stratified Recognition tests     8/8 PASS
exact controls                     9 PASS
Singularity v5 recheck          30/30 PASS
Python 3.11                      PASS
Python 3.12                      PASS
```

## Claim boundary

```text
FINITE-DIMENSIONAL LINEAR FAITHFULNESS           VERIFIED
EXACT BLIND DIMENSION / MINIMUM REPAIR           VERIFIED
STRATUM-TRUNCATION CRITERION                     VERIFIED
D_DELTA / mathbb D FALSE-CLOSURE NO-GO           VERIFIED IN DECLARED LINEAR MODEL
COMPUTATIONAL HARDNESS                           NOT CLAIMED
CRYPTOGRAPHIC SECURITY                           NOT CLAIMED
NONLINEAR TOPOLOGICAL COMPLETENESS               NOT CLAIMED
INFINITE-DIMENSIONAL MINIMUM RANK                 NOT CLAIMED
PHYSICAL SENSOR FAITHFULNESS WITHOUT ADAPTER     NOT CLAIMED
GLOBAL EXACTNESS FROM DIFFERENTIAL CLOSURE        NOT CLAIMED
```
