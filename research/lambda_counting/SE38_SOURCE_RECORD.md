# SE38 construction order and source record

12 October 2026. Owner: Monty.

Parent: `a1ee0d0fa7154c2dc513892b27f9ea4f1e229dc3`, branch
`agent/rh-source-energy-tail`; parent tree
`4f513351d73e4b08f420877cd119329879dacd97`.

The parent commit holds the SE38 derivations. This record adds the
observer certificate for them.

| Source read | Use in this stage |
| --- | --- |
| SE30, section 3 | Typed coefficient cuts and marked retained targets |
| SE31, sections 3--4 | Labelled unit-memory readings and ordered actions |
| SE32, section 4 | Retained coefficient carriers and lawful descent |
| SE33 | Finite polynomial response and joint-increment expansion |
| SE34 | Unit-order propagation through polynomial operations |
| SE36 | Affine-cut polynomial action catalogues; its polynomial response layer is imported unchanged |
| SE37 | The relative calibration equation and the cubic counterexample repaired here |
| Canonical native_operator.cjs | Exact rational arithmetic |

The proof order is: the monomial calibration algebra and its expression
rule; the degree/unit-order criterion and the closed observer; the least
bank for a monomial action; the induced cut of the memory algebra; and
the calibration depth from labelled unit readings.

The bank decoder evaluates formulas derived from the supplied catalogue
on the recorded calibration readings and relative reading; the depth
decoder shifts the recorded labelled packet to its shallower carrier and
uses the lift-independent update. Neither reads the source or the
calibration state itself.

The source manifest inherits SE37's 150 pins. It adds that manifest,
the SE38 derivation and this stage's four non-manifest files: the
scope, this record, the application and its result archive. The SE30,
SE31 and SE32 sources are already pinned. Its 156 hashes bind source,
proof, code and readings. Navigation files and the manifest itself
remain outside the self-reference cycle.

Verification on this commit:

- `node proof_lab/lambda_calibration_depth.cjs --check`: PASS, 25 checks,
  8 negative controls, archive byte-identical, 156 source pins.
- The SE33--SE37 replays are unchanged and pass.
- `python3.12 -m unittest proof_lab.test_mathematics_index -v`: all
  navigation tests pass.
- `node operator_foundation/verify_all.cjs --check`: the inherited
  first-suite pin mismatch in tests/verify.cjs --check recurs with the
  actual hash recorded in SE33. Later aggregate suites do not run. No
  pin is changed to claim a PASS.

No prior application certificate is revised. See [scope](SE38_SCOPE.md)
for the exact executed controls.
