# SE14 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Complete source-null calibration | SE14.1--SE14.5; support, Parseval and polarization | Same full form, domain, kernel and inertia; finite comparisons can differ |
| Uniform moving-calibration edge recovery | SE14.6--SE14.11; compact band transform and full-null tail identity | Fixed aperture and cap, arbitrary uniformly bounded source-null marker choices, even without marker convergence |
| Uniform mode recovery and local completeness | SE14.12--SE14.14 | Common finite head for the bounded marker family at a fixed cutoff; effective arithmetic still requires an enclosable chosen marker |
| Radius-0.840 source certificate | SE14.15--SE14.25; complete frequency condition, 208 interval pivots and all errors | Complete complex odd source floor 1e-20 through radius 21/25 |
| Native invariant return | SE14.26--SE14.27 and inclusion | Local kappa_eta=0 and zero nullity through the certified radius; no global count inferred |

## Reproducible verification

```text
python proof_lab/endpoint_moving_calibration_certificate.py --check
python proof_lab/endpoint_observer_index_certificate.py --check
python -m unittest proof_lab.test_endpoint_moving_calibration_certificate proof_lab.test_endpoint_aperture_convergence_certificate proof_lab.test_endpoint_support_marker_certificate proof_lab.test_endpoint_precision_frontier_certificate proof_lab.test_endpoint_prime_power_certificate proof_lab.test_endpoint_prime_event_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The supported Python runtime is 3.12.14. The new full replay uses
only the standard library and unchanged local imports. All point
values use outward intervals; all signed-Gram sums are exact integers.
A separate directed 512-digit LDL acts on the archived exact rational
candidate. Source-to-candidate error, quadrature and the entire
infinite complement are charged independently.

The nine new controls cover signed integer interval operations,
independent shift-2048 Gamma readings through the far-tail boundary,
direct j_1/j_3 formulas through z=256 and a widened node interval,
all 208 retained odd orders against the Parseval identity, the
recalibration reading, high-precision LDL against exact ill-conditioned
rank-one pivots and an indefinite control, marker harmonics against
Chebyshev identities, exact support-null translations with a nonnull
overlap control, and the larger analytic ellipse and its error bound.

## Executed verification record

The full generating replay and a fresh complete read-only replay
both returned PASS under Python 3.12.14. Each recomputed the entire
frequency corridor, 1024 Gauss panels, coefficients, exact signed-Gram
sums, pole, all 208 interval LDL pivots and every error allowance.
Neither loads the diagnostic candidate checkpoint. The recomputed
matrix and complete result match their archives exactly. Matrix SHA256:
c5f6ddb6ecc9cbf75b7e64178ad9d5c7c0f76e3bdaeb03e1f26de2fcaa202d0c.

The tail proof accepts 1923 dyadic cells, maximum depth six, covering
[512,2048] exactly. Their minimum certified lower value exceeds
0.10069637213, above the cap 0.1. Every remaining frequency has a
certified floor greater than 0.31700509752. The complete head operator
error is below 2.120e-25, and all 208 directed interval LDL pivots
pass. These are enclosed outputs, not sampled spectral estimates.

The first combined run passed its numerical controls but found the
not-yet-generated source-pin file through the navigation link test.
That file has now been generated. The complete final rerun passed
all 41 tests: nine new controls, twenty-four inherited certificate
controls and eight mathematics-navigation checks.

The inherited moving-reference program's 21 exact rational controls
passed a fresh read-only replay. They do not establish any uncomputed
global source count or formal Atiyah--Singer verification.

The required Node engine gate was executed and failed at the unchanged
tests/verify.cjs pin comparison under installed Node 24.19.0. Its actual
hash is 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e;
the expected hash is
f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The documented Node 22.16.0 runtime is unavailable here. The existing
pins were not regenerated. Engine-gate and remote-CI success are not
claimed; the Python mathematical replays are separate evidence.

## Boundaries and preservation

The new uniform theorem fixes the aperture and cap. Its multiplier
family must be bounded and exactly source-null on the whole carrier.
It does not authorize arbitrary physical observer changes, unsigned
replacement of the source, or loss of cross terms. Positivity is still
a source property; invariance alone never makes a count zero.

Local positive margins imply local zero obstruction. SE13's global
criterion still requires zero counts along a cofinal positive-eta
sequence, or equivalent cofinal actual source control. Finite radius
increments through 0.840 do not provide unbounded coverage. A declining
sufficient margin is not an error estimate for global stabilization.

Prime 7, the global eta-zero sign, historical five-label closure, K0
and RH remain open. The actual zero-threshold source is not Fredholm.
The 208-mode comparison is not the historical five-label matrix.
No universal optimizer, global convergence rate, formal proof-assistant
verification or external review is claimed.

All 1158 parent blobs outside the four current navigation files are
byte-preserved. Eight files are added; no earlier theorem, arithmetic
certificate, preserved register or shared-engine file changes. The
source pins verify 88 inherited inputs, four new arithmetic artifacts
and the new theorem note. All 27 equation tags are individually unique.
All added local links resolve, and whitespace checking passes.

See the [theorems](SE14_MOVING_CALIBRATION_AND_INVARIANT_RECOVERY.md),
[source record](SE14_SOURCE_RECORD.md) and [pins](SE14_SOURCE_PINS.json).
