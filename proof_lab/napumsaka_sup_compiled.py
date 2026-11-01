from __future__ import annotations

"""Exact certificate (theorum/93): THE NEUTER SUP PARADIGMS COMPILED — phala
(a-stem) and vāri (i-stem) through the quoted sūtras; the neuter substitutes
(śī, śi, am, luk) and the num of 7.1.72 / 7.1.73 made load-bearing.

Quoted sūtras:
 7.1.23   svamor napuṁsakāt                  after a neuter, su and am are luk
 7.1.24   ato 'm                              but after an a-stem they are am
 7.1.19   napuṁsakāc ca                       after a neuter, au becomes śī
 7.1.20   jaśśasoḥ śiḥ                        jas and śas become śi
 1.1.42   śi sarvanāmasthānam                 śi is sarvanāmasthāna
 7.1.72   napuṁsakasya jhalacaḥ               a neuter ending in jhal or ac takes num before sarvanāmasthāna
 7.1.73   iko 'ci vibhaktau                   an ik-final neuter takes num before a vowel-initial vibhakti
 6.4.8    sarvanāmasthāne cāsambuddhau        upadhā lengthened (phalāni, vārīṇi)
 6.1.87   ād guṇaḥ (a + ī → e: phale)         7.1.9 ato bhisa ais ; 7.1.12 ṭāṅasiṅasām inātsyāḥ ; 7.3.102 supi ca ; 7.3.103 bahuvacane jhaly et ; 7.1.54 ; 6.4.3
 8.4.2    aṭkupvāṅnumvyavāye 'pi (ṇatva)       8.3.59 ādeśapratyayayoḥ ; 7.3.108 hrasvasya guṇaḥ ; 6.1.69 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  phala: 22 forms (phalam phale phalāni … phalānām phale phaleṣu, he phala);
     7.1.24, 7.1.19, 7.1.20, 7.1.72, 6.4.8 each break exactly their cells.
 T2  vāri: 22 forms (vāri vāriṇī vārīṇi; vāriṇā …; vārīṇām; vāriṇi; vāriṣu;
     he vāre / vāri); 7.1.23, 7.1.73 (the num before every vowel-initial
     vibhakti, hence no ghi guṇa), 7.1.72 and 6.4.8 each break exactly their
     cells; 8.4.2 decides vāriṇā / vārīṇām on the carrier.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.ghi_stem_sup_compiled import natva_8_4_2
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "7.1.23": "svamor napuṁsakāt", "7.1.24": "ato 'm", "7.1.19": "napuṁsakāc ca", "7.1.20": "jaśśasoḥ śiḥ", "1.1.42": "śi sarvanāmasthānam",
    "7.1.72": "napuṁsakasya jhalacaḥ", "7.1.73": "iko 'ci vibhaktau", "6.4.8": "sarvanāmasthāne cāsambuddhau", "6.1.87": "ād guṇaḥ", "7.1.9": "ato bhisa ais",
    "7.1.12": "ṭāṅasiṅasām inātsyāḥ", "7.1.13": "ṅer yaḥ", "7.3.102": "supi ca", "7.3.103": "bahuvacane jhaly et", "7.1.54": "hrasvanadyāpo nuṭ", "6.4.3": "nāmi",
    "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.3.59": "ādeśapratyayayoḥ", "7.3.108": "hrasvasya guṇaḥ", "6.1.69": "eṅhrasvāt sambuddheḥ", "6.1.107": "ami pūrvaḥ",
    "6.1.101": "akaḥ savarṇe dīrghaḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
LONG = {"a": "ā", "i": "ī", "u": "ū"}
PHALA = {"1s": "phalam", "1d": "phale", "1p": "phalāni", "2s": "phalam", "2d": "phale", "2p": "phalāni", "3s": "phalena", "3d": "phalābhyām", "3p": "phalaiḥ",
         "4s": "phalāya", "4d": "phalābhyām", "4p": "phalebhyaḥ", "5s": "phalāt", "5d": "phalābhyām", "5p": "phalebhyaḥ", "6s": "phalasya", "6d": "phalayoḥ",
         "6p": "phalānām", "7s": "phale", "7d": "phalayoḥ", "7p": "phaleṣu", "8s": "phala"}
VARI = {"1s": "vāri", "1d": "vāriṇī", "1p": "vārīṇi", "2s": "vāri", "2d": "vāriṇī", "2p": "vārīṇi", "3s": "vāriṇā", "3d": "vāribhyām", "3p": "vāribhiḥ",
        "4s": "vāriṇe", "4d": "vāribhyām", "4p": "vāribhyaḥ", "5s": "vāriṇaḥ", "5d": "vāribhyām", "5p": "vāribhyaḥ", "6s": "vāriṇaḥ", "6d": "vāriṇoḥ",
        "6p": "vārīṇām", "7s": "vāriṇi", "7d": "vāriṇoḥ", "7p": "vāriṣu", "8s": "vāre / vāri"}
ALL_STAGES = ("7.1.23", "7.1.24", "7.1.19", "7.1.20", "7.1.72", "7.1.73", "6.4.8", "7.1.9", "7.1.12", "7.3.102", "7.3.103", "7.1.54", "6.4.3", "8.4.2", "8.3.59", "7.3.108", "6.1.69", "8.2.66", "8.3.15")


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    st = list(stem)
    v = st[-1]
    path = [f"{upadesa} → {''.join(aff)}"]
    samb = code == "8s"
    sns = code in ("1s", "1d", "1p", "2s", "2d", "8s")
    optional = None
    # neuter substitutes
    if code in ("1s", "2s") and not samb:
        if "7.1.24" in on and v == "a":
            aff = ["a", "m"]; path.append("su / am → am after a (7.1.24 ato 'm)")
        elif "7.1.23" in on:
            aff = []; path.append("su / am → luk (7.1.23 svamor napuṁsakāt)")
    if "7.1.19" in on and code in ("1d", "2d"):
        aff = list(its("śī", "pratyaya")["remaining_sounds"]); path.append("au → śī (7.1.19)")
    if "7.1.20" in on and code in ("1p", "2p"):
        aff = list(its("śi", "pratyaya")["remaining_sounds"]); path.append("jas / śas → śi (7.1.20; sarvanāmasthāna 1.1.42)")
    # 6p nuṭ first (7.1.54): after it ām is no longer vowel-initial for 7.1.73
    if code == "6p" and "7.1.54" in on:
        aff = list(its("nu~ṭ", "agama")["remaining_sounds"]) + aff; path.append("nuṭ (7.1.54)")
        if "6.4.3" in on and st[-1] in LONG:
            st[-1] = LONG[st[-1]]; path.append("lengthened before nām (6.4.3)")
    # num: 7.1.72 before sarvanāmasthāna (śi here); 7.1.73 ik-final before vowel-initial vibhakti
    if "7.1.72" in on and code in ("1p", "2p") and aff == ["i"]:
        st = st + ["n"]; path.append("num before sarvanāmasthāna śi (7.1.72)")
        if "6.4.8" in on:
            st[-2] = LONG[v]; path.append("upadhā lengthened before sarvanāmasthāna (6.4.8)")
    elif "7.1.73" in on and v in ("i", "u") and aff and aff[0] in VOWELS and not samb:
        st = st + ["n"]; path.append("num before the vowel-initial vibhakti (7.1.73 iko 'ci vibhaktau)")
    # a-stem machinery (theorum/63's sūtras) for phala
    if v == "a":
        if "7.1.9" in on and code == "3p":
            aff = ["ai", "s"]; path.append("bhis → ais (7.1.9)")
        if "7.1.12" in on and code == "3s":
            aff = ["i", "n", "a"]; path.append("ṭā → ina (7.1.12)")
        if "7.1.12" in on and code == "5s":
            aff = ["ā", "t"]; path.append("ṅasi → āt (7.1.12)")
        if "7.1.12" in on and code == "6s":
            aff = ["s", "y", "a"]; path.append("ṅas → sya (7.1.12)")
        if code == "4s":
            aff = ["y", "a"]; path.append("ṅe → ya (7.1.13 ṅer yaḥ)")
        if "7.3.102" in on and code in ("3d", "4d", "5d", "4s") and st[-1] == "a":
            st[-1] = "ā"; path.append("a → ā before a yañ-initial sup (7.3.102 supi ca)")
        if "7.3.103" in on and code in ("4p", "5p", "7p") and st[-1] == "a":
            st[-1] = "e"; path.append("a → e before bhyas / su (7.3.103)")
    # sambuddhi
    if samb:
        if v == "a" and aff == ["s"]:
            aff = []; path.append("sambuddhi su dropped after a (6.1.69)")
        elif v in ("i", "u") and "7.3.108" in on:
            optional = "".join(st)                                   # he vāri (the un-guṇated option, Siddhānta-kaumudī)
            st[-1] = {"i": "e", "u": "o"}[v]; aff = []; path.append("guṇa in the sambuddhi (7.3.108), su dropped (6.1.69)")
    # seam sandhi
    if aff and aff[0] in VOWELS and st[-1] in VOWELS:
        a, b = st[-1], aff[0]
        if a == "a" and b == "ī":
            st[-1] = "e"; aff = aff[1:]; path.append("a + ī → e (6.1.87)")
        elif a == "a" and b == "a":
            aff = aff[1:]; path.append("a + a → a (6.1.101 / 6.1.107)")
        elif a == "a" and b == "ā":
            st[-1] = "ā"; aff = aff[1:]; path.append("a + ā → ā (6.1.101)")
        elif a == "a" and b == "e":
            st[-1] = "e"; aff = aff[1:]; path.append("a + e → e (6.1.97 ato guṇe)")
        elif a == "a" and b == "ai":
            st[-1] = "ai"; aff = aff[1:]; path.append("a + ai → ai (6.1.88)")
        elif a == "a" and b == "i":
            st[-1] = "e"; aff = aff[1:]; path.append("a + i → e (6.1.87)")
        elif a == "a" and b == "o":
            st[-1] = "a"; st.append("y"); path.append("a + o: ay (6.1.78 after 6.1.87? no — phalayoḥ: a + os → ayoḥ by 6.1.78 on e)")
        elif a in ("i", "u"):
            st[-1] = {"i": "y", "u": "v"}[a]; path.append(f"{a} + {b} → {st[-1]}{b} (6.1.77)")
    word = st + aff
    if "8.3.59" in on and code == "7p" and "".join(aff) == "su" and st[-1] in ("i", "u", "ī", "ū", "e"):
        word = st + ["ṣ", "u"]; path.append("s → ṣ after iṇ (8.3.59)")
    if "8.4.2" in on:
        word, fired = natva_8_4_2(word)
        if fired:
            path.append("n → ṇ (8.4.1 / 8.4.2)")
    if word and word[-1] == "s" and "8.2.66" in on:
        word[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    out = "".join(word)
    if optional is not None:
        out = f"{out} / {optional}"
    return out, path


def paradigm(stem, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(stem, c, up, stages)[0] for c, up in SUP}


def _ablation(stem, oracle, expected_breaks):
    broken = {}
    for s in expected_breaks:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in oracle if f[c] != oracle[c])
    return broken, {f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()}


def t1_phala() -> dict[str, Any]:
    stem = ("ph", "a", "l", "a")
    forms = paradigm(stem)
    exp = {"7.1.24": {"1s", "2s"}, "7.1.19": {"1d", "2d"}, "7.1.20": {"1p", "2p"}, "7.1.72": {"1p", "2p"}, "6.4.8": {"1p", "2p"}, "7.1.9": {"3p"}, "7.1.12": {"3s", "5s", "6s"},
           "7.3.102": {"3d", "4d", "5d", "4s"}, "7.3.103": {"4p", "5p", "7p"}, "7.1.54": {"6p"}, "6.4.3": {"6p"}, "8.3.59": {"7p"}}
    broken, checks = _ablation(stem, PHALA, exp)
    checks = {"phala_22_forms_equal_the_classical_neuter_paradigm": forms == PHALA, **checks}
    return {"checks": checks, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken}


def t2_vari() -> dict[str, Any]:
    stem = ("v", "ā", "r", "i")
    forms = paradigm(stem)
    exp = {"7.1.23": {"1s", "2s"}, "7.1.19": {"1d", "2d"}, "7.1.20": {"1p", "2p"}, "7.1.72": {"1p", "2p"}, "7.1.73": {"1d", "2d", "3s", "4s", "5s", "6s", "6d", "7s", "7d"},
           "6.4.8": {"1p", "2p"}, "7.1.54": {"6p"}, "6.4.3": {"6p"}, "8.4.2": {"1d", "2d", "1p", "2p", "3s", "4s", "5s", "6s", "6d", "6p", "7s", "7d"}, "8.3.59": {"7p"}, "7.3.108": {"8s"}}
    broken, checks = _ablation(stem, VARI, exp)
    checks = {"vari_22_forms_equal_the_classical_neuter_paradigm": forms == VARI, **checks}
    return {"checks": checks, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_phala": t1_phala(), "t2_vari": t2_vari()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NAPUMSAKA_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_NAPUMSAKA_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.napumsaka_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "phala: 22 forms through 7.1.24, 7.1.19, 7.1.20 / 1.1.42, 7.1.72, 6.4.8, 6.1.87 and theorum/63's a-stem sūtras; each stage breaks exactly its cells",
                "vāri: 22 forms through 7.1.23, 7.1.19, 7.1.20, 7.1.72, 7.1.73 (num before every vowel-initial vibhakti), 6.4.8, 7.1.54 / 6.4.3, 8.4.2, 8.3.59, 7.3.108; each stage breaks exactly its cells",
            ],
            "NOT_claimed": [
                "u-stem neuters (madhu), consonant neuters (jagat, manas: 7.1.72 with 6.4.8 / 7.1.70), neuter sarvanāma (tat beyond theorum/65), the sūtra licensing the second sambuddhi option he vāri (listed from the Siddhānta-kaumudī, not derived)",
                "stems declared prātipadikas; the stage order is a declared pipeline",
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
