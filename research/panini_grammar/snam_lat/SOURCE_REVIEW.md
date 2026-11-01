# PG7 — Source readings and claim boundaries

Author: Monty. 1 November 2026.

The primary digital edition is [ashtadhyayi-com/data at
5744762](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
[SOURCE_PINS.json](SOURCE_PINS.json) binds eight external files and 40 unchanged
predecessor files. Sūtrapāṭha, Kāśikā, Siddhāntakaumudī, Bālamanoramā,
Tattvabodhinī and Laghusiddhāntakaumudī are distinct attributed witnesses.
Their hosting in one digital repository does not constitute independent
edition agreement. Full Sanskrit and term bindings are in
[RULE_RECORDS.json](RULE_RECORDS.json); the following interpretations are ours.

## The eleven contracts

| Sūtra / Sanskrit | Admitted operation and boundary |
| --- | --- |
| [1.1.47](https://ashtadhyayi.com/sutraani/1/1/47) मिदचोऽन्त्यात्परः | Place identified m-it śnam after the host root's last vowel; preserve the root and the affix as owned constituents |
| [1.1.58](https://ashtadhyayi.com/sutraani/1/1/58) न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु | Only the cited nasal query after śnam a-lopa; the deleted a is not restored |
| [3.1.78](https://ashtadhyayi.com/sutraani/3/1/78) रुधादिभ्यः श्नम् | Reuse class selection; add the local nitya śnam-before-laghūpadha-guṇa contract |
| [6.4.23](https://ashtadhyayi.com/sutraani/6/4/23) श्नान्नलोपः | Delete root-owned n immediately after identified śnam; neither an arbitrary string `na` nor śnā licenses it |
| [6.4.111](https://ashtadhyayi.com/sutraani/6/4/111) श्नसोरल्लोपः | Delete śnam's a before kit/ṅit/ṅitvat sārvadhātuka tiṅ; the separate as-root branch is not implemented |
| [8.2.30](https://ashtadhyayi.com/sutraani/8/2/30) चोः कुः | Identified root-final c/j before jhal; no all-cu or separate padānta implementation is claimed |
| [8.2.40](https://ashtadhyayi.com/sutraani/8/2/40) झषस्तथोर्धोऽधः | t/th after jhaṣ; the excluded dadhā root is not in this lexical domain |
| [8.2.41](https://ashtadhyayi.com/sutraani/8/2/41) षढोः कः सि | k before s; the admitted śiṣ/piṣ paths use the ṣ branch, with tṛh's ḍh interactions still open |
| [8.3.59](https://ashtadhyayi.com/sutraani/8/3/59) आदेशप्रत्यययोः | Adjacent tiṅ s after the reviewed iṇ/ku triggers, now including the velar in yuṅkṣe; no full intervening-domain claim |
| [8.4.55](https://ashtadhyayi.com/sutraani/8/4/55) खरि च | Reviewed stops devoice before khar in the admitted internal junctions; h processing is excluded |
| [8.4.65](https://ashtadhyayi.com/sutraani/8/4/65) झरो झरि सवर्णे | Optional jhar deletion after hal and before savarṇa jhar, with at most one site in the admitted non-doubled profile |

1.1.47, 1.1.58, 3.1.78 and 8.3.59 already have bounded predecessor records.
These new local contracts do not count as four newly discovered sūtras.

## Placement, ownership and guṇa

Kāśikā 1.1.47 treats mit placement as an exception to default substitution
and following-affix placement. Siddhāntakaumudī says
`तस्यैवान्तावयवो मित्स्यात्`: the mit unit is a member of its host. Accordingly,
PG7 preserves the base root, affix identity and a root-with-mit constituent,
while a layout interleaves their owned sounds. It does not create two roots
from the left and right pieces of `bhi-na-d`.

Bālamanoramā 3.1.78 explicitly explains why an attempted guṇa argument based
only on śnam's ś-it and apit ṅitvat is unnecessary: there is no relevant
ik-final aṅga *before* this internal affix. The actual competition is the
earlier root upadhā relative to the following ending. Śnam can apply with or
without that guṇa; the commentary gives it nitya precedence. After insertion,
the old root vowel is no longer the aṅga upadhā. PG7 records this specific
relation and queries the actual root-with-infix sequence. It does not supply
a general nitya classifier or apply guṇa to the isolated base-root string.

## Two deletions with different owners

Kāśikā 6.4.23 names anakti, bhanakti and hinasti. In these paths the n after
śnam belongs to the root; the n inside śnam must survive. In hiṃs that
root-owned n was itself introduced as num by 7.1.58. PG7 retains both its
earlier insertion and its later deletion, with different identities for the
root n and affix n.

6.4.111 separately deletes śnam's a before qualifying weak tiṅ. Kāśikā's
negative example bhinatti retains a before the strong ending. The as-root
member of the same sūtra is not admitted merely because its text is bound.

The local schedule applies 6.4.23 before 6.4.111 and retains both conditions.
Tattvabodhinī 6.4.23 discusses the visibility problem that prevents replacing
this with a naive post-a-lopa application of 6.4.24. PG7 neither implements
that competing rule nor treats every visible n as its target. General
6.4.22 scheduling remains open.

## Ordered phonetics and the non-restored a

Siddhāntakaumudī and Bālamanoramā 3.1.78 explicitly distinguish the earlier
ṇatva from the later anusvāra/parasavarṇa sequence and invoke 1.1.58 for the
deleted a. PG7's readout therefore uses this finite order:

1. Root c/j-to-ku, t/th-to-dh, and ṣ/ḍh-to-k where admitted: 8.2.30/40/41.
2. Final s-to-ru and visarga at the supplied pause: 8.2.66, 8.3.15.
3. Nasal hiding before jhal: 8.3.24. Weak śnam's deleted a is not restored.
4. The admitted adjacent-affix ṣatva and PG6 local ṇatva: 8.3.59, 8.4.1–2.
5. PG4's contact parameters and prohibitions: 8.4.40–44.
6. Voicing, devoicing and nasal restoration: 8.4.53, 8.4.55, 8.4.58.
7. Optional savarṇa jhar collapse: 8.4.65.

All admitted junctions are internal to one supplied pada; 8.4.42's
cross-pada exception analysis is not generalized. A late n restored by
8.4.58 cannot re-enter earlier ṇatva. Thus strong ruṇaddhi and weak rundhanti
retain different nasal histories. Every readout is a copy; its output cannot
be fed back as a pre-Tripādī source.

## The 8.4.65 scope decision and spelling profile

The publisher's annotated 8.4.65 frame includes inherited `परसवर्णः` from
8.4.58. Kāśikā instead states the hal, jhar, savarṇa, lopa and optionality
conditions; Laghusiddhāntakaumudī states the same lopa operation. PG7 excludes
that inherited replacement word locally, while retaining the sūtra's own
`सवर्णे` and all the licensed deletion conditions. The source bytes and raw
edge remain preserved in the excluded view.

Savarnatva here does not require identical aspiration/voicing: t/th and d/dh
can form an eligible stop pair. A nasal is not jhar, and a sibilant is not
savarṇa to a stop merely because their place agrees. The prior hal condition
prevents collapse of strong bhinatti's tt, which follows a vowel.

The profile does not select optional consonant doubling under 8.4.46–47.
It therefore does not enumerate all optional pronunciation variants. Within
this declared profile it includes both runddhaḥ/rundhaḥ and analogous
8.4.65 alternatives. Multiple interacting collapse sites are explicitly
rejected rather than silently truncated.

## Evidence separation and source anomalies

The 85 literal cases are **word-membership witnesses**, not exhaustive
paradigms in the commentaries. An attested form must occur in the generated
set; other alternatives need their own derivational rules. Complete generated
sets for all 288 cells are compared separately with pinned Vidyut output.
Some admitted roots have rule/lexical evidence and software comparison but
no direct word witness among these 85 cases. No identical-evidence claim is
made for every root or cell.

The pinned Bālamanoramā 3.1.78 contains `भिन्त्त्थः` at the bhid second-dual
position. This is preserved as printed and is not used to attest either
ordinary bhintthaḥ or bhinthaḥ. Whether it reflects doubling or transmission
needs separate edition review. No source is silently normalized to fit the
chosen spelling profile. Forms printed with an added *iti* are cited from a
witness that actually contains the standalone form when available.

PG7 supplies no raw Sanskrit interpreter, unrestricted phonetic transducer,
general validity oracle or native operator/quantum-calculator theorem.

## Concurrent theorem-branch work

Before publication, the theorem branch advanced to
[`7802a35`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/7802a351dec44dc8e6dfdfe12b4b6f5ecace9fad).
The T86 capsule, implementation and updated ledger were read at that exact
commit. [The observation snapshot](CONCURRENT_THEOREM_SNAPSHOT.json) records
their scope without copying or merging their implementation or replaying a
certificate. It also preserves the older review-branch ledger's counts as a
dated baseline, not as the current companion-branch inventory. This avoids
making PG7 depend on an evolving ledger file as if it were a frozen grammar
source.

T86 reports eleven kta stems and 242 outputs through the bounded T63 nominal
ladder, with aniṭ supplied rather than inferred from accent. Its laṭ side
reads existing PG reference cases. These are separate evidence and morphology
domains: they neither add 242 laṭ cells nor close hu's missing present paradigm.
The six listed exclusions were read as declarations, not newly checked as
runtime refusal behavior.
