from __future__ import annotations

"""Exact certificate (theorum/153): THE KṚDANTA DECLINED — the kṛt table's prātipadika (theorum/151–152) handed to the
nominal table (theorum/125) in the three genders: the stem's class and flags by the sūtras that name them (the ugit of
ktavatu / śatṛ, 1.1.26 / 3.2.124; the ṛ-stem of tṛc; the a-stem of the rest), the feminine stem by its own rows
(4.1.4 ṭāp, 4.1.5 ṅīp after the ṛ-stem, 4.1.6 ṅīp after the ugit with 7.1.80 / 7.1.81's num), and every cell of the
independent generator's lane (research/independent_oracle/VIDYUT_KRDANTA_SUP_LANE.json) read.

Three tables, one derivation: the verbal table builds the laṭ aṅga for śatṛ / śānac, the kṛt table the prātipadika,
the nominal table the pada. Nothing is re-stated here: this module holds the feminine rows and the hand-off.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab import krt_rule_table_engine as KRT
from proof_lab import sup_rule_table_engine as SUP
from proof_lab.sup_rule_table_engine import V, tok

SOURCES = {
    "4.1.1": "ṅyāpprātipadikāt", "4.1.3": "striyām", "4.1.4": "ajādyataṣ ṭāp", "4.1.5": "ṛnnebhyo ṅīp", "4.1.6": "ugitaś ca", "6.1.77": "iko yaṇ aci",
    "7.1.80": "ācchīnadyor num", "7.1.81": "śapśyanor nityam", "1.1.26": "ktaktavatū niṣṭhā", "3.2.124": "laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe", "7.3.44": "pratyayasthāt kāt pūrvasyāta id āpy asupaḥ",
    "1.1.39": "kṛn mejantaḥ", "1.1.40": "ktvātosunkasunaḥ", "7.1.78": "nābhyastāc chatuḥ", "7.1.79": "vā napuṁsakasya", "6.1.5": "ubhe abhyastam", "8.4.39": "kṣubhnādiṣu ca",
}
LANE_FILE = Path(__file__).resolve().parent.parent / "research" / "independent_oracle" / "VIDYUT_KRDANTA_SUP_LANE.json"
CLASS = {   # the stem's class for the nominal table, by the affix: (flags for m / n, feminine rule)
    "kta": ((), "ṭāp"), "tavya": ((), "ṭāp"), "anīya": ((), "ṭāp"), "ṇvul": ((), "ṭāp-7.3.44"), "śānac": ((), "ṭāp"),
    "ktavatu": (("ugit",), "ṅīp"), "śatṛ": (("ugit", "śatṛ"), "ṅīp"), "tṛc": (("tṛ", "ṛ"), "ṅīp-ṛ"),
}
AVYAYA = ("tumun", "ktvā")   # 1.1.39 / 1.1.40: indeclinable — no sup


class F:
    """The feminine stem under construction."""
    def __init__(self, stem: str, affix: str, anga_a: bool = False):
        self.st = tok(stem); self.affix = affix; self.anga_a = anga_a; self.flags: set[str] = set(); self.done: set[str] = set(); self.path: list[str] = []
    def form(self): return "".join(self.st)


def stri_rules() -> list[tuple[str, Callable[[F], bool], Callable[[F], Any], str]]:
    R: list = []
    def add(n, g, a, note): R.append((n, g, a, note))
    add("7.1.81", lambda s: s.affix == "śatṛ" and s.anga_a and s.st[-1] == "t" and "num" not in s.flags, lambda s: (s.st.insert(len(s.st) - 1, "n"), s.flags.add("num")), "num to the śatṛ stem after śap / śyan before ṅīp — always (bhavantī, dīvyantī, corayantī); after the other a / ā stems optionally by 7.1.80 ācchīnadyor num, the num branch realised (tudantī, krīṇantī); none after the rest (adatī, juhvatī, kurvatī)")
    add("4.1.6", lambda s: s.affix in ("ktavatu", "śatṛ"), lambda s: (s.st.append("ī"), s.flags.add("nadī")), "ṅīp after the ugit (bhūtavatī, bhavantī)")
    add("4.1.5", lambda s: s.affix == "tṛc" and s.st[-1] == "ṛ", lambda s: (s.st.__setitem__(-1, "r"), s.st.append("ī"), s.flags.add("nadī")), "ṅīp after the ṛ-stem, the ṛ → r before it by 6.1.77 (kartrī, bhavitrī)")
    add("7.3.44", lambda s: s.affix == "ṇvul" and s.st[-2:] == ["k", "a"], lambda s: s.st.__setitem__(-3, "i"), "i for the a before the k of the affix before āp (kārikā, pācikā — theorum/111's reading; the generator writes bhāvakā: not in the lane)")
    add("4.1.4", lambda s: s.st[-1] == "a" and s.affix in ("kta", "tavya", "anīya", "ṇvul", "śānac"), lambda s: (s.st.__setitem__(-1, "ā"), s.flags.add("āp")), "ṭāp after the a-stem (bhūtā, bhavitavyā, bhavamānā)")
    return R


STRI = stri_rules()


def feminine(stem: str, affix: str, anga_a: bool = False) -> tuple[str, tuple[str, ...], list[str]]:
    s = F(stem, affix, anga_a)
    for n, g, a, note in STRI:
        before = s.form()
        if g(s):
            a(s)
            if s.form() != before:
                s.done.add(n); s.path.append(f"{n} {note}: {s.form()}")
    return s.form(), tuple(sorted(s.flags)), s.path


def declension(root: str, affix: str, gender: str, code: str) -> tuple[str, list[str]]:
    """The pada: the kṛt table's prātipadika, the feminine rows, the nominal table."""
    k = KRT.derive_state(root, affix); stem = k.form()
    flags, fem = CLASS[affix]
    path = list(k.path)
    if "aṅga-a" in k.flags and gender == "n":
        flags = flags + ("aṅga-a",)
    if "abhyasta" in k.flags and affix == "śatṛ":
        flags = flags + ("abhyasta",)
    if "kṣubhnādi" in k.flags:
        flags = flags + ("kṣubhnādi",)
    if gender == "f":
        stem, flags, fpath = feminine(stem, affix, "aṅga-a" in k.flags); path += fpath
        if "kṣubhnādi" in k.flags:
            flags = flags + ("kṣubhnādi",)
    form, spath = SUP.decline(stem, code, dict(SUP.SUP)[code], gender, flags)
    return form, path + spath


