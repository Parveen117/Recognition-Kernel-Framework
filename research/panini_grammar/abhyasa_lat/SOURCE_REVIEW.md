# PG9 — Source interpretation and local order

Author: Monty. 1 November 2026.

Primary source bytes are pinned to ashtadhyayi-com/data commit
`5744762f010d677cfb43f347a42d02796cf615d6`. The Sanskrit sūtra catalogue,
Dhātupāṭha identities and Kāśikā, Siddhāntakaumudī, Bālamanoramā,
Tattvabodhinī and Laghukaumudī witnesses remain separate from Vidyut's
generated forms. [SOURCE_PINS.json](SOURCE_PINS.json) retains all earlier
pins and freezes the PG8 files at `7ef51011b4ac8bfe22fc6e4261545fa1fc85f1f2`.

## Sixteen bounded contracts

| Sūtra | Admitted reading |
| --- | --- |
| 1.1.20 दाधा घ्वदाप् | The identified डुदाञ् and डुधाञ् are ghu; no general recognition by surface spelling |
| 2.4.75 जुहोत्यादिभ्यः श्लुः | śap is wholly deleted with ślu identity retained, providing the reduplication condition |
| 6.1.1 एकाचो द्वे प्रथमस्य | The selected first one-vowel span is the whole pre-strength CV root in these three entries |
| 6.1.4 पूर्वोऽभ्यासः | The earlier of the two occurrences is abhyāsa |
| 6.1.5 उभे अभ्यस्तम् | The pair is collectively abhyasta, not two independently designated stems |
| 6.1.10 श्लौ | ślu licenses copying the non-abhyāsa root; vowel-initial and second-span alternatives are not admitted |
| 6.4.87 हुश्नुवोः सार्वधातुके | hu's final u becomes v before vowel-initial sārvadhātuka, with multiple vowels in the whole aṅga and no cluster before u |
| 6.4.112 श्नाऽभ्यस्तयोरातः | Final ā of the abhyasta aṅga is deleted before sārvadhātuka kit/ṅit; actual apit tiṅ has the retained 1.2.4 ṅitvat designation |
| 6.4.113 ई हल्यघोः | The non-ghu condition excludes ī in दत्तः and धत्तः, so weak ā-lopa still applies before consonants |
| 7.1.4 अदभ्यस्तात् | Affix jh after abhyasta receives at, the stated exception to ant |
| 7.4.59 ह्रस्वः | Copied ā becomes a; the original root's ā remains separately owned |
| 7.4.60 हलादिः शेषः | The single initial consonant remains; these CV copies require no consonant deletion |
| 7.4.62 कुहोश्चुः | Copied h becomes jh, as Bālamanoramā explicitly resolves the aspirated palatal choice |
| 8.2.38 दधस्तथोश्च | Reduplicated, jhaṣ-final dhā receives abhyāsa d→dh before t/th, s or the dhv sequence |
| 8.2.40 झषस्तथोर्धोऽधः | The t/th→dh operation excludes dadhāti lexically; other dh-final roots are not excluded |
| 8.4.54 अभ्यासे चर्च | The admitted copied voiced aspirates become their jaś sounds: jh→j and dh→d |

Earlier reviewed tiṅ designation, 7.3.84 guṇa, 1.1.5 inhibition, 3.4.79/80,
8.2.66, 8.3.15, 8.3.59, 8.4.53 and 8.4.55 supply the remaining operations.
Hu's u before m/v belongs to the root. Kāśikā 6.4.107 expressly requires
pratyaya ownership for optional u-lopa, so that PG6 operation cannot be
borrowed to create additional hu variants.

## Eight attributed scope overlays

The raw publisher annotations remain untouched. Each overlay and every
retained own/inherited term is bound in [RULE_RECORDS.json](RULE_RECORDS.json).

- At each of 6.1.4 and 6.1.5, exclude the raw inherited `अजादेः` and
  `द्वितीयस्य` restrictions. Kāśikā defines these designations for the two
  occurrences generally; its examples include the consonant-initial roots.
  This accounts for four exclusions. At 6.1.10 the two terms remain bound
  as a conditional vowel-initial alternative outside the current domain.
- At 7.1.4, split the publisher's `प्रत्ययादीनाम्` annotation into affix
  membership and excluded initial-only scope. Kāśikā 7.1.3 explicitly drops
  ādi, and 7.1.4 describes the jh of the affix after abhyasta.
- At 8.2.38, exclude the raw inherited `अन्ते` as a restriction to a final
  substitution target. The target is the abhyāsa's initial d. Separately
  supply `झषन्तस्य` from 8.2.37, explicitly required by Kāśikā: the root
  part must end in jhaṣ. Thus दधाति is not a bhaṣ environment.
- At 6.4.87, supply `ओः` from 6.4.83, following Bālamanoramā's explicit
  inheritance. The whole aṅga supplies the multiple-vowel condition while
  the final root u supplies the substitution target.

These are attributed interpretations within the admitted domain, not an
automatic inference from Sanskrit prose. Matching source terms and literal
citation anchors are checked; that mechanism does not prove the interpreter's
soundness for all contexts.

## The dhā query

Kāśikā 8.2.38 names reduplicated dhā and explicitly suspends both restoration
of the deleted ā under sthānivad and invisibility of abhyāsa-jaśtva here.
Bālamanoramā 6.4.118 supplies the intermediate `दध् तस्`; 8.2.38 distinguishes
the t/th, s and dhv triggers from v/m, and 8.2.40 excludes dadhāti.

For धत्तः the morphological source retains copied `dh a`, original-root
`dh` after ā-lopa, the empty but identified śap, and `t a s`. The specific
8.2.38 query reads the original copy through 8.4.54 to obtain initial d,
then substitutes dh under bhaṣ. It records the source UID and marks that
original jaśtva target consumed once. The later ordinary 8.4.54 pass cannot
repeat on the newly produced dh. This scheduling is a bounded implementation
of the cited permission; it is not a general claim about rule reapplication.
The separate 8.2.40 exclusion preserves the following t, and 8.4.55 devoices
root-final dh to t. Pause readout supplies ḥ.

The same query applies before s in धत्से and before dhv in धद्ध्वे. It is
absent from दधाति, दधति, दध्वः and दध्महे. The unmodified classical source
state remains reusable; no readout can be fed back as an earlier derivation.

## Claim boundary

This work covers one CV copying shape, three lexical identities and their
licensed classical present profiles. More complex reduplication, general
ābhīya/sthānivad interaction, accents, optional consonant doubling and other
lakāras are open. Full native operator-family construction and specialization
compatibility are separate obligations. No numbered theorem or earlier
scientific endpoint is changed.
