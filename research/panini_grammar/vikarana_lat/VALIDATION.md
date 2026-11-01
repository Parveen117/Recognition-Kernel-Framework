# PG5 — Validation record

Author: Monty. 1 November 2026.

The implementation begins at review-branch commit
`bedbd93d6513bfd1747164527640fbce130082bb`. The source checkout is pinned at
`5744762f010d677cfb43f347a42d02796cf615d6`. No predecessor certificate has been
regenerated and no historical source pin has been changed.

The direct PG5 verifier checks:

- 39 source-bound records and the 7.1.3 commentary split;
- 40 literal-commentary word cases, 25 selection cases and 22 expected refusals;
- 44 structural/history controls, including same-surface affix distinctions,
  the actual guṇa trigger, missing exception-record refusal, luk/ślu, ṭer e
  before the edhe seam, optional branches, separate ṇic/aṅga targets, and
  immutable late readout;
- 304 literal citation anchors (255 unique), seven external file hashes, and
  17 unchanged predecessor file hashes;
- all 162 person-number cells of 18 admitted pada paradigms, comprising 198
  branches, against the pinned Vidyut output; zero differences on this domain.

```sh
python3.12 research/panini_grammar/vikarana_lat/verify.py \
  --source-root /workspace/scratch/d4fa9af152dc/panini-primary-data
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The first command reproduces `VERIFICATION_RESULT.json` without writing.
Only the new PG5 report is produced during development with `--write`.
The navigation test is required by `AGENTS.md`; the operator-wide suite is
not relevant because the operator engine is unchanged. CI/main merge and
frozen predecessor-suite replay remain deferred.

The CLI was checked on the complete tud P paradigm and a requested hu word:
tud returns all nine forms; hu exits unresolved with its remaining word-path
obligation. Agreement with Vidyut is recorded separately from the traditional
word witnesses, and does not certify all Sanskrit or all gaṇa members.
