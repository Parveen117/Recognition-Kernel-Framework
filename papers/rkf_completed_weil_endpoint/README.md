# Recognition Kernel Completion of the Five-Label Weil Endpoint

This is the current reviewer-facing paper draft after moving certified MP theorem nodes into RKF and expanding the proof skeletons, numerical certificates and reproducibility boundary.

## Main source

```text
papers/rkf_completed_weil_endpoint/main.tex
```

## Current endpoint development: SE15, 12 October 2026

[Effective localization and a global positive-eta certificate](development/SE15_EFFECTIVE_LOCALIZATION_AND_GLOBAL_ETA.md)
proves S_b >= -(326/369) I_X on the entire corrected complex odd
source. The actual global negative count and nullity are zero for
eta>=326/369. This uses complete prime-mass and weighted pole bounds,
with every prime power included; it is not an eta-zero certificate.

An exact signed localization identity supplies explicit full-source
tail and exterior bounds. For each smaller positive eta it gives a
sufficient aperture and physical local tolerance that would imply
global zero count. The printed larger-aperture source obligations
are conditional and have not been executed. Eta and aperture radius
are different parameters; the positive local frontier remains 0.840.
The cofinal eta-zero condition, global contractivity and RH remain open.

See the [result](../../proof_lab/ENDPOINT_GLOBAL_ETA_RESULT.json),
[replay](../../proof_lab/endpoint_global_eta_certificate.py),
[sources](development/SE15_SOURCE_RECORD.md),
[audit](development/SE15_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE14, 12 October 2026

[Moving calibration and uniform local recovery](development/SE14_MOVING_CALIBRATION_AND_INVARIANT_RECOVERY.md)
proves recovery of the same local lower source edge under arbitrary
uniformly bounded source-null calibrations. The marker can change at
every frequency refinement without itself converging. The aperture
and cap are fixed in this theorem; cofinal global coverage is still
required separately.

The executed certificate extends the complete complex odd source from
0.820 to 21/25=0.840. Its physical floor is 1e-20, native floor
1/2965000000000000000001 and squared observer reserve
2/32615000000000000000011. Three exactly null markers, all 208 pivots,
the entire frequency tail and infinite complement are included.
Native inclusion proves zero local obstruction kappa_eta for all
eta>=0 throughout the smaller apertures. These are actual source
counts; the remaining global eta-zero condition is not closed.

See the [result](../../proof_lab/ENDPOINT_MOVING_CALIBRATION_RESULT.json),
[replay](../../proof_lab/endpoint_moving_calibration_certificate.py),
[sources](development/SE14_SOURCE_RECORD.md),
[audit](development/SE14_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE13, 12 October 2026

[Aperture growth and the observer limit](development/SE13_APERTURE_GROWTH_AND_OBSERVER_LIMIT.md)
certifies the complete odd source through radius 41/50=0.820, with
physical floor 4e-16, native floor 1/71500000000000001 and squared
reserve 2/786500000000000011. All smaller apertures follow by inclusion.
The 196-mode certificate recalibrates the support marker and retains
the whole frequency tail, mixed block and infinite complement.

The convergence result identifies the correct limit: canonical aperture
observers converge on fixed event vectors and their norms increase to
the global norm. Their uniform operator-norm error remains at least
one at every finite aperture, by the actual escaping-packet proof.
Global closure requires cofinal source control and limit norm at most
one. A finite list of successful radii cannot establish that condition.

The companion [moving-reference index theorems](development/SE13_MOVING_REFERENCE_INDEX_THEOREMS.md)
allow all faithful observer charts and positive references to move.
They give Atiyah--Singer descent with a block certificate, covariant
spectral flow/index, and Birman--Schwinger inertia. Their actual-source
corollary makes the remaining condition an invariant-zero criterion:
kappa_eta=N_-(S_b+eta I)=0 along a cofinal positive-eta sequence.
The written hypotheses and 21 exact finite controls are distinguished;
the full source is not Fredholm at eta zero and its sign remains open.

See the [result](../../proof_lab/ENDPOINT_APERTURE_CONVERGENCE_RESULT.json),
[replay](../../proof_lab/endpoint_aperture_convergence_certificate.py),
[sources](development/SE13_SOURCE_RECORD.md),
[audit](development/SE13_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE12, 12 October 2026

[Support calibration and prime-5 crossing](development/SE12_SUPPORT_MARKER_AND_PRIME_FIVE.md)
certifies the full complex odd source through radius 161/200=0.805.
The source floor is 2e-15, native floor 1/13925000000000001 and
squared observer reserve 2/153175000000000011. Every smaller
aperture follows by native inclusion.

An exact support-zero cosine calibrates the finite comparison while
preserving the source. All 168 interval pivots, mixed and infinite
tails, and the marker's complete high-frequency condition pass.
At a specified frequency, removing the marker invalidates this
chosen positive cap. The next event is prime 7; the cofinal/global
sign remains open. No universal self-correction theorem is inferred.

See the [result](../../proof_lab/ENDPOINT_SUPPORT_MARKER_RESULT.json),
[replay](../../proof_lab/endpoint_support_marker_certificate.py),
[source record](development/SE12_SOURCE_RECORD.md),
[audit](development/SE12_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE11, 12 October 2026

SE12 now crosses the prime-5 event left open in this historical record.

[Precision frontier and cutoff obstruction](development/SE11_PRECISION_FRONTIER_AND_CUTOFF_OBSTRUCTION.md)
certifies the full odd source on radius 4/5 with floor 4e-15, native
floor 1/6600000000000001 and squared reserve 2/72600000000000011.
Its 116-mode certificate uses exact signed-Gram sums and includes the
entire infinite complement and every error.

An independent rational witness identifies a negative lower comparison
at radius 0.8047 with the same T=256 cutoff. Increasing only the modes
or precision cannot repair that comparison. This is not a negative
source value; a larger band or another proved comparison is needed.
Prime 5 and the cofinal/global sign remain open.

See the [result](../../proof_lab/ENDPOINT_PRECISION_FRONTIER_RESULT.json),
[cutoff witness](../../proof_lab/ENDPOINT_CUTOFF_OBSTRUCTION_RESULT.json),
[source record](development/SE11_SOURCE_RECORD.md),
[audit](development/SE11_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE10, 12 October 2026

[Prime-power crossing and certificate completeness](development/SE10_PRIME_POWER_AND_CERTIFICATE_COMPLETENESS.md)
certifies scale 7/5 across prime power 4. The whole odd physical aperture
of radius 7/10 has source floor 1/20000000000, native floor 1/466500000001
and squared observer reserve 2/5131500000011. Its 88-mode interval
certificate includes all mixed and infinite-tail terms.

The new local lower-edge theorem also shows that a strict positive
source margin can be detected by this certificate family with sufficient
frequency, mode and accuracy refinement. It does not assume positivity
at every aperture or bound the required work. Prime 5 and the cofinal
global sign remain open.

See the [result](../../proof_lab/ENDPOINT_PRIME_POWER_RESULT.json),
[source record](development/SE10_SOURCE_RECORD.md),
[audit](development/SE10_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE9, 12 October 2026

SE10 now crosses the prime-power-4 event left open in this historical record.

[Prime-event crossing and native continuity](development/SE9_PRIME_EVENT_AND_NATIVE_CONTINUITY.md)
certifies scale 9/8, crossing the activation of prime 3. The whole odd
physical aperture of radius 9/16 has source floor 1/500000, native floor
1/9906251 and squared observer reserve 2/108968761, with all mixed and
infinite-tail terms included. Every intermediate aperture is covered.

A fixed prime catalogue keeps the source equation intact through the
event. An explicit native continuity bound handles concentrated states
for which shrinking L2 overlap alone gives no small operator bound.
The next prime-power event and the cofinal/global sign remain open.

See the [replay result](../../proof_lab/ENDPOINT_PRIME_EVENT_RESULT.json),
[source record](development/SE9_SOURCE_RECORD.md),
[audit](development/SE9_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE8, 12 October 2026

SE9 now crosses the prime-3 event left open in this historical record.

[Moving observer and a certified signed transport](development/SE8_MOVING_OBSERVER_AND_SIGNED_TRANSPORT.md)
writes the actual dilation of the corrected prime--Gamma--pole source
and its native metric. A fixed reference chart now certifies scale 21/20,
giving source floor 1/100000, native floor 1/1806251 and squared observer
reserve 2/19868761 on radius 21/40 and every intermediate aperture.

The complete signed comparison passes even though its indefinite change
has norm larger than the old scalar floor. This instantiates SE2's
existing transport law; it does not rebrand it as a new general theorem.
The next prime event and a cofinal all-scale rule remain open.

See the [replay result](../../proof_lab/ENDPOINT_OBSERVER_TRANSPORT_RESULT.json),
[source record](development/SE8_SOURCE_RECORD.md),
[audit](development/SE8_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE7, 12 October 2026

[Full prime-active aperture and the fifteen-moment Schur sign](development/SE7_FULL_PRIME_ACTIVE_APERTURE.md)
certifies the corrected source on every complex odd state of radius 1/2,
with physical floor 1/25000, native floor 2/903127 and squared joint
observer reserve 4/9934397. No extra moment restriction remains there.

A forty-mode comparison matrix, enclosed quadrature, interval LDL and
complete infinite-tail bounds establish this result. It also proves
the positive sign of SE6's F_15 by domination, without computing its
entries. The global eta=0 sign and historical five-label endpoint remain
open. The frequency-split method has cited prior art.

See the [replay result](../../proof_lab/ENDPOINT_FULL_APERTURE_RESULT.json),
[source record](development/SE7_SOURCE_RECORD.md),
[audit](development/SE7_SCOPE.md) and [claim boundary](CLAIM_BOUNDARY.md).

## Preceding endpoint development: SE6, 11 October 2026

The full radius-1/2 sign left open in the historical SE6 record below
is now settled by SE7; its other scope restrictions remain in force.

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
