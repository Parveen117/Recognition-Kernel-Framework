# Recognition Kernel Completion of the Five-Label Weil Endpoint

This is the current reviewer-facing paper draft after moving certified MP theorem nodes into RKF and expanding the proof skeletons, numerical certificates and reproducibility boundary.

## Main source

```text
papers/rkf_completed_weil_endpoint/main.tex
```

## Reviewer guide

```text
papers/rkf_completed_weil_endpoint/REVIEWER_GUIDE.md
```

## Corrected proof chain

```text
positive-eta amplitude path equality
-> zero-as-cut endpoint discipline
-> common five-matrix seam integer
-> certified M3 positive accepted block
-> one-sector terminal reduction
-> zero-cut T03 projection defect
-> classical explicit-formula / Weil-criterion membrane
```

The older fragile route through an independent even-source positivity assertion is not used.

## Main theorem nodes now expanded

```text
Classical normalization contract
Framework minimality / source restriction and minimal lift
Fixed-five positive-eta path equality
Zero-as-cut projector theorem
Common five-matrix covariance
Certified M3 accepted block
Formal single-sector terminal sufficiency
Six-block T03 source-Gram convergence
Zero-cut projection-defect positivity
Independent T18--T20 odd burden appendix
Auxiliary certified theorem-node appendix
```

## Numerical values now visible in the paper

```text
M3 interval:
  3.08520376681449e-13 < M3 < 2.993597611951253e-12

T19 burden:
  beta_partial^cut <= 0.9998319617060448 < 1

T20 strict reserve:
  1 - beta_partial^cut >= 0.0001680382939552
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

## Reproducibility records

```text
Reviewer reproducibility archive DOI: 10.5281/zenodo.21760119
Unified publication record DOI:     10.5281/zenodo.21735284
```

## Compilation

The source uses standard LaTeX packages:

```text
pdflatex main.tex
pdflatex main.tex
```

No bibliography file is required for this draft because theorem provenance is recorded through local RKF theorem folders and the reviewer reproducibility archive.

## Claim discipline

This paper draft records the RKF-native endpoint theorem chain and clearly marks the classical terminal membrane:

```text
classical completed explicit formula
+ classical Weil criterion in the declared normalization
```

It does not claim that raw UGD, the prime torus, or the diagonal Euler determinant alone proves RH. It does not claim that the even sector is absent. It does not use independent b3 boxes to prove M3.
