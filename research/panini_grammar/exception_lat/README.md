# PG8 — Bhuj senses, nested im, and the first adādi paths

Author: Monty. 1 November 2026.

PG8 adds four identified roots and five sense/pada profiles to the present
generator: **45 person-number cells, 45 branches**. Bhuj and tṛh close the two
lexical exclusions in PG7's particular class-7 profile; ad and as begin class 2.
Prefixes, other lakāras and the full grammar of either gaṇa remain open.

| Root and declared meaning | Example | Derivational change |
| --- | --- | --- |
| भुजँ, पालने | भुनक्ति / भुञ्जन्ति | The protection sense does not satisfy 1.3.66's anavana condition; contextual P license is supplied |
| भुजँ, अभ्यवहारे | भुङ्क्ते / भुञ्जाते | 1.3.66 prescribes A for the admitted eating sense; the original lexicon's P label remains unchanged |
| तृहँ, हिंसायाम् | तृणेढि / तृण्ढः / तृंहन्ति | im belongs to the root-with-śnam host; a local visibility permission admits ṣṭutva to the ḍh-lopa query |
| अदँ, भक्षणे | अत्ति / अदन्ति | śap-luk is retained as whole-affix deletion; ordinary consonant readout completes these paths |
| असँ, भुवि | अस्ति / सन्ति / असि | Weak root-a deletion under 6.4.111 and separate root-s deletion before s under 7.4.50 |

The generator reads teaching forms, lexical identities and rule records. It
does not read expected output forms or a conjugation table. The new im unit is
a **typed augment**, not a pratyaya; its m-it remains in history. The source
root stays a single morpheme despite the interleaved surface layout.

## Use

From the repository root, with the pinned ashtadhyayi-com/data checkout:

```sh
python3.12 -m research.panini_grammar.exception_lat.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1070017 --sense अभ्यवहारे --pada A --pada-licensed --all-forms
```

Use `--trace` to inspect original sounds, markers, owned replacements,
deletions and query-relative visibility. Supply `पालने` with P for the other
bhuj profile. Its combined dictionary meaning `पालनाभ्यवहारयोः` is deliberately
unresolved until a meaning is selected. A supplied pada license does not
override that semantic restriction. Other PG5–PG7 paths remain available.

## Evidence and coverage

[Verification](VERIFICATION_RESULT.json) records **29 literal commentary
word witnesses, 16 expected refusals, 53 direct controls and 80 citation
anchors**. All 45 new cells separately agree with the pinned Vidyut output.
This is agreement with another implementation, not a Sanskrit validity oracle.

The [coverage record](COVERAGE_STATUS.json) now has **50 / 2,229 root entries,
648 laṭ cells, 72 paradigms and 740 branches** across PG5–PG8. There remain
**2,179 root entries without a complete path in this declared PG present
profile**. That is not an overall grammar-completion percentage. PG4–PG8
contain 98 record definitions referring to 88 distinct sūtra IDs, each within
its stated operation domain. The 3,983-entry text catalogue remains separate.

[Concurrent review](CONCURRENT_REVIEW.json) covers the latest head `ef8e982`,
T87 at `7a88722`, T86 at `7802a35` and the `1dff274` ledger update. T86's shared lexical IDs are useful for distinguishing
nominal and verbal progress: ad now has a present path here while its kta path
is still outside that packet. T86's reported 242 nominal outputs are not added
to the verb-cell count. The review also identifies a missing domain guard in
the internal kta helper; the bounded certificate loop itself uses an allowlist.
T87 adds four reported kta stems (pakta/labdha/tunna/lūna). Its final-dh
exception requires lexical refinement before wider reuse; one isolated helper
probe and a PG routing control record that boundary. No companion certificate
is replayed and no companion branch is merged.

[Source interpretation](SOURCE_REVIEW.md), [actual validation](VALIDATION.md)
and [remaining work](REMAINING.md) specify the boundaries. This is a linguistic
adapter. A full native operator-family construction, zero-specialization
compatibility and quantum-calculator integration remain separate obligations.
CI and main merging remain deferred by the owner.
