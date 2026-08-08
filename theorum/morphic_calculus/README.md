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

Verification may correct proof status or a source defect, but does not silently replace this language with application-specific terminology.

## Source gate

Uploaded canonical source candidate:

`Morphic calculus complete(1).tex`

Source SHA-256:

`ccc376bd423bb7266f9d66c2fb163596d35373f92790666767d60a01d115ffc1`

The untouched uploaded source remains provenance. A verified publication copy will be transferred here only after source-integrity, LaTeX, theorem-obligation, and RNKE certification gates are recorded.

## Current status

```text
SOURCE IDENTIFIED                         PASS
SOURCE HASH PINNED                       PASS
NATIVE TERMINOLOGY PRESERVATION          REQUIRED
RAW LATEX COMPILE                        FAIL
FULL MATHEMATICAL CERTIFICATION          INCOMPLETE
RNKE FULL-MANUSCRIPT CERTIFICATE         NOT YET ISSUED
TRANSFER AS VERIFIED MAIN.TEX            BLOCKED UNTIL ABOVE GATES CLOSE
```

The current raw compile reaches the body and then fails on an unconfigured Unicode implication symbol `⇒`. This is a LaTeX source defect, not by itself a mathematical refutation.

The older flat-clock wording must also be audited carefully: loss of resolution of the selected clock is not automatically proof that the native transition/seam is zero.

See `CERTIFICATION_STATUS.md` for the gate record.
