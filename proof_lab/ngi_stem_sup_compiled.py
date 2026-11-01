from __future__ import annotations

"""Exact certificate (theorum/89): THE NADĪ (ṅī-STEM) SUP PARADIGM COMPILED —
nadī and the ṅīp agent nouns kartrī, śrotrī, hotrī, cetrī, sotrī built from
the pinned Dhātupāṭha roots with tṛc (theorum/82) and the guṇa of theorum/80.

Quoted sūtras:
 1.4.3    yū stryākhyau nadī                  a feminine stem in ī / ū is called nadī
 4.1.5    ṛnnebhyo ṅīp                        ṅīp after ṛ-final and n-final stems (feminine)
 3.1.133  ṇvultṛcau                           the affixes ṇvul and tṛc (agent)
 3.4.114  ārdhadhātukaṁ śeṣaḥ                 the remaining (non-sārvadhātuka) affixes after a dhātu are ārdhadhātuka
 7.3.84   sārvadhātukārdhadhātukayoḥ          guṇa of an ik-final aṅga before them (theorum/80 compiled)
 1.1.51   ur aṇ raparaḥ                        (theorum/80)
 6.1.64   dhātvādeḥ ṣaḥ saḥ                   (theorum/86)
 7.3.112  āṇ nadyāḥ                            a ṅit sup after nadī takes the augment āṭ
 7.3.116  ṅer ām nadyāmnībhyaḥ ; 7.1.54 hrasvanadyāpo nuṭ ; 6.1.68 (su drops after ṅī) ; 6.1.69
 7.3.107  ambārthanadyor hrasvaḥ               nadī is shortened in the sambuddhi
 6.1.77   iko yaṇ aci                          ī + vowel → y
 6.1.102  prathamayoḥ pūrvasavarṇaḥ            in the first two cases, ak + ac → the long savarṇa of the prior (jas / śas)
 6.1.105  dīrghāj jasi ca                      but not jas after a long vowel (so nadyaḥ, by 6.1.77)
 6.1.107  ami pūrvaḥ ; 6.1.88 vṛddhir eci ; 6.1.101 akaḥ savarṇe dīrghaḥ
 8.3.57   iṇkoḥ ; 8.3.59 ādeśapratyayayoḥ       s of an affix → ṣ after iṇ / ku
 8.2.66 ; 8.3.15 ; 1.1.46 ; 1.1.56 ; 1.3.2–1.3.9

 T1  nadī's 22 forms equal the classical paradigm; each stage breaks exactly
     its own cells (7.3.112 on 4s/5s/6s only — on 7s the āṭ collapses into
     ām by 6.1.101, so there it is redundant; 7.3.116, 7.1.54, 7.3.107,
     6.1.68, 6.1.69, 6.1.105, 8.3.59).
 T2  kṛ, śru, hu, ci, ṣu (pinned entries) + tṛc → kartṛ, śrotṛ, hotṛ, cetṛ,
     sotṛ by theorum/80's guṇa with 1.1.51 and theorum/86's 6.1.64; + ṅīp →
     kartrī … sotrī by 6.1.77; each is nadī (1.4.3) and declines as nadī:
     5 × 22 = 110 forms.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.nirukta_dhatupatha_nama import load_entries, upadesa_iast
from proof_lab.paninian_instruction_format import BASE, GUNA_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "1.4.3": "yū stryākhyau nadī", "4.1.5": "ṛnnebhyo ṅīp", "3.1.133": "ṇvultṛcau", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "7.3.84": "sārvadhātukārdhadhātukayoḥ",
    "1.1.51": "ur aṇ raparaḥ", "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "7.3.112": "āṇ nadyāḥ", "7.3.116": "ṅer ām nadyāmnībhyaḥ", "7.1.54": "hrasvanadyāpo nuṭ",
    "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "6.1.69": "eṅhrasvāt sambuddheḥ", "7.3.107": "ambārthanadyor hrasvaḥ", "6.1.77": "iko yaṇ aci",
    "6.1.102": "prathamayoḥ pūrvasavarṇaḥ", "6.1.105": "dīrghāj jasi ca", "6.1.107": "ami pūrvaḥ", "6.1.88": "vṛddhir eci", "6.1.101": "akaḥ savarṇe dīrghaḥ",
    "8.3.57": "iṇkoḥ", "8.3.59": "ādeśapratyayayoḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
IK_TO_58 = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R", "ḷ": "L"}
FROM_58 = {"ar": "ar", "e": "e", "o": "o", "al": "al"}
NADI_ORACLE = {"1s": "nadī", "1d": "nadyau", "1p": "nadyaḥ", "2s": "nadīm", "2d": "nadyau", "2p": "nadīḥ", "3s": "nadyā", "3d": "nadībhyām", "3p": "nadībhiḥ",
               "4s": "nadyai", "4d": "nadībhyām", "4p": "nadībhyaḥ", "5s": "nadyāḥ", "5d": "nadībhyām", "5p": "nadībhyaḥ", "6s": "nadyāḥ", "6d": "nadyoḥ",
               "6p": "nadīnām", "7s": "nadyām", "7d": "nadyoḥ", "7p": "nadīṣu", "8s": "nadi"}
ALL_STAGES = ("7.3.116", "7.3.112", "7.1.54", "7.3.107", "6.1.68", "6.1.69", "6.1.105", "sandhi", "8.3.59", "8.2.66", "8.3.15")


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    ngit = "ṅ" in r["its"]
    st = list(stem)
    path = [f"{upadesa} → {''.join(aff)}"]
    samb = code == "8s"
    if "7.3.116" in on and code == "7s":
        aff = ["ā", "m"]; path.append("ṅi → ām (7.3.116; ṅit retained 1.1.56)")
    if "7.3.112" in on and ngit:
        aff = ["ā"] + aff; path.append("āṭ prefixed (7.3.112; 1.1.46)")
    if "7.1.54" in on and code == "6p":
        aff = list(its("nu~ṭ", "agama")["remaining_sounds"]) + aff; path.append("nuṭ prefixed (7.1.54)")
    if "7.3.107" in on and samb:
        st[-1] = "i"; path.append("ī → i in the sambuddhi (7.3.107)")
    if code == "1s" and "6.1.68" in on and st[-1] == "ī" and aff == ["s"]:
        aff = []; path.append("su dropped after ṅī (6.1.68)")
    if samb and "6.1.69" in on and st[-1] == "i" and aff == ["s"]:
        aff = []; path.append("su of the sambuddhi dropped after the short vowel (6.1.69)")
    # inside the augmented affix: ā + e → ai, ā + a → ā
    if aff[:1] == ["ā"] and len(aff) > 1 and aff[1] in VOWELS:
        if aff[1] == "e":
            aff = ["ai"] + aff[2:]; path.append("ā + e → ai (6.1.88)")
        elif aff[1] in ("a", "ā"):
            aff = ["ā"] + aff[2:]; path.append("ā + a → ā (6.1.101)")
    if "sandhi" in on and aff and aff[0] in VOWELS and st[-1] == "ī":
        b = aff[0]
        if code == "2s":
            aff = aff[1:]; path.append("ī + am → īm (6.1.107 ami pūrvaḥ)")
        elif code == "2p":
            aff = aff[1:]; path.append("ī + as → īs (6.1.102 pūrvasavarṇa)")
        elif code == "1p" and "6.1.105" not in on:
            aff = aff[1:]; path.append("ī + as → īs (6.1.102; 6.1.105 absent)")
        else:
            st[-1] = "y"; path.append(f"ī + {b} → y{b} (6.1.77" + ("; 6.1.105 blocks 6.1.102 for jas" if code == "1p" else "") + ")")
    word = st + aff
    if "8.3.59" in on and code == "7p" and word[-2] in ("i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au") and word[-1] == "s" and aff and aff[0] == "s":
        pass
    if "8.3.59" in on and code == "7p" and "".join(aff) == "su" and st[-1] in ("i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au"):
        word = st + ["ṣ", "u"]; path.append("s → ṣ after iṇ (8.3.59, 8.3.57)")
    if word and word[-1] == "s":
        if "8.2.66" in on:
            word[-1] = "r"; path.append("s → ru (8.2.66)")
            if "8.3.15" in on:
                word[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word), path


def paradigm(stem, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(stem, c, up, stages)[0] for c, up in SUP}


def t1_nadi() -> dict[str, Any]:
    stem = ("n", "a", "d", "ī")
    forms = paradigm(stem)
    # on 7s, āṭ + ām collapses to ām (6.1.101): 7.3.112 is redundant there — recorded.
    # (The first pinned run had this comment inline, which swallowed five entries of the table: external review found it; repaired.)
    expected_breaks = {"7.3.112": {"4s", "5s", "6s"}, "7.3.116": {"7s"}, "7.1.54": {"6p"}, "7.3.107": {"8s"}, "6.1.68": {"1s"}, "6.1.69": {"8s"},
                       "6.1.105": {"1p"}, "8.3.59": {"7p"}}
    broken = {}
    for s in expected_breaks:
        f = paradigm(stem, tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in NADI_ORACLE if f[c] != NADI_ORACLE[c])
    checks = {"nadi_22_forms_equal_the_classical_paradigm": forms == NADI_ORACLE}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {c: decline(stem, c, up)[1] for c, up in SUP}, "broken_cells": broken}


AGENTS = {"1080010": "kartṛ", "1011092": "śrotṛ", "1030001": "hotṛ", "1050005": "cetṛ", "1050001": "sotṛ"}   # aniṭ before tṛc (declared)


def trc_agent(lex: str, entries: dict) -> dict[str, Any]:
    """Admitted (aniṭ-declared) entries only: any other id is refused here (guard added after external review)."""
    if lex not in AGENTS:
        raise ValueError(f"{lex}: not an admitted tṛc entry of theorum/89 (aniṭ before tṛc is declared only for {sorted(AGENTS)})")
    up = upadesa_iast(entries[lex]["aupadeshik"])
    dh = list(its(up, "dhatu")["remaining_sounds"])
    steps = [f"{entries[lex]['aupadeshik']} → {''.join(dh)}"]
    if dh[0] == "ṣ":
        dh[0] = "s"; steps.append("ṣ → s (6.1.64)")
    aff = list(its("tṛc", "pratyaya")["remaining_sounds"])      # tṛ (c it)
    steps.append("tṛc → tṛ (1.3.3); ārdhadhātuka (3.4.114)")
    if dh[-1] in IK_TO_58:
        g = rapara_1_1_51(BASE[IK_TO_58[dh[-1]]], antaratama(IK_TO_58[dh[-1]], GUNA_SET))   # theorum/80: 1.1.50 + 1.1.51
        dh = dh[:-1] + list(g)
        steps.append(f"guṇa of the ik-final aṅga before the ārdhadhātuka (7.3.84; antaratama 1.1.50, 1.1.51) → {''.join(dh)}")
    agent = dh + aff
    steps.append(f"agent noun {''.join(agent)} (3.1.133)")
    nip = list(its("ṅīp", "pratyaya")["remaining_sounds"])      # ī
    fem = agent[:-1] + ["r"] + nip                                # ṛ + ī → rī (6.1.77)
    steps.append(f"+ ṅīp (4.1.5): ṛ + ī → rī (6.1.77) → {''.join(fem)}; nadī (1.4.3)")
    return {"agent": "".join(agent), "feminine": "".join(fem), "sounds": tuple(fem), "steps": steps}


def t2_agent_feminines() -> dict[str, Any]:
    entries = load_entries()
    out, ok_agents, ok_forms, n = {}, True, True, 0
    for lex, exp in AGENTS.items():
        a = trc_agent(lex, entries)
        ok_agents &= a["agent"] == exp
        forms = paradigm(a["sounds"])
        pref = "".join(a["sounds"][:-1])
        for c, f in forms.items():
            ok_forms &= f == pref + NADI_ORACLE[c][3:]
            n += 1
        out[a["feminine"]] = {"steps": a["steps"], "forms": forms}
    checks = {"kartr_srotr_hotr_cetr_sotr_by_guna_and_rapara": ok_agents, "five_nip_feminines_110_forms_equal_the_exchanged_nadi_paradigm": ok_forms and n == 110}
    return {"checks": checks, **out}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_nadi": t1_nadi(), "t2_agent_feminines": t2_agent_feminines()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NGI_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_NGI_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.ngi_stem_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "nadī's 22 forms from the teaching forms through 7.3.112, 7.3.116, 7.1.54, 7.3.107, 6.1.68, 6.1.69, 6.1.77, 6.1.102 / 6.1.105, 6.1.107, 6.1.88, 6.1.101, 8.3.59, 8.2.66, 8.3.15; each stage breaks exactly its own cells",
                "kṛ, śru, hu, ci, ṣu (pinned entries) + tṛc → kartṛ, śrotṛ, hotṛ, cetṛ, sotṛ by theorum/80's guṇa with 1.1.51 and 6.1.64; + ṅīp → kartrī … sotrī; 110 forms equal the exchanged nadī paradigm",
            ],
            "NOT_claimed": [
                "aniṭ before tṛc is declared (bhū, pū, lū, tan take iṭ and are not fed)",
                "the stage order is a declared pipeline; ṅīṣ / ṅīn stems, ū-stems (vadhū), strī, the gaurādi list are cited at most",
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
