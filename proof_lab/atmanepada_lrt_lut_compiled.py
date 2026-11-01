from __future__ import annotations

"""Exact certificate (theorum/112): ĀTMANEPADA lṛṭ AND luṭ COMPILED — labh (aniṭ)
and edh (seṭ), theorum/66's roots, in the two futures: sya / tās (3.1.33), the
iṭ decision 7.2.35 / 7.2.10, 8.4.55 (lapsyate) and 8.2.40 + 8.4.53 (labdhā),
8.3.59, the ṭit endings 3.4.79 / 3.4.80, 7.2.81's chain on ātām (theorum/66),
2.4.85 with 6.4.143 / 7.4.51 (luṭ 3rd person), 7.4.52 ha eti (labdhāhe), 7.3.101;
each rule shown load-bearing on exactly its cells.

Quoted sūtras:
 3.1.33   syatāsī lṛluṭoḥ ; 3.4.114 ārdhadhātukaṁ śeṣaḥ ; 1.3.12 anudāttaṅita ātmanepadam (labh, edh)
 7.2.35   ārdhadhātukasyeḍ valādeḥ ; 7.2.10 ekāca upadeśe 'nudāttāt (labh: no iṭ)
 8.4.55   khari ca (bh + s → ps) ; 8.2.40 jhaṣas tathor dho 'dhaḥ ; 8.4.53 jhalāṁ jaś jhaśi (labh + tās → labdhā)
 8.3.59   ādeśapratyayayoḥ (edhiṣyate)
 3.4.78   ; 3.4.79 ṭita ātmanepadānāṁ ṭer e ; 3.4.80 thāsaḥ se ; 7.1.3 jho 'ntaḥ ; 7.2.81 āto ṅitaḥ ; 6.1.66 lopo vyor vali ; 6.1.97 ato guṇe ; 7.3.101 ato dīrgho yañi
 2.4.85   luṭaḥ prathamasya ḍāraurasaḥ ; 6.4.143 ṭeḥ ; 7.4.51 ri ca ; 7.4.50 tāsastyor lopaḥ (labdhāse) ; 7.4.52 ha eti
 8.2.66   sasajuṣo ruḥ ; 8.3.15 kharavasānayor visarjanīyaḥ

 T1  lṛṭ: lapsyate … / edhiṣyate … (6 cells each) ; T2  luṭ: labdhā … / edhitā … (6 cells each).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.1.33": "syatāsī lṛluṭoḥ", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "1.3.12": "anudāttaṅita ātmanepadam", "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.10": "ekāca upadeśe 'nudāttāt",
    "8.4.55": "khari ca", "8.2.40": "jhaṣas tathor dho 'dhaḥ", "8.4.53": "jhalāṁ jaś jhaśi", "8.3.59": "ādeśapratyayayoḥ",
    "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "3.4.79": "ṭita ātmanepadānāṁ ṭer e", "3.4.80": "thāsaḥ se", "7.1.3": "jho 'ntaḥ",
    "7.2.81": "āto ṅitaḥ", "6.1.66": "lopo vyor vali", "6.1.97": "ato guṇe", "7.3.101": "ato dīrgho yañi",
    "2.4.85": "luṭaḥ prathamasya ḍāraurasaḥ", "6.4.143": "ṭeḥ", "7.4.51": "ri ca", "7.4.50": "tāsastyor lopaḥ", "7.4.52": "ha eti", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
ROOTS = {"labh": ("l", "a", "bh"), "edh": ("e", "dh")}
ANUDATTA = {"labh"}   # 7.2.10 (declared from the Dhātupāṭha accent: ḍulabhaṣ)
CELLS = [("3s", "ta"), ("3d", "ātām"), ("3p", "jha"), ("1s", "iṭ"), ("2s", "thās"), ("1p", "mahiṅ")]
ORACLE = {
    "lrt": {"labh": {"3s": "lapsyate", "3d": "lapsyete", "3p": "lapsyante", "1s": "lapsye", "2s": "lapsyase", "1p": "lapsyāmahe"},
            "edh": {"3s": "edhiṣyate", "3d": "edhiṣyete", "3p": "edhiṣyante", "1s": "edhiṣye", "2s": "edhiṣyase", "1p": "edhiṣyāmahe"}},
    "lut": {"labh": {"3s": "labdhā", "3d": "labdhārau", "3p": "labdhāraḥ", "1s": "labdhāhe", "2s": "labdhāse", "1p": "labdhāsmahe"},
            "edh": {"3s": "edhitā", "3d": "edhitārau", "3p": "edhitāraḥ", "1s": "edhitāhe", "2s": "edhitāse", "1p": "edhitāsmahe"}},
}
LRT_STAGES = ("3.1.33", "7.2.35", "7.2.10", "8.4.55", "8.3.59", "3.4.79", "3.4.80", "7.1.3", "7.2.81", "6.1.66", "6.1.97", "7.3.101")
LUT_STAGES = ("3.1.33", "7.2.35", "7.2.10", "8.2.40", "8.4.53", "3.4.79", "3.4.80", "2.4.85", "6.4.143", "7.4.51", "7.4.50", "7.4.52", "8.2.66", "8.3.15")


def _it(name, on, path):
    if "7.2.35" not in on:
        return []
    if name in ANUDATTA and "7.2.10" in on:
        path.append("no iṭ: the root is anudātta in the upadeśa (7.2.10)"); return []
    path.append("iṭ before the val-initial ārdhadhātuka (7.2.35)"); return ["i"]


def _ending(up, on, path):
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    if up == "jha" and "7.1.3" in on:
        aff = ["a", "n", "t"] + aff[1:]; path.append("jh → ant (7.1.3)")
    if up == "thās" and "3.4.80" in on:
        aff = ["s", "e"]; path.append("thās → se (3.4.80)")
    elif "3.4.79" in on and up != "thās":
        k = max(i for i, x in enumerate(aff) if x in VOWELS)
        aff = aff[:k] + ["e"]; path.append(f"ṭi of the ṭit ātmanepada ending → e (3.4.79; ṭi 1.1.64): {''.join(aff)}")
    return aff


def lrt(name, code, up, stages=LRT_STAGES):
    on = set(stages)
    st = list(ROOTS[name]); path = [f"{name} + lṛṭ; ātmanepada (1.3.12)"]
    vik = ["s", "y", "a"] if "3.1.33" in on else []
    if vik:
        path.append("sya before lṛṭ (3.1.33; ārdhadhātuka 3.4.114)")
    it = _it(name, on, path) if vik else []
    if not it and st[-1] == "bh" and vik and "8.4.55" in on:
        st[-1] = "p"; path.append("bh → p before the khar s (8.4.55 khari ca; 8.4.53 having given b)")
    stem = st + it + vik
    if it and vik and "8.3.59" in on:
        stem[len(st) + 1] = "ṣ"; path.append("s → ṣ after the iṭ (8.3.59)")
    aff = _ending(up, on, path)
    if up == "ātām" and stem[-1] == "a" and aff[0] == "ā" and "7.2.81" in on:
        aff = ["i", "y"] + aff[1:]; path.append("ā → iy after a (7.2.81 āto ṅitaḥ)")
        if "6.1.66" in on:
            aff = ["i"] + aff[2:]; path.append("y dropped before val (6.1.66)")
    if stem[-1] == "a" and aff and aff[0] in ("i", "e") and "6.1.97" in on:
        stem[-1] = "e"; aff = aff[1:]; path.append("a + i / e → e (6.1.97 ato guṇe)")
    if up == "mahiṅ" and stem[-1] == "a" and "7.3.101" in on:
        stem[-1] = "ā"; path.append("a → ā before the yañ-initial mahe (7.3.101)")
    if stem[-1] == "a" and aff and aff[0] == "a":
        aff = aff[1:]; path.append("a + a → a (6.1.97)")
    return "".join(stem + aff), path


def lut(name, code, up, stages=LUT_STAGES):
    on = set(stages)
    st = list(ROOTS[name]); path = [f"{name} + luṭ; ātmanepada (1.3.12)"]
    vik = ["t", "ā", "s"] if "3.1.33" in on else []
    if vik:
        path.append("tās before luṭ (3.1.33; ārdhadhātuka 3.4.114)")
    it = _it(name, on, path) if vik else []
    if not it and st[-1] == "bh" and vik:
        if "8.2.40" in on:
            vik[0] = "dh"; path.append("t of tās → dh after the jhaṣ bh (8.2.40 jhaṣas tathor dho 'dhaḥ)")
        if "8.4.53" in on:
            st[-1] = "b"; path.append("bh → b before the jhaś dh (8.4.53 jhalāṁ jaś jhaśi)")
    stem = st + it + vik
    aff = _ending(up, on, path)
    if up in ("ta", "ātām", "jha") and "2.4.85" in on:
        aff = {"ta": ["ḍ", "ā"], "ātām": ["r", "au"], "jha": ["r", "a", "s"]}[up]; path.append(f"{up} → {''.join(aff)} (2.4.85 luṭaḥ prathamasya ḍāraurasaḥ)")
        if up == "ta":
            if "6.4.143" in on:
                k = max(i for i, s in enumerate(stem) if s in VOWELS); stem = stem[:k]; path.append("ṭi of the aṅga dropped before the ḍit (6.4.143 ṭeḥ)")
            aff = aff[1:]; path.append("ḍ it (1.3.7)")
        elif "7.4.51" in on and stem[-1] == "s":
            stem = stem[:-1]; path.append("s of tās dropped before r (7.4.51 ri ca)")
    if up == "thās" and stem[-1] == "s" and aff and aff[0] == "s" and "7.4.50" in on:
        stem = stem[:-1]; path.append("s of tās dropped before the s-initial ending (7.4.50 tāsastyor lopaḥ)")
    if up == "iṭ" and stem[-1] == "s" and aff == ["e"] and "7.4.52" in on:
        stem[-1] = "h"; path.append("s of tās → h before e (7.4.52 ha eti)")
    w = stem + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(fn, name, stages):
    return {c: fn(name, c, up, stages)[0] for c, up in CELLS}


def _packet(key, fn, stages, exp_breaks):
    forms = {n: paradigm(fn, n, stages) for n in ROOTS}
    broken = {s: sorted(f"{n}.{c}" for n in ROOTS for c, _ in CELLS if paradigm(fn, n, tuple(x for x in stages if x != s))[c] != ORACLE[key][n][c]) for s in exp_breaks}
    checks = {f"{key}_twelve_cells_equal_oracle": all(forms[n][c] == ORACLE[key][n][c] for n in ROOTS for c, _ in CELLS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {n: fn(n, "3s", "ta", stages)[1] for n in ROOTS}, "broken": broken}


def t1_lrt():
    allc = {f"{n}.{c}" for n in ROOTS for c, _ in CELLS}
    labh = {f"labh.{c}" for c, _ in CELLS}; edh = {f"edh.{c}" for c, _ in CELLS}
    return _packet("lrt", lrt, LRT_STAGES, {"3.1.33": allc, "7.2.35": edh, "7.2.10": labh, "8.4.55": labh, "8.3.59": edh, "3.4.79": {x for x in allc if not x.endswith(".2s") and not x.endswith(".1s")},
                                            "3.4.80": {f"{n}.2s" for n in ROOTS}, "7.1.3": {f"{n}.3p" for n in ROOTS}, "7.2.81": {f"{n}.3d" for n in ROOTS}, "6.1.66": {f"{n}.3d" for n in ROOTS},
                                            "6.1.97": {f"{n}.{c}" for n in ROOTS for c in ("3d", "1s")}, "7.3.101": {f"{n}.1p" for n in ROOTS}})


def t2_lut():
    allc = {f"{n}.{c}" for n in ROOTS for c, _ in CELLS}
    labh = {f"labh.{c}" for c, _ in CELLS}; edh = {f"edh.{c}" for c, _ in CELLS}
    return _packet("lut", lut, LUT_STAGES, {"3.1.33": allc, "7.2.35": edh, "7.2.10": labh, "8.2.40": labh, "8.4.53": labh, "3.4.79": {f"{n}.{c}" for n in ROOTS for c in ("1s", "1p")},
                                            "3.4.80": {f"{n}.2s" for n in ROOTS}, "2.4.85": {f"{n}.{c}" for n in ROOTS for c in ("3s", "3d", "3p")}, "6.4.143": {f"{n}.3s" for n in ROOTS},
                                            "7.4.51": {f"{n}.{c}" for n in ROOTS for c in ("3d", "3p")}, "7.4.50": {f"{n}.2s" for n in ROOTS}, "7.4.52": {f"{n}.1s" for n in ROOTS}, "8.2.66": {f"{n}.3p" for n in ROOTS}, "8.3.15": {f"{n}.3p" for n in ROOTS}})


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lrt": t1_lrt(), "t2_lut": t2_lut()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_ATMANEPADA_LRT_LUT_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_ATMANEPADA_LRT_LUT_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.atmanepada_lrt_lut_compiled_candidate.v1", "status": status, "sources": SOURCES,
        "stage_order": {"lrt": list(LRT_STAGES), "lut": list(LUT_STAGES)},
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "labh and edh in lṛṭ and luṭ ātmanepada, six cells each (24 forms), by 3.1.33 with 7.2.35 / 7.2.10, 8.4.55, 8.2.40 + 8.4.53, 8.3.59, 3.4.79 / 3.4.80, 7.1.3, 7.2.81 + 6.1.66 + 6.1.97, 7.3.101, 2.4.85 + 6.4.143 + 7.4.51, 7.4.50, 7.4.52; each rule breaks exactly the cells stated",
            ],
            "NOT_claimed": ["in lṛṭ 1s (lapsye) 3.4.79 is surface-neutral: a + iṭ gives e by 6.1.97 either way — recorded, not forced", "the anudātta status of labh (7.2.10) declared from the Dhātupāṭha; the 2d / 2p / 1d cells; other roots; lṛṅ", "RH, YM untouched"],
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
