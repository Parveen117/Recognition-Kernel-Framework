# PG7 — Śnam inside an owned root: class-7 laṭ

Author: Monty. 1 November 2026.

PG7 completes a declared unprefixed, classical, unaccented present kartari
profile for **23 identified class-7 roots**: **32 pada paradigms, 288
person-number cells and 330 branches**. It extends the PG6 adapter and keeps
every predecessor implementation, source pin and report unchanged.

The central change is structural. Śnam is placed after the last vowel by
**1.1.47**, while the base root remains one morpheme. A separate root-with-mit
constituent includes that root and the affix; an owned layout supplies their
interleaved surface order. Replacements and deletions retain which unit owned
each sound. No full word or software comparison table is used by the generator.

| Path | New distinction |
| --- | --- |
| bhid → bhinatti / bhindanti | Strong śnam `na` versus weak `n`; 6.4.111 reads actual tiṅ features |
| rudh → ruṇaddhi / rundhanti | Earlier ṇatva cannot see the dental n restored later by 8.4.58 |
| runddhaḥ / rundhaḥ | Optional 8.4.65 retains both the unchanged and root-consonant-deletion histories |
| yuj → yunakti / yuṅkṣe / yuñjanti | Root palatal/velar, ṣatva, voicing and nasal rules use ordered views |
| indh → inddhe / indhe; hiṃs → hinasti | 6.4.23 deletes the root-owned n, including a previously inserted num; śnam's own n remains |
| śiṣ → śinaṣṭi / śinakṣi | Retroflex contact differs from the k substitution before s |

The 23 entries are rudh, bhid, chid, ric, vic, kṣud, yuj, chṛd, tṛd, kṛt,
indh, khid, vid, śiṣ, piṣ, bhañj, hiṃs, und, añj, tañc, vij, vṛj and pṛc.
Exact teaching forms, senses and IDs are in [the lexical manifest](LEXICAL_ENTRIES.json).
Homonyms from other gaṇas do not share this admission.

Two class-7 entries remain outside PG7: **bhuj**, whose sense/pada contract
must include 1.3.66, and **tṛh**, which needs im and h/ḍh interactions. Pada
licensing and the exact lexical sense are supplied inputs, not inferred from
spelling. Optional pronunciation doubling under 8.4.46–47 is outside this
explicit spelling profile; optional collapse under 8.4.65 is included.

## Source and derivation contracts

Eleven source-bound records include seven IDs new to the PG4–PG6 record union
and four IDs reused for new local contracts. One commentary decision removes
the publisher's inherited `परसवर्णः` at 8.4.65 while retaining its actual
`सवर्णे` condition, prior hal and optional lopa. This is a documented local
reading, not a change to the pinned Sanskrit source.

The śnam/guṇa interaction follows the specific nitya argument in the
Siddhāntakaumudī and Bālamanoramā. It does **not** make the pre-infix root
vowel into an aṅga before śnam and then explain everything by ṅit. After
insertion, the aṅga relative to tiṅ has a different upadhā.

See [source review](SOURCE_REVIEW.md) for the exact readings, the local
1.1.58 nasal-visibility query and the finite phase schedule. General nitya,
ābhīya and sthānivad interpretation remain open.

## Use

From the repository root with the pinned primary-data checkout:

```sh
python3.12 -m research.panini_grammar.snam_lat.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1070001 --sense आवरणे --pada P --pada-licensed --all-forms
```

Use `--trace` for ownership, markers, placement, the root-with-mit constituent,
the aṅga query, partial deletion and phonetic branches. `Grammar.derive` also
routes existing PG5/PG6 requests. Unsupported requests return `UNRESOLVED`;
that status does not mean the requested Sanskrit form is impossible.

## Evidence and remaining grammar

[Verification](VERIFICATION_RESULT.json) records **85 literal word-membership
witnesses**, **13 expected refusals**, **63 direct controls**, and **208 literal
anchors**. A word witness establishes membership, not every optional spelling.
Complete sets for all 288 new cells are separately compared with pinned
Vidyut output: **zero differences**, 330 branches. This software comparison
is not a Sanskrit soundness oracle.

[Coverage](COVERAGE.md) now separates 3,983 catalogued sūtras, 80 distinct
source-bound IDs in PG4–PG7, the frozen root-preprocessing diagnostic, and
46 completed root entries / 603 laṭ cells across PG5–PG7. None is an overall
grammar-completion percentage. [Remaining work](REMAINING.md) starts with
the two excluded class-7 entries and adādi/juhotyādi mechanisms.

This is a linguistic adapter. The native operator-family and
zero-specialization obligations remain open before any quantum-calculator
application. CI and main merging remain deferred by the owner.
