# PG43 — Source review and adopted policies

Author: Monty. 4 November 2026.

## S1. Immutable source and scope of reading

Use the 3,983-record catalogue and commentary files at
[ashtadhyayi-com/data, 5744762f](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
The five source files are `sutraani/data.txt`, `kashika.txt`,
`vasu_english.txt`, `kaumudi.txt` and `nyaas.txt`. Their complete immutable
bytes, SHA-256 hashes and Git blob identities are rechecked and recorded in
[SOURCE_PINS.json](SOURCE_PINS.json). Live navigation links are not edition pins.

|Archived literal material|Fields|
|---|---:|
|Sūtra texts|442|
|Kāśikā|442|
|Vasu English|442|
|Siddhāntakaumudī|28|
|Nyāsa|9|
|Total|1,363|

The archive contains the complete **393-ID envelope from 2.2.1 through
3.2.47** plus **49 external controls**. There are 300 new contracts and
**142 controls with no new coverage credit**. Ten controls absent from PG42's
combined union remain gaps: **3.2.188; 3.3.11, 59, 69, 102; 3.4.47, 59, 66,
76, 117**. Importing or discussing their source text does not construct them
fully or add them to the coverage union.

All **300 target Kāśikā fields** were read in full. One, 2.4.28, is misassigned;
**299 supply operative Kāśikā support**. Selected controls were also read.
Additional targeted readings are:

- **Kaumudī, 28:** 2.2.7, 11, 19, 20, 32, 33, 35; 2.3.17, 51, 58, 59, 66;
  2.4.12, 28, 35, 67, 69, 80, 81; 3.1.6, 13, 27, 62, 65, 90, 103, 110, 112.
- **Nyāsa, 9:** 2.2.7; 2.3.17; 2.4.12, 28, 80, 81; 3.1.13, 90, 103.
- **Vasu, 5:** 2.2.7; 2.4.28, 80, 81; 3.1.103.

Kaumudī 3.1.5 and Nyāsa 2.4.69 were inspected but are empty; neither is counted.
Other imported Vasu fields are archived comparison material, not a claim of
complete independent review. Literal spelling, accent marks, HTML and embedded
references remain unchanged in [SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json).

## S2. Misassigned Kāśikā 2.4.28

The pinned field at key `24028` discusses **अपोनप्तृ/अपान्नप्तृ, छ and deity
affixes**, with additional पैङ्गाक्षीपुत्र/शतरुद्र material. This corresponds
to the subject of **4.2.28 छ च**, which is archived as a control. The two
fields are not byte-identical; this is a subject mismatch, not a claimed exact
duplicate. It cannot support the actual 2.4.28 Vedic compound-gender rule.

Kaumudī, Nyāsa and Vasu support first-member gender for **हेमन्तशिशिर** and
**अहोरात्र** in छन्दस्. Nyāsa distinguishes the ordinary last-member gender
rule and the masculine रात्र compound prescription. Vasu also explains that
the displayed dual is not a restriction to dual inflection.

Adopt that qualified gender clause. Mark Kāśikā 2.4.28
`MISASSIGNED_NONOPERATIVE_LITERAL_FIELD` in the archive, and list it among
inspected nonoperative sources in the register. Do not repair the pinned
source or claim manuscript collation. The mismatch remains a source-data
obligation; it does not leave the adopted clause without declared support.

## S3. Lexical and number distinctions resolved by Nyāsa

**2.2.7, ईषत् and apparently kṛt words.** The source restricts the compound to
non-kṛt quality expressions, yet displays पीत/उन्नत forms. Nyāsa explicitly
treats these witnesses as underived lexical qualities in this use. Retain that
analysis rather than erasing the non-kṛt gate or accepting every derived
participle. गार्ग्य remains the negative quality-control example.

**2.3.17, contempt with मन्यते.** The required root is the दैवादिक formation,
not तानादिक मन्वे. Nyāsa and Kaumudī explain the व्यवस्थित option through
the stated lexical exclusions: नौ, काक, अन्न, शुक and शृगाल do not acquire
dative, while श्वन् may. The comparison object is addressed separately from
the person compared; त्वाम् does not gain dative by being another object.

**2.4.12, बहुप्रकृति.** Nyāsa states plural-denoting or plural-inflected
constituent inputs. It is not a count of lexical member nodes. Kaumudī's
बदराणि + आमलकानि example makes this visible: two written member names can
produce बदरामलकम्, whereas the two-item बदरामलके stays outside that condition.
The same-class restrictions, exact अश्ववडव pair and other source conditions
remain in force.

**3.1.13, लोहितादि.** Kāśikā and Nyāsa explicitly move the other listed
नीलादि words to the भृशादि क्यङ् analysis. लोहित and डाच् forms retain क्यष्,
as do properly admitted unlisted analogical members such as वर्मन्. The short
Kaumudī field does not discuss this list correction. Do not flatten the printed
gaṇa into one suffix assignment or treat analogical membership as automatically
known. This packet does not rewrite the separate Gaṇapāṭha dataset.

## S4. Distinct deletion and grammatical-view owners

**2.4.80.** Nyāsa explicitly derives अक्षन् by deleting **च्लि** and explains
that returning from the inherited सिच् wording prevents a सिच्-specific effect
such as **6.1.187**. The final finite ending is not globally erased. Kaumudī
also preserves a qualified non-deletion witness, अजनिष्ट, and the Brāhmaṇa
extension of the stated register. Vasu's broad historical gloss of लि is not
adopted as a universal deletion instruction.

**2.4.81.** Nyāsa requires the actual prescribed आम् affix. Its following
primary लिट् position differs from the auxiliary's own लिट्. जगाम, शशाम and
the homonymous root आम् are explicit controls against substring matching.

**3.1.90.** Kaumudī restricts the paired श्यन्/P choice to the **यक् domain**.
Nyāsa identifies the excluded लिङ् example as **आशीर्लिङ्**, and explains
स्यादि through स्य/तासि and the other stated environments. Therefore do not
block ordinary विधिलिङ् merely from the bare name लिङ्; nor generalize the
P choice to future, perfect or the cited aorist. The two operations remain a
coupled clause, with the ordinary यक्/A alternative distinct.

**3.4.117 control.** Kāśikā's उपस्थेयाम example invokes सार्वधातुक behavior
for one consumer and आर्धधातुक behavior for another. Preserve source-qualified
consumer views rather than forcing one exclusive global designation. This
control remains an uncovered ID in the combined catalogue.

## S5. Commentary policies not silently merged

|ID|Policy boundary retained|
|---|---|
|2.3.66|शेषे विभाषा limited to other feminine affixes in one analysis, broader optionality in another|
|2.4.67|Kāśikā limits गोपवनादि to eight members and rejects the overextended हरितादि reading|
|2.4.69|Kāśikā keeps 68's obligatory deletion for three overlapping pairs; Kaumudī displays optional retained forms for those pairs|
|3.1.58|Primary ग्लुञ्च् nasal-loss treatment and explicitly reported no-loss अग्लुञ्चत् analysis remain separate|
|3.1.137|Prefix-required श formation and the reported prefix-free पश्य reading have distinct source policies|

For 2.4.69, the authored default is the Kāśikā boundary: the three pairs
**उपक–लमक, भ्रष्टक–कपिष्ठल and कृष्णाजिन–कृष्णसुन्दर** retain their 68
condition. Kaumudī's optional examples are preserved as an alternative policy,
not harmonized by inventing a new sense restriction. Its variant spellings
also remain literal in the archive. Unknown policy yields Open where the
choice affects the result.

## S6. Accent and editorial references

**3.1.103.** Kāśikā's displayed accented अर्य examples reverse the distinction
stated by its own explicit vārttika. Nyāsa clearly assigns **initial उदात्त to
वैश्य and final उदात्त to स्वामिन्**; Vasu confirms the latter exception to
6.1.213. Adopt that reading and retain the conflicting source display literally.
Identical unaccented spellings do not merge the two histories.

**2.3.10.** Retain PG42's local correction: the अप/परि exclusion belongs to
**1.4.88**, while **1.4.89** concerns आङ्. The incorrect embedded reference
does not establish a global numbering offset. **3.1.122** also contains an
embedded `2.1.122` verse reference; the local field and subject are 3.1.122,
not a new entry beyond the pinned 2.1 catalogue.

Minor damaged renderings remain literal. Authored examples use legible source
witnesses and the prescribed lexical/affix identities; no repaired archive or
new paradigm count is inferred from normalized display. The full source lists,
vārttikas and historical illustrations likewise do not grant automatic
implementation or scientific-truth status.

PG42's extra **तिरस्कृत्वा** at 1.4.72 remains unresolved. Neither the new
compound rules nor this source audit closes it. See
[Predecessor review](PREDECESSOR_REVIEW.md) and [Handoff](HANDOFF_AND_WORK.md).
