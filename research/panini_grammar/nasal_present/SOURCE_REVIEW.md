# PG12 — Source readings and lexical boundaries

Author: Monty. 2 November 2026.

Primary source: [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data),
commit `5744762f010d677cfb43f347a42d02796cf615d6`. Sanskrit text,
inheritance/case annotations, Dhātupāṭha entries and named commentaries
remain separate evidence. [SOURCE_PINS.json](SOURCE_PINS.json) binds eight
external files and 115 historical repository files against baseline
`18ecae563b457e3f0fe2edcacb941b2a03b0bd1c`.

The preflight matches **717 literal anchor references / 673 unique
anchors** across the new rule, lexical, adjudication and word-case packets.
It makes no alteration to the external source or older grammar evidence.
The pinned Vidyut table is only an implementation comparison.

## Rule frame and selection

The 22 new records bind every reviewed term to its source occurrence and
case. They reuse PG11's occurrence-aware compiler. In 6.4.2 the selected
Kāśikā reading expressly retains the aṇ condition; the new view supplies
that occurrence from 6.3.111 and records its provenance. Omitting it leaves
the record unresolved. No earlier scope view is edited.

3.1.73, 3.1.79 and 3.1.81 select śnu, u and śnā respectively on the exact
lexical profiles. 3.1.82 provides both śnu and śnā for sku and the four
sūtra-listed stambh roots. Kāśikā explicitly discusses their status as
sūtra-listed roots and their wider usability. That status is retained; it
is not confused with a Vedic-only register restriction.

Each completed derivation retains one root, one vikaraṇa and one ending.
Its pronunciation projection is separate from source identity and history.
śnu and śnā are śit/ṅitvat triggers; u is a different affix. A pit ending
can strengthen u without authorizing root guṇa through a śit vikaraṇa.

## Seven recorded decisions

Full literal anchors are in
[SOURCE_ADJUDICATIONS.json](SOURCE_ADJUDICATIONS.json).

| Decision | Reading implemented and retained boundary |
| --- | --- |
| Pvādi endpoint | Kāśikā at 7.3.80 expressly records both the subdivision ending at plī and a through-end-of-gaṇa reading. PG12 selects the former and lists its admitted members explicitly. Later vrī, bhrī, kṣī and heṭ do not receive shortening in this profile. |
| Tanādi guṇa | Siddhāntakaumudī at 2.4.79 records both omission and application of root guṇa. Bālamanoramā extends that disagreement from kṣiṇ to ṛṇ and the following entries. Both branches are retained for kṣiṇ/ṛṇ/tṛṇ/ghṛṇ, rather than declaring all guṇa optional. |
| Class-5 register | Siddhāntakaumudī at 7.3.56 describes pṛ/spṛ/smṛ as Vedic although their selected lexical rows lack that tag. They remain deferred. At 7.4.72 it explicitly permits kṣi in classical language; Bālamanoramā identifies kṣi as the intended root. Its raw Vedic tag remains unchanged. |
| Initial u in udhras | Entry 1090060 explicitly marks initial u as nasal. The selected traditional passage also calls u an it marker, while reporting another root-member reading. PG12 uses the marker reading and retains the modern note reporting the alternative. |
| Printed heṭ shortening | The selected Siddhāntakaumudī passage gives hiṭhṇāti, consistent with its broader shortening discussion. PG12's separately declared narrow endpoint retains heṭ. The shortened word is not counted as a matching witness for the unshortened path. |
| Printed śranth order | The selected Siddhāntakaumudī field has śranthāti. PG12 follows the explicit penultimate-n deletion of 6.4.24, then śnā, producing śrathnāti. The differing printed word is preserved, not repaired into a witness. |
| Separate śṝñ entry | Entry 1090015 occurs at an inserted position in the pinned lexical list, while the selected traditional named pvādi sequence does not resolve its membership. It is deferred. The later parasmaipada śṝ entry 1090021 is independently identified and admitted. |

These decisions define the present finite adapter. They do not reconcile
all editions or identify the software table as an independent textual
authority. Van's source-listed ātmanepada profile is retained; a separate
commentary report of parasmaipada in the Cāndra tradition is not silently
added to this profile.

## Root operations with retained intermediate states

**N-lopa, 6.4.24.** The target is the penultimate n of a consonant-final,
non-idit root before the actual kit/ṅit trigger. The deleted sound belongs
to the root. This is neither deletion of the vikaraṇa's n nor a generic
rule for every nasal. The original teaching form and deleted sound UID
remain inspectable in dambh, bandh and the stambh/śranth groups.

