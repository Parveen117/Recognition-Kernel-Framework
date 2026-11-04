# PG41 — Source decisions and literal archive

Author: Monty. 4 November 2026.

The primary edition is [ashtadhyayi-com/data at 5744762](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
[SOURCE_PINS.json](SOURCE_PINS.json) records exact byte counts, SHA-256 and
Git blob identities. All four primary files used here—catalogue, Kāśikā,
Vasu and Kaumudi—were retrieved and independently rehashed.

[SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json) preserves 406 literal sūtra
fields, 406 Kāśikā fields, 406 Vasu fields and 15 selected Kaumudi fields:
**1,233 fields**. There are 391 contract IDs and 15 uncredited controls.
No normalization is applied inside these source strings. All 391 operative
Kāśikā fields and the selected controls were read; additional commentary
reading was targeted. Archiving every Vasu field is not a claim of independent
line-by-line adjudication of every English sentence.

## S1. Text and numbering corrections

|Entry|Literal issue|Adopted treatment|
|---|---|---|
|7.4.84|K contains damaged चनीइकस्यते among examples|Retain literal field; use unambiguous lexical admission and other witnesses; no invented paradigm from damaged token|
|7.4.87|K has पञ्चूर्यते / पञ्चूरीति for चर्|Use चञ्चूर्यते / चञ्चूरीति supported by 7.4.88 and Vasu 7.4.87; keep augmentation and root-vowel change separate|
|8.2.35|K prose gives धकारादेशः although sūtra says आहस्थः|Adopt थ्, supported explicitly by Vasu and by the sūtra; derive आत्थ through subsequent चर् treatment|
|8.3.15|K's last sentence says visarga occurs in नार्कुट/नार्पत्य, omitting the expected negative|Vasu explicitly says it does not; preserve K and adopt the negative control|
|8.1.26|Vasu's final English restatement reverses the preceding अन्वादेश analysis|Use the two Sanskrit commentary policies; do not adopt the reversed summary as a third rule|
|8.2.106|Vasu opening names ए/ओ, while sūtra and explanatory body concern ऐ/औ|Adopt ऐ/औ; duration alternatives remain a genuine analysis difference|
|8.4.51|K prints बह्मा in the no-duplication examples|Use ब्रह्मा in authored explanation; preserve literal field|
|8.2.86|K quotes प्रत्यभिवादेऽशूद्रे with number 8.2.86|Text corresponds to pinned 8.2.83; do not follow self-reference mechanically|
|8.3.28, 101 and related prose|सात्पदाद्योः is quoted as 8.3.109|Pinned catalogue locates it at 8.3.111|
|8.3.98|सेधतेर्गतौ is quoted as 8.3.111|Pinned catalogue locates it at 8.3.113|
|8.3.110|पूर्वपदात् is quoted as 8.3.104|Pinned catalogue locates it at 8.3.106|

These are explicit local mappings, not a universal numeric offset. IDs in
the register follow the pinned catalogue. Literal references inside archived
commentaries retain their original numbers.

## S2. Policies that remain distinct

|Boundary|Required policy or qualification|
|---|---|
|8.1.12|The sūtra's quality-resemblance rule and the commentary's order, alarm, sound imitation and reciprocal extensions have separate admission tags|
|8.1.26|One view restricts the local option to अनन्वादेश; another allows general अनन्वादेश options and uses the local rule even in अन्वादेश. Kaumudi supports the latter extension|
|8.1.44|One view protects only the verb directly linked to किम्; another extends the relation to the full questioned alternative. Preserve the selected scope|
|8.1.55|Exactly one intervening पद is required; the commentary differs on distance, एकश्रुति and pluti interaction. A prefix is relevant to counting|
|8.2.1–3 and 8.4.21|Named visibility exceptions do not make every tripādī operation available to every earlier copy operation|
|8.2.4|Direct यण्-derived स्वरित and a स्वरित produced by 8.4.66 have differing treatment; the cited recensional reading is retained separately|
|8.2.19–21|प्रति reach and swallowing-versus-praising root interpretation remain source-policy boundaries|
|8.2.25|The adopted सिच् domain and the broader Bhāṣya discussion are separate; the broad reading needs an additional ordinary-word boundary account|
|8.2.62|The root licensed for क्विन् can carry कुत्व under other affixes, but the source itself flags रज्जुसृड्भ्याम् as requiring further treatment|
|8.2.80|Double-द् अद्रि cases admit both-target, final-neighbor-only, or restricted त्यदाद्यत्व analyses. Kaumudi also explicitly maps a consonant target to short उ|
|8.2.83–92|Greeting and ritual formulas retain source roles, utterance placement and attestation; no unrestricted productive pluti rule is inferred|
|8.2.106–107|Three-mora-total and four-mora ऐ/औ are separate analyses. Kaumudi explicitly selects four; this packet requires a declared convention|
|8.3.5/6/12|रु and direct-स् accounts retain distinct histories while excluding unwanted visarga branches in the selected forms|
|8.3.18–20|Attenuated pronunciation, deletion and a fully audible semivowel are distinct; the ओ + य् passage itself has two analyses|
|8.3.45/48|Nested-compound सर्पिष्कुण्डिका has conflicting lexical-extension treatment; no blanket exception is inferred|
|8.3.58 versus 8.4.2|The first allows individual listed interveners; the second permits their combinations. नुम् in the latter denotes audible anusvāra; 8.4.32 uses the same qualification|
|8.3.79|With intervening युट्, analyses differ over whether इट् must immediately follow the अङ्ग or merely an इण् sound|
|8.4.3|Source presents restrictive and new-license accounts of compound णत्व; both retain named semantic and structural boundaries|
|8.4.19–20|The पर्यनिति / पर्यणिति issue depends on the selected near-trigger interpretation|
|8.4.47–52|Commentary extensions give alternate directions for यण्/मय् and शर्/खय् duplication; teacher-specific no-duplication policies remain separate|
|8.4.63|Kaumudi explicitly qualifies the झय् trigger as पद-final; अम् extension remains separately labelled|
|8.4.68|Short अ pronunciation returns to संवृत while its earlier grammatical view remains विवृत; long/pluta excluded|

The rule tables retain further lexical restrictions and negative controls.
An open गण, a बहुल passage or a named Vedic witness does not justify an
unbounded lexicon. Literal source disagreement is neither silently repaired
nor converted into free grammatical optionality.

## S3. Evidence boundary

All 1,233 archived fields are byte-preserving string matches against the
four retrieved, pinned primary files. This verifies transcription, not the
truth of every interpretation. [Predecessor review](PREDECESSOR_REVIEW.md)
separately records that the older Nyāsa file could not be downloaded this
turn; its nine PG40 fields are inherited and were not independently
recompared. No new PG41 contract relies on an unretrieved Nyāsa field.
