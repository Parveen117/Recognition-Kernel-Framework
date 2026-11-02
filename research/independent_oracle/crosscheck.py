"""Independent-oracle cross-check of the two rule-table engines against vidyut-prakriya.

vidyut-prakriya (ambuda-org/vidyut, Rust, open source) derives Sanskrit forms by the
Aṣṭādhyāyī and records the sūtra applied at every step.  It was written without any
knowledge of this repository, from the same primary text, so it is an independent
oracle for BOTH the surface forms and the rule attributions of the engines
(proof_lab/sup_rule_table_engine.py, proof_lab/ting_rule_table_engine.py).

The script is not part of CI (it needs the vidyut package and its data download);
its output is pinned as research/independent_oracle/CROSSCHECK.json and summarised
in CROSSCHECK.md.  Run:

    pip install vidyut==0.4.0 ; python -c "import vidyut; vidyut.download_data('/tmp/vidyut_data')"
    python -m research.independent_oracle.crosscheck --data /tmp/vidyut_data/prakriya

Every disagreement is data, not a verdict: it is adjudicated against the pinned
sūtrapāṭha and the commentaries in the theorem capsule that cites this file.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import vidyut.lipi as L
import vidyut.prakriya as vp

from proof_lab import sup_rule_table_engine as SUP
from proof_lab import ting_rule_table_engine as TIN

HERE = Path(__file__).resolve().parent


def slp(iast: str) -> str:
    return L.transliterate(iast, L.Scheme.Iast, L.Scheme.Slp1)


def iast(s: str) -> str:
    return L.transliterate(s, L.Scheme.Slp1, L.Scheme.Iast)


def strip_accents(a: str) -> str:
    return a.replace("\\", "").replace("^", "")


GANA = {1: vp.Gana.Bhvadi, 2: vp.Gana.Adadi, 3: vp.Gana.Juhotyadi, 4: vp.Gana.Divadi, 5: vp.Gana.Svadi, 6: vp.Gana.Tudadi,
        7: vp.Gana.Rudhadi, 8: vp.Gana.Tanadi, 9: vp.Gana.Kryadi, 10: vp.Gana.Curadi}
LAK = {"laṭ": vp.Lakara.Lat, "laṅ": vp.Lakara.Lan, "loṭ": vp.Lakara.Lot, "liṅ": vp.Lakara.VidhiLin, "lṛṭ": vp.Lakara.Lrt, "luṭ": vp.Lakara.Lut,
       "āśīrliṅ": vp.Lakara.AshirLin, "luṅ": vp.Lakara.Lun, "liṭ": vp.Lakara.Lit}
PUR = {"3": vp.Purusha.Prathama, "2": vp.Purusha.Madhyama, "1": vp.Purusha.Uttama}
VAC = {"s": vp.Vacana.Eka, "d": vp.Vacana.Dvi, "p": vp.Vacana.Bahu}
VIB = {"1": vp.Vibhakti.Prathama, "2": vp.Vibhakti.Dvitiya, "3": vp.Vibhakti.Trtiya, "4": vp.Vibhakti.Caturthi, "5": vp.Vibhakti.Panchami,
       "6": vp.Vibhakti.Sasthi, "7": vp.Vibhakti.Saptami, "8": vp.Vibhakti.Sambodhana}
LINGA = {"m": vp.Linga.Pum, "f": vp.Linga.Stri, "n": vp.Linga.Napumsaka}
META_PREFIX = ("1.1.", "1.2.", "1.3.", "1.4.", "8.4.68")   # saṁjñā / paribhāṣā / it steps: not compared as attributions


def norm_rule(r: str) -> str:
    return re.sub(r"[a-z]+$", "", r)


def load_dhatus(data_dir: str):
    data = vp.Data(data_dir)
    by = {}
    for e in data.load_dhatu_entries():
        a = e.dhatu.aupadeshika
        key = (strip_accents(a).replace("~", ""), e.dhatu.gana.name)
        by.setdefault(key, []).append((e.code, a, e.dhatu.gana))
    return by


GANA_NAME = {1: "Bhvadi", 2: "Adadi", 3: "Juhotyadi", 4: "Divadi", 5: "Svadi", 6: "Tudadi", 7: "Rudhadi", 8: "Tanadi", 9: "Kryadi", 10: "Curadi"}


def find_dhatu(by, upadesa: str, gana: int):
    key = (slp(upadesa).replace("~", ""), GANA_NAME[gana])
    hits = by.get(key, [])
    return hits[0] if hits else None


def ting_cross(by) -> dict:
    v = vp.Vyakarana()
    rows = []
    for root, lak, cells, pada in TIN.SUITE:
        if root in TIN.NASAL:
            up, g, pd0, _ = TIN.NASAL[root]
        else:
            up, pd0 = TIN.ROOTS[root]; g = TIN.GANA.get(root, 1)
        pada = pada or pd0
        hit = find_dhatu(by, up, g)
        if hit is None:
            rows.append({"root": root, "lakara": lak, "status": "NO_VIDYUT_ENTRY", "upadesa": up, "gana": g}); continue
        code, aup, _ = hit
        dh = vp.Dhatu.mula(aup, GANA[g])
        for c in cells:
            ours, path = TIN.conjugate(root, lak, c, pada=pada)
            our_rules = sorted({norm_rule(x.split(" ")[0]) for x in path[1:]})
            try:
                ps = v.derive(vp.Pada.Tinanta(dhatu=dh, prayoga=vp.Prayoga.Kartari, lakara=LAK[lak], purusha=PUR[c[0]], vacana=VAC[c[1]],
                                              dhatu_pada=vp.DhatuPada.Parasmaipada if pada == "P" else vp.DhatuPada.Atmanepada))
            except Exception as e:  # noqa: BLE001
                rows.append({"root": root, "lakara": lak, "cell": c, "pada": pada, "ours": ours, "status": "VIDYUT_ERROR", "error": str(e)}); continue
            forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
            vrules = sorted({s.code for p in ps for s in p.history if not s.code.startswith(META_PREFIX)})
            status = "AGREE" if ours in forms else ("VIDYUT_EMPTY" if not forms else "DIFFER")
            rows.append({"root": root, "upadesa": up, "code": code, "lakara": lak, "cell": c, "pada": pada, "ours": ours, "vidyut": forms, "status": status,
                         "our_rules": our_rules, "vidyut_rules": vrules,
                         "ours_not_vidyut": sorted(set(our_rules) - set(vrules)), "vidyut_not_ours": sorted(set(vrules) - set(our_rules))})
    return {"rows": rows}


def sup_input(stem: str, gender: str, flags: tuple):
    """Map the engine's declared stem to a vidyut prātipadika."""
    fl = set(flags)
    if stem == "bhavat":
        raise ValueError("the honorific pronoun bhavat (ugit by bhavatu~) has no vidyut prātipadika input in this harness")
    if stem == "kartṛ":
        return vp.Pratipadika.krdanta(vp.Dhatu.mula("qukf\\Y", vp.Gana.Tanadi), vp.Krt.tfc)
    if "āp" in fl and stem.endswith("ā"):
        return vp.Pratipadika.basic(slp(stem[:-1] + "a"))      # vidyut forms the ṭāp itself (and offers the ṅīp branch beside it)
    return vp.Pratipadika.basic(slp(stem))


