# SS1 validation record

Date: 12 October 2026.

The new finite packet has 24 exact checks, including 8 counterexample
controls. It imports the unchanged rational cut-scalar engine; it is an
application packet, not a second operator implementation.

Executed gates:

| Gate | Runtime | Result |
|---|---|---|
| `node research/sectoral_signal/verify.cjs --write` | Node v24.19.0 | PASS, initial evidence creation |
| `node research/sectoral_signal/verify.cjs --check` | Node v24.19.0 | PASS, 24 checks including 8 negative controls |
| `python -m unittest proof_lab.test_mathematics_index -v` | Python 3.12.14 | PASS, 8 navigation checks |
| `node operator_foundation/verify_all.cjs --check` | Node v24.19.0 | FAIL at existing `tests/verify.cjs` pin mismatch |

The engine failure is the inherited mismatch already recorded in SE23:
actual `35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`,
expected `f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`.
The engine and its pins were not edited. Later suites in the master command
were not reached, so no whole-engine PASS is claimed.

SS1 result SHA256:
`d1f49050727c9be2fd34c2826ae1e11970e8338128e392c3195951520119cb1d`.

Written proofs, finite computation, formal verification and external review
are distinct. There is no physical experiment or new RH eta certificate.
