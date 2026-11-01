# SE1 validation record

Date: 2026-10-11. Local Python: 3.12.14. Local Node: v24.19.0.

| Check | Observed result |
| --- | --- |
| `python -m unittest proof_lab.test_endpoint_shared_energy_budget -v` | PASS, 16 finite controls |
| `python -m unittest proof_lab.test_mathematics_index -v` | PASS, 8 navigation checks |
| `python -m proof_lab.endpoint_shared_energy_budget --check` | PASS, exact rational profile accumulation; source attachment OPEN |
| Added/edited paper and index local links | PASS, 51 links resolve |
| `git diff --check` | PASS |
| Original theorem files, preserved register and operator engine | Unchanged |
| `node operator_foundation/verify_all.cjs --check` on Node v24.19.0 | FAIL at the first finite-certificate hash comparison |
| Same full engine check on documented Node v22.16.0 | Not run locally; runtime unavailable |
| All historical Python scientific suites / Lean / Arb regeneration | Not run |

The observed engine hash is
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`;
the expected historical hash is
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`.
`operator_foundation/tests/verify.cjs` includes `process.version` in
the hashed report. Thus the local runtime differs from the documented
certificate runtime. The finite assertions preceding this comparison
completed; the full master verification did not complete.

No historical certificate, expected hash, or engine source was rewritten.
The dedicated [workflow](../../../.github/workflows/endpoint-shared-energy.yml)
uses Node 22.16.0 and Python 3.12 for a read-only replay. Configuring that
workflow is not a claim that remote CI has passed.

The mathematical scope is in the [SE1 note](SE1_SHARED_ENERGY_BUDGET.md)
and [paper claim boundary](../CLAIM_BOUNDARY.md).
