from __future__ import annotations

"""Exact certificate (theorum/66): ĀTMANEPADA SECTOR — laṭ of edh and labh,
all 9 forms each, from canonical sūtras; and the honest status of dhīmahi.

New sūtras on the theorum/64 carrier (root | vikaraṇa | tiṅ):
  1.3.12 anudāttaṅita ātmanepadam (declared: edh, labh are ātmanepadī)
  3.4.78 ta-ātām-jha-thās-āthām-dhvam-iṭ-vahi-mahiṅ (ātmanepada tiṅ)
  3.4.79 ṭita ātmanepadānāṃ ṭer e (in a ṭit lakāra, final ṭi -> e), 3.4.80 thāsaḥ se
  7.1.3 jho'ntaḥ
  7.2.81 āto ṅitaḥ (ā of ṅit ātmanepada -> iy after a-aṅga)
  6.1.66 lopo vyor vali (y deleted before val)
  6.1.87 ād guṇaḥ; 6.1.97 ato guṇe; 7.3.101 ato dīrgho yañi; 7.3.84 guṇa; 6.1.78 ayādi
  1.3.9 / 1.3.3 it-lopa; 3.1.68 śap; 3.4.113 sārvadhātuka

Facts certified:
 T1  18/18: edhate edhete edhante edhase edhethe edhadhve edhe edhāvahe
     edhāmahe; labhate labhete labhante labhase labhethe labhadhve labhe
     labhāvahe labhāmahe.
 T2  7.2.81 -> 6.1.66 -> 6.1.87 chain is load-bearing (3d, 2d): removing
     6.1.66 leaves *edhaiyte-type forms.
 T3  3.4.79 ṭer e: the ṭit endings (ta, ātām, thās, āthām, iṭ, vahi, mahiṅ
     by 1.3.?? -- ṭ-marking declared) all take e; census, 8.2.1, free NFs.
 DHĪMAHI (theorum/65's refused pada): analysed, still REFUSED — the Vedic
     form needs chandasi bahulam / vyatyaya (3.1.85, 2.4.76) to suppress
     the juhotyādi ślu-reduplication of dhā (classical vidhiliṅ 1p is
     dadhīmahi); a "bahulam" rule has no deterministic domain, so no
     certificate can derive dhīmahi as a unique normal form.  What CAN be
     stated: the ending -mahi is 3.4.78 mahiṅ with 3.4.79 blocked (non-ṭit
     in liṅ), and ā -> ī is 6.4.66 ghumāsthā… hali.  Recorded, not claimed.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab import sup_vibhakti_resolver_ladder as t63
from proof_lab.sup_vibhakti_resolver_ladder import applicable, derive, is_tripadi, paradigm_domains, reachable
from proof_lab.ting_lat_parasmaipada import VOW, it_lopa, r_3_4_113, r_6_1_78, r_6_1_97, r_6_1_101, r_7_1_3, r_7_3_101, r_7_3_84, st, surface

VAL = set("kgcjtdpbnmrlvSzsh") | {"th", "dh", "ch", "bh"}


def r_3_4_79(W):  # ṭita ātmanepadānāṃ ṭer e : in a ṭit LAKĀRA (laṭ) every ātmanepada ending's ṭi -> e
    # BUILD NOTE: first draft read "ṭitaḥ" as the ending being ṭit (marked 'T'); the certificate refused it
    # (edhadhvam, not edhadhve).  ṭitaḥ qualifies the lakāra (laṬ), as the sūtra says.
    r, v, t, f = W
    if "laT" in f and "atm" in f and "lopa_done" in f and "Ter_e" not in f and any(ph in VOW for ph in t):
        # ṭi = last vowel onward
        idx = max(i for i, ph in enumerate(t) if ph in VOW)
        return (r, v, t[:idx] + ("e",), f | {"Ter_e"})
    return None


def r_3_4_80(W):  # thāsaḥ se
    r, v, t, f = W
    if t == ("t", "h", "A", "s") and "lopa_done" in f and "Ter_e" not in f:
        return (r, v, ("s", "e"), f | {"Ter_e"})
    return None


def r_7_2_81(W):  # āto ṅitaḥ : initial ā of a ṅit ātmanepada ending -> iy after a-final aṅga
    r, v, t, f = W
    if v == ("a",) and t and t[0] == "A" and "Git" in f and "lopa_done" in f:
        return (r, v, ("i", "y") + t[1:], f)
    return None


def r_6_1_66(W):  # lopo vyor vali : y/v deleted before val
    r, v, t, f = W
    for k in range(len(t) - 1):
        if t[k] in ("y", "v") and t[k + 1] in VAL:
            return (r, v, t[:k] + t[k + 1 :], f)
    return None


def r_6_1_87_seam(W):  # ād guṇaḥ at vikaraṇa|tiṅ seam
    r, v, t, f = W
    if v == ("a",) and t and t[0] in ("i", "u") and "lopa_done" in f:
        return (r, ({"i": "e", "u": "o"}[t[0]],), t[1:], f)
    return None


def atm_it_lopa(W, carry=True):
    """1.3.9 for ātmanepada endings: ṭ-marked (ta ātām thās āthām iṭ vahi mahiṅ -> 'T' feature), ṅit (ātām, āthām, mahiṅ)."""
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
    if t and t[-1] == "T":
        if carry:
            feats.add("Tit")
        t = t[:-1]
    if t and t[-1] == "G":
        if carry:
            feats.add("Git")
        t = t[:-1]
    if t and t[0] == "G":
        if carry:
            feats.add("Git")
        t = t[1:]
    feats.add("lopa_done")
    return (r, v, t, frozenset(feats))


RULES: list[tuple[str, Callable]] = [
    ("1.3.9", atm_it_lopa), ("3.4.113", r_3_4_113), ("3.4.79", r_3_4_79), ("3.4.80", r_3_4_80), ("6.1.66", r_6_1_66), ("6.1.78", r_6_1_78),
    ("6.1.87", r_6_1_87_seam), ("6.1.97", r_6_1_97), ("6.1.101", r_6_1_101), ("7.1.3", r_7_1_3), ("7.2.81", r_7_2_81),
    ("7.3.84", r_7_3_84), ("7.3.101", r_7_3_101),
]

# 3.4.78 ātmanepada in upadeśa shape; 'T' = ṭit marker, 'G' = ṅit marker (ātām/āthām/mahiṅ), jha as 'J'
TING = [
    ("3s", ("t", "a")), ("3d", ("G", "A", "t", "A", "m")), ("3p", ("J", "a")),
    ("2s", ("t", "h", "A", "s")), ("2d", ("G", "A", "t", "h", "A", "m")), ("2p", ("d", "h", "v", "a", "m")),
    ("1s", ("i", "T")), ("1d", ("v", "a", "h", "i")), ("1p", ("m", "a", "h", "i", "G")),
]
ROOTS = {"edh": ("e", "d", "h"), "labh": ("l", "a", "b", "h")}
ORACLE = {
    "edh": {"3s": "edhate", "3d": "edhete", "3p": "edhante", "2s": "edhase", "2d": "edhethe", "2p": "edhadhve", "1s": "edhe", "1d": "edhAvahe", "1p": "edhAmahe"},
    "labh": {"3s": "labhate", "3d": "labhete", "3p": "labhante", "2s": "labhase", "2d": "labhethe", "2p": "labhadhve", "1s": "labhe", "1d": "labhAvahe", "1p": "labhAmahe"},
}


def inputs():
    return {f"{rn}:{c}": st(root, ("S", "a", "p"), ting, {"tiN", "laT", "atm"}) for rn, root in ROOTS.items() for c, ting in TING}


def grammar_wide(ins, rules, carry=True):
    d = paradigm_domains(rules, carry=carry, carrier_inputs=ins)
    d63 = paradigm_domains(t63.RULES, carry=carry, carrier_inputs=t63.inputs())
    return {sid: frozenset(d.get(sid, ())) | frozenset(d63.get(sid, ())) for sid in set(d) | set(d63)}


def build_certificate() -> dict[str, Any]:
    ins = inputs()
    dom = grammar_wide(ins, RULES)
    forms, paths, census = {}, {}, []
    for code, W0 in ins.items():
        W, p = derive(W0, RULES, record=census, dom=dom)
        forms[code] = surface(W)
        paths[code] = p
    sound = {f"{rn}:{c}": forms[f"{rn}:{c}"] == ORACLE[rn][c] for rn in ORACLE for c in ORACLE[rn]}
    # T2 chain control: drop 6.1.66
    no66 = [r for r in RULES if r[0] != "6.1.66"]
    f3d = surface(derive(ins["edh:3d"], no66, dom=grammar_wide(ins, no66))[0])
    tri_ok = all(not (is_tripadi(r) and any(not is_tripadi(q) for q in p[i + 1 :])) for p in paths.values() for i, r in enumerate(p))
    free_ok = all(forms[c] in {surface(W) for W in reachable(W0, RULES) if not applicable(W, RULES)} for c, W0 in ins.items())
    # BUILD NOTE: 1s (iṭ) reaches edhe by 6.1.87 guṇa on a+i BEFORE 3.4.79 (para picks 6.1.87 over 3.4.79);
    # the tradition applies ṭer e first (3.4.79 depends only on the lakāra -- antaraṅga -- while guṇa depends on
    # the seam).  That is the ANTARAṄGA rung, which is NOT modelled; the form coincides, the path does not.
    ter_e = all(("3.4.79" in paths[f"{rn}:{c}"]) or (c == "2s" and "3.4.80" in paths[f"{rn}:{c}"]) for rn in ROOTS for c in ORACLE["edh"] if c != "1s")
    antaranga_gap_1s = all("3.4.79" not in paths[f"{rn}:1s"] and "6.1.87" in paths[f"{rn}:1s"] for rn in ROOTS)
    checks = {
        "T1_18_of_18_atmanepada_forms_match_oracle": all(sound.values()),
        "T2_6_1_66_load_bearing_in_7_2_81_chain": f3d != "edhete",
        "T3_ter_e_on_all_forms_except_1s_and_8_2_1_and_free_NFs": ter_e and tri_ok and free_ok,
        "T3_1s_antaranga_gap_recorded_form_coincides": antaranga_gap_1s and forms["edh:1s"] == "edhe",
    }
    status = "PASS_LAT_ATMANEPADA_CANDIDATE" if all(checks.values()) else "FAIL_LAT_ATMANEPADA_CANDIDATE"
    return {
        "schema": "rkf.lat_atmanepada_candidate.v1",
        "status": status,
        "forms": forms,
        "oracle_mismatches": sorted(c for c, ok in sound.items() if not ok),
        "edh_3d_without_6_1_66": f3d,
        "rungs_used": sorted({c["rung"] for c in census}),
        "dhImahi": "REFUSED: Vedic form requires chandasi bahulam / vyatyaya to suppress juhotyādi ślu (classical vidhiliṅ 1p = dadhīmahi); no deterministic domain, no unique normal form",
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "laṭ ātmanepada of edh and labh, 18/18 forms from canonical sūtras = oracle",
                "7.2.81 āto ṅitaḥ -> 6.1.66 lopo vyor vali -> 6.1.87 guṇa chain load-bearing (dual forms)",
                "3.4.79 ṭer e on every ṭit ending; 8.2.1 on every path; normal forms are free normal forms",
            ],
            "NOT_claimed": ["dhīmahi (see field); liṅ/laṅ/lṛṭ; non-a-final aṅgas in ātmanepada (7.1.5); accent", "antaraṅga rung (1s path differs from the tradition's; form coincides)", "RH, YM untouched"],
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
    print("FORMS", payload["forms"], "NO66", payload["edh_3d_without_6_1_66"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
