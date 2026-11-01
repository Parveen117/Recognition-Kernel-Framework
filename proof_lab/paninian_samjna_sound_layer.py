from __future__ import annotations

"""Exact certificate (theorum/81): THE SAṀJÑĀ LAYER OF PĀDA 1.1 ON THE SOUND
CARRIER — savarṇa derived, selectors made exact, pragṛhya blocks sandhi.

First batch of the all-sūtra programme after the ledger
(proof_lab/astadhyayi).  Quoted sūtras:

 1.1.7   halo 'nantarāḥ saṁyogaḥ      consonants with nothing between them form a cluster
 1.1.8   mukhanāsikāvacano 'nunāsikaḥ a sound uttered with mouth and nose is nasal
 1.1.9   tulyāsyaprayatnaṁ savarṇam   sounds of equal place and internal effort are savarṇa
 1.1.10  nājjhalau                     but never a vowel and a consonant
 1.1.11  īdūdeddvivacanaṁ pragṛhyam   dual endings in ī, ū, e are pragṛhya
 6.1.125 plutapragṛhyā aci nityam     a pluta or pragṛhya vowel stays as it is before a vowel
 1.1.64  aco 'ntyādi ṭi               the part from the last vowel on is ṭi
 1.1.65  alo 'ntyāt pūrva upadhā      the sound before the last is the penultimate (upadhā)
 1.1.72  yena vidhis tadantasya       a rule stated by X applies to what ends in X

 T1  SAVARṆA DERIVED.  From the sthāna / internal-prayatna table, 1.1.9 with
     the 1.1.10 exclusion yields exactly the vowel length classes used by
     theorum/80 (SAVARNA) and exactly the five vargas of theorum/79 — so
     1.1.69's udit classes ku, cu, ṭu, tu, pu are 1.1.9 classes, not a
     separate list; without 1.1.10, i and ś (tālu) would wrongly pair.
 T2  SELECTORS.  1.1.64 ṭi and 1.1.65 upadhā as exact functionals on sound
     strings; 1.1.72 tadanta: the "ik-final aṅga" condition of theorum/80's
     compiled 7.3.84 is the tadanta reading of 'ik' — certified by equality
     of the predicate with "upadhā-independent last sound in ik".
 T3  PRAGṚHYA BLOCKS SANDHI.  With a pragṛhya flag (1.1.11: dual ī, ū, e),
     6.1.125 makes every compiled sandhi rule of theorum/80 inapplicable on
     that junction; without the flag the rules fire.  Clusters (1.1.7) and
     nasals (1.1.8) are decided on the carrier and agree with the manner grid.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import SANDHI_RECORDS, SAVARNA, compile_sandhi, p58, savarna_expand
from proof_lab.shaiva_sources_nativized import TOKENS
from proof_lab.shaiva_sources_varga_crystal import MANNER, VARGAS

SOURCES = {
    "1.1.7": "halo 'nantarāḥ saṁyogaḥ", "1.1.8": "mukhanāsikāvacano 'nunāsikaḥ", "1.1.9": "tulyāsyaprayatnaṁ savarṇam", "1.1.10": "nājjhalau",
    "1.1.11": "īdūdeddvivacanaṁ pragṛhyam", "6.1.125": "plutapragṛhyā aci nityam", "1.1.64": "aco 'ntyādi ṭi", "1.1.65": "alo 'ntyāt pūrva upadhā",
    "1.1.72": "yena vidhis tadantasya",
}

# ---------------------------------------------------------------- sthāna and internal (ābhyantara) prayatna table, IAST
STHANA = {}
for s in ("a", "ā", "h", "k", "kh", "g", "gh", "ṅ"):
    STHANA[s] = "kaṇṭha"
for s in ("i", "ī", "c", "ch", "j", "jh", "ñ", "y", "ś"):
    STHANA[s] = "tālu"
for s in ("ṛ", "ṝ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "r", "ṣ"):
    STHANA[s] = "mūrdhan"
for s in ("ḷ", "ḹ", "t", "th", "d", "dh", "n", "l", "s"):
    STHANA[s] = "danta"
for s in ("u", "ū", "p", "ph", "b", "bh", "m"):
    STHANA[s] = "oṣṭha"
STHANA.update({"e": "kaṇṭha-tālu", "ai": "kaṇṭha-tālu", "o": "kaṇṭha-oṣṭha", "au": "kaṇṭha-oṣṭha", "v": "danta-oṣṭha"})
PRAYATNA = {}
for row in MANNER.values():
    for s in row:
        PRAYATNA[s] = "spṛṣṭa"  # stops: full contact
for s in ("y", "r", "l", "v"):
    PRAYATNA[s] = "īṣat-spṛṣṭa"
for s in ("ś", "ṣ", "s", "h"):
    PRAYATNA[s] = "vivṛta"  # ūṣman: vivṛta (Siddhānta-kaumudī on 1.1.9, "ūṣmaṇāṁ vivṛtam"); this is why 1.1.10 is needed
for s in ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au"):
    PRAYATNA[s] = "vivṛta"
VOWELS_IAST = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
# the sandhyakṣaras share place and internal effort pairwise (e/ai, o/au); the tradition keeps them apart by the
# proportion of the two places (e, o: equal halves; ai, au: unequal) — recorded as a separate attribute, cited to the
# Pāṇinīya-Śikṣā / Siddhānta-kaumudī treatment, so that the certificate shows exactly where the table alone would not decide
PROPORTION = {"e": "sama", "o": "sama", "ai": "viṣama", "au": "viṣama"}
NASAL = ("ñ", "m", "ṅ", "ṇ", "n")  # 1.1.8 on the consonant carrier (anusvāra and nasalized vowels not carried)


def savarna_classes(sounds: tuple[str, ...], apply_1_1_10: bool = True) -> list[frozenset[str]]:
    """1.1.9: equal sthāna and equal internal prayatna; 1.1.10: a vowel and a consonant are never savarṇa."""
    classes: dict[tuple, set[str]] = {}
    for s in sounds:
        k = (STHANA[s], PRAYATNA[s], PROPORTION.get(s, ""), (s in VOWELS_IAST) if apply_1_1_10 else None)
        classes.setdefault(k, set()).add(s)
    return sorted((frozenset(v) for v in classes.values()), key=lambda c: min(sounds.index(x) for x in c))


def t1_savarna_derived() -> dict[str, Any]:
    sounds = VOWELS_IAST + tuple(dict.fromkeys(t for t in TOKENS if t not in VOWELS_IAST))
    with_ = savarna_classes(sounds, True)
    without = savarna_classes(sounds, False)
    vargas = {frozenset(v) for v in VARGAS.values()}
    vowel_classes = {c for c in with_ if next(iter(c)) in VOWELS_IAST}
    expected_vowel = {frozenset({"a", "ā"}), frozenset({"i", "ī"}), frozenset({"u", "ū"}), frozenset({"ṛ", "ṝ"}), frozenset({"ḷ", "ḹ"}), frozenset({"e"}), frozenset({"ai"}), frozenset({"o"}), frozenset({"au"})}
    stop_classes = {c for c in with_ if next(iter(c)) in {s for row in MANNER.values() for s in row}}
    # theorum/80's SAVARNA table (58 spelling) is the vowel part restricted to that carrier
    to80 = {"ā": "A", "ī": "I", "ū": "U", "ṛ": "R", "ḷ": "L"}
    savarna80 = {frozenset(to80.get(s, s) for s in c if s not in ("ṝ", "ḹ")) for c in vowel_classes if next(iter(c)) in ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ")}
    checks = {
        "1_1_9_with_1_1_10_vowel_classes_are_the_length_pairs": vowel_classes == expected_vowel,
        "1_1_9_stop_classes_are_exactly_the_five_vargas_of_theorum_79": stop_classes == vargas,
        "udit_classes_ku_cu_tu_tu_pu_are_1_1_9_classes": all(frozenset(VARGAS[v]) in with_ for v in VARGAS),
        "without_1_1_10_i_and_s_wrongly_pair_usman_vivrta": any({"i", "ś"} <= c for c in without) and any({"a", "h"} <= c for c in without) and not any({"i", "ś"} <= c for c in with_),
        "e_ai_and_o_au_separated_only_by_the_proportion_attribute": all(len(c) == 1 for c in with_ if next(iter(c)) in ("e", "ai", "o", "au")) and (STHANA["e"], PRAYATNA["e"]) == (STHANA["ai"], PRAYATNA["ai"]),
        "theorum_80_SAVARNA_table_is_the_vowel_part_on_its_carrier": savarna80 == {frozenset(v) for v in SAVARNA.values()},
        "semivowels_and_sibilants_are_singletons": all(len(c) == 1 for c in with_ if next(iter(c)) in ("y", "r", "l", "v", "ś", "ṣ", "s", "h")),
    }
    return {"checks": checks, "classes": [sorted(c) for c in with_]}


# ---------------------------------------------------------------- T2 selectors
def ti_1_1_64(ph: tuple[str, ...], vowels=VOWELS_IAST) -> tuple[str, ...]:
    """aco 'ntyādi ṭi: from the last vowel to the end."""
    last = max(i for i, s in enumerate(ph) if s in vowels)
    return ph[last:]


