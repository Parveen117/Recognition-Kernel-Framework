from __future__ import annotations

"""Exact certificate (theorum/65): STEM CLASSES FOR THE FIRST ŚLOKA LINE —
ṛ-stem (savitṛ), s-stem (bhargas), neuter sarvanāma (tad) — plus the
ŚLOKA COVERAGE TEST on Gāyatrī line 1: tat savitur vareṇyam bhargo devasya dhīmahi.

New sūtras on top of theorum/63's rule set (same carrier type):
  7.1.23 svamor napuṃsakāt (luk of su/am after neuter), 1.1.63 na lumatāṅgasya
  (luk blocks pratyaya-lakṣaṇa — 7.2.102 tyadādīnām aḥ does NOT fire),
  8.2.39 jhalāṃ jaśo'nte, 8.4.56 vāvasāne (optional; pause form chosen),
  6.1.68 halṅyābbhyo dīrghāt sutisyapṛktaṃ hal (su-lopa after hal),
  8.2.24 rāt sasya, 8.2.7 nalopaḥ prātipadikāntasya,
  6.1.111 ṛta ut + 1.1.51 ur aṇ raparaḥ, 7.1.94 ṛdu-śanas… anaṅ,
  6.4.11 ap-tṛn-tṛc… upadhā-dīrgha.

Facts certified:
 T1  savitā / savituḥ, bhargaḥ / bhargasaḥ, tat (neuter 1s = 2s) match the
     oracle; 6.1.97 pararūpa and 7.2.102 are correctly BLOCKED for neuter
     tad by 1.1.63 (luk) — a planted "tyadādyatva fires anyway" gives *ta.
 T2  Gāyatrī line 1 pada coverage: 5/6 padas derived (tat, savituḥ,
     vareṇyam, bhargaḥ, devasya); dhīmahi REFUSED (liṅ ātmanepada, chandas
     3.4.6 — not modelled).  Sandhi between padas (savituḥ+v → savitur v,
     bhargaḥ+d → bhargo d: 8.3.15/6.1.113–114) reported but NOT claimed.
 T3  Resolver ladder re-census on the enlarged grammar-wide carrier
     (63 ∪ 64 ∪ 65 domains); 8.2.1 still on every path.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab import sup_vibhakti_resolver_ladder as t63
from proof_lab import ting_lat_parasmaipada as t64
from proof_lab.sup_vibhakti_resolver_ladder import RULES as RULES63
from proof_lab.sup_vibhakti_resolver_ladder import SUP, applicable, derive, is_tripadi, paradigm_domains, reachable, st, surface

HAL = set("kgcjtdpbnmyrlvSzsh") | {"ch", "N"}


def r_7_1_23(W):  # svamor napuṃsakāt : luk of su / am after a neuter (non-a) stem
    stem, aff, f = W
    if "napum" in f and "lopa_done" in f and aff in (("s",), ("a", "m")) and "luk" not in f:
        return (stem, (), f | {"luk"})
    return None


def r_7_2_102(W):  # tyadādīnām aḥ : final of tyad-ādi -> a before vibhakti (blocked by 1.1.63 if luk)
    stem, aff, f = W
    if "tyadadi" in f and stem and stem[-1] == "d" and aff and "luk" not in f and "lopa_done" in f:
        return (stem[:-1] + ("a",), aff, f | {"tyad_done"})
    return None


def r_8_2_39(W):  # jhalāṃ jaśo'nte (d stays d; t -> d) — pada-final jhal -> jaś
    stem, aff, f = W
    # 8.2.1 within the tripādī: 8.4.56's output is asiddha to 8.2.39, so jaśtva never re-fires on the pause form
    if not aff and stem and stem[-1] == "t" and "luk" in f and "avasana" not in f:
        return (stem[:-1] + ("d",), aff, f)
    return None


def r_8_4_56(W):  # vāvasāne : pause form (optional) — jaś -> car chosen
    stem, aff, f = W
    if not aff and stem and stem[-1] == "d" and "luk" in f and "avasana" not in f:
        return (stem[:-1] + ("t",), aff, f | {"avasana"})
    return None


def r_6_1_68(W):  # halṅyābbhyo dīrghāt sutisyapṛktaṃ hal : su lopa after hal-final stem
    stem, aff, f = W
    if aff == ("s",) and "su" in f and "lopa_done" in f and stem and stem[-1] in HAL and "luk" not in f:
        return (stem, (), f | {"su_lopa"})
    return None


def r_8_2_66_stem(W):  # ruḥ on pada-final s of the STEM (after su-lopa / luk)
    stem, aff, f = W
    if not aff and ("su_lopa" in f or "luk" in f) and stem and stem[-1] == "s" and "ru_done" not in f:
        return (stem[:-1] + ("r",), aff, f | {"ru_done"})
    return None


def r_8_3_15_stem(W):
    stem, aff, f = W
    if "ru_done" in f and not aff and stem and stem[-1] == "r":
        return (stem[:-1] + ("H",), aff, f)
    return None


def r_8_2_24(W):  # rāt sasya : s after r deleted at pada end
    stem, aff, f = W
    if aff == ("s",) and stem and stem[-1] == "r" and "ur_done" in f:
        return (stem, (), f | {"su_lopa"})  # then ruḥ? no: r is already r; visarga by 8.3.15 at pause
    return None


def r_8_3_15_r(W):  # visarga on pada-final r at pause (after 8.2.24)
    stem, aff, f = W
    if not aff and "ur_done" in f and stem and stem[-1] == "r" and "su_lopa" in f:
        return (stem[:-1] + ("H",), aff, f | {"ru_done"})
    return None


def r_8_2_7(W):  # nalopaḥ prātipadikāntasya
    stem, aff, f = W
    if not aff and "su_lopa" in f and stem and stem[-1] == "n":
        return (stem[:-1], aff, f)
    return None


def r_6_1_111(W):  # ṛta ut (+1.1.51 ur aṇ raparaḥ): ṛ + a -> ur
    stem, aff, f = W
    if stem and stem[-1] == "R" and aff and aff[0] == "a" and "lopa_done" in f and "Git" in f:
        return (stem[:-1] + ("u", "r"), aff[1:], f | {"ur_done"})
    return None


def r_7_1_94(W):  # ṛdu-śanas-puru-daṃso'neha-sāṃ ca : anaṅ for ṛ-final before su (non-sambuddhi)
    stem, aff, f = W
    if stem and stem[-1] == "R" and aff == ("s",) and "su" in f and "samb" not in f and "lopa_done" in f:
        return (stem[:-1] + ("a", "n"), aff, f | {"anaN"})
    return None


def r_6_4_11(W):  # ap-tṛn-tṛc-svasṛ-naptṛ-… upadhāyāḥ dīrgha (before su, anaṅ stems)
    stem, aff, f = W
    if "anaN" in f and len(stem) >= 2 and stem[-1] == "n" and stem[-2] == "a" and "dirgha_done" not in f:
        return (stem[:-2] + ("A", "n"), aff, f | {"dirgha_done"})
    return None


NEW: list[tuple[str, Callable]] = [
    ("1.1.63", lambda W: None),  # declared: blocking is encoded in r_7_2_102's guard (no separate action)
    ("6.1.68", r_6_1_68), ("6.1.111", r_6_1_111), ("6.4.11", r_6_4_11), ("7.1.23", r_7_1_23), ("7.1.94", r_7_1_94),
    ("7.2.102", r_7_2_102), ("8.2.7", r_8_2_7), ("8.2.24", r_8_2_24), ("8.2.39", r_8_2_39), ("8.4.56", r_8_4_56),
    ("8.2.66s", r_8_2_66_stem), ("8.3.15s", r_8_3_15_stem), ("8.3.15r", r_8_3_15_r),
]
RULES = [r for r in RULES63 if r[0] != "1.1.63"] + NEW


def sup(code):
    aff, feats = [(a, f) for c, a, f in SUP if c == code][0]
    return tuple(aff), set(feats) | {"sup"}


def inputs():
    out = {}
    a, f = sup("1s"); out["savitA"] = st(("s", "a", "v", "i", "t", "R"), a, f)
    a, f = sup("6s"); out["savituH"] = st(("s", "a", "v", "i", "t", "R"), a, f)
    a, f = sup("1s"); out["bhargaH"] = st(("b", "h", "a", "r", "g", "a", "s"), a, f | {"napum"})
    a, f = sup("6s"); out["bhargasaH"] = st(("b", "h", "a", "r", "g", "a", "s"), a, f)
    a, f = sup("1s"); out["tat_1s"] = st(("t", "a", "d"), a, f | {"napum", "tyadadi"})
    a, f = sup("2s"); out["tat_2s"] = st(("t", "a", "d"), a, f | {"napum", "tyadadi"})
    a, f = sup("6s"); out["devasya"] = st(("d", "e", "v", "a"), a, f)
    a, f = sup("2s"); out["vareNyam"] = st(("v", "a", "r", "e", "N", "y", "a"), a, f)
    return out


ORACLE = {"savitA": "savitA", "savituH": "savituH", "bhargaH": "bhargaH", "bhargasaH": "bhargasaH", "tat_1s": "tat", "tat_2s": "tat", "devasya": "devasya", "vareNyam": "vareNyam"}
GAYATRI_LINE_1 = ["tat", "savituH", "vareNyam", "bhargaH", "devasya", "dhImahi"]


def sutra_key_safe(sid):
    return t63.sutra_key(sid.rstrip("sr"))


def grammar_wide(ins, carry=True):
    d65 = paradigm_domains(RULES, carry=carry, carrier_inputs=ins)
    d63 = paradigm_domains(RULES63, carry=carry, carrier_inputs=t63.inputs())
    d64 = paradigm_domains(t64.RULES, carry=carry, carrier_inputs=t64.inputs())
    out = {}
    for sid in set(d65) | set(d63) | set(d64):
        out[sid] = frozenset(d65.get(sid, ())) | frozenset(d63.get(sid, ())) | frozenset(d64.get(sid, ()))
    return out


def build_certificate() -> dict[str, Any]:
    # the resolver keys sūtra numbers via sutra_key; our split tripādī rules carry suffix letters -- patch key
    t63.sutra_key, orig = (lambda sid: orig(sid.rstrip("sr"))), t63.sutra_key  # type: ignore[assignment]
    try:
        ins = inputs()
        dom = grammar_wide(ins)
        forms, paths, census = {}, {}, []
        for code, W0 in ins.items():
            W, p = derive(W0, RULES, record=census, dom=dom)
            forms[code] = surface(W)
            paths[code] = p
        sound = {c: forms[c] == ORACLE[c] for c in ORACLE}
        # planted: remove the 1.1.63 block (luk no longer guards tyadādyatva)
        planted = [(s, (lambda W: (lambda st_, af, f_: (st_[:-1] + ("a",), af, f_ | {"tyad_done"}) if "tyadadi" in f_ and st_ and st_[-1] == "d" and "lopa_done" in f_ and "tyad_done" not in f_ else None)(*W))) if s == "7.2.102" else (s, fn) for s, fn in RULES]
        W_pl, _ = derive(ins["tat_1s"], planted, dom=grammar_wide(ins))
        tri_ok = all(not (is_tripadi(r.rstrip("sr")) and any(not is_tripadi(q.rstrip("sr")) for q in p[i + 1 :])) for p in paths.values() for i, r in enumerate(p))
        free_ok = all(forms[c] in {surface(W) for W in reachable(W0, RULES) if not applicable(W, RULES)} for c, W0 in ins.items())
        pada_status = {}
        for pada in GAYATRI_LINE_1:
            key = {"tat": "tat_1s"}.get(pada, pada)
            pada_status[pada] = "DERIVED" if key in forms and forms[key] == pada else "REFUSED: liṅ ātmanepada / chandas 3.4.6 not modelled"
        checks = {
            "T1_all_stem_class_forms_match_oracle": all(sound.values()),
            "T1_neuter_tad_blocks_tyadadyatva_by_luk_planted_gives_ta": surface(W_pl) != "tat" and forms["tat_1s"] == "tat",
            "T2_gayatri_line1_five_of_six_padas_derived": sum(v == "DERIVED" for v in pada_status.values()) == 5,
            "T3_8_2_1_on_every_path_and_free_normal_forms": tri_ok and free_ok,
        }
        status = "PASS_STEM_CLASSES_GAYATRI_COVERAGE_CANDIDATE" if all(checks.values()) else "FAIL_STEM_CLASSES_GAYATRI_COVERAGE_CANDIDATE"
        return {
            "schema": "rkf.stem_classes_gayatri_coverage_candidate.v1",
            "status": status,
            "forms": forms,
            "oracle_mismatches": sorted(c for c, ok in sound.items() if not ok),
            "planted_tat_without_1_1_63": surface(W_pl),
            "gayatri_line_1": pada_status,
            "rungs_used": sorted({c["rung"] for c in census}),
            "sutras_added": [s for s, _ in NEW if not s.endswith(("s", "r"))] + ["1.1.51"],
            "claim_boundary": {
                "proved_by_exact_finite_certificate": [
                    "savitā/savituḥ (ṛ-stem 1s/6s), bhargaḥ/bhargasaḥ (s-stem), tat (neuter sarvanāma 1s=2s via 7.1.23 luk + 1.1.63 block + 8.2.39/8.4.56) from canonical sūtras = oracle",
                    "1.1.63 is load-bearing: without it 7.2.102 fires on neuter tad and the form is wrong",
                    "Gāyatrī line 1: 5/6 padas derived by the engine; the sixth refused with the missing sectors named",
                ],
                "NOT_claimed": ["full ṛ-/s-stem paradigms; inter-pada sandhi of the line (savitur v-, bhargo d-); dhīmahi; accent", "RH, YM untouched"],
            },
            "checks": checks,
        }
    finally:
        t63.sutra_key = orig  # type: ignore[assignment]


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
    print("FORMS", payload["forms"], "PLANTED", payload["planted_tat_without_1_1_63"])
    print("GAYATRI", payload["gayatri_line_1"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
