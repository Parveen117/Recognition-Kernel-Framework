# SE22 verification scope

12 October 2026. A global positive-shift improvement; eta=0 remains open.

## Exact executed result

```text
Entire corrected complex odd native carrier X
eta anchor                         227/400 = 0.5675
strict shifted native floor        1/1476000
implied nonnegative shift           837629/1476000
negative count and nullity          zero for eta >= 227/400
prime comparison alpha             103/200
uniform seed floor                 1/1000
complete pole burden upper         0.99499985722595977134... < 199/200
initial seed cells                 75
complete integral cells            6738
maximum bisection depth            14
complete prime catalogue head      604 prime powers through 4096
omitted prime powers               all covered by inherited tails
unbounded spatial exterior         covered analytically; pole integral included
```

The strict native floor belongs to the shifted source. At the implied
smaller shift only nonnegativity is claimed. No exact lower spectral
edge, eta-zero sign or new positive support radius is inferred.

The replay has nine named checks. Its integral uses exact rational
numerator masses and positive whole-cell denominator lower bounds.
There is no sampled quadrature acceptance or omitted spatial tail.
The final result stores the exact partition digest; the read-only
replay reconstructs every cell and verifies complete adjacency, positive
seed floors, the total numerator mass 1/12 and the strict pole cap.

## Independent controls

Nine new Python tests cover independent monomial integration,
partition additivity, a separately integrable linear-seed example,
a deliberately false midpoint heuristic, refusal of nonpositive seeds
and non-strict caps, complete complex rank-one target correlations,
direct even-weight translations at the new alpha, the old comparison's
strict failure, and the exact native norm conversion and claim boundary.

The complete test result and source replay are checked under Python
3.12.14. The existing eight navigation tests pass. The read-only replay
checks the new source pins. The inherited engine remains unchanged.

## Required engine check

The required command was run under Node v24.19.0:

```text
node operator_foundation/verify_all.cjs --check
FAIL at tests/verify.cjs --check: Pin mismatch
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
```

This matches the earlier documented failure. Its pins are not replaced.
The new source certificate's PASS does not assert a repository-wide
engine PASS, formal proof-assistant check or external review.

## Boundary retained

SE21's eta-zero sign on V_16 and SE14's positive support radius 21/25
remain valid and unchanged. The new global positive-shift frontier
supersedes SE17's sufficient shift 10883/18450, without invalidating
the earlier certificate. Eta=1/2, global eta=0, the universal signed
arithmetic inequality, the infinite complementary source sign,
critical recovery, historical five-label attachment, K0 and RH remain
open. SE20's obstruction explains why this fixed diagonal seed alone
cannot be extrapolated to zero.

See the [proof](SE22_GLOBAL_RECIPROCAL_POLE.md),
[source record](SE22_SOURCE_RECORD.md), [pins](SE22_SOURCE_PINS.json)
and [result](../../../proof_lab/ENDPOINT_RECIPROCAL_POLE_RESULT.json).
