"""Generalisation test: the tiṅ engine on cells OUTSIDE its certified / declared suite, against vidyut-prakriya.

For every root the engine knows, derive the full nine-cell paradigm in the lakāras the
engine covers for that class, and compare with vidyut.  The suite cells are excluded, so
every cell counted here is one the rows were never fitted to.  Output: GENERALIZE.json
(pinned by hash in the capsule) and the summary printed here.

    python -m research.independent_oracle.generalize --data /tmp/vidyut_data/prakriya
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import vidyut.prakriya as vp

from proof_lab import ting_rule_table_engine as TIN
from research.independent_oracle.crosscheck import GANA, LAK, PUR, VAC, find_dhatu, iast, load_dhatus

HERE = Path(__file__).resolve().parent
PRESENT = ("laṭ", "laṅ", "loṭ", "liṅ")


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "GENERALIZE.json")); a = ap.parse_args()
    by = load_dhatus(a.data); v = vp.Vyakarana()
    suite = {(r, l, c, pd) for r, l, cs, pd in TIN.SUITE for c in cs}
    # (root, pada) pairs the engine declares, with the lakāras its rows cover for that root's class
    targets: dict[tuple[str, str], tuple] = {}
    for r, l, cs, pd in TIN.SUITE:
        if r in TIN.NASAL:
            up, g, pd0, _ = TIN.NASAL[r]
        else:
            up, pd0 = TIN.ROOTS[r]; g = TIN.GANA.get(r, 1)
        pada = pd or pd0
        laks = PRESENT if g != 1 or r in ("pac",) else ("laṭ", "laṅ", "loṭ", "liṅ", "lṛṭ", "luṭ", "luṅ")
        if r in ("bhū", "gam", "nī", "edh", "labh"):
            laks = ("laṭ", "laṅ", "loṭ", "liṅ", "lṛṭ", "luṭ", "luṅ", "āśīrliṅ")
        targets[(r, pada)] = (up, g, laks)
    rows = []
    for (r, pada), (up, g, laks) in sorted(targets.items()):
        hit = find_dhatu(by, up, g)
        if hit is None:
            continue
        dh = vp.Dhatu.mula(hit[1], GANA[g])
        for l in laks:
            for c in TIN.CODES:
                if (r, l, c, pada) in suite:
                    continue
                try:
                    ours, path = TIN.conjugate(r, l, c, pada=pada)
                except Exception as e:  # noqa: BLE001
                    rows.append({"root": r, "pada": pada, "lakara": l, "cell": c, "status": "ENGINE_ERROR", "error": str(e)}); continue
                try:
                    ps = v.derive(vp.Pada.Tinanta(dhatu=dh, prayoga=vp.Prayoga.Kartari, lakara=LAK[l], purusha=PUR[c[0]], vacana=VAC[c[1]],
                                                  dhatu_pada=vp.DhatuPada.Parasmaipada if pada == "P" else vp.DhatuPada.Atmanepada))
                except Exception as e:  # noqa: BLE001
                    rows.append({"root": r, "pada": pada, "lakara": l, "cell": c, "ours": ours, "status": "VIDYUT_ERROR", "error": str(e)}); continue
                forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
                status = "AGREE" if ours in forms else ("VIDYUT_EMPTY" if not forms else "DIFFER")
                rows.append({"root": r, "upadesa": up, "gana": g, "pada": pada, "lakara": l, "cell": c, "ours": ours, "vidyut": forms, "status": status,
                             "our_path": [x.split(" ")[0] for x in path[1:]]})
    st = Counter(r["status"] for r in rows)
    by_lak = defaultdict(Counter)
    for r in rows:
        by_lak[r["lakara"]][r["status"]] += 1
    differ = [r for r in rows if r["status"] == "DIFFER"]
    by_root = Counter((r["root"], r["lakara"]) for r in differ)
    report = {"vidyut_version": "0.4.0", "cells": len(rows), "status": dict(st), "by_lakara": {k: dict(v) for k, v in by_lak.items()},
              "differ_by_root_lakara": [[k[0], k[1], n] for k, n in by_root.most_common()], "rows": rows}
    Path(a.out).write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(rows), dict(st)); print({k: dict(v) for k, v in by_lak.items()})
    for d in differ[:80]:
        print("  DIFFER", d["root"], d["pada"], d["lakara"], d["cell"], d["ours"], d["vidyut"])


if __name__ == "__main__":
    main()
