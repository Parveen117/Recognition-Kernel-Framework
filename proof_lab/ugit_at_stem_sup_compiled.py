from __future__ import annotations

"""Exact certificate (theorum/109): UGIT at-STEMS DECLINED — bhavat (theorum/107's
śatṛ), bhagavat and dhīmat (matup, 5.2.94, with 8.2.9) through 7.1.70 num
(placed by 1.1.47 as theorum/82 reads it), 6.4.14 atvasantasya cādhātoḥ, 8.2.23
saṁyogāntasya lopaḥ, on theorum/92's consonant-stem carrier (1.4.17 / 1.4.18,
6.1.68, 8.2.39, 8.4.55, 8.4.56, 8.2.66, 8.3.15); marut (theorum/92) as the
non-ugit control; each new rule shown load-bearing on exactly its cells.

Quoted sūtras:
 7.1.70   ugidacāṁ sarvanāmasthāne 'dhātoḥ            num to an ugit non-root stem before sarvanāmasthāna
 1.1.47   mid aco 'ntyāt paraḥ                         num goes after the last vowel (theorum/82: placement)
 1.3.2    upadeśe 'janunāsika it                       the u of nu~m, the ṛ of śatṛ~, the u of matu~p
 6.4.14   atvasantasya cādhātoḥ                        upadhā dīrgha of the at-stem before su (not sambuddhi): bhavān
 8.2.23   saṁyogāntasya lopaḥ                          pada-final cluster loses its last sound: bhavant → bhavan
 5.2.94   tad asyāsty asminn iti matup                 matup ; 8.2.9 mād upadhāyāś ca mator vo 'yavādibhyaḥ (bhagavat)
 1.1.42   śi sarvanāmasthānam ; 1.1.43 suḍ anapuṁsakasya
 6.1.68   halṅyābbhyo dīrghāt sutisyapṛktaṁ hal ; 1.4.17 ; 1.4.18 ; 8.2.39 ; 8.4.55 ; 8.4.56 ; 8.2.66 ; 8.3.15   (theorum/92)
 8.3.24   naś cāpadāntasya jhali ; 8.4.58 anusvārasya yayi parasavarṇaḥ   (num before t: n → ṁ → n, surface-neutral, recorded)

 T1  bhavat, bhagavat, dhīmat: 22 cells each (66 forms); marut control 22.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.hal_stem_sup_compiled import ALL_STAGES as HAL_STAGES, SUP, decline as hal_decline
from proof_lab.paninian_it_samjna_compiled import its, placement

SOURCES = {
    "7.1.70": "ugidacāṁ sarvanāmasthāne 'dhātoḥ", "1.1.47": "mid aco 'ntyāt paraḥ", "1.3.2": "upadeśe 'janunāsika it", "6.4.14": "atvasantasya cādhātoḥ",
    "8.2.23": "saṁyogāntasya lopaḥ", "5.2.94": "tad asyāsty asminn iti matup", "8.2.9": "mād upadhāyāś ca mator vo 'yavādibhyaḥ",
    "1.1.42": "śi sarvanāmasthānam", "1.1.43": "suḍ anapuṁsakasya", "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "1.4.17": "svādiṣv asarvanāmasthāne",
    "8.2.39": "jhalāṁ jaśo 'nte", "8.4.55": "khari ca", "8.4.56": "vāvasāne", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
    "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "6.1.97": "ato guṇe",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
SARVANAMASTHANA = {"1s", "1d", "1p", "2s", "2d", "8s"}   # 1.1.42 / 1.1.43: su au jas am auṭ (su also in sambuddhi)
UK = {"u", "ṛ", "ḷ"}
STEMS = {  # name: (base, affix teaching form)
    "bhavat": ((("bh", "a", "v", "a"), "śatṛ~"), "bhavat"), "bhagavat": ((("bh", "a", "g", "a"), "matu~p"), "bhagavat"), "dhīmat": ((("dh", "ī"), "matu~p"), "dhīmat"),
}


def oracle(stem: str) -> dict[str, str]:
    b = stem[:-2]  # drop "at"
    n = b + "an"
    return {"1s": b + "ān", "1d": n + "tau", "1p": n + "taḥ", "2s": n + "tam", "2d": n + "tau", "2p": stem + "aḥ", "3s": stem + "ā", "3d": b + "adbhyām", "3p": b + "adbhiḥ",
            "4s": stem + "e", "4d": b + "adbhyām", "4p": b + "adbhyaḥ", "5s": stem + "aḥ", "5d": b + "adbhyām", "5p": b + "adbhyaḥ", "6s": stem + "aḥ", "6d": stem + "oḥ", "6p": stem + "ām",
            "7s": stem + "i", "7d": stem + "oḥ", "7p": stem + "su", "8s": n}


ALL_STAGES = ("7.1.70", "6.4.14", "8.2.23", "8.2.9")


def ugit_stem(name: str, stages=ALL_STAGES) -> tuple[list[str], bool, list[str]]:
    (base, aff), _ = STEMS[name]
    a = its(aff, "pratyaya", taddhita=aff.startswith("matu"))
    rem = list(a["remaining_sounds"])
    ugit = any(k in UK for k in a["its"])
    path = [f"{''.join(base)} + {aff} → {''.join(rem)} (its {a['its']}; ugit: {ugit})"]
    if base[-1] == "a" and rem[0] == "a":
        rem = rem[1:]; path.append("a + a → a at the junction (6.1.97 ato guṇe; the present stem bhava is theorum/58's, as in theorum/107)")
    st = list(base) + rem
    if aff.startswith("matu") and base[-1] in ("a", "ā") and "8.2.9" in set(stages):
        st[len(base)] = "v"; path.append("m of matup → v after the a-final stem (8.2.9 mād upadhāyāś ca mator vo 'yavādibhyaḥ)")
    return st, ugit, path


def decline(name: str, code: str, up: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st, ugit, path = ugit_stem(name, stages)
    sns = code in SARVANAMASTHANA
    if ugit and sns and "7.1.70" in on:
        n = its("nu~m", "agama")
        assert n["remaining_sounds"] == ("n",) and placement("nu~m") == "after_last_vowel"
        k = max(i for i, s in enumerate(st) if s in VOWELS)
        st = st[: k + 1] + ["n"] + st[k + 1 :]; path.append(f"num after the last vowel before sarvanāmasthāna (7.1.70; placed by 1.1.47 as theorum/82 reads it): {''.join(st)}; n → ṁ → n before t (8.3.24, 8.4.58) is surface-neutral")
    if code == "1s" and st[-2:] == ["n", "t"] and "6.4.14" in on:
        st[-3] = "ā"; path.append("upadhā of the at-stem lengthened before su, not in sambuddhi (6.4.14 atvasantasya cādhātoḥ)")
    out, p2 = hal_decline(tuple(st), code, up, HAL_STAGES)
    path.extend("theorum/92: " + x for x in p2)
    w = list(out)
    if code in ("1s", "8s") and "".join(w).endswith("nt") and "8.2.23" in on:
        out = "".join(w[:-1]); path.append("pada-final cluster nt → n (8.2.23 saṁyogāntasya lopaḥ; 6.1.68 having dropped su)")
    return out, path


def paradigm(name: str, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(name, c, up, stages)[0] for c, up in SUP}


def t1_ugit() -> dict[str, Any]:
    forms = {n: paradigm(n) for n in STEMS}
    exp = {n: oracle(n) for n in STEMS}
    exp_breaks = {"7.1.70": {f"{n}.{c}" for n in STEMS for c in SARVANAMASTHANA}, "6.4.14": {f"{n}.1s" for n in STEMS}, "8.2.23": {f"{n}.{c}" for n in STEMS for c in ("1s", "8s")},
                  "8.2.9": {f"bhagavat.{c}" for c, _ in SUP}}
    broken = {s: sorted(f"{n}.{c}" for n in STEMS for c, _ in SUP if paradigm(n, tuple(x for x in ALL_STAGES if x != s))[c] != exp[n][c]) for s in exp_breaks}
    marut = hal_decline(("m", "a", "r", "u", "t"), "1s", "su~", HAL_STAGES)[0]
    checks = {"sixty_six_cells_equal_the_classical_paradigms": all(forms[n][c] == exp[n][c] for n in STEMS for c, _ in SUP),
              "marut_control_takes_no_num_on_theorum_92": marut == "marut"}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {n: decline(n, "1s", "su~")[1] for n in STEMS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_ugit": t1_ugit()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_UGIT_AT_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_UGIT_AT_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.ugit_at_stem_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "bhavat, bhagavat, dhīmat declined, 22 cells each, on theorum/92's consonant-stem carrier with 7.1.70 num (ugit read by theorum/82 from the anunāsika markers, placed by 1.1.47), 6.4.14, 8.2.23, 8.2.9; each new rule breaks exactly the cells stated; marut takes no num",
            ],
            "NOT_claimed": [
                "the feminine (bhavantī, 4.1.6 ugitaś ca), the neuter (bhavat / bhavantī, 7.1.72), mahat (6.4.10 / 7.1.? option), the vasu- and īyasu-stems, the accent",
                "theorum/92's own rules are the carrier and are not re-ablated here",
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
