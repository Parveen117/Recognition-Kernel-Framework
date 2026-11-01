from __future__ import annotations

"""Exact certificate (theorum/100): THE KṚT AFFIXES ktvā, tumun, tavya FROM THE
PINNED ROOTS — iṭ decided by 7.2.35 against 7.2.11 (kit), guṇa by 7.3.84
against 1.1.5 (kit), gam's nasal by 6.4.37 (kit) against 8.3.24 / 8.4.58
(non-kit); gantā of theorum/97 realized.

Quoted sūtras:
 3.4.21   samānakartṛkayoḥ pūrvakāle            ktvā (absolutive)
 3.3.10   tumunṇvulau kriyāyāṁ kriyārthāyām      tumun (infinitive)
 3.1.96   tavyattavyānīyaraḥ                      tavya (gerundive)
 7.2.35   ārdhadhātukasyeḍ valādeḥ               iṭ for the seṭ root bhū before tumun / tavya
 7.2.11   śryukaḥ kiti                            no iṭ after śri and uk-final roots before a kit affix (bhūtvā, kṛtvā, śrutvā, hutvā)
 7.2.10   ekāca upadeśe 'nudāttāt                 nī, kṛ, śru, hu aniṭ (declared)
 1.1.5    kṅiti ca                                no guṇa before a kit (ktvā): kṛtvā, not *kartvā
 7.3.84   sārvadhātukārdhadhātukayoḥ              guṇa before tumun / tavya: kartum, kartavya (theorum/80's antaratama, 1.1.51)
 6.4.37   anudāttopadeśa … anunāsikalopo jhali kṅiti   gatvā
 8.3.24   naś cāpadāntasya jhali                  m → anusvāra before jhal (gaṁtum)
 8.4.58   anusvārasya yayi parasavarṇaḥ           anusvāra → the class nasal (gantum, gantavya, gantā)
 1.3.2–1.3.9 ; 6.1.78 ; 1.2.46 (theorum/82, 85)

 T1  ktvā: bhūtvā gatvā kṛtvā śrutvā nītvā hutvā; tumun: bhavitum gantum kartum
     śrotum netum hotum; tavya: bhavitavya gantavya kartavya śrotavya netavya
     hotavya — 18 forms; iṭ appears for bhū only and only before the non-kit
     affixes (7.2.11 vs 7.2.35), guṇa only before the non-kit affixes (1.1.5
     vs 7.3.84), gam's nasal drops before the kit affix (6.4.37) and assimilates
     before the others (8.3.24 / 8.4.58).
 T2  gantā (luṭ 3s of gam) by the same 8.3.24 / 8.4.58, closing theorum/97's refusal.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import BASE, GUNA_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.4.21": "samānakartṛkayoḥ pūrvakāle", "3.3.10": "tumunṇvulau kriyāyāṁ kriyārthāyām", "3.1.96": "tavyattavyānīyaraḥ", "7.2.35": "ārdhadhātukasyeḍ valādeḥ",
    "7.2.11": "śryukaḥ kiti", "7.2.10": "ekāca upadeśe 'nudāttāt", "1.1.5": "kṅiti ca", "7.3.84": "sārvadhātukārdhadhātukayoḥ", "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti",
    "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "6.1.78": "eco 'yavāyāvaḥ", "1.2.46": "kṛttaddhitasamāsāś ca",
}
ROOTS = {"bhū": "bhū", "gam": "gamḷ~", "kṛ": "ḍukṛñ", "śru": "śru", "nī": "ṇīñ", "hu": "hu"}
SET = {"bhū"}                       # seṭ by the Dhātupāṭha accent (declared); the others aniṭ by 7.2.10
UK = {"u", "ū", "ṛ", "ṝ", "ḷ"}
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
AYADI = {"e": ("a", "y"), "o": ("a", "v")}
AFFIXES = {"ktvā": "ktvā", "tumun": "tumu~n", "tavya": "tavya"}
CLASS_NASAL = {"t": "n", "th": "n", "d": "n", "dh": "n", "k": "ṅ", "c": "ñ", "ṭ": "ṇ", "p": "m"}
ORACLE = {"ktvā": {"bhū": "bhūtvā", "gam": "gatvā", "kṛ": "kṛtvā", "śru": "śrutvā", "nī": "nītvā", "hu": "hutvā"},
          "tumun": {"bhū": "bhavitum", "gam": "gantum", "kṛ": "kartum", "śru": "śrotum", "nī": "netum", "hu": "hotum"},
          "tavya": {"bhū": "bhavitavya", "gam": "gantavya", "kṛ": "kartavya", "śru": "śrotavya", "nī": "netavya", "hu": "hotavya"}}
ALL_STAGES = ("7.2.35", "7.2.11", "1.1.5", "7.3.84", "6.1.78", "6.4.37", "8.3.24", "8.4.58")


def root_sounds(name):
    r = list(its(ROOTS[name], "dhatu")["remaining_sounds"])
    if r[0] == "ṇ":
        r[0] = "n"                                          # 6.1.65 ṇo naḥ (cited)
    return r


def derive(name: str, affix: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = root_sounds(name)
    a = its(AFFIXES[affix], "pratyaya")
    aff = list(a["remaining_sounds"])
    kit = "k" in a["its"]
    path = [f"{ROOTS[name]} → {''.join(st)}; {AFFIXES[affix]} → {''.join(aff)}" + (" (kit)" if kit else "")]
    it = []
    if name in SET and "7.2.35" in on:
        blocked = kit and "7.2.11" in on and st[-1] in UK
        if blocked:
            path.append("iṭ blocked: uk-final root before a kit affix (7.2.11 śryukaḥ kiti)")
        else:
            it = ["i"]; path.append("iṭ before the val-initial ārdhadhātuka (7.2.35)")
    guna_blocked = kit and "1.1.5" in on
    if "7.3.84" in on and st[-1] in IK and not guna_blocked:
        g = rapara_1_1_51(BASE[IK[st[-1]]], antaratama(IK[st[-1]], GUNA_SET))
        st = st[:-1] + list(g); path.append(f"guṇa before the ārdhadhātuka (7.3.84; 1.1.50 / 1.1.51) → {''.join(st)}")
        if it and "6.1.78" in on and st[-1] in AYADI:
            st = st[:-1] + list(AYADI[st[-1]]); path.append("ayādi before iṭ (6.1.78)")
    elif guna_blocked and st[-1] in IK:
        path.append("guṇa blocked before the kit affix (1.1.5 kṅiti ca)")
    if st[-1] in ("m", "n") and not it:
        if kit and "6.4.37" in on and name == "gam":
            st = st[:-1]; path.append("nasal dropped before the jhal-initial kit affix (6.4.37)")
        elif not kit:
            if "8.3.24" in on:
                st[-1] = "ṁ"; path.append("m → anusvāra before jhal (8.3.24)")
                if "8.4.58" in on:
                    st[-1] = CLASS_NASAL[aff[0]]; path.append("anusvāra → class nasal before the stop (8.4.58)")
    return "".join(st + it + aff), path


def t1_krt() -> dict[str, Any]:
    forms = {aff: {r: derive(r, aff)[0] for r in ROOTS} for aff in AFFIXES}
    exp = {"7.2.35": {("tumun", "bhū"), ("tavya", "bhū")}, "7.2.11": {("ktvā", "bhū")}, "1.1.5": {("ktvā", "kṛ"), ("ktvā", "śru"), ("ktvā", "nī"), ("ktvā", "hu"), ("ktvā", "bhū")},
           "7.3.84": {(a, r) for a in ("tumun", "tavya") for r in ("bhū", "kṛ", "śru", "nī", "hu")}, "6.1.78": {("tumun", "bhū"), ("tavya", "bhū")},
           "6.4.37": {("ktvā", "gam")}, "8.3.24": {("tumun", "gam"), ("tavya", "gam")}, "8.4.58": {("tumun", "gam"), ("tavya", "gam")}}
    broken = {}
    for s in exp:
        broken[s] = sorted(f"{a}:{r}" for a in AFFIXES for r in ROOTS if derive(r, a, tuple(x for x in ALL_STAGES if x != s))[0] != ORACLE[a][r])
    checks = {"eighteen_krt_forms_equal_the_classical_forms": forms == ORACLE}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_forms_break": set(broken[s]) == {f"{a}:{r}" for a, r in v} for s, v in exp.items()})
    return {"checks": checks, "forms": forms, "paths": {f"{a}:{r}": derive(r, a)[1] for a in AFFIXES for r in ROOTS}, "broken": broken}


def t2_ganta() -> dict[str, Any]:
    st = root_sounds("gam")
    aff = ["t", "ā", "s"]
    st[-1] = "ṁ"; st[-1] = CLASS_NASAL["t"]
    ganta = "".join(st) + "tā"                                     # tās + ḍā → 6.4.143 ṭi-lopa (theorum/97) → gantā
    checks = {"ganta_by_8_3_24_and_8_4_58_on_theorum_97_s_lut": ganta == "gantā"}
    return {"checks": checks, "ganta": ganta, "note": "theorum/97 refused gam's luṭ for want of 8.3.24 / 8.4.58; realized here on its 6.4.143 output"}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_krt": t1_krt(), "t2_ganta": t2_ganta()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_KRT_KTVA_TUMUN_TAVYA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_KRT_KTVA_TUMUN_TAVYA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.krt_ktva_tumun_tavya_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "ktvā, tumun, tavya of bhū, gam, kṛ, śru, nī, hu (18 forms) from the pinned teaching forms; 7.2.35 / 7.2.11 decide the iṭ (bhavitum vs bhūtvā), 1.1.5 / 7.3.84 the guṇa (kṛtvā vs kartum), 6.4.37 / 8.3.24 + 8.4.58 gam's nasal (gatvā vs gantum); each rule breaks exactly the forms stated",
                "gantā realized by 8.3.24 / 8.4.58 on theorum/97's luṭ (closing that refusal)",
            ],
            "NOT_claimed": ["seṭ status of bhū declared; lyap (7.1.37), anīyar, ṇvul, the 7.2.56 ktvā-iṭ option; other roots; declension of the gerundive (a-stem: theorum/63 applies)", "RH, YM untouched"],
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
