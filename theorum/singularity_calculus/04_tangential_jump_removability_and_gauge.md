# SC-04 — Tangential-Jump Removability and Coherent-Gauge Theorem

## 1. Local decomposition of the jump

Near a regular seam \(\Sigma=\{\rho=0\}\), choose local coordinates

\[
(\rho,y^1,\ldots,y^{n-1}).
\]

Write the jump 1-form as

\[
\alpha_+-\alpha_-
=
a\,d\rho+\sum_j b_j\,dy^j.
\]

Then the singular curvature term from SC-03 is

\[
\Omega_\Sigma
=
\delta(\rho)
\sum_j b_j\,d\rho\wedge dy^j.
\]

The normal coefficient \(a\) does not contribute.

## Theorem 1.1 — Removable seam-curvature criterion

The seam-supported curvature current vanishes if and only if the tangential
jump residue vanishes:

\[
\boxed{
\Omega_\Sigma=0
\iff
R_\Sigma=i^*(\alpha_+-\alpha_-)=0.
}
\]

### Proof

In the local decomposition,

\[
d\rho\wedge(\alpha_+-\alpha_-)
=
\sum_j b_j\,d\rho\wedge dy^j.
\]

The current is zero exactly when all tangential coefficients \(b_j\) vanish on
the seam, which is exactly \(i^*(\alpha_+-\alpha_-)=0\). ∎

## 2. Coherent gauge changes

Suppose the two side forms transform by

\[
\alpha_\pm'
=
\alpha_\pm+d\chi_\pm.
\]

Assume the gauge functions have the same seam trace:

\[
i^*\chi_+=i^*\chi_-.
\]

## Theorem 2.1 — Coherent-gauge invariance of seam residue

Under the preceding condition,

\[
\boxed{
R_\Sigma'=R_\Sigma.
}
\]

### Proof

Pull back the transformed jump:

\[
R_\Sigma'
=
R_\Sigma
+
i^*d(\chi_+-\chi_-).
\]

Pullback commutes with exterior differentiation, so

\[
i^*d(\chi_+-\chi_-)
=
d_\Sigma\,i^*(\chi_+-\chi_-)
=
0.
\]

Hence \(R_\Sigma'=R_\Sigma\). ∎

## Corollary 2.2 — Gauge mismatch is itself gluing data

If the gauge traces do not agree on \(\Sigma\), the change in residue is the
exact seam form

\[
d_\Sigma\,i^*(\chi_+-\chi_-).
\]

Therefore a discontinuous gauge change may not be silently treated as a
representation change. Its transition function belongs to the seam/gluing
ledger.

## Recognition interpretation

This is a representation-faithfulness rule:

```text
coherent re-presentation
    => same seam residue;

mismatched seam gauge
    => additional declared gluing datum.
```

## Status

```text
TANGENTIAL-JUMP REMOVABILITY     PROVED
NORMAL-ONLY JUMP GIVES NO DELTA CURVATURE PROVED
COHERENT-GAUGE RESIDUE INVARIANCE PROVED
MISMATCHED GAUGE AS EXTRA GLUING DATA       PROVED AS TRANSFORMATION LAW
```
