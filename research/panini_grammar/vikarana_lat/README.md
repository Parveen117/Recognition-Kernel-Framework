# PG5 — Vikaraṇa selection and complete bounded laṭ derivations

Author: Monty. 1 November 2026.

PG5 turns PG4's śap candidate into **reviewed vikaraṇa choices**, then derives
complete unaccented classical laṭ forms for **13 identified roots**. Eighteen
pada paradigms contain **162 person-number cells and 198 derivation branches**.
The extra branches are licensed options, not errors to discard.

There are **39 source-bound records**, **28 admitted lexical entries**, and one
new commentary correction to anuvṛtti. A source-bound record is a manually
reviewed semantic contract whose terms bind to PG4's annotated scope frame.
It is not an automatically inferred interpretation or a claim that all uses
of that sūtra are implemented. Runtime actions remain bounded Python adapters.

## What now runs

| Layer | Implemented contract |
| --- | --- |
| Selection | The ten gaṇa prescriptions on the identified entries below; selected lexical/sense exceptions in 3.1.70–82 |
| Marker-dependent effects | Śap and śa retain different marker histories despite both projecting to a; 1.2.4 produces ṅitvat status; 1.1.5 blocks the guṇa caused by that affix |
| Whole-affix disappearance | Adādi śap-luk and juhotyādi śap-ślu remain different events; 1.1.63 blocks the deleted śap's aṅga effect; further word operations remain obligations |
| Present endings | All nine parasmaipada and all nine ātmanepada cells, with supplied pada/person/number; ṭit belongs to laṭ, not to invented markers on individual endings |
| Derived root | Cur in its listed theft sense: ṇic, root-upadhā guṇa, sanādyanta dhātu, śap, guṇa of ṇic's i, ayādi |
| Interactions | Source-declared śap exceptions, 6.1.97 over 6.1.101/88, thās-specific 3.4.80, and trigger-relative guṇa prohibition; missing exception records are refused |
| Late reading | 8.2.77 for div/siv, pause ru/visarga, and PG4's admitted phonetic readout; the pre-Tripādī state is retained |

The runtime consumes the declared exception relations. It does not infer them
from finite domain containment or replace missing relations with numerical
priority. No universal nitya/antaraṅga/bahiraṅga resolver is claimed.

### Selection across the ten classes

| Gaṇa | Identified example | Prescription | Complete word generation here |
| --- | --- | --- | --- |
| 1 bhvādi | bhū | śap, 3.1.68 | Yes, on the admitted thematic entries |
| 2 adādi | ad | śap → luk, 2.4.72 | No |
| 3 juhotyādi | hu | śap → ślu, 2.4.75 | No; 6.1.10 reduplication remains required |
| 4 divādi | div | śyan, 3.1.69 | Yes, on the admitted entries |
| 5 svādi | su | śnu, 3.1.73 | No |
| 6 tudādi | tud | śa, 3.1.77 | Yes, tud/nud |
| 7 rudhādi | rudh | śnam, 3.1.78 | No; mit infix placement and subsequent operations remain required |
| 8 tanādi | tan, identified kṛ | u, 3.1.79 | No |
| 9 kryādi | krī | śnā, 3.1.81 | No |
| 10 curādi | cur | ṇic, 3.1.25; derived dhātu, 3.1.32; then śap | Yes, this cur entry only |

The table is a set of witnessed prescriptions, not an implementation of every
member, sense or directive in all ten gaṇas. Selection-only plans have explicit
unexecuted obligations and cannot be returned as complete words. In particular,
śnam's position in a plan's constituent list is not its spoken position.

### Complete admitted paradigms

| Root identity | Pada | Distinct behavior |
| --- | --- | --- |
| 1010001 bhū | P | bhavati, bhavanti, bhavāmi |
| 1011151 pac | P, A | All 18 cells have literal Kāśikā 3.4.78 examples |
| 1010002 edh | A | edhe follows ṭer e before the internal pararūpa seam |
| 1011130 labh | A | labhate … labhāmahe |
| 1040001 div; 1040002 siv | P | Guṇa blocked; later dīvyati/sīvyati by 8.2.77 |
| 1040098 śam | P | śāmyati by the identified śamādi 7.3.74 domain |
| 1060001 tud; 1060002 nud | P, A | śa is apit/ṅitvat; no spurious todati/nodati |
| 1100001 cur | P, A | corayati/corayate through the two distinct aṅgas |
| 1040102 bhram | P | bhramati / bhrāmyati, with branch-specific 7.3.74 |
| 1011033 laṣ | P, A | laṣati / laṣyati and the corresponding A branches |
| 1040107 yas | P | yasati / yasyati without a prefix |

P/A in this table does not infer a contextual pada license. `Request` requires
that fact and the exact admitted lexical sense. Sanskrit *prathama* corresponds
to English third person, *madhyama* to second, and *uttama* to first. Prefixes
sam/pra/ā are admitted only for the reviewed selection queries; complete
prefixed words remain unresolved.

## Use

From the repository root, with the [pinned primary data](SOURCE_REVIEW.md):

```sh
python3.12 -m research.panini_grammar.vikarana_lat.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1060001 --sense व्यथने --pada P --pada-licensed --all-forms
```

Add `--trace` for morphemes, original teaching sounds, markers, inherited scope
evidence, blocked operations, replacements and the separate pause readout.
`Grammar.select(request)` returns choices; `plan(request)` retains unexecuted
obligations; `derive(request)` returns complete branches only within the
reviewed domain. `UNRESOLVED` means the adapter cannot establish the requested
path. It does not mean the requested Sanskrit form is impossible.

## Verification and limits

Run the direct changed-claim check:

```sh
python3.12 research/panini_grammar/vikarana_lat/verify.py \
  --source-root /path/to/ashtadhyayi-data
```

The [report](VERIFICATION_RESULT.json) separates 40 literal commentary word
cases, 25 selection cases, 22 expected refusals, structural/history controls,
and the full 162-cell comparison to pinned Vidyut output. Agreement with
another implementation is a diagnostic, not an independent Sanskrit validity
oracle. Detailed evidence and unimplemented domains are in
[source review](SOURCE_REVIEW.md), [validation](VALIDATION.md), and
[remaining work](REMAINING.md).

PG5 adds a discrete linguistic adapter over PG3/PG4. It introduces no new native
operator theorem, physical identification, clock or quantum-calculator mapping.
PG1's full-family specialization requirement remains an obligation for such an
application. The historical theorem/source packets and operator engine remain
unchanged. CI and main-branch merging are deferred by the owner's instruction.
