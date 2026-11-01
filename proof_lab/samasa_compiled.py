from __future__ import annotations

"""Exact certificate (theorum/104): SAMĀSA COMPILED — tatpuruṣa, karmadhāraya,
dvandva and bahuvrīhi from two sup-ending padas: the inner sup deleted by 2.4.71,
the upasarjana placed first by 1.2.43 / 2.2.30 (dvandva by 2.2.34), the junction
sandhi 6.1.87 / 6.1.101 (with 1.1.51), 8.2.7 on the pūrvapada rājan, 6.3.46 +
5.4.91 ṭac + 6.4.144 for mahārāja, 1.2.48 for citragu; then the compound declined
by theorum/63's resolver ladder (rājapuruṣa, 21 cells, with the ṣ-trigger of
8.4.1 supplied by theorum/91's ṇatva), theorum/91 (citragu) and theorum/93
(nīlotpala); each rule shown load-bearing on exactly its compounds.

Quoted sūtras:
 2.1.3    prāk kaḍārāt samāsaḥ ; 2.1.4 saha supā ; 2.1.22 tatpuruṣaḥ
 2.1.24   dvitīyā śritātītapatitagatātyastaprāptāpannaiḥ     kṛṣṇaśrita
 2.1.36   caturthī tadarthārthabalihitasukharakṣitaiḥ         yūpadāru
 2.1.37   pañcamī bhayena                                     vṛkabhaya
 2.1.40   saptamī śauṇḍaiḥ                                    akṣaśauṇḍa
 2.2.8    ṣaṣṭhī                                              rājapuruṣa, devālaya
 1.2.42   tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ           nīlotpala, rājarṣi, mahārāja
 2.2.23   śeṣo bahuvrīhiḥ ; 2.2.24 anekam anyapadārthe        pītāmbara, citragu
 2.2.29   cārthe dvandvaḥ                                     rāmalakṣmaṇa
 1.2.43   prathamānirdiṣṭaṁ samāsa upasarjanam ; 2.2.30 upasarjanaṁ pūrvam ; 2.2.34 alpāctaram
 2.4.71   supo dhātuprātipadikayoḥ                             luk of the inner sup
 1.2.46   kṛttaddhitasamāsāś ca ; 2.4.26 paraval liṅgaṁ dvandvatatpuruṣayoḥ
 1.4.14   suptiṅantaṁ padam ; 1.1.62 pratyayalope pratyayalakṣaṇam ; 8.2.7 nalopaḥ prātipadikāntasya
 6.1.87   ād guṇaḥ ; 6.1.101 akaḥ savarṇe dīrghaḥ ; 1.1.51 ur aṇ raparaḥ
 6.3.46   ān mahataḥ samānādhikaraṇajātīyayoḥ ; 5.4.91 rājāhaḥsakhibhyaṣ ṭac ; 6.4.144 nas taddhite
 1.2.48   gostriyor upasarjanasya
 8.4.1    raṣābhyāṁ no ṇaḥ samānapade ; 8.4.2 aṭkupvāṅnumvyavāye 'pi

 T1  twelve compounds from their sup-ending members — 12/12.
 T2  rājapuruṣa declined on theorum/63's ladder (21 cells; 3s rājapuruṣeṇa, 6p
     rājapuruṣāṇām by 8.4.1's ṣ-trigger), rāmalakṣmaṇau (1d), citragu (theorum/91),
     nīlotpala (theorum/93, neuter by 2.4.26).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.ghi_stem_sup_compiled import natva_8_4_2
from proof_lab.ghi_stem_sup_compiled import paradigm as ghi_paradigm
from proof_lab.napumsaka_sup_compiled import paradigm as napumsaka_paradigm
from proof_lab.paninian_instruction_format import GUNA_SET, VRDDHI_SET, antaratama, rapara_1_1_51
from proof_lab.sup_vibhakti_resolver_ladder import RULES, SUP, derive as ladder_derive, paradigm_domains, st, surface

SOURCES = {
    "2.1.3": "prāk kaḍārāt samāsaḥ", "2.1.4": "saha supā", "2.1.22": "tatpuruṣaḥ",
    "2.1.24": "dvitīyā śritātītapatitagatātyastaprāptāpannaiḥ", "2.1.36": "caturthī tadarthārthabalihitasukharakṣitaiḥ",
    "2.1.37": "pañcamī bhayena", "2.1.40": "saptamī śauṇḍaiḥ", "2.2.8": "ṣaṣṭhī",
    "1.2.42": "tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ", "2.2.23": "śeṣo bahuvrīhiḥ", "2.2.24": "anekam anyapadārthe",
    "2.2.29": "cārthe dvandvaḥ", "1.2.43": "prathamānirdiṣṭaṁ samāsa upasarjanam", "2.2.30": "upasarjanaṁ pūrvam", "2.2.34": "alpāctaram",
    "2.4.71": "supo dhātuprātipadikayoḥ", "1.2.46": "kṛttaddhitasamāsāś ca", "2.4.26": "paraval liṅgaṁ dvandvatatpuruṣayoḥ",
    "1.4.14": "suptiṅantaṁ padam", "1.1.62": "pratyayalope pratyayalakṣaṇam", "8.2.7": "nalopaḥ prātipadikāntasya",
    "6.1.87": "ād guṇaḥ", "6.1.101": "akaḥ savarṇe dīrghaḥ", "1.1.51": "ur aṇ raparaḥ",
    "6.3.46": "ān mahataḥ samānādhikaraṇajātīyayoḥ", "5.4.91": "rājāhaḥsakhibhyaṣ ṭac", "6.4.144": "nas taddhite",
    "1.2.48": "gostriyor upasarjanasya", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.4.2": "aṭkupvāṅnumvyavāye 'pi",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
SUP_TEACH = {"1": "su", "2": "am", "3": "ṭā", "4": "ṅe", "5": "ṅasi", "6": "ṅas", "7": "ṅi"}
UPASARJANA_VIBHAKTI = {"2.1.24": "2", "2.1.36": "4", "2.1.37": "5", "2.1.40": "7", "2.2.8": "6"}  # the vibhakti named in prathamā in the vidhi (1.2.43)
KIND = {"2.1.24": "tatpuruṣa", "2.1.36": "tatpuruṣa", "2.1.37": "tatpuruṣa", "2.1.40": "tatpuruṣa", "2.2.8": "tatpuruṣa",
        "1.2.42": "karmadhāraya", "2.2.24": "bahuvrīhi", "2.2.29": "dvandva"}
# member = (prātipadika, vibhakti); the order given is the vigraha order, not yet the samāsa order
CASES = [  # (members, vidhi sūtra, expected prātipadika)
    (((("p", "u", "r", "u", "ṣ", "a"), "1"), (("r", "ā", "j", "a", "n"), "6")), "2.2.8", "rājapuruṣa"),
    (((("ś", "r", "i", "t", "a"), "1"), (("k", "ṛ", "ṣ", "ṇ", "a"), "2")), "2.1.24", "kṛṣṇaśrita"),
    (((("y", "ū", "p", "a"), "4"), (("d", "ā", "r", "u"), "1")), "2.1.36", "yūpadāru"),
    (((("bh", "a", "y", "a"), "1"), (("v", "ṛ", "k", "a"), "5")), "2.1.37", "vṛkabhaya"),
    (((("a", "kṣ", "a"), "7"), (("ś", "au", "ṇ", "ḍ", "a"), "1")), "2.1.40", "akṣaśauṇḍa"),
    (((("d", "e", "v", "a"), "6"), (("ā", "l", "a", "y", "a"), "1")), "2.2.8", "devālaya"),
    (((("n", "ī", "l", "a"), "1"), (("u", "t", "p", "a", "l", "a"), "1")), "1.2.42", "nīlotpala"),
    (((("r", "ā", "j", "a", "n"), "1"), (("ṛ", "ṣ", "i"), "1")), "1.2.42", "rājarṣi"),
    (((("m", "a", "h", "a", "t"), "1"), (("r", "ā", "j", "a", "n"), "1")), "1.2.42", "mahārāja"),
    (((("p", "ī", "t", "a"), "1"), (("a", "m", "b", "a", "r", "a"), "1")), "2.2.24", "pītāmbara"),
    (((("c", "i", "t", "r", "a"), "1"), (("g", "o"), "1")), "2.2.24", "citragu"),
    (((("l", "a", "kṣ", "m", "a", "ṇ", "a"), "1"), (("r", "ā", "m", "a"), "1")), "2.2.29", "rāmalakṣmaṇa"),
]
ALL_STAGES = ("2.4.71", "2.2.30", "2.2.34", "6.3.46", "5.4.91", "6.4.144", "8.2.7", "1.2.48", "6.1.101", "6.1.87", "1.1.51")


def _vowels(s) -> int:
    return sum(1 for x in s if x in VOWELS)


def compound(members, vidhi: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    kind = KIND[vidhi]
    path = [f"{' + '.join(''.join(m) + '-' + SUP_TEACH[v] for m, v in members)} ({kind}, {vidhi}; 2.1.4 saha supā)"]
    # 1.2.43 / 2.2.30: the member whose vibhakti is named in prathamā in the vidhi is upasarjana and goes first
    ms = list(members)
    if vidhi in UPASARJANA_VIBHAKTI and "2.2.30" in on:
        v = UPASARJANA_VIBHAKTI[vidhi]
        ms.sort(key=lambda m: 0 if m[1] == v else 1)
        path.append(f"the {SUP_TEACH[v]}-ending member is upasarjana (1.2.43) and stands first (2.2.30)")
    if kind == "dvandva" and "2.2.34" in on:
        ms.sort(key=lambda m: _vowels(m[0]))
        path.append("the member with fewer vowels stands first (2.2.34 alpāctaram)")
    # 2.4.71: luk of the inner sup
    if "2.4.71" in on:
        padas = [list(m[0]) for m in ms]
        path.append("inner sup deleted (2.4.71 supo dhātuprātipadikayoḥ); the compound is a prātipadika (1.2.46)")
    else:
        padas = [list(m[0]) + list(SUP_TEACH[m[1]]) for m in ms]
    p1, p2 = padas
    # 6.3.46: mahat → mahā before a samānādhikaraṇa uttarapada
    if kind == "karmadhāraya" and p1 == list("mahat") and "6.3.46" in on:
        p1 = ["m", "a", "h", "ā"]; path.append("mahat → mahā (6.3.46 ān mahataḥ)")
    # 5.4.91: ṭac after a tatpuruṣa ending in rājan; 6.4.144: the ṭi (an) of the bha drops before the taddhita
    if kind in ("karmadhāraya",) and p2 == list("rājan") and "5.4.91" in on:
        p2 = p2 + ["ṭ", "a"]; path.append("samāsānta ṭac after rājan (5.4.91; a-it 1.3.7 → a)")
        p2.remove("ṭ")
        if "6.4.144" in on:
            p2 = p2[:3] + ["a"]; path.append("ṭi (an) of the bha deleted before the taddhita (6.4.144 nas taddhite)")
    # 8.2.7: the pūrvapada is a pada (1.4.14 by 1.1.62) → its final n drops
    if p1[-1] == "n" and "8.2.7" in on:
        p1 = p1[:-1]; path.append("pada-final n of the pūrvapada deleted (8.2.7 nalopaḥ prātipadikāntasya; pada by 1.4.14 with 1.1.62)")
    # 1.2.48: go as upasarjana (bahuvrīhi) → short
    if kind == "bahuvrīhi" and p2 == ["g", "o"] and "1.2.48" in on:
        p2 = ["g", "u"]; path.append("go, upasarjana in the bahuvrīhi, shortened (1.2.48 gostriyor upasarjanasya; 1.1.48 eca ig ghrasvādeśe)")
    # junction sandhi
    a, b = p1[-1], p2[0]
    if a in ("a", "ā") and b in ("a", "ā") and "6.1.101" in on:
        p1, p2 = p1[:-1] + ["ā"], p2[1:]; path.append("a / ā + a / ā → ā (6.1.101 akaḥ savarṇe dīrghaḥ)")
    elif a in ("a", "ā") and b in ("i", "ī", "u", "ū", "ṛ") and "6.1.87" in on:
        g = antaratama({"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}[b], GUNA_SET)
        if b == "ṛ" and "1.1.51" in on:
            g = rapara_1_1_51("R", g)
        p1, p2 = p1[:-1] + list(g), p2[1:]; path.append(f"a + {b} → {g} (6.1.87 ād guṇaḥ; 1.1.50" + ("; 1.1.51 ur aṇ raparaḥ)" if b == "ṛ" else ")"))
    return "".join(p1 + p2), path


def t1_compounds() -> dict[str, Any]:
    forms = {e: compound(ms, v)[0] for ms, v, e in CASES}
    exp_breaks = {
        "2.4.71": {e for *_, e in CASES}, "2.2.30": {"rājapuruṣa", "kṛṣṇaśrita", "vṛkabhaya"}, "2.2.34": {"rāmalakṣmaṇa"},
        "6.3.46": {"mahārāja"}, "5.4.91": {"mahārāja"}, "6.4.144": {"mahārāja"}, "8.2.7": {"rājapuruṣa", "rājarṣi"},
        "1.2.48": {"citragu"}, "6.1.101": {"devālaya", "pītāmbara"}, "6.1.87": {"nīlotpala", "rājarṣi"}, "1.1.51": {"rājarṣi"},
    }
    broken = {s: sorted(e for ms, v, e in CASES if compound(ms, v, tuple(x for x in ALL_STAGES if x != s))[0] != e) for s in exp_breaks}
    checks = {"twelve_compounds_equal_the_classical_pratipadikas": all(forms[e] == e for e in forms)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "kinds": {e: KIND[v] for _, v, e in CASES}, "paths": {e: compound(ms, v)[1] for ms, v, e in CASES}, "broken": broken}


# theorum/63 works on 58-code tokens
TO58 = {"ā": "A", "ī": "I", "ū": "U", "ṛ": "R", "ṇ": "N", "ṣ": "z", "ś": "S", "ṭ": "T", "ṅ": "G", "ḥ": "H"}
FROM58 = {v: k for k, v in TO58.items()}
ORACLE_RAJAPURUSA = {
    "1s": "rājapuruṣaḥ", "1d": "rājapuruṣau", "1p": "rājapuruṣāḥ", "2s": "rājapuruṣam", "2d": "rājapuruṣau", "2p": "rājapuruṣān",
    "3s": "rājapuruṣeṇa", "3d": "rājapuruṣābhyām", "3p": "rājapuruṣaiḥ", "4s": "rājapuruṣāya", "4d": "rājapuruṣābhyām", "4p": "rājapuruṣebhyaḥ",
    "5s": "rājapuruṣāt", "5d": "rājapuruṣābhyām", "5p": "rājapuruṣebhyaḥ", "6s": "rājapuruṣasya", "6d": "rājapuruṣayoḥ", "6p": "rājapuruṣāṇām",
    "7s": "rājapuruṣe", "7d": "rājapuruṣayoḥ", "7p": "rājapuruṣeṣu", "8s": "rājapuruṣa",
}


def decline_a_stem(stem_iast: str, natva: bool = True) -> dict[str, str]:
    """theorum/63's ladder on the compound a-stem, then the ṣ-trigger of 8.4.1 (theorum/91's ṇatva) inside the samānapada."""
    stem = tuple(TO58.get(c, c) for c in stem_iast)
    dom = paradigm_domains(RULES)
    out = {}
    for code, aff, feats in SUP:
        aff = tuple(aff) if code != "7p" else ("s", "u")
        W, _ = ladder_derive(st(stem, aff, set(feats) | {"sup"}), RULES, dom=dom)
        word = [FROM58.get(c, c) for c in surface(W)]
        if natva:
            word, _ = natva_8_4_2(word)
        out[code] = "".join(word)
    return out


def t2_declension() -> dict[str, Any]:
    rp = decline_a_stem("rājapuruṣa")
    rp_no_natva = decline_a_stem("rājapuruṣa", natva=False)
    rl = decline_a_stem("rāmalakṣmaṇa")
    cg = ghi_paradigm(("c", "i", "t", "r", "a", "g", "u"))
    nu = napumsaka_paradigm(("n", "ī", "l", "o", "t", "p", "a", "l", "a"))
    checks = {
        "rajapurusa_21_cells_equal_oracle": all(rp[c] == ORACLE_RAJAPURUSA[c] for c in ORACLE_RAJAPURUSA),
        "without_8_4_1_sa_trigger_exactly_3s_6p_break": sorted(c for c in ORACLE_RAJAPURUSA if rp_no_natva[c] != ORACLE_RAJAPURUSA[c]) == ["3s", "6p"],
        "ramalaksmanau_dual_1d_2d": rl["1d"] == "rāmalakṣmaṇau" and rl["2d"] == "rāmalakṣmaṇau",
        "citragu_ghi_1s_3s_6s": (cg["1s"], cg["3s"], cg["6s"]) == ("citraguḥ", "citraguṇā", "citragoḥ"),
        "nilotpala_neuter_1s_1p_by_2_4_26": (nu["1s"], nu["1p"]) == ("nīlotpalam", "nīlotpalāni"),
    }
    return {"checks": checks, "rajapurusa": rp, "ramalaksmana_1d": rl["1d"], "citragu": {k: cg[k] for k in ("1s", "3s", "6s")}, "nilotpala": {k: nu[k] for k in ("1s", "1p")}}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_compounds": t1_compounds(), "t2_declension": t2_declension()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SAMASA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_SAMASA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.samasa_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "twelve compounds (five tatpuruṣa, three karmadhāraya, two bahuvrīhi, one dvandva, devālaya) from their sup-ending members by 2.4.71, 1.2.43 / 2.2.30, 2.2.34, 6.3.46, 5.4.91, 6.4.144, 8.2.7, 1.2.48, 6.1.101, 6.1.87, 1.1.51; each rule breaks exactly the compounds stated",
                "rājapuruṣa declined on theorum/63's ladder, 21 cells, with 8.4.1's ṣ-trigger (theorum/91) load-bearing on exactly 3s and 6p; rāmalakṣmaṇau; citragu on theorum/91; nīlotpala neuter (2.4.26) on theorum/93",
            ],
            "NOT_claimed": [
                "the kind of each compound (and the vidhi sūtra) is declared from the meaning; the order of the karmadhāraya / bahuvrīhi members is declared (the vidhi names both in prathamā)",
                "samāsānta affixes other than 5.4.91; the accent 6.1.223; dvigu, avyayībhāva, ekaśeṣa; the number of a dvandva (itaretarayoga dual declared)",
                "theorum/63's own 8.4.2 rule looks only for an r trigger, so the ṣ-trigger of 8.4.1 is applied after the ladder by theorum/91's ṇatva (recorded, not hidden)",
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
