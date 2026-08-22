from __future__ import annotations

"""Exact certificate (theorum/67): PADA → LINE CARRIER — external sandhi of the
Gāyatrī (three lines) from its padas.

Carrier: a line is a tuple of padas; each pada is its pada-final form BEFORE
pause rules (the state theorum/63/65 reach just before 8.3.15).  Rules act
on the seam between consecutive padas or at the line end (avasāna):
  8.2.66 sasajuṣo ruḥ        pada-final s -> r(u)
  6.1.113 ato ror aplutād aplute   ru -> u after a, before a
  6.1.114 haśi ca             ru -> u after a, before haś (voiced)
  6.1.87 ād guṇaḥ             a + u -> o   (bhargas + d -> bhargo d)
  8.3.15 kharavasānayor visarjanīyaḥ   r(u) -> ḥ before khar or at pause
  8.3.23 mo'nusvāraḥ          pada-final m -> ṃ before a consonant
  (ru before a voiced consonant stays r: savitur vareṇyam)

Facts certified:
 T1  Line 1  tat savitur vareṇyaṃ bhargo devasya dhīmahi   = oracle
     Line 2/3 dhiyo yo naḥ pracodayāt                        = oracle
     (the Vedic text's lines: tat savitur vareṇyam | bhargo devasya dhīmahi |
      dhiyo yo naḥ pracodayāt)
 T2  Pada provenance is counted, not blurred: 5 padas DERIVED by the sūtra
     engine (theorum/63/65), 5 GIVEN as tokens (dhīmahi, dhiyas, yas, nas,
     pracodayāt) with the missing sector named for each.
 T3  Controls: ru before a voiced consonant must NOT become visarga
     (planted unconditional 8.3.15 gives *savituḥ vareṇyam); 6.1.114 without
     6.1.87 leaves *bhargau? no -- leaves *bhargau is wrong: leaves bhargau→
     certified: without 6.1.87 the seam stays a+u (bhargaudevasya).
 T4  Confluence (theorum/60 engine): unique normal form for each line under
     free application; every seam rule pair commutes or is 8.2.1-ordered.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.seam_compensated_confluence_verdict import verdict

VOW = {"a", "A", "i", "I", "u", "U", "R", "e", "o", "ai", "au"}
HAS = set("gjdbnmyrlvh") | {"gh", "jh", "dh", "bh", "G", "N"}  # haś: voiced
KHAR = set("kctpSzs") | {"kh", "ch", "th", "ph"}

# a pada = tuple of phones; a line = tuple of padas
Line = tuple[tuple[str, ...], ...]


def _replace(line: Line, i: int, pada: tuple[str, ...]) -> Line:
    return line[:i] + (pada,) + line[i + 1 :]


def r_8_2_66(L: Line):
    for i, p in enumerate(L):
        if p and p[-1] == "s":
            return _replace(L, i, p[:-1] + ("ru",))
    return None


def r_6_1_113(L: Line):
    for i, p in enumerate(L[:-1]):
        if len(p) >= 2 and p[-1] == "ru" and p[-2] == "a" and L[i + 1][0] == "a":
            return _replace(L, i, p[:-1] + ("u",))
    return None


def r_6_1_114(L: Line):
    for i, p in enumerate(L[:-1]):
        if len(p) >= 2 and p[-1] == "ru" and p[-2] == "a" and L[i + 1][0] in HAS:
            return _replace(L, i, p[:-1] + ("u",))
    return None


def r_6_1_87(L: Line):
    for i, p in enumerate(L):
        if len(p) >= 2 and p[-2] == "a" and p[-1] == "u":
            return _replace(L, i, p[:-2] + ("o",))
    return None


def r_8_3_15(L: Line):
    for i, p in enumerate(L):
        if p and p[-1] in ("ru", "r") and (i == len(L) - 1 or L[i + 1][0] in KHAR):
            return _replace(L, i, p[:-1] + ("H",))
    return None


def r_8_3_23(L: Line):
    for i, p in enumerate(L[:-1]):
        if p and p[-1] == "m" and L[i + 1][0] not in VOW:
            return _replace(L, i, p[:-1] + ("M",))
    return None


RULES: list[tuple[str, Callable]] = [("6.1.87", r_6_1_87), ("6.1.113", r_6_1_113), ("6.1.114", r_6_1_114), ("8.2.66", r_8_2_66), ("8.3.15", r_8_3_15), ("8.3.23", r_8_3_23)]


def render(L: Line) -> str:
    return " ".join("".join({"ru": "r"}.get(ph, ph) for ph in p) for p in L)


def tok(s: str) -> tuple[str, ...]:
    out, i = [], 0
    while i < len(s):
        if s[i : i + 2] in ("ai", "au", "kh", "gh", "ch", "jh", "th", "dh", "ph", "bh"):
            out.append(s[i : i + 2]); i += 2
        else:
            out.append(s[i]); i += 1
    return tuple(out)


# pada-final forms before pause rules; provenance
PADAS = {
    "tat": ("DERIVED theorum/65", "tat"), "savitur": ("DERIVED theorum/65 (before 8.3.15)", "savitur"),
    "vareNyam": ("DERIVED theorum/65", "vareNyam"), "bhargas": ("DERIVED theorum/65 (before 8.2.66)", "bhargas"),
    "devasya": ("DERIVED theorum/65", "devasya"), "dhImahi": ("GIVEN: chandasi bahulam (theorum/66)", "dhImahi"),
    "dhiyas": ("GIVEN: ī-stem + śas, 6.4.77 iyaṅ not modelled", "dhiyas"), "yas": ("GIVEN: sarvanāma yad + su (7.2.102/7.2.106) masc not modelled", "yas"),
    "nas": ("GIVEN: asmad + śas → nas (8.1.21) not modelled", "nas"), "pracodayAt": ("GIVEN: ṇic + loṭ/liṅ (āśīrliṅ pracodayāt) not modelled", "pracodayAt"),
}
LINES = {
    "line1": (["tat", "savitur", "vareNyam", "bhargas", "devasya", "dhImahi"], "tat savitur vareNyaM bhargo devasya dhImahi"),
    "line2": (["dhiyas", "yas", "nas", "pracodayAt"], "dhiyo yo naH pracodayAt"),
}


def derive(L: Line, rules) -> tuple[Line, list[str]]:
    path = []
    for _ in range(40):
        for sid, fn in sorted(rules, key=lambda r: (r[0].startswith("8."), r[0])):  # 8.2.1: tripādī waits
            L2 = fn(L)
            if L2 is not None and L2 != L:
                path.append(sid)
                L = L2
                break
        else:
            return L, path
    raise AssertionError("no normal form")


def build_certificate() -> dict[str, Any]:
    results, paths = {}, {}
    for name, (padas, oracle) in LINES.items():
        L0 = tuple(tok(PADAS[p][1]) for p in padas)
        L, p = derive(L0, RULES)
        results[name] = render(L)
        paths[name] = p
    sound = {n: results[n] == LINES[n][1] for n in LINES}
    # controls
    planted = [(s, (lambda L: next((_replace(L, i, p[:-1] + ("H",)) for i, p in enumerate(L) if p and p[-1] in ("ru", "r")), None))) if s == "8.3.15" else (s, f) for s, f in RULES]
    L0 = tuple(tok(PADAS[p][1]) for p in LINES["line1"][0])
    planted_line = render(derive(L0, planted)[0])
    no87 = [r for r in RULES if r[0] != "6.1.87"]
    no87_line = render(derive(L0, no87)[0])
    # T4 confluence per line via theorum/60 engine (rules as step functions)
    conf = {}
    for name, (padas, _) in LINES.items():
        L0 = tuple(tok(PADAS[p][1]) for p in padas)
        v = verdict(L0, [(s, f) for s, f in RULES], lambda a, b: a == b, priority=False)
        conf[name] = {"verdict": v["verdict"], "open": v["open"], "nfs": v["normal_forms_mod_ledger"]}
    prov = {p: PADAS[p][0] for line in LINES.values() for p in line[0]}
    n_derived = sum(v.startswith("DERIVED") for v in prov.values())
    checks = {
        "T1_both_lines_match_oracle": all(sound.values()),
        "T2_provenance_5_derived_5_given": n_derived == 5 and len(prov) == 10,
        "T3_planted_unconditional_visarga_breaks_savitur_v": "savituH vareNyaM" in planted_line,
        "T3_without_6_1_87_seam_stays_a_u_no_bhargo": no87_line != results["line1"] and "bhargo" not in no87_line and "bharga" in no87_line,
        "T4_each_line_confluent_unique_nf": all(c["verdict"] == "CONFLUENT_MOD_LEDGER" for c in conf.values()),
    }
    status = "PASS_PADA_TO_LINE_EXTERNAL_SANDHI_CANDIDATE" if all(checks.values()) else "FAIL_PADA_TO_LINE_EXTERNAL_SANDHI_CANDIDATE"
    return {
        "schema": "rkf.pada_to_line_external_sandhi_candidate.v1",
        "status": status,
        "lines": results,
        "paths": paths,
        "provenance": prov,
        "controls": {"planted_unconditional_8_3_15": planted_line, "without_6_1_87": no87_line},
        "confluence": conf,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Gāyatrī lines from their padas by 8.2.66, 6.1.113/114, 6.1.87, 8.3.15 (khar/avasāna only), 8.3.23 = the received text",
                "ru before a voiced consonant stays r (savitur vareṇyam); bhargas + d -> bhargo d through ruḥ -> u -> guṇa",
                "each line has a unique normal form under free application (theorum/60 verdict)",
            ],
            "NOT_claimed": ["the five GIVEN padas (provenance table names each missing sector)", "accent; jihvāmūlīya/upadhmānīya options; avagraha", "RH, YM untouched"],
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
    print("LINES", payload["lines"], "CONTROLS", payload["controls"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
