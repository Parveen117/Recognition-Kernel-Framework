# SE45 source and development record

13 October 2026 (Asia/Kolkata). Author: Monty.

Parent: `b07ccf7a97fbc1371119a3bfdb70c98ddeded14f`, branch
`agent/rh-source-energy-tail`, Recognition-Kernel-Framework.

## Decision and prior boundary

SE44 supplies fixed-turn jya, a general fixed-operator recurrence and a
varying-step residual. Its literal sine feedback retains a fixed source.
The next useful extension is to changing turns and changing sources,
with an explicit distinction between open-path calibration and a paired
curvature reading. Merely labelling the old recurrence residual as
curvature would not establish that distinction.

SE45 derives the variable-turn two-channel/scalar laws and their exact
two-reading blind case. It then attaches complete paired-path readings
to an inhomogeneous counting connection. A per-cell curvature bound
allows finite refinement to recover the lifted scalar flux, including
coarse full-turn collisions. Finally the source-preserving calibration
identity is extended to a changing, possibly noncommuting source, while
quantitative sine tracking is proved in the scalar circular sector.

## Existing results reused

| Source | Role and distinction |
| --- | --- |
| [Primitive order](../../operator_foundation/theory/NATIVE_PRIMITIVE_ORDER.md), [native algebra](../../operator_foundation/theory/01_NATIVE_ALGEBRA.md) | Typed cuts, lawful response composition and target-specific complete readings precede the finite representation. |
| [Completion and memory, N09](../../operator_foundation/theory/02_COMPLETION_AND_MEMORY.md) | Time-varying chronological memory is already available. SE45 does not claim to invent variable-step memory elimination. |
| [F00-E](../../theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md) | Derived scalar Euler, sine/cosine and completed radial calculus. |
| [SE30](../../papers/rkf_completed_weil_endpoint/development/SE30_CONSTANT_LAMBDA_COUNTING_AND_CUT.md) | Constant marked counting unit and formula product. |
| [SE41](SE41_ORDERED_RETURN_AND_MOVING_CUT_FEEDBACK.md) | Complementary response acquisition, fixed-source reconstruction and a one-step noisy rational update. The new long-run drift bound concerns literal scalar sine tracking. |
| [SE42](SE42_COUNTING_CURVATURE_AND_OBSERVER_MEMORY.md) | Counting connection curvature and its labelled mixed-response target. |
| [SE43](SE43_COUNTING_TO_EMK_SEAM_TRANSPORT.md) | Native translations, endpoint frame transport and ordered seam defects. |
| [SE44](SE44_TVSP_LINES_ANGLE_AND_NATIVE_JYA.md) | Native angle and period, counting lines, formal horizontal transport, fixed jya, mixed rotational curvature and fixed-source literal sine correction. |
| [RT-02](../../theorum/recognition_topology/02_abelian_holonomy_variation_transgression.md) | Existing abelian curvature/holonomy variation, with the explicit extra term for a changing connection. The polynomial flux proof here is a counting-specific construction, not a new general Stokes or transgression theorem. |
| [RT-03](../../theorum/recognition_topology/03_principal_holonomy_blindness_and_lifted_memory.md) | Existing terminal-phase kernel and retained branch repair. The new finite cell decoder supplies its lift using SE44's native period and a stated curvature bound. |

The native index and preserved register were consulted; the exact
SE41--SE44 boundaries control the continuation. Standard transfer,
gauge-covariance, rank, phase-lifting and contraction arguments are
derived on the declared carriers. No exhaustive literature search or
external novelty priority is claimed. The earlier supplied Surya notes
and compass remain recorded in SE44; they are not silently promoted
to additional physical or universal premises here.

## Orientation and observation details

SE44 defines forward horizontal response by P'=-A P. For the forward
T-then-V path P and V-then-T path Q, SE45 uses H=Q^(-1)P. Its first
mixed reading is -F. SE42's displayed positive-flow commutator instead
has +F. This is a declared convention difference; a negative control
rejects copying the sign without its orientation.

The exact response packets retain both input and output calibrations,
accepted/complementary columns and the ordered path label. The cell
example retains four separate complete phase readings and a source-derived
angle bound in native quarter units. It does not infer those bounds from
an identity-valued endpoint. The exact finite cell decoder handles its
recorded quarter-sector witness; the written theorem handles arbitrary
angles under its stated bound. This scope distinction is explicit.

The tracking tests use prescribed nonnegative scalar disturbances with
rational outward sine enclosures. They do not infer sensor noise from
successful closure or implement a predictor for an unknown future source.
All script arithmetic uses Python 3.12 and the prior finite rational,
polynomial and observer adapters. The shared operator engine is unchanged.

See [scope](SE45_SCOPE.md) for executed checks, supplied instances and
the inherited full-engine pin mismatch. Source hashes authenticate
bytes; the recorded response banks are the finite observer evidence.
