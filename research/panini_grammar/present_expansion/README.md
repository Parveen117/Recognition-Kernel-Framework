# PG10 — Further juhotyādi and vowel-final adādi present paths

Author: Monty. 1 November 2026.

PG10 adds **38 identified roots, 44 licensed pada paradigms, 396 present
cells and 438 derivation branches**. The scope is unprefixed, unaccented,
classical kartari laṭ with the exact lexical meaning and pada license in
[LEXICAL_ENTRIES.json](LEXICAL_ENTRIES.json). A cell is one lexical profile,
person and number; optional forms are separate branches of that cell.

| New group | Roots | Pada paradigms | Cells | Branches |
| --- | ---: | ---: | ---: | ---: |
| Further juhotyādi | 11 | 15 | 135 | 145 |
| Vowel-final adādi in u | 13 | 15 | 135 | 167 |
| Vowel-final adādi in ā | 14 | 14 | 126 | 126 |
| PG10 total | 38 | 44 | 396 | 438 |

The juhotyādi additions are bhī, hrī, long pṝ and the separately identified
short pṛ, bhṛ, māṅ, hāṅ, hāk, nij, vij and viṣ. The u-final adādi group is
yu, ru, tu, nu, kṣu, kṣṇu, snu, ūrṇu, dyu, su, ku, stu and hnu. The ā-final
group is yā, vā, bhā, snā, śrā, drā, psā, pā in protection, rā, lā, dāp in
cutting, khyā, prā and mā. Source spellings, markers and meanings remain in
the lexical packet; these display names do not replace lexical identity.

## What the derivations retain

Each new reduplicating path keeps the original root, a separately owned
copy, links from copied sounds to their source identities, and ordered
replacement/deletion history. Copy shortening, lexical copy guṇa or i,
r-accompanied substitution and later consonant deletion are distinct
operations. Root strength is read from the actual ending. This separates
`bibhyati` from cluster-conditioned `jihriyati`, `pipūrtaḥ` from `pipṛtaḥ`,
and strong `nenekti` from weak `nenijati`.

Bhī and hāk retain both licensed weak consonant-initial options:
`bibhitaḥ / bibhītaḥ` and `jahitaḥ / jahītaḥ`. Māṅ and hāṅ use their own
copy-i and non-ghu root changes. Class-2 mā and dāp cannot borrow those
class-3 operations merely because their final vowel is the same.

Ru, tu and stu admit optional īṭ as an initial member of the following
tiṅ, with its deleted ṭ marker retained. It belongs to the ending, not to
the aṅga. Actual ending substitution precedes the eligibility query; īṭ
then changes the junction before strength and vowel replacement. This
gives `rauti / ravīti`, `rutaḥ / ruvītaḥ`, but a single `ruvanti`.
Ātmanepada stu admits `stute / stuvīte` without a pit requirement. Ūrṇu's
separate option gives `ūrṇoti / ūrṇauti` in strong cells.

The phonetic readout preserves ownership and source history and cannot
feed its result back into the earlier morphological state. In `prānti`,
earlier anusvāra and later dental-n restoration are kept in order; the
restored n does not trigger a second ṇatva pass.

## Evidence and current coverage

[Source review](SOURCE_REVIEW.md) explains 29 bounded rule records and two
new commentary-supported scope overlays. [Validation](VALIDATION.md)
records 153 literal Sanskrit word witnesses, 35 expected refusals, 94
direct controls and a separate 396-cell / 438-branch Vidyut comparison
with zero differences. The generator reads neither expected words nor
the comparison table.

Literal word witnesses cover 32 of the 38 new entries. Six entries have
pinned lexical/rule evidence and implementation comparisons but no
separate full-word witness in the selected commentary passages: su
(`1020036`), ku (`1020037`), śrā (`1020048`), rā (`1020052`), dāp
(`1020054`) and prā (`1020056`). This evidence gap is explicit in
[COVERAGE_STATUS.json](COVERAGE_STATUS.json).

Cumulative bounded coverage is **91 / 2,229 root entries, 121 pada
paradigms, 1,089 cells and 1,223 branches**. Class 3 now includes the first
14 unmarked entries of the pinned 26-row list. The 12 tagged entries are
unadmitted; the tagged vowel-initial ṛ entry has a traditional discussion
of classical use and still needs its own review. This is not a claim that
all classical class-3 grammar is complete. Class 2 covers 29 entries; its
77 source rows contain 76 lexical rows and one gaṇasūtra placeholder.

There are 143 bounded rule-record definitions across PG4–PG10, addressing
112 distinct sūtra IDs. The 3,983-record text inventory remains a
catalogue, and no overall grammar-completion percentage is assigned.

## Inspect a path

Use the pinned `ashtadhyayi-com/data` checkout identified in
[SOURCE_PINS.json](SOURCE_PINS.json):

```sh
python3.12 -m research.panini_grammar.present_expansion.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1020038 --sense स्तुतौ --pada A --pada-licensed \
  --all-forms
```

Add `--trace` to inspect copies, owners, optional branches, blocked
alternatives and ordered events. Unsupported contexts remain unresolved.

The primitive software carrier is the inherited finite grammatical plan:
typed morphemes and sounds, source identities, visible units, retained
memory and ordered history. PG10 extends that explicit linguistic
adapter. It does not construct the native full operator family or prove
its zero-specialization compatibility. Those obligations, general
grammar and quantum-calculator integration remain [open](REMAINING.md).
PG1–PG9 source packets and certificates are preserved. Hosted CI and main
merge remain deferred.