def sup_cross() -> dict:
    v = vp.Vyakarana()
    O = SUP.oracles()
    rows = []
    for name, e in SUP.SUITE.items():
        stem, gender, flags = e[0], e[1], e[2]
        cells = e[4] if len(e) > 4 else [c for c, _ in SUP.SUP]
        try:
            prat = sup_input(stem, gender, flags)
        except Exception as ex:  # noqa: BLE001
            rows.append({"stem": name, "status": "NO_VIDYUT_INPUT", "error": str(ex)}); continue
        for c in cells:
            up = dict(SUP.SUP)[c]
            ours = SUP.decline(stem, c, up, gender, flags)[0]
            path = SUP.decline(stem, c, up, gender, flags)[1]
            our_rules = sorted({norm_rule(x.split(" ")[0]) for x in path[1:]})
            try:
                ps = v.derive(vp.Pada.Subanta(pratipadika=prat, linga=LINGA[gender], vibhakti=VIB[c[0]], vacana=VAC[c[1]]))
            except Exception as ex:  # noqa: BLE001
                rows.append({"stem": name, "cell": c, "ours": ours, "status": "VIDYUT_ERROR", "error": str(ex)}); continue
            forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
            vrules = sorted({s.code for p in ps for s in p.history if not s.code.startswith(META_PREFIX)})
            status = "AGREE" if ours in forms else ("VIDYUT_EMPTY" if not forms else "DIFFER")
            rows.append({"stem": name, "gender": gender, "cell": c, "ours": ours, "oracle": O[name][c], "vidyut": forms, "status": status,
                         "our_rules": our_rules, "vidyut_rules": vrules,
                         "ours_not_vidyut": sorted(set(our_rules) - set(vrules)), "vidyut_not_ours": sorted(set(vrules) - set(our_rules))})
    return {"rows": rows}


def summarise(name: str, res: dict) -> dict:
    rows = res["rows"]
    st = Counter(r["status"] for r in rows)
    differ = [r for r in rows if r["status"] == "DIFFER"]
    onv = Counter(x for r in rows if r["status"] == "AGREE" for x in r.get("ours_not_vidyut", []))
    vno = Counter(x for r in rows if r["status"] == "AGREE" for x in r.get("vidyut_not_ours", []))
    return {"engine": name, "cells": len([r for r in rows if "cell" in r]), "status": dict(st),
            "differ": [{k: r[k] for k in r if k in ("root", "stem", "lakara", "cell", "pada", "gender", "ours", "vidyut", "oracle")} for r in differ],
            "our_rules_not_cited_by_vidyut_on_agreeing_cells": onv.most_common(40),
            "vidyut_rules_not_in_our_path_on_agreeing_cells": vno.most_common(40)}


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--data", required=True); ap.add_argument("--out", default=str(HERE / "CROSSCHECK.json")); a = ap.parse_args()
    by = load_dhatus(a.data)
    t = ting_cross(by); s = sup_cross()
    report = {"vidyut_version": "0.4.0", "ting": summarise("ting_rule_table_engine", t), "sup": summarise("sup_rule_table_engine", s), "ting_rows": t["rows"], "sup_rows": s["rows"]}
    Path(a.out).write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for k in ("ting", "sup"):
        print(k, report[k]["cells"], report[k]["status"])
        for d in report[k]["differ"][:60]:
            print("   DIFFER", d)


if __name__ == "__main__":
    main()
