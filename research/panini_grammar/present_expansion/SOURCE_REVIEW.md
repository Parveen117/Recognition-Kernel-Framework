# PG10 — Source review and local rule domains

Author: Monty. 1 November 2026.

The primary text and attributed commentaries are pinned to
[`ashtadhyayi-com/data` at `5744762f010d677cfb43f347a42d02796cf615d6`](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
[SOURCE_PINS.json](SOURCE_PINS.json) retains eight external file hashes
and 86 historical repository file hashes. The compiler requires each
reviewed Sanskrit wording and every supplied/inherited term to remain
bound. The source verifier also checks literal commentary anchors.

## Twenty-nine bounded records

[RULE_RECORDS.json](RULE_RECORDS.json) gives exact Sanskrit, term bindings,
parameters, local priority edges and attributed evidence for each record.
The groups below describe their implemented domains, not unrestricted
implementations of the named sūtras.

| Rule IDs | Reviewed operation in PG10 |
| --- | --- |
| 1.1.46; 1.3.3; 1.3.9 | Initial placement of īṭ in tiṅ, its final marker and marker lopa |
| 1.1.51 | r-accompaniment of the reviewed replacements of ṛ/ṝ |
| 2.4.72; 2.4.75; 6.1.10 | Retained śap-luk or śap-ślu, and copying the admitted consonant-initial one-vowel roots |
| 7.4.59; 7.4.60 | Shortening the copy vowel and deleting its later consonants |
| 7.4.75–77 | Copy guṇa for nij/vij/viṣ and lexical copy i for bhṛ/māṅ/hāṅ/pṝ/pṛ |
| 6.4.112; 6.4.113; 6.4.115; 6.4.116 | Weak non-ghu ā changes and the separate bhī/hāk options |
| 7.1.102; 8.2.77 | Weak pṝ to ur, with subsequent lengthening before a consonant |
| 7.3.89; 7.3.90; 7.3.95 | Non-abhyasta u-vṛddhi after luk, ūrṇu's option and ru/tu/stu īṭ |
| 6.1.77; 6.1.78; 6.1.101; 6.4.77; 6.4.82 | Reviewed vowel junctions, joint ā, iy/uv and cluster-sensitive i-to-y |
| 8.2.30; 8.3.59; 8.4.54 | Newly scoped consonant readout contracts and copy deaspiration |

The 8.2.30 and 8.3.59 definitions explicitly admit the new lexical domains;
the frozen PG7 records are not edited or silently broadened. Other
inherited contracts are used only where their existing domain applies.

## Copy and root remain distinct

Ślu is the trigger for copying; luk is not interchangeable with it. The
copy retains a source link for every original sound. For hrī, deleting r
from the copy leaves the root-internal hr cluster intact. The h-to-jh
operation precedes the copy's later deaspiration. The cluster condition
of 6.4.82 is evaluated inside the root, while its multiple-vowel condition
uses the whole aṅga. Thus bhī has `bibhyati`, whereas hrī has `jihriyati`.

The Bālamanoramā on 7.4.77 explicitly takes the copy's ṛ replacement
through r-accompaniment and halādiśeṣa. PG10 therefore records i+r and
then deletes that r from the copy. It does not replace the entire history
with a direct ṛ-to-i output. Root guṇa remains a separate operation.
7.4.76's three-root restriction admits bhṛ, māṅ and hāṅ; it does not admit
the distinct hāk root whose strong output is `jahāti`.

Long pṝ and short pṛ are separate pinned entries, even though they share
a meaning and some strong forms. In weak pṝ, 7.1.102 and 1.1.51 give ur;
8.2.77 lengthens u only before a consonant, producing `pipūrtaḥ` but
`pipurati`. The Kāśikā's local priority discussion gives guṇa precedence
over the i/u replacement in strong contexts. Short pṛ therefore retains
its own weak forms, such as `pipṛtaḥ` and `piprati`.

6.4.115 supplies bhī's optional short i only in the inherited weak,
consonant-initial domain. 6.4.116 gives hāk's separate short-i option
alongside the long ī of 6.4.113. Before a vowel, the non-ghu ā roots take
the reviewed 6.4.112 lopa. Class-2 mā and dāp have neither collective
abhyasta nor these lexical identities and cannot inherit this pathway.

## Ending ownership and īṭ ordering

Two new scope overlays supplement the frozen views:

| Target | Supplied inheritance | Attribution |
| --- | --- | --- |
| 7.3.89 | न and अभ्यस्तस्य from 7.3.87 | Kāśikā and Siddhāntakaumudī preserve the prohibition for abhyasta |
| 7.3.95 | तिङि from 7.3.88 | Bālamanoramā explicitly carries the tiṅ condition |

7.3.95's repeated sārvadhātuka admits apit endings; a pit requirement
would wrongly remove stu's ātmanepada alternatives. The implementation
still requires the exact ru/tu/stu lexical identity, sārvadhātuka tiṅ and
an actual consonant-initial ending. Other roots in the sūtra are not
claimed by this bounded record.

The Bālamanoramā resolves the plural ending before the īṭ query. Once jhi
has become vowel-initial anti, it cannot receive this hal-conditioned
augment. Where īṭ is admitted, its ī is the first visible sound of the
augmented ending. The ṭ is retained only as marker evidence, and the
ordered constituent is `[īṭ, tiṅ]`. Neither unit is reclassified as part
of the root or aṅga.

Consequently īṭ removes the consonant-initial condition of 7.3.89 before
that rule is queried. In a strong ru cell, guṇa gives o and 6.1.78 gives
av before ī: `ravīti`. The unaugmented branch retains `rauti`. Weak cells
use uv instead, as in `ruvītaḥ`. Ūrṇu has its own 7.3.90 guṇa/vṛddhi
option and does not borrow īṭ. These are explicit local ordering and
priority contracts, not a general conflict scheduler.

## Readout and source evidence limits

The new readout copies the retained morphological state and applies
ordered phonetic phases. The root-owned ur of pṝ lengthens locally;
copy deaspiration targets copy owners alone. In `prānti`, 8.3.24 removes
the dental n before the ṇatva query, and 8.4.58 restores dental n later.
The later result cannot feed the earlier query again. This is a reviewed
local schedule, not a general solution to asiddha.

[REFERENCE_CASES.json](REFERENCE_CASES.json) contains 153 whole-word
Devanāgarī witnesses in the selected primary commentary passages and 35
refusal cases. Candidate slots were located using the pinned comparison
table; admission as a word witness additionally requires a literal
whole-word match in the cited primary passage. This procedure is stated
explicitly and is not an independent random sample of Sanskrit usage.

The six entries without a separate full-word witness are:

| Lexical ID | Entry | Evidence present |
| --- | --- | --- |
| 1020036 | ṣu, प्रसवैश्वर्ययोः | Pinned lexical identity, reviewed rule contracts and nine-cell comparison |
| 1020037 | ku, शब्दे | Same evidence layers |
| 1020048 | śrā, पाके | Same evidence layers |
| 1020052 | rā, दाने | Same evidence layers |
| 1020054 | dāp, लवने | Same evidence layers |
| 1020056 | prā, पूरणे | Same evidence layers |

The Vedic `dāti` discussed at 2.4.76 is not used as evidence for the
different dāp-in-cutting entry. Tu's source annotation `सौत्रः` is retained;
its classical present treatment is supported by the Siddhāntakaumudī
passage cited in the lexical packet. All 12 tagged class-3 entries remain
outside this implementation, including the vowel-initial ṛ entry whose
classical-use discussion requires a distinct copying review.

Vidyut agreement is a separate implementation comparison. It neither
fills missing literal witnesses nor establishes unrestricted soundness.
The native operator carrier, its admitted grammatical operators and the
typed zero-specialization compatibility proof remain open constructions.
