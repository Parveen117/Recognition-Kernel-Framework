# SE37 construction order and source record

12 October 2026. Owner: Monty.

Parent: `d2a5bdbd077bb2fad06068d24a47ed12ee2fbcc3`, branch
`agent/rh-source-energy-tail`; parent tree
`9278ffeffe97751c608c5f1a87ae2d43a01d12e0`.

The SE37 derivations were committed in
`e0cac19b8a9c60ddba7e20a680b5fccc00857145`. The parent holds the SE34,
SE35 and SE36 certificates.

| Source read | Use in this stage |
| --- | --- |
| SE33 response calculus | Polynomial response coefficients and finite expansion |
| SE34 unit memory | Retained unit quotients and compatible reduction between depths |
| SE35 active readings | Polynomial decoding on lawful readings, not arbitrary output tuples |
| SE36 action closure | The available action-word bank, the worked unit action and the polynomial response layer, imported unchanged |
| Canonical native_operator.cjs | Exact rational arithmetic |
| Canonical 01_NATIVE_ALGEBRA.md, N03--N05 | Minimum linear closure and the distinction between state observation and operator-algebra quotient |

The proof order is: the available bank and its relation ideal; polynomial
descent on the observation image; the least future-target algebra by
finite closure; calibration dependence after nonlinear compression; and
the uniform relative observer for the unit-scaled family.

The decoders take the recorded retained readings, relative reading and
calibration coordinate, and the supplied update and decoder polynomials.
They do not read the unknown source or the calibration state itself.
Symbolic identities are checked in Q[Lambda] before truncation where
the theorem states them so, and at the declared depth otherwise.

The source manifest inherits SE36's 144 pins. It adds that manifest,
the SE37 derivation and this stage's four non-manifest files: the
scope, this record, the application and its result archive. Its 150
hashes bind source, proof, code and readings. Navigation files and the
manifest itself remain outside the self-reference cycle.

Verification on this commit:

- `node proof_lab/lambda_target_algebra.cjs --check`: PASS, 22 checks,
  7 negative controls, archive byte-identical, 150 source pins.
- The SE33--SE36 replays are unchanged and pass.
- `python3.12 -m unittest proof_lab.test_mathematics_index -v`: all
  navigation tests pass.
- `node operator_foundation/verify_all.cjs --check`: the inherited
  first-suite pin mismatch in tests/verify.cjs --check recurs with the
  actual hash recorded in SE33. Later aggregate suites do not run. No
  pin is changed to claim a PASS.

No prior application certificate is revised. See [scope](SE37_SCOPE.md)
for the exact executed controls.
