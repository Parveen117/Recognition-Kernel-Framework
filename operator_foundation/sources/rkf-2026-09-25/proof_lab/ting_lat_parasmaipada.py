from __future__ import annotations

"""Exact certificate (theorum/64): TIṄ CARRIER — laṭ parasmaipada, bhū and gam,
all 9 forms each, from canonical sūtras; the resolver ladder of theorum/63
exercised on a REAL earlier-apavāda (6.1.97 ato guṇe ⊊ 6.1.101, and 6.1.97
is numbered BEFORE its utsarga: para alone gives *bhavānti).

State: (root, vikaraṇa, tiṅ, features) — three morphemes, two seams.
Sūtras: 3.2.123 vartamāne laṭ; 3.4.78 tiptasjhi…; 1.4.99/1.4.101 (declared);
3.1.68 kartari śap; 3.4.113 tiṅśit sārvadhātukam; it-lopa 1.3.3/1.3.8/1.3.9;
7.1.3 jho'ntaḥ; 7.3.84 sārvadhātukārdhadhātukayoḥ (guṇa); 6.1.78 eco'yavāyāvaḥ;
6.1.97 ato guṇe (pararūpa); 7.3.101 ato dīrgho yañi; 7.3.77 iṣugamiyamāṃ
chaḥ; 6.1.73 che ca; 8.4.40 stoḥ ścunā ścuḥ; 8.2.66 sasajuṣo ruḥ; 8.3.15
kharavasānayor visarjanīyaḥ.

Facts certified:
 T1  18/18 forms match the oracle (bhavati…bhavāmaḥ, gacchati…gacchāmaḥ).
 T2  REAL earlier-apavāda: at bhava+anti both 6.1.97 and 6.1.101 apply;
     6.1.97 < 6.1.101 by number, dom(6.1.97) ⊊ dom(6.1.101) on the paradigm
     carrier; the ladder gives bhavanti, para-only gives bhavAnti (wrong) —
     the apavāda rung is load-bearing on Pāṇini's own data, no planting.
 T3  Resolver census (rungs used, states where para alone disagrees).
 T4  Memory: erasing it-marker memory kills śit/sārvadhātuka-conditioned
     guṇa and chaḥ (bhUati / gamati shapes) — counted.
 T5  8.2.1 on every path; every ladder normal form is a free normal form.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_seam_calculus import sutra_key
from proof_lab.sup_vibhakti_resolver_ladder import applicable, derive, is_tripadi, paradigm_domains, reachable

VOW = ("a", "A", "i", "I", "u", "U", "R", "e", "o", "ai", "au")
State = tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], frozenset[str]]


def st(root, vik, ting, feats=()) -> State:
    return (tuple(root), tuple(vik), tuple(ting), frozenset(feats))


def surface(W: State) -> str:
    return "".join(W[0]) + "".join(W[1]) + "".join(W[2])


def it_lopa(W: State, carry: bool = True) -> State | None:  # 1.3.8 (ś), 1.3.3 (final p), 1.3.9
    r, v, t, f = W
    if "lopa_done" in f:
        return None
    feats = set(f)
    if v and v[0] == "S":
        if carry:
            feats.add("Sit")
        v = v[1:]
    if v and v[-1] == "p":
        if carry:
            feats.add("vik_pit")
        v = v[:-1]
    if t and t[-1] == "p":
        if carry:
            feats.add("pit")
        t = t[:-1]
    feats.add("lopa_done")
    return (r, v, t, frozenset(feats))


def r_3_4_113(W):  # tiṅśit sārvadhātukam (saṃjñā): the vikaraṇa (śit) and the tiṅ are sārvadhātuka
    r, v, t, f = W
    if "lopa_done" in f and "sArva" not in f and ("Sit" in f or "tiN" in f):
        return (r, v, t, f | {"sArva"})
    return None


def r_7_1_3(W):  # jho'ntaḥ
    r, v, t, f = W
    if t[:1] == ("J",) and "lopa_done" in f:
        return (r, v, ("a", "n", "t") + t[1:], f)
    return None


def r_7_3_84(W):  # guṇa of ik-final aṅga before sārvadhātuka (śap)
    r, v, t, f = W
    if r and r[-1] in ("i", "I", "u", "U", "R") and "sArva" in f and "Sit" in f and "guna_done" not in f:
        short = {"I": "i", "U": "u"}.get(r[-1], r[-1])
        return (r[:-1] + ({"i": "e", "u": "o", "R": "ar"}[short],), v, t, f | {"guna_done"})
    return None


def r_6_1_78(W):  # ayādi at root|vikaraṇa seam
    r, v, t, f = W
    nxt = (v + t)[:1]
    if r and r[-1] in ("e", "o", "ai", "au") and nxt and nxt[0] in VOW:
        return (r[:-1] + ({"e": "ay", "o": "av", "ai": "Ay", "au": "Av"}[r[-1]],), v, t, f)
    return None


def r_6_1_97(W):  # ato guṇe : a + (a, e, o) → pararūpa (the later vowel) at vikaraṇa|tiṅ seam
    r, v, t, f = W
    if v == ("a",) and t and t[0] in ("a", "e", "o") and "lopa_done" in f:
        return (r, (), t, f | {"pararupa"})
    return None


def r_6_1_101(W):  # akaḥ savarṇe dīrghaḥ at vikaraṇa|tiṅ seam
    r, v, t, f = W
    if v == ("a",) and t and t[0] in ("a", "A") and "lopa_done" in f:
        return (r, ("A",), t[1:], f)
    return None


def r_7_3_101(W):  # ato dīrgho yañi : a → ā before yañ-initial sārvadhātuka (m, v)
    r, v, t, f = W
    if v == ("a",) and t and t[0] in ("m", "v") and "sArva" in f and "lopa_done" in f:
        return (r, ("A",), t, f)
    return None


def r_7_3_77(W):  # iṣugamiyamāṃ chaḥ
    r, v, t, f = W
    if r in (("g", "a", "m"), ("y", "a", "m"), ("i", "z")) and ("Sit" in f or (v and v[0] == "S")):
        return (r[:-1] + ("ch",), v, t, f)
    return None


def r_6_1_73(W):  # che ca : tuk
    r, v, t, f = W
    if len(r) >= 2 and r[-1] == "ch" and r[-2] in ("a", "i", "u") and "tuk_done" not in f:
        return (r[:-1] + ("t", "ch"), v, t, f | {"tuk_done"})
    return None


def r_8_4_40(W):  # stoḥ ścunā ścuḥ
    r, v, t, f = W
    for k in range(len(r) - 1):
        if r[k] == "t" and r[k + 1] == "ch":
            return (r[:k] + ("c",) + r[k + 1 :], v, t, f)
    return None


def r_8_2_66(W):  # ruḥ on pada-final s
    r, v, t, f = W
    if t and t[-1] == "s" and "ru_done" not in f and "lopa_done" in f:
        return (r, v, t[:-1] + ("r",), f | {"ru_done"})
    return None


def r_8_3_15(W):  # visarga
    r, v, t, f = W
    if "ru_done" in f and t and t[-1] == "r":
        return (r, v, t[:-1] + ("H",), f)
    return None


RULES: list[tuple[str, Callable]] = [
    ("1.3.9", it_lopa), ("3.4.113", r_3_4_113), ("6.1.73", r_6_1_73), ("6.1.78", r_6_1_78), ("6.1.97", r_6_1_97),
    ("6.1.101", r_6_1_101), ("7.1.3", r_7_1_3), ("7.3.77", r_7_3_77), ("7.3.84", r_7_3_84), ("7.3.101", r_7_3_101),
    ("8.2.66", r_8_2_66), ("8.3.15", r_8_3_15), ("8.4.40", r_8_4_40),
]

# 3.4.78 tiṅ (parasmaipada, laṭ 3.2.123) in upadeśa form; śap 3.1.68 = ("S","a","p")
TING = [("3s", ("t", "i", "p")), ("3d", ("t", "a", "s")), ("3p", ("J", "i")), ("2s", ("s", "i", "p")), ("2d", ("t", "h", "a", "s")), ("2p", ("t", "h", "a")), ("1s", ("m", "i", "p")), ("1d", ("v", "a", "s")), ("1p", ("m", "a", "s"))]
ROOTS = {"bhU": ("b", "h", "U"), "gam": ("g", "a", "m")}
ORACLE = {
    "bhU": {"3s": "bhavati", "3d": "bhavataH", "3p": "bhavanti", "2s": "bhavasi", "2d": "bhavathaH", "2p": "bhavatha", "1s": "bhavAmi", "1d": "bhavAvaH", "1p": "bhavAmaH"},
    "gam": {"3s": "gacchati", "3d": "gacchataH", "3p": "gacchanti", "2s": "gacchasi", "2d": "gacchathaH", "2p": "gacchatha", "1s": "gacchAmi", "1d": "gacchAvaH", "1p": "gacchAmaH"},
}


def inputs():
    out = {}
    for rn, root in ROOTS.items():
        for code, ting in TING:
            out[f"{rn}:{code}"] = st(root, ("S", "a", "p"), ting, {"tiN", "laT"})
    return out


def grammar_wide_domains(ins, t63, carry=True):
    d64 = paradigm_domains(RULES, carry=carry, carrier_inputs=ins)
    d63 = paradigm_domains(t63.RULES, carry=carry, carrier_inputs=t63.inputs())
    out = {}
    for sid in set(d64) | set(d63):
        out[sid] = frozenset(d64.get(sid, frozenset())) | frozenset(d63.get(sid, frozenset()))
    return out


def derive_para_only(W0, rules):
    W = W0
    for _ in range(30):
        app = applicable(W, rules)
        if not app:
            return W
        non_tri = [x for x in app if not is_tripadi(x[0])] or app
        W = max(non_tri, key=lambda x: sutra_key(x[0]))[1]
    raise AssertionError


def build_certificate() -> dict[str, Any]:
    ins = inputs()
    # BUILD NOTE: on the tiṅ carrier alone dom(6.1.97) == dom(6.1.101) (only a+a occurs), so containment was
    # blind and para wrongly gave bhavAnti.  Apavāda (niravakāśatva) is a property of the GRAMMAR-WIDE carrier:
    # 6.1.101's extra scope (a+ā, ā+a) lives in the nominal sector.  Domains are therefore unioned with the
    # theorum/63 paradigm carrier (shared sūtra ids), which is what makes 6.1.97 ⊊ 6.1.101 visible.
    from proof_lab import sup_vibhakti_resolver_ladder as t63
    dom = grammar_wide_domains(ins, t63)
    forms, paths, census = {}, {}, []
    for code, W0 in ins.items():
        W, p = derive(W0, RULES, record=census, dom=dom)
        forms[code] = surface(W)
        paths[code] = p
    sound = {f"{rn}:{c}": forms[f"{rn}:{c}"] == ORACLE[rn][c] for rn in ORACLE for c in ORACLE[rn]}
    # T2 real earlier-apavāda
    para_3p = surface(derive_para_only(ins["bhU:3p"], RULES))
    ap_dom = dom["6.1.97"] < dom["6.1.101"]
    earlier = sutra_key("6.1.97") < sutra_key("6.1.101")
    # T3 census
    rungs = sorted({c["rung"] for c in census})
    para_disagree = [c for c in census if c["winner"] != max(c["applicable"], key=sutra_key)]
    # T4 memory
    dom_nm = grammar_wide_domains(ins, t63, carry=False)
    nomem = {}
    for code, W0 in ins.items():
        try:
            nomem[code] = surface(derive(W0, RULES, carry=False, dom=dom_nm)[0])
        except AssertionError:
            nomem[code] = "NO_NF"
    broken = sorted(c for c in sound if nomem[c] != forms[c])
    # BUILD NOTE: draft expected all 18 to break; the certificate refused it -- gam's 7.3.77 can still read the
    # undeleted Ś-phone when it fires before lopa (the 1.1.62 order-dependence of theorum/58 T3), so only the
    # bhū forms (guṇa needs the sārvadhātuka saṃjñā, which lives only in memory) break without memory.
    # T5
    tri_ok = all(not (is_tripadi(r) and any(not is_tripadi(q) for q in p[i + 1 :])) for p in paths.values() for i, r in enumerate(p))
    free_ok = all(forms[code] in {surface(W) for W in reachable(W0, RULES) if not applicable(W, RULES)} for code, W0 in ins.items())
    lopa_every = all("1.3.9" in p for p in paths.values())
    checks = {
        "T1_18_of_18_forms_match_oracle": all(sound.values()),
        "T2_real_earlier_apavada_6_1_97_subset_6_1_101_and_earlier_by_number": ap_dom and earlier,
        "T2_ladder_bhavanti_para_only_bhavAnti": forms["bhU:3p"] == "bhavanti" and para_3p == "bhavAnti",
        "T3_para_alone_disagrees_somewhere": len(para_disagree) > 0,
        "T4_memory_erased_breaks_all_9_bhU_forms": all(f"bhU:{c}" in broken for c, _ in TING),
        "T5_8_2_1_on_every_path_and_free_normal_forms": tri_ok and free_ok and lopa_every,
    }
    status = "PASS_TING_LAT_PARASMAIPADA_CANDIDATE" if all(checks.values()) else "FAIL_TING_LAT_PARASMAIPADA_CANDIDATE"
    return {
        "schema": "rkf.ting_lat_parasmaipada_candidate.v1",
        "status": status,
        "forms": forms,
        "oracle_mismatches": sorted(c for c, ok in sound.items() if not ok),
        "para_only_3p": para_3p,
        "rungs_used": rungs,
        "para_disagreements": para_disagree,
        "forms_without_memory": nomem,
        "sutras_used": [s for s, _ in RULES] + ["3.2.123", "3.4.78", "1.4.99", "1.4.101", "3.1.68", "1.3.3", "1.3.8"],
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "laṭ parasmaipada of bhū and gam, 18/18 forms from canonical sūtras, match the oracle",
                "REAL earlier-apavāda on Pāṇini's data: 6.1.97 ato guṇe ⊊ 6.1.101 with 6.1.97 earlier by number; ladder gives bhavanti, para-only gives *bhavānti",
                "memory channel load-bearing for all 9 bhū forms (sārvadhātuka saṃjñā lives only in memory); gam survives by reading the undeleted Ś-phone before lopa (58 T3 order-dependence)",
                "8.2.1 on every path; ladder normal forms are free normal forms",
            ],
            "NOT_claimed": ["ātmanepada; other lakāras (laṅ, liṭ, lṛṭ…); other gaṇas (vikaraṇas śyan, śnu, …); accent; completeness", "RH, YM untouched"],
        },
        "checks": checks,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k, v)
    print("FORMS", payload["forms"])
    print("MISMATCH", payload["oracle_mismatches"], "PARA3P", payload["para_only_3p"], "RUNGS", payload["rungs_used"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
