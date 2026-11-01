from __future__ import annotations

"""Exact certificate (theorum/117): ĀŚĪRLIṄ ĀTMANEPADA COMPILED — labh and edh in
the benedictive ātmanepada (3s, 3d, 3p, 1s): sīyuṭ (3.4.102), suṭ before t / th
(3.4.107), jha → ran (3.4.105), iṭ → a (3.4.106), 6.1.66 lopo vyor vali, the iṭ
decision 7.2.35 / 7.2.10, 8.4.55 (laps-), 8.3.59 + 8.4.41 (-ṣīṣṭa); each rule
shown load-bearing on exactly its cells.

Quoted sūtras:
 3.3.173  āśiṣi liṅloṭau ; 3.4.116 liṅāśiṣi ; 3.4.104 kid āśiṣi (surface-neutral on labh / edh: recorded) ; 1.3.12
 3.4.102  liṅaḥ sīyuṭ ; 3.4.107 suṭ tithoḥ ; 3.4.105 jhasya ran ; 3.4.106 iṭo 't
 6.1.66   lopo vyor vali (the y of sīy before a val) ; 7.2.35 ; 7.2.10
 8.4.55   khari ca ; 8.3.59 ādeśapratyayayoḥ ; 8.4.41 ṣṭunā ṣṭuḥ ; 3.4.78

 T1  lapsīṣṭa, lapsīyāstām, lapsīran, lapsīya ; edhiṣīṣṭa, edhiṣīyāstām, edhiṣīran, edhiṣīya.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.3.173": "āśiṣi liṅloṭau", "3.4.116": "liṅāśiṣi", "3.4.104": "kid āśiṣi", "1.3.12": "anudāttaṅita ātmanepadam",
    "3.4.102": "liṅaḥ sīyuṭ", "3.4.107": "suṭ tithoḥ", "3.4.105": "jhasya ran", "3.4.106": "iṭo 't", "6.1.66": "lopo vyor vali",
    "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.10": "ekāca upadeśe 'nudāttāt", "8.4.55": "khari ca", "8.3.59": "ādeśapratyayayoḥ", "8.4.41": "ṣṭunā ṣṭuḥ",
    "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
ROOTS = {"labh": ("l", "a", "bh"), "edh": ("e", "dh")}
ANUDATTA = {"labh"}
CELLS = [("3s", "ta"), ("3d", "ātām"), ("3p", "jha"), ("1s", "iṭ")]
ORACLE = {"labh": {"3s": "lapsīṣṭa", "3d": "lapsīyāstām", "3p": "lapsīran", "1s": "lapsīya"},
          "edh": {"3s": "edhiṣīṣṭa", "3d": "edhiṣīyāstām", "3p": "edhiṣīran", "1s": "edhiṣīya"}}
ALL_STAGES = ("3.4.102", "3.4.107", "3.4.105", "3.4.106", "6.1.66", "7.2.35", "7.2.10", "8.4.55", "8.3.59", "8.4.41")


def asirlin(name, code, up, stages=ALL_STAGES):
    on = set(stages)
    st = list(ROOTS[name]); path = [f"{name} + liṅ in āśis (3.3.173); ārdhadhātuka (3.4.116); kit (3.4.104); ātmanepada (1.3.12)"]
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    siy = []
    if "3.4.102" in on:
        s = its("sīyu~ṭ", "agama"); siy = list(s["remaining_sounds"]); path.append(f"sīyuṭ before the ātmanepada ending (3.4.102) → {''.join(siy)}")
    it = []
    if siy and "7.2.35" in on:
        if name in ANUDATTA and "7.2.10" in on:
            path.append("no iṭ (7.2.10)")
        else:
            it = ["i"]; path.append("iṭ before the val-initial sīyuṭ (7.2.35)")
    if up == "jha" and "3.4.105" in on:
        aff = ["r", "a", "n"]; path.append("jha → ran (3.4.105 jhasya ran)")
    if up == "iṭ" and "3.4.106" in on:
        aff = ["a"]; path.append("iṭ → a (3.4.106 iṭo 't)")
    sut = []
    k_t = next((i for i, x in enumerate(aff) if x in ("t", "th")), None)
    if siy and k_t is not None and "3.4.107" in on:
        sut = ["s"]; path.append("suṭ before the t of the ending (3.4.107 suṭ tithoḥ)")
    if siy and "6.1.66" in on and siy[-1] == "y" and ((k_t == 0 and sut) or (aff and aff[0] not in VOWELS)):
        siy = siy[:-1]; path.append("y of sīy dropped before the val (6.1.66 lopo vyor vali)")
    if not it and st[-1] == "bh" and siy and "8.4.55" in on:
        st[-1] = "p"; path.append("bh → p before the khar s (8.4.55 khari ca)")
    stem = st + it + siy
    if siy and "8.3.59" in on:
        if it:
            stem[len(st) + 1] = "ṣ"; path.append("s of sīy → ṣ after the iṭ (8.3.59)")
        if sut:
            sut = ["ṣ"]; (path.append("suṭ s → ṣ after ī (8.3.59)") if k_t == 0 else None)
            if k_t == 0 and "8.4.41" in on:
                aff[0] = {"t": "ṭ", "th": "ṭh"}[aff[0]]; path.append("t → ṭ after ṣ (8.4.41 ṣṭunā ṣṭuḥ)")
            if k_t != 0:
                sut = ["s"]; path.append("suṭ s after ā stays s (8.3.59 needs iṇ / ku before it)")
    w = stem + (aff[:k_t] + sut + aff[k_t:] if sut else aff)
    return "".join(w), path


def paradigm(name, stages=ALL_STAGES):
    return {c: asirlin(name, c, up, stages)[0] for c, up in CELLS}


def t1_asirlin():
    forms = {r: paradigm(r) for r in ROOTS}
    L = lambda cs: {f"labh.{c}" for c in cs}; E = lambda cs: {f"edh.{c}" for c in cs}
    allc = [c for c, _ in CELLS]
    exp_breaks = {"3.4.102": L(allc) | E(allc), "3.4.107": L(["3s", "3d"]) | E(["3s", "3d"]), "3.4.105": L(["3p"]) | E(["3p"]), "3.4.106": L(["1s"]) | E(["1s"]),
                  "6.1.66": L(["3s", "3p"]) | E(["3s", "3p"]), "7.2.35": E(allc), "7.2.10": L(allc), "8.4.55": L(allc), "8.3.59": E(allc) | L(["3s"]), "8.4.41": L(["3s"]) | E(["3s"])}
    broken = {s: sorted(f"{r}.{c}" for r in ROOTS for c, _ in CELLS if paradigm(r, tuple(x for x in ALL_STAGES if x != s))[c] != ORACLE[r][c]) for s in exp_breaks}
    checks = {"eight_benedictive_atmanepada_forms_equal_oracle": all(forms[r][c] == ORACLE[r][c] for r in ROOTS for c, _ in CELLS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {r: asirlin(r, "3s", "ta")[1] for r in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_asirlin": t1_asirlin()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_ASIRLIN_ATMANEPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_ASIRLIN_ATMANEPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.asirlin_atmanepada_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": ["labh and edh in the benedictive ātmanepada 3s / 3d / 3p / 1s (8 forms) by 3.4.102 sīyuṭ with 3.4.107, 3.4.105, 3.4.106, 6.1.66, 7.2.35 / 7.2.10, 8.4.55, 8.3.59, 8.4.41; each rule breaks exactly the cells stated"],
            "NOT_claimed": ["3.4.104's kit is surface-neutral on labh / edh (no final ik) — recorded; the anudātta status of labh declared; the 2nd persons and the duals / plurals of 1st and 2nd; ik-final roots in the ātmanepada benedictive", "RH, YM untouched"],
        },
        "checks": checks, **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=None); args = parser.parse_args()
    payload = build_certificate(); data = canonical_bytes(payload)
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
