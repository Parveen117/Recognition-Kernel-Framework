# PG8 — Source readings, scope, and retained derivations

Author: Monty. 1 November 2026.

The source edition is [ashtadhyayi-com/data at 5744762](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
[SOURCE_PINS.json](SOURCE_PINS.json) binds eight external files and 57
unchanged predecessor files. Kāśikā, Siddhāntakaumudī, Bālamanoramā,
Tattvabodhinī and Laghusiddhāntakaumudī are individually attributed. Their
presence on one platform is not independent-edition confirmation.

[RULE_RECORDS.json](RULE_RECORDS.json) supplies original Sanskrit, inherited
terms, operation roles and literal commentary anchors. These are manually
reviewed bounded contracts, not automatic interpretation of Sanskrit prose.

| Sūtra | Sanskrit and IAST | PG8 interpretation |
| --- | --- | --- |
| [1.3.66](https://ashtadhyayi.com/sutraani/1/3/66) | भुजोऽनवने — bhujo 'navane | A for the admitted non-protection meaning of the class-7 bhuj; homonymous class-6 bhuj is excluded |
| [7.3.92](https://ashtadhyayi.com/sutraani/7/3/92) | तृणह इम् — tṛṇaha im | im after śnam, with consonant-initial pit sārvadhātuka tiṅ |
| [8.2.31](https://ashtadhyayi.com/sutraani/8/2/31) | हो ढः — ho ḍhaḥ | tṛh's final h becomes ḍh before jhal; separate word-final cases are not implemented |
| [8.3.13](https://ashtadhyayi.com/sutraani/8/3/13) | ढो ढे लोपः — ḍho ḍhe lopaḥ | First ḍh disappears before ḍh in the admitted internal junction |
| [8.2.1](https://ashtadhyayi.com/sutraani/8/2/1) | पूर्वत्रासिद्धम् — pūrvatrāsiddham | Preserve ordered query views; the commentary licenses one named exception, not a global reverse pass |
| [1.1.47](https://ashtadhyayi.com/sutraani/1/1/47) | मिदचोऽन्त्यात्परः — mid aco 'ntyāt paraḥ | Place mit after the last vowel of its current host, including the root-with-śnam host for im |
| [1.3.3](https://ashtadhyayi.com/sutraani/1/3/3) | हलन्त्यम् — halantyam | Designate the original im teaching unit's final m |
| [1.3.9](https://ashtadhyayi.com/sutraani/1/3/9) | तस्य लोपः — tasya lopaḥ | Remove that designated m from the surface and retain its identity |
| [6.1.87](https://ashtadhyayi.com/sutraani/6/1/87) | आद्गुणः — ād guṇaḥ | Internal śnam a + im i gives e; both source sounds remain in the joint-substitution record |
| [2.4.72](https://ashtadhyayi.com/sutraani/2/4/72) | अदिप्रभृतिभ्यः शपः — adiprabhṛtibhyaḥ śapaḥ | Reuse inherited luk for identified ad/as; retain the deleted śap unit |
| [6.4.111](https://ashtadhyayi.com/sutraani/6/4/111) | श्नसोरल्लोपः — śnasor allopaḥ | Extend the earlier śnam contract to the identified as root; actual tiṅ features determine weakness |
| [7.4.50](https://ashtadhyayi.com/sutraani/7/4/50) | तासस्त्योर्लोपः — tāsastyor lopaḥ | Delete as's s before an s-initial affix; the tās branch is not implemented |

## Bhuj: a lexical label is not a contextual decision

The pinned Dhātupāṭha record 1070017 has pada P and the composite meaning
पालनाभ्यवहारयोः. Its own `pada_note` states that eating takes A. Kāśikā
1.3.66 explicitly limits the rule to the rudhādi entry, contrasting the
tudādi root meaning crookedness. Siddhāntakaumudī gives `महीं भुनक्ति`
and `ओदनं भुङ्क्ते`.

PG8 preserves the source row and admits two disambiguated requests: पालने/P
and अभ्यवहारे/A. The composite label, the crossed pairs and absent contextual
license return UNRESOLVED. This is an explicit semantic interface, not
automatic inference of meaning from spelling. Other non-protection senses
are not silently included merely because the traditional rule is broader.

## Tṛh: the augment's host changes after śnam

Kāśikā 7.3.92 says that the tṛṇah aṅga receives im under hal, pit and
sārvadhātuka conditions, and specifically requires śnam to have applied.
Bālamanoramā explains that without the composed tṛṇah designation one could
incorrectly treat im as displacing śnam. Its mit explanation places im after
the last vowel of the already assembled host.

The owned derivation is therefore:

1. Keep tṛh as one root. Place śnam after its ṛ by 1.1.47.
2. For strong qualifying tiṅ, prescribe im with a separate m-it owner. The
   host's last vowel is now śnam's a. The new augment enters after that a.
3. Apply 6.1.87 to a+i. The e sound carries both predecessor UIDs, with the
   augment as surface owner; the original root and śnam remain recoverable.
4. Before t/th, h → ḍh by 8.2.31 and t/th → dh by 8.2.40. For the 8.3.13
   query only, admit dh → ḍh by ṣṭutva, then delete the first ḍh. Ordered nasal
   processing yields tṛṇeḍhi or weak tṛṇḍhaḥ.

The early visibility is not an inference from a desired spelling. Kāśikā
8.3.13 expressly states `ष्टुत्वस्यात्र सिद्धत्वमाश्रयाद् द्रष्टव्यम्`.
Its discussion also denies a general reinterpretation as a jaśtva exception.
Bālamanoramā 7.3.92 gives the particular sequence of ḍhatva, dhatva, ṣṭutva
and ḍh-lopa for both strong and weak tṛh. The source-bound permission is
required by the executable query; removing it produces an error.

In weak forms 6.4.111 deletes śnam's a and there is no im. Before s, the
8.2.41 k path is used instead of ḍh-lopa. Before h/v/m junctions outside
jhal, h remains. Nasal readout gives tṛṃhanti, tṛṃhvaḥ and tṛṃhmaḥ in this
profile. Optional pronunciation doubling remains outside the spelling domain.

## Ad and as: two distinct kinds of deletion

Kāśikā 2.4.72 supplies śap-luk for adādi. The deleted affix retains its
identity and source markers; it is not treated as ordinary it-lopa. PG8
reuses PG5's already recorded 1.1.63 inhibition of guṇa from deleted śap.

For as, 6.4.111 removes root a before qualifying weak endings, yielding
staḥ/santi/sthaḥ/stha/svaḥ/smaḥ. Strong asti and asmi retain a. Before sip,
7.4.50 instead removes the root's s, leaving the ending's s and giving asi.
The earlier śnam-specific 1.1.58 nasal visibility record is not attached to
as's deletion. A general sthānivad or ābhīya engine is not claimed.

## Concurrent work and evidence grades

[CONCURRENT_REVIEW.json](CONCURRENT_REVIEW.json) pins the reviewed T86 source
blob at `7802a35`. Its bounded nominal work and shared lexical IDs are useful.
Its `kta_from_entry` function does not read `lex_id`, `ENTRIES` or `REFUSED`;
the certificate loop supplies its finite domain, while the refusal section
checks inventory membership and disjointness. This is a static API-boundary
finding, not a claim that its eleven tested stems fail. A future public adapter
must enforce that domain and retain its declared aniṭ premise.

PG8 consequently retains explicit lexical/sense guards, executable expected
refusals, and separate present/nominal coverage. The source corpus and old
reports are unchanged. No companion certificate, main merge, CI result,
universal grammar theorem or physical identification is inferred.

### T87 arrived during this review

The latest companion head is `ef8e982`, whose note points to T87 at
`7a88722`. Its four-root packet realizes pakta/labdha/tunna/lūna, with 88
reported nominal outputs. Its labdha order witness is useful; its own scope
correctly excludes general 8.2.1. PG8's tṛh path shows why a reusable schedule
must also carry source-declared query exceptions rather than sorting every
rule once and treating that as the whole grammar.

A targeted, isolated probe of T87's `r_8_2_40` on `(r,u,dh,t,i)` at boundary
3 leaves the t unchanged because the function excludes every preceding dh.
Kāśikā 8.2.40 excludes **dadhāti**, a lexical root, not all final dh sounds.
This probe is outside T87's four-root certificate; it identifies a future reuse
boundary, not failure of its four stated examples. The source anchor is pinned
in CONCURRENT_REVIEW.json. PG7's rudh path already applies the rule and yields
ruṇaddhi; PG8's targeted routing control preserves this correct distinction.
No companion certificate is replayed or changed. The T86 helper guard finding
also remains limited to reuse beyond its enclosing finite certificate loop.
