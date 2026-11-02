# PG14 — Source decisions for the written grammar

Author: Monty. 2 November 2026.

The primary data edition is `ashtadhyayi-com/data` at
`5744762f010d677cfb43f347a42d02796cf615d6`, the same fixed edition used by
the preceding grammar stages. [SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json)
contains the selected complete commentary entries and lexical records;
[SOURCE_PINS.json](SOURCE_PINS.json) binds the original file bytes. The
publisher's `kaumudi` collection is attributed here to Siddhāntakaumudī;
`balamanorama` to Bālamanoramā; `kashika` to Kāśikā. Commentaries are not
silently promoted into additional numbered Pāṇini sūtras.

## Reading decisions

| Issue | Source and adopted reading | Consequence |
|---|---|---|
| Voice is an interpretation of la | Kāśikā 3.4.69: karman/kartṛ for a transitive use, bhāva/kartṛ for an intransitive use | Select the expressed role before agreement or endings |
| Intransitive is contextual | Bālamanoramā 3.4.69 also discusses avivakṣita-karman | PG14 explicitly excludes that extension; missing noun text alone is insufficient |
| A is not synonymous with passive | Kāśikā 1.3.13 versus 1.3.74 | A causative kārayate can be kartari, with śap |
| Bhāva number/person | Siddhāntakaumudī 3.1.67, with Bālamanoramā's detailed explanation | Default 3sg even with first/second-person or plural agents |
| Expression controls case | Kāśikā 2.3.1, 2.3.2, 2.3.18, 2.3.46 | Retain the abhihita role; do not assign accusative to every semantic patient |
| Causation licenses formation | Kāśikā 1.4.54–55 and 3.1.26 | The causer has hetu and kartṛ status; ṇic follows a declared inducing event |
| The whole sanādi constituent is a dhātu | Kāśikā 3.1.32 | Ṇic's vowel and the root's vowel have different later operations |
| Causee is not uniformly karman | Kāśikā 1.4.52 with its nī/vah, ad/khād and other qualifications | Preserve root/sense classes and counterexamples; only the stated subset is closed |
| Optional hṛ/kṛ causee | Kāśikā 1.4.53 | Retain both karman and kartṛ branches; A-conditioned abhivādi/dṛś additions remain separate |
| Principal result, not any benefit | Kāśikā 1.3.72 | A wage or incidental advantage is not sufficient for F |
| Ṇic A depends on causer-directed result | Kāśikā 1.3.74, with inherited condition from 1.3.72 | Derive A permission from the completed frame |
| Upapada optionality | Kāśikā 1.3.77 expressly spans 1.3.72–76 | Actual conveyed benefit licenses A/P branches; unknown meaning does not |
| Residual P is truly residual | Kāśikā 1.3.78 | Do not choose P merely because an A condition has not yet been checked |
| budh and other named exceptions | Kāśikā 1.3.86 | Override the 1.3.74 A result in the stated causative frame |
| Different semantic classes | Kāśikā 1.3.87 glosses nigaraṇa as abhyavahāra, calana as kampana | Do not identify its calana predicate with every 1.4.52 gati frame |
| Intransitive conscious causee | Kāśikā 1.3.88 | A genuine predicate on the base event, not the final causative's transitivity |
| pā exception has a scoped target | Kāśikā 1.3.89 explicitly prohibits the preceding two P rules | Preserve 1.3.74 and the residual P domain; do not ban P lexically |
| Yak and its following ending differ | Kāśikā 3.1.67 and 3.4.113–114 | Yak is kit ārdhadhātuka introduced before sārvadhātuka tiṅ |
| Guṇa prohibition retains its trigger | Kāśikā 1.1.5 | Marker lopa does not destroy yak's kit property |
| Ṛ-final passive substitute | Kāśikā 7.4.28 and 1.1.53 | Short riṅ supplies multi-sound ri at the final ṛ; kriyate/hriyate |
| Drinking pā's augment | Kāśikā and Bālamanoramā 7.3.37 | Yuk contributes y, with k it and u pronunciation-only; not puk |
| yathā similarity qualification | Kāśikā 2.1.7 | The rule is asādṛśya, expressly excluding a similarity reading |

The extended readings of 1.3.67–71, 1.3.75–76 and the qualifications inside
1.4.52–53 are retained in the source extract. Most lie outside D_C. Keeping
their passages visible makes the domain exclusions reviewable; their mere
presence is not a claim that all their forms have been constructed.

## Lexical identity and witness discipline

PG14's twelve causative identities are copied from PG13's source-bound
selection, including knowing vid, understanding budh, drinking pā and
class-8 kṛ. The new sleeping example identifies svap 1020063. The simple
voice derivations do not treat all homonyms or prefixed senses as equivalent.

Kāśikā 1.4.52's gamayati example genuinely concerns causative lexical gam.
The substitution example for iṇ at 2.4.46 is not repurposed as that witness.
The original PG13 word-witness gaps stay unchanged. Generic D1 endings
support written rule consequences; they do not create literal commentary
attestations for every person-number word in V7.

## Public source access

The public page for [3.1.67](https://ashtadhyayi.com/sutraani/3/1/67) was
also consulted through web retrieval, including the indexed Siddhāntakaumudī
passage on default singular. Relevant public locators include
[1.3.77](https://ashtadhyayi.com/sutraani/1/3/77),
[1.3.89](https://ashtadhyayi.com/sutraani/1/3/89),
[1.4.52](https://ashtadhyayi.com/sutraani/1/4/52),
[2.1.7](https://ashtadhyayi.com/sutraani/2/1/7) and
[7.4.28](https://ashtadhyayi.com/sutraani/7/4/28).
Dynamic page retrieval did not expose every commentary body, so the pinned
publisher data and its exact keys are the reproducible source record.

The operator construction uses the canonical native primitive order,
N01/N04/N06 of `01_NATIVE_ALGEBRA.md`, and PC1/PC4/PC5 of the Pāṇinian
operator compiler. It declares its own pairing and augmentation instead of
assuming an arbitrary matrix transpose or compression supplies them. T61's
finite realization is an earlier example, not a proof of this new carrier's
linguistic completeness or its integration into existing Python modules.
