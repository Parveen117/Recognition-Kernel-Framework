# Morphic Calculus

This folder is the canonical theorem-first home for the Morphic Calculus manuscript and its Recognition-Kernel verification record.

## Native terminology

The manuscript language is preserved, including:

```text
Recognition
Śūnya
Cut
Morphisum / Morphic transformation
coherence
chosen measure / clock / scale
g-derivative
collapse / loss of distinguishability
morphic flow
commutator / curvature
holonomy
clock recovery as representation choice
```

Verification may correct proof status or a source defect, but it does not silently replace this language with application-specific terminology.

## Canonical source and verified publication copy

Uploaded canonical source:

`Morphic calculus complete(1).tex`

Exact source snapshot:

`source_original.tex`

Source SHA-256:

`ccc376bd423bb7266f9d66c2fb163596d35373f92790666767d60a01d115ffc1`

Audited publication copy:

`main.tex`

Verified `main.tex` SHA-256:

`b8179549dc097417b10bde505c4025924c591702052fb1ef9b294d6077570c17`

`source_original.tex` preserves the supplied manuscript as provenance. `main.tex` is the compile-clean, audited publication copy. The source vocabulary and the Śūnya/Cut/Morphisum/Recognition architecture are retained.

## RNKE certification status

```text
SOURCE IDENTIFIED                                  PASS
EXACT SOURCE SHA PINNED                            PASS
EXACT SOURCE TRANSFERRED                           PASS
NATIVE TERMINOLOGY PRESERVED                       PASS
VERIFIED MAIN.TEX GENERATED                        PASS
LATEX BUILD                                        PASS
COMPILED PAGES                                     55
CLAIM ENVIRONMENTS                                 12
AXIOM ENVIRONMENTS                                  0
RNKE STATUS                                        RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS
FULL MANUSCRIPT MATHEMATICAL CERTIFICATION         FALSE
FORMAL PROOF-ASSISTANT CERTIFICATION               FALSE
```

Claim-status ledger:

```text
CERTIFIED_ALGEBRAIC                                 5
CONDITIONAL_ON_DECLARED_REPRESENTATION              2
INCOMPLETE_OR_OVERBROAD_IN_SOURCE                   4
META_GUARD_NOT_MATHEMATICAL_CONSISTENCY_PROOF       1
```

RNKE certificate SHA-256:

`36236e50b166c5c0ef13be3dc6c3fa4b56271bc0c45274440aea0b1b8d029c25`

The verified publication copy also keeps an important hardened distinction from Recognition-Seam Calculus: a flat or singular clock is failure of that chosen rate presentation, not automatic proof that the underlying native transition or seam is zero. Broad foundational-closure and universality statements remain open unless separately proved.

See:

- `CERTIFICATION_STATUS.md` — compact gate state
- `CERTIFICATION_SUMMARY.md` — build and claim-count summary
- `RNKE_CERTIFICATE.json` — machine-readable theorem-status ledger
- `PREPARE_MANIFEST.json` — source/materialization manifest
- `source_original.tex` — untouched source provenance
- `main.tex` — verified publication copy
