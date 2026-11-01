# PG6 — Validation record

Author: Monty. 1 November 2026.

Baseline review-branch commit: `35e124fdb33b14e8fb59b3f8887b40283f32a6aa`.
Primary data commit: `5744762f010d677cfb43f347a42d02796cf615d6`.

The direct changed-claim checks record:

- 17 new source-bound records and three explicit local scope decisions;
- 53 literal traditional word cases and eight expected refusals;
- 54 direct controls covering inherited conditions, distinct guṇa triggers,
  cluster-sensitive junctions, optional/mandatory loss, śnā/tiṅ ordering,
  specific visibility queries, late nasal feedback, and four PG5 routing checks;
- 152 literal source anchors (142 unique), seven external hashes, and
  26 unchanged predecessor hashes;
- 153 cells across 17 new pada paradigms: 167 branches and zero differences
  from the pinned Vidyut output on this domain.

```sh
python3.12 research/panini_grammar/non_thematic_lat/verify.py \
  --source-root /workspace/scratch/d4fa9af152dc/panini-primary-data
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The verifier reproduces `VERIFICATION_RESULT.json` without writing. Only this
new stage's report is created during development with `--write`. The required
navigation check contains eight tests. The CLI is checked on the su P paradigm,
including both u-loss options, and on a non-admitted kṛ-in-hiṃsā word path.

An initial literal-anchor check caught a mismatch between the stored single
daṇḍa and the source's double daṇḍa in the 6.4.108 citation. Only the new
anchor was corrected; no source text or old pin was changed.

No frozen certificate or untouched predecessor suite is replayed. The four
old-form controls check dispatch through the changed adapter only. The
operator engine, calculator, CI and main merge are outside this stage.
Software comparison and source-attested cases remain distinct evidence grades.
