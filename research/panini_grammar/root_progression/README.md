# PG3 — Root preprocessing after the sound and marker layers

Author: Monty. 1 November 2026.

PG3 reviews `36a8ff6` (T81) and `674fdc5` (T82) against the pinned Sanskrit
sources, then develops a bounded root pipeline using their admitted selectors
and augment-placement contract. It extends the PG2 marker ledger, keeps the
original teaching sounds and marker units, and separates a later phonetic
query from the earlier root state.

**Status: grammar incomplete; no general valid-Sanskrit oracle.** The new
reference cases, source findings and remaining differences are recorded in
[VERIFICATION_RESULT.json](VERIFICATION_RESULT.json). Earlier theorem,
certificate and PG2 result files retain their original bytes. The canonical
operator engine and quantum calculator are unchanged.

## What is executable

| Step | Reviewed rule | Admitted operation |
| --- | --- | --- |
| Marker designation and lopa | 1.3.2–9, with commentary exceptions | Reuse PG2's original-position and compound-marker ledger; add identified jh/ch/ṭh/ḍh affix exceptions |
| Initial root substitution | 6.1.64 धात्वादेः षः सः | Initial ṣ → s, with source-identified exclusions |
| Initial root substitution | 6.1.65 णो नः | Initial ṇ → n; retain the original sound and its identity |
| num licensing | 7.1.58 इदितो नुम् धातोः | A standalone short nasal i-it licenses num; a component of ñi or ir does not |
| Ordinary num placement | 1.1.47 मिदचोऽन्त्यात्परः | Insert n after the last surviving vowel, using T81's ṭi selector and T82's ordinary num contract |
| Separate phonetic query | 8.3.24 नश्चापदान्तस्य झलि | For the newly inserted n only, read anusvāra before jhal inside the supplied root |
| Query continuation | 8.4.58 अनुस्वारस्य ययि परसवर्णः | Before an admitted stop, select the corresponding nasal from T81's stop-varga class |

The query does not overwrite the earlier state. This implements one bounded
separation motivated by 8.2.1 पूर्वत्रासिद्धम्; the full rule-relative asiddha
calculus remains open. The hand-reviewed contracts are in [RULES.json](RULES.json),
the adapter in [root_preprocess.py](root_preprocess.py), and the source reasoning
in [SOURCE_REVIEW.md](SOURCE_REVIEW.md).

`RootInput` requires lexical identity, an explicit Devanāgarī teaching form,
root origin and a declaration that conventional nasality has been supplied.
It has no expected-headword field. Root origin, meaning, gaṇa, pada and seṭ
status are not inferred from spelling. The `nasal` flag on inherited sound
records denotes teaching-vowel nasalization, not consonant manner.

## Why marker units must survive

| Supplied teaching form | Retained marker unit | It-only projection | Preprocessed root |
| --- | --- | --- | --- |
| भिदिँ, entry 1010067 | i | bhid | bhind, by 7.1.58 and 1.1.47 |
| भिदिँर्, entry 1070002 | ir | bhid | bhid; the compound ir does not license this num |
| णीञ्, entry 1011049 | ñ | ṇī | nī, by 6.1.65 |
| गडिँ, entry 1010068 | i | gaḍ | ganḍ; the separate phonetic query reads gaṇḍ |

The first two rows have the same visible marker-only output and different
licensed next operations. Kāśikā 7.1.58 explicitly distinguishes compound ir
from idit. The implementation retains both the unit and its original sound
positions. Substitution preserves a sound's UID; augmentation creates a fresh
UID; lopa retains the removed positions in history.

## Source corrections to carry forward

- **T82 lakāras:** its ten supplied rows remove l and keep the vowel. The
  reviewed Kāśikā/Tattvabodhinī reading retains technical l. PG3 supplies the
  conventional nasal vowel explicitly and retains l. Direct probes also feed
  the same annotated form to T82, isolating its missing l exception from the
  separate omission of nasal notation in the old inputs.
- **PG2 jhi:** PG2 retained affix identity but deleted jh. That reading is
  superseded here: the identified affixes retain jh for the later replacement.
  PG2's passing historical fixture is not treated as linguistic confirmation.
- **T81 savarṇa:** its ṛ/ḷ split and long ḹ inventory do not exhaust the
  Kāśikā reading of 1.1.9. PG3 uses the stop-varga domain only; a full corrected
  vowel inventory and savarṇa profile remain open.
- **Aṅga and coverage:** whole-string prefixes and ordinary augment placement
  do not establish all aṅga/augment cases. The historical ledger counts
  declarations; they are not percentages of grammar verified or compiled.

The attributed findings are in [CLAIM_REVIEW.json](CLAIM_REVIEW.json).

## Pinned-witness diagnostic

All 2,259 source records are examined: **2,229 roots** and **30 gaṇasūtra
directives**, kept separately. Two root teaching conventions remain unresolved
at every stage.

| View of the 2,229 roots | Exact source-headword agreement | Different projection | Unresolved |
| --- | ---: | ---: | ---: |
| PG2 marker-only baseline | 1,703 | 524 | 2 |
| PG3 root preprocessing | 1,844 | 383 | 2 |
| PG3 separate num phonetic query | 2,081 | 146 | 2 |

There are 141 additional agreements after root preprocessing and another 237
after the phonetic query, with no lost agreements on this pinned witness.
These counts compare spellings. They do not establish full root derivations,
coverage of the Aṣṭādhyāyī, or independent grammatical correctness.

All 146 remaining differences, both unresolved entries and the 30 directives
are retained in the report. Examples include length differences (उर्दँ / ऊर्द्),
the cluster after initial ṣ → s (ष्टुचँ / स्तुच्), and existing root nasals
(कुन्चँ / कुञ्च्) outside the new-num-only query. Nothing is silently changed to
make a headword match. The unresolved teaching forms are छदिः and दुःख; their
ayogavāha conventions require a separate source review.

## Reproduce the direct checks

Use the `ashtadhyayi-com/data` checkout at
`5744762f010d677cfb43f347a42d02796cf615d6`, then run from the repository root:

```sh
python3.12 research/panini_grammar/root_progression/verify.py --source-root /path/to/ashtadhyayi-data
```

The default invocation checks pinned bytes and reproduces the checked-in report.
`--write` writes this stage's report only. [VALIDATION.md](VALIDATION.md) records
what was executed and distinguishes source checking, local cases, corpus
diagnostics and repository navigation checks.

The next grammar work still includes automatic inherited-scope interpretation,
broader exception/priority and sthānivad domains, the remaining lexical
differences, gaṇasūtra/Uṇādi semantics and independent derivation references.
CI, main-branch merging and calculator integration remain deferred.
