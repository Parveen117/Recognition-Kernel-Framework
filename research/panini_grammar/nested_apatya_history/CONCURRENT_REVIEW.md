# PG48 — Concurrent T153/T154 review, without replay

Author: Monty. 4 November 2026.

The companion branch `shaiva-sources-maheshvara-spanda-pratyabhijna` advanced
from the previously checked T152 head to
`e492ae69c514e5013d0f0a6e0c61f36e74ada22f` before PG48 publication.
The three intervening commits add T153, T154 and the retained wiring script.
The two theorem documents and their two certificate modules were read in full;
their expected-hash files were read, and the ledger identity was re-pinned.
All seven immutable file identities are in [SOURCE_PINS.json](SOURCE_PINS.json).
No companion module, generator or certificate was executed for this review.

## CR1. Reported results and their limits

|Companion material|Result reported by that document|PG48 interpretation|
|---|---|---|
|[T153](https://github.com/Parveen117/Recognition-Kernel-Framework/blob/e492ae69c514e5013d0f0a6e0c61f36e74ada22f/theorum/153_krdanta_declension_theorem.md)|50,265 agreements out of 51,326 kṛdanta declension cells; 196 differences inherited from the kṛt residue and 865 classified as generator ṅīp 7s/6p residue|An attributed finite-lane report, not a result reproduced here or a certificate for the present taddhita history|
|[T154](https://github.com/Parveen117/Recognition-Kernel-Framework/blob/e492ae69c514e5013d0f0a6e0c61f36e74ada22f/theorum/154_written_construction_replay_theorem.md)|1,124 reference cases; 648 replayed, 604 agreeing, 43 classified as other optional branches and one left to adjudicate|The replayed subset and its classifications must remain visible; the reported candidate status does not mean every written form agrees|

T153 composes the verbal, kṛt and nominal tables, with feminine formation and
selected stem flags passed across the boundaries. Its source document leaves
the residual kṛt cases, neuter tṛc, feminine ṇvul lane and other stated limits
open. The large independent lane and every dependency were not independently
audited here. Its expected-certificate hash file contains
`bbea4a11f9700ac3d1b5781650eb841b38e91f6ed8402b29f0b8b23d15f0db89`.

T154 describes its reported snapshot as PG1–PG18. Its expected-certificate hash file contains
`8824583c49310c4b768dd874901462ee16d0beca61e6b8bfe0525ccf1bd8aa4f`.
Reading those hash strings is not recomputing either certificate.

## CR2. Actual code scope and candidate status

Read-only inspection of
[pg_replay.py](https://github.com/Parveen117/Recognition-Kernel-Framework/blob/e492ae69c514e5013d0f0a6e0c61f36e74ada22f/proof_lab/pg_replay.py)
shows that form discovery selects directories containing `REFERENCE_CASES.json`.
It reads lexical entries and IAST expectations from the corresponding legacy
files, selects `derive`/`attested_member` cases, and calls the verbal table for
supported requests. It does not consume PG48's `HISTORY_REGISTER.json`, its
fourteen written stages, nested owner records or six consumer controls.
The separate rule scan reads `RULE_RECORDS.json`; it does not scan the full
modern written-ID unions or every archived commentary field.

`PASS_PG_REPLAY_CANDIDATE` requires a nonempty replay and the scanned rule
ID/text checks. The code does **not** require zero disagreements. Its
`OPTIONS` classification is keyed by lexical ID: a mismatch for a listed
lexical ID receives the associated optional-rule label, without a separate
case-specific derivation check inside that classifier. Thus the reported
43 branch classifications are retained as the companion's account, not
independently established here as 43 source-adjudicated equivalences.
Nor does a shared root alone prove that a difference must be a missing rule;
admission, policy, scheduling and implementation also require review.

Read-only inspection of
[krdanta_sup.py](https://github.com/Parveen117/Recognition-Kernel-Framework/blob/e492ae69c514e5013d0f0a6e0c61f36e74ada22f/proof_lab/krdanta_sup.py)
shows that its candidate status requires a nonempty lane, no disagreement
outside the two declared residue classes, and the declared feminine-row
load-bearing check. It does not require zero lane differences; 7.3.44 is
explicitly exempted as vacuous on that lane. This is a boundary reading of
the code, not independent semantic validation of those classifications.

## CR3. Pending form adjudication and coverage separation

T154 leaves **kṣiṇoti** in the PG12 written line versus **kṣeṇoti** in the
tables unresolved. It discusses the table's 3.1.79 / 3.4.114 / 7.3.86 route
and reports both forms in the generator. A later bounded source review must
fix the lexical entry, suffix/status conditions, readings and selection
policy before deciding whether either path needs correction. PG48 changes
neither form and claims no adjudication of that case.

The same report places 161 scanned rule IDs as 106 table rows, 35 ledger
entries and 20 in neither operative category. Those 20 are **companion
operational coverage gaps** in that scan, not missing IDs in PG48's two
3,983-member written unions. T154 also reports 115 undeclared-root cases
across 32 roots. In total 476 of the 1,124 cases were not replayed, including
refusal/selection contracts and other exclusions; these are distinct from the
replayed form comparisons. These categories cannot be added to PG48's
new-position or new-rule counts.

## CR4. Handoff

Retain the nested owner, source-policy and consumer-view requirements in
[HANDOFF_AND_FRONTIER.md](HANDOFF_AND_FRONTIER.md). A future adapter would
need to represent those records and their explicit Open/Blocked/Applied
outcomes before a runtime result could cover H01 or C01–C06. T154's existing
legacy-file scan supplies no such coverage merely because PG48 is present.
The written next frontier remains the source-qualified हस्तिशिरस्/शीर्ष
history. The kṣiṇoti/kṣeṇoti difference is a separate pending adjudication.
Grammar tests, generators and certificate replay remain deferred here.
