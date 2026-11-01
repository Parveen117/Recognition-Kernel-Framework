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

## Sanskrit register and first calculator application

The [Sanskrit passage register](SANSKRIT_PASSAGES.md) was checked against the
linked source texts on 1 November 2026. It retains passage identifiers,
Devanagari, IAST, attribution qualifications and our own short glosses.
It is not a critical edition or an assertion that those texts contain SP1's
modern equations. The addition passed the navigation/public audit checks and
[hosted repository CI](https://github.com/Parveen117/Recognition-Kernel-Framework/actions/runs/41294282656).

The quantum calculator's first source-derived attachment was integrated by
[PR #10](https://github.com/Parveen117/quantum-classical-provisional/pull/10),
head `7563a59f4c38de15be6841d7ee552ad95cf6755a`, merge
`68c900d58347ed1f308e0901b631cc997645f16d`. The merge tree equals the tested
head tree. Its [application note](https://github.com/Parveen117/quantum-classical-provisional/blob/7563a59f4c38de15be6841d7ee552ad95cf6755a/native_relational_qc/OBSERVER_CYCLE.md)
derives H and b from the existing convex qubit source rather than attaching a
free affine law. The source has a physical fixed point and zero obstruction;
the retained software protocol count is separately declared.

| Calculator check | Actual result |
|---|---|
| Local observer-cycle and observer-state tests, Python 3.12.14 | 17 passed, 2 optional Qiskit checks skipped locally. |
| PR CI, Python 3.11 core | 1,092 passed, 57 skipped; 334 subtests passed. |
| PR CI, Python 3.12 core | 1,092 passed, 57 skipped; 334 subtests passed. |
| PR CI, Python 3.12 with Qiskit and benchmark extras | 1,140 passed, 9 skipped; 342 subtests passed. |
| Wheel, installed command, ledger verification and certificate export | Passed in all three CI environments. |

[PR CI evidence](https://github.com/Parveen117/quantum-classical-provisional/actions/runs/41294309150)
includes the independent Kraus-channel and fixed-point comparison. Exact
controls also show a detector reading returning while the source differs,
one-step future detection, a permanently blind fixed analyzer, correct frame
transport, and source return with a retained classical count. These are
model calculations, not acquired quantum measurements or hardware timing.
