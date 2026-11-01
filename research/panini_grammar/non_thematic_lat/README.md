# PG6 — Non-thematic laṭ: strong/weak stems and retained visibility

Author: Monty. 1 November 2026.

PG6 completes classical, unaccented present kartari laṭ paths for **ten more
identified roots**. Seventeen pada paradigms contain **153 person-number cells
and 167 derivation branches**. It extends PG5's linguistic adapter, preserving
the original PG1–PG5 code, reports and source pins.

The stage adds **17 source-bound records** and three explicit local scope
decisions. These are hand-reviewed contracts bound to the pinned annotated
source. They are not automatic Sanskrit-text interpretation or complete
implementations of all uses of the seventeen sūtras. 6.4.22 is a reviewed
visibility obligation, and 1.1.58 is used only for the documented kur query.

## Newly completed domain

| Lexical ID | Root / supplied sense | Pada | Representative new paths |
| --- | --- | --- | --- |
| 1050001 | su, अभिषवे | P, A | sunoti / sunutaḥ; sunvanti; sunuṣe |
| 1050005 | ci, चयने | P, A | cinoti / cinutaḥ; cinvanti / cinvate |
| 1050016 | āp, व्याप्तौ | P | āpnoti / āpnutaḥ; āpnuvanti |
| 1050017 | śak, शक्तौ | P | śaknoti / śaknutaḥ; śaknuvanti |
| 1080001 | tan, विस्तारे | P, A | tanoti / tanutaḥ; tanvanti / tanvate |
| 1080010 | kṛ, करणे | P, A | karoti / kurutaḥ; kurvaḥ; kurute |
| 1090001 | krī, द्रव्यविनिमये | P, A | krīṇāti / krīṇītaḥ; krīṇanti / krīṇate |
| 1011092 | śru, श्रवणे | P | śru → śṛ with śnu; śṛṇoti / śṛṇutaḥ |
| 1090014 | pū, पवने | P, A | pū → pu before śit; punāti / punītaḥ |
| 1090016 | lū, छेदने | P, A | lū → lu before śit; lunāti / lunītaḥ |

The lexical identity, exact listed sense and contextual pada license are
inputs. The engine does not infer the intended meaning or pada from a word.
No other member of classes 5, 8 or 9 is silently admitted by this table.

## The distinctions implemented

- **Two guṇa triggers:** śnu's ṅitvat blocks root guṇa; pit tiṅ can still
  license guṇa of the vikaraṇa's u. Apit tiṅ blocks that second operation.
- **Two vowel-junction paths:** sunvanti uses 6.4.87. The consonant cluster
  across āp + nu blocks it, so āpnuvanti uses 6.4.77. Tan's u is a different
  affix and uses 6.1.77.
- **Optional versus mandatory loss:** 6.4.107 gives sunuvaḥ/sunvaḥ and the
  corresponding eligible m/v options. 6.4.108 makes kṛ's u-loss mandatory.
  Śak/āp retain u after the consonant cluster; strong sunomi is not an option.
- **Weak śnā:** following consonants select ī by 6.4.113; following vowels
  select ā-lopa by 6.4.112. Jh substitution happens first, so a surface vowel
  trigger is available in krīṇanti/krīṇate.
- **Non-a ātmanepada:** 7.1.5 replaces immediately following jh with at, while
  the ordinary ant rule remains available outside that domain. Long ā is
  included in this non-short-a domain.
- **Late sound operations:** bounded adjacent-affix ṣatva and ṇatva are
  inserted into the correct phase of the phonetic reading. A late 8.4.58 n
  cannot feed back into earlier ṇatva: kurvanti remains dental, while krīṇanti
  retains both the earlier retroflex ṇ and the later dental n.
- **A specific visibility query:** after kṛ u-loss, lengthening sees kur
  under the Kāśikā 6.4.108 reading of 1.1.58; 8.2.79 then blocks lengthening.
  The deleted affix and the prohibition both remain in history.

PG6's phonetic adapter uses PG4's reviewed 8.3.24 parameters before the new
operations. It then reuses PG4's later contact/parasavarṇa pass, with a guard
that rejects any re-entry into an earlier phase. The pre-Tripādī state is
immutable under a readout, and a readout cannot be accepted as a new source.
This finite scheduling contract is not a general asiddha/ābhīya interpreter.

## Use and inspect

From the repository root with the pinned primary-data checkout:

```sh
python3.12 -m research.panini_grammar.non_thematic_lat.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1050001 --sense अभिषवे --pada P --pada-licensed --all-forms
```

Use `--trace` to inspect the original teaching form, affix markers, strong/weak
cause, optional branch, replacement targets, retained deletions and late query.
`Grammar.derive(Request(...))` returns full branches. It delegates unaffected
thematic requests to PG5; its unexecuted morphological `plan` still records
obligations until `derive` discharges them. Unsupported contexts return
`UNRESOLVED`, which is not a claim of linguistic impossibility.

## Verification and remaining work

[Verification](VERIFICATION_RESULT.json) separates **53 literal traditional
word cases**, **eight expected refusals**, **54 direct controls**, and the
complete comparison of 153 new cells to pinned Vidyut output. There are zero
comparison differences on this domain. The comparison is not a soundness
oracle or an independent manuscript edition.

See [source readings](SOURCE_REVIEW.md), [validation](VALIDATION.md), and
[remaining work](REMAINING.md). The next stage is śnam infix placement and
strong/weak class 7 derivation, followed by adādi and juhotyādi reduplication.
No percentage of full Sanskrit grammar is inferred from these counts.

This is a discrete linguistic adapter, not a new native operator theorem.
PG1's operator-family and zero-specialization compatibility requirements
remain open before a claimed quantum-calculator mapping. CI and main merging
remain deferred by the owner's instruction.