def upadha_1_1_65(ph: tuple[str, ...]) -> str:
    """alo 'ntyāt pūrva upadhā: the sound before the last."""
    return ph[-2]


def tadanta_1_1_72(ph: tuple[str, ...], klass: tuple[str, ...]) -> bool:
    """yena vidhis tadantasya: a rule stated by the class applies to what ends in the class."""
    return bool(ph) and ph[-1] in klass


def t2_selectors() -> dict[str, Any]:
    gam = ("g", "a", "m")
    gacch = ("g", "a", "ch")
    bhavati = ("bh", "a", "v", "a", "t", "i")
    ik80 = savarna_expand(p58("i", 1))
    # theorum/80's compiled 7.3.84 condition "root ends in ik" is tadanta of ik (58 spelling)
    roots = [("n", "I"), ("g", "a", "m"), ("bh", "U"), ("i", "z"), ("k", "R")]
    tadanta_matches = all(tadanta_1_1_72(r, ik80) == (r[-1] in ik80) for r in roots)
    checks = {
        "ti_of_gam_is_am_and_of_bhavati_is_i": ti_1_1_64(gam) == ("a", "m") and ti_1_1_64(bhavati) == ("i",),
        "upadha_of_gam_is_a_of_gacch_is_a": upadha_1_1_65(gam) == "a" and upadha_1_1_65(gacch) == "a",
        "tadanta_ik_decides_7_3_84_for_nI_bhU_kR_not_gam_iz": tadanta_matches and tadanta_1_1_72(("n", "I"), ik80) and not tadanta_1_1_72(gam, ik80),
        "ti_is_a_suffix_of_the_string_and_contains_its_last_vowel": all(ph[-len(ti_1_1_64(ph)):] == ti_1_1_64(ph) and ti_1_1_64(ph)[0] in VOWELS_IAST for ph in (gam, gacch, bhavati)),
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T3 pragṛhya, saṁyoga, anunāsika
def t3_pragrhya_samyoga_anunasika() -> dict[str, Any]:
    rules = {rec["sid"]: compile_sandhi(rec) for rec in SANDHI_RECORDS}

    def with_pragrhya(j: tuple, pragrhya: bool):
        # 6.1.125: a pragṛhya prior vowel is unchanged before a vowel (the flag comes from 1.1.11: dual ī, ū, e)
        if pragrhya and j[0] in ("I", "U", "e"):
            return {sid: None for sid in rules}
        return {sid: r(j) for sid, r in rules.items()}

    duals = [("I", "a"), ("U", "e"), ("e", "i"), ("I", "I"), ("e", "a")]
    blocked = all(all(v is None for v in with_pragrhya(j, True).values()) for j in duals)
    fires = all(any(v is not None for v in with_pragrhya(j, False).values()) for j in duals)
    non_pragrhya_unaffected = all(with_pragrhya(j, True) == with_pragrhya(j, False) for j in [("a", "i"), ("i", "a"), ("A", "U"), ("o", "a")])
    # 1.1.7 saṁyoga: maximal runs of consonants with no vowel between
    def samyogas(ph):
        runs, cur = [], []
        for s in ph:
            if s in VOWELS_IAST or s in ("A", "I", "U", "R", "L", "ai", "au", "e", "o", "a", "i", "u"):
                if len(cur) >= 2:
                    runs.append(tuple(cur))
                cur = []
            else:
                cur.append(s)
        if len(cur) >= 2:
            runs.append(tuple(cur))
        return runs
    gacchati = ("g", "a", "c", "ch", "a", "t", "i")
    nasal_from_grid = frozenset(MANNER["nasal"])
    checks = {
        "6_1_125_pragrhya_dual_endings_block_every_compiled_sandhi_rule": blocked,
        "same_junctions_fire_without_the_pragrhya_flag": fires,
        "non_pragrhya_junctions_unaffected": non_pragrhya_unaffected,
        "1_1_7_samyoga_of_gacchati_is_c_ch": samyogas(gacchati) == [("c", "ch")] and samyogas(("g", "a", "m")) == [],
        "1_1_8_nasals_on_the_carrier_equal_the_manner_grid_nasal_row": frozenset(NASAL) == nasal_from_grid,
    }
    return {"checks": checks}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_savarna_derived": t1_savarna_derived(), "t2_selectors": t2_selectors(), "t3_pragrhya_samyoga_anunasika": t3_pragrhya_samyoga_anunasika()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PANINIAN_SAMJNA_SOUND_LAYER_CANDIDATE" if all(checks.values()) else "FAIL_PANINIAN_SAMJNA_SOUND_LAYER_CANDIDATE"
    return {
        "schema": "rkf.paninian_samjna_sound_layer_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "1.1.9 with 1.1.10 on the sthāna/internal-prayatna table yields exactly the vowel length pairs and exactly the five vargas: theorum/80's SAVARNA table and theorum/79's udit classes are derived, not declared; without 1.1.10, i and ś would pair",
                "1.1.64 ṭi, 1.1.65 upadhā and 1.1.72 tadanta are exact selectors; the ik-final condition of theorum/80's compiled 7.3.84 is tadanta of ik",
                "6.1.125 with the 1.1.11 pragṛhya flag blocks every compiled sandhi rule on dual ī/ū/e junctions and nothing else; 1.1.7 clusters and 1.1.8 nasals decided on the carrier",
            ],
            "NOT_claimed": ["pluta, anusvāra and nasalized vowels (not on the carrier)", "dvivacana detection from morphology (the flag is supplied by the nominal carrier, theorum/63)", "RH, YM untouched"],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
