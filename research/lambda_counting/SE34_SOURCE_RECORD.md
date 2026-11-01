# SE34 construction order and source record

12 October 2026. Owner: Monty.

Parent: `e0cac19b8a9c60ddba7e20a680b5fccc00857145`, branch
`agent/rh-source-energy-tail`; parent tree
`2609825d861cac19ec5d4052dde00c296a5e6fe5`.

The SE34 derivations were committed in
`df6a70d1a77177fcc83c133c9d18bf5d01895069`. The SE35 certificate
(`c342cb77c0a33de74f45b1b92f398332b591ffe2`) pins that text unchanged.
The parent adds the SE37 development draft, which this certificate
neither uses nor certifies. This record adds the observer certificate
for SE34 after SE35, so its manifest inherits SE35's.

| Source read | Use in this stage |
| --- | --- |
| SE32 reading calculus | Finite-output linear actions, coefficient cuts and locally finite geometric inversion |
| SE33 joint and nonlinear calculus | Joint banks, the bank reader, response coefficients and the fixed-order inverse used as a comparison control |
| SE35 bank construction | Symmetric banks from declared polynomial terms, their evaluation and linear frame transport, imported unchanged |
| Canonical native_operator.cjs | Exact rational cut arithmetic |
| Canonical AUTOMATIC_REGULAR_MODEL.md, WB1 | Finite acyclic graph ordering in a different target |
| Canonical NATIVE_LAURENT_JET_REPAIR.md | Formal unit towers and retained jet memory |
| Canonical WEIGHTED_OPERATOR_COMPLETION.md, WC7 | Analytic contraction in its own setting, a comparison source |
| research/recognition_return RR1--RR2 and r2 | The quadratic return recurrence and coefficientwise uniqueness |

The proof order is: locally polynomial operations on finite sectors and
the unit-memory tower; dependency order; weighted feedback cycles; the
supplied cut inverse and its lift; residual decoding and order doubling;
and frame transport.

The decoders read the dependency graph and its unit weights directly from
the saved banks of F. Every retained operation is cut to the declared
unit depth. The cut inverse is checked at the target cut and is never
constructed by the decoder.

The source manifest inherits SE35's 130 pins. It adds that manifest,
the canonical WB1 source, the two recognition-return theorem sources
and this stage's four non-manifest files: the scope, this record, the
application and its result archive. The SE34 derivation is already pinned.
Its 138 hashes bind source, proof, code and readings. Navigation files and
the manifest itself remain outside the self-reference cycle.

Verification on this commit:

- `node proof_lab/lambda_unit_memory_lifting.cjs --check`: PASS,
  29 checks, 11 negative controls, archive byte-identical, 138 source pins.
- The SE33 and SE35 replays are unchanged and pass.
- `python3.12 -m unittest proof_lab.test_mathematics_index -v`: all
  navigation tests pass.
- `node operator_foundation/verify_all.cjs --check`: the inherited
  first-suite pin mismatch in tests/verify.cjs --check recurs with the
  actual hash recorded in SE33 and SE35. Later aggregate suites do not
  run. No pin is changed to claim a PASS.

No prior application certificate is revised. See [scope](SE34_SCOPE.md)
for the exact executed controls.
