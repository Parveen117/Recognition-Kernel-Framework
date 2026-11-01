# SE13 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Aperture observer limit | SE13.2--SE13.6; closed event ranges, core density and canonical projections | Strong convergence on every fixed event; increasing norms tend to the actual global observer norm |
| Actual uniform-error obstruction | SE13.7--SE13.11; SE4 escaping packets and SE5 compact mismatch remainder | Norm of O_*-O_A is at least one at every finite aperture, and equals one if the global source is nonnegative |
| Global sign criterion | SE13.12--SE13.15; source identity and SE10 local completeness | Requires cofinal source control; infinitesimal steps in a bounded aperture range are insufficient |
| Recalibrated next aperture | SE13.16--SE13.24; full tail and 196 interval pivots | Complete complex odd source floor 1/2500000000000000 through radius 41/50 |
| Native local recovery | SE13.25--SE13.27 and native inclusion | Native floor 1/71500000000000001; squared reserve 2/786500000000000011 |
| Moving-reference index theorems | SE13.I1--SE13.I14; transported domains, pairings, symbols and connections | Conditional Atiyah--Singer descent/block certificate, spectral-flow/index and Birman--Schwinger inertia; classical results remain cited inputs |
| Actual invariant-zero criterion | SE13.I15--SE13.I18 and SE5's signed compact defect | Finite kappa_eta for eta>0; cofinal zero counts equivalent to positivity; fixed-eta local counts eventually capture it |

## What convergence means here

| Parameter or check | Established status |
| --- | --- |
| Global inverse regularization epsilon tends to zero | Operator-norm convergence already proved by SE5; this does not prove contractivity |
| Frequency, modes and precision at a fixed aperture | Local source-edge recovery and finite-certificate completeness from SE10, also valid for a fixed bounded support marker |
| Aperture tends to infinity | Strong convergence of the canonical exact observers; true local norms increase to the global norm |
| Uniform error of the whole aperture observer | Cannot tend to zero: the actual escaping-packet lower bound is one |
| Finite boundary component | Operator-norm convergence follows from its finite rank, reusing SE2 |
| Global norm at most one | Open; the finite sequence through radius 0.820 does not certify cofinal coverage |

SE13's new obstruction is a written proof on the actual source, not
a conclusion inferred from a toy matrix. The diagonal tolerance
criterion is a complete reduction of the remaining sign condition,
not a claim that its infinitely many tests have passed. A zero local
margin does not logically invalidate that non-strict protocol.

## Reproducible arithmetic

```text
python proof_lab/endpoint_aperture_convergence_certificate.py --check
python proof_lab/endpoint_observer_index_certificate.py --check
python -m unittest proof_lab.test_endpoint_aperture_convergence_certificate proof_lab.test_endpoint_support_marker_certificate proof_lab.test_endpoint_precision_frontier_certificate proof_lab.test_endpoint_prime_power_certificate proof_lab.test_endpoint_prime_event_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Python 3.12.14 is the supported runtime. The complete replay uses only
the standard library and pinned local imports. Node values use the
unchanged 90-digit outward class. The normalized Bessel recurrence
uses a 240-place integer interval grid, signed-Gram sums are exact
integers, and the archived candidate has forty significant digits.
A separate directed 320-digit LDL factorizes that exact rational
candidate. Its precision does not replace any source-to-candidate error.

The first attempt with the inherited 90-digit LDL was inconclusive
at zero-based pivot 106, with enclosure approximately [-0.723,0.479].
It produced no PASS archive. This was not treated as either a source
counterexample or a successful certificate. The subsequent refinement
retains the endpoint, marker, frequency and proposed positive floor.
The optional candidate checkpoint is explicitly marked uncertified and
is never loaded by the full replay or accepted as evidence.

Six new controls check signed integer interval arithmetic, independent
shift-2048 Gamma values through the far-tail boundary, j_1/j_3 formulas
through z=256 and a wide node enclosure, all retained Bessel orders
against the odd Parseval identity, the marker recalibration reading,
and the higher-precision LDL against exact ill-conditioned rank-one
pivots and an indefinite control.

## Executed verification record

The generating refined replay and a fresh independent full read-only
replay both returned PASS under Python 3.12.14. Each recomputed the
whole frequency corridor, 1024 Gauss panels, normalized coefficients,
exact Gram sums, pole, all 196 interval LDL pivots, matrix error and
infinite-complement allowances; neither read the candidate checkpoint.
The archived matrix SHA256 is
831b381d19e3abc9d6baf7ae2455c4618fd78133bf03e89b5710827dda7ee20a.

The 1757 accepted dyadic tail cells cover [512,2048] exactly, with
maximum depth seven and minimum certified lower value greater than
0.03106441198, above the required 0.03. All higher frequencies have
lower bound greater than 0.81054709486. The complete leading-matrix
operator error is less than 1.730e-21. These are enclosure outputs,
not sampled estimates.

The combined 32 tests passed: six new arithmetic controls, eighteen
inherited certificate controls, and eight mathematics-navigation tests.
The separate moving-reference program generated and independently
replayed all 21 exact Fraction controls. Their recorded status is
PASS_FINITE_RATIONAL_CONTROLS, not an Atiyah--Singer proof-assistant
verification or a computation of the actual global seam count.

Source integrity verified 77 unchanged parent inputs, six new arithmetic
artifacts and two new theorem notes against their Git-blob/SHA256 pins.
All added local links resolve; the 27 aperture equation tags and 18
index equation tags are individually unique. Whitespace checking passed.
The 1147 parent blobs outside the four navigation files are preserved.
The stage adds eleven files, with no modification of prior source proofs,
certificates or the shared engine.

The required Node engine gate was executed and failed at the unchanged
tests/verify.cjs pin comparison under installed Node 24.19.0. Its actual
hash is 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e;
the expected hash is
f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The documented Node 22.16.0 runtime is unavailable here. The existing
pins were not regenerated. Engine-gate and remote-CI success are not
claimed; the Python mathematical replays are separate passing evidence.

## Limits and preservation

The certified range is finite. Prime 7 at log(7)/2 lies outside the
new radius; cofinal source signs, the global eta=0 sign, historical
five-label closure, K0 and RH remain open. The strong-limit theorem
alone cannot settle any of those signs. A decrease in sufficient
local reserve is not a measured distance to global stabilization.

The index packet does not supply a new native elliptic symbol adapter
for RH. The actual source has essential spectrum at zero and is not
Fredholm there. Its proved invariant-zero condition uses positive-eta
counts; invariance alone does not show that any uncomputed count is
zero. The original user-supplied canvas is preserved unchanged.

The source definition, all earlier theorem and arithmetic files, and
the canonical engine are preserved. Only four active navigation files
are updated. The finite comparison is not the historical five-label
matrix. No universal marker rule, record aperture, proof-assistant
verification, external review or remote CI success is claimed.

See the [aperture proof](SE13_APERTURE_GROWTH_AND_OBSERVER_LIMIT.md),
[index theorems](SE13_MOVING_REFERENCE_INDEX_THEOREMS.md),
[source record](SE13_SOURCE_RECORD.md) and [pins](SE13_SOURCE_PINS.json).
