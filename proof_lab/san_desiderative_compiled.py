from __future__ import annotations

"""Exact certificate (theorum/106): san DESIDERATIVES COMPILED — nine roots with
san (3.1.7) in laṭ 3s: reduplication by 6.1.9 on theorum/102's abhyāsa
carrier (with 7.4.79 sanyataḥ in place of liṭ's 7.4.73), the iṭ decision
7.2.35 / 7.2.10 / 7.2.58, the kit of 1.2.9 blocking guṇa, 7.1.100 + 8.2.77 for
kṛ, the ṣatva 8.3.59 after iṇ / ku, 8.2.30 for pac, the is-substitution 7.4.54
with 7.4.49 and 7.4.58 for dā, and the ātmanepada of jñā (1.3.57, 3.4.79);
each rule shown load-bearing on exactly the forms it governs.

Quoted sūtras:
 3.1.7    dhātoḥ karmaṇaḥ samānakartṛkād icchāyāṁ vā     san
 3.1.32   sanādyantā dhātavaḥ ; 3.4.114 ārdhadhātukaṁ śeṣaḥ ; 1.3.3 halantyam (n of san)
 6.1.9    sanyaṅoḥ                                      reduplication before san (6.1.1, 6.1.4)
 7.4.79   sanyataḥ                                      abhyāsa a → i before san
 7.4.59   hrasvaḥ ; 7.4.60 halādiḥ śeṣaḥ ; 7.4.62 kuhoś cuḥ ; 7.4.66 ur at ; 8.4.54 abhyāse car ca
 7.2.35   ārdhadhātukasyeḍ valādeḥ ; 7.2.10 ekāca upadeśe 'nudāttāt ; 7.2.58 gamer iṭ parasmaipadeṣu
 1.2.9    iko jhal                                      san after an ik-final root is kit (no guṇa: 1.1.5)
 7.3.84   sārvadhātukārdhadhātukayoḥ ; 1.1.5 kṅiti ca
 6.4.16   ajjhanagamāṁ sani ; 7.1.100 ṝta id dhātoḥ ; 8.2.77 hali ca     kṛ → kṝ → kir → kīr
 8.3.59   ādeśapratyayayoḥ (8.3.57 iṇkoḥ)                s of san → ṣ after iṇ / ku
 8.2.30   coḥ kuḥ                                        pac + s → pakṣ
 7.4.54   sani mīmāghurabhalabhaśakapatapadām aca is ; 7.4.49 saḥ syārdhadhātuke ; 7.4.58 atra lopo 'bhyāsasya     ditsati
 1.3.57   jñāśrusmṛdṛśāṁ sanaḥ ; 3.4.79 ṭita ātmanepadānāṁ ṭer e     jijñāsate
 3.1.68   kartari śap ; 3.4.78 ; 1.3.78

 T1  pipaṭhiṣati, bubhūṣati, cikīrṣati, jigamiṣati, pipāsati, ninīṣati,
     pipakṣati, jijñāsate, ditsati — 9 forms.
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
    "3.1.7": "dhātoḥ karmaṇaḥ samānakartṛkād icchāyāṁ vā", "3.1.32": "sanādyantā dhātavaḥ", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "1.3.3": "halantyam",
    "6.1.9": "sanyaṅoḥ", "7.4.79": "sanyataḥ", "7.4.59": "hrasvaḥ", "7.4.60": "halādiḥ śeṣaḥ", "7.4.62": "kuhoś cuḥ", "7.4.66": "ur at", "8.4.54": "abhyāse car ca",
    "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.10": "ekāca upadeśe 'nudāttāt", "7.2.58": "gamer iṭ parasmaipadeṣu",
    "1.2.9": "iko jhal", "7.3.84": "sārvadhātukārdhadhātukayoḥ", "1.1.5": "kṅiti ca", "6.4.16": "ajjhanagamāṁ sani", "7.1.100": "ṝta id dhātoḥ", "8.2.77": "hali ca",
    "8.3.59": "ādeśapratyayayoḥ", "8.3.57": "iṇkoḥ", "8.2.30": "coḥ kuḥ",
    "7.4.54": "sani mīmāghurabhalabhaśakapatapadām aca is", "7.4.49": "saḥ syārdhadhātuke", "7.4.58": "atra lopo 'bhyāsasya",
    "1.3.57": "jñāśrusmṛdṛśāṁ sanaḥ", "3.4.79": "ṭita ātmanepadānāṁ ṭer e", "3.1.68": "kartari śap", "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "1.3.78": "śeṣāt kartari parasmaipadam",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
FROM58 = {"e": "e", "o": "o", "a": "a", "ar": ("a", "r")}
IN_KU = set(VOWELS) - {"a", "ā"} | {"h", "y", "v", "r", "l", "k", "kh", "g", "gh", "ṅ"}   # iṇ (8.3.57) and ku
ROOTS = {"paṭh": ("p", "a", "ṭh"), "bhū": ("bh", "ū"), "kṛ": ("k", "ṛ"), "gam": ("g", "a", "m"), "pā": ("p", "ā"), "nī": ("n", "ī"),
         "pac": ("p", "a", "c"), "jñā": ("j", "ñ", "ā"), "dā": ("d", "ā")}
ANUDATTA = {"bhū", "kṛ", "pā", "nī", "pac", "jñā", "dā"}   # 7.2.10: anudātta in the Dhātupāṭha (declared), hence no iṭ
GAM_IT = {"gam"}            # 7.2.58
GHU_IS = {"dā"}             # 7.4.54: ghu (dā) — ac → is before an iṭ-less san
ATMANEPADA = {"jñā"}        # 1.3.57
ORACLE = {"paṭh": "pipaṭhiṣati", "bhū": "bubhūṣati", "kṛ": "cikīrṣati", "gam": "jigamiṣati", "pā": "pipāsati", "nī": "ninīṣati",
          "pac": "pipakṣati", "jñā": "jijñāsate", "dā": "ditsati"}
ALL_STAGES = ("6.1.9", "7.4.79", "7.4.59", "7.4.60", "7.4.62", "7.4.66", "8.4.54", "7.2.35", "7.2.10", "7.2.58", "1.2.9", "6.4.16", "7.1.100", "8.2.77",
              "8.3.59", "8.2.30", "7.4.54", "7.4.49", "7.4.58", "3.4.79")
ABHYASA_STAGES = {"6.1.9": "6.1.8", "7.4.59": "7.4.59", "7.4.60": "7.4.60", "7.4.62": "7.4.62", "7.4.66": "7.4.66", "8.4.54": "8.4.54"}   # theorum/102's carrier, 7.4.73 (liṭ only) never on


def desiderative(name: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    root = list(ROOTS[name])
    s = its("san", "pratyaya")
    assert s["remaining_sounds"] == ("s", "a") and set(s["its"]) == {"n"}
    path = [f"{name} + san (3.1.7; n it 1.3.3 → sa; ārdhadhātuka 3.4.114; the sannanta is a dhātu 3.1.32)"]
    # iṭ decision: 7.2.35 for the valādi ārdhadhātuka, blocked by 7.2.10, restored for gam by 7.2.58
    it: list[str] = []
    if "7.2.35" in on:
        if name in ANUDATTA and "7.2.10" in on:
            path.append("no iṭ: the root is anudātta in the upadeśa (7.2.10)")
        elif name in GAM_IT and "7.2.58" not in on:
            path.append("no iṭ (7.2.58 off)")
        else:
            it = ["i"]; path.append("iṭ before the valādi ārdhadhātuka san (7.2.35" + ("; 7.2.58 gamer iṭ parasmaipadeṣu)" if name in GAM_IT else ")"))
    kit = (not it) and root[-1] in IK and "1.2.9" in on
    if kit:
        path.append("san (jhalādi, after an ik-final root) is kit (1.2.9): no guṇa (1.1.5)")
    # reduplication on theorum/102's abhyāsa carrier
    ab_on = {ABHYASA_STAGES[k] for k in ABHYASA_STAGES if k in on}
    ab = abhyasa(list(root), path, ab_on) if "6.1.9" in on else []
    if ab:
        path[-len(path) + path.index(next(x for x in path if "6.1.8" in x))] = next(x for x in path if "6.1.8" in x).replace("6.1.8", "6.1.9 sanyaṅoḥ")
    if ab and ab[-1] == "a" and "7.4.79" in on:
        ab[-1] = "i"; path.append(f"abhyāsa a → i before san (7.4.79 sanyataḥ): {''.join(ab)}")
    st = list(root)
    if name in GHU_IS and not it and "7.4.54" in on:
        st = st[:-1] + ["i", "s"]; path.append("the ac of the ghu root → is before the iṭ-less san (7.4.54)")
        if "7.4.49" in on:
            st[-1] = "t"; path.append("s → t before the s-initial ārdhadhātuka (7.4.49 saḥ syārdhadhātuke)")
        if "7.4.58" in on and ab:
            ab = []; path.append("the abhyāsa is deleted (7.4.58 atra lopo 'bhyāsasya)")
    if st[-1] in ("ṛ", "ū", "ī") and not it and "6.4.16" in on:
        st[-1] = {"ṛ": "ṝ", "ū": "ū", "ī": "ī"}[st[-1]]; path.append(f"root-final vowel lengthened before the jhalādi san (6.4.16 ajjhanagamāṁ sani): {''.join(st)}")
    if st[-1] == "ṝ" and kit and "7.1.100" in on:
        st = st[:-1] + ["i", "r"]; path.append("root-final ṝ → ir (7.1.100 ṝta id dhātoḥ)")
        if "8.2.77" in on:
            st[-2] = "ī"; path.append("ir → īr before hal (8.2.77 hali ca)")
    if st[-1] in IK and not kit:
        g = antaratama(IK[st[-1]], GUNA_SET)
        g = rapara_1_1_51(IK[st[-1]], g)
        st = st[:-1] + list(FROM58.get(g, g)); path.append(f"guṇa of the final ik before the ārdhadhātuka (7.3.84): {''.join(st)}")
    aff = ["s", "a"]
    if st[-1] == "c" and "8.2.30" in on:
        st[-1] = "k"; path.append("c → k before the jhal (8.2.30 coḥ kuḥ)")
    before = (it or st)[-1]
    if before in IN_KU and "8.3.59" in on:
        aff[0] = "ṣ"; path.append(f"s → ṣ after {before} (8.3.59 ādeśapratyayayoḥ; 8.3.57 iṇkoḥ)")
    sap = list(its("śap", "pratyaya")["remaining_sounds"])
    ting = "ta" if name in ATMANEPADA else "tip"
    t = list(its(ting, "pratyaya", vibhakti=True)["remaining_sounds"])
    if name in ATMANEPADA:
        path.append("ātmanepada after san of jñā (1.3.57)")
        if "3.4.79" in on:
            t = t[:-1] + ["e"]; path.append("ṭi of the ṭit ātmanepada ending → e (3.4.79): te")
    # a + a → a between san and śap (6.1.97)
    word = ab + st + it + aff + sap[1:] + t
    path.append(f"{''.join(ab)}-{''.join(st + it)}-{''.join(aff)}-{''.join(sap)}-{''.join(t)} (3.1.68 śap; 6.1.97 ato guṇe; 3.4.78) → {''.join(word)}")
    return "".join(word), path


def t1_san() -> dict[str, Any]:
    forms = {r: desiderative(r)[0] for r in ROOTS}
    exp_breaks = {
        "6.1.9": set(ROOTS) - {"dā"}, "7.4.79": {"paṭh", "kṛ", "gam", "pā", "pac", "jñā"}, "7.4.59": {"pā", "nī", "bhū", "jñā"},
        "7.4.60": {"jñā"}, "7.4.62": {"kṛ", "gam"}, "7.4.66": {"kṛ"}, "8.4.54": {"bhū"},
        "7.2.35": {"paṭh", "gam"}, "7.2.10": {"bhū", "kṛ", "pā", "nī", "pac", "jñā", "dā"}, "7.2.58": {"gam"},
        "1.2.9": {"bhū", "kṛ", "nī"}, "6.4.16": {"kṛ"}, "7.1.100": {"kṛ"}, "8.2.77": {"kṛ"},
        "8.3.59": {"paṭh", "bhū", "kṛ", "gam", "nī", "pac"}, "8.2.30": {"pac"}, "7.4.54": {"dā"}, "7.4.49": {"dā"}, "7.4.58": {"dā"}, "3.4.79": {"jñā"},
    }
    broken = {s: sorted(r for r in ROOTS if desiderative(r, tuple(x for x in ALL_STAGES if x != s))[0] != ORACLE[r]) for s in exp_breaks}
    checks = {"nine_desideratives_equal_the_classical_forms": all(forms[r] == ORACLE[r] for r in ROOTS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {r: desiderative(r)[1] for r in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_san": t1_san()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SAN_DESIDERATIVE_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_SAN_DESIDERATIVE_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.san_desiderative_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "nine desideratives in laṭ 3s by 3.1.7 with 6.1.9 (theorum/102's abhyāsa carrier: 7.4.59, 7.4.60, 7.4.62, 7.4.66, 8.4.54) and 7.4.79, the iṭ decision 7.2.35 / 7.2.10 / 7.2.58, 1.2.9, 6.4.16, 7.1.100, 8.2.77, 8.3.59, 8.2.30, 7.4.54, 7.4.49, 7.4.58, 1.3.57 with 3.4.79; each rule breaks exactly the forms stated",
            ],
            "NOT_claimed": [
                "the anudātta status of the roots (7.2.10) is declared from the Dhātupāṭha accent, not read from it; the ghu status of dā (1.1.20) is declared",
                "6.4.16 is vacuous on bhū and nī (already long) and so an ablation target only through kṛ",
                "other persons and lakāras, the sannanta's kṛt forms (bubhūṣā, cikīrṣu), roots with 7.4.55–57, the optional forms",
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
