# The Vedāṅga Packets 71–73 Bound to Their Quoted Sources — Piṅgala, Baudhāyana, Lagadha

1 November 2026. theorum/71 (Chandas), 72 (Śulba) and 73 (Jyotiṣa) were
certified from the owner's notes and the texts' integers, but did not quote
the sūtras and verses themselves. The repository's standing rule for the
Śaiva and Pāṇini lines (theorum/78–83) is that every statement starts from a
quoted primary text. This capsule quotes the three texts and certifies that
every number the three **pinned** packets use is the text's number — by
importing their functions and comparing; their pins are not touched.

## 1. Sources (quoted)

```text
Chandaḥśāstra 8 (Piṅgala; standard printed numbering)
  8.20 dvikau glau   8.21 miśrau ca   8.22 pṛthag lā miśrāḥ   8.23 vasavas trikāḥ
  8.24 l-ardhe   8.25 saike g   8.26 pratilomagaṇaṁ dvir l-ādyam   8.27 tato gy ekaṁ jahyāt
  8.28 dvir ardhe   8.29 rūpe śūnyam   8.30 dviḥ śūnye   8.31 tāvad ardhe tad guṇitam
  8.32 dvir dvy ūnaṁ tad antānām   8.34 pare pūrṇam   8.35 pare pūrṇam iti

Baudhāyana Śulbasūtra (Thibaut / Sen–Bag numbering)
  i.48 / 1.12     dīrghacaturasrasyākṣṇayā rajjuḥ pārśvamānī tiryaṅmānī ca
                  yat pṛthagbhūte kurutas tad ubhayaṁ karoti
  i.61–62 / 2.12  samasya dvikaraṇī / pramāṇaṁ tṛtīyena vardhayet tac
                  caturthenātmacatustriṁśonena saviśeṣaḥ

Ṛgveda Vedāṅga Jyotiṣa (Lagadha; GRETIL text)
  1   pañcasaṁvatsaramayaṁ yugādhyakṣaṁ prajāpatim
  4   nirekaṁ dvādaśārdhābdaṁ dviguṇaṁ gatasaṁjñikam /
      ṣaṣṭyā ṣaṣṭyā yutaṁ dvābhyāṁ parvaṇāṁ rāśir ucyate
  22  yad uttarasyāyanato gataṁ syāc cheṣaṁ tu yad dakṣiṇato 'yanasya /
      tad ekaṣaṣṭyā dviguṇaṁ vibhaktaṁ sadvādaśaṁ syād divasapramāṇam
  32  yugasya pañcavarṣasya kālajñānaṁ pracakṣate
```

## 2. Results

**T1 Chandas.** The procedures written from the sūtras — prastāra (8.20–8.23),
naṣṭa (8.24–8.25), uddiṣṭa (8.26–8.27), saṅkhyā (8.28–8.31), meru
(8.34–8.35) — equal theorum/71's pinned functions on every input, n ≤ 10
(meru n ≤ 12). **Discrepancy recorded:** 8.32 *dvir dvy ūnam* ("twice, less
two") gives adhvayoga = 2·2^n − 2, the sum over lengths 1..n; theorum/71's
pinned adhvayoga is 2·2^n − 1 — one more, for every n (it counts the empty
pattern). The pin is left as it is; the owner decides.

**T2 Śulba.** The cord read from i.61–62 — the measure increased by its third,
that by its fourth, less the thirty-fourth part of that — is 1 + 1/3 + 1/12 −
1/408 = **577/408** = theorum/72's `sqrt2_cord()`; the diagonal rule i.48 is
theorum/72's `diagonal_bindu = 0` on the text's six triples.

**T3 Jyotiṣa.** RVJ 1 / 32: five years = theorum/73's `YEARS`. RVJ 4's "sixty
and sixty, with two and two" = **124 parvans = 2 × 62** = theorum/73's
`SYN_MONTHS`, the two adhimāsas being 62 − 60. RVJ 22's day-length rule —
days elapsed from the northern solstice, doubled, divided by sixty-one, plus
twelve — equals theorum/73's `daylight(d)` for **every day** of the half-year
(12 at d = 0, 18 at d = 183): the zigzag of theorum/73 T4 is the verse.

## 3. Certificate

```text
python -m proof_lab.vedanga_sources_quoted
python -m unittest proof_lab.test_vedanga_sources_quoted -v
```
Status `PASS_VEDANGA_SOURCES_QUOTED_CANDIDATE`, SHA-256
`a13d6fe56945ec2faffa37a33ce38d12e17db349c8ceeee027b44f050f679fb1`
(`proof_lab/VEDANGA_SOURCES_QUOTED_EXPECTED.sha256`). Imports theorum/71, 72,
73; their pins `PINGALA_CHANDAS_PRATYAYA`, `SULBA_MEASURE_RESIDUE`,
`VEDANGA_JYOTISA_YUGA_LEDGER` are unchanged.

## 4. Claim boundary

```text
theorum/71 PRASTĀRA, NAṢṬA, UDDIṢṬA, SAṄKHYĀ, MERU = QUOTED 8.20–8.35 PROCEDURES     PROVED
theorum/71 ADHVAYOGA = LITERAL 8.32 + 1 FOR EVERY n                                 DISCREPANCY RECORDED, PIN UNTOUCHED
theorum/72 √2 CORD = BŚS i.61–62 READ LITERALLY (577/408); i.48 ON THE TRIPLES       PROVED
theorum/73 YEARS, 62 MONTHS (RVJ 4: 124 PARVANS), DAYLIGHT RULE (RVJ 22)            PROVED
1830 DAYS, 67 NAKṢATRA MONTHS, 1835 SIDEREAL DAYS, 1860 TITHIS (YAJUS RECENSION)     NOT QUOTED HERE — DECLARED INPUTS OF theorum/73
RVJ 4 AS THE YUGA'S PARVAN TOTAL                                                    KUPPANNA SASTRY'S READING
ŚULBA NUMBERING                                                                     BOTH SYSTEMS GIVEN; theorum/72 MIXES THEM, LEFT AS PINNED
RH, YM                                                                              UNTOUCHED
```
