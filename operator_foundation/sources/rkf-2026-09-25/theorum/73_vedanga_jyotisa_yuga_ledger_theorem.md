# Jyotiṣa — Lagadha's Yuga as an Exact Cyclic Ledger

Owner's note (Vedic repo, *Jyotisha Siddhanta Cyclic Recognition Engine*):
Kāla = cycles with Phase and Wind; calendar = phase ordering + cycle count +
**intercalation Smṛti**; prediction gap K = Res − S = 0. Executed on the
Vedāṅga Jyotiṣa's own integers — 5 years × 366 = 1830 days, 62 cāndra months
= 1860 tithis, 67 nakṣatra months, 1835 sidereal days, 2 adhimāsas.

## T1 The intercalation Smṛti closes the yuga exactly
One year's solar–lunar residue: 12·(1830/62) − 366 = **−366/31** day. Over five
years: **−1830/31 day = exactly −2 synodic months.** So S = 2 adhimāsa gives
K_yuga = 0 with no remainder: 60 + 2 = 62. The owner's closure law holds on
the text's numbers with equality, not approximation.

## T2 Ledgers
1860 − 1830 = 30 omitted (kṣaya) tithis; tithi = 61/62 day; 1835 − 1830 = 5 =
the years — one extra rotation per solar year.

## T3 Wind / Phase
For day, tithi, synodic month, sidereal month, sidereal day, year: Phase(1830)
= 0 and Wind(1830) integer (1830, 1860, 62, 67, 1835, 5); **no earlier day
closes all cycles** — 1830 is the least common closure.

## T4 Daylight zigzag (VJ water clock)
12 → 18 → 12 muhūrtas over 183 + 183 days, linear; solstice ratio 3:2,
equinox 15, symmetric, total 366·15 exactly.

## T5 Calendar ∼ chandas
The yuga's intercalation pattern (62 months, adhimāsa at the middle and the
end) is a word of theorum/71's prastāra with an uddiṣṭa index and lagakriyā
count C(62,2) = 1891. The owner's "calendar cycle ∼ metrical cycle" is
certified as a **representation**; nothing deeper is claimed.

## Certificate
```text
python proof_lab/vedanga_jyotisa_yuga_ledger.py
python -m unittest proof_lab.test_vedanga_jyotisa_yuga_ledger -v
```
`PASS_VEDANGA_JYOTISA_YUGA_LEDGER_CANDIDATE`, SHA-256 `569b61ea6a8ab4852bd422faf68228c55ff5fed817f21e670a972e630b964295`.

## Claim boundary
```text
5-YEAR RESIDUE = −2 SYNODIC MONTHS = INTERCALATION SMṚTI; K_yuga = 0 EXACT   PROVED
TITHI/KṢAYA; SIDEREAL − CIVIL = YEARS; PHASES ZERO AT 1830, NOT BEFORE        PROVED
DAYLIGHT ZIGZAG EXACT                                                         PROVED
CALENDAR ∼ CHANDAS AS PRASTĀRA REPRESENTATION                                 PROVED (representation)
DṚK CHANNEL / PREDICTION GAP; PRECESSION; ASTRONOMICAL ACCURACY OF 366        NOT CLAIMED
RH, YM                                                                        UNTOUCHED
```
