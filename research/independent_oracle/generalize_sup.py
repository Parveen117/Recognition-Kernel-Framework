"""Generalisation test for the sup engine: new stems of every class the engine declares, against vidyut-prakriya.

    python -m research.independent_oracle.generalize_sup --data /tmp/vidyut_data/prakriya

Each stem is given with the class flags the engine reads (the same flags the suite stems carry) and the
vidyut input that names the same word; all 24 cells (8s / 8d / 8p vocatives included) are compared.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import vidyut.prakriya as vp

from proof_lab import sup_rule_table_engine as SUP
from research.independent_oracle.crosscheck import LINGA, VAC, VIB, iast, slp

HERE = Path(__file__).resolve().parent

# (name, engine stem, gender, flags, vidyut pratipadika spec)
NEW = [
    ("deva", "deva", "m", (), ("basic", "deva")), ("nara", "nara", "m", (), ("basic", "nara")), ("vṛkṣa", "vṛkṣa", "m", (), ("basic", "vfkza")), ("putra", "putra", "m", (), ("basic", "putra")),
    ("jñāna", "jñāna", "n", (), ("basic", "jYAna")), ("vana", "vana", "n", (), ("basic", "vana")), ("puṣpa", "puṣpa", "n", (), ("basic", "puzpa")),
    ("senā", "senā", "f", ("āp",), ("basic-f", "senA")), ("kanyā", "kanyā", "f", ("āp",), ("basic-f", "kanyA")), ("māyā", "māyā", "f", ("āp",), ("basic-f", "mAyA")),
    ("devī", "devī", "f", ("nadī",), ("basic", "devI")), ("gaurī", "gaurī", "f", ("nadī",), ("basic", "gOrI")), ("vāpī", "vāpī", "f", ("nadī",), ("basic", "vApI")),
    ("muni", "muni", "m", (), ("basic", "muni")), ("agni", "agni", "m", (), ("basic", "agni")), ("kavi", "kavi", "m", (), ("basic", "kavi")),
    ("śakti", "śakti", "f", (), ("basic", "Sakti")), ("buddhi", "buddhi", "f", (), ("basic", "budDi")),
    ("śatru", "śatru", "m", (), ("basic", "Satru")), ("bhānu", "bhānu", "m", (), ("basic", "BAnu")), ("sādhu", "sādhu", "m", (), ("basic", "sADu")),
    ("ambu", "ambu", "n", (), ("basic", "ambu")), ("aśru", "aśru", "n", (), ("basic", "aSru")),
    ("dātṛ", "dātṛ", "m", ("tṛ", "ṛ"), ("krdanta", "qudA\\Y", "Juhotyadi", "tfc")), ("bhartṛ", "bhartṛ", "m", ("tṛ", "ṛ"), ("krdanta", "Bf\\Y", "Bhvadi", "tfc")),
    ("bhrātṛ", "bhrātṛ", "m", ("ṛ",), ("basic", "BrAtf")), ("duhitṛ", "duhitṛ", "f", ("ṛ",), ("basic", "duhitf")), ("naptṛ", "naptṛ", "m", ("tṛ", "ṛ"), ("basic", "naptf")),
    ("brahman", "brahman", "n", ("an",), ("basic", "brahman")), ("karman", "karman", "n", ("an",), ("basic", "karman")), ("nāman", "nāman", "n", ("an",), ("basic", "nAman")),
    ("yajvan", "yajvan", "m", ("an",), ("basic", "yajvan")),
    ("suhṛd", "suhṛd", "m", (), ("basic", "suhfd")), ("jagat", "jagat", "n", (), ("basic", "jagat")), ("sarit", "sarit", "f", (), ("basic", "sarit")), ("vidyut", "vidyut", "f", (), ("basic", "vidyut")),
    ("payas", "payas", "n", (), ("basic", "payas")), ("tejas", "tejas", "n", (), ("basic", "tejas")), ("yaśas", "yaśas", "n", (), ("basic", "yaSas")),
    ("yogin", "yogin", "m", ("in",), ("basic", "yogin")), ("hastin", "hastin", "m", ("in",), ("basic", "hastin")), ("balin", "balin", "m", ("in",), ("basic", "balin")),
    ("anya", "anya", "m", ("sarvanāma",), ("basic", "anya")), ("viśva", "viśva", "m", ("sarvanāma",), ("basic", "viSva")), ("eka", "eka", "m", ("sarvanāma",), ("basic", "eka")),
    ("anyā", "anyā", "f", ("sarvanāma", "āp"), ("basic", "anya")), ("anya_n", "anya", "n", ("sarvanāma",), ("basic", "anya")),
    ("pūrva", "pūrva", "m", ("sarvanāma",), ("basic", "pUrva")), ("para", "para", "m", ("sarvanāma",), ("basic", "para")),
]


def prat(spec):
    kind = spec[0]
    if kind == "basic":
        return vp.Pratipadika.basic(spec[1])
    if kind == "basic-f":
        return vp.Pratipadika.basic(spec[1][:-1] + "a")
    if kind == "krdanta":
        return vp.Pratipadika.krdanta(vp.Dhatu.mula(spec[1], getattr(vp.Gana, spec[2])), getattr(vp.Krt, spec[3]))
    raise ValueError(kind)


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "GENERALIZE_SUP.json")); a = ap.parse_args()
    v = vp.Vyakarana()
    rows = []
    for name, stem, g, flags, spec in NEW:
        try:
            pr = prat(spec)
        except Exception as e:  # noqa: BLE001
            rows.append({"stem": name, "status": "NO_VIDYUT_INPUT", "error": str(e)}); continue
        for c, up in SUP.SUP:
            try:
                ours, path = SUP.decline(stem, c, up, g, flags)
            except Exception as e:  # noqa: BLE001
                rows.append({"stem": name, "cell": c, "status": "ENGINE_ERROR", "error": str(e)}); continue
            try:
                ps = v.derive(vp.Pada.Subanta(pratipadika=pr, linga=LINGA[g], vibhakti=VIB[c[0]], vacana=VAC[c[1]]))
            except Exception as e:  # noqa: BLE001
                rows.append({"stem": name, "cell": c, "ours": ours, "status": "VIDYUT_ERROR", "error": str(e)}); continue
            forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
            status = "AGREE" if ours in forms else ("VIDYUT_EMPTY" if not forms else "DIFFER")
            rows.append({"stem": name, "gender": g, "flags": list(flags), "cell": c, "ours": ours, "vidyut": forms, "status": status, "our_path": [x.split(" ")[0] for x in path[1:]]})
    st = Counter(r["status"] for r in rows)
    by_stem = defaultdict(Counter)
    for r in rows:
        by_stem[r["stem"]][r["status"]] += 1
    report = {"vidyut_version": "0.4.0", "cells": len(rows), "status": dict(st), "by_stem": {k: dict(v) for k, v in by_stem.items()}, "rows": rows}
    Path(a.out).write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(rows), dict(st))
    for r in rows:
        if r["status"] == "DIFFER":
            print("  DIFFER", r["stem"], r["cell"], r["ours"], r["vidyut"][:3])


if __name__ == "__main__":
    main()
