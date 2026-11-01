from __future__ import annotations

"""Exact certificate (theorum/98): THE FEMININE SARVANĀMA (ĀP) SUP PARADIGMS
COMPILED — sarvā and sā on theorum/88's āp engine with 7.3.114 (syāṭ and the
shortening) and 7.1.52 (suṭ); 7.1.17 / 7.1.15 shown NOT to reach the feminine
(their 'ataḥ' anuvṛtti), 7.2.102 / 7.2.106 on sā.

Quoted sūtras:
 1.1.27   sarvādīni sarvanāmāni ; 4.1.4 ajādyataṣ ṭāp ; 7.2.102 tyadādīnām aḥ ; 7.2.106 tadoḥ saḥ sāv anantyayoḥ
 7.3.114  sarvanāmnaḥ syāḍ ḍhrasvaś ca        a ṅit sup after a sarvanāma āp takes syāṭ, and the āp is shortened
 7.3.113  yāḍ āpaḥ                             (the general āp rule, superseded here)
 7.1.52   āmi sarvanāmnaḥ suṭ                  sarvāsām, tāsām
 7.1.17   jasaḥ śī ; 7.1.15 ṅasiṅyoḥ smātsminau   under 'ataḥ' (7.1.9): a-stems only — sarvāḥ, sarvasyām
 7.1.18   auṅ āpaḥ ; 7.3.116 ṅer ām ; 7.3.105 āṅi cāpaḥ ; 7.3.106 sambuddhau ca ; 6.1.68 ; 6.1.69 ; 6.1.87 ; 6.1.88 ; 6.1.101 ; 6.1.107 ; 6.1.78 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  sarvā: 22 forms (sarvā sarve sarvāḥ … sarvasyai … sarvasyāḥ … sarvāsām
     sarvasyām … sarvāsu, he sarve); 7.3.114 breaks exactly {4s, 5s, 6s, 7s},
     7.1.52 {6p}; applying 7.1.17 / 7.1.15 to the feminine would give
     *sarve (1p) / *sarvasmin (7s): both are shown wrong against the oracle.
 T2  sā: 22 forms (sā te tāḥ … tasyai … tāsām … tāsu, he se? — refused: no
     vocative); 7.2.102 every cell, 7.2.106 exactly {1s}.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "1.1.27": "sarvādīni sarvanāmāni", "4.1.4": "ajādyataṣ ṭāp", "7.2.102": "tyadādīnām aḥ", "7.2.106": "tadoḥ saḥ sāv anantyayoḥ", "7.3.114": "sarvanāmnaḥ syāḍ ḍhrasvaś ca",
    "7.3.113": "yāḍ āpaḥ", "7.1.52": "āmi sarvanāmnaḥ suṭ", "7.1.17": "jasaḥ śī", "7.1.15": "ṅasiṅyoḥ smātsminau", "7.1.9": "ato bhisa ais", "7.1.18": "auṅ āpaḥ",
    "7.3.116": "ṅer ām nadyāmnībhyaḥ", "7.3.105": "āṅi cāpaḥ", "7.3.106": "sambuddhau ca", "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "6.1.69": "eṅhrasvāt sambuddheḥ",
    "6.1.87": "ād guṇaḥ", "6.1.88": "vṛddhir eci", "6.1.101": "akaḥ savarṇe dīrghaḥ", "6.1.107": "ami pūrvaḥ", "6.1.78": "eco 'yavāyāvaḥ", "6.1.97": "ato guṇe",
    "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
SARVA_F = {"1s": "sarvā", "1d": "sarve", "1p": "sarvāḥ", "2s": "sarvām", "2d": "sarve", "2p": "sarvāḥ", "3s": "sarvayā", "3d": "sarvābhyām", "3p": "sarvābhiḥ",
           "4s": "sarvasyai", "4d": "sarvābhyām", "4p": "sarvābhyaḥ", "5s": "sarvasyāḥ", "5d": "sarvābhyām", "5p": "sarvābhyaḥ", "6s": "sarvasyāḥ", "6d": "sarvayoḥ",
           "6p": "sarvāsām", "7s": "sarvasyām", "7d": "sarvayoḥ", "7p": "sarvāsu", "8s": "sarve"}
SA = {"1s": "sā", "1d": "te", "1p": "tāḥ", "2s": "tām", "2d": "te", "2p": "tāḥ", "3s": "tayā", "3d": "tābhyām", "3p": "tābhiḥ", "4s": "tasyai", "4d": "tābhyām",
      "4p": "tābhyaḥ", "5s": "tasyāḥ", "5d": "tābhyām", "5p": "tābhyaḥ", "6s": "tasyāḥ", "6d": "tayoḥ", "6p": "tāsām", "7s": "tasyām", "7d": "tayoḥ", "7p": "tāsu"}
ALL_STAGES = ("sarvanāma", "7.2.102", "7.2.106", "7.1.18", "7.3.116", "7.3.114", "7.3.113", "7.1.52", "7.3.105", "7.3.106", "6.1.68", "6.1.69", "sandhi", "8.2.66", "8.3.15")


def decline(a_stem: tuple[str, ...], code: str, up: str, stages=ALL_STAGES, tyadadi: bool = False, wrong_masculine_rules: bool = False) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(up, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    ngit = "ṅ" in r["its"]
    st = list(a_stem)
    path = []
    samb = code == "8s"
    if tyadadi and samb:
        raise ValueError("no sambuddhi of tad")
    if tyadadi and "7.2.102" in on and st[-1] not in VOWELS:
        st[-1] = "a"; path.append("final → a before a vibhakti (7.2.102)")
        if len(st) >= 2 and st[-2] == "a":
            st = st[:-1]; path.append("a + a → a (6.1.97)")
    if tyadadi and "7.2.106" in on and code == "1s" and st[0] == "t":
        st[0] = "s"; path.append("t → s before su (7.2.106)")
    # ṭāp
    if st[-1] == "a":
        st[-1] = "ā"; path.append("ṭāp (4.1.4): a + ā → ā (6.1.101)")
    sn = "sarvanāma" in on
    if wrong_masculine_rules and code == "1p":
        aff = ["ī"]; path.append("(control) jas → śī applied to the feminine (7.1.17 misread)")
    if wrong_masculine_rules and code == "7s":
        aff = ["s", "m", "i", "n"]; path.append("(control) ṅi → smin applied to the feminine (7.1.15 misread)")
        ngit = False
    if "7.1.18" in on and up == "auṭ":
        aff = ["ī"]; path.append("auṭ → śī (7.1.18)")
    if "7.3.116" in on and code == "7s" and not wrong_masculine_rules:
        aff = ["ā", "m"]; path.append("ṅi → ām (7.3.116; ṅit retained 1.1.56)")
    if ngit:
        if sn and "7.3.114" in on:
            aff = ["s", "y", "ā"] + aff; st[-1] = "a"; path.append("syāṭ prefixed and the āp shortened (7.3.114 sarvanāmnaḥ syāḍ ḍhrasvaś ca)")
        elif "7.3.113" in on:
            aff = ["y", "ā"] + aff; path.append("yāṭ prefixed (7.3.113)")
    if code == "6p":
        if sn and "7.1.52" in on:
            aff = ["s"] + aff; path.append("suṭ before ām (7.1.52)")
        else:
            aff = ["n"] + aff; path.append("nuṭ (7.1.54)")
    if "7.3.105" in on and code in ("3s", "6d", "7d") and st[-1] == "ā":
        st[-1] = "e"; path.append("ā → e before ṭā / os (7.3.105)")
    if "7.3.106" in on and samb:
        st[-1] = "e"; path.append("ā → e in the sambuddhi (7.3.106)")
    if code == "1s" and "6.1.68" in on and st[-1] == "ā" and aff == ["s"]:
        aff = []; path.append("su dropped after āp (6.1.68)")
    if samb and "6.1.69" in on and st[-1] == "e" and aff == ["s"]:
        aff = []; path.append("sambuddhi su dropped (6.1.69)")
    # inside syā / yā + vowel
    for i in range(len(aff) - 1):
        if aff[i] == "ā" and aff[i + 1] in ("a", "ā"):
            aff = aff[:i + 1] + aff[i + 2:]; path.append("ā + a → ā (6.1.101)"); break
        if aff[i] == "ā" and aff[i + 1] == "e":
            aff = aff[:i] + ["ai"] + aff[i + 2:]; path.append("ā + e → ai (6.1.88)"); break
    if "sandhi" in on and aff and aff[0] in VOWELS:
        a, b = st[-1], aff[0]
        if a == "ā" and b == "ī":
            st[-1] = "e"; aff = aff[1:]; path.append("ā + ī → e (6.1.87)")
        elif a == "e":
            st[-1] = "a"; st.append("y"); path.append("e + vowel → ay (6.1.78)")
        elif a == "ā" and b in ("a", "ā"):
            aff = aff[1:]; path.append("ā + a → ā (6.1.101 / 6.1.107)")
        elif a == "ā" and b == "e":
            st[-1] = "ai"; aff = aff[1:]; path.append("ā + e → ai (6.1.88)")
    w = st + aff
    if w and w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(stem, stages=ALL_STAGES, tyadadi=False, wrong=False) -> dict[str, str]:
    return {c: decline(stem, c, up, stages, tyadadi, wrong)[0] for c, up in SUP if not (tyadadi and c == "8s")}


def t1_sarva_f() -> dict[str, Any]:
    stem = ("s", "a", "r", "v", "a")
    forms = paradigm(stem)
    exp = {"sarvanāma": {"4s", "5s", "6s", "7s", "6p"}, "7.3.114": {"4s", "5s", "6s", "7s"}, "7.1.52": {"6p"}, "7.1.18": {"1d", "2d"}, "7.3.116": {"7s"}, "7.3.105": {"3s", "6d", "7d"},
           "7.3.106": {"8s"}, "6.1.68": {"1s"}, "6.1.69": {"8s"}, "7.3.113": set()}
    broken = {}
    for s in exp:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in SARVA_F if f[c] != SARVA_F[c])
    wrong = paradigm(stem, wrong=True)
    checks = {"sarva_feminine_22_forms_equal_the_classical_paradigm": forms == SARVA_F,
              "masculine_7_1_17_and_7_1_15_would_give_wrong_feminines": wrong["1p"] == "sarve" and wrong["7s"].endswith("smin") and wrong["1p"] != SARVA_F["1p"] and wrong["7s"] != SARVA_F["7s"]}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v)) if v else 'nothing'}_break": set(broken[s]) == v for s, v in exp.items()})
    return {"checks": checks, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken, "control_misreadings": {"1p": wrong["1p"], "7s": wrong["7s"]}}


def t2_sa() -> dict[str, Any]:
    stem = ("t", "a", "d")
    forms = paradigm(stem, tyadadi=True)
    exp = {"7.2.102": set(SA), "7.2.106": {"1s"}, "7.3.114": {"4s", "5s", "6s", "7s"}, "7.1.52": {"6p"}}
    broken = {}
    for s in exp:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s), tyadadi=True)
        broken[s] = sorted(c for c in SA if f[c] != SA[c])
    checks = {"sa_21_forms_equal_the_classical_paradigm": forms == SA}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in exp.items()})
    return {"checks": checks, "forms": forms, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_sarva_f": t1_sarva_f(), "t2_sa": t2_sa()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SARVANAMA_AP_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_SARVANAMA_AP_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.sarvanama_ap_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "sarvā: 22 forms through 4.1.4, 7.3.114 (syāṭ + shortening), 7.1.52, and the āp sūtras of theorum/88; sarvanāma breaks exactly {4s, 5s, 6s, 7s, 6p}; 7.3.113 is superseded (removing it changes nothing)",
                "the masculine 7.1.17 / 7.1.15 do not reach the feminine: applying them gives *sarve, *sarvasmin against the oracle",
                "sā: 21 forms; 7.2.102 every cell, 7.2.106 exactly {1s}; sambuddhi refused",
            ],
            "NOT_claimed": ["neuter pronouns, idam / etad / yad feminines, the option cells of 1.1.34, 7.3.115 (dvitīyā-ṭāp forms)", "stage order a declared pipeline", "RH, YM untouched"],
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