def lane_oracle() -> dict[str, list[str]]:
    if not LANE_FILE.exists():
        return {}
    return json.loads(LANE_FILE.read_text(encoding="utf-8"))["cells"]


def t1_lane() -> dict[str, Any]:
    O = lane_oracle(); rows = {}
    for key, forms in O.items():
        r, a, g, c = key.split("|")
        try:
            ours = declension(r, a, g, c)[0]
        except Exception as e:  # noqa: BLE001
            ours = f"ENGINE_ERROR {e}"
        rows[key] = {"ours": ours, "vidyut": forms, "agree": ours in forms}
    by = {}
    for k, x in rows.items():
        r, a, g, c = k.split("|"); by.setdefault(f"{a} {g}", [0, 0]); by[f"{a} {g}"][1] += 1; by[f"{a} {g}"][0] += x["agree"]
    krt_residue = set(KRT.t1_lane()["disagree"])
    dis = {k: x for k, x in rows.items() if not x["agree"]}
    inherited = {k for k in dis if f"{k.split('|')[0]}|K|{k.split('|')[1]}" in krt_residue}
    generator = {k for k, x in dis.items() if k.split("|")[2] == "f" and k.split("|")[1] in ("ktavatu", "śatṛ", "tṛc") and ((k.endswith("|7s") and x["vidyut"][0].endswith("yai")) or (k.endswith("|6p") and x["vidyut"][0].endswith("yām")))}
    return {"cells": len(rows), "agree": sum(1 for x in rows.values() if x["agree"]), "by_affix_gender": by, "disagree": dis, "inherited_from_the_krt_residue": sorted(inherited),
            "generator_residue": {"rule": "the generator's 7s of the ṅīp stem of ktavatu / śatṛ / tṛc ends in -yai and its 6p in -yām (the 4s and 7s shapes), against the certified nadī paradigm of theorum/89 (nadyām, nadīnām) that the nominal table derives; the cells are listed, the engine's forms stand", "cells": sorted(generator)},
            "agreeing_keys": [k for k, x in rows.items() if x["agree"]]}


