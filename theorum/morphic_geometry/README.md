# Morphic Operator Geometry

This folder is the canonical theorem-first home for the **Morphic Operator Geometry** manuscript and its Recognition-Kernel verification record.

## Provenance

The historical source first entered branch `agent/morphic-path-recognition-theorems` manually. Its exact bytes are now preserved canonically as:

`theorum/morphic_geometry/source_original.tex`

Pinned Git blob SHA-1:

`ebb8ef8c6fefdbcaaff8186cc3d470259dfbbb37`

Source SHA-256:

`c810ae640cab85ca9eda6927a3512421de74fefd316bb9f220b5231f8cd36cea`

The original source is evidence and is never silently repaired. The reviewer-facing `main.tex` is generated separately and carries the mathematical/LaTeX corrections plus the RNKE verification appendix.

Verified `main.tex` SHA-256:

`bb376c2e0ace5d531d8a99ba845897f54b75583b1b2e0df12802e59497799702`

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

## RNKE audit result

Final status:

`RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`

The canonical-source CI build passes and produces a **20-page** audited manuscript. The historical source contains **22 theorem-level claims** and **5 axiom environments**.

Status groups:

```text
CERTIFIED_OR_CERTIFIED_AFTER_CORRECTION      3
REPLACED_BY_PROVED_OR_PRECISE_STATEMENT      5
CONDITIONAL                                  1
INCOMPLETE_OR_OVERBROAD                     11
REJECTED_AND_REPLACED                        1
META_GUARD                                    1
```

Certificate SHA-256:

`dc169404ab9dfe232d5fdd316b9e2fb17f19b0328c3cb610cbe54077b365ad46`

## Critical corrections

The verified publication copy makes necessary corrections rather than hiding them:

1. The historical `Confluence ⇔ Flatness` equivalence is reduced to the proved diamond/class-holonomy statement. Confluence, pairwise generator commutation, and phase flatness are not treated as identical without extra hypotheses.
2. Twist isospectrality is proved under unitary conjugacy; isospectrality alone is not treated as a converse faithfulness theorem.
3. Holonomy accumulation uses the correct scaling `h_n = T/sqrt(n)`, not `T/n`.
4. Spectral metric descent is tied to an exact quotient seminorm condition, not merely `P Delta = Delta P`.
5. Equality of heat traces yields isospectrality under the declared trace-class/discrete-spectrum hypotheses, but does not by itself force curvature to vanish.
6. The historical no-go claim that curvature must always leave a spectral footprint is rejected. It conflicts with the proved Morphic Recognition path-blindness theorem. The audited copy replaces it with the exact blindness criterion and minimal-memory repair dimension.
7. Spectral completeness is treated as injectivity of the spectral-signature map. Finiteness or compactness alone is not accepted as proof of injectivity.

## Recognition compatibility

See `RECOGNITION_COMPATIBILITY.md` for the formal bridge to MR-02 and MR-03. The key separation is:

```text
flat class holonomy
    ≠ spectral completeness
    ≠ absence of path memory
```

Those levels coincide only when a separate recognition-faithfulness theorem closes the relevant observation kernel.

## Certification boundary

The certificate verifies exact source identity, reproducible LaTeX build, the corrected elementary results, and the theorem-status ledger. It does **not** certify the unresolved reduction, rigidity, information-geometry, Wasserstein, kernel, or universality program as established mathematics, and it is not a formal-proof-assistant certificate.

See `CERTIFICATION_STATUS.md`, `CERTIFICATION_SUMMARY.md`, and `RNKE_CERTIFICATE.json` for the machine-verifiable record.
