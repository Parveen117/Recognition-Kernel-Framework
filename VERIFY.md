# Verification guide

Run commands from the repository root. Use **Node 22.16.0** (`.node-version`)
and **Python 3.12**. These commands check existing evidence without
overwriting its expected hashes.

## Choose the affected surface

| Change or review target | Command |
|---|---|
| Mathematics navigation | `python -m unittest proof_lab.test_mathematics_index -v` |
| Public-release text | `python -m unittest scripts.test_public_release_audit -v` and `python scripts/public_release_audit.py` |
| Canonical operator engine | `node operator_foundation/verify_all.cjs --check` |
| MR-04–MR-07 memory contracts | `python -m unittest proof_lab.test_morphic_memory proof_lab.test_guarded_lopa proof_lab.test_holonomy_scaling proof_lab.test_memory_certificate -v` |
| Archived MR-04–MR-07 evidence | `python -m proof_lab.morphic_recognition.certify_memory --check-archive` |
| R3 structure report | `node research/structure_report/verify.cjs --check` and `node research/structure_report/mutate.cjs` |
| R4 declared-pairing repair | `node research/structure_report/r4/verify.cjs --check` and `node research/structure_report/r4/mutate.cjs` |
| SS1 sectoral signals | `node research/sectoral_signal/verify.cjs --check` |
| SP1 cycle-memory examples and dependencies | `python research/spanda_recognition/check_examples.py` |
| Historical November integration snapshot | `python scripts/verify_pending_integration.py` |

The integration audit checks the recorded snapshot's ancestry and source bytes.
It does not require its old branch references to remain present. Future changes
to a snapshotted packet may legitimately require a new dated integration record;
do not turn this historical audit into a universal test for all future versions.

For other packages, use the command and runtime in their README, scope record
or certificate specification. The foundation cartridge has its own
[reproduction guide](REPRODUCE.md). Full archive test discovery and numerical
campaigns are separate from these bounded checks.

## Routine GitHub Actions

[Repository checks](.github/workflows/repository-checks.yml) always checks the
mathematics navigation and public-release text. It selects existing engine,
memory, structure, SS1 and SP1 checks from the changed paths. SP1 also follows
its declared dependency pins. A manual invocation runs those bounded checks
together. Its token has read-only repository permission.

The older [proof-lab campaign](.github/workflows/rkf-proof-lab-ci.yml) is
manual, so a README edit does not rerun all historical scientific certificates.
The foundation review and MR-01–MR-03 workflows run automatically only when
their own inputs change. Other historical workflows retain their package
scope and manual entry points.

## Interpret the result

A source hash mismatch, failed obligation or missing runtime must be reported
as such. In particular, the frozen Laurent evidence includes `process.version`;
use Node 22.16.0 rather than replacing its expected hash to fit another runtime.

Finite PASS, a written general proof, a Lean witness, source provenance and
independent review are distinct. See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md) and
the exact packet's hypotheses before stating what a check establishes.