def t2_feminine_rows_load_bearing(agreeing: list[str]) -> dict[str, Any]:
    dead = []
    fem = [k for k in agreeing if k.split("|")[2] == "f"]
    for n, _, _, _ in STRI:
        hit = False
        for key in fem:
            r, a, g, c = key.split("|")
            k = KRT.derive_state(r, a); stem = k.form(); aa = "aṅga-a" in k.flags
            s = F(stem, a, aa)
            for m, gd, ac, _ in STRI:
                if m == n:
                    continue
                if gd(s):
                    ac(s)
            if s.form() != feminine(stem, a, aa)[0]:
                hit = True; break
        if not hit and n != "7.3.44":
            dead.append(n)
    return {"rows": [n for n, _, _, _ in STRI], "not_load_bearing": dead, "declared_vacuous_on_the_lane": ["7.3.44"]}


def build_certificate() -> dict[str, Any]:
    t1 = t1_lane(); t2 = t2_feminine_rows_load_bearing(t1["agreeing_keys"])
    new_dis = {k: x for k, x in t1["disagree"].items() if k not in set(t1["inherited_from_the_krt_residue"]) and k not in set(t1["generator_residue"]["cells"])}
    checks = {"t1_lane_read": t1["cells"] > 0, "t1_every_disagreement_is_the_krt_residue_or_the_generator_s_i_stem_7s_6p": not new_dis, "t2_feminine_rows_load_bearing": not t2["not_load_bearing"]}
    status = "PASS_KRDANTA_SUP_CANDIDATE" if all(checks.values()) else "FAIL_KRDANTA_SUP_CANDIDATE"
    return {"schema": "rkf.krdanta_sup_candidate.v1", "status": status, "checks": checks, "sources": SOURCES, "classes": {a: list(v[0]) + [v[1]] for a, v in CLASS.items()}, "avyaya": list(AVYAYA),
            "stri_rows": [(n, note) for n, _, _, note in STRI], "lane": {k: t1[k] for k in ("cells", "agree", "by_affix_gender", "disagree", "inherited_from_the_krt_residue", "generator_residue")}, "new_disagreements": new_dis, "load_bearing": t2,
            "claim_boundary": {"proved_by_exact_finite_certificate": ["every agreeing lane cell is derived by the three tables in sequence (verbal → kṛt → nominal) with the feminine rows; every disagreement is a cell of the kṛt residue (theorum/151) declined or a cell of the generator's residue (its 7s / 6p of the ṅīp stem, listed by rule); the feminine rows load-bearing"],
                               "declared": ["the lane (vidyut-prakriya) as an oracle of implementation grade; 7.1.80's option realised on the num branch; 7.3.44 as theorum/111 reads it (kārikā), the generator's bhāvakā not in the lane"],
                               "NOT_claimed": ["the kṛt residue; the neuter of tṛc; the ṇvul feminine; lyuṭ / ghañ / ṇini / kvip; the bhavān of the pronoun beside the bhavan of śatṛ as one stem (they are two: 6.4.14 adhātoḥ); RH, YM"]}}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"]); print("    lane:", cert["lane"]["cells"], cert["lane"]["agree"]); print("    by:", cert["lane"]["by_affix_gender"])
    print("    new disagreements:", len(cert["new_disagreements"]), list(cert["new_disagreements"].items())[:12]); print("    load-bearing:", cert["load_bearing"])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
