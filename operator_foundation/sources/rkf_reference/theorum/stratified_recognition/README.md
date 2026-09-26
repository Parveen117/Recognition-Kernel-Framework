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

4. `04_physical_observer_minimum_sensor_repair.md`
   - device-facing specialization of the observer theorem;
   - installed sensor map \(S\) is target-faithful iff
     \[
     \ker S\subseteq\ker\Pi;
     \]
   - physical blind dimension
     \[
     b_{\rm phys}=\operatorname{rank}(\Pi|_{\ker S});
     \]
   - exact minimum independent sensor repair
     \[
     \boxed{m_{\min}=b_{\rm phys}};
     \]
   - differential-obstruction and higher-stratum truncation corollaries.

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

## Red-team and device interface

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

For a physical sensor map \(S\):

\[
\boxed{
Sv=0,
\qquad
\Pi v\neq0.
}
\]

This gives a clean challenge and bench architecture:

```text
intentionally incomplete observer/sensor
-> guaranteed target-blind direction
-> witness discovered experimentally or adversarially
-> theorem computes exact minimum repair
-> same target re-tested with repaired observer.
```

No absence-of-search-hit is treated as a proof of faithfulness; faithfulness is a
kernel theorem.

## Public theorem / private proof policy

`theorum/PUBLIC_THEOREM_REGISTER_2026_08_08.md` records the public theorem surface.
Canonical proof archives for the SC/SR chain developed in this cycle are retained
in the private `IEL3_FINAL_UPGRADED` proof vault on branch
`agent/recognition-private-proof-vault-2026-08-08`.

Earlier development commits may contain historical proof text. Going forward, new
public theorem files should expose theorem statement, assumptions, consequences,
claim boundary, and proof/certificate digest rather than the canonical derivation.

## Verification

The SR-01 through SR-03 linear core was validated at:

```text
7915fc739611370a0ef4befa63dcab0da9dcb23f
GitHub Actions run 31262853402
```

```text
Stratified Recognition tests     8/8 PASS
exact controls                     9 PASS
Singularity v5 recheck          30/30 PASS
Python 3.11                      PASS
Python 3.12                      PASS
```

The SR-04 public theorem surface was added at commit
`ecf25adbe0420164ec65f003e9384fc7bf49ffb1` and the same public certification
workflow completed successfully in run `31264426930`.

## Certificate

`RNKE_CERTIFICATE.json` records theorem, dependency, verifier, test, and CI hashes.
`RNKE_STATUS.md` records the reviewer-facing scope and claim boundary.

## Claim boundary

This layer does not claim computational hardness, cryptographic security,
universal physical-sensor faithfulness, nonlinear topological completeness,
infinite-dimensional minimum rank, or global exactness from differential closure.
Those require separate theorems/adapters.
