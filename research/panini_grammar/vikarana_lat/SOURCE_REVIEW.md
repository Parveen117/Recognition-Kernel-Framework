# PG5 — Source readings and derivation boundaries

Author: Monty. 1 November 2026.

Primary witness: [ashtadhyayi-com/data at 5744762f010d677cfb43f347a42d02796cf615d6](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
The exact file hashes, lexical fields and literal citation anchors are checked
by `verify.py`; [SOURCE_PINS.json](SOURCE_PINS.json) pins seven external files
and 17 predecessor files. The sūtra and commentary texts are preserved rather
than normalized to agree with the implementation.

Sources used below are the pinned [sūtrapāṭha](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/data.txt),
[Kāśikā](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/kashika.txt),
[Siddhāntakaumudī](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/kaumudi.txt),
[Bālamanoramā](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/balamanorama.txt),
and the publisher's [Dhātupāṭha entries](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/dhatu/data.txt).
In these JSON witnesses, `31069` means 3.1.69; a lexical ID such as `1040001`
identifies a specific entry, not every root spelled div.

## 1. Vikaraṇa prescriptions have lexical and semantic domains

3.1.68 **कर्तरि शप्**, *kartari śap*, inherits the following sārvadhātuka
condition. Kāśikā explicitly describes a root before an agent-expressing
sārvadhātuka and gives भवति, पचति. 3.1.69, 73, 77, 78, 79 and 81 name narrower
lexical domains and their commentaries identify them as **शपोऽपवादः**. The
records preserve those declared relations instead of treating every later
affix rule as applicable to every root.

3.1.70 **वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः** supplies an option.
Kāśikā calls it **उभयत्र विभाषेयम्** and explicitly includes two bhram entries.
PG5 implements the option on its reviewed bhram/laṣ identities; it does not
claim all eight named roots are fully conjugated. For divādi bhram, śyan and
śap branches remain separate and 7.3.74 lengthens only the śyan branch.

3.1.71 **यसोऽनुपसर्गात्**, *yaso 'nupasargāt*, gives the unprefixed yas option;
3.1.72 **संयसश्च**, *saṃyasaś ca*, extends it to sam-prefixed yas. Kāśikā's
contrast आयस्यति / प्रयस्यति prevents silently carrying the option to every
prefix. Selection queries check this contrast; prefix morphology and sandhi
are not implemented by returning those examples from a lookup table.

3.1.75's optional śnu applies to the identified akṣ. 3.1.76
**तनूकरणे तक्षः**, *tanūkaraṇe takṣaḥ*, additionally restricts the sense.
The tanūkaraṇa entry `1010743` and the tvacana entry `1010756` therefore have
different selection results. Likewise kṛ `1050007` (hiṃsā, class 5) and kṛ
`1080010` (karaṇa, class 8) are not collapsed by their headword spelling.

3.1.74 couples śnu with the śru → śṛ substitution. 3.1.80 couples u with a
substitution on the named roots. PG5 records these required actions but does
not execute the subsequent word derivations. 3.1.82 is demonstrated on sku;
its other four named roots and their sautra teaching conventions remain open.

## 2. It-lopa, ṅitvat and whole-affix deletion are different

The PG3 reviewed marker profile leaves śap → a with ś/p history, śa → a with
ś history, śyan → ya with ś/n history, and ṇic → i with ṇ/c history.
1.2.4 **सार्वधातुकमपित्**, *sārvadhātukam apit*, inherits ङित्; Kāśikā reads
this as **ङिद्वद्**, not as inserting a fictitious ṅ into the teaching form.
Thus ātām and āthām receive ṅitvat through this rule, not through invented
initial markers.

1.1.5 **क्ङिति च**, *kṅiti ca*, is explicitly described by Kāśikā as
**निमित्तसप्तमी**: it blocks the guṇa/vṛddhi caused by that affix, including
laghūpadha guṇa. Śa therefore blocks tud → tod even when the later tip is pit.
Conversely a later apit/ṅitvat tas does not block the bhū guṇa caused by śap.
This triggering-affix distinction is checked directly.

2.4.72 **अदिप्रभृतिभ्यः शपः** inherits luk. 2.4.75
**जुहोत्यादिभ्यः श्लुः** inherits śap, with Kāśikā explicitly excluding yaṅ.
The whole affix disappears while identity and markers remain in the record.
1.1.61 distinguishes the deletion names, and 1.1.63 blocks the relevant
aṅga effects despite that retained history. Ślu also requires the separately
recorded 6.1.10 reduplication; it is not implemented as a synonym for luk.
The ad/hu plans are consequently selection/deletion demonstrations, not
complete aorist, present or reduplication engines.

## 3. A new inherited-scope correction at 7.1.3

7.1.3 **झोऽन्तः**, *jho 'ntaḥ*, has editorial `प्रत्ययादीनाम्` inherited
from 7.1.2. Kāśikā says:

> प्रत्ययग्रहणमनुवर्तते, आदिग्रहणं निवृत्तम्।

The PG5 overlay splits the annotation: **प्रत्ययस्य** remains as the
affix-membership domain and **आदि** is excluded. It does not edit the source
or PG4. Kāśikā's शयान्तै example and Tattvabodhinī explain why an initial-only
condition is too narrow. The local action replaces affix-member jh by ant;
the final a in the grammatical citation अन्त is not an extra spoken vowel.
A noninitial-affix control checks the scope, without claiming a complete leṭ
derivation or a Vedic domain.

## 4. Laṭ and ātmanepada path correction

3.2.123 **वर्तमाने लट्** supplies the present lakāra. Kāśikā 3.4.77
**लस्य** identifies **लकारमात्रं स्थानित्वेनाधिक्रियते**. The PG3 reviewed
profile preserves l and the retained ṭ marker; it is used here instead of
the incorrect old T82 lakāra expectations. the theorem branch's subsequent commit
[7040a9a](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/7040a9a13d3c47a74299fb059c0d433d12b5867f)
also addresses that old reading. PG5 does not merge or rewrite that frozen
historical packet to obtain its results.

Kāśikā 3.4.78 supplies all eighteen pac examples. 1.4.101–102 supply the
person/number order. Contextual pada choice remains input: the lexical P/A/U
field alone is not a substitute for 1.3's semantic and prefix conditions.

3.4.79 **टित आत्मनेपदानां टेरे** takes ṭit from the lakāra and uses the last
vowel onward selector of 1.1.64. 3.4.80 **थासस्से** is the thās-specific
substitution. For duals, ātām/āthām first have their ṭi replaced; their
remaining initial ā becomes iy under 7.2.81 after the a-ending aṅga. In the
admitted local path y is deleted before t/th by 6.1.66, and the vowel seam
undergoes 6.1.87.

For **edhe**, Bālamanoramā 3.4.80 explicitly describes iṭ → e followed by
śap's a + e. PG5 therefore applies 3.4.79 before 6.1.97. It closes the local
path discrepancy documented in T66, while preserving T66 as historical
evidence. It does not prove a general antaraṅga ordering algorithm.

Kāśikā 6.1.97 **अतो गुणे** explicitly identifies the 6.1.101 exception and
discusses the otherwise-expected 6.1.88 in पचे. The runtime retains both
original seam constituents and consumes these declared exception records.

## 5. Cur and the late div/siv reading

3.1.25's curādi ṇic is **स्वार्थे**, as Kāśikā states. Bālamanoramā explains
cur's upadhā guṇa before ṇic; Siddhāntakaumudī gives the sequence
**सनाद्यन्ताः … धातुत्वम् … तिप्शबादि … गुणायादेशौ … चोरयति**.
The first guṇa acts on the root before ṇic (7.3.86); the second acts on ṇic's
i at the end of the derived dhātu before śap (7.3.84). These are different
targets and aṅga boundaries, with separate events. No general causative or
curādi optional-ṇic semantics is inferred from this one entry.

8.2.77 **हलि च**, *hali ca*, inherits a root ending in r/v, its ik upadhā,
and lengthening. Kāśikā gives **दीव्यति। सीव्यति।** and contrasts a denominal
दिव्यति. It says **अपदान्तार्थोऽयमारम्भः**, so the reviewed operation is not
restricted to a root that is itself a complete pada. PG5 retains divyati in
the pre-Tripādī state and exposes dīvyati in the late readout; that lengthening
cannot feed the earlier guṇa stage. The query then uses PG4's admitted
nasal/contact operations and explicit word-final pause conditions.

## 6. Evidence grades

The 40 positive word cases quote traditional-commentary forms. The entire
162-cell comparison uses the separately pinned
[Vidyut-generated table](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/dhatu/dhatuforms_vidyut_shuddha_kartari.txt).
It is another implementation output hosted with the source corpus, not
another manuscript edition and not proof of linguistic soundness. Expected
forms and comparison data are never imported by `grammar.py`.

The bhvādi bhram entry `1010985` illustrates why the boundary matters: the
comparison table prints bhramyati for its śyan branch, while Kāśikā 3.1.70
mentions both bhram entries and presents bhrāmyati (भ्राम्यति). The exact
reach of the divādi śamādi lengthening needs separate review. PG5 selects
the option for both identities but generates complete words only for the
unambiguous admitted divādi entry. It does not normalize a disputed entry
to satisfy the external table.
