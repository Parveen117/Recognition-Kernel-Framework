# Morphic Operator Geometry

This folder is the canonical theorem-first home for the **Morphic Operator Geometry** manuscript and its Recognition-Kernel verification record.

## Provenance

The historical source was manually added on branch `agent/morphic-path-recognition-theorems` as:

`theorum/morphic_calculus/Morphic operator geometry..tex`

Pinned Git blob SHA-1:

`ebb8ef8c6fefdbcaaff8186cc3d470259dfbbb37`

The certification pipeline copies those exact bytes to `source_original.tex`. That file is evidence and is never silently repaired. The reviewer-facing `main.tex` is generated separately.

## Native terminology

The audited copy preserves the manuscript's native language and architecture, including:

```text
Morphic Algebra
Morphic Calculus
Morphic Operator Geometry
Ś-0 Emptiness Guard
collapse / quotient
phase connection
trace holonomy / class holonomy
diamond coherence
curvature / commutator residue
Laplacian / heat operator
spectral metric
Flat / Curved
Rigid / Deformable
```

## RNKE audit policy

A theorem environment is not certified merely because the historical manuscript labels it a theorem or supplies a proof sketch. Each claim receives a machine-readable status in `RNKE_CERTIFICATE.json`.

The verified publication copy makes several necessary corrections rather than hiding them:

1. The historical `Confluence ⇔ Flatness` equivalence is reduced to the proved diamond/class-holonomy statement. Confluence, pairwise generator commutation, and phase flatness are not treated as identical without extra hypotheses.
2. Twist isospectrality is proved under unitary conjugacy; isospectrality alone is not treated as a converse faithfulness theorem.
3. Holonomy accumulation uses the correct scaling `h_n = T/sqrt(n)`, not `T/n`.
4. Spectral metric descent is tied to an exact quotient seminorm condition, not merely `P Delta = Delta P`.
5. Equality of heat traces yields isospectrality under the declared trace-class/discrete-spectrum hypotheses, but does not by itself force curvature to vanish.
6. The historical no-go claim that curvature must always leave a spectral footprint is rejected. It conflicts with the proved Morphic Recognition path-blindness theorem. The audited copy replaces it with the exact blindness criterion and minimal-memory repair dimension.
7. Spectral completeness is treated as injectivity of the spectral-signature map. Finiteness or compactness alone is not accepted as proof of injectivity.

## Certification boundary

The intended final status is:

`RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`

That means source identity, reproducible LaTeX build, corrected elementary results, negative controls, and the theorem-status ledger are verified. It does **not** mean that every historical reduction, rigidity, information-geometry, Wasserstein, kernel, or universality claim has been formally proved.

See `CERTIFICATION_STATUS.md` and `CERTIFICATION_SUMMARY.md` after the certification workflow completes.
