# Chandas — Piṅgala's Pratyayas, the Meru Closure, the Mātrā-Meru, and the Gāyatrī's Own Metre

Owner's note (Vedic repo): {L, G}, w(L)=1, w(G)=2; Prastāra(n) = {L,G}ⁿ; meru
closure `M(n,r) − M(n−1,r−1) − M(n−1,r) − S_M = 0`; meter closure K_C.

## T1 Pratyayas (Chandaḥ-sūtra 8.20–8.35), exact
prastāra in Piṅgala's order (row 1 = Gⁿ, last = Lⁿ); **naṣṭa ∘ uddiṣṭa = id =
uddiṣṭa ∘ naṣṭa** on every row, n ≤ 10; lagakriyā = meru = prastāra counts;
saṅkhyā by doubling/squaring = 2ⁿ; adhvayoga = 2·2ⁿ − 1.

## T2 Meru closure — and what S_M is
With the correct boundary, S_M = 0 for n ≤ 12; row sums = saṅkhyā.
*Build note:* the first control measured a planted wrong boundary against the
recursion itself and got residue 0 — a wrong boundary propagates
consistently. Measured against the **recognized object** (the prastāra's own
counts) it shows the defect. So S_M must be Rec-anchored, exactly as the
owner's note writes it — not a self-consistency check. (56 B5's binomial law
is the same object; not re-claimed.)

## T3 Mātrā-meru
Patterns of total weight m obey F(m) = F(m−1) + F(m−2), F(1)=1, F(2)=2
(Virahāṅka), by enumeration to m = 16.

## T4 The Gāyatrī's metre from theorum/67's text
laghu/guru by 1.4.10–12 (hrasvaṃ laghu; saṃyoge guru; dīrghaṃ ca; anusvāra /
visarga guru):
```text
tat savitur vareṇyaṃ        7 syllables   GLLGLGG      (as written)
bhargo devasya dhīmahi      8             GGGGLGLL     uddiṣṭa #…
dhiyo yo naḥ pracodayāt     8             LGGGLGLG
```
**As written the first pāda has seven syllables.** The gāyatrī metre (3 × 8 =
24) is reached only with the traditional metrical restoration **vareṇiyam**
(svarabhakti) — a declared Vedic recitation reading, not a sūtra of the
engine. Both counts certified (7-8-8 written; 8-8-8 restored). The
certificate surfaced a well-known fact the tradition knows and a naive
counter would miss.

## Certificate
```text
python proof_lab/pingala_chandas_pratyaya.py
python -m unittest proof_lab.test_pingala_chandas_pratyaya -v
```
`PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE`, SHA-256 `316a794e34981420da9e1151440e5e66ec31323a764a81862be10ce9cd718568`.

## Claim boundary
```text
SIX PRATYAYAS EXACT; naṣṭa/uddiṣṭa INVERSE; MERU = PRASTĀRA COUNTS         PROVED
MERU CLOSURE S_M = 0; S_M IS Rec-ANCHORED (planted control)                PROVED
MĀTRĀ-MERU VIRAHĀṄKA RECURSION (m ≤ 16)                                    PROVED
GĀYATRĪ 7-8-8 AS WRITTEN; 8-8-8 WITH DECLARED vareṇiyam                    PROVED / DECLARED
ACCENT; CAESURA; OTHER VṚTTAS                                              NOT CLAIMED
RH, YM                                                                     UNTOUCHED
```
