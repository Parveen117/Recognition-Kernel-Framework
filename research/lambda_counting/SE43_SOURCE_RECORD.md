# SE43 source comparison and development record

13 October 2026 (Asia/Kolkata). Author: Monty.

RKF parent: `56c6a6c05a6643c1ff685cb1ad135119fb70ac3d`, branch
`agent/rh-source-energy-tail`. Public Publications snapshot:
`7ad1f7b6013da4f1d62d642f779f27bae41c9bcf`.

## Decision after comparison

The user asked whether the new counting curvature duplicated the existing
EMK torus/helical geometry, emphasizing that TVSP and classical names do
not imply the same movement rules. The comparison found overlapping
connection mechanisms, but different carriers and targets. SE42 remains
a valid counting-carrier derivation and observer interface. Its generic
curvature formula is not promoted to a newly discovered universal
curvature or to a replacement for EMK geometry. Re-derivation stops here.

SE43 instead attaches the specific count translations and response module
to explicit seam generators. It computes the exact two-order relation,
its moving-frame law, its observer decoder and the unit depth needed to
retain a seam defect. An integer-memory example consumes MR-03 rather
than announcing the cocycle construction as new. The public G3 boundary
explicitly leaves its non-Abelian lift unimplemented. SE43 supplies a
specified matrix-valued counting lift and a non-Abelian path-memory
example; it does not close every possible lift, distributional term or
physical adapter left open there.

## Public geometry sources actually compared

All links in this table are immutable public source links. The recorded
blob identities are in [the pins](SE43_SOURCE_PINS.json).

| Source | What is reused or distinguished |
| --- | --- |
| [EMK-C1 connection calculus](https://github.com/Parveen117/Publications/blob/7ad1f7b6013da4f1d62d642f779f27bae41c9bcf/papers/emk-ugd-algebra/CONNECTION_CALCULUS.md) | General connection identity, direction-frame subtraction, covariance and observation contract. Its inner R/K directions are not identified with the counting D_i. |
| [EMK-G1/G2/G3 and UGD-G1](https://github.com/Parveen117/Publications/blob/7ad1f7b6013da4f1d62d642f779f27bae41c9bcf/papers/emk-recognition-geometry/README.md) | Metric curvature, recognition curvature, quotient topology, global monodromy and separate phase/scale/sheet memory. These are not one scalar target. |
| [EMK-G3 executable source](https://github.com/Parveen117/Publications/blob/7ad1f7b6013da4f1d62d642f779f27bae41c9bcf/papers/emk-recognition-geometry/certificates/emkg3_helical_sheet_memory.py) | The actual rho, inverse-rho and deck functions; the different forward map in `certify_T2`; declared non-Abelian/distributional boundary. |
| [EMK-G2 executable source](https://github.com/Parveen117/Publications/blob/7ad1f7b6013da4f1d62d642f779f27bae41c9bcf/papers/emk-recognition-geometry/certificates/emkg2_global_quotient_holonomy.py) | The exact inherited period `L_PERIOD = Fr(5)` used in the deck-sign audit. Only this source constant is consumed by the new finite audit. |
| [Recognition-seam topology capsules](https://github.com/Parveen117/Publications/blob/7ad1f7b6013da4f1d62d642f779f27bae41c9bcf/papers/recognition-seam-topology/README.md) | Already existing projected-return blindness, retained sheets, ordered loops and sector-specific closure. No new priority for these mechanisms. |

The geometry front door describes the helical object as a mapping torus,
not a curve drawn in ambient Euclidean space. The product-fibre table
in SE43 is an explicitly conditional presentation of point/circle,
line/cylinder and circle/torus. A complete equivalence to the user's
TVSP/double-helical movement system was not established by this source
comparison. No unseen diagram or unspecified double-helical rule is
treated as if it had been verified.

## The scoped orientation correction

The public G3 T1 deck uses rho^(-1) when u increases by L. Its T2
compensator uses a minus sign, while the T2 check increases both u and
the fibre coordinates. Thus T2 tests a forward lift distinct from T1's
deck. With the source period 5 and scale shift 2/5, the minus-compensated
scale changes by -4/5 on the actual deck. The plus-compensated scale is
invariant. Phase modulo 6 can mask part of this discrepancy, so the
scale sector is used as the decisive witness.

SE43 records this as a negative control and uses the corrected
deck-compatible compensator. The older public certificate is not edited,
re-pinned or silently labelled as fully revalidated. This correction
concerns the T2 deck-invariance claim; it does not negate T1's quotient
construction, the distinction between local flatness and global memory,
or the other independently stated sectors.

## Local dependencies and integration

| Source | Role |
| --- | --- |
| [Primitive order](../../operator_foundation/theory/NATIVE_PRIMITIVE_ORDER.md), [native algebra](../../operator_foundation/theory/01_NATIVE_ALGEBRA.md) | Cut scalars and typed paths first; state observation and algebra homomorphism remain distinct. |
| [SE30](../../papers/rkf_completed_weil_endpoint/development/SE30_CONSTANT_LAMBDA_COUNTING_AND_CUT.md) | Falling-count basis, formula product and faithful coefficient chart. |
| [SE31](../../papers/rkf_completed_weil_endpoint/development/SE31_COUNTING_OPERATOR_RECOVERY_AND_ORDERED_FLOW.md) | Ordered counting actions and memory-cut rules. |
| [SE34](SE34_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY.md) | Separated unit completion and retained coefficient memory. |
| [SE42 theorem](SE42_COUNTING_CURVATURE_AND_OBSERVER_MEMORY.md), [scope](SE42_SCOPE.md), [record](SE42_SOURCE_RECORD.md) | Existing counting connection, frame transport and complementary observer interface, with its original boundaries. |
| [SE42 evaluator](../../proof_lab/counting_curvature.py) | Reused finite rational polynomial/matrix operations; no second native operator engine. |
| [MR-03](../../theorum/morphic_recognition/03_cocycle_lifted_path_recognition.md) | Existing associative memory extension and projection blindness. |
| [Noncommutative holonomy](../../theorum/thermodynamics/lambda_geometry/11_noncommutative_holonomy_and_irreducibility.md) | Already established path-order and spectral-shadow distinction; not identified with the new flat seam example. |

The new replay acquires declared ordered responses and decodes detached
serialized records. Full polynomial coefficients are its readings;
there is no unproved finite-point interpolation or physical detector
claim. Integer sheets are not reduced modulo a unit-depth cutoff.

Source hashes bind local byte identity and public provenance. They are
not extra observer measurements. The [scope](SE43_SCOPE.md) separates
the written proofs, finite execution, inherited engine failure and
unperformed formal/external verification. Live navigation is updated
in the same commit; every older theorem and certificate stays unchanged.
