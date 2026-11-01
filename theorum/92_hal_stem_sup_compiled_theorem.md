# The Consonant-Stem Sup Paradigms Compiled — rājan, ātman, marut; pada and bha load-bearing; 6.4.137 as a control

1 November 2026. Sixth nominal class: consonant stems. Here the saṁjñās that
decide everything are *pada* (1.4.17) and *bha* (1.4.18) — the same stem is
a pada before bhyām and a bha before ṅas — and the capsule shows each of them
breaking exactly its own cells, with ātman as the control for 6.4.137 and
marut for the Tripādī jaś / car alternation.

## 1. Sources (quoted)

```text
1.4.14  suptiṅantaṁ padam           1.4.17  svādiṣv asarvanāmasthāne      1.4.18  yaci bham         1.1.42 / 1.1.43
6.4.8   sarvanāmasthāne cāsambuddhau 6.1.68  halṅyābbhyo dīrghāt …          8.2.7   nalopaḥ prātipadikāntasya   8.2.8 na ṅisambuddhyoḥ
6.4.129 bhasya                      6.4.134 allopo 'naḥ                    6.4.136 vibhāṣā ṅiśyoḥ   6.4.137 na saṁyogād vamantāt
8.4.40  stoḥ ścunā ścuḥ             8.2.39  jhalāṁ jaśo 'nte               8.4.55  khari ca         8.4.56 vāvasāne
8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1 rājan.** rājā, rājānau, rājānaḥ; rājānam, rājānau, rājñaḥ; rājñā,
rājabhyām, rājabhiḥ; rājñe …; rājñaḥ …; rājñaḥ, rājñoḥ, rājñām; rājñi / rājani
(6.4.136), rājñoḥ, rājasu; he rājan — 22/22. **pada** breaks exactly the
consonant-initial cells {3d, 3p, 4d, 4p, 5d, 5p, 7p}; **bha** exactly the
vowel-initial non-sarvanāmasthāna cells {2p, 3s, 4s, 5s, 6s, 6d, 6p, 7s, 7d};
6.4.8 {1s, 1d, 1p, 2s, 2d}; 8.2.7 {1s and the pada cells}; 8.2.8 {8s};
6.4.134 and 8.4.40 the bha cells; 6.4.136 {7s}; 6.1.68 {1s, 8s}.

**T2 ātman.** 22/22; without 6.4.137 exactly the bha cells break, the blocked
form being *ātmnaḥ*.

**T3 marut.** 22/22; 8.2.39 breaks exactly {3d, 3p, 4d, 4p, 5d, 5p}
(marudbhyām …); 8.4.55 exactly {7p} (marud-su → marutsu); 8.4.56 restores the
car at pause (without it, *marud*). **Recorded:** on 7p the pada saṁjñā is not
load-bearing, because 8.2.39 and 8.4.55 return the t.

## 3. Certificate

```text
python -m proof_lab.hal_stem_sup_compiled
python -m unittest proof_lab.test_hal_stem_sup_compiled -v
```
Status `PASS_HAL_STEM_SUP_COMPILED_CANDIDATE`, SHA-256
`e1f6ab512415adf1632311d5d915e3cd85ed2b20a9229011be4cfa67d677330c`
(`proof_lab/HAL_STEM_SUP_COMPILED_EXPECTED.sha256`). Imports theorum/82.

## 4. Claim boundary

```text
rājan, ātman, marut: 66 FORMS; pada / bha AND EACH STAGE BREAK EXACTLY THEIR CELLS   PROVED
6.4.137 CONTROL (*ātmnaḥ WITHOUT IT); 8.2.39 / 8.4.55 / 8.4.56 ON marut                PROVED
vāc (8.2.30 AT PADA END), s / in / as STEMS, NEUTERS; OPTION MECHANICS OF 6.4.136      NOT CLAIMED
STEMS DECLARED PRĀTIPADIKAS; STAGE ORDER A DECLARED PIPELINE
RH, YM                                                                               UNTOUCHED
```
