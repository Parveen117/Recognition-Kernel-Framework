# SE15 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Weighted pole bound | SE15.4--SE15.5; evaluated weighted Cauchy--Schwarz integral | Complete odd pole bounded by (log(3)-1) times the 1-m^2 weighted L2 norm |
| Complete prime mass | SE15.6--SE15.7; 1024-term alternating intervals and full remainders | Sum Lambda(n)/n^2 below 57/100, including every prime power |
| Global positive-eta zero count | SE15.8--SE15.10 and executed scalar replay | S_b >= -(326/369) I_X; kappa_eta=0 and zero nullity for eta>=326/369 |
| Signed localization and exterior bounds | SE15.11--SE15.20; jump identity, support geometry and complete tails | Explicit E_M and d_M with every cross term accounted for |
| Effective invariant bracket | SE15.21--SE15.24; injection of negative subspaces | kappa_eta(A)<=kappa_eta<=nu_r(A) under the stated error budget; the auxiliary shift is physical R-dagger R |
| Rational smaller-eta schedule | SE15.25--SE15.26 and executed budget rows | Conditional local obligations only; larger-aperture source signs have not been executed |

## Reproducible verification

```text
python proof_lab/endpoint_global_eta_certificate.py --check
python proof_lab/endpoint_observer_index_certificate.py --check
python -m unittest proof_lab.test_endpoint_global_eta_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The Python runtime is 3.12.14. The new script uses the standard library
and unchanged pinned local interval and constant routines. No
floating-point eigenvalue, optimization sample or downloaded numerical
table is a certificate input. Mathematical arguments about the full
source and infinite tails are written proofs; the executable checks
their rational and interval scalar hypotheses.

## Executed record

Both the generating run and a fresh complete read-only replay pass
all 39 scalar conditions, with exact archive agreement. The complete
prime-mass enclosure is contained in (0.56995690,0.56996508), and the
weighted boundary constant is strictly below 1/10. Their global
threshold is exactly 326/369, with weighted reserve 7877/36900.

All nine new independent controls pass. They compare binary logarithms
to direct rational series, the prime mass to a direct prime-power sieve
plus integral tail, and the weighted boundary constant to a positive
rational series. Exact controls retain complex cross terms, both pole
cross coefficients, the factor two in the Gamma jump transform, and
the source polynomial. Negative controls reject the wrong derivative
sign, native-isometry substitution, positive-diagonal-only inference,
and a zero target passed to the conditional schedule.

The final combined run passes all 21 tests: nine new independent
controls, four inherited interval/certificate controls and eight
mathematics-navigation checks. Earlier expensive aperture replays
are not repeated in this stage; their full archives and inputs are preserved.
The inherited moving-reference replay separately passes its 21 exact
rational controls. It is not a formal index-theorem verification.

The required Node engine gate was executed and failed at the unchanged
tests/verify.cjs pin comparison under installed Node 24.19.0. The actual
hash is 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e;
the expected hash is
f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The documented Node 22.16.0 runtime is unavailable. Existing pins are
not regenerated. Neither the engine gate nor remote CI is reported
as passing. The Python source checks are a separate evidence category.

## Conditional target table

| Desired global eta | M | Required aperture radius | Required physical lower floor | Local sign executed? |
| --- | --- | --- | --- | --- |
| 1/2 | 256 | 33/5 = 6.6 | -1/4 | No |
| 1/4 | 1024 | 8 | -1/8 | No |
| 1/10 | 2048 | 87/10 = 8.7 | -1/20 | No |
| 1/100 | 32768 | 23/2 = 11.5 | -1/200 | No |
| 1/1000 | 262144 | 68/5 = 13.6 | -1/2000 | No |

Each floor means s[h]>=floor times ||Rh||_2^2 for every h in that
entire odd aperture, not a finite matrix or sampled state. The budget
rows are labelled CONDITIONAL_LOCAL_OBLIGATION and cannot be promoted
to global zero counts without these hypotheses. The schedule is a
conservative sufficient bound, not an optimal aperture or work estimate.

## Boundaries and preservation

The executed global positive-eta bound and SE14's positive local
radius 21/25 concern different parameters. Eta=326/369 is not an
increase of radius 0.840, a measured distance to RH, or eta-zero
positivity. The weighted reserve is not claimed as a uniform native
reserve. The current positive local frontier remains unchanged.

Faithful observer changes transport the source, pairing, cut maps and
physical tolerance together. An L2 partition is not assumed to be a
native isometry. Sign conventions do not authorize removal of any
prime, Gamma or pole cross term. The general transfer only certifies
a nonnegative shifted source; zero nullity is separately proved for
the particular global eta=326/369 bound.

The cofinal eta-zero signs, global critical contraction, historical
five-label endpoint, K0 and RH remain open. No native elliptic adapter,
universal optimization rule, formal verification or external review
is supplied. The older source's non-Fredholm zero threshold is retained.

Source-pin, parent-preservation and local-link checks pass. All 1166
parent blobs outside the four navigation files are byte-preserved.
Seven new files and four navigation updates are the only changes
from SE14. The pins verify 96 inherited inputs, three new arithmetic
artifacts and the new theorem note. All 26 equation tags are unique
and ordered. Added local links resolve and whitespace checking passes.

See the [theorems](SE15_EFFECTIVE_LOCALIZATION_AND_GLOBAL_ETA.md),
[sources](SE15_SOURCE_RECORD.md) and [pins](SE15_SOURCE_PINS.json).
