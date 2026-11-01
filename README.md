# Recognition Kernel Framework

Research software and a source-pinned theorem archive for typed cuts, operator
composition, observer completion, retained memory and recognition.

**Author:** Monty Dabas · **Canonical branch:** `main` · **Operator engine:** v0.5

<!-- patent-status-notice:start -->
> **Patent pending — rights reserved.** The repository owner confirms filed PCT and/or provisional patent applications in the related invention portfolio. This notice applies to subject matter supported by the applicable pending filings. Public disclosure is not intended to waive patent rights. Existing licences and permissions remain effective. See [PATENT_NOTICE.md](PATENT_NOTICE.md).
<!-- patent-status-notice:end -->

## Start here

| Goal | Entry point |
|---|---|
| Use the executable operator engine | [Operator Workbench](operator_foundation/README.md) |
| Find a theorem and its hypotheses | [Mathematics Index](MATHEMATICS_INDEX.md) |
| Review Sanskrit grammar before implementation | [PG1: Pāṇini grammar foundation](research/panini_grammar/README.md) |
| Verify a package | [Verification guide](VERIFY.md) |
| Review evidence and open obligations | [Certificate Index](CERTIFICATE_INDEX.md) · [Claim Boundary](CLAIM_BOUNDARY.md) |
| Develop or report a problem | [Contribution guide](CONTRIBUTING.md) |

## Quick start

Use **Node 22.16.0** for the archived engine evidence and **Python 3.12** for the
navigation and current finite-contract checks. The engine uses built-in Node
modules; no package installation or other repository checkout is required.

```bash
git clone https://github.com/Parveen117/Recognition-Kernel-Framework.git
cd Recognition-Kernel-Framework
node operator_foundation/verify_all.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
```

The exact Node version is recorded in `.node-version`. The historical Laurent
certificate hashes the runtime version, so another Node version can fail that
archive comparison. Use the recorded runtime; keep the expected hashes intact.

To solve a supplied finite operator job:

```bash
node operator_foundation/cli.cjs solve operator_foundation/examples/emk_job.json emk-result.json
```

See the [verification guide](VERIFY.md) for package-specific commands, expected
scope and the distinction between routine CI and historical campaign replay.

## Repository map

| Location | Role |
|---|---|
| [`operator_foundation/`](operator_foundation/README.md) | Single active operator engine: exact cut arithmetic, paths, Laurent/jet modules, Pāṇinian compilation, regular models and weighted completion. |
| [`research/`](research/) | Additive research packets: [R1/R2 returns](research/recognition_return/README.md), [R3/R4 structure and repair](research/structure_report/README.md), [lambda counting](research/lambda_counting/README.md), [SS1 signals](research/sectoral_signal/README.md), [SP1 cycle memory](research/spanda_recognition/README.md), and [PG1 Sanskrit grammar](research/panini_grammar/README.md). |
| [`papers/rkf_completed_weil_endpoint/`](papers/rkf_completed_weil_endpoint/README.md) | Endpoint paper and source-energy development through SE49, with dated scopes and corrections. |
| [`theorum/`](theorum/README.md) · [`theorems/foundation/`](theorems/foundation/) | T01–T80, parallel theorem families and foundation capsules. Existing source paths are preserved. |
| [`proof_lab/`](proof_lab/) · [`certificates/`](CERTIFICATE_INDEX.md) | Implementations, finite checks, immutable evidence and reproducibility contracts. |
| [`objects/`](objects/README.md) · [`lean/`](lean/README.md) | Native-object audit packets and selected formal witnesses. |
| [`research-history/`](research-history/) | Dated integration records and the [recoverable branch archive](research-history/BRANCH_ARCHIVE_2026_11_01.json). |

The full earlier register is preserved in
[MATHEMATICS_INDEX_2026_09_16.md](MATHEMATICS_INDEX_2026_09_16.md). The framework
overview remains in [README_FRAMEWORK.md](README_FRAMEWORK.md). The corrected
public source tree in `operator_foundation/sources/rkf_reference` is immutable
provenance; shared engine development belongs in `operator_foundation/`.

## Current evidence and scope

The [1 November integration](research-history/PENDING_WORK_2026_11_01.md)
reconciled six pending histories with 60 distinct commits. Its verified tree
passed 65 selected Python tests, the unchanged engine's 557 finite checks and
13 mutation controls, and the imported R3/R4 and SS1 checks. The
[hosted run](https://github.com/Parveen117/Recognition-Kernel-Framework/actions/runs/41280379016)
records that execution. These are dated results, not a substitute for checking
the revision being used.

General proofs, finite computation, source integrity, formal witnesses and
external review remain separate evidence classes. SE49's archived eta-zero
result applies to the finite span V_24. Global eta-zero positivity, K0, RH and
the Yang–Mills mass gap remain open. Each theorem or packet controls its own
assumptions and conclusion.

## Working model and provenance

`main` is the one long-lived branch. Topic branches are temporary and are
removed after their commits are verified in `main`. The 30 merged branch
references from the November cleanup are recorded with their commit IDs in the
[branch archive](research-history/BRANCH_ARCHIVE_2026_11_01.json); their history
remains reachable. See the [cleanup record](research-history/REPOSITORY_CLEANUP_2026_11_01.md)
for recovery and maintenance details.

Use [CITATION.cff](CITATION.cff) and the exact commit or release when citing this
work. [Research provenance](RESEARCH_PROVENANCE.md),
[governance](GOVERNANCE.md), [public review terms](NOTICE.md) and
[patent notice](PATENT_NOTICE.md) describe attribution, ownership and scope.
