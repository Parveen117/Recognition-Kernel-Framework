from __future__ import annotations

"""Exact certificate (theorum/94): THE SARVANĀMA SUP PARADIGMS COMPILED — sarva
and tad (masculine) through the quoted sūtras; the sarvanāma saṁjñā (1.1.27)
load-bearing on exactly its five cells; 7.2.102 / 7.2.106 on tad.

Quoted sūtras:
 1.1.27   sarvādīni sarvanāmāni               sarva and the rest are sarvanāma
 7.1.17   jasaḥ śī                             after a sarvanāma a-stem, jas → śī
 7.1.14   sarvanāmnaḥ smai                     ṅe → smai
 7.1.15   ṅasiṅyoḥ smātsminau                  ṅasi → smāt, ṅi → smin
 7.1.52   āmi sarvanāmnaḥ suṭ                  ām takes suṭ after a sarvanāma a-stem
 7.3.103  bahuvacane jhaly et                  a → e before a jhal-initial plural sup (bhyas, su, sām)
 8.3.59   ādeśapratyayayoḥ (ṣatva)             sarveṣām, sarveṣu
 7.2.102  tyadādīnām aḥ                        tyad and the rest end in a before a vibhakti
 7.2.106  tadoḥ saḥ sāv anantyayoḥ             the non-final t / d of tad (etad) becomes s before su
 6.1.87   ād guṇaḥ ; 7.1.9 ; 7.1.12 ; 7.1.13 ; 7.3.102 ; 6.1.102 / 6.1.103 ; 6.1.107 ; 6.1.97 ; 6.1.78 ; 8.4.2 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  sarva: 22 forms (sarvaḥ sarvau sarve … sarvasmai … sarvasmāt … sarveṣām
     sarvasmin … sarveṣu, he sarva); the sarvanāma saṁjñā breaks exactly
     {1p, 4s, 5s, 6p, 7s}; 7.1.17 {1p}, 7.1.14 {4s}, 7.1.15 {5s, 7s},
     7.1.52 {6p}, 7.3.103 {4p, 5p, 6p, 7p}, 8.4.2 {3s}.
 T2  tad: 21 forms (saḥ tau te … tasmin tayoḥ teṣu); 7.2.102 breaks every
     cell, 7.2.106 exactly {1s}; the sambuddhi is refused (no vocative of
     tad: 7.2.102's aḥ needs a vibhakti and the tradition lists none).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.ghi_stem_sup_compiled import natva_8_4_2
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "1.1.27": "sarvādīni sarvanāmāni", "7.1.17": "jasaḥ śī", "7.1.14": "sarvanāmnaḥ smai", "7.1.15": "ṅasiṅyoḥ smātsminau", "7.1.52": "āmi sarvanāmnaḥ suṭ",
    "7.3.103": "bahuvacane jhaly et", "8.3.59": "ādeśapratyayayoḥ", "7.2.102": "tyadādīnām aḥ", "7.2.106": "tadoḥ saḥ sāv anantyayoḥ", "6.1.87": "ād guṇaḥ",
    "7.1.9": "ato bhisa ais", "7.1.12": "ṭāṅasiṅasām inātsyāḥ", "7.1.13": "ṅer yaḥ", "7.3.102": "supi ca", "6.1.102": "prathamayoḥ pūrvasavarṇaḥ",
    "6.1.103": "tasmāc chaso naḥ puṁsi", "6.1.107": "ami pūrvaḥ", "6.1.97": "ato guṇe", "6.1.78": "eco 'yavāyāvaḥ", "8.4.2": "aṭkupvāṅnumvyavāye 'pi",
    "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
SARVA = {"1s": "sarvaḥ", "1d": "sarvau", "1p": "sarve", "2s": "sarvam", "2d": "sarvau", "2p": "sarvān", "3s": "sarveṇa", "3d": "sarvābhyām", "3p": "sarvaiḥ",
         "4s": "sarvasmai", "4d": "sarvābhyām", "4p": "sarvebhyaḥ", "5s": "sarvasmāt", "5d": "sarvābhyām", "5p": "sarvebhyaḥ", "6s": "sarvasya", "6d": "sarvayoḥ",
         "6p": "sarveṣām", "7s": "sarvasmin", "7d": "sarvayoḥ", "7p": "sarveṣu", "8s": "sarva"}
TAD = {"1s": "saḥ", "1d": "tau", "1p": "te", "2s": "tam", "2d": "tau", "2p": "tān", "3s": "tena", "3d": "tābhyām", "3p": "taiḥ", "4s": "tasmai", "4d": "tābhyām",
       "4p": "tebhyaḥ", "5s": "tasmāt", "5d": "tābhyām", "5p": "tebhyaḥ", "6s": "tasya", "6d": "tayoḥ", "6p": "teṣām", "7s": "tasmin", "7d": "tayoḥ", "7p": "teṣu"}
ALL_STAGES = ("sarvanāma", "7.1.17", "7.1.14", "7.1.15", "7.1.52", "7.3.103", "7.2.102", "7.2.106", "7.1.9", "7.1.12", "7.3.102", "6.1.102", "8.4.2", "8.3.59", "8.2.66", "8.3.15")


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES, tyadadi: bool = False) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    st = list(stem)
    path = [f"{upadesa} → {''.join(aff)}"]
    samb = code == "8s"
    sn = "sarvanāma" in on
    if tyadadi and samb:
        raise ValueError("no sambuddhi of tad")
    # 7.2.102 tyadādīnām aḥ: final sound → a before a vibhakti
    if tyadadi and "7.2.102" in on and st[-1] not in VOWELS:
        st[-1] = "a"; path.append("final → a before a vibhakti (7.2.102 tyadādīnām aḥ; 1.1.52)")
        if len(st) >= 2 and st[-2] == "a":
            st = st[:-1]; path.append("a + a → a within the stem (6.1.97 ato guṇe, pararūpa)")
    # 7.2.106 tadoḥ saḥ sāv anantyayoḥ
    if tyadadi and "7.2.106" in on and code == "1s" and st[0] == "t":
        st[0] = "s"; path.append("non-final t → s before su (7.2.106)")
    if st[-1] != "a":
        return "".join(st + aff), path
    # sarvanāma substitutes
    if sn and "7.1.17" in on and code == "1p":
        aff = list(its("śī", "pratyaya")["remaining_sounds"]); path.append("jas → śī (7.1.17)")
    if sn and "7.1.14" in on and code == "4s":
        aff = ["s", "m", "ai"]; path.append("ṅe → smai (7.1.14)")
    elif code == "4s":
        aff = ["y", "a"]; path.append("ṅe → ya (7.1.13)")
    if sn and "7.1.15" in on and code == "5s":
        aff = ["s", "m", "ā", "t"]; path.append("ṅasi → smāt (7.1.15)")
    elif "7.1.12" in on and code == "5s":
        aff = ["ā", "t"]; path.append("ṅasi → āt (7.1.12)")
    if sn and "7.1.15" in on and code == "7s":
        aff = ["s", "m", "i", "n"]; path.append("ṅi → smin (7.1.15)")
    if sn and "7.1.52" in on and code == "6p":
        aff = ["s"] + aff; path.append("suṭ before ām (7.1.52)")
    # a-stem machinery
    if "7.1.9" in on and code == "3p":
        aff = ["ai", "s"]; path.append("bhis → ais (7.1.9)")
    if "7.1.12" in on and code == "3s":
        aff = ["i", "n", "a"]; path.append("ṭā → ina (7.1.12)")
    if "7.1.12" in on and code == "6s":
        aff = ["s", "y", "a"]; path.append("ṅas → sya (7.1.12)")
    if "7.3.102" in on and code in ("3d", "4d", "5d") or ("7.3.102" in on and code == "4s" and aff[:2] == ["y", "a"]):
        st[-1] = "ā"; path.append("a → ā before a yañ-initial sup (7.3.102)")
    if "7.3.103" in on and code in ("4p", "5p", "7p", "6p") and aff and aff[0] in ("bh", "s"):
        st[-1] = "e"; path.append("a → e before a jhal-initial plural sup (7.3.103)")
    if samb and aff == ["s"]:
        aff = []; path.append("sambuddhi su dropped after a (6.1.69)")
    # seam sandhi
    if aff and aff[0] in VOWELS and st[-1] in VOWELS:
        a, b = st[-1], aff[0]
        if a == "a" and b == "ī":
            st[-1] = "e"; aff = aff[1:]; path.append("a + ī → e (6.1.87)")
        elif a == "a" and b == "a":
            aff = aff[1:]; path.append("a + a → a (6.1.107 / 6.1.101)")
        elif a == "a" and b == "au":
            st[-1] = "au"; aff = aff[1:]; path.append("a + au → au (6.1.88)")
        elif a == "a" and b == "ai":
            st[-1] = "ai"; aff = aff[1:]; path.append("a + ai → ai (6.1.88)")
        elif a == "a" and b == "i":
            st[-1] = "e"; aff = aff[1:]; path.append("a + i → e (6.1.87)")
        elif a == "a" and b == "o":
            st[-1] = "a"; st.append("y"); path.append("a + o → ayo (6.1.87 then 6.1.78)")
        elif a == "e" and b in VOWELS:
            st[-1] = "a"; st.append("y"); path.append("e + vowel → ay (6.1.78)")
    if "6.1.102" in on and code == "2p" and st[-1] == "a" and aff == ["s"]:
        st[-1] = "ā"; aff = ["n"]; path.append("a + as → ān (6.1.102, 6.1.103)")
    word = st + aff
    if "8.3.59" in on and code in ("6p", "7p") and st[-1] == "e" and aff and aff[0] == "s":
        word = st + ["ṣ"] + aff[1:]; path.append("s → ṣ after e (8.3.59)")
    if "8.4.2" in on:
        word, fired = natva_8_4_2(word)
        if fired:
            path.append("n → ṇ (8.4.1 / 8.4.2)")
    if word and word[-1] == "s" and "8.2.66" in on:
        word[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word), path


def paradigm(stem, stages=ALL_STAGES, tyadadi=False) -> dict[str, str]:
    return {c: decline(stem, c, up, stages, tyadadi)[0] for c, up in SUP if not (tyadadi and c == "8s")}


def _ablation(stem, oracle, expected, tyadadi=False):
    broken = {}
    for s in expected:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s), tyadadi)
        broken[s] = sorted(c for c in oracle if f[c] != oracle[c])
    return broken, {f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v)) if v else 'nothing'}_break": set(broken[s]) == v for s, v in expected.items()}


def t1_sarva() -> dict[str, Any]:
    stem = ("s", "a", "r", "v", "a")
    forms = paradigm(stem)
    exp = {"sarvanāma": {"1p", "4s", "5s", "6p", "7s"}, "7.1.17": {"1p"}, "7.1.14": {"4s"}, "7.1.15": {"5s", "7s"}, "7.1.52": {"6p"}, "7.3.103": {"4p", "5p", "6p", "7p"},
           "8.4.2": {"3s"}, "8.3.59": {"6p", "7p"}, "7.1.9": {"3p"}, "7.3.102": {"3d", "4d", "5d"}, "6.1.102": {"2p"}}
    broken, checks = _ablation(stem, SARVA, exp)
    return {"checks": {"sarva_22_forms_equal_the_classical_paradigm": forms == SARVA, **checks}, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken}


def t2_tad() -> dict[str, Any]:
    stem = ("t", "a", "d")
    forms = paradigm(stem, tyadadi=True)
    exp = {"7.2.102": set(TAD), "7.2.106": {"1s"}, "sarvanāma": {"1p", "4s", "5s", "6p", "7s"}}
    broken, checks = _ablation(stem, TAD, exp, tyadadi=True)
    refused = False
    try:
        decline(stem, "8s", "su~", tyadadi=True)
    except ValueError:
        refused = True
    return {"checks": {"tad_21_forms_equal_the_classical_paradigm": forms == TAD, "sambuddhi_of_tad_refused": refused, **checks}, "forms": forms, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_sarva": t1_sarva(), "t2_tad": t2_tad()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SARVANAMA_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_SARVANAMA_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.sarvanama_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "sarva: 22 forms through 1.1.27, 7.1.17, 7.1.14, 7.1.15, 7.1.52, 7.3.103, 8.3.59 and theorum/63's a-stem sūtras; the sarvanāma saṁjñā breaks exactly {1p, 4s, 5s, 6p, 7s}, each other stage its own cells",
                "tad: 21 forms through 7.2.102 (every cell) and 7.2.106 ({1s}); the sambuddhi is refused",
            ],
            "NOT_claimed": [
                "feminine / neuter sarvanāma (sā, tat beyond theorum/65), etad / yad / idam / asmad, the sarvanāma option cells (pūrva etc. 1.1.34), pronominal ā-stems (sarvasyāḥ)",
                "the stage order is a declared pipeline; sarva declared a sarvanāma from the gaṇa, not read from it",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    payload = build_certificate()
    data = canonical_bytes(payload)
    if args.output is not None:
        args.output.write_bytes(data)
    print(payload["status"])
    for name, v in payload.items():
        if isinstance(v, dict) and "checks" in v:
            for k, val in v["checks"].items():
                print(f"    {name}.{k}: {val}")
    print("sha256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
