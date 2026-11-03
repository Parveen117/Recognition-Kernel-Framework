"""The san (desiderative) lane: laṭ / laṅ / loṭ / vidhiliṅ of every root the tiṅ engine declares, with san
(3.1.7), in both padas (1.3.62 pūrvavat sanaḥ), as vidyut-prakriya derives them — a DECLARED oracle of
implementation grade, kept as data (theorum/149), in the form of the earlier lanes. Keys: root|SP or SA|lakāra|cell.

    python -m research.independent_oracle.san_lane --data /tmp/vidyut_data/prakriya
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
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "VIDYUT_SAN_LANE.json")); a = ap.parse_args()
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
        dh = vp.Dhatu.mula(hit[1], GANA[g]).with_sanadi([vp.Sanadi.san])
        for pd, dp in (("SP", vp.DhatuPada.Parasmaipada), ("SA", vp.DhatuPada.Atmanepada)):
            for l in LAKS:
                for c in TIN.CODES:
                    try:
                        ps = v.derive(vp.Pada.Tinanta(dhatu=dh, prayoga=vp.Prayoga.Kartari, lakara=LAK[l], purusha=PUR[c[0]], vacana=VAC[c[1]], dhatu_pada=dp))
                    except Exception:  # noqa: BLE001
                        continue
                    forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
                    if not forms:
                        empty += 1; continue
                    cells[f"{r}|{pd}|{l}|{c}"] = forms
    Path(a.out).write_text(json.dumps({"source": "vidyut-prakriya 0.4.0 (ambuda-org/vidyut), kartari with san, both padas, all alternatives in vidyut's order", "lakaras": LAKS, "cells": cells}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(cells), "cells;", empty, "empty")


if __name__ == "__main__":
    main()
