# PG1 validation record

Author: Monty. 1 November 2026.

This file separates text integrity, source interpretation and finite program
checks. It records local integration checks under Python 3.12. Hosted CI runs
against the resulting commit are separate evidence visible in GitHub Actions.
The packet does not certify full Sanskrit grammar or a new implementation.

## Integration inputs

- Canonical main: `3dd4ffa64ffb05e6d6033bf55cc2b3994a5421fc`.
- Theorem 78–80 branch head: `3da34662e7397843e20309a71c17e6cf103b8f56` (T80).
- Its preceding commits: `06f5bef869cb78b67f3d8e2fceae7746d445c3a9` (T79)
  and `67e416a59f7e032de167f442af569b8958bfe4ce` (T78 dependency).
- External text witness: `ashtadhyayi-com/data` at
  `5744762f010d677cfb43f347a42d02796cf615d6`.

The two conflicting navigation/workflow sections were reconciled by keeping
SP1 and T78–T80, then adding PG1. All three incoming theorem/code/test/pin
packets retain their original bytes. The operator engine, its source archive,
SP1 scientific sources and the quantum calculator are unchanged.

## Checks performed

| Check | Actual result | What it establishes |
|---|---|---|
| Compare every TSV row to the pinned publisher `a.p.n`, `i`, `s` fields | 3,983 of 3,983 exact matches | No missing, altered or invented root-text record in this edition's extraction |
| Catalogue structure | All 32 pādas; unique, ordered, contiguous identifiers; expected chapter counts | Internal text-inventory integrity |
| Foundation register against the catalogue | 120 selected Sanskrit texts match | Citation/quotation identity; not closure of all rule interpretations |
| External source files against SHA-256 manifest | All inspected files match | Reproducible electronic witness |
| `python3.12 research/panini_grammar/check_sources.py` | PASS | Catalogue and historical source integrity, offline and read-only |
| Temporary-copy negative controls for that checker | Altered Sanskrit text rejected; changed historical source rejected | The checks detect both a corpus change and an inherited-source change; originals were untouched |
| `proof_lab.test_shaiva_sources_nativized`, `proof_lab.test_shaiva_sources_varga_crystal`, `proof_lab.test_paninian_instruction_format` | **16 tests passed**, including all three frozen certificate digests | The imported finite computations reproduce their own recorded results |
| `proof_lab.test_mathematics_index`, `scripts.test_public_release_audit` | **15 tests passed** | Current navigation and audit behavior |
| `python3.12 scripts/public_release_audit.py` | PASS | Repository public-text audit |
| `python3.12 research/spanda_recognition/check_examples.py` | **13 controls** and dependency hashes passed | The preserved SP1 route still satisfies its direct finite contract after workflow integration |
| Local Markdown links in the PG1 packet | All resolve | Documentation navigation |
| Workflow selector executed on the actual staged Git tree | Selects SP1, PG1 and T78–T80 | Both formerly conflicting routes and the source inventory receive checks; unrelated engine/structure campaigns are not selected |
| `git diff --check` and staged equivalent | PASS | No whitespace/conflict-marker defect in the integration |

The 31 unit tests are 16 imported-packet checks plus 15 navigation/audit
checks. They are not 31 proofs of full Sanskrit correctness. The 13 SP1
controls belong to its separate cycle-memory model.

## Frozen computation pins

| Packet | Unchanged SHA-256 |
|---|---|
| T78 | `3d1ce14b679eb5c02e33473fb808ec4a192502b79d912b927a52240c94c58950` |
| T79 | `4440bf2f0e4f941ba8c7a1e83d7ed63a558c756efddd360a69fe5ef3ce3b37ca` |
| T80 | `8ac53de2a233fbe94d7d6f3f9e3806ade7bd2f68c759faba81882119ae87bccb` |

The TSV digest is
`70dfdfe6ba433b6e211f0f01b078c1b6d13a1ad0938e06fd5789298a04583634`.
This binds the text extraction, not its interpretation. No frozen expected
digest was rewritten to make a check pass.

## Evidence boundaries

The bhavati/bhavanti/rāmaḥ explanations and reading corrections are textual
research checked against the named primary passages. They are not outputs of
a newly implemented Sanskrit engine, independent specialist review, or Lean
verification. Full anuvṛtti/adhikāra closure, lexical completeness, accent,
Vedic domains, all exceptions and unrestricted parsing remain open.

No unchanged operator-engine campaign or older T58–T77 grammar suite was
rerun for this source/specification stage. PG1's conditional specialization
argument states the hypotheses that a later implementation must satisfy;
the existence of a full compatible grammar engine is not asserted.
