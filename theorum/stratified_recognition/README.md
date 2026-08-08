# Stratified Recognition

This folder integrates Morphic Recognition target-faithfulness with the verified
Singularity Calculus v5 normal-crossing obstruction carrier.

Candidate scope:

```text
finite-dimensional linear observer/target models
+
typed stratified obstruction channels
+
D_Delta / mathbb D compatibility targets.
```

## Theorem chain

1. `01_stratified_target_faithfulness_and_decoder.md`
   - combined typed target \(\Pi_*\);
   - faithfulness \(\ker E\subseteq\ker\Pi_*\);
   - decoder criterion \(\Pi_*=LE\);
   - exact blind dimension;
   - theorem-minimal repair rank.

2. `02_stratum_truncation_blindness_and_repair.md`
   - lower-stratum projection \(P_{\le r}\);
   - exact criterion
     \[
     P_{\le r}\text{ faithful}\iff \Pi|_{V_{>r}}=0;
     \]
   - higher-stratum blind witnesses;
   - exact repair rank.

3. `03_differential_obstruction_false_commit_no_go.md`
   - compatibility target \(\partial\), including \(D_\Delta\) and \(\mathbb D\);
   - faithful observer forbids observer-zero / obstruction-nonzero false closure;
   - unfaithful observer guarantees such a blind direction;
   - exact minimum repair rank.

## Core integration statement

The singularity hierarchy supplies typed target-relevant obstruction channels.
Morphic Recognition supplies the exact criterion for whether a representation can
see those channels.

Thus the central question is not merely whether a residual vanishes, but whether
its observation is faithful to what the declared target treats as nonzero:

\[
\boxed{
\ker E\subseteq\ker\Pi_*.
}
\]

For a differential obstruction target,

\[
\boxed{
\ker E\subseteq\ker D_\Delta
}
\]

or, in the totalized theory,

\[
\boxed{
\ker E\subseteq\ker\mathbb D.
}
\]

## Red-team interface

The canonical falsification witness is

\[
\boxed{
Ev=0,
\qquad
\Pi_*v\neq0.
}
\]

For a compatibility target this becomes

\[
\boxed{
Ev=0,
\qquad
\partial v\neq0.
}
\]

If such a witness exists, the observer is target-blind. The exact minimum number
of added scalar linear channels is

\[
\operatorname{rank}(\Pi_*|_{\ker E}).
\]

This is the direct theorem interface to a later `BREAK RECOGNITION` stratified
attack track.

## Claim boundary

This layer does not claim computational hardness, universal physical sensor
faithfulness, nonlinear topological completeness, or infinite-dimensional minimum
rank without further hypotheses.
