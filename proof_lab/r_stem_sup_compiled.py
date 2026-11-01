from __future__ import annotations

"""Exact certificate (theorum/90): THE ṚKĀRĀNTA (tṛc) SUP PARADIGM COMPILED —
kartṛ and the agent nouns of theorum/89 declined through the quoted sūtras;
the sarvanāmasthāna saṁjñā made load-bearing.

Quoted sūtras:
 1.1.42   śi sarvanāmasthānam ; 1.1.43 suḍ anapuṁsakasya     su au jas am auṭ are sarvanāmasthāna (non-neuter)
 7.1.94   ṛdu-śanas-purudaṁso-'nehasāṁ ca                     (anaṅ for ṛ-final stems before su, 7.1.93 anuvṛtti: asambuddhi)
 1.1.53   ṅic ca                                              a ṅit substitute replaces the final sound
 6.4.8    sarvanāmasthāne cāsambuddhau                        upadhā of an n-final aṅga lengthened before sarvanāmasthāna
 6.4.11   aptṛntṛcsvasṛnaptṛneṣṭṛtvaṣṭṛkṣattṛhotṛpotṛpraśāstṝṇām   their upadhā is lengthened (before sarvanāmasthāna, asambuddhi)
 6.1.68   halṅyābbhyo dīrghāt sutisyapṛktaṁ hal                su drops after a consonant
 8.2.7    nalopaḥ prātipadikāntasya                            final n of a prātipadika drops
 7.3.110  ṛto ṅi sarvanāmasthānayoḥ                            guṇa of ṛ before ṅi and sarvanāmasthāna
 1.1.51   ur aṇ raparaḥ
 6.1.111  ṛta ut                                               ṛ + a (ṅasi / ṅas) → ur
 8.2.24   rāt sasya                                            s drops after r (pada end)
 6.1.102  prathamayoḥ pūrvasavarṇaḥ ; 6.1.103 tasmāc chaso naḥ puṁsi
 6.1.77   iko yaṇ aci
 7.1.54   hrasvanadyāpo nuṭ ; 6.4.3 nāmi ; 8.4.1 raṣābhyāṁ no ṇaḥ samānapade (with the vārttika ṛvarṇāc ca)
 8.3.57   iṇkoḥ ; 8.3.59 ādeśapratyayayoḥ
 8.2.66   sasajuṣo ruḥ ; 8.3.15 kharavasānayor visarjanīyaḥ ; 1.3.2–1.3.9

 T1  kartṛ: 22 forms equal the classical paradigm (kartā, kartārau, kartāraḥ;
     kartāram, kartārau, kartṝn; kartrā …; kartuḥ, kartroḥ, kartṝṇām;
     kartari, kartroḥ, kartṛṣu; he kartaḥ); each stage breaks exactly its
     cells, and the sarvanāmasthāna saṁjñā (1.1.42–43) is load-bearing on
     exactly {1s, 1d, 1p, 2s, 2d, 8s}.
 T2  śrotṛ, hotṛ, cetṛ, sotṛ (theorum/89, from the pinned roots): 88 more
     forms equal to the exchanged paradigm.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.ngi_stem_sup_compiled import AGENTS, load_entries, trc_agent
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "1.1.42": "śi sarvanāmasthānam", "1.1.43": "suḍ anapuṁsakasya", "7.1.94": "ṛd uśanaspurudaṁso 'nehasāṁ ca", "1.1.53": "ṅic ca",
    "6.4.8": "sarvanāmasthāne cāsambuddhau", "6.4.11": "aptṛntṛcsvasṛnaptṛneṣṭṛtvaṣṭṛkṣattṛhotṛpotṛpraśāstṝṇām", "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal",
    "8.2.7": "nalopaḥ prātipadikāntasya", "7.3.110": "ṛto ṅi sarvanāmasthānayoḥ", "1.1.51": "ur aṇ raparaḥ", "6.1.111": "ṛta ut", "8.2.24": "rāt sasya",
    "6.1.102": "prathamayoḥ pūrvasavarṇaḥ", "6.1.103": "tasmāc chaso naḥ puṁsi", "6.1.77": "iko yaṇ aci", "7.1.54": "hrasvanadyāpo nuṭ", "6.4.3": "nāmi",
    "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.3.57": "iṇkoḥ", "8.3.59": "ādeśapratyayayoḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
SARVANAMASTHANA = {"1s", "1d", "1p", "2s", "2d", "8s"}    # 1.1.43 suḍ: su au jas am auṭ (the sambuddhi su included)
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
KARTR_ORACLE = {"1s": "kartā", "1d": "kartārau", "1p": "kartāraḥ", "2s": "kartāram", "2d": "kartārau", "2p": "kartṝn", "3s": "kartrā", "3d": "kartṛbhyām",
                "3p": "kartṛbhiḥ", "4s": "kartre", "4d": "kartṛbhyām", "4p": "kartṛbhyaḥ", "5s": "kartuḥ", "5d": "kartṛbhyām", "5p": "kartṛbhyaḥ", "6s": "kartuḥ",
                "6d": "kartroḥ", "6p": "kartṝṇām", "7s": "kartari", "7d": "kartroḥ", "7p": "kartṛṣu", "8s": "kartaḥ"}
ALL_STAGES = ("saṁjñā", "7.1.94", "7.3.110", "6.4.11", "6.4.8", "6.1.68", "8.2.7", "6.1.111", "6.1.102", "7.1.54", "6.4.3", "8.4.1", "8.3.59", "8.2.24", "8.2.66", "8.3.15")


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    st = list(stem)
    assert st[-1] == "ṛ"
    path = [f"{upadesa} → {''.join(aff)}"]
    sns = code in SARVANAMASTHANA if "saṁjñā" in on else False
    samb = code == "8s"
    # 7.1.94 anaṅ before su (not sambuddhi): ṛ → an (1.1.53 final)
    if "7.1.94" in on and code == "1s":
        st = st[:-1] + ["a", "n"]; path.append("ṛ → an (7.1.94 anaṅ; 1.1.53 ṅic ca)")
        if "6.4.8" in on and sns:
            st[-2] = "ā"; path.append("upadhā lengthened before sarvanāmasthāna (6.4.8)")
        if "6.1.68" in on:
            aff = []; path.append("su dropped after a consonant (6.1.68)")
        if "8.2.7" in on and st[-1] == "n" and not aff:
            st = st[:-1]; path.append("final n dropped (8.2.7)")
        return "".join(st + aff), path
    # 7.3.110 guṇa before ṅi and sarvanāmasthāna
    if "7.3.110" in on and (code == "7s" or sns):
        st = st[:-1] + ["a", "r"]; path.append("ṛ → ar (7.3.110; 1.1.51 rapara)")
        if "6.4.11" in on and sns and not samb:
            st[-2] = "ā"; path.append("upadhā lengthened, tṛc (6.4.11; asambuddhi 6.4.8 anuvṛtti)")
        if samb and "6.1.68" in on:
            aff = []; path.append("sambuddhi su dropped after a consonant (6.1.68)")
    # 6.1.111 ṛta ut for ṅasi / ṅas
    if "6.1.111" in on and code in ("5s", "6s") and st[-1] == "ṛ":
        st = st[:-1] + ["u", "r"]; aff = aff[1:]; path.append("ṛ + a → ur (6.1.111; 1.1.51)")
    # 6.1.102 / 6.1.103 for śas
    if "6.1.102" in on and code == "2p" and st[-1] == "ṛ":
        st[-1] = "ṝ"; aff = ["n"]; path.append("ṛ + as → ṝs (6.1.102), s → n (6.1.103 puṁsi)")
    # 7.1.54 nuṭ + 6.4.3 nāmi + 8.4.1 ṇatva
    if code == "6p":
        if "7.1.54" in on:
            aff = list(its("nu~ṭ", "agama")["remaining_sounds"]) + aff; path.append("nuṭ (7.1.54)")
            if "6.4.3" in on:
                st[-1] = "ṝ"; path.append("ṛ → ṝ before nām (6.4.3)")
            if "8.4.1" in on and st[-1] in ("ṛ", "ṝ"):
                aff[0] = "ṇ"; path.append("n → ṇ after ṛ-varṇa (8.4.1 with the vārttika)")
    # seam sandhi: ṛ + vowel → r (6.1.77)
    if aff and aff[0] in VOWELS and st[-1] == "ṛ":
        st[-1] = "r"; path.append(f"ṛ + {aff[0]} → r{aff[0]} (6.1.77)")
    word = st + aff
    # 8.3.59 ṣatva in 7p
    if "8.3.59" in on and code == "7p" and "".join(aff) == "su" and st[-1] in ("i", "ī", "u", "ū", "ṛ", "ṝ"):
        word = st + ["ṣ", "u"]; path.append("s → ṣ after iṇ (8.3.59)")
    # tripādī
    if word[-1] == "s" and "8.2.24" in on and len(word) > 1 and word[-2] == "r":
        word = word[:-1]; path.append("s dropped after r (8.2.24)")
    if word[-1] == "s" and "8.2.66" in on:
        word[-1] = "r"; path.append("s → ru (8.2.66)")
    if word[-1] == "r" and "8.3.15" in on and (code not in ("1s",)):
        word[-1] = "ḥ"; path.append("r → ḥ at pause (8.3.15)")
    return "".join(word), path


def paradigm(stem, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(stem, c, up, stages)[0] for c, up in SUP}


def t1_kartr() -> dict[str, Any]:
    stem = ("k", "a", "r", "t", "ṛ")
    forms = paradigm(stem)
    expected_breaks = {"saṁjñā": {"1s", "1d", "1p", "2s", "2d", "8s"}, "7.1.94": {"1s"}, "7.3.110": {"1d", "1p", "2s", "2d", "7s", "8s"}, "6.4.11": {"1d", "1p", "2s", "2d"},
                       "6.4.8": {"1s"}, "8.2.7": {"1s"}, "6.1.111": {"5s", "6s"}, "6.1.102": {"2p"}, "7.1.54": {"6p"}, "6.4.3": {"6p"}, "8.4.1": {"6p"}, "8.3.59": {"7p"},
                       "8.2.24": {"5s", "6s"}}
    broken = {}
    for s in expected_breaks:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in KARTR_ORACLE if f[c] != KARTR_ORACLE[c])
    checks = {"kartr_22_forms_equal_the_classical_paradigm": forms == KARTR_ORACLE}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken}


def t2_agents() -> dict[str, Any]:
    entries = load_entries()
    out, ok, n = {}, True, 0
    for lex, exp in AGENTS.items():
        a = trc_agent(lex, entries)
        stem = tuple(a["sounds"][:-2]) + ("ṛ",)        # the masculine agent: kartrī minus ṅīp → kartṛ
        assert "".join(stem) == a["agent"] == exp
        if exp == "kartṛ":
            continue
        forms = paradigm(stem)
        pref = "".join(stem[:-1])
        for c, f in forms.items():
            ok &= f == pref + KARTR_ORACLE[c][4:]
            n += 1
        out[exp] = forms
    checks = {"srotr_hotr_cetr_sotr_88_forms_equal_the_exchanged_kartr_paradigm": ok and n == 88}
    return {"checks": checks, **out}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_kartr": t1_kartr(), "t2_agents": t2_agents()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_R_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_R_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.r_stem_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "kartṛ's 22 forms from the teaching forms through 7.1.94 / 1.1.53, 6.4.8, 6.4.11, 7.3.110 / 1.1.51, 6.1.111, 6.1.102 / 6.1.103, 6.1.77, 7.1.54 / 6.4.3 / 8.4.1, 8.3.59, 8.2.7, 8.2.24, 8.2.66, 8.3.15, 6.1.68",
                "the sarvanāmasthāna saṁjñā (1.1.42–43) and each stage break exactly the cells stated",
                "śrotṛ, hotṛ, cetṛ, sotṛ (theorum/89's agents from the pinned roots): 88 forms equal to the exchanged paradigm",
            ],
            "NOT_claimed": [
                "kinship ṛ-stems (pitṛ: no 6.4.11 lengthening in 1p), naptṛ / svasṛ etc. of 6.4.11's list, neuter ṛ-stems; the stage order is a declared pipeline",
                "8.4.1's ṛ-varṇa extension is the vārttika's, cited",
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
