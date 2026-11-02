# PG1 sources, edition and attribution

Author: Monty. 1 November 2026.

## Text witness and reproducibility

The principal electronic witness is **Nīleśh Bodas / ashtadhyayi.com**,
[ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data), commit
[`5744762f010d677cfb43f347a42d02796cf615d6`](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
The publisher's README permits reuse with appropriate credit. PG1 credits the
publisher here and in the machine-readable source record. Its modern English
and Sanskrit explanations have not been imported wholesale.

[SUTRAPATHA.tsv](SUTRAPATHA.tsv) contains only the public-domain sūtra text and
its identifiers extracted from `sutraani/data.txt`: `a.p.n`, the publisher's
`i` key, and `s`. Spelling and word spacing are preserved byte-for-byte within
each text field. The foundation register adds a conventional IAST rendering;
that transliteration is editorial, not another manuscript witness. The raw
text is retained whenever a normalized reading might differ.

The count **3,983** is the number of records in this electronic edition. It is
not an assertion that every edition counts the Aṣṭādhyāyī identically, nor that
every numbered record has identical textual status across recensions.
Alternative numbering, split sūtras and readings need an explicit concordance.
PG1 does not silently reconcile them.

[SOURCE_PINS.json](SOURCE_PINS.json) records the source commit, Git blobs,
SHA-256 digests, record counts and local historical dependencies. A digest
certifies bytes, not philological correctness. The source checkout was used
for inspection; it is not a runtime dependency of the Recognition repository.

## Distinguish text, commentary and our model

| Evidence | Role in PG1 | Attribution boundary |
|---|---|---|
| Aṣṭādhyāyī sūtrapāṭha | Numbered Sanskrit formulations | Pāṇini's text in the pinned electronic witness |
| Māheśvara sūtras | Ordered phonetic material and terminal markers | The grammatical fourteen-sūtra collection; not Vasugupta's work |
| Kāśikāvṛtti | Principal commentary used for the interpretations below | Traditionally Jayāditya and Vāmana; consult the entry under the exact sūtra |
| Mahābhāṣya and vārttikas | Deeper argument, exceptions and textual questions | Patañjali and the vārttika tradition; not interchangeable with the root sūtra |
| Siddhāntakaumudī and later paribhāṣā literature | Derivational organization and interpretive tradition | Later witnesses; record their particular reading when used |
| Publisher's *padaccheda*, *anuvṛtti*, *adhikāra*, expanded reading | Helpful editorial annotations for review | Human annotations; not proof that raw text parses itself |
| T58–T80 and the operator compiler | Explicit finite modern constructions | Their certificates establish their declared computations, not ancient authorship of an algorithm |

For example, the publisher's metadata on 6.1.87 inherits **aci**, not **iki**.
T80 restricts its input to *ik* in its five-rule carrier. That restriction can
be useful in the local model but is not the source text's full inherited
condition. On 3.1.68, *sārvadhātuke* is inherited from 3.1.67; *kartari* gives
a semantic condition. Both must survive a rule-record translation.

## Primary readings actually used

The hyperlinks open the publisher's individual sūtra pages; immutable
commentary bytes are pinned in `sutraani/kashika.txt`. In that file, for
example, key `11062` is 1.1.62 and key `64022` is 6.4.22.

| Sūtra and primary reading | Consequence adopted here |
|---|---|
| [1.1.50, Kāśikā](https://ashtadhyayi.com/sutraani/1/1/50) | Similarity is discussed through place, meaning, qualities and measure. T80's Jaccard score is an authored selection model on specified candidate sets. |
| [1.1.56, Kāśikā](https://ashtadhyayi.com/sutraani/1/1/56) | Sthānivad inheritance has the *an-al-vidhi* restriction; substitution does not copy every property without qualification. |
| [1.1.62](https://ashtadhyayi.com/sutraani/1/1/62) and [1.1.63, Kāśikā](https://ashtadhyayi.com/sutraani/1/1/63) | Entire-affix disappearance and affix-conditioned effects are distinguished from a disappearing segment; lu-marked deletion blocks specified aṅga effects. Neither is a universal memory-erasure rule. |
| [1.1.68](https://ashtadhyayi.com/sutraani/1/1/68) and [1.1.72, Kāśikā](https://ashtadhyayi.com/sutraani/1/1/72) | Literal form versus technical designation and tadanta scope require interpretation, including stated restrictions. |
| [1.3.4](https://ashtadhyayi.com/sutraani/1/3/4), [1.3.8](https://ashtadhyayi.com/sutraani/1/3/8), [1.3.9, Kāśikā](https://ashtadhyayi.com/sutraani/1/3/9) | It designation depends on category and position; there is no rule to remove every final consonant from every suffix. |
| [1.4.2, Kāśikā](https://ashtadhyayi.com/sutraani/1/4/2) | The later rule resolves a conflict of equal strength. This is not a total ordering overriding every exception. |
| [3.1.68, Kāśikā](https://ashtadhyayi.com/sutraani/3/1/68) | Śap occurs after a root before an agent-expressing sārvadhātuka affix; its ś marker supports the sārvadhātuka designation. |
| [6.1.84, Kāśikā](https://ashtadhyayi.com/sutraani/6/1/84) | The ekādeśa scope continues through 6.1.111, before 6.1.112. |
| [6.1.97, Kāśikā](https://ashtadhyayi.com/sutraani/6/1/97) | Preserve *apadāntāt* from 6.1.96 and *pararūpam* from 6.1.94; the reading explicitly relates this rule to 6.1.101 as an exception. |
| [6.4.22, Kāśikā](https://ashtadhyayi.com/sutraani/6/4/22) | Adopt the Kāśikā reading extending through the end of 6.4, including the *bhasya* region, subject to *samānāśraya*. Do not mistake 6.4.129 for a universally agreed stopping point. |
| [8.2.1, Kāśikā](https://ashtadhyayi.com/sutraani/8/2/1) | Tripādī effects are asiddha to earlier rules, also within the Tripādī; commentary discusses saṃjñā/paribhāṣā qualifications. |
| [8.3.15, Kāśikā](https://ashtadhyayi.com/sutraani/8/3/15) | Visarga depends on *khar* or pause; a voiced following sound is not automatically a visarga context. |

On 6.4.22 the publisher's `vasu_english.txt` reports a narrower translation
attributed to Böhtlingk alongside the Kāśikā's longer scope. PG1 selects the
Kāśikā witness and preserves the disagreement as an editorial decision. Its
same-support qualification and exceptions still require rule-by-rule review;
the scope choice alone is not an executable visibility algorithm.

## Lexical and phonetic companions required for grammar

| Companion | What must be represented | Inspected witness; coverage boundary |
|---|---|---|
| Dhātupāṭha | Root identity, upadeśa, gaṇa, meaning, accents/markers, pada and iṭ conditions | Publisher `dhatu/data.txt`, 2,259 electronic records; only the bhū record is selected in the worked trace; other records are not declared linguistically reviewed |
| Gaṇapāṭha | Named lexical groups, members, readings and open/closed-list interpretation | Publisher `ganapath/data.txt`, 262 records; membership cannot be guessed from surface spelling |
| Māheśvara / pratyāhāra material | Positional markers, repeated ha, alternative aṇ endpoints, ordered members and savarṇa rules | Publisher `shivasutra/data.txt`, 14 records; T78–T80 finite results remain separately scoped |
| Śikṣā and prātiśākhya traditions | Articulation, duration, nasalization, accents and recitational conventions | Companion source families identified; no single recitation tradition is declared exhaustive here |
| Uṇādi material | Additional affix traditions and lexical derivation questions | 3.3.1 makes this a real dependency; text collection and rule interpretation remain open |
| Liṅgānuśāsana, lexica, Phiṭ and accent sources | Gender, indeclinables and lexical accent not recoverable from sound alone | Witness selection and concordance remain open |

Counts describe the pinned publisher dataset, not universal canonical counts.
None of these companion inventories is replaced by a hand-picked root list.

## Independent reference routes

- [Sanskrit Library Aṣṭādhyāyī catalogue](https://sanskritlibrary.org/catalogsText/azwADyAyI.html):
  Peter M. Scharf's electronic edition with its own editorial and licensing
  terms. Useful for later collation; not bulk-copied into this packet.
- [Sanskrit Documents Pāṇini resources](https://sanskritdocuments.org/iast/panini.php):
  separate resources for the sūtrapāṭha and accented/unaccented Dhātupāṭha.
- [Gérard Huet's Sanskrit Heritage manual](https://sanskrit.uohyd.ac.in/SKT/manual.html):
  an author's description of an independent morphology/segmentation system.
  It can supply comparison cases later, not a proof that this repository
  implements Pāṇini or that one analyser's output is uniquely correct.

The Śaiva quotations and mathematical interpretations in T78–T79 have their
own source claims. PG1 does not independently certify every quotation there
and does not use them as evidence of Sanskrit grammatical correctness.


## DHATUPATHA.tsv (theorum/144)

ashtadhyayi.com's Dhātupāṭha (2,259 records: code, upadeśa with accent and anubandha marks in SLP1, meaning) as packaged with vidyut-prakriya 0.4.0 (ambuda-org/vidyut, MIT licence; its data README credits ashtadhyayi.com). Pinned: sha256 `bb2013ead0ea536dc7f887164c385c703cb0014ccf6e5af35b87e6d3049ba380` (`proof_lab/ting_rule_table_engine.DHATUPATHA_SHA256`). Read for 7.2.10 (the anudātta mark after the root vowel → aniṭ) and for the root identity of every declared verbal entry.
