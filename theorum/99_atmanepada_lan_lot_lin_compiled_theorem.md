# Laṅ, Loṭ and Vidhi-Liṅ Ātmanepada Compiled — labh and edh on Theorem 66's stems; 3.4.90–93 and the sīyuṭ chain; āṭ for the vowel-initial root

1 November 2026. theorum/66 gave laṭ ātmanepada of edh and labh. This capsule
adds the three further lakāras on the same śap stems: the imperfect with aṭ
(6.4.71) or āṭ (6.4.72, with 6.1.90: aidhata), the imperative with Pāṇini's
ātmanepada substitutions 3.4.90–93, and the optative with sīyuṭ (3.4.102) cut
down by 7.2.79 and 6.1.66 to the *e* of labheta.

## 1. Sources (quoted)

```text
1.3.12 anudāttaṅita ātmanepadam   3.4.78 ; 3.4.79 ṭita ātmanepadānāṁ ṭer e ; 3.4.80 thāsaḥ se
6.4.71 luṅlaṅlṛṅkṣv aḍ udāttaḥ    6.4.72 āḍ ajādīnām   6.1.90 āṭaś ca   7.2.81 āto ṅitaḥ   6.1.66 lopo vyor vali   6.1.97 ato guṇe   6.1.87 ād guṇaḥ   7.1.3   7.3.101
3.4.90 ām etaḥ   3.4.91 savābhyāṁ vāmau   3.4.92 āḍ uttamasya pic ca   3.4.93 eta ai
3.4.102 liṅaḥ sīyuṭ   3.4.105 jhasya ran   3.4.106 iṭo 't   3.4.107 suṭ tithoḥ   7.2.79 liṅaḥ salopo 'nantyasya   8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1 laṅ.** alabhata, alabhetām, alabhanta; alabhathāḥ, alabhethām,
alabhadhvam; alabhe, alabhāvahi, alabhāmahi; aidhata … aidhāmahi — 18/18.
6.4.71 breaks all nine of labh; **6.4.72 breaks all nine of edh and none of
labh**; 7.1.3 {3p}; 7.2.81 and 6.1.66 {3d, 2d}; 6.1.97 {3d, 2d, 1s}; 7.3.101
{1d, 1p}; 8.2.66 {2s}. Recorded: on 1s the ṭi-to-e of 3.4.79 and the plain
iṭ reach the same surface (alabhe) through 6.1.97.

**T2 loṭ.** labhatām, labhetām, labhantām; labhasva, labhethām, labhadhvam;
labhai, labhāvahai, labhāmahai; edhatām … — 18/18. 3.4.90 breaks exactly
{3s, 3d, 3p, 2d}; 3.4.91 {2s, 2p}; 3.4.93 {1s, 1d, 1p}; 3.4.80 {2s}; 7.1.3 {3p};
7.2.81 / 6.1.66 {3d, 2d}. Recorded: 3.4.92's āṭ coincides on the surface with
7.3.101 / 6.1.88 (labhāvahai, labhai).

**T3 vidhi-liṅ.** labheta, labheyātām, labheran; labhethāḥ, labheyāthām,
labhedhvam; labheya, labhevahi, labhemahi; edheta … — 18/18. 3.4.102, 7.2.79
and 6.1.87 each break all nine; 3.4.105 {3p}; 3.4.106 {1s}; 6.1.66 the six
consonant-initial cells; **7.3.101 is blocked by sīyuṭ** (labhevahi);
recorded: 3.4.107's suṭ is removed again by 7.2.79, so removing 3.4.107
changes no surface form.

## 3. Certificate

```text
python -m proof_lab.atmanepada_lan_lot_lin_compiled
python -m unittest proof_lab.test_atmanepada_lan_lot_lin_compiled -v
```
Status `PASS_ATMANEPADA_LAN_LOT_LIN_COMPILED_CANDIDATE`, SHA-256 `494ca1c894b7a576a97d7b8dfbf79f837726ea9d49a2ed56f5609d4e014489ea`
(`proof_lab/ATMANEPADA_LAN_LOT_LIN_COMPILED_EXPECTED.sha256`). Imports theorum/82.

## 4. Claim boundary

```text
laṅ, loṭ, vidhi-liṅ ĀTMANEPADA OF labh, edh: 54 FORMS; EACH STAGE BREAKS EXACTLY ITS CELLS   PROVED
6.4.72 / 6.1.90 ON THE VOWEL-INITIAL ROOT ONLY; 7.3.101 BLOCKED BY sīyuṭ                      PROVED
3.4.79 (laṅ 1s), 3.4.92 (loṭ), 3.4.107 (liṅ): SURFACE-NEUTRAL HERE                            RECORDED
OTHER ROOTS, luṅ / liṭ / lṛṭ ĀTMANEPADA, 3.4.95–96, ACCENT                                     NOT CLAIMED
STAGE ORDERS DECLARED PIPELINES ; RH, YM UNTOUCHED
```
