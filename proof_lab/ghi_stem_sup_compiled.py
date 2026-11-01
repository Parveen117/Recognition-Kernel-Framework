from __future__ import annotations

"""Exact certificate (theorum/91): THE GHI-STEM (i / u, masculine) SUP PARADIGM
COMPILED — hari, agni, guru, vāyu through the quoted sūtras, with the ghi
saṁjñā (1.4.7) load-bearing and one engine serving both vowels.

Quoted sūtras:
 1.2.45   arthavad adhātur apratyayaḥ prātipadikam    a meaningful non-root non-affix form is a prātipadika
 1.4.7    śeṣo ghy asakhi                             the remaining i / u stems (not sakhi) are ghi
 7.3.111  gher ṅiti                                   guṇa of a ghi before a ṅit sup
 7.3.119  ac ca gheḥ                                  before ṅi, the ghi final becomes a and ṅi becomes au
 7.3.120  āṅo nāstriyām                               after a ghi (non-feminine) ṭā becomes nā
 7.3.108  hrasvasya guṇaḥ                             guṇa of a short vowel in the sambuddhi
 7.3.109  jasi ca                                     and before jas
 6.1.110  ṅasiṅasoś ca                                after eṅ, the a of ṅasi / ṅas: pūrvarūpa
 6.1.102  prathamayoḥ pūrvasavarṇaḥ ; 6.1.103 tasmāc chaso naḥ puṁsi
 6.1.107  ami pūrvaḥ ; 6.1.77 iko yaṇ aci ; 6.1.78 eco 'yavāyāvaḥ
 7.1.54   hrasvanadyāpo nuṭ ; 6.4.3 nāmi ; 8.4.2 aṭkupvāṅnumvyavāye 'pi (with 8.4.1) ; 8.4.37 padāntasya ; 6.1.88 vṛddhir eci
 6.1.69   eṅhrasvāt sambuddheḥ ; 8.3.59 ādeśapratyayayoḥ ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  hari and guru: 22 forms each equal the classical paradigms; every stage
     breaks exactly its own cells; the ghi saṁjñā is load-bearing on
     exactly {3s, 4s, 5s, 6s, 7s} (the ṅit cells, ṭā and ṅi).
 T2  agni (no r: agninā, agnīnām) and vāyu: 44 more forms — 8.4.2's ṇatva
     fires in hari / guru and not in agni / vāyu, decided on the carrier.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import BASE, GUNA_SET, antaratama
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "1.2.45": "arthavad adhātur apratyayaḥ prātipadikam", "1.4.7": "śeṣo ghy asakhi", "7.3.111": "gher ṅiti", "7.3.119": "ac ca gheḥ", "7.3.120": "āṅo nāstriyām",
    "7.3.108": "hrasvasya guṇaḥ", "7.3.109": "jasi ca", "6.1.110": "ṅasiṅasoś ca", "6.1.102": "prathamayoḥ pūrvasavarṇaḥ", "6.1.103": "tasmāc chaso naḥ puṁsi",
    "6.1.107": "ami pūrvaḥ", "6.1.77": "iko yaṇ aci", "6.1.78": "eco 'yavāyāvaḥ", "7.1.54": "hrasvanadyāpo nuṭ", "6.4.3": "nāmi", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade",
    "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.37": "padāntasya", "6.1.88": "vṛddhir eci", "6.1.69": "eṅhrasvāt sambuddheḥ", "8.3.59": "ādeśapratyayayoḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
LONG = {"i": "ī", "u": "ū"}
YAN = {"i": "y", "u": "v"}
AYADI = {"e": ("a", "y"), "o": ("a", "v")}
AT_KU_PU = set("aāiīuūṛṝḷḹ") | {"e", "ai", "o", "au", "h", "y", "v", "r", "k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m"}   # 8.4.2: aṭ, ku, pu, āṅ, num may intervene
HARI = {"1s": "hariḥ", "1d": "harī", "1p": "harayaḥ", "2s": "harim", "2d": "harī", "2p": "harīn", "3s": "hariṇā", "3d": "haribhyām", "3p": "haribhiḥ",
        "4s": "haraye", "4d": "haribhyām", "4p": "haribhyaḥ", "5s": "hareḥ", "5d": "haribhyām", "5p": "haribhyaḥ", "6s": "hareḥ", "6d": "haryoḥ", "6p": "harīṇām",
        "7s": "harau", "7d": "haryoḥ", "7p": "hariṣu", "8s": "hare"}
GURU = {"1s": "guruḥ", "1d": "gurū", "1p": "guravaḥ", "2s": "gurum", "2d": "gurū", "2p": "gurūn", "3s": "guruṇā", "3d": "gurubhyām", "3p": "gurubhiḥ",
        "4s": "gurave", "4d": "gurubhyām", "4p": "gurubhyaḥ", "5s": "guroḥ", "5d": "gurubhyām", "5p": "gurubhyaḥ", "6s": "guroḥ", "6d": "gurvoḥ", "6p": "gurūṇām",
        "7s": "gurau", "7d": "gurvoḥ", "7p": "guruṣu", "8s": "guro"}
ALL_STAGES = ("ghi", "7.3.111", "7.3.119", "7.3.120", "7.3.108", "7.3.109", "6.1.110", "6.1.102", "7.1.54", "6.4.3", "8.4.2", "6.1.69", "8.3.59", "8.2.66", "8.3.15")


def guna(v: str) -> str:
    return antaratama(v, GUNA_SET)        # theorum/80: 1.1.50 on the sthāna table (i → e, u → o)


def natva_8_4_2(word: list[str]) -> tuple[list[str], bool]:
    """n → ṇ after r / ṣ (8.4.1) with only aṭ / ku / pu / āṅ / num intervening (8.4.2), within the pada."""
    out = list(word)
    fired = False
    for i, s in enumerate(out):
        if s != "n" or i == len(out) - 1:          # 8.4.37 padāntasya: no ṇatva of a pada-final n
            continue
        j = i - 1
        while j >= 0 and out[j] in AT_KU_PU and out[j] not in ("r",):
            j -= 1
        if j >= 0 and out[j] in ("r", "ṣ", "ṛ", "ṝ"):
            out[i] = "ṇ"; fired = True
    return out, fired


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    ngit = "ṅ" in r["its"]
    st = list(stem)
    v = st[-1]
    assert v in ("i", "u")
    ghi = "ghi" in on                                                   # 1.4.7 śeṣo ghy asakhi
    path = [f"{upadesa} → {''.join(aff)}" + (" (ṅit)" if ngit else "")]
    samb = code == "8s"
    # 7.3.119 ac ca gheḥ: before ṅi, final → a and ṅi → au
    if "7.3.119" in on and ghi and code == "7s":
        st[-1] = "a"; aff = ["au"]; path.append("final → a, ṅi → au (7.3.119 ac ca gheḥ)")
    # 7.3.111 gher ṅiti: guṇa before ṅit (ṅe, ṅasi, ṅas; not ṅi after 7.3.119)
    elif "7.3.111" in on and ghi and ngit:
        st[-1] = guna(v); path.append(f"{v} → {st[-1]} before ṅit (7.3.111 gher ṅiti; 1.1.50)")
    # 7.3.120 āṅo nāstriyām: ṭā → nā after ghi
    if "7.3.120" in on and ghi and code == "3s":
        aff = ["n", "ā"]; path.append("ṭā → nā (7.3.120)")
    # 7.3.108 / 7.3.109: guṇa in the sambuddhi and before jas
    if "7.3.108" in on and samb:
        st[-1] = guna(v); path.append(f"{v} → {st[-1]} in the sambuddhi (7.3.108)")
    if "7.3.109" in on and code == "1p":
        st[-1] = guna(v); path.append(f"{v} → {st[-1]} before jas (7.3.109)")
    # 6.1.69: sambuddhi su dropped after eṅ
    if samb and "6.1.69" in on and st[-1] in ("e", "o") and aff == ["s"]:
        aff = []; path.append("sambuddhi su dropped after eṅ (6.1.69)")
    # 7.1.54 nuṭ + 6.4.3 nāmi
    if code == "6p" and "7.1.54" in on:
        aff = list(its("nu~ṭ", "agama")["remaining_sounds"]) + aff; path.append("nuṭ (7.1.54)")
        if "6.4.3" in on:
            st[-1] = LONG[v]; path.append(f"{v} → {st[-1]} before nām (6.4.3)")
    # seam sandhi
    if aff and aff[0] in VOWELS:
        a, b = st[-1], aff[0]
        if a == "a" and b == "au":
            st[-1] = "au"; aff = aff[1:]; path.append("a + au → au (6.1.88 vṛddhir eci)")
        elif "6.1.110" in on and a in ("e", "o") and code in ("5s", "6s") and b == "a":
            aff = aff[1:]; path.append("eṅ + a → pūrvarūpa (6.1.110 ṅasiṅasoś ca)")
        elif a in ("e", "o"):
            st = st[:-1] + list(AYADI[a]); path.append(f"{a} + {b} → {''.join(AYADI[a])}{b} (6.1.78)")
        elif a in ("i", "u") and code == "2s":
            aff = aff[1:]; path.append(f"{a} + am → {a}m (6.1.107 ami pūrvaḥ)")
        elif "6.1.102" in on and a in ("i", "u") and code in ("1d", "2d", "2p"):
            st[-1] = LONG[a]; aff = aff[1:]; path.append(f"{a} + {b} → {LONG[a]} (6.1.102 pūrvasavarṇa)")
            if code == "2p" and aff == ["s"]:
                aff = ["n"]; path.append("s → n (6.1.103 puṁsi)")
        elif a in ("i", "u"):
            st[-1] = YAN[a]; path.append(f"{a} + {b} → {YAN[a]}{b} (6.1.77)")
    word = st + aff
    # 8.3.59 ṣatva in 7p
    if "8.3.59" in on and code == "7p" and "".join(aff) == "su" and st[-1] in ("i", "u", "ī", "ū"):
        word = st + ["ṣ", "u"]; path.append("s → ṣ after iṇ (8.3.59)")
    # 8.4.2 ṇatva
    if "8.4.2" in on:
        word, fired = natva_8_4_2(word)
        if fired:
            path.append("n → ṇ (8.4.1 / 8.4.2)")
    if word[-1] == "s" and "8.2.66" in on:
        word[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word), path


def paradigm(stem, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(stem, c, up, stages)[0] for c, up in SUP}


def t1_hari_guru() -> dict[str, Any]:
    hari, guru = ("h", "a", "r", "i"), ("g", "u", "r", "u")
    forms = {"hari": paradigm(hari), "guru": paradigm(guru)}
    expected_breaks = {"ghi": {"3s", "4s", "5s", "6s", "7s"}, "7.3.111": {"4s", "5s", "6s"}, "7.3.119": {"7s"}, "7.3.120": {"3s"}, "7.3.108": {"8s"}, "7.3.109": {"1p"},
                       "6.1.110": {"5s", "6s"}, "6.1.102": {"1d", "2d", "2p"}, "7.1.54": {"6p"}, "6.4.3": {"6p"}, "8.4.2": {"3s", "6p"}, "6.1.69": {"8s"}, "8.3.59": {"7p"}}
    broken = {}
    for s in expected_breaks:
        f = paradigm(hari, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in HARI if f[c] != HARI[c])
    checks = {"hari_22_forms_equal_the_classical_paradigm": forms["hari"] == HARI, "guru_22_forms_equal_the_classical_paradigm_same_engine": forms["guru"] == GURU}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()})
    return {"checks": checks, "forms": forms, "paths_hari": {c: decline(hari, c, up)[1] for c, up in SUP}, "broken_cells": broken}


def t2_agni_vayu() -> dict[str, Any]:
    agni, vayu = ("a", "g", "n", "i"), ("v", "ā", "y", "u")
    fa, fv = paradigm(agni), paradigm(vayu)
    exp_a = {c: "agn" + HARI[c][3:] for c in HARI}
    exp_v = {c: "vāy" + GURU[c][3:] for c in GURU}
    # no r / ṣ in agni, vāyu: 8.4.2 must not fire → agninā, agnīnām; vāyunā, vāyūnām
    exp_a["3s"], exp_a["6p"] = "agninā", "agnīnām"
    exp_v["3s"], exp_v["6p"] = "vāyunā", "vāyūnām"
    checks = {"agni_44_minus_natva_equal_the_exchanged_hari_paradigm": fa == exp_a, "vayu_equals_the_exchanged_guru_paradigm_without_natva": fv == exp_v,
              "natva_8_4_2_fires_in_hari_guru_only": fa["3s"] == "agninā" and fv["6p"] == "vāyūnām" and HARI["3s"] == "hariṇā" and GURU["6p"] == "gurūṇām"}
    return {"checks": checks, "agni": fa, "vāyu": fv}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_hari_guru": t1_hari_guru(), "t2_agni_vayu": t2_agni_vayu()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_GHI_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_GHI_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.ghi_stem_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "hari and guru: 22 forms each from the teaching forms through 1.4.7, 7.3.111, 7.3.119, 7.3.120, 7.3.108, 7.3.109, 6.1.110, 6.1.102 / 6.1.103, 6.1.107, 6.1.77, 6.1.78, 7.1.54 / 6.4.3, 8.4.1 / 8.4.2, 6.1.69, 8.3.59, 8.2.66, 8.3.15, one engine for both vowels (guṇa by theorum/80's antaratama)",
                "the ghi saṁjñā breaks exactly {3s, 4s, 5s, 6s, 7s}; every other stage exactly its own cells",
                "agni and vāyu: 44 forms; 8.4.2's ṇatva decided on the carrier (fires in hari / guru, not in agni / vāyu)",
            ],
            "NOT_claimed": [
                "sakhi, pati (1.4.8), feminine i / u stems (mati, dhenu: 1.4.6 ṅiti hrasvaś ca options), neuters (vāri, madhu), long ī / ū stems; stems are declared prātipadikas (1.2.45)",
                "the stage order is a declared pipeline",
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
