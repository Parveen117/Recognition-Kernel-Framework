from __future__ import annotations

"""Exact certificate (theorum/124): yuṣmad AND asmad DECLINED — the two personal
pronouns, 21 cells each, by the substitution block 7.2.86–7.2.97 on the stem
(ā before non-ādeśa endings and in the 2nd case, ya before vowels, the
maparyanta substitutes tva / ma, yuva / āva, yūya / vaya, tvā / aha, tubhya /
mahya, tava / mama, lopa of the rest) and the ending block 7.1.27–7.1.33 (ṅas →
aś, ṅe and the 1st / 2nd endings → am, śas → n, bhyas → bhyam / at, ṅasi → at,
ām → ākam), with 6.1.107 and 6.1.97; each rule shown load-bearing on exactly
its cells.

Quoted sūtras:
 7.2.86  yuṣmadasmador anādeśe       the final (ad) → ā before an ending that is not an ādeśa (bhyām, bhis, su …)
 7.2.87  dvitīyāyāṁ ca              … and before the 2nd-case endings (tvām, yuṣmān)
 7.2.88  prathamāyāś ca dvivacane bhāṣāyām   … and before the 1st dual (yuvām, āvām)
 7.2.89  yo 'ci                      → y before a non-ādeśa vowel-initial ending (tvayā, mayi, yuvayoḥ; anādeśe continues)
 7.2.90  śeṣe lopaḥ                  elsewhere the final is dropped (tvam, tava, yuṣmabhyam)
 7.2.91  maparyantasya               the substitutes below replace the part up to m
 7.2.92  yuvāvau dvivacane ; 7.2.93 yūyavayau jasi ; 7.2.94 tvāhau sau ; 7.2.95 tubhyamahyau ṅayi ; 7.2.96 tavamamau ṅasi ; 7.2.97 tvamāv ekavacane
 7.1.27  yuṣmadasmadbhyāṁ ṅaso 'ś ; 7.1.28 ṅe prathamayor am ; 7.1.29 śaso na ; 7.1.30 bhyaso bhyam ; 7.1.31 pañcamyā at ; 7.1.32 ekavacanasya ca ; 7.1.33 sāma ākam
 6.1.107 ami pūrvaḥ ; 6.1.101 akaḥ savarṇe dīrghaḥ ; 6.1.97 ato guṇe (the pararūpa of the substitute's a with the a of ad: tva + ad → tvad) ; 1.1.52 alo 'ntyasya ; 1.3.8 (ś of aś) ; 1.1.27 sarvādīni sarvanāmāni (yuṣmad, asmad are sarvanāma)

 T1  tvam … yuṣmāsu ; aham … asmāsu — 42 cells.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "7.2.86": "yuṣmadasmador anādeśe", "7.2.87": "dvitīyāyāṁ ca", "7.2.88": "prathamāyāś ca dvivacane bhāṣāyām", "7.2.89": "yo 'ci", "7.2.90": "śeṣe lopaḥ",
    "7.2.91": "maparyantasya", "7.2.92": "yuvāvau dvivacane", "7.2.93": "yūyavayau jasi", "7.2.94": "tvāhau sau", "7.2.95": "tubhyamahyau ṅayi", "7.2.96": "tavamamau ṅasi",
    "7.2.97": "tvamāv ekavacane", "7.1.27": "yuṣmadasmadbhyāṁ ṅaso 'ś", "7.1.28": "ṅe prathamayor am", "7.1.29": "śaso na", "7.1.30": "bhyaso bhyam", "7.1.31": "pañcamyā at",
    "7.1.32": "ekavacanasya ca", "7.1.33": "sāma ākam", "6.1.107": "ami pūrvaḥ", "6.1.101": "akaḥ savarṇe dīrghaḥ", "6.1.97": "ato guṇe", "1.1.52": "alo 'ntyasya", "1.3.8": "laśakv ataddhite", "1.1.27": "sarvādīni sarvanāmāni",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"), ("7s", "ṅi"), ("7d", "os"), ("7p", "sup")]
STEM = {"yuṣmad": ["y", "u", "ṣ", "m", "a", "d"], "asmad": ["a", "s", "m", "a", "d"]}
MAPARYANTA = {  # 7.2.91: the substitute replaces the part of the stem up to and including m
    "yuṣmad": {"dual": "yuva", "jas": "yūya", "su": "tva", "ṅe": "tubhya", "ṅas": "tava", "sg": "tva"},
    "asmad": {"dual": "āva", "jas": "vaya", "su": "aha", "ṅe": "mahya", "ṅas": "mama", "sg": "ma"},
}
ORACLE = {
    "yuṣmad": {"1s": "tvam", "1d": "yuvām", "1p": "yūyam", "2s": "tvām", "2d": "yuvām", "2p": "yuṣmān", "3s": "tvayā", "3d": "yuvābhyām", "3p": "yuṣmābhiḥ",
               "4s": "tubhyam", "4d": "yuvābhyām", "4p": "yuṣmabhyam", "5s": "tvat", "5d": "yuvābhyām", "5p": "yuṣmat", "6s": "tava", "6d": "yuvayoḥ", "6p": "yuṣmākam",
               "7s": "tvayi", "7d": "yuvayoḥ", "7p": "yuṣmāsu"},
    "asmad": {"1s": "aham", "1d": "āvām", "1p": "vayam", "2s": "mām", "2d": "āvām", "2p": "asmān", "3s": "mayā", "3d": "āvābhyām", "3p": "asmābhiḥ",
              "4s": "mahyam", "4d": "āvābhyām", "4p": "asmabhyam", "5s": "mat", "5d": "āvābhyām", "5p": "asmat", "6s": "mama", "6d": "āvayoḥ", "6p": "asmākam",
              "7s": "mayi", "7d": "āvayoḥ", "7p": "asmāsu"},
}
ALL_STAGES = ("7.2.92", "7.2.93", "7.2.94", "7.2.95", "7.2.96", "7.2.97", "7.1.27", "7.1.28", "7.1.29", "7.1.30", "7.1.31", "7.1.32", "7.1.33", "7.2.86", "7.2.87", "7.2.88", "7.2.89", "7.2.90", "6.1.107", "6.1.101", "6.1.97", "8.2.66", "8.3.15")


def decline(name: str, code: str, up: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = list(STEM[name]); path = [f"{name} + {up} (sarvanāma 1.1.27)"]
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    num = code[1]; case = code[0]
    # ending substitutions (7.1.27–33); each marks the ending as an ādeśa
    adesa = False
    if up == "ṅas" and "7.1.27" in on:
        aff = ["a"]; adesa = True; path.append("ṅas → aś (7.1.27; ś it 1.3.8 → a)")
    if (up == "ṅe" or case in ("1", "2")) and up != "śas" and "7.1.28" in on:
        aff = ["a", "m"]; adesa = True; path.append(f"{up} → am (7.1.28 ṅe prathamayor am)")
    if up == "śas" and "7.1.29" in on:
        aff = ["n"]; adesa = True; path.append("śas → n (7.1.29 śaso na)")
    if up == "bhyas" and case == "4" and "7.1.30" in on:
        aff = ["bh", "y", "a", "m"]; adesa = True; path.append("bhyas → bhyam (7.1.30)")
    if up == "bhyas" and case == "5" and "7.1.31" in on:
        aff = ["a", "t"]; adesa = True; path.append("bhyas of the 5th → at (7.1.31 pañcamyā at)")
    if up == "ṅasi~" and "7.1.32" in on:
        aff = ["a", "t"]; adesa = True; path.append("ṅasi → at (7.1.32 ekavacanasya ca)")
    if up == "ām" and "7.1.33" in on:
        aff = ["ā", "k", "a", "m"]; adesa = True; path.append("ām → ākam (7.1.33 sāma ākam)")
    # maparyanta substitutions (7.2.91–97)
    m = MAPARYANTA[name]
    k = st.index("m") + 1
    sub = None
    if num == "d" and "7.2.92" in on:
        sub = (m["dual"], "7.2.92 yuvāvau dvivacane")
    elif up == "jas" and "7.2.93" in on:
        sub = (m["jas"], "7.2.93 yūyavayau jasi")
    elif up == "su~" and "7.2.94" in on:
        sub = (m["su"], "7.2.94 tvāhau sau")
    elif up == "ṅe" and "7.2.95" in on:
        sub = (m["ṅe"], "7.2.95 tubhyamahyau ṅayi")
    elif up == "ṅas" and "7.2.96" in on:
        sub = (m["ṅas"], "7.2.96 tavamamau ṅasi")
    elif num == "s" and "7.2.97" in on:
        sub = (m["sg"], "7.2.97 tvamāv ekavacane")
    if sub:
        st = list(sub[0]) + st[k:]; path.append(f"the part up to m → {sub[0]} ({sub[1]}; 7.2.91 maparyantasya): {''.join(st)}")
        if st[-3:-1] == ["a", "a"] and "6.1.97" in on:
            st = st[:-2] + st[-1:]; path.append(f"the substitute's a + the a of ad → a (6.1.97 ato guṇe, pararūpa of the non-pada-final a): {''.join(st)}")
    # the final ad (7.2.86–90): ā / ya / lopa
    if st[-1] == "d":
        if case == "2" and "7.2.87" in on:
            st[-1] = "ā"; path.append("final → ā before the 2nd-case ending (7.2.87 dvitīyāyāṁ ca; 1.1.52)")
        elif case == "1" and num == "d" and "7.2.88" in on:
            st[-1] = "ā"; path.append("final → ā before the 1st dual (7.2.88 prathamāyāś ca dvivacane bhāṣāyām)")
        elif not adesa and aff and aff[0] in VOWELS and "7.2.89" in on:
            st[-1] = "y"; path.append("final → y before the non-ādeśa vowel-initial ending (7.2.89 yo 'ci, anādeśe continuing from 7.2.86; the a of ya uccāraṇārtha, 1.1.52)")
        elif not adesa and "7.2.86" in on:
            st[-1] = "ā"; path.append("final → ā before the non-ādeśa ending (7.2.86 yuṣmadasmador anādeśe)")
        elif "7.2.90" in on:
            st = st[:-1]; path.append("final dropped (7.2.90 śeṣe lopaḥ)")
    # sandhi at the junction
    if st[-2:] == ["a", "ā"] and "6.1.101" in on:
        st = st[:-2] + ["ā"]; path.append("a + ā → ā (6.1.101 akaḥ savarṇe dīrghaḥ)")
    word = st + aff
    if st[-1] == "ā" and aff[:2] == ["a", "m"] and "6.1.107" in on:
        word = st + aff[1:]; path.append("ā + am → ām (6.1.107 ami pūrvaḥ)")
    elif st[-1] == "a" and aff and aff[0] == "ā" and "6.1.101" in on:
        word = st[:-1] + aff; path.append("a + ā → ā (6.1.101)")
    elif st[-1] == "a" and aff and aff[0] == "a" and "6.1.97" in on:
        word = st + aff[1:]; path.append("a + a → a (6.1.97 ato guṇe)")
    if word[-1] == "s" and "8.2.66" in on:
        word[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word), path


def paradigm(name: str, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(name, c, up, stages)[0] for c, up in SUP}


def t1_pronouns() -> dict[str, Any]:
    forms = {n: paradigm(n) for n in STEM}
    both = lambda cs: {f"{n}.{c}" for n in STEM for c in cs}
    exp_breaks = {
        "7.2.92": both(["1d", "2d", "3d", "4d", "5d", "6d", "7d"]), "7.2.93": both(["1p"]), "7.2.94": {"asmad.1s"}, "7.2.95": both(["4s"]), "7.2.96": both(["6s"]),
        "7.2.97": both(["2s", "3s", "5s", "7s"]), "7.1.27": both(["6s"]), "7.1.28": both(["1s", "1d", "1p", "2d", "4s"]), "7.1.29": both(["2p"]), "7.1.30": both(["4p"]),
        "7.1.31": both(["5p"]), "7.1.32": both(["5s"]), "7.1.33": both(["6p"]), "7.2.86": both(["3d", "3p", "4d", "5d", "7p"]), "7.2.87": both(["2s", "2d", "2p"]), "7.2.88": both(["1d"]),
        "7.2.89": both(["3s", "6d", "7s", "7d"]), "7.2.90": both(["1s", "1p", "4s", "4p", "5s", "5p", "6s", "6p"]), "6.1.107": both(["1d", "2s", "2d"]), "6.1.97": both([c for c, _ in SUP if c not in ("2p", "3p", "4p", "6p", "7p")]),
        "8.2.66": both(["3p", "6d", "7d"]), "8.3.15": both(["3p", "6d", "7d"]),
    }
    broken = {s: sorted(f"{n}.{c}" for n in STEM for c, _ in SUP if paradigm(n, tuple(x for x in ALL_STAGES if x != s))[c] != ORACLE[n][c]) for s in exp_breaks}
    checks = {"forty_two_cells_equal_the_classical_paradigms": all(forms[n][c] == ORACLE[n][c] for n in STEM for c, _ in SUP)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {f"{n}.{c}": decline(n, c, dict(SUP)[c])[1] for n in STEM for c in ("1s", "2s", "3s", "6s", "6p")}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_pronouns": t1_pronouns()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_YUSMAD_ASMAD_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_YUSMAD_ASMAD_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.yusmad_asmad_sup_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": ["yuṣmad and asmad declined, 21 cells each (42 forms), by 7.2.86–7.2.97 (the maparyanta substitutes and the ā / ya / lopa of the final) and 7.1.27–7.1.33 (the ending substitutes) with 6.1.107, 6.1.97, 8.2.66 / 8.3.15; twenty-two ablations each break exactly the cells stated; 7.2.94 is surface-neutral on yuṣmad (its tva coincides with 7.2.97's) and load-bearing on asmad's aham — recorded"],
            "NOT_claimed": ["the enclitic forms of anvādeśa (8.1.20–8.1.23: vām, nau, te, me, vaḥ, naḥ), the Vedic 1st dual without 7.2.88's bhāṣāyām, 7.2.98 pratyayottarapadayoś ca (yuṣmadīya, tvadīya, madīya), the accent", "RH, YM untouched"],
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
