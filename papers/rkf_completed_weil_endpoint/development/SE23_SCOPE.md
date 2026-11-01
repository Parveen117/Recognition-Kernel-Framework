# SE23 verification scope

12 October 2026. Complete positive-shift certificate; global eta=0 is open.

| Item | Executed result |
| --- | --- |
| Source | Entire corrected complex odd native carrier X |
| Eta anchor | 113/200 = 0.565 |
| Strict shifted native floor | 1/1476000 |
| Sufficient nonnegative shift | 833939/1476000, approximately 0.56499932249 |
| Negative count and nullity | Zero for eta >= 113/200 |
| Prime comparison alpha | 513/1000 |
| Uniform diagonal seed floor | 1/1000 |
| Retained observation | One normalized coordinate of the actual sixteen-sheet Gamma event analysis |
| Recovered target budget upper | 0.99499934919474752598... < 199/200 |
| Same-parameter diagonal-only burden lower | 1.03640844707971711809... > 103/100 |
| Whole integral cells | 4495, following 88 initial seed cells; maximum depth 14 |
| Prime head and tails | 604 prime powers through 4096; every remaining power covered |
| Infinite spatial exterior | Analytic positive seed and complete residual-target integral |
| Dynamic comparison | Norm-continuous Fredholm path; one positive crossing, negative count 1 to 0 |

The dynamic path is a family of lower comparisons to the same source.
It is not a path changing the original source and is not the eta-to-zero
path. One observation combines the four rational trial monomials and
sixteen event sheets with their full mixed energy. Their contributions
are not counted as independent observations.

The direct target budget is a sufficient upper certificate. It is not
an asserted optimal inverse evaluation. The implied smaller shift has
a nonnegativity conclusion; no strict native gap or zero nullity is
asserted at that exact smaller value.

## Verification performed

The replay has ten named checks, reconstructs the entire adjacent
partition and verifies its digest, checks full-cell lower bounds and
the enclosure of the exact total polynomial target mass, and checks
26 SHA-256 source pins. Fractions are exact and the inherited Decimal
operations round outward at 90 digits. No exploratory floating-point
file enters the replay.

Nine new independent Python controls cover the Dirichlet Green
equation for all retained modes, the separately integrated full event
energy and complex projection inequality, exact polynomial integrals,
a deliberately false midpoint heuristic, prime-breakpoint upper
controls against a finite exact catalogue, the essential observation
cost, the oriented crossing, invalid inputs, and native conversion
with the eta-zero claim boundary. These and the eight existing
navigation tests pass under Python 3.12.14.

## Required engine gate

The required unchanged check was run under Node v24.19.0:

```text
node operator_foundation/verify_all.cjs --check
FAIL at tests/verify.cjs --check: Pin mismatch
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
```

This is the existing failure. No engine file or old pin is modified.
The source certificate's PASS is separate from this failed gate.
No proof-assistant verification or external review is asserted.

## Boundary

Eta=1/2, global eta=0, the complete signed arithmetic inequality,
the infinite complementary source sign, critical recovery,
historical five-label attachment, K0 and RH remain open. The local
radius 21/25 and SE21's finite V_16 eta-zero sign are unchanged.
The fixed-Gamma seed obstruction prevents treating this stage as
an automatic convergence proof to zero. No general Atiyah--Singer
extension or orientation-free spectral flow is claimed.

See the [proof](SE23_DYNAMIC_RESIDUAL_OBSERVER.md),
[sources](SE23_SOURCE_RECORD.md), [pins](SE23_SOURCE_PINS.json)
and [result](../../../proof_lab/ENDPOINT_RESIDUAL_OBSERVER_RESULT.json).
