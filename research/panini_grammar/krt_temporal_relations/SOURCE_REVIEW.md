# PG44 — Primary archive and adopted source policies

Author: Monty. 4 November 2026.

Use the immutable [ashtadhyayi-com/data edition](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6),
commit `5744762f010d677cfb43f347a42d02796cf615d6`, with 3,983 catalogue
records. All five primary files are rehashed: `sutraani/data.txt`,
`kashika.txt`, `vasu_english.txt`, `kaumudi.txt` and `nyaas.txt`.
Complete byte lengths, SHA-256 and Git blob IDs appear in [pins](SOURCE_PINS.json).

## S1. Exact reading and archive scope

|Material|Archived fields|Read commentary fields in full|
|---|---:|---:|
|Sūtra text|380|—|
|Kāśikā|380|342|
|Vasu English|380|2|
|Siddhāntakaumudī|52|52|
|Nyāsa|23|23|
|Total literal fields|1,215|419|

The archive covers the complete **355-ID envelope from 3.2.48 through
3.4.38**, plus 25 external controls. All **300 target Kāśikā fields** were
read in full. The remaining full readings are specified by source and ID in
[SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json). There are no inspected empty
fields in this packet. Other archived fields are comparison material, not
claimed as fully reviewed. Reading sets are deduplicated across blocks.

Of 380 archived IDs, **80 are controls** with no new credit. Controls
**3.4.46 and 3.4.48** remain combined gaps; their use as dependencies does
not construct their complete clauses. Literal spelling, HTML, accent signs
and embedded references are preserved without repairs.

## S2. Block decisions

|Source notes|Principal distinctions|
|---|---|
|[A: 3.2.48–130 gaps](SOURCE_NOTES_A.md)|च्वि/ल्युट् policy; metrical अन्तः; niyama scope; recollective past; direct versus replacement affixes|
|[B: 3.2.131–3.3.22 gaps](SOURCE_NOTES_B.md)|Inclusive habitual authority; qualified coexistence; गित्/कित् policy; two role pairings; contextual future participles|
|[C: 3.3.23–98 gaps](SOURCE_NOTES_C.md)|Ordered prefix/root pairs; restricted backward optionality; lexical meaning; dependent क्त्रि/मप्; accent|
|[D: 3.3.99–3.4.38 gaps](SOURCE_NOTES_D.md)|Feminine scope; non-motion extension; relative time; Vedic affix variants; shared actor and following-root requirements|

3.2.66's **अन्तः means within/middle**, not the end: the non-internal ṛk-pāda
clause and the internal हव्यवाट् control have different affix ownership.
Nyāsa, Kaumudī and Vasu corroborate this reading.

3.2.139's adopted **गित्** policy follows the local Kāśikā and Kaumudī
account. Nyāsa reports disagreement, and Kāśikā 7.2.11 declines the necessity
of that analysis. The alternative कित् account has its own obligations.
No unanimous source resolution is claimed. Similar policy distinctions at
3.2.56, 87 and 3.3.49 are retained in their block notes.

3.3.88 uses the explicitly supported following affix **मप्**. The archived
4.4.20 catalogue heading instead prints **मम्**; Kāśikā, Nyāsa and Vasu
support मप् in their bodies. This is a heading/body discrepancy with declared
adopted support, not a silent correction of the catalogue.

3.3.130's non-motion extension follows the explicit Kaumudī/Nyāsa reading
and Kāśikā's examples despite awkward wording in its explanatory sentence.
The differing मन्या/मत्या displays at 3.3.99 and damaged/example-to-affix
assignments at 3.4.9 remain unresolved as stated in D. In particular, the
bounded 3.4.9 suffix inventory does not certify a unique accented paradigm.

## S3. Verification limit

Every table row is transcribed into the register; every archive literal is
compared with the immutable primary field. The 42-pin manifest comprises
five primary, eight predecessor/adapter, one companion and 28 authored-file
identities. The manifest excludes itself. These checks and the sampled
semantic integration review are separate from executable validation.

The [predecessor review](PREDECESSOR_REVIEW.md) retains the older unresolved
readings and records what was rechecked. Full lexical/semantic recognition,
the separate Uṇādi corpus, complete allomorphic/accent realization and runtime
integration remain open. Grammar tests, generators and replay are deferred.
