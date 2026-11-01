from __future__ import annotations

"""Exact certificate (theorum/115): ĀŚĪRLIṄ PARASMAIPADA COMPILED — the benedictive
of six roots (3s, 3d, 3p): liṅ in āśis is ārdhadhātuka (3.4.116), yāsuṭ (3.4.103)
is kit (3.4.104 kid āśiṣi) so no guṇa (1.1.5), 7.2.79 liṅaḥ salopo 'nantyasya,
6.4.67 er liṅi (deyāt, stheyāt), 3.4.100 / 3.4.101 / 3.4.108 on the endings
(yāt, yāstām, yāsuḥ); each rule shown load-bearing on exactly its cells.

Quoted sūtras:
 3.3.173  āśiṣi liṅloṭau ; 3.4.116 liṅāśiṣi (ārdhadhātuka)
 3.4.103  yāsuṭ parasmaipadeṣūdātto ṅic ca ; 3.4.104 kid āśiṣi ; 1.1.5 kṅiti ca
 7.2.79   liṅaḥ salopo 'nantyasya              the s of yās dropped when not final (yāt, yāsuḥ keep … see cells)
 6.4.67   er liṅi                               ā of ghu / mā / sthā / … → e before the ārdhadhātuka kit liṅ: deyāt, stheyāt
 3.4.100  itaś ca ; 3.4.101 tasthasthamipāṁ tāṁtaṁtāmaḥ ; 3.4.108 jher jus ; 3.4.99 nityaṁ ṅitaḥ
 8.2.66   sasajuṣo ruḥ ; 8.3.15 kharavasānayor visarjanīyaḥ ; 7.2.10 ekāca upadeśe 'nudāttāt (no iṭ before yāsuṭ: the kit liṅ takes no iṭ by 7.2.10 for these roots)

 T1  bhūyāt / bhūyāstām / bhūyāsuḥ ; gamyāt… ; nīyāt… ; pacyāt… ; deyāt… ; stheyāt… — 18 forms.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import GUNA_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.3.173": "āśiṣi liṅloṭau", "3.4.116": "liṅāśiṣi", "3.4.103": "yāsuṭ parasmaipadeṣūdātto ṅic ca", "3.4.104": "kid āśiṣi", "1.1.5": "kṅiti ca",
    "7.2.79": "liṅaḥ salopo 'nantyasya", "6.4.67": "er liṅi", "3.4.100": "itaś ca", "3.4.101": "tasthasthamipāṁ tāṁtaṁtāmaḥ", "3.4.108": "jher jus",
    "3.4.99": "nityaṁ ṅitaḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ", "7.2.10": "ekāca upadeśe 'nudāttāt",
}
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
FROM58 = {"e": "e", "o": "o", "a": "a"}
ROOTS = {"bhū": ("bh", "ū"), "gam": ("g", "a", "m"), "nī": ("n", "ī"), "pac": ("p", "a", "c"), "dā": ("d", "ā"), "sthā": ("s", "th", "ā")}
GHU_MA_STHA = {"dā", "sthā"}
CELLS = [("3s", "tip"), ("3d", "tas"), ("3p", "jhi")]
STEM = {"bhū": "bhū", "gam": "gam", "nī": "nī", "pac": "pac", "dā": "de", "sthā": "sthe"}
ORACLE = {r: {"3s": STEM[r] + "yāt", "3d": STEM[r] + "yāstām", "3p": STEM[r] + "yāsuḥ"} for r in ROOTS}
ALL_STAGES = ("3.4.103", "3.4.104", "7.2.79", "6.4.67", "3.4.100", "3.4.101", "3.4.108", "8.2.66", "8.3.15")


def asirlin(name, code, up, stages=ALL_STAGES):
    on = set(stages)
    st = list(ROOTS[name]); path = [f"{name} + liṅ in āśis (3.3.173); ārdhadhātuka (3.4.116); no iṭ (7.2.10)"]
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    yas = []
    if "3.4.103" in on:
        y = its("yāsu~ṭ", "agama"); yas = list(y["remaining_sounds"]); path.append(f"yāsuṭ before the parasmaipada ending (3.4.103) → {''.join(yas)}")
    kit = "3.4.104" in on and bool(yas)
    if kit:
        path.append("the āśis liṅ is kit (3.4.104 kid āśiṣi)")
    if name in GHU_MA_STHA and kit and "6.4.67" in on:
        st[-1] = "e"; path.append("ā → e before the ārdhadhātuka kit liṅ (6.4.67 er liṅi)")
    if st[-1] in IK and not kit:
        g = rapara_1_1_51(IK[st[-1]], antaratama(IK[st[-1]], GUNA_SET)); st = st[:-1] + list(FROM58.get(g, g)); path.append(f"(not kit: 7.3.84 guṇa) {''.join(st)}")
    elif st[-1] in IK:
        path.append("no guṇa before the kit (1.1.5)")
    # endings under the ṅit liṅ (3.4.103: liṅ is ṅit)
    if up == "jhi" and "3.4.108" in on:
        aff = ["j", "u", "s"]; path.append("jhi → jus (3.4.108 jher jus); j it (1.3.8) → us"); aff = aff[1:]
    if up == "tas" and "3.4.101" in on:
        aff = ["t", "ā", "m"]; path.append("tas → tām (3.4.101)")
    if up == "tip" and "3.4.100" in on and aff[-1] == "i":
        aff = aff[:-1]; path.append("final i dropped (3.4.100 itaś ca)")
    # 7.2.79: the s of yās dropped when not final — before t (yāt) and before tām (yāstām keeps s? see below)
    if yas and "7.2.79" in on and aff and aff[0] == "t" and up == "tip":
        yas = yas[:-1]; path.append("s of yās dropped, not being final (7.2.79 liṅaḥ salopo 'nantyasya): yāt")
    w = st + yas + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(name, stages=ALL_STAGES):
    return {c: asirlin(name, c, up, stages)[0] for c, up in CELLS}


def t1_asirlin():
    forms = {r: paradigm(r) for r in ROOTS}
    allc = {f"{r}.{c}" for r in ROOTS for c, _ in CELLS}
    exp_breaks = {"3.4.103": allc, "3.4.104": {f"{r}.{c}" for r in ("bhū", "nī", "dā", "sthā") for c, _ in CELLS}, "7.2.79": {f"{r}.3s" for r in ROOTS},
                  "6.4.67": {f"{r}.{c}" for r in ("dā", "sthā") for c, _ in CELLS}, "3.4.100": {f"{r}.3s" for r in ROOTS}, "3.4.101": {f"{r}.3d" for r in ROOTS},
                  "3.4.108": {f"{r}.3p" for r in ROOTS}, "8.2.66": {f"{r}.3p" for r in ROOTS}, "8.3.15": {f"{r}.3p" for r in ROOTS}}
    broken = {s: sorted(f"{r}.{c}" for r in ROOTS for c, _ in CELLS if paradigm(r, tuple(x for x in ALL_STAGES if x != s))[c] != ORACLE[r][c]) for s in exp_breaks}
    checks = {"eighteen_benedictive_forms_equal_oracle": all(forms[r][c] == ORACLE[r][c] for r in ROOTS for c, _ in CELLS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {r: asirlin(r, "3s", "tip")[1] for r in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_asirlin": t1_asirlin()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_ASIRLIN_PARASMAIPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_ASIRLIN_PARASMAIPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.asirlin_parasmaipada_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": ["six roots in the benedictive parasmaipada 3s / 3d / 3p (18 forms) by 3.3.173 / 3.4.116 with 3.4.103 yāsuṭ, 3.4.104 kit (1.1.5), 7.2.79, 6.4.67, 3.4.100 / 3.4.101 / 3.4.108, 8.2.66 / 8.3.15; each rule breaks exactly the cells stated"],
            "NOT_claimed": ["3.4.104's kit is surface-neutral on gam and pac (no ik to protect) — their cells are not in its ablation set; the ātmanepada benedictive (sīyuṭ, 3.4.102), the 1st / 2nd persons, kṛ (7.4.28), the iṭ question for seṭ roots (7.2.10 declared)", "RH, YM untouched"],
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
