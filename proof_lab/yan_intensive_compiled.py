from __future__ import annotations

"""Exact certificate (theorum/108): yaṅ INTENSIVES COMPILED — six roots with yaṅ
(3.1.22) in laṭ ātmanepada 3s (1.3.12): 7.4.27 rīṅ ṛtaḥ before the
reduplication, 6.1.9 on theorum/102's abhyāsa carrier, the abhyāsa guṇa 7.4.82
and the dīrgha 7.4.83 with its apavāda 7.4.85 (nuk, then 8.3.24 + 8.4.58 →
jaṅ-), 7.4.62, 8.4.54, the ṅit blocking guṇa (1.1.5), 3.4.79; each rule shown
load-bearing on exactly the forms it governs.

Quoted sūtras:
 3.1.22   dhātor ekāco halādeḥ kriyāsamabhihāre yaṅ     yaṅ after a monosyllabic consonant-initial root
 1.3.12   anudāttaṅita ātmanepadam                        yaṅ is ṅit → ātmanepada ; 1.3.3 halantyam (ṅ) ; 3.1.32
 6.1.9    sanyaṅoḥ                                       reduplication (6.1.1, 6.1.4)
 7.4.82   guṇo yaṅlukoḥ                                  abhyāsa guṇa: bo-, ne-, de-, ce-
 7.4.83   dīrgho 'kitaḥ                                  abhyāsa a → ā before the non-kit yaṅ: pā-pac
 7.4.85   nugato 'nunāsikāntasya                         nuk to the a-abhyāsa of a nasal-final root (apavāda of 7.4.83): gan-gam
 8.3.24   naś cāpadāntasya jhali ; 8.4.58 anusvārasya yayi parasavarṇaḥ     gan → gaṁ → gaṅ ; 7.4.62 kuhoś cuḥ → jaṅ
 7.4.27   rīṅ ṛtaḥ                                       kṛ → krī before yaṅ (then reduplicated: ce-krī)
 7.4.59   hrasvaḥ ; 7.4.60 halādiḥ śeṣaḥ ; 7.4.62 kuhoś cuḥ ; 8.4.54 abhyāse car ca
 1.1.5    kṅiti ca                                       no guṇa of the root before the ṅit yaṅ
 3.1.68   kartari śap ; 3.4.78 ; 3.4.79 ṭita ātmanepadānāṁ ṭer e ; 6.1.97 ato guṇe

 T1  bobhūyate, pāpacyate, cekrīyate, dedīpyate, nenīyate, jaṅgamyate — 6 forms.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.lit_parasmaipada_compiled import abhyasa
from proof_lab.paninian_instruction_format import GUNA_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.1.22": "dhātor ekāco halādeḥ kriyāsamabhihāre yaṅ", "1.3.12": "anudāttaṅita ātmanepadam", "1.3.3": "halantyam", "3.1.32": "sanādyantā dhātavaḥ",
    "6.1.9": "sanyaṅoḥ", "7.4.82": "guṇo yaṅlukoḥ", "7.4.83": "dīrgho 'kitaḥ", "7.4.85": "nugato 'nunāsikāntasya",
    "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "7.4.27": "rīṅ ṛtaḥ",
    "7.4.59": "hrasvaḥ", "7.4.60": "halādiḥ śeṣaḥ", "7.4.62": "kuhoś cuḥ", "8.4.54": "abhyāse car ca", "1.1.5": "kṅiti ca",
    "3.1.68": "kartari śap", "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "3.4.79": "ṭita ātmanepadānāṁ ṭer e", "6.1.97": "ato guṇe",
}
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
FROM58 = {"e": "e", "o": "o", "a": "a"}
NASAL = {"m", "n", "ṇ", "ñ", "ṅ"}
ROOTS = {"bhū": ("bh", "ū"), "pac": ("p", "a", "c"), "kṛ": ("k", "ṛ"), "dīp": ("d", "ī", "p"), "nī": ("n", "ī"), "gam": ("g", "a", "m")}
ORACLE = {"bhū": "bobhūyate", "pac": "pāpacyate", "kṛ": "cekrīyate", "dīp": "dedīpyate", "nī": "nenīyate", "gam": "jaṅgamyate"}
ALL_STAGES = ("7.4.27", "6.1.9", "7.4.59", "7.4.60", "7.4.62", "8.4.54", "7.4.82", "7.4.83", "7.4.85", "8.3.24", "8.4.58", "1.1.5", "3.4.79")
ABHYASA_STAGES = {"6.1.9": "6.1.8", "7.4.59": "7.4.59", "7.4.60": "7.4.60", "7.4.62": "7.4.62", "8.4.54": "8.4.54"}   # theorum/102's carrier; 7.4.66 / 7.4.73 (liṭ) never on


def intensive(name: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    root = list(ROOTS[name])
    y = its("yaṅ", "pratyaya")
    assert y["remaining_sounds"] == ("y", "a") and set(y["its"]) == {"ṅ"}
    path = [f"{name} + yaṅ (3.1.22; ṅ it 1.3.3 → ya; ṅit → ātmanepada 1.3.12; the yaṅanta is a dhātu 3.1.32)"]
    if root[-1] == "ṛ" and "7.4.27" in on:
        root = root[:-1] + ["r", "ī"]; path.append(f"ṛ → rī before yaṅ (7.4.27 rīṅ ṛtaḥ): {''.join(root)}")
    ab_on = {ABHYASA_STAGES[k] for k in ABHYASA_STAGES if k in on}
    # the carrier applies 7.4.62 / 8.4.54 to the consonant and 7.4.59 / 7.4.60 to the shape; the yaṅ vowel rules follow
    ab = abhyasa(list(root), path, ab_on) if "6.1.9" in on else []
    if ab:
        k = next(i for i, x in enumerate(path) if "6.1.8" in x)
        path[k] = path[k].replace("6.1.8", "6.1.9 sanyaṅoḥ")
    if ab and ab[-1] in IK and "7.4.82" in on:
        g = antaratama(IK[ab[-1]], GUNA_SET)
        ab[-1] = FROM58[g]; path.append(f"abhyāsa vowel → guṇa before yaṅ (7.4.82 guṇo yaṅlukoḥ): {''.join(ab)}")
    if ab and ab[-1] == "a":
        if root[-1] in NASAL and "7.4.85" in on:
            ab = ab + ["n"]; path.append("nuk to the a-abhyāsa of the nasal-final root (7.4.85 nugato 'nunāsikāntasya; apavāda of 7.4.83)")
            if "8.3.24" in on:
                ab[-1] = "ṁ"; path.append("n → anusvāra before the jhal (8.3.24 naś cāpadāntasya jhali)")
                if "8.4.58" in on:
                    ab[-1] = "ṅ"; path.append("anusvāra → the parasavarṇa ṅ before the yay (8.4.58)")
        elif "7.4.83" in on:
            ab[-1] = "ā"; path.append(f"abhyāsa a → ā before the non-kit yaṅ (7.4.83 dīrgho 'kitaḥ): {''.join(ab)}")
    st = list(root)
    if st[-1] in IK and "1.1.5" not in on:
        g = rapara_1_1_51(IK[st[-1]], antaratama(IK[st[-1]], GUNA_SET))
        st = st[:-1] + list(FROM58.get(g, g)); path.append(f"(1.1.5 off: guṇa 7.3.84 applied) {''.join(st)}")
    else:
        path.append("no guṇa of the root before the ṅit yaṅ (1.1.5 kṅiti ca)")
    sap = list(its("śap", "pratyaya")["remaining_sounds"])
    t = list(its("ta", "pratyaya", vibhakti=True)["remaining_sounds"])
    if "3.4.79" in on:
        t = t[:-1] + ["e"]; path.append("ṭi of the ṭit ātmanepada ending → e (3.4.79): te")
    word = ab + st + ["y", "a"] + sap[1:] + t
    path.append(f"{''.join(ab)}-{''.join(st)}-ya-a-{''.join(t)} (3.1.68 śap; 6.1.97 ato guṇe; 3.4.78) → {''.join(word)}")
    return "".join(word), path


def t1_yan() -> dict[str, Any]:
    forms = {r: intensive(r)[0] for r in ROOTS}
    exp_breaks = {
        "7.4.27": {"kṛ"}, "6.1.9": set(ROOTS), "7.4.59": set(), "7.4.60": {"kṛ"}, "7.4.62": {"kṛ", "gam"}, "8.4.54": {"bhū"},
        "7.4.82": {"bhū", "kṛ", "dīp", "nī"}, "7.4.83": {"pac"}, "7.4.85": {"gam"}, "8.3.24": {"gam"}, "8.4.58": {"gam"},
        "1.1.5": {"bhū", "kṛ", "nī"}, "3.4.79": set(ROOTS),
    }
    broken = {s: sorted(r for r in ROOTS if intensive(r, tuple(x for x in ALL_STAGES if x != s))[0] != ORACLE[r]) for s in exp_breaks}
    checks = {"six_intensives_equal_the_classical_forms": all(forms[r] == ORACLE[r] for r in ROOTS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {r: intensive(r)[1] for r in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_yan": t1_yan()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_YAN_INTENSIVE_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_YAN_INTENSIVE_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.yan_intensive_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "six intensives in laṭ ātmanepada 3s by 3.1.22 / 1.3.12 with 7.4.27, 6.1.9 (theorum/102's abhyāsa carrier: 7.4.59, 7.4.60, 7.4.62, 8.4.54), 7.4.82, 7.4.83 with its apavāda 7.4.85 (+ 8.3.24, 8.4.58), 1.1.5, 3.4.79; each rule breaks exactly the forms stated",
                "7.4.59 hrasvaḥ is recorded as not load-bearing here: the abhyāsa guṇa 7.4.82 (by 1.1.50) gives the same guṇa from the long and from the shortened vowel",
            ],
            "NOT_claimed": [
                "yaṅ-luk (2.4.74 yaṅo 'ci ca: bobhavīti etc.), other persons / lakāras, the 7.4.84–92 abhyāsa augments (nīk, ruk, rik …), the optional forms",
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
