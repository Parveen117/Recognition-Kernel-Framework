"""Verify every sūtra quoted in §A of theorum/118 and theorum/119 against the pinned sūtrapāṭha (PG1).

python -m research.samasa_construction.verify_quotes
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from proof_lab.astadhyayi_ledger import deva_to_iast

ROOT = Path(__file__).resolve().parents[2]
CAPSULES = [ROOT / "theorum/118_samasa_mathematical_construction_theorem.md", ROOT / "theorum/119_samasa_construction_ii_uttarapada_aluk_samasanta_theorem.md"]
TSV = ROOT / "research/panini_grammar/SUTRAPATHA.tsv"


def _norm(s: str) -> str:
    s = s.replace("'", "").replace("’", "").replace(" ", "").lower()
    return re.sub(r"[ṁṃ]", "m", s).replace("ṅ", "n").replace("ñ", "n").replace("ṇ", "n")


def main() -> int:
    pinned = {r[0]: r[-1] for r in csv.reader(TSV.open(encoding="utf-8"), delimiter="\t")}
    items = []
    for cap in CAPSULES:
        text = cap.read_text(encoding="utf-8")
        block = text[text.index("## A. Sources"):]
        block = block[block.index("```text") + 7: block.index("```", block.index("```text") + 7)]
        items += [(cap.name, x.strip()) for line in block.splitlines() for x in line.split(" · ") if x.strip()]
    out, bad = {}, []
    for cap_name, it in items:
        n, q = it.split(" ", 1)
        p = pinned.get(n)
        if p is None:
            bad.append((n, q, "ABSENT")); continue
        pi = deva_to_iast(p)
        ok = _norm(pi) == _norm(q)
        out[n] = {"quoted": q, "pinned_devanagari": p, "pinned_iast": pi, "match": ok, "capsule": sorted(set(out.get(n, {}).get("capsule", []) + [cap_name]))}
        if not ok:
            bad.append((n, q, pi))
    (ROOT / "research/samasa_construction/QUOTES_VERIFIED.json").write_text(json.dumps({"quoted": len(items), "mismatch": len(bad), "entries": out}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"quoted {len(items)}, mismatches {len(bad)}")
    for b in bad:
        print("  ", b)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
