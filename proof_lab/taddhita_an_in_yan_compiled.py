from __future__ import annotations

"""Exact certificate (theorum/103): TADDHITA AFFIXES aṇ, iñ, yañ, ṭhak COMPILED —
the ñit / ṇit vṛddhi of the first vowel (7.2.117), the bha operations 6.4.146
(or guṇaḥ) and 6.4.148 (yasyeti ca), and 7.3.50 (ṭhasyekaḥ) on declared
prātipadikas; each rule shown load-bearing on exactly its derivations.

Quoted sūtras:
 4.1.76   taddhitāḥ (adhikāra) ; 4.1.82 samarthānāṁ prathamād vā
 4.1.83   prāg dīvyato 'ṇ                       aṇ is the default taddhita up to 4.4.2
 4.1.92   tasyāpatyam                           'his offspring': aupagava, kaurava, dāśarathi, dākṣi, gārgya
 4.1.95   ata iñ                                iñ after an a-final stem (dāśarathi, dākṣi)
 4.1.105  gargādibhyo yañ                        yañ after the gargādi (gārgya)
 4.3.120  tasyedam                              'belonging to him / it': śaiva, bauddha, paurāṇika (ṭhak taken as declared)
 7.2.117  taddhiteṣv acām ādeḥ                   vṛddhi of the first vowel before a ñit / ṇit taddhita ; 7.2.118 kiti ca (ṭhak)
 6.4.146  or guṇaḥ                               guṇa of a bha's final u before a taddhita (aupagava, kaurava)
 6.4.148  yasyeti ca                             a bha's final a / i drops before ī and before a taddhita (dāśarathi, śaiva, gārgya, paurāṇika)
 7.3.50   ṭhasyekaḥ                              the ṭha of a taddhita → ika (paurāṇika)
 6.4.129  bhasya ; 1.4.18 yaci bham ; 6.1.78 eco 'yavāyāvaḥ ; 1.2.46 kṛttaddhitasamāsāś ca ; 1.3.2–1.3.9

 T1  upagu + aṇ → aupagava ; kuru + aṇ → kaurava ; daśaratha + iñ → dāśarathi ;
     dakṣa + iñ → dākṣi ; garga + yañ → gārgya ; śiva + aṇ → śaiva ; buddha + aṇ →
     bauddha ; purāṇa + ṭhak → paurāṇika — 8 derivations; 7.2.117 breaks the seven ñit / ṇit, 7.2.118 paurāṇika,
     6.4.146 the two u-stems, 6.4.148 the six a / i-final bhas, 7.3.50 paurāṇika,
     6.1.78 the two u-stems.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import BASE, GUNA_SET, VRDDHI_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "4.1.76": "taddhitāḥ", "4.1.82": "samarthānāṁ prathamād vā", "4.1.83": "prāg dīvyato 'ṇ", "4.1.92": "tasyāpatyam", "4.1.95": "ata iñ", "4.1.105": "gargādibhyo yañ",
    "4.3.120": "tasyedam", "7.2.117": "taddhiteṣv acām ādeḥ", "7.2.118": "kiti ca", "6.4.146": "or guṇaḥ", "6.4.148": "yasyeti ca", "7.3.50": "ṭhasyekaḥ", "6.4.129": "bhasya", "1.4.18": "yaci bham",
    "6.1.78": "eco 'yavāyāvaḥ", "1.2.46": "kṛttaddhitasamāsāś ca",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
V58 = {"A": "ā", "ai": "ai", "au": "au", "e": "e", "o": "o"}
TO58 = {"a": "a", "i": "i", "u": "u", "ā": "A", "ī": "I", "ū": "U", "ṛ": "R"}
AYADI = {"e": ("a", "y"), "o": ("a", "v"), "ai": ("ā", "y"), "au": ("ā", "v")}
CASES = [  # (prātipadika, affix teaching form, sense sūtra, expected)
    (("u", "p", "a", "g", "u"), "aṇ", "4.1.92", "aupagava"), (("k", "u", "r", "u"), "aṇ", "4.1.92", "kaurava"),
    (("d", "a", "ś", "a", "r", "a", "th", "a"), "iñ", "4.1.95", "dāśarathi"), (("d", "a", "kṣ", "a"), "iñ", "4.1.95", "dākṣi"),
    (("g", "a", "r", "g", "a"), "yañ", "4.1.105", "gārgya"), (("ś", "i", "v", "a"), "aṇ", "4.3.120", "śaiva"),
    (("b", "u", "ddh", "a"), "aṇ", "4.3.120", "bauddha"), (("p", "u", "r", "ā", "ṇ", "a"), "ṭhak", "4.3.120", "paurāṇika"),
]
ALL_STAGES = ("7.2.117", "7.2.118", "6.4.146", "6.4.148", "7.3.50", "6.1.78")


def derive(stem: tuple[str, ...], affix: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = list(stem)
    a = its(affix, "pratyaya", taddhita=True)
    aff = list(a["remaining_sounds"])
    marks = a["its"]
    path = [f"{''.join(st)} + {affix} → {''.join(aff)} (its {marks}; taddhita 4.1.76; prātipadika 1.2.46)"]
    nit = "ṇ" in marks or "ñ" in marks
    kit = "k" in marks
    if "7.3.50" in on and aff[:2] == ["ṭh", "a"]:
        aff = ["i", "k", "a"] + aff[2:]; path.append("ṭha → ika (7.3.50 ṭhasyekaḥ)")
    if (nit and "7.2.117" in on) or (kit and "7.2.118" in on):
        k = next(i for i, s in enumerate(st) if s in VOWELS)
        v = antaratama(TO58[st[k]], VRDDHI_SET)
        st[k] = V58[v]; path.append(f"vṛddhi of the first vowel before the taddhita (" + ("7.2.117 ñit / ṇit" if nit else "7.2.118 kiti ca") + f"; 1.1.50) → {''.join(st)}")
    # bha operations (1.4.18: the stem before the vowel-initial taddhita is bha; 6.4.129 adhikāra)
    if st[-1] == "u" and "6.4.146" in on:
        g = antaratama("u", GUNA_SET)
        st[-1] = V58[g]; path.append("final u of the bha → guṇa before the taddhita (6.4.146 or guṇaḥ)")
        if "6.1.78" in on and aff and aff[0] in VOWELS and st[-1] in AYADI:
            st = st[:-1] + list(AYADI[st[-1]]); path.append("ayādi before the vowel (6.1.78)")
    elif st[-1] in ("a", "i") and "6.4.148" in on:
        st = st[:-1]; path.append("final a / i of the bha dropped before the taddhita (6.4.148 yasyeti ca)")
    return "".join(st + aff), path


def t1_taddhita() -> dict[str, Any]:
    forms = {exp: derive(st, aff)[0] for st, aff, _, exp in CASES}
    exp_breaks = {"7.2.117": {e for *_, e in CASES if e != "paurāṇika"}, "7.2.118": {"paurāṇika"}, "6.4.146": {"aupagava", "kaurava"}, "6.4.148": {"dāśarathi", "dākṣi", "gārgya", "śaiva", "bauddha", "paurāṇika"}, "7.3.50": {"paurāṇika"}, "6.1.78": {"aupagava", "kaurava"}}
    broken = {s: sorted(e for st, aff, _, e in CASES if derive(st, aff, tuple(x for x in ALL_STAGES if x != s))[0] != e) for s in exp_breaks}
    checks = {"eight_taddhita_derivations_equal_the_classical_forms": all(forms[e] == e for e in forms)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {e: derive(st, aff)[1] for st, aff, _, e in CASES}, "senses": {e: s for *_, s, e in CASES}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_taddhita": t1_taddhita()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_TADDHITA_AN_IN_YAN_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_TADDHITA_AN_IN_YAN_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.taddhita_an_in_yan_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "aupagava, kaurava, dāśarathi, dākṣi, gārgya, śaiva, bauddha, paurāṇika by the quoted sense sūtras with 7.2.117 / 7.2.118 (first-vowel vṛddhi by theorum/80's antaratama), 6.4.146, 6.4.148, 7.3.50, 6.1.78; each rule breaks exactly the derivations stated",
            ],
            "NOT_claimed": ["the choice of affix per stem is declared from the sense sūtra / gaṇa (gargādi, the ṭhak of purāṇa), not inferred; feminines (ṅīp / ṣyaṅ), 1.1.73 vṛddha, the exceptions of 7.3, declension (a-stems: theorum/63)", "RH, YM untouched"],
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
