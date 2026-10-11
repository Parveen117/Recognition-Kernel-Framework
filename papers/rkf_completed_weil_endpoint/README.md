# Recognition Kernel Completion of the Five-Label Weil Endpoint

This is the current reviewer-facing paper draft after moving certified MP theorem nodes into RKF and expanding the proof skeletons, numerical certificates and reproducibility boundary.

## Main source

```text
papers/rkf_completed_weil_endpoint/main.tex
```

## Current endpoint development: SE6, 11 October 2026

[Paired prime-boundary apertures and a certified moment complement](development/SE6_PAIRED_APERTURE_AND_MOMENT_SCHUR.md)
proves the corrected joint observer is a strict contraction on the whole
odd aperture of radius 1/16. It retains the exact pairing of prime events
and completion poles, with a support rule and full-tail estimate.

At radius 1/2, including the prime 2, fifteen native moment readings leave
an infinite complement with source floor 8/1453. The full aperture sign
therefore reduces to an exact 15 by 15 Schur matrix with a proved positive
pivot. That matrix has not been evaluated, and the larger-aperture/global
sign remains open. This is separate from the historical five-label endpoint.

[Twenty-five exact rational checks](../../proof_lab/ENDPOINT_PAIRED_APERTURE_RESULT.json)
verify the scalar budgets. See [source record and prior art](development/SE6_SOURCE_RECORD.md),
[audit](development/SE6_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE5, 11 October 2026

[Stable exact observer and compact critical defect](development/SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md)
proves a positive lower bound for the corrected mismatch Gram. The exact
joint debt/boundary observer therefore exists as a bounded operator, and
its full regularized path converges in operator norm. This completes
bounded recovery; its norm being at most one remains unproved.

The completed source has an explicit compact defect relative to its
positive graph part. Finite-rank and all-prime tail bounds connect this
source to the existing MP Gold 06 spectral-certificate machinery. Zero
remains an essential threshold, and the floor constant has no numerical
enclosure yet. The full five-source endpoint and RH sign remain open.
See [source record](development/SE5_SOURCE_RECORD.md),
[audit](development/SE5_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE4, 11 October 2026

[Central Gamma repair and critical observer reserve](development/SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md)
settles a normalization issue left open in SE3. An explicit odd sine
packet rules out a unit contraction for SE3's full two-sheet Gamma model.
The repaired construction follows the declared T40 form: Gamma on the
central transform, prime events on the Hardy sheets, and their respective
debt factors retained in the native graph metric.

The full odd source now has an exact bounded factorization. A uniform
strict reserve is also proved impossible on this carrier, even after a
fixed finite-dimensional removal. The remaining sign question uses a
critical norm-one observer and source-relative boundary estimates.
See [source record](development/SE4_SOURCE_RECORD.md),
[audit](development/SE4_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).
No RH sign or complete five-source Feshbach certificate is claimed.

## Preceding endpoint development: SE3, 11 October 2026

SE3's projector, boundary and abstract regularization results remain valid.
Its full two-sheet Gamma source is superseded for this endpoint by SE4.

[Explicit Hardy compatibility and arithmetic observer path](development/SE3_HARDY_COMPATIBILITY_OBSERVER.md)
constructs the two-sheet projector, the minimum odd evaluation vector,
and its exact return to the T35 native graph boundary. It retains the
native metric in the debt pullback and writes the actual prime mismatch
as weighted translations, with the Gamma event factors unchanged.

An explicit regularized observer is now defined for every positive
regularization parameter. Its recovery residual tends strongly to zero,
and its finite boundary residual tends to zero in norm. The full joint
Gram still needs a uniform contraction bound toward zero; small residual
alone does not establish it. Source normalization on the selected
Feshbach complement and its complete five-source data remain open.
See [source record](development/SE3_SOURCE_RECORD.md) and
[scope](development/SE3_SCOPE.md). No actual RH sign is claimed.

## Preceding endpoint development: SE2, 11 October 2026

[Observer-path operator certificate](development/SE2_OBSERVER_PATH_OPERATOR_CERTIFICATE.md)
puts the observer in a joint debt/boundary recovery equation. It reuses the
Yang–Mills moving-observer and source-history route, permits both endpoint
frames to move, and retains complete operator defects and mixed pairings.
The finite observed block is eliminated first, so the certificate does not
assume an inverse for the completed source.

The written theorem derives source positivity and K0 positivity from the
contractive joint observer. With a supplied debt observer, its remaining
comparison is a five-column Gram. Constructing that observer for the
actual RH source remains open. See the [YM source record](development/SE2_YM_SOURCE_RECORD.md)
and [scope](development/SE2_SCOPE.md). The historical main manuscript and
certificate pins are not rewritten by this development.

## Preceding endpoint development: SE1, 11 October 2026

[Native graph energy and a shared endpoint residual budget](development/SE1_SHARED_ENERGY_BUDGET.md)
adds a written quarter-energy identity, an exact 2,400-cell chart replay,
and a five-column residual bound for the existing sine/reserve route.
The conditional chart upper is below 2/15; the residual Gram coefficient
is below 8/5. See the [result](../../proof_lab/ENDPOINT_SHARED_ENERGY_RESULT.json)
and [source pins](development/SOURCE_PINS.json).

This development has not been promoted into the historical main manuscript.
The actual debt-paid source/chart identity and final endpoint matrix sign
remain open in SE1. The sharper chart number is not an RH certificate;
see the [claim boundary](CLAIM_BOUNDARY.md).

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
