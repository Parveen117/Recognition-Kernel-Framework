"""The kṛt lane: eight kṛt affixes — kta, ktavatu (3.2.102), tavya, anīyar (3.1.96), tumun (3.3.10), ktvā (3.4.21),
tṛc, ṇvul (3.1.133) — on every root the tiṅ engine declares, as vidyut-prakriya derives the prātipadika — a
DECLARED oracle of implementation grade, kept as data (theorum/151), in the form of the earlier lanes.
Keys: root|K|affix.

    python -m research.independent_oracle.krt_lane --data /tmp/vidyut_data/prakriya
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import vidyut.prakriya as vp

from proof_lab import ting_rule_table_engine as TIN
from research.independent_oracle.crosscheck import GANA, find_dhatu, iast, load_dhatus

HERE = Path(__file__).resolve().parent
KRT = {"kta": vp.Krt.kta, "ktavatu": vp.Krt.ktavatu, "tavya": vp.Krt.tavya, "anīya": vp.Krt.anIyar, "tumun": vp.Krt.tumun, "ktvā": vp.Krt.ktvA, "tṛc": vp.Krt.tfc, "ṇvul": vp.Krt.Rvul}


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "VIDYUT_KRT_LANE.json")); a = ap.parse_args()
    by = load_dhatus(a.data); v = vp.Vyakarana()
    roots = {}
    for r, l, cs, pd in TIN.SUITE:
        if r in TIN.NASAL:
            up, g, _, _ = TIN.NASAL[r]
        else:
            up, _ = TIN.ROOTS[r]; g = TIN.GANA.get(r, 1)
        roots[r] = (up, g)
    cells = {}; empty = 0
    for r, (up, g) in sorted(roots.items()):
        hit = find_dhatu(by, up, g)
        if hit is None:
            continue
        dh = vp.Dhatu.mula(hit[1], GANA[g])
        for name, k in KRT.items():
            try:
                ps = v.derive(vp.Pratipadika.krdanta(dh, k))
            except Exception:  # noqa: BLE001
                continue
            forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
            if not forms:
                empty += 1; continue
            cells[f"{r}|K|{name}"] = forms
    Path(a.out).write_text(json.dumps({"source": "vidyut-prakriya 0.4.0 (ambuda-org/vidyut), the kṛdanta prātipadika, all alternatives in vidyut's order", "affixes": list(KRT), "cells": cells}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(cells), "cells;", empty, "empty")


if __name__ == "__main__":
    main()
