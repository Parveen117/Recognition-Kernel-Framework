# Tiṅ Carrier — laṭ parasmaipada of bhū and gam (18 forms) and a real earlier-apavāda

State: (root, vikaraṇa, tiṅ, features) — three morphemes, two seams. Sūtras:
3.2.123 laṭ, 3.4.78 tiṅ, 1.4.99/1.4.101 (declared), 3.1.68 kartari śap,
3.4.113 sārvadhātuka, 1.3.3/1.3.8/1.3.9 it-lopa, 7.1.3 jho'ntaḥ, 7.3.84 guṇa,
6.1.78 ayādi, **6.1.97 ato guṇe**, 6.1.101 savarṇadīrgha, 7.3.101 ato dīrgho
yañi, 7.3.77 chaḥ, 6.1.73 tuk, 8.4.40 ścutva, 8.2.66 ruḥ, 8.3.15 visarga.

## T1 Soundness
18/18: bhavati bhavataḥ bhavanti bhavasi bhavathaḥ bhavatha bhavāmi bhavāvaḥ
bhavāmaḥ; gacchati gacchataḥ gacchanti gacchasi gacchathaḥ gacchatha gacchāmi
gacchāvaḥ gacchāmaḥ — match the oracle.

## T2 A real earlier-apavāda on Pāṇini's own data
At bhava+anti both 6.1.97 (pararūpa) and 6.1.101 (dīrgha) apply. **6.1.97 is
numbered before its utsarga**, so para alone gives \*bhavānti. With apavāda =
grammar-wide domain containment (6.1.101's extra scope a+ā lives in the
nominal carrier of theorum/63), the ladder gives **bhavanti**. Yesterday's
planted control is today a theorem: para is insufficient, and apavāda needs
the whole grammar's carrier, not one paradigm — *niravakāśatva* made
executable.
*Build notes (certificate refusals):* (i) on the tiṅ carrier alone the two
domains coincide and the rung was blind → domains unioned across carriers;
(ii) saṃjñā rule 3.4.113 blocked an all-vs-all apavāda check → resolver v2
(8.2.1 first, nirvirodha, pairwise ladder among conflicting rules); (iii)
ayādi had to read the next phone across an emptied vikaraṇa.

## T3 Census
Rungs used: nirvirodha, apavāda(/nitya), 8.2.1; para disagrees at several states.

## T4 Memory
All 9 bhū forms break without it-marker memory (the sārvadhātuka saṃjñā lives
only in memory); gam survives by reading the undeleted Ś-phone before lopa —
the theorum/58 T3 order-dependence, now visible on a paradigm. *Draft expected
all 18 to break; refused.*

## T5 8.2.1 on every path; normal forms are free normal forms; lopa on every path.

## Certificate
```text
python proof_lab/ting_lat_parasmaipada.py
python -m unittest proof_lab.test_ting_lat_parasmaipada -v
```
`PASS_TING_LAT_PARASMAIPADA_CANDIDATE`, SHA-256 `073705dabbd629242140637068f55ef4f7cfb256674f09a9e7251ba6b071feb9`.

## Claim boundary
```text
18/18 laṭ PARASMAIPADA FORMS (bhū, gam) FROM CANONICAL SŪTRAS         PROVED
REAL EARLIER-APAVĀDA 6.1.97 ⊊ 6.1.101; para ALONE GIVES *bhavānti       PROVED
APAVĀDA DOMAINS ARE GRAMMAR-WIDE (nominal ∪ verbal carriers)            PROVED (load-bearing)
MEMORY LOAD-BEARING FOR ALL bhū FORMS                                   PROVED
ĀTMANEPADA; OTHER LAKĀRAS; OTHER GAṆAS; ACCENT; COMPLETENESS            NOT CLAIMED
RH, YM                                                                  UNTOUCHED
```
