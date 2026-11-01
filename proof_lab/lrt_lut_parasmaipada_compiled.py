from __future__ import annotations

"""Exact certificate (theorum/97): LṚṬ AND LUṬ (THE TWO FUTURES) PARASMAIPADA
COMPILED — bhū, gam, nī with sya / tās (3.1.33), the iṭ of 7.2.35 / 7.2.58,
guṇa before the ārdhadhātuka, and luṭ's ḍā / rau / ras (2.4.85) with 6.4.143,
7.4.50 and 7.4.51.

Quoted sūtras:
 3.3.13   lṛṭ śeṣe ca                          3.3.15  anadyatane luṭ
 3.1.33   syatāsī lṛluṭoḥ                      sya before lṛ (lṛṭ, lṛṅ), tās before luṭ
 3.4.114  ārdhadhātukaṁ śeṣaḥ                  sya, tās are ārdhadhātuka
 7.2.35   ārdhadhātukasyeḍ valādeḥ             a val-initial ārdhadhātuka takes iṭ (seṭ roots)
 7.2.58   gamer iṭ parasmaipadeṣu              gam takes iṭ before an s-initial ārdhadhātuka in parasmaipada (lṛṭ, not luṭ)
 7.2.10   ekāca upadeśe 'nudāttāt              no iṭ for nī (aniṭ, declared)
 7.3.84   sārvadhātukārdhadhātukayoḥ (guṇa)    bhū → bho, nī → ne ; 6.1.78 eco 'yavāyāvaḥ (bhav-i-)
 8.3.59   ādeśapratyayayoḥ (ṣatva)             iṣya, neṣya
 2.4.85   luṭaḥ prathamasya ḍārauras           tip, tas, jhi of luṭ → ḍā, rau, ras
 6.4.143  ṭeḥ                                  the ṭi of the aṅga drops before a ḍit (1.1.64 aco 'ntyādi ṭi)
 7.4.50   tāsastyor lopaḥ                      the s of tās drops before an s-initial ending (bhavitāsi)
 7.4.51   ri ca                                 and before r (bhavitārau, bhavitāraḥ)
 8.2.66   sasajuṣo ruḥ
 7.1.3 ; 7.3.101 ; 8.3.15 ; 1.3.2–1.3.9

 T1  lṛṭ: bhaviṣyati … bhaviṣyāmaḥ, gamiṣyati … (iṭ by 7.2.58), neṣyati …
     (no iṭ): 27 forms; each stage breaks exactly its cells; removing 7.2.58
     breaks all nine of gam and nothing of bhū / nī.
 T2  luṭ: bhavitā bhavitārau bhavitāraḥ / bhavitāsi bhavitāsthaḥ bhavitāstha /
     bhavitāsmi bhavitāsvaḥ bhavitāsmaḥ and netā …: 18 forms; 2.4.85 {3s, 3d,
     3p}, 6.4.143 {3s}, 7.4.50 {2s}, 7.4.51 {3d, 3p}; gam's luṭ (gantā: 8.3.24 / 8.4.58)
     refused by name.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import BASE, GUNA_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.3.13": "lṛṭ śeṣe ca", "3.3.15": "anadyatane luṭ", "3.1.33": "syatāsī lṛluṭoḥ", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "7.2.35": "ārdhadhātukasyeḍ valādeḥ",
    "7.2.58": "gamer iṭ parasmaipadeṣu", "7.2.10": "ekāca upadeśe 'nudāttāt", "7.3.84": "sārvadhātukārdhadhātukayoḥ", "6.1.78": "eco 'yavāyāvaḥ", "8.3.59": "ādeśapratyayayoḥ",
    "2.4.85": "luṭaḥ prathamasya ḍārauras", "6.4.143": "ṭeḥ", "1.1.64": "aco 'ntyādi ṭi", "7.4.50": "tāsastyor lopaḥ", "7.4.51": "ri ca", "8.2.66": "sasajuṣo ruḥ",
    "7.1.3": "jho 'ntaḥ", "7.3.101": "ato dīrgho yañi", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
TING_P = [("3s", "tip"), ("3d", "tas"), ("3p", "jhi"), ("2s", "sip"), ("2d", "thas"), ("2p", "tha"), ("1s", "mip"), ("1d", "vas"), ("1p", "mas")]
ROOTS = {"bhū": ("bhū", "dhatu"), "gam": ("gamḷ~", "dhatu"), "nī": ("ṇīñ", "dhatu")}
SET = {"bhū"}            # 7.2.35: seṭ roots (declared from the Dhātupāṭha accent); gam by 7.2.58 before s-initial; nī aniṭ (7.2.10)
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
AYADI = {"e": ("a", "y"), "o": ("a", "v")}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
LRT = {"bhū": {"3s": "bhaviṣyati", "3d": "bhaviṣyataḥ", "3p": "bhaviṣyanti", "2s": "bhaviṣyasi", "2d": "bhaviṣyathaḥ", "2p": "bhaviṣyatha", "1s": "bhaviṣyāmi", "1d": "bhaviṣyāvaḥ", "1p": "bhaviṣyāmaḥ"},
       "gam": {"3s": "gamiṣyati", "3d": "gamiṣyataḥ", "3p": "gamiṣyanti", "2s": "gamiṣyasi", "2d": "gamiṣyathaḥ", "2p": "gamiṣyatha", "1s": "gamiṣyāmi", "1d": "gamiṣyāvaḥ", "1p": "gamiṣyāmaḥ"},
       "nī": {"3s": "neṣyati", "3d": "neṣyataḥ", "3p": "neṣyanti", "2s": "neṣyasi", "2d": "neṣyathaḥ", "2p": "neṣyatha", "1s": "neṣyāmi", "1d": "neṣyāvaḥ", "1p": "neṣyāmaḥ"}}
LUT = {"bhū": {"3s": "bhavitā", "3d": "bhavitārau", "3p": "bhavitāraḥ", "2s": "bhavitāsi", "2d": "bhavitāsthaḥ", "2p": "bhavitāstha", "1s": "bhavitāsmi", "1d": "bhavitāsvaḥ", "1p": "bhavitāsmaḥ"},
       "nī": {"3s": "netā", "3d": "netārau", "3p": "netāraḥ", "2s": "netāsi", "2d": "netāsthaḥ", "2p": "netāstha", "1s": "netāsmi", "1d": "netāsvaḥ", "1p": "netāsmaḥ"}}
LRT_STAGES = ("3.1.33", "7.2.35", "7.2.58", "7.3.84", "6.1.78", "8.3.59", "7.1.3", "7.3.101", "8.2.66", "8.3.15")
LUT_STAGES = ("3.1.33", "7.2.35", "7.3.84", "6.1.78", "2.4.85", "6.4.143", "7.4.50", "7.4.51", "8.2.66", "8.3.15")


def root_sounds(name: str) -> list[str]:
    up, kind = ROOTS[name]
    r = list(its(up, kind)["remaining_sounds"])
    if r[0] == "ṇ":
        r[0] = "n"                                   # 6.1.65 ṇo naḥ (theorum/86 cites it; hand-applied here)
    return r


def guna_ardhadhatuka(st: list[str], path: list[str], on: set) -> list[str]:
    if "7.3.84" in on and st[-1] in IK:
        g = rapara_1_1_51(BASE[IK[st[-1]]], antaratama(IK[st[-1]], GUNA_SET))
        st = st[:-1] + list(g); path.append(f"guṇa of the ik-final aṅga before the ārdhadhātuka (7.3.84; 1.1.50) → {''.join(st)}")
    return st


def lrt(name: str, code: str, up: str, stages=LRT_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = root_sounds(name)
    path = [f"{ROOTS[name][0]} → {''.join(st)}"]
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    vik = ["s", "y", "a"] if "3.1.33" in on else []
    if vik:
        path.append("sya before lṛṭ (3.1.33; ārdhadhātuka 3.4.114)")
    it = []
    if vik and (("7.2.35" in on and name in SET) or ("7.2.58" in on and name == "gam")):
        it = list(its("iṭ", "agama")["remaining_sounds"]); path.append("iṭ before the val-initial ārdhadhātuka (" + ("7.2.35" if name in SET else "7.2.58 gamer iṭ parasmaipadeṣu") + ")")
    st = guna_ardhadhatuka(st, path, on) if (vik or it) else st
    if "6.1.78" in on and it and st[-1] in AYADI:
        st = st[:-1] + list(AYADI[st[-1]]); path.append("ayādi before the iṭ (6.1.78)")
    stem = st + it + vik
    if "8.3.59" in on and vik and len(stem) >= 4 and stem[-4] in ("i", "e", "u", "o", "ī", "ū", "ṛ") and stem[-3] == "s":
        stem[-3] = "ṣ"; path.append("s → ṣ after iṇ (8.3.59)")
    # laṭ endings on the a-final stem
    if "7.1.3" in on and up == "jhi":
        aff = ["a", "n", "t"] + aff[1:]; path.append("jh → ant (7.1.3)")
    if "7.3.101" in on and up in ("mip", "vas", "mas") and stem[-1] == "a":
        stem[-1] = "ā"; path.append("a → ā before m / v (7.3.101)")
    if stem[-1] == "a" and aff and aff[0] == "a":
        aff = aff[1:]; path.append("a + a → a (6.1.97)")
    w = stem + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def lut(name: str, code: str, up: str, stages=LUT_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    if name == "gam":
        raise ValueError("gam's luṭ (gantā) needs 8.3.24 / 8.4.58 — refused")
    st = root_sounds(name)
    path = [f"{ROOTS[name][0]} → {''.join(st)}"]
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    vik = ["t", "ā", "s"] if "3.1.33" in on else []
    if vik:
        path.append("tās before luṭ (3.1.33; ārdhadhātuka 3.4.114)")
    it = []
    if vik and "7.2.35" in on and name in SET:
        it = list(its("iṭ", "agama")["remaining_sounds"]); path.append("iṭ (7.2.35)")
    st = guna_ardhadhatuka(st, path, on) if vik else st
    if "6.1.78" in on and it and st[-1] in AYADI:
        st = st[:-1] + list(AYADI[st[-1]]); path.append("ayādi before the iṭ (6.1.78)")
    stem = st + it + vik
    if "2.4.85" in on and up in ("tip", "tas", "jhi"):
        aff = {"tip": ["ḍ", "ā"], "tas": ["r", "au"], "jhi": ["r", "a", "s"]}[up]; path.append(f"{up} → {''.join(aff)} (2.4.85 luṭaḥ prathamasya ḍārauras)")
        if up == "tip":
            if "6.4.143" in on:
                k = max(i for i, s in enumerate(stem) if s in VOWELS)
                stem = stem[:k]; path.append("ṭi of the aṅga dropped before the ḍit (6.4.143 ṭeḥ; 1.1.64)")
            aff = aff[1:]                                            # ḍ is an it (1.3.7)
            path.append("ḍ it (1.3.7, 1.3.9)")
        elif "7.4.51" in on and stem[-1] == "s" and aff[0] == "r":
            stem = stem[:-1]; path.append("s of tās dropped before r (7.4.51 ri ca)")
    if "7.4.50" in on and stem[-1] == "s" and aff and aff[0] == "s":
        stem = stem[:-1]; path.append("s of tās dropped before s (7.4.50 tāsastyor lopaḥ)")
    w = stem + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(fn, name, stages) -> dict[str, str]:
    return {c: fn(name, c, up, stages)[0] for c, up in TING_P}


def _ablate(fn, name, oracle, stages, expected):
    broken = {}
    for s in expected:
        f = paradigm(fn, name, tuple(x for x in stages if x != s))
        broken[s] = sorted(c for c in oracle if f[c] != oracle[c])
    return broken, {f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v)) if v else 'nothing'}_break": set(broken[s]) == v for s, v in expected.items()}


def t1_lrt() -> dict[str, Any]:
    forms = {r: paradigm(lrt, r, LRT_STAGES) for r in ROOTS}
    exp = {"3.1.33": set(LRT["bhū"]), "7.2.35": set(LRT["bhū"]), "7.3.84": set(LRT["bhū"]), "6.1.78": set(LRT["bhū"]), "8.3.59": set(LRT["bhū"]), "7.1.3": {"3p"},
           "7.3.101": {"1s", "1d", "1p"}, "8.2.66": {"3d", "2d", "1d", "1p"}, "7.2.58": set()}
    broken, checks = _ablate(lrt, "bhū", LRT["bhū"], LRT_STAGES, exp)
    gam_wo = paradigm(lrt, "gam", tuple(x for x in LRT_STAGES if x != "7.2.58"))
    ni_wo = paradigm(lrt, "nī", tuple(x for x in LRT_STAGES if x != "7.2.35"))
    checks["without_7_2_58_all_nine_of_gam_break_and_none_of_ni_without_7_2_35"] = all(gam_wo[c] != LRT["gam"][c] for c in gam_wo) and ni_wo == LRT["nī"]
    return {"checks": {"lrt_27_forms_equal_the_classical_paradigms": forms == LRT, **checks}, "forms": forms, "paths_bhu": {c: lrt("bhū", c, up)[1] for c, up in TING_P}, "broken_cells": broken}


def t2_lut() -> dict[str, Any]:
    forms = {r: paradigm(lut, r, LUT_STAGES) for r in ("bhū", "nī")}
    exp = {"3.1.33": set(LUT["bhū"]), "7.2.35": set(LUT["bhū"]), "7.3.84": set(LUT["bhū"]), "2.4.85": {"3s", "3d", "3p"}, "6.4.143": {"3s"}, "7.4.50": {"2s"}, "7.4.51": {"3d", "3p"}, "8.2.66": {"3p", "2d", "1d", "1p"}}
    broken, checks = _ablate(lut, "bhū", LUT["bhū"], LUT_STAGES, exp)
    refused = False
    try:
        lut("gam", "3s", "tip")
    except ValueError:
        refused = True
    return {"checks": {"lut_18_forms_equal_the_classical_paradigms": forms == LUT, "gam_lut_refused_by_name": refused, **checks}, "forms": forms, "paths_bhu": {c: lut("bhū", c, up)[1] for c, up in TING_P}, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lrt": t1_lrt(), "t2_lut": t2_lut()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_LRT_LUT_PARASMAIPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_LRT_LUT_PARASMAIPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.lrt_lut_parasmaipada_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": {"lrt": list(LRT_STAGES), "lut": list(LUT_STAGES)},
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "lṛṭ parasmaipada of bhū (iṭ by 7.2.35), gam (iṭ by 7.2.58), nī (no iṭ): 27 forms by 3.1.33 sya, 7.3.84 guṇa (theorum/80's antaratama), 6.1.78, 8.3.59 and the laṭ endings; each stage breaks exactly its cells; 7.2.58 breaks all of gam and nothing else",
                "luṭ parasmaipada of bhū, nī: 18 forms by 3.1.33 tās, 7.2.35, 7.3.84, 2.4.85 ḍā / rau / ras, 6.4.143 with 1.1.64, 7.4.50, 7.4.51, 8.2.66; each stage breaks exactly its cells",
                "gam's luṭ refused by name (needs 8.3.24 / 8.4.58)",
            ],
            "NOT_claimed": ["seṭ / aniṭ status declared (7.2.10 by accent), lṛṅ, luṅ, liṭ, ātmanepada futures, other roots", "stage orders declared pipelines", "RH, YM untouched"],
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
