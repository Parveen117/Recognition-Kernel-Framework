from __future__ import annotations

"""Exact certificate (theorum/116): ĀTMANEPADA luṅ COMPILED — labh (aniṭ) and edh
(seṭ, vowel-initial) in luṅ, six cells each: sic (3.1.44), aṭ / āṭ (6.4.71 /
6.4.72 with 6.1.90 → ai-), the iṭ decision 7.2.35 / 7.2.10, 8.2.26 jhalo jhali
(sic deleted in alabdha, alabdhāḥ), 8.2.40 + 8.4.53 (labdha), 8.4.55 (alapsātām),
8.3.59 + 8.4.41 (aidhiṣṭa), 7.1.5 ātmanepadeṣv anataḥ (alapsata, aidhiṣata);
each rule shown load-bearing on exactly its cells.

Quoted sūtras:
 3.1.43   cli luṅi ; 3.1.44 cleḥ sic ; 3.4.114 ; 1.3.12 (ātmanepada)
 6.4.71   luṅlaṅlṛṅkṣv aḍ udāttaḥ ; 6.4.72 āḍ ajādīnām ; 6.1.90 āṭaś ca (ā + e → ai)
 7.2.35   ārdhadhātukasyeḍ valādeḥ ; 7.2.10 ekāca upadeśe 'nudāttāt
 8.2.26   jhalo jhali (sic dropped between jhal and jhal) ; 8.2.40 jhaṣas tathor dho 'dhaḥ ; 8.4.53 jhalāṁ jaś jhaśi ; 8.4.55 khari ca
 8.3.59   ādeśapratyayayoḥ ; 8.4.41 ṣṭunā ṣṭuḥ
 7.1.3    jho 'ntaḥ ; 7.1.5 ātmanepadeṣv anataḥ (jh → at after a non-a stem) ; 3.4.78 ; 8.2.66 ; 8.3.15

 T1  alabdha, alapsātām, alapsata, alapsi, alabdhāḥ, alapsmahi ; aidhiṣṭa, aidhiṣātām, aidhiṣata, aidhiṣi, aidhiṣṭhāḥ, aidhiṣmahi.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its, placement

SOURCES = {
    "3.1.43": "cli luṅi", "3.1.44": "cleḥ sic", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "1.3.12": "anudāttaṅita ātmanepadam",
    "6.4.71": "luṅlaṅlṛṅkṣv aḍ udāttaḥ", "6.4.72": "āḍ ajādīnām", "6.1.90": "āṭaś ca", "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.10": "ekāca upadeśe 'nudāttāt",
    "8.2.26": "jhalo jhali", "8.2.40": "jhaṣas tathor dho 'dhaḥ", "8.4.53": "jhalāṁ jaś jhaśi", "8.4.55": "khari ca", "8.3.59": "ādeśapratyayayoḥ", "8.4.41": "ṣṭunā ṣṭuḥ",
    "7.1.3": "jho 'ntaḥ", "7.1.5": "ātmanepadeṣv anataḥ", "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
JHAL = {"k", "kh", "g", "gh", "c", "ch", "j", "jh", "ṭ", "ṭh", "ḍ", "ḍh", "t", "th", "d", "dh", "p", "ph", "b", "bh", "ś", "ṣ", "s", "h"}
ROOTS = {"labh": ("l", "a", "bh"), "edh": ("e", "dh")}
ANUDATTA = {"labh"}
CELLS = [("3s", "ta"), ("3d", "ātām"), ("3p", "jha"), ("1s", "iṭ"), ("2s", "thās"), ("1p", "mahiṅ")]
ORACLE = {"labh": {"3s": "alabdha", "3d": "alapsātām", "3p": "alapsata", "1s": "alapsi", "2s": "alabdhāḥ", "1p": "alapsmahi"},
          "edh": {"3s": "aidhiṣṭa", "3d": "aidhiṣātām", "3p": "aidhiṣata", "1s": "aidhiṣi", "2s": "aidhiṣṭhāḥ", "1p": "aidhiṣmahi"}}
ALL_STAGES = ("3.1.44", "6.4.71", "6.4.72", "6.1.90", "7.2.35", "7.2.10", "8.2.26", "8.2.40", "8.4.53", "8.4.55", "8.3.59", "8.4.41", "7.1.3", "7.1.5", "8.2.66", "8.3.15")


def lun(name, code, up, stages=ALL_STAGES):
    on = set(stages)
    st = list(ROOTS[name]); path = [f"{name} + luṅ; ātmanepada (1.3.12)"]
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    sic = ["s"] if "3.1.44" in on else []
    if sic:
        path.append("cli → sic (3.1.43, 3.1.44; c it 1.3.7 → s; ārdhadhātuka 3.4.114)")
    it = []
    if sic and "7.2.35" in on:
        if name in ANUDATTA and "7.2.10" in on:
            path.append("no iṭ (7.2.10)")
        else:
            it = ["i"]; path.append("iṭ before the val-initial sic (7.2.35)")
    # augment
    aug = []
    if st[0] in VOWELS:
        if "6.4.72" in on:
            assert placement("āṭ") == "before"
            aug = ["ā"]; path.append("āṭ before the vowel-initial aṅga (6.4.72 āḍ ajādīnām; 1.1.46)")
            if "6.1.90" in on and st[0] == "e":
                aug, st = [], ["ai"] + st[1:]; path.append("ā + e → ai (6.1.90 āṭaś ca; vṛddhi 6.1.88)")
    elif "6.4.71" in on:
        aug = ["a"]; path.append("aṭ before the aṅga (6.4.71)")
    # endings
    if up == "jha":
        if "7.1.5" in on:
            aff = ["a", "t", "a"]; path.append("jh → at after the non-a stem (7.1.5 ātmanepadeṣv anataḥ)")
        elif "7.1.3" in on:
            aff = ["a", "n", "t", "a"]; path.append("jh → ant (7.1.3)")
    stem = st + it + sic
    # 8.2.26: sic between jhal and jhal dropped
    if sic and not it and st[-1] in JHAL and aff and aff[0] in JHAL and "8.2.26" in on:
        stem = st; path.append("sic dropped between jhal and jhal (8.2.26 jhalo jhali)")
        if st[-1] == "bh" and aff[0] == "th" and "8.2.40" in on:
            aff[0] = "dh"; path.append("th → dh after the jhaṣ (8.2.40)")
        elif st[-1] == "bh" and aff[0] == "t" and "8.2.40" in on:
            aff[0] = "dh"; path.append("t → dh after the jhaṣ (8.2.40 jhaṣas tathor dho 'dhaḥ)")
        if st[-1] == "bh" and aff[0] == "dh" and "8.4.53" in on:
            stem[-1] = "b"; path.append("bh → b before the jhaś (8.4.53)")
    elif sic and not it and st[-1] == "bh" and "8.4.55" in on:
        stem[len(st) - 1] = "p"; path.append("bh → p before the khar s (8.4.55 khari ca)")
    if it and sic and "8.3.59" in on:
        stem[-1] = "ṣ"; path.append("s → ṣ after the iṭ (8.3.59)")
        if aff and aff[0] in ("t", "th") and "8.4.41" in on:
            aff[0] = {"t": "ṭ", "th": "ṭh"}[aff[0]]; path.append("t / th → ṭ / ṭh after ṣ (8.4.41 ṣṭunā ṣṭuḥ)")
    w = aug + stem + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(name, stages=ALL_STAGES):
    return {c: lun(name, c, up, stages)[0] for c, up in CELLS}


def t1_lun():
    forms = {r: paradigm(r) for r in ROOTS}
    L = lambda cs: {f"labh.{c}" for c in cs}; E = lambda cs: {f"edh.{c}" for c in cs}
    allcells = [c for c, _ in CELLS]
    exp_breaks = {"3.1.44": L(allcells) | E(allcells), "6.4.71": L(allcells), "6.4.72": E(allcells), "6.1.90": E(allcells), "7.2.35": E(allcells), "7.2.10": L(allcells),
                  "8.2.26": L(["3s", "2s"]), "8.2.40": L(["3s", "2s"]), "8.4.53": L(["3s", "2s"]), "8.4.55": L(["3d", "3p", "1s", "1p"]),
                  "8.3.59": E(allcells), "8.4.41": E(["3s", "2s"]), "7.1.3": set(), "7.1.5": L(["3p"]) | E(["3p"]), "8.2.66": L(["2s"]) | E(["2s"]), "8.3.15": L(["2s"]) | E(["2s"])}
    broken = {s: sorted(f"{r}.{c}" for r in ROOTS for c, _ in CELLS if paradigm(r, tuple(x for x in ALL_STAGES if x != s))[c] != ORACLE[r][c]) for s in exp_breaks}
    checks = {"twelve_lun_atmanepada_forms_equal_oracle": all(forms[r][c] == ORACLE[r][c] for r in ROOTS for c, _ in CELLS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {r: lun(r, "3s", "ta")[1] for r in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lun": t1_lun()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_ATMANEPADA_LUN_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_ATMANEPADA_LUN_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.atmanepada_lun_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": ["labh and edh in luṅ ātmanepada, six cells each (12 forms), by 3.1.44 with 6.4.71 / 6.4.72 + 6.1.90, 7.2.35 / 7.2.10, 8.2.26, 8.2.40 + 8.4.53, 8.4.55, 8.3.59 + 8.4.41, 7.1.5, 8.2.66 / 8.3.15; each rule breaks exactly the cells stated; 7.1.3 is overridden by 7.1.5 on both roots (ablation set empty, recorded)"],
            "NOT_claimed": ["the anudātta status of labh declared; the 2d / 2p / 1d cells; roots taking kṣa (3.1.45), aṅ, ciṇ (3.1.60–66) or the sic-luk; parasmaipada luṅ is theorum/101", "RH, YM untouched"],
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
