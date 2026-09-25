# Pada → Line: the Gāyatrī from its padas by external sandhi

Carrier: a line = tuple of padas in their pada-final form *before* pause
rules. Rules act on seams between padas or at avasāna:
8.2.66 ruḥ · 6.1.113 ato ror aplutād aplute · 6.1.114 haśi ca · 6.1.87 ād guṇaḥ
· 8.3.15 kharavasānayor visarjanīyaḥ (khar / pause only) · 8.3.23 mo'nusvāraḥ.

## T1 The text
```text
tat savitur vareṇyaṃ bhargo devasya dhīmahi     = received text
dhiyo yo naḥ pracodayāt                          = received text
```
savitur + v: ru stays r before a voiced consonant. bhargas + d: ruḥ → u
(6.1.114) → guṇa (6.1.87) → bhargo. dhiyas + y, yas + n: same chain. nas + p:
visarga before khar. vareṇyam + bh: anusvāra.

## T2 Provenance — counted, not blurred
```text
DERIVED (theorum/63/65):  tat  savitur  vareṇyam  bhargas  devasya          5
GIVEN (sector named):     dhīmahi (chandasi bahulam, 66)  dhiyas (6.4.77 iyaṅ)
                          yas (masc sarvanāma 7.2.106)  nas (8.1.21 asmad)
                          pracodayāt (ṇic + āśīrliṅ)                          5
```
So the Gāyatrī is **half derived by sūtra, half given** — the honest number.

## T3 Controls
Planted unconditional 8.3.15 → \*savituḥ vareṇyaṃ (wrong); without 6.1.87 the
bhargas seam stalls at a+u. Both refused by the certificate.

## T4 Confluence
theorum/60 verdict on each line under free application: CONFLUENT_MOD_LEDGER,
unique normal form (a generalisation of `repr_state` to nested carriers was
needed; theorum/60's pin is unchanged).

## Certificate
```text
python proof_lab/pada_to_line_external_sandhi.py
python -m unittest proof_lab.test_pada_to_line_external_sandhi -v
```
`PASS_PADA_TO_LINE_EXTERNAL_SANDHI_CANDIDATE`, SHA-256 `75d6abbbabf1498ef49d23067398a47c3ff3a5a64104b6184988137693b923a9`.

## Claim boundary
```text
GĀYATRĪ LINES FROM PADAS BY EXTERNAL SANDHI = RECEIVED TEXT          PROVED
LINES CONFLUENT, UNIQUE NORMAL FORM                                  PROVED
5 PADAS DERIVED / 5 GIVEN (sectors named)                            RECORDED
ACCENT; JIHVĀMŪLĪYA/UPADHMĀNĪYA OPTIONS; AVAGRAHA                    NOT CLAIMED
RH, YM                                                               UNTOUCHED
```
