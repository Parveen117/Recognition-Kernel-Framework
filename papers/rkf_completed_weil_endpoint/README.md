# Recognition Kernel Completion of the Five-Label Weil Endpoint

This is the current cleaned paper draft after moving certified MP theorem nodes into RKF.

## Main source

```text
papers/rkf_completed_weil_endpoint/main.tex
```

## Purpose

The paper is rewritten around the corrected theorem chain:

```text
positive-eta path equality
-> seam integer/common five-matrix reduction
-> certified M3 positive accepted block
-> one-sector terminal reduction
-> zero-cut T03 endpoint completion
-> classical completed-Weil / Weil-criterion membrane
```

The older fragile route through an independent even-source positivity assertion is not used.

## Key included theorem nodes

```text
Fixed-Five Positive-Eta Path Equality
Framework Minimality / Source-Restriction Repair
Common Five-Matrix Seam Integer
Certified M3 Accepted Block
Single-Sector Terminal Reduction
Zero-Cut T03 Projection-Defect Endpoint
```

## Repository dependencies

Terminal theorem capsules:

```text
theorum/
```

Reusable proof machinery:

```text
mp_gold/
```

## Compilation

The source is intentionally self-contained and uses only standard LaTeX packages:

```text
pdflatex main.tex
pdflatex main.tex
```

No bibliography is required for this draft because theorem provenance is recorded through the local RKF theorem folders rather than an external citation file.

## Claim discipline

This paper draft records the RKF-native endpoint theorem chain and then clearly marks the classical terminal membrane:

```text
classical completed explicit formula
+ classical Weil criterion in the declared normalization
```

It does not claim that raw UGD, the prime torus, or the diagonal Euler determinant alone proves RH.
