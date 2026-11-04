"""The kṛdanta declension lane: the sup forms of the kṛdanta prātipadika (theorum/151–152's affixes) of every root the
tiṅ engine declares, in the three genders, as vidyut-prakriya derives them — a DECLARED oracle of implementation grade,
kept as data (theorum/153), in the form of the earlier lanes. Keys: root|affix|gender|cell. Masculine: all 22 cells
of the eight declinable affixes; neuter (not tṛc) and feminine (not ṇvul: 7.3.44 is read as theorum/111 reads it, the
generator otherwise) on nine cells.

    python -m research.independent_oracle.krdanta_sup_lane --data /tmp/vidyut_data/prakriya
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import vidyut.prakriya as vp

from proof_lab import ting_rule_table_engine as TIN
from research.independent_oracle.crosscheck import GANA, LINGA, VAC, VIB, find_dhatu, iast, load_dhatus
from research.independent_oracle.krt_lane import KRT, KRT_PADA, PADA_KRT

HERE = Path(__file__).resolve().parent
CELLS_M = [f"{v}{n}" for v in "1234567" for n in "sdp"] + ["8s"]
CELLS_9 = ["1s", "1d", "1p", "2s", "3s", "4s", "6p", "7s", "8s"]
DECLINABLE = ["kta", "ktavatu", "tavya", "anīya", "tṛc", "ṇvul", "śatṛ", "śānac"]


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "VIDYUT_KRDANTA_SUP_LANE.json")); a = ap.parse_args()
    by = load_dhatus(a.data); v = vp.Vyakarana()
    roots = {}
    for r, l, cs, pd in TIN.SUITE:
        if r in TIN.NASAL:
            up, g, pd0, _ = TIN.NASAL[r]
        else:
            up, pd0 = TIN.ROOTS[r]; g = TIN.GANA.get(r, 1)
        roots[r] = (up, g, pd0)
    cells = {}; empty = 0
    for r, (up, g, pd0) in sorted(roots.items()):
        hit = find_dhatu(by, up, g)
        if hit is None:
            continue
        dh = vp.Dhatu.mula(hit[1], GANA[g])
        for name in DECLINABLE:
            if name in KRT_PADA and pd0 not in PADA_KRT[name]:
                continue
            kd = vp.Pratipadika.krdanta(dh, KRT.get(name) or KRT_PADA[name])
            for gender, cs in (("m", CELLS_M), ("n", CELLS_9), ("f", CELLS_9)):
                if (gender == "n" and name == "tṛc") or (gender == "f" and name == "ṇvul"):
                    continue
                for c in cs:
                    try:
                        ps = v.derive(vp.Pada.Subanta(pratipadika=kd, linga=LINGA[gender], vibhakti=VIB[c[0]], vacana=VAC[c[1]]))
                    except Exception:  # noqa: BLE001
                        continue
                    forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
                    if not forms:
                        empty += 1; continue
                    cells[f"{r}|{name}|{gender}|{c}"] = forms
    Path(a.out).write_text(json.dumps({"source": "vidyut-prakriya 0.4.0 (ambuda-org/vidyut), the sup forms of the kṛdanta prātipadika, all alternatives in vidyut's order", "cells": cells}, indent=0, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(cells), "cells;", empty, "empty")


if __name__ == "__main__":
    main()
