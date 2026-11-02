"""The karmaṇi (passive) lane: laṭ / laṅ / loṭ / vidhiliṅ of every root the tiṅ engine declares, in the
karmaṇi prayoga, as vidyut-prakriya derives them — a DECLARED oracle of implementation grade, kept as data
(theorum/147), in the form of the earlier lanes. The pada is ātmanepada by 1.3.13; one row per root.

    python -m research.independent_oracle.karmani_lane --data /tmp/vidyut_data/prakriya
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import vidyut.prakriya as vp

from proof_lab import ting_rule_table_engine as TIN
from research.independent_oracle.crosscheck import GANA, LAK, PUR, VAC, find_dhatu, iast, load_dhatus

HERE = Path(__file__).resolve().parent
LAKS = ("laṭ", "laṅ", "loṭ", "liṅ")


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "VIDYUT_KARMANI_LANE.json")); a = ap.parse_args()
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
        for l in LAKS:
            for c in TIN.CODES:
                try:
                    ps = v.derive(vp.Pada.Tinanta(dhatu=dh, prayoga=vp.Prayoga.Karmani, lakara=LAK[l], purusha=PUR[c[0]], vacana=VAC[c[1]]))
                except Exception:  # noqa: BLE001
                    continue
                forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
                if not forms:
                    empty += 1; continue
                cells[f"{r}|K|{l}|{c}"] = forms
    Path(a.out).write_text(json.dumps({"source": "vidyut-prakriya 0.4.0 (ambuda-org/vidyut), karmaṇi, all alternatives in vidyut's order", "lakaras": LAKS, "cells": cells}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(cells), "cells;", empty, "empty")


if __name__ == "__main__":
    main()
