# PG2 — Source reading of the missing metarules

Author: Monty. 1 November 2026.

This review distinguishes Pāṇini's sūtras, Kāśikā explanations, later
commentarial qualifications, and authored executable contracts. A JSON
record expresses a supplied interpretation; matching it against examples
does not prove that interpretation universally or derive it from the text.

## It-saṃjñā: all seven rules, with explicit teaching units

| Sūtra | Sanskrit | Reviewed condition |
|---|---|---|
| [1.3.2](https://ashtadhyayi.com/sutraani/1/3/2) | उपदेशेऽजनुनासिक इत् | Nasal vowel in upadeśa; ordinary nasal pronunciation is excluded. Conventional nasality must be supplied, not guessed from an unmarked printed form. |
| [1.3.3](https://ashtadhyayi.com/sutraani/1/3/3) | हलन्त्यम् | Final consonant of the original teaching unit, subject to the following prohibition. |
| [1.3.4](https://ashtadhyayi.com/sutraani/1/3/4) | न विभक्तौ तुस्माः | Protect dental-varga consonants, s and m in vibhakti. This does not protect the p of tip. Kāśikā explicitly qualifies the prohibition for `at` in 5.3.12 and 3.4.106. |
| [1.3.5](https://ashtadhyayi.com/sutraani/1/3/5) | आदिर्ञिटुडवः | Initial **ñi, ṭu, ḍu** as compound markers, not arbitrary deletion of initial ñ/ṭ/ḍ or interior occurrences. |
| [1.3.6](https://ashtadhyayi.com/sutraani/1/3/6) | षः प्रत्ययस्य | Initial ṣ of an affix; not every ṣ in a word or affix. |
| [1.3.7](https://ashtadhyayi.com/sutraani/1/3/7) | चुटू | Initial palatal/retroflex varga sound of an affix, with the named Kāśikā exceptions cuñcup, caṇap and ṭīṭañ. |
| [1.3.8](https://ashtadhyayi.com/sutraani/1/3/8) | लशक्वतद्धिते | Initial l, ś or velar-varga sound of a non-taddhita affix. Category and teaching identity must be retained. |

The records keep the **prohibition** 1.3.4 distinct from the designating rules.
Only after designation does 1.3.9 project away the selected sound identities.
The interpreter never runs `halantyam` again on the projected string.

Important positive and adverse cases are supplied in `ORACLE_CASES.json`:

- `गमॢँ → gam`: original-final nasal vocalic ḷ is a marker; the exposed m
  is retained. `ḍukṛñ` preserves the marker unit `ḍu`, not a standalone u-it.
- `jas → as`: initial j is designated, final s is protected. `yat → ya`
  has no vibhakti protection. `at` requires its source identity to apply
  the two explicitly stated exceptions.
- `cuñcup`, `caṇap`, `ṭīṭañ` retain their initial consonant under the
  Kāśikā's named qualification. In `aṭhac`, an interior retroflex is not
  an initial marker. In `ṭiṣac`, the interior ṣ is retained.
- `lyuṭ → yu`, `śap → a`, `kta → ta`; taddhita `lac`, `śa`, `kan`
  retain the l/ś/k that 1.3.8 would otherwise designate.
- `jhi → i` is an **it-only projection**, not its eventual realized ending.
  The identity jhi survives for the subsequent 7.1.3 substitution. Thus
  marker erasure cannot be the sole representation of an affix.

### Two qualifications beyond a literal seven-rule transcription

**Technical lakāras.** Tattvabodhinī on
[3.4.77](https://ashtadhyayi.com/sutraani/3/4/77) explicitly denies
it-designation of the technical l. Bālamanoramā on
[3.2.123](https://ashtadhyayi.com/sutraani/3/2/123) identifies a and ṭ as
markers. With the supplied conventional teaching form `लँट्`, the review
retains l; printed `लट्` without the required nasality evidence remains
`UNRESOLVED`. Neither the l exception nor the nasal annotation is invented
by the tokenizer. This is an attributed later reading, not an additional
Pāṇini sūtra.

**Compound ir.** Kāśikā on
[7.1.58](https://ashtadhyayi.com/sutraani/7/1/58) cites the supplementary
instruction **इरितां समुदायस्येत्संज्ञा** and explicitly says it does not
make the root independently *idit*. In the source data:

| Lexical ID | Teaching form | Marker unit | It-only projection | Publisher headword |
|---|---|---|---|---|
| 1010067 | भिदिँ | i | bhid | भिन्द् |
| 1070002 | भिदिँर् | ir | bhid | भिद् |

The first needs num treatment under 7.1.58; the second must not acquire
standalone i-it merely because the letter i occurs inside ir. There are 27
nasal-i+r teaching forms in the pinned root witness. The supplemental record
uses that supplied pattern and preserves a compound unit. Its two letters
are not independently reclassified as i-it/r-it in the ledger.

This is why the 1,703 exact marker-only headword matches are not 1,703 proven
root derivations. Even identical projections can have different grammatical
consequences. The supplement does not claim an exhaustive catalogue of all
vārttikas, recitational conventions or exceptional markers.

## Sthānivad 1.1.56–59: restricted inheritance

| Sūtra | Contract supported by the reviewed Kāśikā |
|---|---|
| [1.1.56 स्थानिवदादेशोऽनल्विधौ](https://ashtadhyayi.com/sutraani/1/1/56) | A substitute can retain sthānin-dependent grammatical treatment outside the specified sound-dependent operations. Examples include root, aṅga, kṛt, taddhita, avyaya, sup, tiṅ and pada status. |
| [1.1.57 अचः परस्मिन् पूर्वविधौ](https://ashtadhyayi.com/sutraani/1/1/57) | For the reviewed phonological extension: a vowel substitute, caused by a following condition, with the queried operation on the preceding portion. `parasmin` is causal locative; `pūrvavidhau` is the operation's domain. |
| [1.1.58 न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु](https://ashtadhyayi.com/sutraani/1/1/58) | Qualified prohibitions on the preceding extension. They cannot be implemented by an unqualified flat blacklist. |
| [1.1.59 द्विर्वचनेऽचि](https://ashtadhyayi.com/sutraani/1/1/59) | Original-form treatment of a vowel substitute for morphological reduplication under its vowel-initial reduplication trigger. This restoration has a limited lifetime. |

Kāśikā 1.1.56 gives as → bhū and brū → vac as retaining root treatment,
and ktvā → lyap as retaining kṛt treatment. This supports typed continuity;
it does not imply that all phonetic properties of the original are copied.

For 1.1.57, *paṭayati* and *avadhīt* illustrate retained-original treatment
that blocks inappropriate vṛddhi. *Praśna* supplies a consonant-original
negative case; *yuvajāni* lacks the following-cause condition; *he gauḥ*
lacks the relevant preceding-operation condition. The locatives therefore
cannot all compile to an undifferentiated “right-hand context.”

The 1.1.58 controls cover padānta, phonetic doubling, y-lopa, accent,
savarṇa, anusvāra, lengthening, jaś and car operations. **Vare** concerns
the vowel replacement made in the varac context, illustrated by
*yāyāvara*; it is not simply another output-operation name.

The closing Kāśikā sentence explicitly restricts **svara/dīrgha/y-lopa**
noninheritance to a **lopa substitute**. The text then contrasts nondeletion
substitutes with *bahukhaṭvaka, kiryoḥ, giryoḥ, vāyvoḥ*. The records and
negative cases retain this distinction. Calling every replacement a
deletion would invalidate that reading.

For 1.1.59 the examples include *papatuḥ, cakratuḥ, ninaya*. The review
requires the vowel-initial element to be the **reduplication trigger**:
*dudyūṣati* and *jeghrīyate* demonstrate why a vowel somewhere in the
derivation is insufficient. The *jagle* control rejects permanent
restoration after the reduplication query. Actual replacement history is
unchanged by every review query.

The 26 cases check these local judgments. They do not generate all these
words, automatically derive their grammatical annotations, or establish
the classification of every possible operation under the four sūtras.

## Priority: conditional, attributed evidence

Kāśikā on [1.4.2](https://ashtadhyayi.com/sutraani/1/4/2) explicitly frames
vipratiṣedha as an equal-strength conflict. PG2 therefore has **no default
numeric fallback** when strength, scope or the exception relation is unknown.

The reviewed record-level witnesses are:

| Winner / competing rule | Premises | Evidence |
|---|---|---|
| 6.1.97 / 6.1.101 | a before guṇa, apadānta | Kāśikā 6.1.97 explicitly calls it an exception to savarṇadīrgha; *pacanti*. |
| 6.1.97 / 6.1.88 | a before guṇa, apadānta | Same commentary contrasts expected vṛddhi in *pace*. This also shows why a tiny a+a sample cannot define the exception domain. |
| 6.1.109 / 6.1.78 | padānta e/o before short a | Kāśikā explicitly calls pūrvarūpa an exception to ay/av; *agne'tra*, *vāyo'tra*. |
| 3.1.77 / 7.3.86 | reviewed tud + sārvadhātuka case, śa pending | Paribhāṣenduśekhara 42 explicitly uses *tudati* for nitya before later guṇa. Kāśikā 3.1.77 identifies **śa**, not śap. The light-upadhā guṇa ID is identified from 7.3.86; 1.2.4 and 1.1.5 explain the subsequent restriction. |

The last witness is a source example with an attributed rule-ID
interpretation, not a generic derivation of nityatva from two booleans.
Changing the root to an unreviewed case returns `UNRESOLVED`.

The later **Paribhāṣenduśekhara of Nāgeśa** is kept separate from Pāṇini's
sūtras. Numbers below refer to this pinned publisher witness:

| Number | Consequence for verification |
|---|---|
| 42 | Nitya can outrank a later rule. |
| 43–45, 49 | Same-word/target, licensing condition and accent matter. In the source's *nyaviśata* example, aṭ operates on the dhātu before vikaraṇa but on the vikaraṇa-ending unit after it. Reusing the name “aṭ” does not establish an unchanged event. |
| 50 | Bahiraṅga is asiddha relative to antaraṅga; the discussion concerns the relation between phonological conditioning constituents and explicitly rejects a blanket classification of every meaning-conditioned operation as bahiraṅga. |
| 51 | Vowel adjacency qualifies the bahiraṅga account. |
| 57–58 | Apavāda can outrank antaraṅga, but the particular bādhaka relation must be established. |
| 59 | Even the blanket claim “an exception always suppresses its general rule” needs qualification. |

Identity controls in `verify.py` reject the specific naive nitya shortcuts.
They are not a complete nitya algorithm. General antaraṅga/bahiraṅga
inference, the T66 *edhe* ordering, alternative traditions and all optional
outcomes remain **open**, with no fabricated total ranking.

## Source identity

The canonical retrieval identity is
[`ashtadhyayi-com/data@5744762`](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
The exact files are `sutraani/data.txt`, `sutraani/kashika.txt`,
`sutraani/balamanorama.txt`, `sutraani/tattvabodhini.txt`,
`dhatu/data.txt` and `paribhashendushekhar/data.txt`.
Every executable reference case has a key and literal anchor in those files;
their hashes are pinned separately from the authored interpretation. The
source website is useful for reading; the pinned bytes determine this review.
