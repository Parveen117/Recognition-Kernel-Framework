# Rule-Table Engine II — s-stems, feminine i / u, neuter u and the kinship ṛ-stems as five new rows (manas, mati, dhenu, madhu, pitṛ, mātṛ: 132 cells)

2 November 2026. The multiplier at work. Six classes no earlier packet certified are added to theorum/125's table as **five rows** — 6.4.10 *sāntamahataḥ saṁyogasya* (manāṁsi), the pada-internal 8.2.66 *ru* with 6.1.114 *haśi ca* (manobhyām), 8.3.24 *naś cāpadāntasya jhali* (the anusvāra of manāṁsi), 8.3.15 before the khar s (manaḥsu) — and one guard generalisation (the ṛ flag: 7.1.94's anaṅ for every ṛ-stem, 6.4.11's dīrgha for the tṛ-class only, so pitarau against kartārau). The feminine i / u (mati, dhenu) and the neuter u (madhu) needed **no new row**: 7.3.120 *āṅo nāstriyām* already excludes the feminine (matyā), 7.3.111 gives mataye / mateḥ, 7.1.73 + 8.4.2 give madhunī; and one correction to the state: for a neuter only śi is sarvanāmasthāna (1.1.42 with 1.1.43 *suḍ anapuṁsakasya*), so no 6.4.8 before the neuter śī (madhunī, vāriṇī — not *madhūnī).

## 1. The new rows (cells of the 462 each breaks when removed)

```text
6.4.10   sāntamahataḥ saṁyogasya                  — 2   (manāṁsi 1p / 2p)
8.2.66p  sasajuṣo ruḥ, pada-internal               — 7   (manobhyām ×3, manobhiḥ, manobhyaḥ ×2, manaḥsu)
6.1.114  haśi ca (with 6.1.87)                    — 6   (manobhyām ×3, manobhiḥ, manobhyaḥ ×2)
8.3.24   naś cāpadāntasya jhali                   — 2   (manāṁsi 1p / 2p)
8.3.15p  kharavasānayor visarjanīyaḥ, before su   — 1   (manaḥsu)
```

## 2. Results

- 462 / 462 cells: the fifteen certified paradigms of theorum/125 (330) plus manas, mati, dhenu, madhu, pitṛ, mātṛ (132, declared from the Siddhāntakaumudī paradigms as oracles); every one of the 69 rows load-bearing.
- mātṝḥ against pitṝn: 6.1.103 *tasmāc chaso naḥ puṁsi* fires on the masculine only — the gender guard is load-bearing on exactly that pair.
- mati / dhenu are realised in the non-nadī branch (mataye, mateḥ, matau); the 1.4.6 *ṅiti hrasvaś ca* option (matyai, matyāḥ, matyām) and 8.3.36 *vā śari* (manassu) are recorded, not realised (set-valued output remains theorum/118 D4's channel).

## 3. Certificate

The certificate is theorum/125's module, re-pinned: `proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256` = `3a7b26cd6c4c72ff78692333c9d5db5793718123f1cbaa9427e0acc09fd4a163` (status `PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE`); the previous pin `6263db862e2afba169867a52ae1536c90350728555a05d4d07b89bf992ea5c8d` is in the history (commit bb9d8d4). Re-pinned again by theorum/127 (numerals), commit 671a790 holds this pin.

```text
python -m proof_lab.sup_rule_table_engine
python -m unittest proof_lab.test_sup_rule_table_engine -v
```

## 4. Claim boundary

```text
SIX NEW CLASSES, 132 CELLS, FROM FIVE ROWS AND ONE GUARD; 69 ROWS ALL LOAD-BEARING ON 462 CELLS     PROVED
THE DECLARED ORACLES OF THE SIX CLASSES (SIDDHĀNTAKAUMUDĪ PARADIGMS)                                 DECLARED
1.4.6 AND 8.3.36 OPTIONS AS SET-VALUED OUTPUT                                                        NOT CLAIMED
RH, YM                                                                                               UNTOUCHED
```
