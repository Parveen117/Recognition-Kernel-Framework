# PG26 — T144/T145 review and bounded integration handoff

Author: Monty. 2 November 2026.

Companion branch: `shaiva-sources-maheshvara-spanda-pratyabhijna`.
The initial reviewed head was **T144,
`3de268ddded005c37bf0a0a569538e7a135983d3`**. The closing snapshot is
its child **T145, `d5d0994c3828a87e1b30114a15ba5d4838c10eaa`**.
Both complete theorem capsules, the T144 lane generator, relevant
engine rows/helpers/diff sections, kernel changes and ledger records
were read. This is targeted static review, not a whole-engine audit
or runtime replay. T145's attributed capsule date is 3 November 2026;
this work record retains the session's UTC date. No merge or cherry-pick
is performed.

## Useful work credited

| Companion work | Use and retained boundary |
|---|---|
| T144 pinned Dhātupāṭha TSV and accent lookup | Supplies a reproducible lexical accent source for short iṭ decisions. PG26 retains its exact primary lexical IDs; long īṭ under 7.3.95 is a different rule. |
| T144 future and āśīrliṅ expansion | Adds productive ārdhadhātuka contexts, source substitutions and the separate P/A kit account. Those are different position keys from PG26's I/O/B. |
| T144 6.4.118 lakāra guard | Keeps hāk's vidhiliṅ y-lopa from being transported indiscriminately into āśīrliṅ. |
| T144 7.1.4 actual intervening segments | Requires no surviving vikaraṇa or iṭ before the abhyasta jh replacement; avoids transporting a direct-contact rule through future morphology. |
| T145 liṭ breadth | Adds A endings, periphrastic ām, copy/root distinctions, cluster handling, weak root shapes and thal conditions. Optional branches recorded but not all emitted remain explicit. |
| T145 lṛṅ | Adds the conditional semantic/lakāra context and reuses sya plus past augment machinery. The semantic admission condition remains part of a written extension. |
| T145 conjunct helper | Treats the kṣ token as a conjunct before a final vowel. Token ownership matters independently of how a word prints. |

The T144 TSV hash is
`bb2013ead0ea536dc7f887164c385c703cb0014ccf6e5af35b87e6d3049ba380`.
The lookup strips accent/marker notation for its key, includes gaṇa,
and chooses the first hit, with a separate śru fallback. This is not
a proof that every normalized key has one sense or one lexical record.
The thirty relevant raw rows are archived for provenance; D's exact
IDs and inherited sense contracts continue to govern admission.

## Attributed reports, without replay

| Snapshot/context | Report |
|---|---|
| T145 present-system lane | 5,373/5,373, retained from T143/144 |
| T145 fixed verbal suite | 908/908; 200 rows |
| T145 lṛṭ, luṭ and āśīrliṅ | 1,845/1,854 each; nine daridrā cases remain in each |
| T145 liṭ | 1,799/1,849; headline remainder 50 |
| T145 lṛṅ | 1,845/1,854; nine daridrā cases |
| T145 luṅ baseline | 1,077/1,854, measured and not claimed complete |
| T145 kernel | 261 distinct rule IDs; 90 nominal and 189 verbal, sharing 18 |

Four rows are declared surface-coincident: 3.4.92, 7.1.58, 8.4.56
and 6.4.2. These units are distinct from PG26's written positions and
source-choice-labelled readings. The capsule's liṭ root breakdown
lists jakṣ 8 + stubh 9 + stṛ 15 + ūrṇu 18 + i-thal 2 = **52**,
whereas 1,849−1,799 is **50**. Its text does not state an overlap.
Retain both attributed statements and request reconciliation of that
breakdown; do not silently correct a root count or invent an overlap.
No committed per-cell engine comparison report resolving it was found
among the inspected report paths. The pinned oracle lane is not itself
an engine-agreement report.

T145's verbal expected hash is
`8b1d51cbe96a8d630bc8121dd9d4b1a8f9707f6eb47b0a1f9bf46ffbca6e1fd5`;
its kernel expected hash is
`1919bac6b5f86201d650de783b9608f97f31eac7ad195882388c5e34f7a758c6`.
These are companion pins, not results executed by PG26.

The companion ledger now labels **544 IDs** compiled/meta/hand_coded.
Retaining Codex's independent written records and the new PG26 clauses
gives **609 bounded-rule IDs**. T144 supplies eight new IDs beyond
PG25's union and T145 supplies another twenty-seven. Cited-only and
misnumbered entries are excluded. Implementation grades remain
attributed; neither the union nor a one-word agreement establishes
every context or every licensed alternative of a rule.

## Current implementation handoff

1. **PG26 ending-owned īṭ.** Implement 7.3.95's complete absent/present
   fibres after ending refinement. Its hal test includes modal y and
   has no pit requirement. Strong augmented tu uses av; weak tām/hi/y/tāt
   uses uv. Complete jh/āṭ first so antu and first persons do not gain
   spurious īṭ. Keep short iṭ's lexical accent policy separate.
2. **Ūrṇu and blessing choices.** Add 7.3.90's second ordinary strong-tu
   reading without spreading it to weak tāt or vowel-facing first
   persons. Keep 7.1.35 tāt as an ending-dependent branch. PG26 requires
   864 positions /991 readings, with 307 I, 315 O and 369 B readings.
3. **PG25 choices still open.** Full 6.4.115/116 branches and 6.4.117's
   actual-hi triple remain outside the inspected runtime claims. PG24's
   optional weak-vowel mṛj branch also remains a separate obligation.
4. **Ṛ copy remains a specific gap.** T145 now has a 6.4.78 row, so
   saying that row is wholly absent would be stale. Its guard is
   explicitly `lak == "liṭ"`; it does not yet supply PG25's ślu
   ṛ-copy iyaṅ in I/O/B. Keep copy/root owners separate when extending
   it to iyṛhi, iyratu, iyarāṇi and iyṛyāt.
5. **Source-view/native adapters.** The historical `_siyut` policy
   remains distinct from the written resolved-ī policy. Equal words
   do not identify the histories. Preserve augment choice, actual
   context and effective markers through the native carrier; PG26 N3
   proves why its coarse two-history observer cannot carry the hal
   query without repair. T142's surface pairing still needs an explicit
   adapter to the canonical full carrier and typed specialization.
6. **T145 frontier.** Reconcile the liṭ residue breakdown in the
   written report; retain the named liṭ/luṅ and daridrā limitations,
   recorded-but-unemitted alternatives and semantic scope. The capsule's
   “only luṅ” statement describes its comparison lane, not completion
   of every Sanskrit kartari input or the whole grammar.

Codex's next written block is the remaining admitted consonant adādi
and rudhādi/contextual modal scope. Claude can work on these explicit
choice/history obligations and its separate ārdhadhātuka frontier.
The owner's grammar-first priority still defers Python tests and
certificate replay. This file is a prepared handoff; no external message
was sent, and frozen certificates were not overwritten.
