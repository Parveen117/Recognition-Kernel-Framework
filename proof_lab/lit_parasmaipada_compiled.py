from __future__ import annotations

"""Exact certificate (theorum/102): LIṬ (THE PERFECT) PARASMAIPADA COMPILED WITH
REDUPLICATION — bhū, gam, kṛ, nī in the option-free cells (3s, 3d, 3p, 1d, 1p);
the abhyāsa by 6.1.1–8 and 7.4.59–73, the kit / pit split of 1.2.5 deciding
vṛddhi (7.2.115 / 7.2.116) against upadhā-lopa (6.4.98) and no-guṇa (1.1.5).

Quoted sūtras:
 3.2.115  parokṣe liṭ                           3.4.82 parasmaipadānāṁ ṇalatususthalathusaṇalvamāḥ
 1.2.5    asaṁyogāl liṭ kit                     the apit liṭ endings are kit after a root not ending in a cluster
 6.1.8    liṭi dhātor anabhyāsasya               6.1.1 ekāco dve prathamasya ; 6.1.4 pūrvo 'bhyāsaḥ
 7.4.59   hrasvaḥ ; 7.4.60 halādiḥ śeṣaḥ ; 7.4.62 kuhoś cuḥ ; 7.4.66 ur at ; 7.4.73 bhavater aḥ ; 8.4.54 abhyāse car ca     the abhyāsa
 6.4.88   bhuvo vug luṅliṭoḥ                     babhūva
 7.2.115  aco ñṇiti ; 7.2.116 ata upadhāyāḥ      vṛddhi before ṇal (ṇit): cakāra, nināya, jagāma
 6.4.98   gamahanajanakhanaghasāṁ lopaḥ kṅity anaṅi    jagmatuḥ
 7.2.13   kṛsṛbhṛvṛstudrusruśruvo liṭi            no iṭ for kṛ (cakṛva) ; 7.2.35 iṭ for the others (babhūviva, jagmiva, ninyiva)
 1.1.5    kṅiti ca ; 6.1.77 iko yaṇ aci ; 6.1.78 eco 'yavāyāvaḥ ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  babhūva babhūvatuḥ babhūvuḥ babhūviva babhūvima ; jagāma jagmatuḥ jagmuḥ
     jagmiva jagmima ; cakāra cakratuḥ cakruḥ cakṛva cakṛma ; nināya ninyatuḥ
     ninyuḥ ninyiva ninyima — 20 forms; each stage breaks exactly its cells
     on exactly its roots (7.4.62 gam / kṛ, 7.4.66 kṛ, 7.4.73 bhū, 6.4.88 bhū,
     7.2.116 gam, 7.2.115 kṛ / nī, 6.4.98 gam, 7.2.13 kṛ, 1.2.5 the kit cells).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import BASE, VRDDHI_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.2.115": "parokṣe liṭ", "3.4.82": "parasmaipadānāṁ ṇalatususthalathusaṇalvamāḥ", "1.2.5": "asaṁyogāl liṭ kit", "6.1.8": "liṭi dhātor anabhyāsasya",
    "6.1.1": "ekāco dve prathamasya", "6.1.4": "pūrvo 'bhyāsaḥ", "7.4.59": "hrasvaḥ", "7.4.60": "halādiḥ śeṣaḥ", "7.4.62": "kuhoś cuḥ", "7.4.66": "ur at", "7.4.73": "bhavater aḥ", "8.4.54": "abhyāse car ca",
    "6.4.88": "bhuvo vug luṅliṭoḥ", "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "6.4.98": "gamahanajanakhanaghasāṁ lopaḥ kṅity anaṅi", "7.2.13": "kṛsṛbhṛvṛstudrusruśruvo liṭi",
    "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "1.1.5": "kṅiti ca", "6.1.77": "iko yaṇ aci", "6.1.78": "eco 'yavāyāvaḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
CELLS = [("3s", "tip", ("a",), "ṇal", True), ("3d", "tas", ("a", "t", "u", "s"), "atus", False), ("3p", "jhi", ("u", "s"), "us", False), ("1d", "vas", ("v", "a"), "va", False), ("1p", "mas", ("m", "a"), "ma", False)]   # (cell, tiṅ, substitute sounds, name, pit)
ROOTS = {"bhū": "bhū", "gam": "gamḷ~", "kṛ": "ḍukṛñ", "nī": "ṇīñ"}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
SHORT = {"ā": "a", "ī": "i", "ū": "u", "ṝ": "ṛ", "e": "i", "ai": "i", "o": "u", "au": "u"}
CU = {"k": "c", "kh": "ch", "g": "j", "gh": "jh", "ṅ": "ñ", "h": "j"}
CAR = {"bh": "b", "ph": "p", "dh": "d", "th": "t", "gh": "g", "kh": "k", "jh": "j", "ch": "c", "ḍh": "ḍ", "ṭh": "ṭ"}   # 8.4.54 abhyāse car ca: aspirate → unaspirate in the abhyāsa
V58 = {"A": ("ā",), "ai": ("ai",), "au": ("au",), "Ar": ("ā", "r"), "Al": ("ā", "l")}
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
YAN = {"i": "y", "ī": "y", "u": "v", "ū": "v", "ṛ": "r"}
AYADI = {"ai": ("ā", "y"), "au": ("ā", "v"), "e": ("a", "y"), "o": ("a", "v")}
NO_IT_LIT = {"kṛ"}      # 7.2.13
GAM_LIST = {"gam"}      # 6.4.98
ORACLE = {"bhū": {"3s": "babhūva", "3d": "babhūvatuḥ", "3p": "babhūvuḥ", "1d": "babhūviva", "1p": "babhūvima"},
          "gam": {"3s": "jagāma", "3d": "jagmatuḥ", "3p": "jagmuḥ", "1d": "jagmiva", "1p": "jagmima"},
          "kṛ": {"3s": "cakāra", "3d": "cakratuḥ", "3p": "cakruḥ", "1d": "cakṛva", "1p": "cakṛma"},
          "nī": {"3s": "nināya", "3d": "ninyatuḥ", "3p": "ninyuḥ", "1d": "ninyiva", "1p": "ninyima"}}
ALL_STAGES = ("6.1.8", "7.4.59", "7.4.60", "7.4.62", "7.4.66", "7.4.73", "8.4.54", "1.2.5", "7.2.35", "7.2.13", "6.4.88", "7.2.115", "7.2.116", "6.4.98", "1.1.5", "6.1.77", "6.1.78", "8.2.66", "8.3.15")


def root_sounds(name):
    s = list(its(ROOTS[name], "dhatu")["remaining_sounds"])
    if s[0] == "ṇ":
        s[0] = "n"
    return s


def abhyasa(root: list[str], path: list[str], on: set) -> list[str]:
    if "6.1.8" not in on:
        return []
    k = next(i for i, s in enumerate(root) if s in VOWELS)
    ab = root[: k + 1]                                           # 6.1.1 ekāco dve prathamasya: the first vowel-syllable (with its consonants)
    path.append(f"reduplication of the first ekāc (6.1.8, 6.1.1): abhyāsa {''.join(ab)} (6.1.4 pūrvo 'bhyāsaḥ)")
    if "7.4.60" in on and k > 0:
        ab = [root[0], root[k]]; path.append("only the first consonant kept (7.4.60 halādiḥ śeṣaḥ)")
    if "7.4.59" in on and ab[-1] in SHORT:
        ab[-1] = SHORT[ab[-1]]; path.append("abhyāsa vowel shortened (7.4.59 hrasvaḥ)")
    if "7.4.66" in on and ab[-1] == "ṛ":
        ab[-1] = "a"; path.append("ṛ → a in the abhyāsa (7.4.66 ur at)")
    if "7.4.73" in on and root == ["bh", "ū"] and ab[-1] == "u":
        ab[-1] = "a"; path.append("u → a in bhū's abhyāsa (7.4.73 bhavater aḥ)")
    if "7.4.62" in on and ab[0] in CU:
        ab[0] = CU[ab[0]]; path.append(f"ku / h → cu in the abhyāsa (7.4.62): {''.join(ab)}")
    if "8.4.54" in on and ab[0] in CAR:
        ab[0] = CAR[ab[0]]; path.append(f"aspirate → unaspirate in the abhyāsa (8.4.54 abhyāse car ca): {''.join(ab)}")
    return ab


def lit(name: str, cell: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    root = root_sounds(name)
    c, ting, subst, sname, pit = next(x for x in CELLS if x[0] == cell)
    aff = list(subst)
    path = [f"{ROOTS[name]} → {''.join(root)}; {ting} → {sname} (3.4.82)" + (" pit, ṇit" if pit else "")]
    kit = (not pit) and "1.2.5" in on
    if kit:
        path.append("apit liṭ ending is kit after a non-cluster root (1.2.5)")
    ab = abhyasa(list(root), path, on)
    st = list(root)
    it: list[str] = []
    if sname in ("va", "ma") and "7.2.35" in on:
        if name in NO_IT_LIT and "7.2.13" in on:
            path.append("no iṭ before va / ma of liṭ for kṛ (7.2.13)")
        else:
            it = ["i"]; path.append("iṭ before the val-initial va / ma (7.2.35)")
    if name == "bhū" and "6.4.88" in on and (aff[0] in VOWELS or it):
        st = st + ["v"]; path.append("vuk before the vowel-initial liṭ ending (6.4.88)")
    elif pit:
        if "7.2.115" in on and st[-1] in IK:
            v = rapara_1_1_51(BASE[IK[st[-1]]], antaratama(IK[st[-1]], VRDDHI_SET))
            st = st[:-1] + list(V58[v]); path.append(f"vṛddhi of the ik-final before the ṇit ṇal (7.2.115; 1.1.50 / 1.1.51) → {''.join(st)}")
            if "6.1.78" in on and st[-1] in AYADI:
                st = st[:-1] + list(AYADI[st[-1]]); path.append("ayādi before the vowel (6.1.78)")
        elif "7.2.116" in on and len(st) >= 2 and st[-2] == "a" and st[-1] not in VOWELS:
            st[-2] = "ā"; path.append("vṛddhi of the penultimate a before the ṇit ṇal (7.2.116)")
    else:
        if kit and name in GAM_LIST and "6.4.98" in on:
            st = [x for i, x in enumerate(st) if i != len(st) - 2]; path.append("upadhā dropped before the kit ending (6.4.98)")
        if kit and st[-1] in IK and "1.1.5" in on:
            path.append("no guṇa before the kit ending (1.1.5)")
        if "6.1.77" in on and st[-1] in YAN and (aff[0] in VOWELS or it):
            st = st[:-1] + [YAN[st[-1]]]; path.append(f"ik → yaṇ before the vowel (6.1.77): {''.join(st)}")
    w = ab + st + it + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(name, stages=ALL_STAGES):
    return {c: lit(name, c, stages)[0] for c, *_ in CELLS}


def t1_lit() -> dict[str, Any]:
    forms = {r: paradigm(r) for r in ROOTS}
    exp = {"6.1.8": {(r, c) for r in ROOTS for c in ORACLE[r]}, "7.4.60": set(),   # no cluster-initial root here: 7.4.60 is not load-bearing on these four (recorded)
           "8.4.54": {("bhū", c) for c in ORACLE["bhū"]}, "7.4.59": {("bhū", c) for c in ORACLE["bhū"]} | {("nī", c) for c in ORACLE["nī"]},
           "7.4.62": {("gam", c) for c in ORACLE["gam"]} | {("kṛ", c) for c in ORACLE["kṛ"]}, "7.4.66": {("kṛ", c) for c in ORACLE["kṛ"]}, "7.4.73": {("bhū", c) for c in ORACLE["bhū"]},
           "6.4.88": {("bhū", c) for c in ORACLE["bhū"]}, "7.2.115": {("kṛ", "3s"), ("nī", "3s")}, "7.2.116": {("gam", "3s")}, "6.4.98": {("gam", c) for c in ("3d", "3p", "1d", "1p")},
           "7.2.13": {("kṛ", "1d"), ("kṛ", "1p")}, "7.2.35": {(r, c) for r in ("bhū", "gam", "nī") for c in ("1d", "1p")}, "1.2.5": {("gam", c) for c in ("3d", "3p", "1d", "1p")}, "6.1.77": {("kṛ", c) for c in ("3d", "3p")} | {("nī", c) for c in ("3d", "3p", "1d", "1p")}}
    broken = {}
    for s in exp:
        broken[s] = sorted(f"{r}:{c}" for r in ROOTS for c in ORACLE[r] if lit(r, c, tuple(x for x in ALL_STAGES if x != s))[0] != ORACLE[r][c])
    checks = {"lit_20_forms_equal_the_classical_forms": forms == ORACLE}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_forms_break": set(broken[s]) == {f"{r}:{c}" for r, c in v} for s, v in exp.items()})
    return {"checks": checks, "forms": forms, "paths": {f"{r}:{c}": lit(r, c)[1] for r in ROOTS for c in ORACLE[r]}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lit": t1_lit()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_LIT_PARASMAIPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_LIT_PARASMAIPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.lit_parasmaipada_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "liṭ parasmaipada of bhū, gam, kṛ, nī in 3s, 3d, 3p, 1d, 1p (20 forms) with the abhyāsa by 6.1.1 / 6.1.4 / 6.1.8 and 7.4.59 / 60 / 62 / 66 / 73, 1.2.5 kit, 7.2.115 / 7.2.116 vṛddhi, 6.4.98, 6.4.88, 7.2.13 / 7.2.35; each stage breaks exactly the forms stated",
            ],
            "NOT_claimed": ["the option cells 2s / 2d / 2p / 1s (thal with 7.2.61–63, 7.1.91 ṇal uttamo vā), ātmanepada liṭ, periphrastic liṭ (3.1.35 ām), roots with clusters or vowel-initial roots (6.1.2, 7.4.69), 7.4.70 ata ādeḥ, accent", "stage order a declared pipeline", "RH, YM untouched"],
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
