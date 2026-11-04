# PG35 — Primary readings and editorial decisions

Author: Monty. 4 November 2026.

## S1. Reproducible source

Primary data: [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data)
at commit `5744762f010d677cfb43f347a42d02796cf615d6`. The literal archive
copies the sūtra text and complete Kāśikā and Vasu English fields for all
313 selected entries, plus the three inherited taddhita foundations.
The source-key map is `(a,p,n) → a + p + zero_pad(n,3)`; e.g. 4.3.168 is
`43168`, not a guessed six-digit key.

[SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json) preserves those fields without
normalization. [SOURCE_PINS.json](SOURCE_PINS.json) pins source-file bytes,
the baseline coverage and native-construction files, the unchanged companion
ledger, and the authored packet. [RULE_REGISTER.json](RULE_REGISTER.json)
links each authored contract to its exact source entry and table location.
Archive inclusion itself earns no coverage credit.

Direct web opens of the two checked ashtadhyayi.com pages were unavailable
to the retrieval service. The source review uses the independently available
local checkout at the exact Git commit, not an assertion that those web
pages were successfully read. Source text and commentaries were compared;
no grammar generator or test supplied the Sanskrit decisions.

## S2. Adopted readings where English/catalogue fields differ

These are examples of consequential discrepancies, not a silently repaired
edition. The original field remains in the archive; the contract uses the
Sanskrit sūtra and Kāśikā reading shown here.

| IDs | Raw field issue / ambiguity | Adopted written decision |
|---|---|---|
|4.2.14–15|English prints अञ् while citing 4.1.83|Residual अण्; 14 retains Kāśikā's qualified uddhṛta/food-vessel sense|
|4.2.20|English opening names दधि|Base क्षीर and affix ढञ्|
|4.2.23|English opening prints ढक् and omits श्रवणा from enumeration|Optional ठक् for all four named full-moon bases|
|4.2.32|English separates द्यावा and पृथिवी|One द्यावापृथिवी unit; six base units, each with छ/यत्|
|4.2.51|English corrupts the third affix|खल→इनि, गो→त्र, रथ→कट्यच्|
|4.2.60|English opening prints ठञ्|ठक्, including the qualified technical उक्थ and non-कल्प सूत्र-final gate|
|4.2.74|English opening still says polysyllabic|The northern-Vipāś well rule also covers shorter bases|
|4.2.75/77|English swaps अण्/अञ् in the opening|75 selects अञ्; 77 explicitly selects अण्|
|4.2.80|Repeated कुमुद gaṇa headings can collapse in a simple map|Keep ordinal 4→ठच् and ordinal 17→ठक्; all seventeen pairs printed|
|4.2.94|English prints व for the first affix|य and खञ्|
|4.2.100|Literal “non-human” could include blankets|Kāśikā's animate human-like non-human restriction; blanket is a negative control|
|4.2.106|English opening corrupts रूप्य|Actual तीर/रूप्य uttara-pada distinction, with अञ्/ञ respectively|
|4.2.126|Catalogue sūtra text has वर्त्त in the last member; Sanskrit examples and commentary identify गर्त|Adopt गर्त for this contract; retain catalogue bytes unchanged|
|4.2.141|English witness gives an inconsistent first place-name|Use Kāśikā आरीहणकीय, preserving the source gaṇa identity|
|4.3.22|English can suggest हैमन्तिक is only Vedic|Kāśikā explicitly also admits ठञ् in bhāṣā; distinguish both अण् histories by त्-lopa|
|4.3.28–30/48/98/125|English repeatedly labels the affix वुञ्|वुन् in these clauses; 27/45/49/99/126 really use वुञ्|
|4.3.41|English's measure wording reverses the Sanskrit exclusion|अवक्लृप्ति and प्रमाणानतिरेक, not measure-exceeding; distinct from birth/existence|
|4.3.69|English negative example repeats a ठञ्-looking form|Kāśikā's control is वासिष्ठी ऋक्; chapter condition retained|
|4.3.81|English construes humans as causes|Kāśikā says मनुष्यग्रहणमहेत्वर्थम्: human branch includes non-cause readings|
|4.3.84|English opening gives य|ञ्य with the Vidūra/Valavāya lexical convention retained|
|4.3.105–111|Some English output spellings lose strengthening or conflate suffixes|Keep source-defined original affix and text gates; use कालाप and कार्मन्द/कार्शाश्व controls from Kāśikā|
|4.3.120|English narrows relation to a short property list|Use Kāśikā's admitted genitive relation with its anabhidhāna control; no universal English “of” parser|
|4.3.139|English opening gives अण् and loses the u-ending condition|उ/ऊ-final base → अञ्|
|4.3.143–154|A blanket “latest rule wins” loses explicit alternatives|Retain कपोतमय/कापोत and लोहमय/लौह; retain member-specific blocking clauses separately|
|4.3.148|English calls व्रीहि barley|Use the exact Sanskrit rice base व्रीहि; do not substitute यव|
|4.3.151|English example uses भूम where Kāśikā has धूम|Short उ condition does not block long ऊ; source control धूममय|
|4.3.159|English calls ढञ् optional|Kāśikā has no continuing वा; female एणी obligatorily selects ढञ् here|
|4.3.164–165|An affix-only summary can miss the blocked लुक्|Specific अण् remains audible by the prescription; ordinary fruit branch still undergoes लुक्|
|4.3.167|Generic लुप् concordance would copy number too|Kāśikā explicitly transfers gender, while number follows the fruits|
|4.3.168|“Elide the affix” has several possible targets|Inner nominal छ/यत् only; preserve outer यञ्/अञ् and root-affix history|

## S3. Boundaries deliberately retained

Kāśikā's ordinary text is the adopted policy; commentary variants are not
free optional branches. At 4.3.27 its reported *kecit* wider saṃjñā scope
is recorded as a separate reading. Gaṇa variants and ākṛtigaṇa extensions
require explicit lexical evidence. The tables sometimes specify only a
source-witnessed subdomain of a broader inherited class; this is why the
metric is **bounded rule reach**, not rule-complete coverage.

Historical statements about ancient/new works, social classes, regions or
promulgators are source predicates in a grammatical construction. They
are not independent historical findings by this project. The late/early
classification at 4.3.105 is therefore supplied from the commentary, not
deduced from current beliefs about the authors.

The pinned catalogue has **3,983 numbered records**. Vasu discusses the
textual status of 4.2.8 and 4.3.132–133 as vārttika-like entries; the archive
keeps that discussion. PG35 follows the same catalogue denominator and
IDs as PG1–34. It does not settle why other editions/counting conventions
report another total, and it does not create a separate grammar.

## S4. Evidence level

Static verification compares exact literal fields, source/file hashes,
rule-table IDs, duplicate-free set unions and local document links.
Those checks establish provenance and accounting, not the semantic truth
of the supplied inputs or implementation correctness. Native proofs are
written domain-relative proofs. Grammar tests, independent generators,
certificate replay and broader runtime suites remain deferred.
