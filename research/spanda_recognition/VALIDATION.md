# SP1 validation record

Author: Monty. 1 November 2026.

Written proofs, direct finite examples and source integrity are separate.
The proof is not formalized and no external review is claimed.

Executed locally with Python **3.12.14**:

| Check | Actual result |
|---|---|
| `python3.12 research/spanda_recognition/check_examples.py` | 13 finite mathematical controls passed; all 6 predecessor hashes matched. |
| `python3.12 -m unittest proof_lab.test_mathematics_index scripts.test_public_release_audit -v` | 15 tests passed: 8 navigation checks and 7 existing audit regressions. |
| `python3.12 scripts/public_release_audit.py` | `PASS_PUBLIC_RELEASE_AUDIT`. |
| Workflow selection, executed with controlled changed-path/event inputs | 7 cases passed: README, SP1 packet, pinned predecessor, workflow change, engine change, manual invocation and this actual diff. This diff selects only SP1 beyond the always-on checks. |
| Changed Markdown links and `git diff --check` | Local targets resolve; no whitespace errors. |

The exact controls compare ordered composition with sequential evaluation,
exercise cancellation and non-reset counterexamples, check the affine frame
sign, retain the complete six-coordinate jet and its zero-specialization,
decode the count from a future reading, and reject nilpotent division and
dropping the rational-scalar hypothesis. They are declared rational-coordinate
fixtures, not physical measurements or a universal theorem certificate.

Routine [repository CI](../../.github/workflows/repository-checks.yml) now
selects the SP1 checker when this packet, its pinned dependencies or the
selection workflow change. No archived engine or predecessor scientific
campaign was rerun for this packet. The shared engine, historical evidence,
preserved register and patent notices are unchanged. Hosted CI evidence is
recorded by the workflow run for the integrated commit, separately from these
local results.
