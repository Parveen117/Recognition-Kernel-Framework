# Nāma from the Pinned Dhātupāṭha — Theorem 85 extended to the PG5 / PG6 lexical entries, with their ākhyāta forms as the other half

1 November 2026. The PG5 / PG6 stages (`research/panini_grammar/vikarana_lat`,
`non_thematic_lat`) pinned Dhātupāṭha entries by record id, with the
aupadeśika form in Devanagari (candrabindu for the anunāsika it) and their
laṭ reference forms. This capsule reads those entries directly: theorum/82's
it-interpreter takes the Devanagari teaching form, kta follows as in
theorum/85, and theorum/63's pinned ladder gives the nouns; the PG stages'
own laṭ forms supply the ākhyāta side of Yāska's partition.

## 1. Sources

```text
Pinned lexical entries (Dhātupāṭha record ids): 1010001 भू, 1050001 षुञ्, 1050005 चिञ्, 1050016 आपॢँ,
  1050017 शकॢँ, 1080001 तनुँ, 1080010 डुकृञ्, 1090001 डुक्रीञ्, 1011092 श्रु, 1090014 पूञ्, 1030001 हु
Nirukta 1.12 (theorum/85) ; Aṣṭādhyāyī 1.3.2–1.3.9 (theorum/82) ; 1.1.26, 3.2.102, 1.2.46, 4.1.2, 1.4.14 (theorum/85)
6.1.64  dhātvādeḥ ṣaḥ saḥ      6.4.37 (theorum/85)      7.2.10 (theorum/85)      8.2.44 lvādibhyaḥ (cited)
```

## 2. Results

**T1 Eleven kta-prātipadikas, 242 nouns.** From the pinned forms: bhū → bhūta,
ṣuñ → **suta** (6.1.64, fires here only), ciñ → cita, āpḷ~ → āpta, śakḷ~ →
śakta, tanu~ → **tata** (6.4.37, fires here only), ḍukṛñ → kṛta, ḍukrīñ →
krīta (1.3.5), śru → śruta, pūñ → pūta, hu → huta. theorum/63's pinned ladder
derives all 22 sup forms of each: **242 forms**, equal to the rāma paradigm
with the stem exchanged (no 8.4.2 ṇatva: the stem's *t* intervenes).

**T2 Ākhyāta from PG5 / PG6.** The laṭ 3sg forms those stages pin for the same
entries — भवति, सुनोति, चिनोति, आप्नोति, शक्नोति, तनोति, करोति, क्रीणाति, शृणोति,
पुनाति — are read from the repository and are disjoint from the 242 nāma
forms; हु has no PG case and stands nāma-only.

**T3 Refusals.** लूञ् (8.2.44 lūna), अदँ (2.4.36 jagdha), डुपचँष् (8.2.30
pakta), डुलभँष् (8.2.40 / 8.4.53 labdha), तुदँ (8.2.42 tunna), दिवुँ
(samprasāraṇa dyūta) need rules not realized and are refused by name. (Four of these — pakta, labdha, tunna, lūna — are realized in theorum/87; this certificate's refusals and pin stand as recorded.)

Note (after external review): `kta_from_entry` now refuses any lexical id outside the admitted eleven instead of merely listing refusals; the certificate output and pin are unchanged.

## 3. Certificate

```text
python -m proof_lab.nirukta_dhatupatha_nama
python -m unittest proof_lab.test_nirukta_dhatupatha_nama -v
```
Status `PASS_NIRUKTA_DHATUPATHA_NAMA_CANDIDATE`, SHA-256
`fdd0f424280bf180ba92c1b00a1f90423c9c36a232230c154acd8d38b71464d2`
(`proof_lab/NIRUKTA_DHATUPATHA_NAMA_EXPECTED.sha256`). Reads the PG5 / PG6
`LEXICAL_ENTRIES.json` and `REFERENCE_CASES.json` as pinned data; imports
theorum/82, 63, 85 and the ledger's transliteration; no pin is changed.

## 4. Claim boundary

```text
ELEVEN kta-PRĀTIPADIKAS FROM THE PINNED DEVANAGARI TEACHING FORMS (82-its, 6.1.64, 6.4.37, 7.2.10)   PROVED
242 SUP FORMS BY theorum/63's PINNED LADDER                                                         PROVED
PG5 / PG6 LAṬ 3SG FORMS DISJOINT FROM THE NĀMA FORMS                                                 PROVED (PG forms read, not re-derived)
SIX ENTRIES REFUSED BY THE RULE THEY NEED                                                           HONEST REFUSAL
ANIṬ STATUS                                                                                         DECLARED (accent not carried)
GĀRGYA'S "na sarvāṇi"                                                                               NOT DECIDED
RH, YM                                                                                              UNTOUCHED
```
