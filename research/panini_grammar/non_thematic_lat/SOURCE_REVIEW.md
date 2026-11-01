# PG6 — Primary readings and local interpretation decisions

Author: Monty. 1 November 2026.

The primary witness remains [ashtadhyayi-com/data, commit 5744762](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
[SOURCE_PINS.json](SOURCE_PINS.json) pins seven external files and 26 unchanged
predecessor files. [RULE_RECORDS.json](RULE_RECORDS.json) stores exact Sanskrit
sūtra text, term roles, inherited sources and literal commentary anchors.
The verifier checks every anchor against the original file bytes.

References below use the pinned [Kāśikā](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/kashika.txt),
[Siddhāntakaumudī](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/kaumudi.txt),
and [Dhātupāṭha data](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/dhatu/data.txt).
A key such as `64087` identifies 6.4.87 in these files. Lexical identifiers
preserve gaṇa and sense; kṛ in hiṃsā is not the kṛ in karaṇa admitted here.

## Guṇa is relative to its actual triggering affix

PG5 already binds 1.2.4 **सार्वधातुकमपित्**, *sārvadhātukam apit*, and 1.1.5
**क्ङिति च**, *kṅiti ca*. PG6 applies them at two separate aṅga boundaries.
The śnu affix is apit/ṅitvat, so it cannot cause guṇa of su's root vowel.
Tip is pit, however, and can cause guṇa of the final u of the śnu-ending
aṅga under 7.3.84: su-nu-ti → su-no-ti. Before apit tas that second guṇa is
blocked: su-nu-tas. Kāśikā 1.2.4 contrasts the weak forms with करोति, करोषि,
करोमि; Kāśikā 7.3.89 separately supplies सुनोति, सुनोषि, सुनोमि.

Strong/weak labels in the output summarize these derived marker conditions.
They are not a hardcoded rule that a named person is always strong in every
lakāra. The implemented domain contains only classical laṭ endings.

## Junctions and optional u-loss

6.4.77 **अचि श्नुधातुभ्रुवां य्वोरियङुवङौ** supplies iy/uv replacements in
its stated domains. PG6 implements only the śnu-ending u branch. Kāśikā gives
आप्नुवन्ति, राध्नुवन्ति, शक्नुवन्ति. 6.4.87
**हुश्नुवोः सार्वधातुके**, *huśnuvoḥ sārvadhātuke*, additionally inherits
**अनेकाचः** and **असंयोगपूर्वस्य**. Its śnu branch gives सुन्वन्ति, while the
same commentary explicitly excludes आप्नुवन्ति because of the cluster.
The runtime counts the cluster across the root/affix seam; looking only
inside the affix nu would incorrectly admit the short v replacement for āp.
The hu branch itself is not implemented here.

6.4.107 **लोपश्चास्यान्यतरस्यां म्वोः** permits loss of eligible affix-final u
before m/v. Kāśikā lists सुन्वः/सुनुवः, सुन्मः/सुनुमः, तन्वः/तनुवः,
तन्मः/तनुमः, and excludes शक्नुवः/शक्नुमः from the loss. It explicitly says
**लोपग्रहणमन्त्यलोपार्थम्**: this is final-sound deletion, not wholesale
luk of a morpheme. Siddhāntakaumudī notes that guṇa occurs in mip, with
धिनोमि; PG6's strong sunomi likewise does not branch into u-loss forms.

6.4.108 **नित्यं करोतेः**, *nityaṃ karoteḥ*, makes the loss mandatory for the
identified kṛ. Its relation to 6.4.107 is a recorded local exception; it does
not establish a general algorithm for all traditional nitya priorities.

## Kṛ, retained deletion, and a bounded 1.1.58 query

The class 8 u prescription first permits kṛ's guṇa to kar. Before weak
sārvadhātuka, 6.4.110 **अत उत् सार्वधातुके** prescribes the short u in kur.
Kāśikā explicitly explains the t-qualification as preventing renewed
laghūpadha guṇa. PG6 records that inhibition instead of rerunning guṇa on
the new u and erasing the weak-form distinction.

Kāśikā 6.4.108 explains that after u-loss, the lengthening query does not
restore the deleted vowel under 1.1.58; 8.2.77 would then apply, but
8.2.79 **न भकुर्छुराम्** blocks it. Thus ku-r + vas gives kurvaḥ, not kūrvaḥ.
PG6 retains the original u-affix identity, its deletion event, the specific
lengthening view and the explicit prohibition. A missing sound is not
identical to an unrecorded affix.

**Local scope decision:** the publisher carries `पदस्य` into 8.2.79. The
kur example in Kāśikā 6.4.108 requires the prohibition inside the whole word,
where kur itself is not a complete pada. PG6 excludes that inherited
restriction in its **local kur query**. This is an explicit interpretation
supported by the quoted derivation, not an alteration of the original
annotation or a complete settlement of the bh/chur domains.

## Śnā, endings, and lexical shortening

6.4.112 **श्नाऽभ्यस्तयोरातः** deletes the relevant long ā before weak
sārvadhātuka; 6.4.113 **ई हल्यघोः** selects ī before a consonant, outside
the ghu exclusion. The implemented branch is śnā, not the whole abhyasta
domain. Kāśikā gives लुनते versus लुनीते, लुनीतः, पुनीतः.

Siddhāntakaumudī 3.1.81 expressly places jh → ant/at **before** this ī/ā-lopa
decision. Otherwise the jh teaching consonant would wrongly trigger ī in
the plural. PG6 therefore derives krīṇanti and krīṇate by distinct tiṅ
substitutes followed by the vowel-conditioned ā-lopa.

7.1.5 **आत्मनेपदेष्वनतः** gives at for ātmanepada jh directly after the
non-short-a aṅga. Kāśikā supplies चिन्वते, पुनते and लुनते. Long ā is not
the short a excluded by this rule. The inherited affix-membership reading
of 7.1.3 remains, but the immediate aṅga-to-jh condition cannot skip an
affix-internal augment. A separate local control checks that distinction.

**Scope decision:** PG5's Kāśikā-based split of editorial `प्रत्ययादीनाम्`
is carried to the 7.1.5 record: retain affix membership, exclude a universal
initial-only inheritance. The adjacency guard comes from 7.1.5's own
relation to the aṅga and its commentary, not from that excluded component.

7.3.80 **प्वादीनां ह्रस्वः** is applied to the explicitly identified pū/lū
entries before śit. Kāśikā directly gives पुनाति and लुनाति. Its discussion
of competing endpoints of the larger pvādi group is preserved as open;
two unambiguous members do not settle the entire gaṇa boundary.

## Śru and ordered phonetic views

3.1.74 **श्रुवः शृ च**, *śruvaḥ śṛ ca*, couples śnu with the śru → śṛ
substitution. PG5 had retained the unexecuted obligation. PG6 executes it
on lexical ID 1011092 while keeping the original root and replacement target
identities, yielding the Kāśikā examples शृणोति, शृणुतः, शृण्वन्ति.

8.3.59 **आदेशप्रत्यययोः** is implemented only for adjacent eligible vowels
and tiṅ-member s in this domain, giving sunoṣi and krīṇīṣe; it does not
turn krīṇāsi into a ṣ-form. Broader intervening-num/visarga/śar cases and
the rest of the iṇ/ku domain remain open.

8.4.1 **रषाभ्यां नो णः समानपदे** and 8.4.2
**अट्कुप्वाङ्नुम्व्यवायेऽपि** supply a bounded ṇatva reading. Kāśikā 8.4.1's
**ऋवर्णाच्चेति वक्तव्यम्** is separately attributed for śṛ. The reviewed
gap consists of aṭ sounds (vowels and h/y/v); other intervening classes
and the general lexical prohibition system are not implemented. Same-pada,
pada-final status, and reviewed exception context remain required inputs.

**Scope decision:** the editorial 8.4.2 annotation carries only r/ṣ. Its
Kāśikā explicitly continues the n → ṇ operation. PG6 supplies the inherited
target, output and same-pada condition from 8.4.1 with their parent identities.
It does not infer these terms from numerical proximity alone.

Before ṇatva, 8.3.24 has already turned the n before t into anusvāra. The
dental n produced later by 8.4.58 is not available to the earlier operation.
That is why **kurvanti** retains n, and **krīṇanti** contains an earlier ṇ
in the vikaraṇa plus a later n in tiṅ. The verifier checks both the output
and this order; final spelling alone would miss the distinction.

## Evidence quality and preserved source issues

The 53 positive word cases quote traditional-commentary forms. The 153-cell
comparison separately uses the pinned
[Vidyut-generated table](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/dhatu/dhatuforms_vidyut_shuddha_kartari.txt).
Its agreement is a software diagnostic, not a Sanskrit validity oracle or
independent edition. Expected forms are never read by `grammar.py`.

The digitized Siddhāntakaumudī 3.1.81 prints क्रीणाते twice after क्रीणीते;
the third item is not silently treated as an attestation of क्रीणते.
The latter output is checked through the stated 7.1.5/6.4.112 derivation
and separately against the software table. Kāśikā 6.4.113 prints इलादौ
where the sūtra and other commentary identify the hal condition. Both
source strings remain unchanged; the adopted readings are explicit here.

The local paths do not implement every same-support clause of 6.4.22, every
sthānivad exception, or a general priority resolver. These are linguistic
adapters; no native operator-family, physical or calculator theorem follows
from the finite checks.
