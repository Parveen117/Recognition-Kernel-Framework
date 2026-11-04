"""Gaṇa sweep: every root of one gaṇa in vidyut-prakriya's Dhātupāṭha, declared to the tiṅ table provisionally (upadeśa and
pada read from the entry's accent), compared cell by cell with vidyut across the ten kartari lakāras, the karmaṇi, the ṇic
and the san (the same cells the seven lanes carry) — a pre-check, not a certificate: it tells which roots the table already
derives whole (to declare), and for the rest which cells disagree, grouped by lakāra, so the missing rows can be read off.

    python3.12 -B -W ignore -m research.independent_oracle.gana_sweep --data /tmp/vidyut_data/prakriya --gana 2 --out /tmp/sweep2.json
    python3.12 -B -W ignore -m research.independent_oracle.gana_sweep --data … --gana 2 --roots ad,han      # a few roots only

The upadeśa is taken as vidyut spells it (SLP1 → IAST, the it-vowels' nasal mark kept as ~); the pada from the final
vowel's accent (anudātta → ātmanepada, svarita → ubhayapada, else parasmaipada). Roots the table already declares are
skipped unless --all is given. Nothing here is pinned.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys

import vidyut.prakriya as vp

from proof_lab import ting_rule_table_engine as TIN
from research.independent_oracle.crosscheck import GANA, LAK, PUR, VAC, iast, strip_accents

LAK2 = {**LAK, "lṛṅ": vp.Lakara.Lrn}
KARTARI = ("laṭ", "laṅ", "loṭ", "liṅ", "lṛṭ", "luṭ", "āśīrliṅ", "liṭ", "luṅ", "lṛṅ")
PRESENT = ("laṭ", "laṅ", "loṭ", "liṅ")


def pada_of(aupadeshika: str) -> str:
    """The pada from the accent on the upadeśa's last vowel (1.3.12 anudāttaṅita ātmanepadam, 1.3.72 svaritañitaḥ kartrabhiprāye)."""
    m = list(re.finditer(r"[aAiIuUfFxXeEoO]~?([\\^])?", aupadeshika))
    if not m:
        return "P"
    acc = m[-1].group(1)
    return "A" if acc == "\\" else "U" if acc == "^" else "P"


def upadesa_iast(aupadeshika: str) -> str:
    """vidyut's SLP1 upadeśa → the table's IAST spelling: the nasal mark of an it-vowel as ~ after the vowel (vida~, cakṣi~ṅ)."""
    return iast(strip_accents(aupadeshika)).replace("ṃ", "ṁ").replace("m̐", "~").replace("\u0310", "~")


def derive(v, dh, prayoga, lak, c, pada):
    kw = dict(dhatu=dh, prayoga=prayoga, lakara=LAK2[lak], purusha=PUR[c[0]], vacana=VAC[c[1]])
    if pada is not None:
        kw["dhatu_pada"] = vp.DhatuPada.Parasmaipada if pada == "P" else vp.DhatuPada.Atmanepada
    try:
        ps = v.derive(vp.Pada.Tinanta(**kw))
    except Exception:  # noqa: BLE001
        return None
    forms = [iast(p.text).replace("ṃ", "ṁ") for p in ps]
    return forms or None


def ours(key, lak, c, code):
    try:
        return TIN.conjugate(key, lak, c, pada=code)[0]
    except Exception as e:  # noqa: BLE001
        return "ENGINE_ERROR " + type(e).__name__ + " " + str(e)[:40]


