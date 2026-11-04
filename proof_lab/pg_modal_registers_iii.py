from __future__ import annotations

"""Exact certificate (theorum/159): THE WRITTEN MODAL REGISTERS REPLAYED III — the three remaining adādi / rudhādi
registers of the written line, PG24 (consonant_modals), PG26 (vowel_modals) and PG27 (consonant_inventory_modals), read from
their PARADIGMS.md tables — explicit tuples where they are explicit, the packets' own parametric constructors where they are
parametric — and every position on a declared root and pada re-derived by the verbal table (theorum/129, pin
TING_RULE_TABLE_ENGINE_EXPECTED, as corrected by theorum/158).

  PG24  §P1: 12 explicit loṭ tuples (dviṣ P / A, duh P / A, dih P / A, lih P / A, īḍ, īś, vas, mṛj); §P2: the K / J factors
        of O_P / O_A for the vidhiliṅ (constructors as PG21 §E5, quoted in proof_lab.pg_modal_registers).
  PG26  §P1: twelve short-u P profiles by U_P(R;Q) with the īṭ overlay E_P (7.3.95 turustuśamyamaḥ sārvadhātuke) where the
        packet marks it; §P2: four explicit A tuples; §P3: fourteen ā-root profiles by A_P(R) and two explicit i-vowel
        tuples; §P4: the K / J parameters of O_P / O_A, the ā roots' K from §P3.
  PG27  §P1: fourteen adādi A profiles by A(W,G,T,Z,D); §P2: sixteen rudhādi roots by P(Q,W,G,T,D) and A(W,G,T,Z,D)
        with their brace alternatives (8.4.65); §P3: vac and class-2 vid explicit (⊥ = source-excluded, not a position);
        §P4: O_P(W) / O_A(W) on every W / pada binding.

Each constructor is quoted here and checked against the written file at run time. A position agrees when the table's form is
one of the written readings; a row with several branch tuples is checked for tuple-level uniformity. The roots the table does
not declare (or declares in another class: su 'ṣu prasave' of class 2 against the table's class-5 ṣuñ, dāp against ḍudāñ, the
class-2 nij / śij / pij / pṛj / vṛj / pṛc against the table's class-3 or none) and the tāt words (no 7.1.35 row) are placed
outside the table by reason. Which reading is right where they differ is not claimed.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from proof_lab import pg_modal_registers as PMR
from proof_lab import pg_modal_registers_ii as PM2
from proof_lab import pg_replay as PGR
from proof_lab import ting_rule_table_engine as TIN

ROOT = Path(__file__).resolve().parent.parent
PG = ROOT / "research" / "panini_grammar"
PG24 = PG / "consonant_modals"; PG26 = PG / "vowel_modals"; PG27 = PG / "consonant_inventory_modals"
SLOTS = PMR.SLOTS

WRITTEN = {
    "PG26 U_P": ("vowel_modals/PARADIGMS.md", "U_P(R;Q)=(Qtu,Rutām,Ruvantu,Ruhi,Rutam,Ruta,\\nu(Ravāni),Ravāva,Ravāma)"),
    "PG26 A_P": ("vowel_modals/PARADIGMS.md", "A_P(R)=(Rātu,Rātām,Rāntu,Rāhi,Rātam,Rāta,\\nu(Rāni),Rāva,Rāma)"),
    "PG27 A": ("consonant_inventory_modals/PARADIGMS.md", "A(W,G,T,Z,D)=(Tām,Wātām,Watām,Zva,Wāthām,Dvam,Gai,Gāvahai,Gāmahai)"),
    "PG27 P": ("consonant_inventory_modals/PARADIGMS.md", "P(Q,W,G,T,D)=(Q,Tām,Wantu,Di,Tam,Ta,Gāni,Gāva,Gāma)"),
    "PG27 O_P": ("consonant_inventory_modals/PARADIGMS.md", "O_P(W)=(Wyāt,Wyātām,Wyuḥ,Wyāḥ,Wyātam,Wyāta,Wyām,Wyāva,Wyāma)"),
    "PG27 O_A": ("consonant_inventory_modals/PARADIGMS.md", "O_A(W)=(Wīta,Wīyātām,Wīran,Wīthāḥ,Wīyāthām,Wīdhvam,Wīya,Wīvahi,Wīmahi)"),
}
E_P = {"3s": "avītu", "3d": "uvītām", "2s": "uvīhi", "2d": "uvītam", "2p": "uvīta"}   # PG26 §P1: the five īṭ readings, R + these

KEYS = {"dviṣ": {"P": "dviṣ2", "A": "dviṣ2A"}, "duh": {"P": "duh2", "A": "duh2A"}, "dih": {"P": "dih2", "A": "dih2A"}, "lih": {"P": "lih2", "A": "lih2A"}, "īḍ": "īḍ2A", "īś": "īś2A", "vas": "vas2A", "mṛj": "mṛj2",
        "yu": "yu2", "ru": "ru2", "tu": "tu2", "nu": "nu2", "kṣu": "kṣu2", "kṣṇu": "kṣṇu2", "snu": "snu2", "ūrṇu": {"P": "ūrṇu2", "A": "ūrṇu2A"}, "dyu": "dyu2", "su": None, "ku": None, "stu": {"P": "stu2", "A": "stu2A"},
        "hnu": "hnu2A", "sū": "sū2A", "yā": "yā2", "vā": "vā2", "bhā": "bhā2", "snā": "snā2", "śrā": None, "drā": "drā2", "psā": "psā2", "pā": "pā2", "rā": None, "lā": "lā2", "dāp": None, "khyā": "khyā2", "prā": None, "mā": "mā2",
        "iṇ": "i2", "vī": "vī2",
        "cakṣ": None, "īr": "īr2A", "ās": "ās2A", "kas": "kas2A", "kaś": "kaś2A", "nis": None, "nij": None, "śij": None, "pij": None, "pṛj": None, "vṛj": None, "pṛc": None,
        "ric": "ric", "vic": "vic", "kṣud": "kṣud", "chṛd": "chṛd", "tṛd": "tṛd", "kṛt": "kṛt", "indh": None, "khid": None, "vid": None, "bhañj": None, "und": None, "añj": None, "tañc": None, "vij": None, "vac": "vac2"}
OPTIONS = {"ru": "7.3.95 turustuśamyamaḥ sārvadhātuke (rautu / ravītu)", "tu": "7.3.95 (tautu / tavītu)", "stu": "7.3.95 (stautu / stavītu; stutām / stuvītām)", "ūrṇu": "7.3.90 ūrṇoter vibhāṣā (ūrṇautu / ūrṇotu)",
           "mṛj": "7.2.114 mṛjer vṛddhiḥ with the vārttika mṛjer vibhāṣā (mṛjantu / mārjantu)", "kṣud": "8.4.65 jharo jhari savarṇe (kṣunttām / kṣuntām)", "chṛd": "8.4.65 (chṛnttām / chṛntām)", "tṛd": "8.4.65 (tṛnttām / tṛntām)", "kṛt": "8.4.65 (kṛnttām / kṛntām)",
           "kas": "8.4.65 (kaṃssva / kaṃsva)", "nis": "8.4.65 (niṃssva / niṃsva)"}
SOURCES = {"7.3.95": "turustuśamyamaḥ sārvadhātuke", "7.3.90": "ūrṇoter vibhāṣā", "7.2.114": "mṛjer vṛddhiḥ", "8.4.65": "jharo jhari savarṇe", "7.1.35": "tuhyos tātaṅṅ āśiṣy anyatarasyām"}


def written_constructors_checked() -> dict[str, bool]:
    out = {}
    for name, (rel, quoted) in WRITTEN.items():
        flat = re.sub(r"\s+", "", (PG / rel).read_text(encoding="utf-8")).replace("\\", "")
        out[name] = quoted.replace(" ", "").replace("\\", "") in flat
    return out


def key_for(root: str, pada: str | None):
    k = KEYS.get(root)
    return k.get(pada or "P") if isinstance(k, dict) else k


def compare(row_id, root, pada, lak, tuples, st, br, und, opt, dis, skip=()):
    key = key_for(root, pada); branch_of = []
    for i, cell in enumerate(SLOTS):
        if cell in skip:
            continue
        readings: list[str] = []
        for t in tuples:
            v = t[i]; readings.extend(sorted(v) if isinstance(v, set) else [v])
        st["positions"] += 1
        if key is None:
            st["root_not_declared"] += 1; und[root] += 1; continue
        ours = PM2.replay(key, lak, cell, pada)
        if ours is None:
            st["pada_not_declared"] += 1; und[f"{root} ({pada})"] += 1; continue
        st["replayed"] += 1
        if any(PGR.same(ours, w) for w in readings):
            st["agree"] += 1
            if len(readings) > 1:
                opt.setdefault(f"{row_id}:{lak}:{cell}", {"ours": ours, "written": readings, "option": OPTIONS.get(root, "a set-valued written cell")})
            if len(tuples) > 1:
                branch_of.append([b for b, t in enumerate(tuples) if any(PGR.same(ours, w) for w in (sorted(t[i]) if isinstance(t[i], set) else [t[i]]))])
        else:
            dis[f"{row_id}:{lak}:{cell}"] = {"root": key, "pada": pada, "lak": lak, "written": readings, "ours": ours}
    if len(tuples) > 1 and branch_of:
        uniform = any(all(b in bs for bs in branch_of) for b in range(len(tuples)))
        br[f"{row_id}:{lak}"] = {"branches": len(tuples), "branch_of_each_cell": branch_of, "uniform": uniform, "option": OPTIONS.get(root, "")}


def sec(text, a, b):
    i = text.index(a); j = text.index(b) if b else len(text)
    return text[i:j]


def cat(x, suffix: str):
    """x + suffix, where x may be a set of alternatives (a set-valued parameter)."""
    return {y + suffix for y in x} if isinstance(x, set) else x + suffix


def o_tuple(kind, factor):
    return [cat(factor, e) for e in (PMR.O_P if kind == "P" else PMR.O_A)]


# ---------------------------------------------------------------------------------------------------------------------
def pg24() -> dict[str, Any]:
    text = (PG24 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0
    for line in sec(text, "## P1", "## P2").splitlines():
        m = re.match(r"\|\s*(\S+)\s+([PA])\s*\|\s*\((.*)\)\s*\|", line)
        if m:
            tup = [PMR.parse_set(x) for x in PMR.split_top(m.group(3))]; assert len(tup) == 9
            rows += 1; compare(f"{m.group(1)}-{m.group(2)}", m.group(1), m.group(2), "loṭ", [tup], st, br, und, opt, dis)
    for root, k, j in PM2.factor_rows(sec(text, "## P2", "## P3")):
        if k != "—":
            rows += 1; compare(f"{root}-P", root, "P", "liṅ", [o_tuple("P", k)], st, br, und, opt, dis)
        if j != "—":
            rows += 1; compare(f"{root}-A", root, "A", "liṅ", [o_tuple("A", j)], st, br, und, opt, dis)
    tat = len(re.findall(r"\|\s*\S+\s*\|\s*\S+tāt\s*\|", sec(text, "## P3", "## P4")))
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "placed_outside_the_table": {"tāt words at P 3sg / 2sg": {"words": tat, "reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}}


# ---------------------------------------------------------------------------------------------------------------------
def pg26() -> dict[str, Any]:
    text = (PG26 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0; a_k: dict[str, str] = {}
    # P1: short-u P profiles
    for line in sec(text, "## P1", "## P2").splitlines():
        m = re.match(r"\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(yes|no)\s*\|\s*(\S+)\s*\|", line)
        if not m or m.group(1) in ("Root",):
            continue
        root, R, Q, ep, first = m.groups(); Q = PMR.parse_set(Q)
        tup: list = [cat(Q, "tu"), R + "utām", R + "uvantu", R + "uhi", R + "utam", R + "uta", first, R + "avāva", R + "avāma"]
        if ep == "yes":
            tup = [({t} if not isinstance(t, set) else set(t)) | {R + E_P[c]} if c in E_P else t for c, t in zip(SLOTS, tup)]
        rows += 1; compare(root + "-P", root, "P", "loṭ", [tup], st, br, und, opt, dis)
    # P2: explicit A tuples
    for line in sec(text, "## P2", "## P3").splitlines():
        m = re.match(r"\|\s*(\S+)\s*\|\s*\((.*)\)\s*\|", line)
        if m:
            tup = [PMR.parse_set(x) for x in PMR.split_top(m.group(2))]; assert len(tup) == 9
            rows += 1; compare(m.group(1) + "-A", m.group(1), "A", "loṭ", [tup], st, br, und, opt, dis)
    # P3: ā roots and the two i-vowel tuples
    p3 = sec(text, "## P3", "## P4")
    for line in p3.splitlines():
        m = re.match(r"\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+tāt)\s*\|", line)
        if m:
            root, R, first, K, _ = m.groups(); a_k[root] = K
            tup = [R + "ātu", R + "ātām", R + "āntu", R + "āhi", R + "ātam", R + "āta", first, R + "āva", R + "āma"]
            rows += 1; compare(root + "-P", root, "P", "loṭ", [tup], st, br, und, opt, dis); continue
        m = re.match(r"\|\s*(\S+)\s*\|\s*\((.*)\)\s*\|", line)
        if m:
            tup = [PMR.parse_set(x) for x in PMR.split_top(m.group(2))]; assert len(tup) == 9
            rows += 1; compare(m.group(1) + "-P", m.group(1), "P", "loṭ", [tup], st, br, und, opt, dis)
    # P4: vidhiliṅ parameters
    for line in sec(text, "## P4", "## P5").splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if not m or m.group(1) in ("Root", "---"):
            continue
        root, k, j = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        if root.startswith("fourteen"):
            for r2, K in a_k.items():
                rows += 1; compare(r2 + "-P", r2, "P", "liṅ", [o_tuple("P", K)], st, br, und, opt, dis)
            continue
        if k != "—":
            rows += 1; compare(root + "-P", root, "P", "liṅ", [o_tuple("P", PMR.parse_set(k))], st, br, und, opt, dis)
        if j != "—":
            rows += 1; compare(root + "-A", root, "A", "liṅ", [o_tuple("A", PMR.parse_set(j))], st, br, und, opt, dis)
    tat = len(a_k) + len(re.findall(r"tāt\b", sec(text, "## P5", "## P6")))
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "placed_outside_the_table": {"tāt words": {"words": tat, "reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}}


# ---------------------------------------------------------------------------------------------------------------------
def pg27() -> dict[str, Any]:
    text = (PG27 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0; bindings: list[tuple[str, str, str, Any]] = []   # (row_id, root, pada, W)
    def A(W, G, T, Z, D): return [cat(T, "ām"), cat(W, "ātām"), cat(W, "atām"), cat(Z, "va"), cat(W, "āthām"), cat(D, "vam"), cat(G, "ai"), cat(G, "āvahai"), cat(G, "āmahai")]
    def P(Q, W, G, T, D): return [Q, cat(T, "ām"), cat(W, "antu"), cat(D, "i"), cat(T, "am"), cat(T, "a"), cat(G, "āni"), cat(G, "āva"), cat(G, "āma")]
    for line in sec(text, "## P1", "## P2").splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|" + r"\s*([^|]+?)\s*\|" * 5, line)
        if not m or m.group(1).startswith(("Exact", "---")):
            continue
        label = m.group(1); root = label.split(",")[0].split(" ")[0]
        W, G, T, Z, D = [PMR.parse_set(x) for x in m.groups()[1:]]
        rid = label.replace(" ", "_")
        rows += 1; compare(rid + "-A", root if "1020014" not in label else "kas-num", pada := "A", "loṭ", [A(W, G, T, Z, D)], st, br, und, opt, dis); bindings.append((rid, root if "1020014" not in label else "kas-num", "A", W))
    for line in sec(text, "## P2", "## P3").splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|" + r"\s*([^|]+?)\s*\|" * 6, line)
        if not m or m.group(1).startswith(("Root", "---")):
            continue
        label = m.group(1); root = label.split(",")[0].strip(); padas = [p.strip() for p in m.group(2).split(",")]
        W, G, Q, T, Z, D = [PMR.parse_set(x) for x in m.groups()[2:]]
        root_key = root if "class 7" not in label else root + "7"
        rid = label.replace(" ", "_").replace(",", "")
        if "P" in padas:
            rows += 1; compare(rid + "-P", root_key, "P", "loṭ", [P(Q, W, G, T, D)], st, br, und, opt, dis); bindings.append((rid, root_key, "P", W))
        if "A" in padas:
            rows += 1; compare(rid + "-A", root_key, "A", "loṭ", [A(W, G, T, Z, D)], st, br, und, opt, dis); bindings.append((rid, root_key, "A", W))
    for line in sec(text, "## P3", "## P4").splitlines():
        m = re.match(r"\|\s*(\S+)\s*\|\s*\((.*)\)\s*\|", line)
        if m:
            parts = PMR.split_top(m.group(2)); skip = tuple(c for c, x in zip(SLOTS, parts) if x.strip() == "⊥")
            tup = [PMR.parse_set(x) if x.strip() != "⊥" else "⊥" for x in parts]; assert len(tup) == 9
            root = m.group(1); root_key = "vid2" if root == "vid" else root
            rows += 1; compare(root + "-P", root_key, "P", "loṭ", [tup], st, br, und, opt, dis, skip=skip); bindings.append((root, root_key, "P", root))
    for rid, root_key, pada, W in bindings:
        rows += 1; compare(rid + "-" + pada, root_key, pada, "liṅ", [o_tuple(pada, W)], st, br, und, opt, dis)
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "placed_outside_the_table": {"tāt words (§P5)": {"reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}, "vac loṭ 3pl": {"reason": "⊥ in the written register (source-excluded on its selected view): not a position"}}}


KEYS.update({"kas-num": None, "vid7": None, "vṛj7": None, "pṛc7": None, "vid2": None})


def build_certificate() -> dict[str, Any]:
    checked = written_constructors_checked()
    r = {"PG24": pg24(), "PG26": pg26(), "PG27": pg27()}
    tot = Counter()
    for v in r.values():
        for k, n in v["statuses"].items():
            tot[k] += n
    tot["other_branch_of_an_option"] = sum(len(v["other_branch_of_an_option"]) for v in r.values()); tot["to_adjudicate"] = sum(len(v["to_adjudicate"]) for v in r.values())
    mixed = {f"{p}:{k}": v for p, pk in r.items() for k, v in pk["branch_rows"].items() if not v["uniform"]}
    tot["branch_rows"] = sum(len(v["branch_rows"]) for v in r.values()); tot["branch_rows_mixed"] = len(mixed)
    und = Counter()
    for v in r.values():
        und.update(v["roots_not_declared"])
    checks = {"written_constructors_found_in_the_written_files": all(checked.values()), "replay_run_and_recorded": tot["replayed"] > 0,
              "pg24_rows_read": r["PG24"]["rows_replayed"] == 12 + 12, "pg26_rows_read": r["PG26"]["rows_replayed"] == 12 + 4 + 16 + 32, "pg27_rows_read": r["PG27"]["rows_replayed"] >= 14 + 21 + 2,
              "every_option_cell_names_its_sutra": all(any(o["option"].startswith(s) for s in SOURCES) for v in r.values() for o in v["other_branch_of_an_option"].values())}
    status = "PASS_PG_MODAL_REGISTERS_III_CANDIDATE" if all(checks.values()) else "FAIL_PG_MODAL_REGISTERS_III_CANDIDATE"
    return {"schema": "rkf.pg_modal_registers_iii_candidate.v1", "status": status, "checks": checks, "written_constructors": {k: v[1] for k, v in WRITTEN.items()}, "written_constructors_checked": checked,
            "sources": SOURCES, "options": OPTIONS, "packets": r, "totals": dict(tot), "roots_not_declared_by_the_verbal_table": dict(sorted(und.items())), "branch_rows_the_table_realises_mixed": mixed,
            "claim_boundary": {
                "proved_by_exact_finite_certificate": ["PG24 §P1–P2, PG26 §P1–P4 and PG27 §P1–P4 expand from the packets' own tuples and constructors (quoted, found in the files) to the positions counted here; every position on a declared root and pada is replayed by the verbal table; the agreements, the other-branch cells (named by sūtra) and every disagreement (both forms) are listed; the undeclared roots and the positions outside the table are counted by reason"],
                "counted_not_claimed": ["the counts: on the packets in the repository at this commit"],
                "NOT_claimed": ["which reading is right where they differ", "the tāt forms (no 7.1.35 row), the undeclared and other-class roots", "RH, YM"],
            }}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=sorted) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"]); print("    checks:", cert["checks"])
    for p, v in cert["packets"].items():
        print(f"    {p}: rows {v['rows_replayed']} {v['statuses']} undeclared {v['roots_not_declared']}")
        for k, d in list(v["to_adjudicate"].items())[:80]:
            print("        to adjudicate:", k, d["written"], "ours:", d["ours"])
    print("    totals:", cert["totals"]); print("    undeclared:", cert["roots_not_declared_by_the_verbal_table"])
    for k, v in cert["branch_rows_the_table_realises_mixed"].items():
        print("    mixed branches:", k, v["branch_of_each_cell"], v["option"][:60])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
