# Stratified Recognition

```text
STATUS: RNKE_VERIFIED_STRATIFIED_RECOGNITION_LINEAR_CORE
```

This folder integrates Morphic Recognition target-faithfulness with the verified
Singularity Calculus v5 normal-crossing obstruction carrier.

The scope is deliberately finite-dimensional and linear:

```text
typed target channels
+
observer/representation kernels
+
exact blindness dimension
+
minimum repair rank
+
D_Delta / mathbb D compatibility targets.
```

## Theorem chain

1. `01_stratified_target_faithfulness_and_decoder.md`
   - combined typed target \(\Pi_*\);
   - faithfulness
     \[
     \ker E\subseteq\ker\Pi_*;
     \]
   - decoder criterion \(\Pi_*=LE\);
   - exact blind dimension
     \[
     b(E,\Pi_*)
     =\operatorname{rank}\begin{pmatrix}E\\\Pi_*\end{pmatrix}
     -\operatorname{rank}E;
     \]
   - theorem-minimal repair rank.

2. `02_stratum_truncation_blindness_and_repair.md`
   - lower-stratum projection \(P_{\le r}\);
   - exact criterion
     \[
     \boxed{
     P_{\le r}\text{ faithful}
     \iff
     \Pi|_{V_{>r}}=0;
     }
     \]
   - guaranteed higher-stratum blind witness when the criterion fails;
   - exact repair rank.

3. `03_differential_obstruction_false_commit_no_go.md`
   - compatibility target \(\partial\), including \(D_\Delta\) and finite-model
     \(\mathbb D\);
   - faithful observer forbids observer-zero / obstruction-nonzero false closure;
   - unfaithful observer guarantees such a blind direction;
   - exact minimum repair rank.

## Core integration theorem

Singularity Calculus supplies typed obstruction channels. Morphic Recognition
supplies the exact criterion for whether an observation can faithfully represent
those channels.

For any declared typed target packet,

\[
\boxed{
\ker E\subseteq\ker\Pi_*.
}
\]

For the normal-crossing compatibility differential,

\[
\boxed{
\ker E\subseteq\ker D_\Delta.
}
\]

For the total stratified differential,

\[
\boxed{
\ker E\subseteq\ker\mathbb D.
}
\]

Failure of the relevant inclusion guarantees an invisible but target-relevant
direction.

## Exact repair law

The blind quotient is

\[
\mathcal B(E,\Pi_*)
=
\ker E/(\ker E\cap\ker\Pi_*),
\]

with dimension

\[
\boxed{
\dim\mathcal B(E,\Pi_*)
=
\operatorname{rank}(\Pi_*|_{\ker E}).
}
\]

That same number is the minimum number of added scalar linear channels required
to repair the observer.

## Red-team interface

The canonical falsification witness is

\[
\boxed{
Ev=0,
\qquad
\Pi_*v\neq0.
}
\]

For a compatibility target:

\[
\boxed{
Ev=0,
\qquad
\partial v\neq0.
}
\]

This gives a clean public challenge architecture:

```text
intentionally incomplete observer
-> guaranteed target-blind direction
-> red team discovers witness
-> theorem computes exact minimum repair
-> attack repaired observer again.
```

No absence-of-search-hit is treated as a proof of faithfulness; faithfulness is a
kernel theorem.

## Verification

Validated theorem/proof head:

```text
7915fc739611370a0ef4befa63dcab0da9dcb23f
```

GitHub Actions run:

```text
31262853402
```

```text
Stratified Recognition tests     8/8 PASS
exact controls                     9 PASS
Singularity v5 recheck          30/30 PASS
Python 3.11                      PASS
Python 3.12                      PASS
```

## Certificate

`RNKE_CERTIFICATE.json` records theorem, dependency, verifier, test, and CI hashes.
`RNKE_STATUS.md` records the reviewer-facing scope and claim boundary.

## Claim boundary

This layer does not claim computational hardness, cryptographic security,
universal physical-sensor faithfulness, nonlinear topological completeness,
infinite-dimensional minimum rank, or global exactness from differential closure.
Those require separate theorems/adapters.
