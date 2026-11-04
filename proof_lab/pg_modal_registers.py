from __future__ import annotations

"""Exact certificate (theorum/156): THE WRITTEN MODAL REGISTERS REPLAYED — the complete nine-slot registers the written
line writes for the moods beyond laṭ, in PG20 (benediction: āśīrliṅ), PG21 (nasal-class modals: loṭ / vidhiliṅ of the
śnu / u / śnā roots) and PG22 (athematic modals: loṭ / vidhiliṅ of the adādi / juhotyādi / rudhādi roots), expanded cell by
cell from the packets' own constructors and factor tables, and every cell whose root and pada the verbal table (theorum/129,
pin TING_RULE_TABLE_ENGINE_EXPECTED) declares re-derived by the table and compared.

What is read from the written files (nothing is retyped from them except the constructor definitions, which are quoted
and checked against the files):
  PG20  benediction/PARADIGMS.md §P2 (24 rows BA01–BA24: B_P(R) / B_A(Z,δ)); ENDING_CONSTRUCTION.md §E4–E5 define the two
        constructors; the causal rows (CA, CP), the basic karma / bhāva rows (BP, BV) and the blessing-loṭ register (P6:
        PG19's loṭ tuples with tātaṅ) are counted and placed outside the table by reason;
  PG21  nasal_modals/PARADIGMS.md §P2 (27 rows NM01–NM27: U_P / U_A / A_P / A_A for loṭ, O_P / O_A for vidhiliṅ, the
        tātaṅ word); STEM_CONSTRUCTION.md §S4 (Q, J, H of every u-ending interface) and §S5 (S of every śnā interface);
        MODAL_ENDINGS.md §E3–E5 define the constructors; braces are the union of complete branch tuples (3.1.82's śnu /
        śnā, the tanādi G0 / G1 guṇa policies) and a cell agrees when the table's form is one of the branches;
  PG22  athematic_modals/PARADIGMS.md §P1 (18 explicit loṭ tuples, braces = sets), §P2 (the K / J factors of O_P / O_A),
        §P3 (the tāt sets, placed outside the table: no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām).

The verbal table carries loṭ and vidhiliṅ (the present system) and āśīrliṅ for the kartari; it has no tātaṅ row, no
karmaṇi / ṇic beyond the present system, and declares a fixed root list. Every written position is therefore either
replayed (agree / other branch / to adjudicate), or placed outside the table with its reason and counted. Which reading is
right where they differ is not claimed: a difference names a rule one of them lacks, to be adjudicated against the source.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from proof_lab import pg_replay as PGR
from proof_lab import ting_rule_table_engine as TIN

ROOT = Path(__file__).resolve().parent.parent
PG = ROOT / "research" / "panini_grammar"
PG20 = PG / "benediction"; PG21 = PG / "nasal_modals"; PG22 = PG / "athematic_modals"
SLOTS = ["3s", "3d", "3p", "2s", "2d", "2p", "1s", "1d", "1p"]

# the constructors, quoted from the written files and checked against them at run time (written_constructors_checked)
WRITTEN = {
    "PG20 B_P": ("benediction/ENDING_CONSTRUCTION.md", "B_P(R)=(Ryāt,Ryāstām,Ryāsuḥ,Ryāḥ,Ryāstam,Ryāsta,Ryāsam,Ryāsva,Ryāsma)"),
    "PG20 B_A": ("benediction/ENDING_CONSTRUCTION.md", "B_A(Z,δ)=(Zīṣṭa,Zīyāstām,Zīran,Zīṣṭhāḥ,Zīyāsthām,Zīδvam,Zīya,Zīvahi,Zīmahi)"),
    "PG21 I_P^u": ("nasal_modals/MODAL_ENDINGS.md", "I_P^u(Q,J,H)=(Qotu,Qutām,Jantu,H,Qutam,Quta,Qavāni,Qavāva,Qavāma)"),
    "PG21 I_A^u": ("nasal_modals/MODAL_ENDINGS.md", "I_A^u(Q,J)=(Qutām,Jātām,Jatām,Quṣva,Jāthām,Qudhvam,Qavai,Qavāvahai,Qavāmahai)"),
    "PG21 I_P^ā": ("nasal_modals/MODAL_ENDINGS.md", "I_P^ā(S)=(Sātu,Sītām,Santu,Sīhi,Sītam,Sīta,Sāni,Sāva,Sāma)"),
    "PG21 I_A^ā": ("nasal_modals/MODAL_ENDINGS.md", "I_A^ā(S)=(Sītām,Sātām,Satām,Sīṣva,Sāthām,Sīdhvam,Sai,Sāvahai,Sāmahai)"),
    "PG21 O_P": ("nasal_modals/MODAL_ENDINGS.md", "O_P(K)=(Kyāt,Kyātām,Kyuḥ,Kyāḥ,Kyātam,Kyāta,Kyām,Kyāva,Kyāma)"),
    "PG21 O_A": ("nasal_modals/MODAL_ENDINGS.md", "O_A(J)=(Jīta,Jīyātām,Jīran,Jīthāḥ,Jīyāthām,Jīdhvam,Jīya,Jīvahi,Jīmahi)"),
    "PG22 O_P": ("athematic_modals/PARADIGMS.md", "O_P(K)=(Kyāt,Kyātām,Kyuḥ,Kyāḥ,Kyātam,Kyāta,Kyām,Kyāva,Kyāma)"),
    "PG22 O_A": ("athematic_modals/PARADIGMS.md", "O_A(J)=(Jīta,Jīyātām,Jīran,Jīthāḥ,Jīyāthām,Jīdhvam,Jīya,Jīvahi,Jīmahi)"),
}
B_P = ["yāt", "yāstām", "yāsuḥ", "yāḥ", "yāstam", "yāsta", "yāsam", "yāsva", "yāsma"]
B_A = ["īṣṭa", "īyāstām", "īran", "īṣṭhāḥ", "īyāsthām", "īδvam", "īya", "īvahi", "īmahi"]
U_P = ["{Q}otu", "{Q}utām", "{J}antu", "{H}", "{Q}utam", "{Q}uta", "{Q}avāni", "{Q}avāva", "{Q}avāma"]
U_A = ["{Q}utām", "{J}ātām", "{J}atām", "{Q}uṣva", "{J}āthām", "{Q}udhvam", "{Q}avai", "{Q}avāvahai", "{Q}avāmahai"]
A_P = ["{S}ātu", "{S}ītām", "{S}antu", "{S}īhi", "{S}ītam", "{S}īta", "{S}āni", "{S}āva", "{S}āma"]
A_A = ["{S}ītām", "{S}ātām", "{S}atām", "{S}īṣva", "{S}āthām", "{S}īdhvam", "{S}ai", "{S}āvahai", "{S}āmahai"]
O_P = ["yāt", "yātām", "yuḥ", "yāḥ", "yātam", "yāta", "yām", "yāva", "yāma"]
O_A = ["īta", "īyātām", "īran", "īthāḥ", "īyāthām", "īdhvam", "īya", "īvahi", "īmahi"]

# the written roots → the verbal table's keys (None: the table does not declare the root; a dict: by pada)
KEYS = {"bhū": "bhū", "pac": "pac", "edh": "edh", "labh": "labh", "tud": "tud", "nī": "nī", "gam": "gam", "śam": "śam", "kṛ": "kṛ", "krī": "krī", "dā": "dā",
        "vac": "vac2", "jāgṛ": "jāgṛ2", "hṛ": None, "sthā": None, "pā": None, "vid": None, "budh": None, "kṛṣ": None,
        "su": "su", "ci": "ci", "āp": "āp", "śak": "śak", "śru": "śru", "tan": "tan", "pū": "pū", "lū": "lū", "sku": {"P": "sku9", "A": "sku9A"}, "kṣiṇ": "kṣiṇ8",
        "stambh": None, "stumbh": None, "skambh": None, "skumbh": None, "ṛṇ": None, "tṛṇ": None, "ghṛṇ": None,
        "ad": "ad", "as": "as", "hu": "hu", "dhā": "dhā", "rudh": "rudh", "bhid": "bhid", "hiṃs": "hiṁs", "chid": None, "yuj": None, "śiṣ": None, "piṣ": None}
OPTIONS = {   # a written row with several branch tuples: the sūtra whose option the branches realise (quoted in SOURCES)
    "sku": "3.1.82 stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuś ca (śnu / śnā): the table declares sku as a class-9 root (skunāti), the śnā branch",
    "kṣiṇ": "3.1.79 tanādikṛñbhya uḥ with the two commentary policies on the guṇa of the root vowel before u (kṣiṇoti / kṣeṇoti: G0 / G1 of the written line; the table realises G1 in the strong cells, G0 in the weak)",
    "rudh": "8.4.65 jharo jhari savarṇe (runddhām / rundhām)", "bhid": "8.4.65 (bhinttām / bhintām)", "hiṃs": "8.4.65 (hinddhi / hindhi)",
}
SOURCES = {"3.1.82": "stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuś ca", "3.1.79": "tanādikṛñbhya uḥ", "8.4.65": "jharo jhari savarṇe", "7.1.35": "tuhyos tātaṅṅ āśiṣy anyatarasyām"}


def written_constructors_checked() -> dict[str, bool]:
    out = {}
    for name, (rel, quoted) in WRITTEN.items():
        text = (PG / rel).read_text(encoding="utf-8")
        flat = re.sub(r"\s+", "", text).replace("\\", "")
        out[name] = quoted.replace(" ", "") in flat
    return out


def key_for(root: str, pada: str | None):
    k = KEYS.get(root)
    if isinstance(k, dict):
        return k.get(pada or "P")
    return k


def replay(key: str, lak: str, cell: str, pada: str) -> str | None:
    try:
        return TIN.conjugate(key, lak, cell, pada=pada)[0]
    except Exception:  # noqa: BLE001
        return None


def compare(row_id: str, root: str, pada: str, lak: str, tuples: list[list[str | set]], st: Counter, out: dict, undeclared: Counter, options: dict, dis: dict) -> None:
    """tuples: the written branch tuples (each nine slots; a slot may be a set). One cell = one position; agree if the
    table's form is one of the written readings of that position. For a row with several branch tuples, `out` records
    which branch the table's form fell in at each cell, and whether the table's nine forms sit in ONE written branch
    (uniform) or mix the branches — a mixed row is a third reading, to be adjudicated against the source."""
    key = key_for(root, pada)
    branch_of: list = []
    for i, cell in enumerate(SLOTS):
        readings: list[str] = []
        for t in tuples:
            v = t[i]
            readings.extend(sorted(v) if isinstance(v, set) else [v])
        st["positions"] += 1
        if key is None:
            st["root_not_declared"] += 1; undeclared[root] += 1; continue
        ours = replay(key, lak, cell, pada)
        if ours is None:
            st["pada_not_declared"] += 1; undeclared[f"{root} ({pada})"] += 1; continue
        st["replayed"] += 1
        if any(PGR.same(ours, w) for w in readings):
            st["agree"] += 1
            if len(readings) > 1:
                options.setdefault(f"{row_id}:{lak}:{cell}", {"ours": ours, "written": readings, "option": OPTIONS.get(root, "a set-valued written cell")})
            if len(tuples) > 1:
                branch_of.append([b for b, t in enumerate(tuples) if any(PGR.same(ours, w) for w in (sorted(t[i]) if isinstance(t[i], set) else [t[i]]))])
        else:
            dis[f"{row_id}:{lak}:{cell}"] = {"root": key, "pada": pada, "lak": lak, "written": readings, "ours": ours}
    if len(tuples) > 1 and branch_of:
        uniform = any(all(b in bs for bs in branch_of) for b in range(len(tuples)))
        out[f"{row_id}:{lak}"] = {"branches": len(tuples), "branch_of_each_cell": branch_of, "uniform": uniform, "option": OPTIONS.get(root, "")}


def parse_set(s: str) -> str | set:
    s = s.strip()
    if s.startswith("{") and s.endswith("}"):
        return {x.strip() for x in s[1:-1].split(",")}
    return s


def split_top(s: str) -> list[str]:
    """Split a tuple body on commas outside braces / parentheses."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "{(":
            depth += 1
        elif ch in "})":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur); cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


# ---------------------------------------------------------------------------------------------------------------------
def pg20() -> dict[str, Any]:
    text = (PG20 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); undeclared = Counter(); options = {}; dis = {}; rows = 0; placed = Counter(); branch_rows = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*BA(\d\d)\s*\|\s*(\S+)\s*/\s*([PA])\s*\|\s*B_([PA])\(([^)]*)\)\s*\|", line)
        if not m:
            continue
        rows += 1; root, pada, kind, arg = m.group(2), m.group(3), m.group(4), m.group(5)
        if kind == "P":
            tup: list = [arg + e for e in B_P]
        else:
            z, d = [x.strip() for x in arg.split(",")]
            deltas = sorted(parse_set(d)) if d.startswith("{") else [d]
            tup = [({z + e.replace("δ", dd) for dd in deltas} if len(deltas) > 1 else z + e.replace("δ", deltas[0])) if "δ" in e else z + e for e in B_A]
        compare(f"BA{m.group(1)}", root, pada, "āśīrliṅ", [tup], st, branch_rows, undeclared, options, dis)
    # the rest of the register, placed outside the table by reason (counted from the packet's own accounting table, P7)
    acc = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(Causal active āśīrliṅ|Causal Karma āśīrliṅ|Basic Karma/Bhāva āśīrliṅ|Blessing loṭ)[^|]*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|", line)
        if m:
            acc[m.group(1)] = {"positions": int(m.group(2).replace(",", "")), "readings": int(m.group(3).replace(",", ""))}
    placed = {"Causal active āśīrliṅ": {**acc.get("Causal active āśīrliṅ", {}), "reason": "ṇic beyond the present system: the verbal table's ṇic is laṭ / laṅ / loṭ / liṅ only"},
              "Causal Karma āśīrliṅ": {**acc.get("Causal Karma āśīrliṅ", {}), "reason": "causative passive: no code in the verbal table"},
              "Basic Karma/Bhāva āśīrliṅ": {**acc.get("Basic Karma/Bhāva āśīrliṅ", {}), "reason": "karmaṇi beyond the present system: the table's yak is laṭ / laṅ / loṭ / liṅ only"},
              "Blessing loṭ": {**acc.get("Blessing loṭ", {}), "reason": "PG19's 54 loṭ tuples (replayed by theorum/155) on the āśīs frame, plus tātaṅ at P 3sg / 2sg: no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(undeclared.items())), "other_branch_of_an_option": options, "to_adjudicate": dis, "branch_rows": branch_rows, "placed_outside_the_table": placed}


# ---------------------------------------------------------------------------------------------------------------------
def pg21_interfaces() -> tuple[dict[str, tuple[str, str]], set[str]]:
    text = (PG21 / "STEM_CONSTRUCTION.md").read_text(encoding="utf-8")
    s4: dict[str, tuple[str, str]] = {}; s5: set[str] = set()
    sec4 = text[text.index("## S4"): text.index("## S5")]; sec5 = text[text.index("## S5"): text.index("## S6")]
    for line in sec4.splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(śnu|u)\s*\|\s*(\S+)\s*\|\s*(true|false)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|", line)
        if m:
            s4[m.group(3)] = (m.group(5), m.group(6))   # Q → (J, H)
    for line in sec5.splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(\S+)\s*\|", line)
        if m and m.group(2) not in ("S", "---"):
            s5.add(m.group(2))
    return s4, s5


def pg21_expand(call: str, s4: dict, s5: set) -> list[str]:
    m = re.match(r"([UAO])_([PA])\((\S+)\)", call.strip())
    kind, pada, arg = m.group(1), m.group(2), m.group(3)
    if kind == "U":
        j, h = s4[arg]
        return [e.format(Q=arg, J=j, H=h) for e in (U_P if pada == "P" else U_A)]
    if kind == "A":
        assert arg in s5, arg
        return [e.format(S=arg) for e in (A_P if pada == "P" else A_A)]
    return [arg + e for e in (O_P if pada == "P" else O_A)]


def pg21() -> dict[str, Any]:
    s4, s5 = pg21_interfaces()
    text = (PG21 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); undeclared = Counter(); options = {}; dis = {}; rows = 0; tat = 0; branch_rows = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*NM(\d\d)\s*\|\s*(\S+)\s*/\s*([PA])[^|]*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if not m:
            continue
        rows += 1; rid, root, pada = f"NM{m.group(1)}", m.group(2), m.group(3)
        lot_calls = split_top(m.group(4)[1:-1]) if m.group(4).startswith("{") else [m.group(4)]
        lin_calls = split_top(m.group(5)[1:-1]) if m.group(5).startswith("{") else [m.group(5)]
        compare(rid, root, pada, "loṭ", [pg21_expand(c, s4, s5) for c in lot_calls], st, branch_rows, undeclared, options, dis)
        compare(rid, root, pada, "liṅ", [pg21_expand(c, s4, s5) for c in lin_calls], st, branch_rows, undeclared, options, dis)
        if m.group(6).strip() != "—":
            tat += len([w for w in re.split(r"[;,]", m.group(6)) if w.strip()])
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(undeclared.items())), "other_branch_of_an_option": options, "to_adjudicate": dis,
            "interfaces_read": {"S4_u_ending": len(s4), "S5_sna": len(s5)}, "branch_rows": branch_rows,
            "placed_outside_the_table": {"tātaṅ words at P 3sg / 2sg": {"words": tat, "reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}}


# ---------------------------------------------------------------------------------------------------------------------
def pg22() -> dict[str, Any]:
    text = (PG22 / "PARADIGMS.md").read_text(encoding="utf-8")
    p1 = text[text.index("## P1"): text.index("## P2")]; p2 = text[text.index("## P2"): text.index("## P3")]; p3 = text[text.index("## P3"): text.index("## P4")]
    st = Counter(); undeclared = Counter(); options = {}; dis = {}; rows = 0; branch_rows = {}
    for line in p1.splitlines():
        m = re.match(r"\|\s*(\S+)\s+([PA])\s*\|\s*\((.*)\)\s*\|", line)
        if not m:
            continue
        rows += 1; root, pada = m.group(1), m.group(2)
        tup = [parse_set(x) for x in split_top(m.group(3))]
        assert len(tup) == 9, (root, pada, tup)
        compare(f"{root}-{pada}", root, pada, "loṭ", [tup], st, branch_rows, undeclared, options, dis)
    for line in p2.splitlines():
        m = re.match(r"\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*[^|]*\|", line)
        if not m or m.group(1) in ("Root", "---"):
            continue
        root, k, j = m.group(1), m.group(2), m.group(3)
        if k != "—":
            rows += 1; compare(f"{root}-P", root, "P", "liṅ", [[k + e for e in O_P]], st, {}, undeclared, options, dis)
        if j != "—":
            rows += 1; compare(f"{root}-A", root, "A", "liṅ", [[j + e for e in O_A]], st, {}, undeclared, options, dis)
    tat = sum(len(parse_set(m.group(2))) for m in re.finditer(r"\|\s*(\S+)\s*\|\s*(\{[^}]*\})\s*\|", p3))
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(undeclared.items())), "other_branch_of_an_option": options, "to_adjudicate": dis, "branch_rows": branch_rows,
            "placed_outside_the_table": {"tāt sets at P 3sg / 2sg": {"words": tat, "reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}}


def build_certificate() -> dict[str, Any]:
    checked = written_constructors_checked()
    r = {"PG20": pg20(), "PG21": pg21(), "PG22": pg22()}
    tot = Counter()
    for v in r.values():
        for k, n in v["statuses"].items():
            tot[k] += n
    tot["other_branch_of_an_option"] = sum(len(v["other_branch_of_an_option"]) for v in r.values())
    tot["to_adjudicate"] = sum(len(v["to_adjudicate"]) for v in r.values())
    mixed = {f"{p}:{k}": v for p, pk in r.items() for k, v in pk["branch_rows"].items() if not v["uniform"]}
    tot["branch_rows"] = sum(len(v["branch_rows"]) for v in r.values()); tot["branch_rows_mixed"] = len(mixed)
    undeclared = Counter()
    for v in r.values():
        undeclared.update(v["roots_not_declared"])
    checks = {"written_constructors_found_in_the_written_files": all(checked.values()), "replay_run_and_recorded": tot["replayed"] > 0,
              "pg20_24_rows_read": r["PG20"]["rows_replayed"] == 24, "pg21_27_rows_read": r["PG21"]["rows_replayed"] == 27, "pg22_18_lot_rows_read": r["PG22"]["rows_replayed"] >= 18,
              "every_option_cell_names_its_sutra": all(any(o["option"].startswith(s) for s in SOURCES) for v in r.values() for o in v["other_branch_of_an_option"].values())}
    status = "PASS_PG_MODAL_REGISTERS_CANDIDATE" if all(checks.values()) else "FAIL_PG_MODAL_REGISTERS_CANDIDATE"
    return {"schema": "rkf.pg_modal_registers_candidate.v1", "status": status, "checks": checks, "written_constructors": {k: v[1] for k, v in WRITTEN.items()}, "written_constructors_checked": checked,
            "sources": SOURCES, "options": OPTIONS, "packets": r, "totals": dict(tot), "roots_not_declared_by_the_verbal_table": dict(sorted(undeclared.items())),
            "branch_rows_the_table_realises_mixed": mixed,
            "claim_boundary": {
                "proved_by_exact_finite_certificate": ["the written registers of PG20 §P2, PG21 §P2 and PG22 §P1–P2 expand from the packets' own constructors, factor tables and explicit tuples to the positions counted here; every position on a declared root and pada is replayed by the verbal table; the agreements, the other-branch cells (named by sūtra) and every disagreement (both forms) are listed; the undeclared roots and the positions outside the table are counted by reason"],
                "counted_not_claimed": ["the counts: on the packets in the repository at this commit"],
                "NOT_claimed": ["which reading is right where they differ", "the tātaṅ forms (no 7.1.35 row), the causal and karmaṇi āśīrliṅ (beyond the present system), the undeclared roots", "RH, YM"],
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
        for k, d in list(v["to_adjudicate"].items())[:60]:
            print("        to adjudicate:", k, d["written"], "ours:", d["ours"])
        for k, d in list(v["other_branch_of_an_option"].items())[:6]:
            print("        option:", k, d["ours"], d["written"])
    print("    totals:", cert["totals"]); print("    undeclared:", cert["roots_not_declared_by_the_verbal_table"])
    for k, v in cert["branch_rows_the_table_realises_mixed"].items():
        print("    mixed branches:", k, v["branch_of_each_cell"], v["option"][:60])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
