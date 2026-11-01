# SE36 construction order and source record

12 October 2026. Owner: Monty.

Parent: `53244f288043f3943cc5689e2419202ba779e8c9`, branch
`agent/rh-source-energy-tail`; parent tree
`08a06890bf9f77f4d14c262c8a18092b51218613`.

The SE36 derivations were committed in
`4f56c47cdd09f757cd8c92646feccd734d89ca5a`. The parent holds the SE34
and SE35 certificates and the SE37 development draft, which this
certificate neither uses nor certifies.

| Source read | Use in this stage |
| --- | --- |
| SE33 multilinear and response calculus | Polynomial descriptions and finite coefficient response |
| SE34 unit-memory completion | Typed retained quotients |
| SE35 active readings | Full-translation comparison; its bank construction and blind-subspace calculation are imported unchanged |
| Canonical native_operator.cjs | Exact rational arithmetic |
| Canonical 01_NATIVE_ALGEBRA.md, N03 | Invariant response-space closure and minimum linear refinement |
| Canonical AUTOMATIC_REGULAR_MODEL.md, WB4 | An explicit action catalogue for future-complete observation |
| Canonical NATIVE_PRIMITIVE_ORDER.md | Counting carriers, lawful composition and calibrated targets before interpretations |

The proof order is: the restricted signature and its fibres; closure of
the response span under the affine catalogue, with witness words; the
separating-word corollary; translations synthesized by available
reversible actions; finite closure at fixed unit depth for nonlinear
actions with affine cut; and the moving-observer update.

The application keeps a witness word with every retained response
function. Its decoders consume the recorded protocol readings and the
descended matrices, and compare their predictions with recorded future
readings. The polynomial response layer is exported for the SE37
certificate.

The source manifest inherits SE34's 138 pins. It adds that manifest,
the SE36 derivation and this stage's four non-manifest files: the
scope, this record, the application and its result archive. Its 144
hashes bind source, proof, code and readings. Navigation files and the
manifest itself remain outside the self-reference cycle.

Verification on this commit:

- `node proof_lab/lambda_action_closure.cjs --check`: PASS, 30 checks,
  9 negative controls, archive byte-identical, 144 source pins.
- The SE33, SE34 and SE35 replays are unchanged and pass.
- `python3.12 -m unittest proof_lab.test_mathematics_index -v`: all
  navigation tests pass.
- `node operator_foundation/verify_all.cjs --check`: the inherited
  first-suite pin mismatch in tests/verify.cjs --check recurs with the
  actual hash recorded in SE33. Later aggregate suites do not run. No
  pin is changed to claim a PASS.

No prior application certificate is revised. See [scope](SE36_SCOPE.md)
for the exact executed controls.
