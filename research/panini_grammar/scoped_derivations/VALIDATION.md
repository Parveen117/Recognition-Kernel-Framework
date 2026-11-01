# PG4 — Actual validation

Author: Monty. 1 November 2026.

Baseline: `b9e17f47f6c96e0c39f7f733698efe5becd2f477`.
Primary source: `5744762f010d677cfb43f347a42d02796cf615d6`.

## Direct checks

```sh
python3.12 research/panini_grammar/scoped_derivations/verify.py --source-root /path/to/ashtadhyayi-data
```

- Verified seven external SHA-256 source pins and eleven unchanged historical
  dependencies; no earlier packet or certificate was regenerated.
- Checked **167 literal citation occurrences**, comprising **125 distinct
  file/key/anchor records**, plus 34 lexical teaching-form identities.
- Parsed 3,983 annotated sūtra records, 23,589 inherited-term edges and 9,653
  padaccheda entries. Applied seven source policies to 347 edges. Preserved
  all unknown fields and the one nonstandard annotation layout.
- Bound **19 reviewed rule records** to their effective source frames. This
  includes reused operations, review-only records and the śap candidate gate;
  it is not a count of fully completed sūtras.
- Reproduced **71 local cases**: 26 roots, 13 tuk junctions, 19 phonetic
  contexts, nine length/visibility contexts and four śap candidate contexts.
  All expected outcomes agree. **Eleven** deliberately remain unresolved or
  partial; matching that expected boundary does not solve the missing case.
- Reproduced **52 source/structural controls**, including scope endpoints,
  term splitting, corrected-reference provenance, missing-inheritance failure,
  case-role mismatches, lexical-identity requirements, vowel-owned tuk,
  early-num contact blocking, immutable readouts and headword independence.
- Compared all 2,259 Dhātupāṭha records: 2,229 roots and 30 separate directives.
  **2,219** root query spellings agree with the source headword, **eight**
  differ, and **two** teaching conventions remain unresolved. The new stage
  adds 138 agreements over PG3 with no lost agreements on this witness.
- Recorded actual applications: 34 conditioned dental restorations, ten short
  and three long tuk insertions, 19 root-upadhā lengthenings, 364 anusvāra
  operations, 18 palatal and three retroflex contact operations, four voicing
  operations and 318 parasavarṇa operations. Application counts are not
  independent proof or sūtra-coverage counts.
- Reproduced the checked-in [VERIFICATION_RESULT.json](VERIFICATION_RESULT.json).

## Repository checks, counted separately

```sh
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The required navigation module passed **8 tests**. New local Markdown targets
and `git diff --check` passed. These checks add no linguistic coverage.

CI, predecessor test/certificate campaigns and operator-engine suites were not
run. Main was not updated or merged. The review commit uses `[skip ci]` and
continues the existing grammar review branch.

Expected local outcomes were authored from the documented reading. They have
not received independent specialist review. The source has provisional
lexical/teaching annotations; the complete remaining difference ledger is
preserved. Universal soundness, completeness and calculator integration remain
unclaimed.