def sweep_root(v, key, entry, gana, pada):
    code, aup, _g = entry
    dh = vp.Dhatu.mula(aup, GANA[gana])
    padas = ("P", "A") if pada == "U" else (pada,)
    rows = []
    for pd in padas:
        for l in KARTARI:
            for c in TIN.CODES:
                forms = derive(v, dh, vp.Prayoga.Kartari, l, c, pd)
                if forms is None:
                    continue
                o = ours(key, l, c, pd); rows.append((f"{pd}|{l}|{c}", o, forms, o in forms))
    for l in PRESENT:
        for c in TIN.CODES:
            forms = derive(v, dh, vp.Prayoga.Karmani, l, c, None)
            if forms is None:
                continue
            o = ours(key, l, c, "K"); rows.append((f"K|{l}|{c}", o, forms, o in forms))
    for san, tag in ((vp.Sanadi.Ric, "N"), (vp.Sanadi.san, "S")):
        dhs = vp.Dhatu.mula(aup, GANA[gana]).with_sanadi([san])
        for pd in (("P", "A") if tag == "N" else padas):
            for l in PRESENT:
                for c in TIN.CODES:
                    forms = derive(v, dhs, vp.Prayoga.Kartari, l, c, pd)
                    if forms is None:
                        continue
                    o = ours(key, l, c, tag + pd); rows.append((f"{tag}{pd}|{l}|{c}", o, forms, o in forms))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--gana", type=int, required=True); ap.add_argument("--out")
    ap.add_argument("--roots", default=""); ap.add_argument("--all", action="store_true"); ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    data = vp.Data(a.data); v = vp.Vyakarana()
    declared = {(TIN.ROOTS[k][0].replace("~", ""), TIN.GANA.get(k, 1)) for k in TIN.ROOTS} | {(x[0].replace("~", ""), x[1]) for x in TIN.NASAL.values()}
    want = set(a.roots.split(",")) if a.roots else None
    entries = []
    for e in data.load_dhatu_entries():
        if e.dhatu.gana != GANA[a.gana]:
            continue
        up = upadesa_iast(e.dhatu.aupadeshika)
        try:
            root = TIN.its(up, "dhatu")["remaining"]
        except Exception as e:  # noqa: BLE001
            print(f"SKIP {up}: its() {type(e).__name__} {e!r}"); continue
        if want is not None and root not in want and up not in want:
            continue
        if not a.all and (up.replace("~", ""), a.gana) in declared:
            continue
        entries.append((root, up, pada_of(e.dhatu.aupadeshika), (e.code, e.dhatu.aupadeshika, e.dhatu.gana)))
    if a.limit:
        entries = entries[:a.limit]
    report = {"gana": a.gana, "roots": {}, "clean": [], "by_lakara_disagree": {}}
    seen = collections.Counter()
    for root, up, pada, entry in entries:
        key = f"sweep:{root}:{entry[0]}"
        # the pada vidyut actually derives (probe laṭ 3s in both): the accent's reading is reported beside it when they differ
        dh = vp.Dhatu.mula(entry[1], GANA[a.gana])
        has = {pd for pd in ("P", "A") if derive(v, dh, vp.Prayoga.Kartari, "laṭ", "3s", pd)}
        vpada = "U" if has == {"P", "A"} else ("P" if has == {"P"} else "A" if has == {"A"} else None)
        if vpada is None:
            print(f"{root:12s} {up:14s} {pada} {entry[0]:8s} vidyut derives no kartari laṭ: skipped"); continue
        if vpada != pada:
            print(f"   ({root}: accent says {pada}, vidyut derives {vpada}; using {vpada})")
            pada = vpada
        TIN.ROOTS[key] = (up, pada); TIN.GANA[key] = a.gana
        try:
            rows = sweep_root(v, key, entry, a.gana, pada)
        finally:
            del TIN.ROOTS[key]; del TIN.GANA[key]
        n = len(rows); ok = sum(1 for r in rows if r[3])
        bad = [(k, o, f) for k, o, f, g in rows if not g]
        byl = collections.Counter(k.split("|")[0] + "|" + k.split("|")[1] for k, _, _ in bad)
        report["roots"][f"{root} ({up}, {pada}, {entry[0]})"] = {"cells": n, "agree": ok, "disagree_by_lakara": dict(byl), "sample": bad[:6]}
        if n and ok == n:
            report["clean"].append(f"{root} ({up}, {pada}, {entry[0]})")
        for k in byl:
            seen[k] += byl[k]
        print(f"{root:12s} {up:14s} {pada} {entry[0]:8s} {ok:4d}/{n:4d}  " + ("CLEAN" if n and ok == n else " ".join(f"{k}:{c}" for k, c in sorted(byl.items()))), flush=True)
    report["by_lakara_disagree"] = dict(seen)
    print(json.dumps({"roots": len(entries), "clean": len(report["clean"]), "disagree_by_lakara": dict(seen)}, ensure_ascii=False))
    if a.out:
        json.dump(report, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
