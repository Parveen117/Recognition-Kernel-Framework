# Public Theorem Register — 2026-08-08

## Publication policy

The Recognition-Kernel-Framework repository is the public theorem surface.

Public files expose:

- theorem statements;
- hypotheses;
- exact consequences;
- claim boundaries;
- verification/certificate status.

The canonical proof archive and proof-control notes for this theorem family are retained in the private IEL proof vault. Earlier development commits may contain historical proof text; those remain part of Git history, but they are not the canonical proof-storage surface going forward.

## Singularity Calculus theorem chain

Public theorem statements currently include:

```text
SC-01  Orientation Reversal No-Singularity
SC-02  Process-Form Curvature and Maxwell Defect
SC-03  Distributional Seam Curvature
SC-04  Tangential-Jump Removability and Gauge
SC-05  Seam Stokes Memory
SC-06  Regular/Singular Typed Non-Cancellation
SC-07  Piecewise Enthalpy Seam Law
SC-08  Seam Gauge Class and Period Memory
SC-09  Master Singularity Closure
SC-10  Finite Multi-Seam Additivity and Closure
SC-11  Seam-Filler Cocycle and Curvature Interaction
SC-12  Normal-Crossing No-Spurious-Double-Delta
SC-13  Stratified Bianchi Junction Residue
SC-14  Triple Normal-Crossing Alternating Junction
SC-15  Codimension-Three Realizability Obstruction
SC-16  General Normal-Crossing Jump Complex
SC-17  Total Stratified Differential
SC-18  General Realizability Obstruction and Jump Cohomology
```

The abstract finite normal-crossing hierarchy terminates at SC-18 through the general operator identity

\[
\boxed{D_\Delta^2=0}
\]

and the totalized identity

\[
\boxed{\mathbb D^2=0}
\]

under the stated compatibility hypotheses.

## Stratified Recognition theorem chain

```text
SR-01  Stratified Target-Faithfulness and Decoder
SR-02  Stratum-Truncation Blindness and Minimum Repair
SR-03  Differential-Obstruction Faithfulness and False-Commit No-Go
SR-04  Physical Observer Blindness and Minimum Sensor Repair
```

The device-facing public repair law is

\[
\boxed{
 m_{\min}
 =
 \operatorname{rank}(\Pi|_{\ker S})
 =
 \operatorname{rank}
 \begin{pmatrix}S\\\Pi\end{pmatrix}
 -\operatorname{rank}S.
}
\]

For a compatibility target \(\partial\), observer blindness is witnessed by

\[
\boxed{Sv=0,\qquad \partial v\neq0.}
\]

and the exact minimum repair burden is

\[
\boxed{\operatorname{rank}(\partial|_{\ker S}).}
\]

## Canonical private proof vault

Repository: `IEL3_FINAL_UPGRADED` (private)

Branch:

```text
agent/recognition-private-proof-vault-2026-08-08
```

Vault root:

```text
with verification/recognition_proof_vault_2026_08_08/
```

The private vault contains canonical proof archives for SC-01 through SC-18 and SR-01 through SR-04, together with an exact theorem-chain verifier.

## Public claim boundary

The theorem register does not claim:

- computational hardness;
- universal physical-sensor linearity;
- automatic topological or microscopic interpretation;
- infinite-family normal-crossing convergence;
- nontransverse singular-stratum theory;
- production hardware safety certification.

Domain-specific devices require explicit adapters and bench evidence.
