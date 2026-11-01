from __future__ import annotations

"""Exact certificate (theorum/107): KṚT ghañ / lyuṭ / ṇvul / śatṛ COMPILED — the
nominalisations bhāva, kāra, nāya, pāka, tyāga, yoga (ghañ 3.3.18 with 7.2.115 /
7.2.116, 7.3.86, 7.3.52), bhavana, nayana, karaṇa, gamana, pacana (lyuṭ 3.3.115
with 7.1.1 and 7.3.84 / 6.1.78, 8.4.2), kāraka, pācaka, nāyaka, bhāvaka, yojaka
(ṇvul 3.1.133 with 7.1.1) and the present participles bhavat, gacchat, nayat
(śatṛ 3.2.124 on theorum/58's present stem with 6.1.97); each rule shown
load-bearing on exactly the words it governs.

Quoted sūtras:
 3.1.91   dhātoḥ ; 3.1.93 kṛd atiṅ ; 1.2.46 kṛttaddhitasamāsāś ca
 3.3.18   bhāve                                            ghañ (3.3.16 padarujaviśaspṛśo ghañ: the affix ghañ)
 3.3.115  lyuṭ ca                                          lyuṭ (bhāve, napuṁsake)
 3.1.133  ṇvultṛcau                                        ṇvul (kartari 3.4.67)
 3.2.124  laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe        śatṛ in place of laṭ
 7.1.1    yuvor anākau                                     yu → ana, vu → aka
 7.2.115  aco ñṇiti ; 7.2.116 ata upadhāyāḥ                 ñit / ṇit vṛddhi
 7.3.52   cajoḥ ku ghiṇṇyatoḥ                               c / j → k / g before ghañ (ghit)
 7.3.84   sārvadhātukārdhadhātukayoḥ ; 7.3.86 pugantalaghūpadhasya ca ; 1.1.51 ur aṇ raparaḥ ; 6.1.78 eco 'yavāyāvaḥ
 8.4.2    aṭkupvāṅnumvyavāye 'pi (8.4.1)                     karaṇa
 3.1.68   kartari śap ; 3.4.113 tiṅśit sārvadhātukam ; 6.1.97 ato guṇe      śatṛ after śap
 1.3.2    upadeśe 'janunāsika it ; 1.3.3 halantyam ; 1.3.7 cuṭū ; 1.3.8 laśakv ataddhite ; 1.3.9 tasya lopaḥ

 T1  19 kṛt words.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.ghi_stem_sup_compiled import natva_8_4_2
from proof_lab.lan_parasmaipada_compiled import BHU, present_stem
from proof_lab.paninian_instruction_format import GUNA_SET, VRDDHI_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.paninian_seam_calculus import GAM, NI

SOURCES = {
    "3.1.91": "dhātoḥ", "3.1.93": "kṛd atiṅ", "1.2.46": "kṛttaddhitasamāsāś ca", "3.3.18": "bhāve", "3.3.16": "padarujaviśaspṛśo ghañ", "3.3.115": "lyuṭ ca",
    "3.1.133": "ṇvultṛcau", "3.4.67": "kartari kṛt", "3.2.124": "laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe", "7.1.1": "yuvor anākau",
    "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "7.3.52": "cajoḥ ku ghiṇṇyatoḥ", "7.3.84": "sārvadhātukārdhadhātukayoḥ", "7.3.86": "pugantalaghūpadhasya ca",
    "1.1.51": "ur aṇ raparaḥ", "6.1.78": "eco 'yavāyāvaḥ", "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade",
    "3.1.68": "kartari śap", "3.4.113": "tiṅśit sārvadhātukam", "6.1.97": "ato guṇe",
    "1.3.2": "upadeśe 'janunāsika it", "1.3.3": "halantyam", "1.3.7": "cuṭū", "1.3.8": "laśakv ataddhite", "1.3.9": "tasya lopaḥ",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
TO58 = {"a": "a", "ā": "A", "i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
FROM58 = {"A": "ā", "ai": "ai", "au": "au", "e": "e", "o": "o", "a": "a"}
AYADI = {"e": ("a", "y"), "o": ("a", "v"), "ai": ("ā", "y"), "au": ("ā", "v")}
KU = {"c": "k", "j": "g"}
ROOTS = {"bhū": ("bh", "ū"), "kṛ": ("k", "ṛ"), "nī": ("n", "ī"), "pac": ("p", "a", "c"), "tyaj": ("t", "y", "a", "j"), "yuj": ("y", "u", "j"), "gam": ("g", "a", "m")}
PRESENT = {"bhū": BHU, "gam": GAM, "nī": NI}
CASES = [  # (root, affix, expected)
    ("bhū", "ghañ", "bhāva"), ("kṛ", "ghañ", "kāra"), ("nī", "ghañ", "nāya"), ("pac", "ghañ", "pāka"), ("tyaj", "ghañ", "tyāga"), ("yuj", "ghañ", "yoga"),
    ("bhū", "lyuṭ", "bhavana"), ("nī", "lyuṭ", "nayana"), ("kṛ", "lyuṭ", "karaṇa"), ("gam", "lyuṭ", "gamana"), ("pac", "lyuṭ", "pacana"),
    ("kṛ", "ṇvul", "kāraka"), ("pac", "ṇvul", "pācaka"), ("nī", "ṇvul", "nāyaka"), ("bhū", "ṇvul", "bhāvaka"), ("yuj", "ṇvul", "yojaka"),
    ("bhū", "śatṛ~", "bhavat"), ("gam", "śatṛ~", "gacchat"), ("nī", "śatṛ~", "nayat"),
]
ALL_STAGES = ("7.1.1", "7.2.115", "7.2.116", "7.3.52", "7.3.84", "7.3.86", "1.1.51", "6.1.78", "8.4.2", "6.1.97")


def _vowel_sub(v: str, cands, on) -> list[str]:
    s = antaratama(TO58[v], cands)
    s = rapara_1_1_51(TO58[v], s) if "1.1.51" in on else s
    return [FROM58[s]] if s in FROM58 else [FROM58[s[0]], s[1]]


def krt(root: str, affix: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    a = its(affix, "pratyaya")
    aff = list(a["remaining_sounds"])
    marks = a["its"]
    path = [f"{root} + {affix} → {''.join(aff)} (its {marks}; kṛt 3.1.93; prātipadika 1.2.46)"]
    nit = "ṇ" in marks or "ñ" in marks
    ghit = "gh" in marks
    if affix == "śatṛ~":
        # sārvadhātuka (śit, 3.4.113): śap and theorum/58's present stem
        stem = list(present_stem(PRESENT[root]))
        stem = [c for s in stem for c in (("a", "v") if s == "av" else ("a", "y") if s == "ay" else (s,))]
        path.append(f"śatṛ for laṭ (3.2.124), śit → sārvadhātuka (3.4.113), śap (3.1.68): present stem {''.join(stem)} (theorum/58)")
        if stem[-1] == "a" and aff[0] == "a" and "6.1.97" in on:
            aff = aff[1:]; path.append("a + a → a (6.1.97 ato guṇe)")
        return "".join(stem + aff), path
    if "7.1.1" in on and aff[:2] in (["y", "u"], ["v", "u"]):
        new = ["a", "n", "a"] if aff[0] == "y" else ["a", "k", "a"]
        path.append(f"{''.join(aff[:2])} → {''.join(new)} (7.1.1 yuvor anākau)"); aff = new + aff[2:]
    st = list(ROOTS[root])
    if nit and st[-1] in VOWELS and "7.2.115" in on:
        st = st[:-1] + _vowel_sub(st[-1], VRDDHI_SET, on); path.append(f"final vowel → vṛddhi before the ñit / ṇit kṛt (7.2.115; 1.1.50" + ("; 1.1.51)" if root == "kṛ" else ")") + f": {''.join(st)}")
    elif nit and len(st) >= 2 and st[-2] == "a" and "7.2.116" in on:
        st[-2] = "ā"; path.append(f"penultimate a → ā before the ñit / ṇit kṛt (7.2.116): {''.join(st)}")
    elif st[-1] in ("ū", "ī", "ṛ") and "7.3.84" in on:
        st = st[:-1] + _vowel_sub(st[-1], GUNA_SET, on); path.append(f"final ik → guṇa before the ārdhadhātuka (7.3.84" + ("; 1.1.51)" if root == "kṛ" else ")") + f": {''.join(st)}")
    elif len(st) >= 2 and st[-2] in ("i", "u", "ṛ") and "7.3.86" in on:
        st = st[:-2] + _vowel_sub(st[-2], GUNA_SET, on) + st[-1:]; path.append(f"light penultimate ik → guṇa (7.3.86): {''.join(st)}")
    if st[-1] in AYADI and aff[0] in VOWELS and "6.1.78" in on:
        st = st[:-1] + list(AYADI[st[-1]]); path.append(f"ec → ay / av / āy / āv before the vowel (6.1.78): {''.join(st)}")
    if ghit and st[-1] in KU and "7.3.52" in on:
        st[-1] = KU[st[-1]]; path.append(f"c / j → ku before the ghit (7.3.52 cajoḥ ku ghiṇṇyatoḥ): {''.join(st)}")
    word = st + aff
    if "8.4.2" in on:
        word, fired = natva_8_4_2(word)
        if fired:
            path.append("n → ṇ after r across the aṭ (8.4.2; 8.4.1; theorum/91's ṇatva)")
    return "".join(word), path


def t1_krt() -> dict[str, Any]:
    forms = {e: krt(r, a)[0] for r, a, e in CASES}
    exp_breaks = {
        "7.1.1": {"bhavana", "nayana", "karaṇa", "gamana", "pacana", "kāraka", "pācaka", "nāyaka", "bhāvaka", "yojaka"},
        "7.2.115": {"bhāva", "kāra", "nāya", "kāraka", "nāyaka", "bhāvaka"}, "7.2.116": {"pāka", "tyāga", "pācaka"},
        "7.3.52": {"pāka", "tyāga", "yoga"}, "7.3.84": {"bhavana", "nayana", "karaṇa"}, "7.3.86": {"yoga", "yojaka"},
        "1.1.51": {"kāra", "karaṇa", "kāraka"}, "6.1.78": {"bhāva", "nāya", "nāyaka", "bhāvaka", "bhavana", "nayana"},
        "8.4.2": {"karaṇa"}, "6.1.97": {"bhavat", "gacchat", "nayat"},
    }
    broken = {s: sorted(e for r, a, e in CASES if krt(r, a, tuple(x for x in ALL_STAGES if x != s))[0] != e) for s in exp_breaks}
    checks = {"nineteen_krt_words_equal_the_classical_forms": all(forms[e] == e for e in forms)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {e: krt(r, a)[1] for r, a, e in CASES}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_krt": t1_krt()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_KRT_GHAN_LYUT_NVUL_SATR_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_KRT_GHAN_LYUT_NVUL_SATR_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.krt_ghan_lyut_nvul_satr_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "19 kṛt words — six ghañ, five lyuṭ, five ṇvul, three śatṛ — by the quoted vidhi sūtras with 7.1.1, 7.2.115, 7.2.116, 7.3.52, 7.3.84, 7.3.86, 1.1.51, 6.1.78, 8.4.2, 6.1.97; each rule breaks exactly the words stated",
            ],
            "NOT_claimed": [
                "the choice of affix per word is declared from the sense sūtra (bhāve / kartari); the śatṛ stems rest on theorum/58's present stem (bhū, gam, nī only)",
                "declension of the kṛt words (a-stems: theorum/63; at-stems with num 7.1.70: not claimed), the feminine of śatṛ, ghañ exceptions (7.3.53–59), the accent",
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
