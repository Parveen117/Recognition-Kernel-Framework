# PG12 — Further śnu, u and śnā present paths

Author: Monty. 2 November 2026.

PG12 adds **97 identified roots, 124 licensed pada paradigms, 1,116 present
cells and 1,316 derivation branches**. It extends the earlier non-thematic
adapter with root operations and their effects on following affixes.
Lexical identity, exact listed meaning, contextual pada license, person,
number and register remain explicit inputs.

| New group | Root entries | Pada paradigms | Cells | Branches |
| --- | ---: | ---: | ---: | ---: |
| Further svādi, class 5 | 22 | 30 | 270 | 308 |
| Further tanādi, class 8 | 8 | 14 | 126 | 230 |
| Further kryādi, class 9 | 67 | 80 | 720 | 778 |
| **PG12 total** | **97** | **124** | **1,116** | **1,316** |

The cumulative [coverage register](COVERAGE_STATUS.json) now records
**228 / 2,229 root entries, 290 paradigms, 2,610 present cells and 2,959
branches**. The admitted profiles cover 26/38 class-5 entries, 10/10 class-8
entries and 70/71 class-9 entries. These are identified unaccented,
unprefixed classical kartari laṭ profiles, not every context or textual
reading of those classes. No overall grammar-completion percentage is
assigned.

## What is newly developed

- **Owned root n-lopa.** 6.4.24 deletes the penultimate n of admitted
  non-idit consonant-final roots before the actual kit/ṅit affix. Dambh,
  bandh and the stambh group retain the deleted sound and its root owner.
- **Composing affix options.** Sku and the four sūtra-listed stambh roots
  preserve both śnu and śnā under 3.1.82. Ending changes and cluster-sensitive
  u junctions are then evaluated on each branch separately.
- **Optional root guṇa with later consequences.** Kṣiṇ, ṛṇ, tṛṇ and ghṛṇ
  retain the commentary's two root-guṇa readings. Root guṇa is caused by
  u; strength of that u is separately determined by the ending.
- **Saṃprasāraṇa with intermediate history.** Grah and jyā keep the original
  semivowel, its vowel substitute and the following-vowel merger. Jyā's
  intermediate long ī remains recorded before the later pvādi shortening.
  Grah's nonfinal ṛ does not receive that lengthening.
- **An actual ūṭh substitute.** Khav's final v becomes ūṭh under 6.4.19.
  The marker remains in memory, and 6.1.89 uses that owned substitute to
  produce au. The operation cannot be borrowed by an ordinary long ū or
  represented as an inserted augment.
- **Broader, bounded ṇatva.** The new readout admits reviewed aṭ/ku/pu
  interveners. Tṛp and kṣubh retain their explicit prohibitions. Kṣubh's
  prohibition survives śnā's ā → ī or ā-lopa through a checked local
  identity query; it does not restore deleted sounds.

The optional choices do not always form an unrestricted product. For
example, ṛṇ in first-person dual has these three branches:

| Root reading | Following u | Result |
| --- | --- | --- |
| ṛṇ | retained | ṛṇuvaḥ |
| ṛṇ | deleted | ṛṇvaḥ |
| arṇ after guṇa | retained; rṇ blocks u-lopa | arṇuvaḥ |

Kṣiṇ's i → e does not create that extra consonant cluster, so its
corresponding cells retain four branches. The implementation computes
these conditions from the current owned constituents.

## Source decisions and boundaries

[RULE_RECORDS.json](RULE_RECORDS.json) adds 22 occurrence-bound definitions.
One commentary-supported overlay supplies the aṇ condition at 6.4.2.
Across PG4–PG12 there are 208 bounded definitions / 152 distinct sūtra IDs.
The [source review](SOURCE_REVIEW.md) and seven
[adjudications](SOURCE_ADJUDICATIONS.json) distinguish source disagreement,
profile selection and implementation comparison.

This stage selects the explicit pvādi subdivision ending at plī. It does
not silently combine that reading with the broader through-end-of-gaṇa
interpretation. The class-5 kṣi profile has a positive classical-use
license despite its retained Vedic tag. Conversely, untagged class-5
pṛ/spṛ/smṛ remain deferred because of their commentary register evidence.
The membership of the separate śṝñ entry 1090015 also remains unresolved.

[Validation](VALIDATION.md) records 109 literal-word cases across 73 new
roots, 37 expected refusals and 124 direct controls. All pass. The separate
1,116-cell / 1,316-branch comparison has zero differences. Twenty-four new
entries have no separate exact full-word witness in the selected passages;
their lexical/rule evidence and software agreement are labeled separately.
The seven earlier PG10/PG11 word-witness gaps remain open.

## Run locally

Use the `ashtadhyayi-com/data` checkout pinned in
[SOURCE_PINS.json](SOURCE_PINS.json), commit
`5744762f010d677cfb43f347a42d02796cf615d6`:

```sh
python3.12 -m research.panini_grammar.nasal_present.verify \
  --source-root /path/to/ashtadhyayi-data

python3.12 -m research.panini_grammar.nasal_present.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1080005 --sense 'गतौ' \
  --pada P --pada-licensed --all-forms
```

Add `--trace` to inspect root/affix ownership, the options and readout
history. The verifier's `--write` option regenerates only PG12's result
and coverage files. The generator and CLI read neither the expected-word
packet nor the external conjugation table.

PG1–PG11 remain frozen. [Remaining work](REMAINING.md) includes other
present classes, coupled dhinv/kṛnv substitutions, prefix and register
contexts, wider tense/voice systems and the native operator lift. Full
operator-family lifting, typed zero-specialization compatibility and
quantum-calculator integration remain open. Hosted CI and main merging
remain deferred.
