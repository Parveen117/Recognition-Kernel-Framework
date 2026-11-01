# Piṅgala's Six Pratyayas as Exact Algorithms — the Chandas Vedāṅga on the laghu/guru carrier

1 November 2026. First Vedāṅga after Vyākaraṇa. The Pāṇini line continues in
`research/panini_grammar/` (external branch) and theorum/80–82; this capsule
opens the Chandas line from Piṅgala's own sūtras, quoted, with every result
an exact finite certificate on the two-letter carrier {l, g}.

## 1. Sources (quoted; Chandaḥśāstra adhyāya 8, standard printed numbering)

```text
8.20  dvikau glau                     the two: g, l
8.21  miśrau ca                       and their mixtures
8.22  pṛthag lā miśrāḥ                [prastāra] the l ones separately, under the mixed
8.23  vasavas trikāḥ                  the three-syllable forms are eight
8.24  l-ardhe                         [naṣṭa] on halving, l
8.25  saike g                         when one is added, g
8.26  pratilomagaṇaṁ dvir l-ādyam     [uddiṣṭa] reverse order; double from the first l
8.27  tato gy ekaṁ jahyāt             then at a g subtract one
8.28  dvir ardhe                      [saṅkhyā] two at a half
8.29  rūpe śūnyam                     at a unit, zero
8.30  dviḥ śūnye                      double at a zero
8.31  tāvad ardhe tad guṇitam         at a half, multiply by itself
8.32  dvir dvy ūnaṁ tad antānām       [adhvayoga] twice, less two, for all up to the end
8.34  pare pūrṇam ; 8.35 pare pūrṇam iti   [lagakriyā / meru, as Halāyudha reads it]
```

## 2. Results

**T1 Prastāra.** 8.20–8.23 enumerate the 2^n patterns without repetition
(n ≤ 12); row k, read with laghu = 1, guru = 0, is the little-endian binary
expansion of k − 1; the three-syllable table has eight rows (*vasavas*):
`ggg lgg glg llg ggl lgl gll lll`.

**T2 Naṣṭa / uddiṣṭa.** 8.24–8.25 and 8.26–8.27 are mutually inverse bijections
between {1, …, 2^n} and the prastāra rows, exhaustively for n ≤ 12
(`naṣṭa(4, 11) = glgl`, `uddiṣṭa(glgl) = 11`).

**T3 Saṅkhyā / adhvayoga.** Piṅgala's halving procedure 8.28–8.31 returns 2^n for
every n ≤ 64 using exactly ⌊log₂ n⌋ + popcount(n) multiplications — binary
exponentiation; 8.32 returns 2^(n+1) − 2 = Σ_{k=1}^{n} 2^k.

**T4 Meru.** 8.34–8.35 produce row n = the binomial coefficients = the number of
prastāra rows with r laghus, summing to the saṅkhyā (n ≤ 12). The Vedic pādas
of 8, 11 and 12 syllables (gāyatrī 24 = 3 × 8, triṣṭubh 44 = 4 × 11, jagatī
48 = 4 × 12) have prastāras of 256, 2048 and 4096 rows.

## 3. Certificate

```text
python -m proof_lab.pingala_chandas_pratyaya
python -m unittest proof_lab.test_pingala_chandas_pratyaya -v
```
Status `PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE`, SHA-256
`86da0a82489b815efebad7e2d5692fbebabb15098e22152493b6fa293d51a617`
(`proof_lab/PINGALA_CHANDAS_PRATYAYA_EXPECTED.sha256`). Exact integers and
Fractions only.

## 4. Claim boundary

```text
PRASTĀRA = 2^n ROWS, ROW k = LITTLE-ENDIAN BINARY OF k−1 (n ≤ 12)            PROVED
NAṢṬA ∘ UDDIṢṬA = UDDIṢṬA ∘ NAṢṬA = id (n ≤ 12)                               PROVED
SAṄKHYĀ = 2^n, ⌊log₂ n⌋ + popcount MULTIPLICATIONS (n ≤ 64); ADHVAYOGA = 2^(n+1) − 2   PROVED
MERU = BINOMIALS = r-LAGHU COUNTS, ROW SUM = SAṄKHYĀ (n ≤ 12)                PROVED
SŪTRA NUMBERING                                                              STANDARD EDITIONS; OTHERS DIFFER
8.34–8.35 AS MERU                                                            HALĀYUDHA'S READING, CITED
METRE LENGTHS 24 … 48                                                        TRADITIONAL TABLE, DECLARED
MĀTRĀ METRES, GAṆAS, METRE IDENTIFICATION OF VEDIC LINES, PĀTĀKĀ            NOT CLAIMED
RH, YM                                                                       UNTOUCHED
```
