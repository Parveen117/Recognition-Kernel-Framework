"""The ārdhadhātuka open lane: lṛṭ, luṭ, āśīrliṅ, liṭ, luṅ (and lṛṅ) of every (root, pada) the tiṅ engine
declares, as vidyut-prakriya derives them — a DECLARED oracle of implementation grade, kept as data
(theorum/144), in the form of VIDYUT_OPEN_LANE.json (theorum/139).

    python -m research.independent_oracle.ardhadhatuka_lane --data /tmp/vidyut_data/prakriya
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import vidyut.prakriya as vp

from proof_lab import ting_rule_table_engine as TIN
from research.independent_oracle.crosscheck import GANA, LAK, PUR, VAC, find_dhatu, iast, load_dhatus

HERE = Path(__file__).resolve().parent
LAKS = ("lṛṭ", "luṭ", "āśīrliṅ", "liṭ", "luṅ", "lṛṅ")
LAK2 = {**LAK, "lṛṅ": vp.Lakara.Lrn}


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "VIDYUT_ARDHADHATUKA_LANE.json")); a = ap.parse_args()
    by = load_dhatus(a.data); v = vp.Vyakarana()
    suite = {(r, l, c, pd) for r, l, cs, pd in TIN.SUITE for c in cs}
    targets = {}
    for r, l, cs, pd in TIN.SUITE:
        if r in TIN.NASAL:
            up, g, pd0, _ = TIN.NASAL[r]
        else:
            up, pd0 = TIN.ROOTS[r]; g = TIN.GANA.get(r, 1)
        pada = {"NP": "P", "NA": "A", "SP": "P", "SA": "A", "K": None}.get(pd, pd) or pd0   # a ṇic / san / karmaṇi suite cell names the root's kartari pada for this lane (theorum/160)
        if pada == "U":
            pada = "P"
        targets[(r, pada)] = (up, g)
    cells = {}; empty = 0
    for (r, pada), (up, g) in sorted(targets.items()):
        hit = find_dhatu(by, up, g)
        if hit is None:
            continue
        dh = vp.Dhatu.mula(hit[1], GANA[g])
        for l in LAKS:
            for c in TIN.CODES:
                if (r, l, c, pada) in suite:
                    continue
                try:
                    ps = v.derive(vp.Pada.Tinanta(dhatu=dh, prayoga=vp.Prayoga.Kartari, lakara=LAK2[l], purusha=PUR[c[0]], vacana=VAC[c[1]],
                                                  dhatu_pada=vp.DhatuPada.Parasmaipada if pada == "P" else vp.DhatuPada.Atmanepada))
                except Exception:  # noqa: BLE001
                    continue
                forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
                if not forms:
                    empty += 1; continue
                cells[f"{r}|{pada}|{l}|{c}"] = forms
    Path(a.out).write_text(json.dumps({"source": "vidyut-prakriya 0.4.0 (ambuda-org/vidyut), kartari, all alternatives in vidyut's order", "lakaras": LAKS, "cells": cells}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(cells), "cells;", empty, "empty")


if __name__ == "__main__":
    main()
