from __future__ import annotations

"""Exact certificate (theorum/110): THE PASSIVE (karmaṇi / bhāve) COMPILED — ten
roots with yak (3.1.67) in laṭ ātmanepada 3s / 3p (1.3.13): the kit of yak
blocking guṇa (1.1.5), 6.4.66 ghumāsthāgāpājahātisāṁ hali (dīyate, sthīyate),
the samprasāraṇa 6.1.15 + 6.1.108 with 1.1.45 (ucyate, supyate, ijyate), the 3p
jha → anta (7.1.3) with 6.1.97 and 3.4.79; each rule shown load-bearing on
exactly the forms it governs.

Quoted sūtras:
 3.1.67   sārvadhātuke yak                                yak before a sārvadhātuka in bhāva / karman (3.4.69)
 3.4.69   laḥ karmaṇi ca bhāve cākarmakebhyaḥ ; 1.3.13 bhāvakarmaṇoḥ (ātmanepada)
 1.3.3    halantyam (the k of yak) ; 1.1.5 kṅiti ca (no guṇa) ; 3.4.113 tiṅśit sārvadhātukam
 6.4.66   ghumāsthāgāpājahātisāṁ hali                     ā → ī before a hal-initial kit / ṅit ārdhadhātuka: dīyate, sthīyate
 6.1.15   vacisvapiyajādīnāṁ kiti                          samprasāraṇa before kit: vac, svap, yaj
 6.1.108  samprasāraṇāc ca ; 1.1.45 ig yaṇaḥ samprasāraṇam     the yaṇ → ik and the following vowel absorbed: uc, sup, ij
 7.1.3    jho 'ntaḥ ; 6.1.97 ato guṇe ; 3.4.79 ṭita ātmanepadānāṁ ṭer e ; 3.4.78

 T1  bhūyate, nīyate, gamyate, pacyate, labhyate, hanyate, dīyate, sthīyate,
     ucyate, supyate, ijyate — eleven roots, 3s and 3p: 22 forms.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import GUNA_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.1.67": "sārvadhātuke yak", "3.4.69": "laḥ karmaṇi ca bhāve cākarmakebhyaḥ", "1.3.13": "bhāvakarmaṇoḥ", "1.3.3": "halantyam", "1.1.5": "kṅiti ca",
    "3.4.113": "tiṅśit sārvadhātukam", "6.4.66": "ghumāsthāgāpājahātisāṁ hali", "6.1.15": "vacisvapiyajādīnāṁ kiti", "6.1.108": "samprasāraṇāc ca",
    "1.1.45": "ig yaṇaḥ samprasāraṇam", "7.1.3": "jho 'ntaḥ", "6.1.97": "ato guṇe", "3.4.79": "ṭita ātmanepadānāṁ ṭer e",
    "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ",
}
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
FROM58 = {"e": "e", "o": "o", "a": "a"}
SAMPRASARANA = {"y": "i", "v": "u", "r": "ṛ"}   # 1.1.45
GHU_MA_STHA = {"dā", "sthā"}                    # 6.4.66: ghu (dā, dhā), mā, sthā, gā, pā, hā, sā — the two taken here
VAC_LIST = {"vac", "svap", "yaj"}               # 6.1.15 vacisvapiyajādīnāṁ
ROOTS = {"bhū": ("bh", "ū"), "nī": ("n", "ī"), "gam": ("g", "a", "m"), "pac": ("p", "a", "c"), "labh": ("l", "a", "bh"), "han": ("h", "a", "n"),
         "dā": ("d", "ā"), "sthā": ("s", "th", "ā"), "vac": ("v", "a", "c"), "svap": ("s", "v", "a", "p"), "yaj": ("y", "a", "j")}
ORACLE = {"bhū": "bhūya", "nī": "nīya", "gam": "gamya", "pac": "pacya", "labh": "labhya", "han": "hanya", "dā": "dīya", "sthā": "sthīya",
          "vac": "ucya", "svap": "supya", "yaj": "ijya"}
CELLS = [("3s", "ta"), ("3p", "jha")]
ALL_STAGES = ("1.1.5", "6.4.66", "6.1.15", "6.1.108", "7.1.3", "6.1.97", "3.4.79")


def passive(name: str, code: str, up: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = list(ROOTS[name])
    y = its("yak", "pratyaya")
    assert y["remaining_sounds"] == ("y", "a") and set(y["its"]) == {"k"}
    path = [f"{name} + yak (3.1.67, bhāve / karmaṇi 3.4.69; k it 1.3.3 → ya; kit; ātmanepada 1.3.13)"]
    if name in VAC_LIST and "6.1.15" in on:
        k = next(i for i, s in enumerate(r) if s in SAMPRASARANA and i + 1 < len(r) and r[i + 1] in ("a",))
        r[k] = SAMPRASARANA[r[k]]; path.append(f"samprasāraṇa of the yaṇ before the kit (6.1.15; 1.1.45 ig yaṇaḥ): {''.join(r)}")
        if "6.1.108" in on:
            del r[k + 1]; path.append(f"the following vowel absorbed into the samprasāraṇa (6.1.108 samprasāraṇāc ca): {''.join(r)}")
    if name in GHU_MA_STHA and "6.4.66" in on:
        r[-1] = "ī"; path.append("ā → ī before the hal-initial kit ārdhadhātuka ya (6.4.66 ghumāsthāgāpājahātisāṁ hali)")
    if r[-1] in IK:
        if "1.1.5" in on:
            path.append("no guṇa of the final ik before the kit yak (1.1.5 kṅiti ca)")
        else:
            g = rapara_1_1_51(IK[r[-1]], antaratama(IK[r[-1]], GUNA_SET)); r = r[:-1] + list(FROM58.get(g, g)); path.append(f"(1.1.5 off: 7.3.84 guṇa) {''.join(r)}")
    stem = r + ["y", "a"]
    t = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    if up == "jha" and "7.1.3" in on:
        t = ["a", "n", "t"] + t[1:]; path.append("jh → ant (7.1.3 jho 'ntaḥ)")
    if "3.4.79" in on:
        t = t[:-1] + ["e"]; path.append("ṭi of the ṭit ātmanepada ending → e (3.4.79)")
    if t and t[0] == "a" and stem[-1] == "a" and "6.1.97" in on:
        t = t[1:]; path.append("a + a → a (6.1.97 ato guṇe)")
    word = stem + t
    path.append(f"{''.join(stem)}-{''.join(t)} (3.4.78; sārvadhātuka 3.4.113) → {''.join(word)}")
    return "".join(word), path


def forms_for(name: str, stages=ALL_STAGES) -> dict[str, str]:
    return {c: passive(name, c, up, stages)[0] for c, up in CELLS}


def oracle(name: str) -> dict[str, str]:
    return {"3s": ORACLE[name] + "te", "3p": ORACLE[name] + "nte"}


def t1_passive() -> dict[str, Any]:
    forms = {n: forms_for(n) for n in ROOTS}
    exp = {n: oracle(n) for n in ROOTS}
    cells = lambda names: {f"{n}.{c}" for n in names for c, _ in CELLS}
    exp_breaks = {"1.1.5": cells(["bhū", "nī", "dā", "sthā"]), "6.4.66": cells(["dā", "sthā"]), "6.1.15": cells(VAC_LIST), "6.1.108": cells(VAC_LIST),
                  "7.1.3": {f"{n}.3p" for n in ROOTS}, "6.1.97": {f"{n}.3p" for n in ROOTS}, "3.4.79": cells(ROOTS)}
    broken = {s: sorted(f"{n}.{c}" for n in ROOTS for c, _ in CELLS if forms_for(n, tuple(x for x in ALL_STAGES if x != s))[c] != exp[n][c]) for s in exp_breaks}
    checks = {"twenty_two_passive_forms_equal_the_classical_forms": all(forms[n][c] == exp[n][c] for n in ROOTS for c, _ in CELLS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {n: passive(n, "3s", "ta")[1] for n in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_passive": t1_passive()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PASSIVE_YAK_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_PASSIVE_YAK_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.passive_yak_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "eleven roots in the passive laṭ 3s / 3p (22 forms) by 3.1.67 with 1.1.5, 6.4.66, 6.1.15 + 6.1.108 (1.1.45), 7.1.3, 6.1.97, 3.4.79; each rule breaks exactly the forms stated",
            ],
            "NOT_claimed": [
                "the membership of vac / svap / yaj in 6.1.15's list and of dā / sthā in 6.4.66's list is read from the sūtra, not derived; kṛ (7.4.28 rīṅ) and other ṛ-final roots; ṇic / san passives; other persons and lakāras; the agent in the instrumental",
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