**Saṃprasāraṇa, 6.1.16 / 1.1.45 / 6.1.108.** Grah's r becomes ṛ and jyā's
y becomes i before the admitted ṅitvat śnā. The following original vowel
then participates in a same-root pūrvarūpa merger. Both sound identities
are retained in that event. In grah, the resulting vowel is not root-final,
so 6.4.2 does not lengthen it. In jyā, 6.4.2 first produces long ī, and
7.3.80 subsequently shortens it. The trace therefore retains the real
intermediate long vowel rather than replacing the entire root with a
memorized final string.

**Jñā and residual long ṝ.** Jñā receives long jā under 7.3.79 and cannot
borrow jyā's saṃprasāraṇa. The explicitly selected pvādi members shorten
long ṝ before the residual 7.1.100 path can operate. Svṝ lies outside that
selected subdivision; 7.1.102's labiodental reading gives u with retained
r accompaniment under 1.1.51. Root-final r then licenses 8.2.77 lengthening
in the separate readout, yielding svūrṇāti.

**Khav and ūṭh.** 6.4.19 requires the admitted nasal-initial kit/ṅit affix.
It replaces root-final v with ūṭh; ṭh is a retained teaching marker.
6.1.89's vṛddhi is licensed by the actual resulting substitute and its UID,
not merely by finding the letters a and ū next to each other. The merged
au retains both source sounds. No extra augment or root constituent is
introduced. Khac remains a separate identity with its contact path.

## Options, ordering and ṇatva

The four tanādi root-guṇa options are evaluated before ending-dependent
affix strength and u-lopa. The ar produced from ṛ creates an rṇ cluster,
which blocks 6.4.107 in that branch. The unstrengthened ṛṇ branch still
admits optional u-loss. By contrast, kṣiṇ's e does not create that cluster,
so both root readings can combine with both u choices. Actual root/affix
sounds determine eligibility; the code does not return a stored paradigm.

The earlier 7.1.3/7.1.5 ending substitutions precede weak śnā's 6.4.112
ā-lopa. Consonant-initial weak endings instead produce ī under 6.4.113.
The source teaching form and affix identity survive either operation.

The new 8.4.2 window includes aṭ, gutturals and labials on these reviewed
word profiles. Prefix boundaries and intervening anusvāra/num are not
generalized here. Kāśikā at 8.4.39 explicitly names both tṛpnoti and
kṣubhnāti and explains continuation of kṣubh's prohibition after changes
to ā. PG12 checks the exact retained śnā identity and the local 1.1.56
permission, with no restoration of its visible ā. Retargeting the license
or claiming sound restoration is rejected.

Early nasal processing precedes ṇatva; the later phonetic pass cannot feed
back into it. Thus stṛṇanti retains a retroflex vikaraṇa n and a dental
ending n. The readout cannot mutate or alias its morphological source.
This is a finite ordering contract, not a general asiddha solver.

## Literal words and unresolved evidence

[REFERENCE_CASES.json](REFERENCE_CASES.json) contains **109 literal-word
membership cases across 73 new roots**, plus 37 expected refusals. Word
boundaries use Devanagari letters and treat daṇḍa as punctuation. Selected
passages include the lexical commentaries and directly relevant rule
examples. The slot candidates come from the separate comparison table,
but a candidate is admitted as word evidence only if its exact Sanskrit
spelling occurs in the selected primary passage. This does not attest
every optional branch or independently establish a semantic pada license.

The following **24 new entries** have lexical/rule evidence and complete
comparison cells, but no separate exact full-word witness in this packet:

| Group | IDs |
| --- | --- |
| Svādi | 1050003, 1050008, 1050012, 1050027 |
| Tanādi | 1080007 |
| Kryādi | 1090021, 1090022, 1090024, 1090026, 1090027, 1090028, 1090029, 1090030, 1090033, 1090035, 1090038, 1090039, 1090040, 1090041, 1090042, 1090046, 1090048, 1090069, 1090070 |

Broader source searches found some matching strings in other discussions;
uncertain lexical/sense attribution was not silently treated as a new
witness. The seven earlier gaps remain **1020021, 1020036, 1020037,
1020048, 1020052, 1020054 and 1020056**. Those historical packets and
counts are not rewritten.
