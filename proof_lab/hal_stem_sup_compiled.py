from __future__ import annotations

"""Exact certificate (theorum/92): THE CONSONANT-STEM SUP PARADIGMS COMPILED —
rājan, ātman (n-stems) and marut (t-stem) through the quoted sūtras; the
pada / bha saṁjñās (1.4.17–18) made load-bearing; 6.4.137 as a control.

Quoted sūtras:
 1.4.14   suptiṅantaṁ padam
 1.4.17   svādiṣv asarvanāmasthāne           before a sup other than sarvanāmasthāna (beginning with a consonant) the stem is pada
 1.4.18   yaci bham                           before one beginning with y or a vowel it is bha
 1.1.42 / 1.1.43                              sarvanāmasthāna (theorum/90)
 6.4.8    sarvanāmasthāne cāsambuddhau       upadhā of an n-final aṅga lengthened before sarvanāmasthāna (not sambuddhi)
 6.1.68   halṅyābbhyo dīrghāt sutisyapṛktaṁ hal   su drops after a consonant
 8.2.7    nalopaḥ prātipadikāntasya           pada-final n of a prātipadika drops
 8.2.8    na ṅisambuddhyoḥ                    but not before ṅi or in the sambuddhi
 6.4.129  bhasya (adhikāra) ; 6.4.134 allopo 'naḥ   the a of a bha ending in -an drops
 6.4.136  vibhāṣā ṅiśyoḥ                      optionally before ṅi and śī
 6.4.137  na saṁyogād vamantāt                not after a cluster ending in v or m (ātman)
 8.4.40   stoḥ ścunā ścuḥ                     n + j → ñ (theorum/58, 80)
 8.2.39   jhalāṁ jaśo 'nte                    a pada-final jhal becomes jaś (marud-bhyām)
 8.4.55   khari ca                            a jhal before a khar becomes car (marut-su)
 8.4.56   vāvasāne                            at a pause, optionally the car (marut)
 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  rājan: 22 forms (with the 6.4.136 option rājñi / rājani) equal the
     classical paradigm; pada (1.4.17) breaks exactly the consonant-initial
     cells, bha (1.4.18) exactly the vowel-initial non-sarvanāmasthāna cells,
     and each other stage its own cells.
 T2  ātman: 6.4.137 blocks the a-lopa after -tm- (ātmanaḥ, not *ātmnaḥ);
     without 6.4.137 exactly the bha cells break.
 T3  marut: 22 forms; 8.2.39 breaks exactly the bhyām / bhis / bhyas cells,
     8.4.55 exactly marutsu; 8.4.56 gives the pause form.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "1.4.14": "suptiṅantaṁ padam", "1.4.17": "svādiṣv asarvanāmasthāne", "1.4.18": "yaci bham", "1.1.42": "śi sarvanāmasthānam", "1.1.43": "suḍ anapuṁsakasya",
    "6.4.8": "sarvanāmasthāne cāsambuddhau", "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "8.2.7": "nalopaḥ prātipadikāntasya", "8.2.8": "na ṅisambuddhyoḥ",
    "6.4.129": "bhasya", "6.4.134": "allopo 'naḥ", "6.4.136": "vibhāṣā ṅiśyoḥ", "6.4.137": "na saṁyogād vamantāt", "8.4.40": "stoḥ ścunā ścuḥ",
    "8.2.39": "jhalāṁ jaśo 'nte", "8.4.55": "khari ca", "8.4.56": "vāvasāne", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
SARVANAMASTHANA = {"1s", "1d", "1p", "2s", "2d", "8s"}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
JAS_OF = {"t": "d", "k": "g", "p": "b", "ṭ": "ḍ", "c": "j"}
CAR_OF = {v: k for k, v in JAS_OF.items()}
RAJAN = {"1s": "rājā", "1d": "rājānau", "1p": "rājānaḥ", "2s": "rājānam", "2d": "rājānau", "2p": "rājñaḥ", "3s": "rājñā", "3d": "rājabhyām", "3p": "rājabhiḥ",
         "4s": "rājñe", "4d": "rājabhyām", "4p": "rājabhyaḥ", "5s": "rājñaḥ", "5d": "rājabhyām", "5p": "rājabhyaḥ", "6s": "rājñaḥ", "6d": "rājñoḥ", "6p": "rājñām",
         "7s": "rājñi / rājani", "7d": "rājñoḥ", "7p": "rājasu", "8s": "rājan"}
ATMAN = {"1s": "ātmā", "1d": "ātmānau", "1p": "ātmānaḥ", "2s": "ātmānam", "2d": "ātmānau", "2p": "ātmanaḥ", "3s": "ātmanā", "3d": "ātmabhyām", "3p": "ātmabhiḥ",
         "4s": "ātmane", "4d": "ātmabhyām", "4p": "ātmabhyaḥ", "5s": "ātmanaḥ", "5d": "ātmabhyām", "5p": "ātmabhyaḥ", "6s": "ātmanaḥ", "6d": "ātmanoḥ", "6p": "ātmanām",
         "7s": "ātmani", "7d": "ātmanoḥ", "7p": "ātmasu", "8s": "ātman"}
MARUT = {"1s": "marut", "1d": "marutau", "1p": "marutaḥ", "2s": "marutam", "2d": "marutau", "2p": "marutaḥ", "3s": "marutā", "3d": "marudbhyām", "3p": "marudbhiḥ",
         "4s": "marute", "4d": "marudbhyām", "4p": "marudbhyaḥ", "5s": "marutaḥ", "5d": "marudbhyām", "5p": "marudbhyaḥ", "6s": "marutaḥ", "6d": "marutoḥ", "6p": "marutām",
         "7s": "maruti", "7d": "marutoḥ", "7p": "marutsu", "8s": "marut"}
ALL_STAGES = ("pada", "bha", "6.4.8", "6.1.68", "8.2.7", "8.2.8", "6.4.134", "6.4.136", "6.4.137", "8.4.40", "8.2.39", "8.4.55", "8.4.56", "8.2.66", "8.3.15")


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    st = list(stem)
    path = [f"{upadesa} → {''.join(aff)}"]
    sns = code in SARVANAMASTHANA
    samb = code == "8s"
    n_stem = st[-1] == "n" and st[-2] == "a"
    cons_initial = bool(aff) and aff[0] not in VOWELS
    pada = ("pada" in on) and (not sns) and cons_initial                       # 1.4.17
    bha = ("bha" in on) and (not sns) and bool(aff) and (aff[0] in VOWELS or aff[0] == "y")   # 1.4.18
    # 6.4.8: upadhā dīrgha of the n-stem before sarvanāmasthāna, not sambuddhi
    if "6.4.8" in on and n_stem and sns and not samb:
        st[-2] = "ā"; path.append("upadhā lengthened before sarvanāmasthāna (6.4.8)")
    # 6.1.68: su drops after a consonant (1s, 8s)
    if "6.1.68" in on and code in ("1s", "8s") and aff == ["s"]:
        aff = []; path.append("su dropped after a consonant (6.1.68)")
    # bha: 6.4.134 allopo 'naḥ, 6.4.136 option before ṅi, 6.4.137 block
    optional = None
    if n_stem and bha and "6.4.134" in on:
        blocked = "6.4.137" in on and len(st) >= 4 and st[-3] in ("v", "m") and st[-4] not in VOWELS    # cluster ending in v / m before the an
        if blocked:
            path.append("a-lopa blocked after a cluster ending in v / m (6.4.137)")
        elif code == "7s" and "6.4.136" in on:
            optional = "".join(st + aff)                                          # the un-elided option (rājani)
            st = st[:-2] + ["n"]; path.append("a of -an dropped before ṅi, optionally (6.4.134, 6.4.136)")
        else:
            st = st[:-2] + ["n"]; path.append("a of -an dropped (6.4.134 allopo 'naḥ, bhasya 6.4.129)")
        if "8.4.40" in on and st[-1] == "n" and len(st) >= 2 and st[-2] in ("j", "c", "ch", "jh", "ñ"):
            st[-1] = "ñ"; path.append("n → ñ after j (8.4.40 stoḥ ścunā ścuḥ)")
    word = st + aff
    # pada-final operations: 8.2.7 nalopa (not before ṅi / in sambuddhi: 8.2.8), 8.2.39 jaśtva
    final_is_pada_end = pada or (code in ("1s", "8s") and not aff)
    if final_is_pada_end:
        if n_stem and st[-1] == "n" and "8.2.7" in on and not (("8.2.8" in on) and samb):
            st = st[:-1]; word = st + aff; path.append("pada-final n dropped (8.2.7)")
        elif n_stem and samb and "8.2.8" in on:
            path.append("n kept in the sambuddhi (8.2.8)")
        if st[-1] in JAS_OF and "8.2.39" in on:
            if aff:                                                              # before bhyām / bhis / bhyas / su
                st[-1] = JAS_OF[st[-1]]; word = st + aff; path.append("pada-final jhal → jaś (8.2.39)")
                if "8.4.55" in on and aff[0] in ("s", "k", "kh", "c", "ch", "ṭ", "ṭh", "t", "th", "p", "ph", "ś", "ṣ"):
                    st[-1] = CAR_OF[st[-1]]; word = st + aff; path.append("jaś → car before khar (8.4.55 khari ca)")
            else:
                if "8.4.56" in on:
                    path.append("jaś at pada end (8.2.39), the car restored at pause (8.4.56 vāvasāne)")
                else:
                    st[-1] = JAS_OF[st[-1]]; word = st + aff; path.append("pada-final jhal → jaś (8.2.39)")
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


def t1_rajan() -> dict[str, Any]:
    stem = ("r", "ā", "j", "a", "n")
    forms = paradigm(stem)
    expected_breaks = {"pada": {"3d", "3p", "4d", "4p", "5d", "5p", "7p"}, "bha": {"2p", "3s", "4s", "5s", "6s", "6d", "6p", "7s", "7d"}, "6.4.8": {"1s", "1d", "1p", "2s", "2d"},
                       "6.1.68": {"1s", "8s"}, "8.2.7": {"1s", "3d", "3p", "4d", "4p", "5d", "5p", "7p"}, "8.2.8": {"8s"}, "6.4.134": {"2p", "3s", "4s", "5s", "6s", "6d", "6p", "7s", "7d"},
                       "6.4.136": {"7s"}, "8.4.40": {"2p", "3s", "4s", "5s", "6s", "6d", "6p", "7s", "7d"}}
    broken = {}
    for s in expected_breaks:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in RAJAN if f[c] != RAJAN[c])
    checks = {"rajan_22_forms_equal_the_classical_paradigm": forms == RAJAN}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken}


def t2_atman() -> dict[str, Any]:
    stem = ("ā", "t", "m", "a", "n")
    forms = paradigm(stem)
    without = paradigm(stem, tuple(x for x in ALL_STAGES if x != "6.4.137"))
    broken = sorted(c for c in ATMAN if without[c] != ATMAN[c])
    checks = {"atman_22_forms_equal_the_classical_paradigm": forms == ATMAN,
              "without_6_4_137_exactly_the_bha_cells_break": set(broken) == {"2p", "3s", "4s", "5s", "6s", "6d", "6p", "7s", "7d"},
              "the_blocked_form_would_be_atmnah": without["2p"] == "ātmnaḥ"}
    return {"checks": checks, "forms": forms, "without_6_4_137": without}


def t3_marut() -> dict[str, Any]:
    stem = ("m", "a", "r", "u", "t")
    forms = paradigm(stem)
    expected_breaks = {"8.2.39": {"3d", "3p", "4d", "4p", "5d", "5p"}, "8.4.55": {"7p"}, "8.4.56": {"1s", "8s"}, "pada": {"3d", "3p", "4d", "4p", "5d", "5p"}}   # on 7p, 8.2.39 then 8.4.55 return the t: pada is not load-bearing there (recorded)
    broken = {}
    for s in expected_breaks:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in MARUT if f[c] != MARUT[c])
    checks = {"marut_22_forms_equal_the_classical_paradigm": forms == MARUT}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()})
    checks["without_8_4_56_the_pause_form_is_marud"] = paradigm(stem, tuple(x for x in ALL_STAGES if x != "8.4.56"))["1s"] == "marud"
    return {"checks": checks, "forms": forms, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_rajan": t1_rajan(), "t2_atman": t2_atman(), "t3_marut": t3_marut()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_HAL_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_HAL_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.hal_stem_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "rājan: 22 forms (7s with the 6.4.136 option) through 1.4.17 / 1.4.18, 6.4.8, 6.1.68, 8.2.7 / 8.2.8, 6.4.134 / 6.4.136, 8.4.40, pause rules; pada, bha and every stage break exactly their cells",
                "ātman: 22 forms; 6.4.137 blocks the a-lopa after -tm- and breaks exactly the bha cells when removed (*ātmnaḥ)",
                "marut: 22 forms; 8.2.39 breaks exactly the bhyām / bhis / bhyas cells; 8.4.56 restores the car at pause",
            ],
            "NOT_claimed": [
                "other consonant stems (vāc with 8.2.30 at pada end, s-stems beyond theorum/65, in-stems, -as/-us), neuters, the 1.4.2 option mechanics of 6.4.136 beyond listing both forms",
                "stems are declared prātipadikas; the stage order is a declared pipeline",
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
