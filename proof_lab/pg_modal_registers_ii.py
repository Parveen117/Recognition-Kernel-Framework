from __future__ import annotations

"""Exact certificate (theorum/157): THE WRITTEN MODAL REGISTERS REPLAYED II — four more explicit registers of the written
line, read from their PARADIGMS.md tables and re-derived cell by cell by the verbal table (theorum/129, pin
TING_RULE_TABLE_ENGINE_EXPECTED):

  PG23  lexical_modals: 10 explicit loṭ tuples (han, śās, rud, svap, śvas, an, jakṣ, brū P / A, śī) and the vidhiliṅ
        K / J factors of O_P / O_A (the constructors of PG21 §E5 / PG22 §P2, quoted in proof_lab.pg_modal_registers);
  PG25  abhyasta_modals: 13 loṭ P and 6 loṭ A explicit tuples of the juhotyādi roots (bhī, hrī, pṝ, pṛ, bhṛ, hā, nij, vij,
        viṣ, ṛ, jāgṛ, daridrā, cakās, mā) with their set-valued cells (6.4.115 / 6.4.116), and the vidhiliṅ K / J factors;
  PG31  counterfactual_contexts: 53 explicit lṛṅ rows (basic P1–P2, causal P3), several rows of one root and pada being
        the iṭ branches of 7.2.44 (dhūñ) / 7.2.57 (nṛt) — read as one position with the union of readings;
  PG32  prohibitive_lung: 10 explicit luṅ rows (P01–P10), 8 māṅ-luṅ rows without the augment (P11–P18) and 8 māṅ + sma
        laṅ rows without the augment (P19–P26). The table has no māṅ context: its reading of 6.4.74 na māṅyoge is the
        withholding of its two augment rows, 6.4.71 luṅlaṅlṛṅkṣv aḍ udāttaḥ and 6.4.72 āḍ ajādīnām, through the engine's
        own row-withholding argument (conjugate(..., off=)); those cells are counted separately as replayed under 6.4.74.

A position agrees when the table's form is one of the written readings of that position; a row of several branches is
also checked at the tuple level (uniform / mixed). The causal rows of PG31 (ṇic beyond the present system), the tāt
words (no row for 7.1.35) and the roots the table does not declare are placed outside the table by reason and counted.
Which reading is right where they differ is not claimed.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from proof_lab import pg_modal_registers as PMR
from proof_lab import pg_replay as PGR
from proof_lab import ting_rule_table_engine as TIN

ROOT = Path(__file__).resolve().parent.parent
PG = ROOT / "research" / "panini_grammar"
PG23 = PG / "lexical_modals"; PG25 = PG / "abhyasta_modals"; PG31 = PG / "counterfactual_contexts"; PG32 = PG / "prohibitive_lung"
SLOTS = PMR.SLOTS

KEYS = {"han": "han2", "śās": "śās2", "rud": "rud2", "svap": "svap2", "śvas": "śvas2", "an": "an2", "jakṣ": "jakṣ2", "brū": {"P": "brū2", "A": "brū2A"}, "śī": "śī2A",
        "bhī": "bhī3", "hrī": "hrī3", "pṝ": "pṝ3", "pṛ": "pṛ3", "bhṛ": {"P": "bhṛ3", "A": "bhṛ3A"}, "hāk": "hā3", "hāṅ": "hā3A", "māṅ": "mā3A", "nij": {"P": "nij3", "A": "nij3A"},
        "vij": {"P": "vij3", "A": "vij3A"}, "viṣ": {"P": "viṣ3", "A": "viṣ3A"}, "jāgṛ": "jāgṛ2", "daridrā": "daridrā2", "cakās": "cakās2", "ṛ": None,
        "bhū": "bhū", "gam": "gam", "nī": "nī", "kṛ": "kṛ", "pac": "pac", "labh": "labh", "edh": "edh", "dhūñ": {"P": "dhū5", "A": "dhū5A"},
        "hṛ": "hṛ", "svṛ": "svṛ", "nṛt": "nṛt", "vṛt": "vṛt", "vṛdh": "vṛdh", "śṛdh": "śṛdh", "syand": "syand", "budh": "budh", "kṛṣ": "kṛṣ", "vand": "vand", "mud": "mud", "īkṣ": "īkṣ", "īh": "īh",   # declared by theorum/160
        "iṣ": "iṣ6", "kṛp": "kṛp", "sthā": "sthā", "pā": "pā1",   # declared by theorum/161
        "dā": "dā", "vid": "vid2"}   # vid declared by theorum/162
OPTIONS = {"bhī": "6.4.115 bhiyo 'nyatarasyām (bibhitām / bibhītām)", "hāk": "6.4.116 jahāteś ca (jahitām / jahītām; 6.4.117 ā ca hau: jahāhi / jahihi / jahīhi)",
           "dhūñ": "7.2.44 svaratisūtisūyatidhūñūdito vā (adhoṣyat / adhaviṣyat)", "nṛt": "7.2.57 se 'sici kṛtacṛtacchṛdatṛdanṛtaḥ (anartsyat / anartiṣyat)",
           "syand": "7.2.44 (ūdit: asyantsyata / asyandiṣyata)", "kṛp": "7.2.44 (ūdit: akalpsyata / akalpiṣyata)", "īh": "8.3.79 vibhāṣeṭaḥ (aihidhvam / aihiḍhvam)"}
SOURCES = {"6.4.115": "bhiyo 'nyatarasyām", "6.4.116": "jahāteś ca", "6.4.117": "ā ca hau", "7.2.44": "svaratisūtisūyatidhūñūdito vā", "7.2.57": "se 'sici kṛtacṛtacchṛdatṛdanṛtaḥ",
           "8.3.79": "vibhāṣeṭaḥ", "6.4.74": "na māṅyoge", "6.4.71": "luṅlaṅlṛṅkṣv aḍ udāttaḥ", "6.4.72": "āḍ ajādīnām", "7.1.35": "tuhyos tātaṅṅ āśiṣy anyatarasyām"}
AUGMENT_ROWS = ("6.4.71", "6.4.72")   # withheld for the māṅ rows: 6.4.74 na māṅyoge
SOURCES.update({"6.4.34": "śāsa id aṅhaloḥ", "6.4.35": "śā hau", "8.3.60": "śāsivasighasīnāṁ ca"})
ADJUDICATED = {   # the written cells the table does not reproduce, adjudicated against the source: here the TABLE is wrong
    "śās-P:loṭ:2s": {"written": "śādhi", "ours": "śiḍḍhi", "verdict": "the written form", "reason": "6.4.35 śā hau: śās → śā before hi (Kāśikā: śādhi); the table has no row for 6.4.35 and lets 6.4.34 śāsa id aṅhaloḥ and 6.4.101 run instead — a missing row of the verbal table, corrected by theorum/158"},
    **{f"śās-P:liṅ:{c}": {"written": "śiṣ" + e, "ours": o, "verdict": "the written form", "reason": "6.4.34 śāsa id aṅhaloḥ: ā of śās → i before the hal-initial ṅit yāsuṭ (3.4.103), then 8.3.60 śāsivasighasīnāṁ ca: the s of śās → ṣ after that i (Kāśikā: śiṣyāt); the table's 6.4.34 row does not reach the 3sg yāsuṭ cell and its 8.3.60 row reads only a following t / v / m — two row defects of the verbal table, corrected by theorum/158"}
      for c, e, o in (("3s", "yāt", "śāsyāt"), ("3d", "yātām", "śisyātām"), ("3p", "yuḥ", "śāsyuḥ"), ("2s", "yāḥ", "śāsyāḥ"), ("2d", "yātam", "śisyātam"), ("2p", "yāta", "śisyāta"), ("1s", "yām", "śāsyām"), ("1d", "yāva", "śisyāva"), ("1p", "yāma", "śisyāma"))},
}


def key_for(root: str, pada: str | None):
    k = KEYS.get(root)
    return k.get(pada or "P") if isinstance(k, dict) else k


def replay(key: str, lak: str, cell: str, pada: str, off=()) -> str | None:
    try:
        return TIN.conjugate(key, lak, cell, pada=pada, off=off)[0]
    except Exception:  # noqa: BLE001
        return None


def compare(row_id: str, root: str, pada: str, lak: str, tuples: list[list], st: Counter, branch_rows: dict, undeclared: Counter, options: dict, dis: dict, off=(), status="replayed") -> None:
    key = key_for(root, pada); branch_of = []
    for i, cell in enumerate(SLOTS):
        readings: list[str] = []
        for t in tuples:
            v = t[i]; readings.extend(sorted(v) if isinstance(v, set) else [v])
        st["positions"] += 1
        if key is None:
            st["root_not_declared"] += 1; undeclared[root] += 1; continue
        ours = replay(key, lak, cell, pada, off)
        if ours is None:
            st["pada_not_declared"] += 1; undeclared[f"{root} ({pada})"] += 1; continue
        st[status] += 1
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
        branch_rows[f"{row_id}:{lak}"] = {"branches": len(tuples), "branch_of_each_cell": branch_of, "uniform": uniform, "option": OPTIONS.get(root, "")}


def tuple_rows(section: str, pattern: str) -> list[tuple]:
    out = []
    for line in section.splitlines():
        m = re.match(pattern, line)
        if m:
            out.append(m.groups())
    return out


def factor_rows(section: str) -> list[tuple[str, str, str]]:
    out = []
    for line in section.splitlines():
        m = re.match(r"\|\s*([^|\s]+)\s*\|\s*([^|\s]+)\s*\|\s*([^|\s]+)\s*\|", line)
        if m and m.group(1) not in ("Root", "---", "Exact") and m.group(2) not in ("P",):
            out.append((m.group(1), m.group(2), m.group(3)))
    return out


def section(text: str, start: str, end: str | None) -> str:
    i = text.index(start); j = text.index(end) if end else len(text)
    return text[i:j]


def o_tuple(kind: str, factor) -> list:
    ends = PMR.O_P if kind == "P" else PMR.O_A
    if isinstance(factor, set):
        return [{f + e for f in factor} for e in ends]
    return [factor + e for e in ends]


# ---------------------------------------------------------------------------------------------------------------------
def pg23() -> dict[str, Any]:
    text = (PG23 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0
    for root, pada, body in tuple_rows(section(text, "## P1", "## P2"), r"\|\s*(\S+)\s+([PA])\s*\|\s*\((.*)\)\s*\|"):
        tup = [PMR.parse_set(x) for x in PMR.split_top(body)]; assert len(tup) == 9, (root, tup)
        rows += 1; compare(f"{root}-{pada}", root, pada, "loṭ", [tup], st, br, und, opt, dis)
    for root, k, j in factor_rows(section(text, "## P2", "## P3")):
        if k != "—":
            rows += 1; compare(f"{root}-P", root, "P", "liṅ", [o_tuple("P", k)], st, br, und, opt, dis)
        if j != "—":
            rows += 1; compare(f"{root}-A", root, "A", "liṅ", [o_tuple("A", j)], st, br, und, opt, dis)
    tat = len(re.findall(r"\|\s*\S+\s*\|\s*\S+tāt\s*\|", section(text, "## P3", "## P4")))
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "placed_outside_the_table": {"tāt words at P 3sg / 2sg": {"words": tat, "reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}}


def pg25() -> dict[str, Any]:
    text = (PG25 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0
    for pada, sec in (("P", section(text, "## P1", "## P2")), ("A", section(text, "## P2", "## P3"))):
        for root, body in tuple_rows(sec, r"\|\s*(\S+)\s*\|\s*\((.*)\)\s*\|"):
            tup = [PMR.parse_set(x) for x in PMR.split_top(body)]; assert len(tup) == 9, (root, tup)
            rows += 1; compare(f"{root}-{pada}", root, pada, "loṭ", [tup], st, br, und, opt, dis)
    for root, k, j in factor_rows(section(text, "## P3", "## P4")):
        if k != "—":
            rows += 1; compare(f"{root}-P", root, "P", "liṅ", [o_tuple("P", PMR.parse_set(k))], st, br, und, opt, dis)
        if j != "—":
            rows += 1; compare(f"{root}-A", root, "A", "liṅ", [o_tuple("A", PMR.parse_set(j))], st, br, und, opt, dis)
    tat = sum(len(PMR.parse_set(m.group(1))) if m.group(1).startswith("{") else 1 for m in re.finditer(r"\|\s*\S+\s*\|\s*(\{[^}]*\}|\S+tāt)\s*\|", section(text, "## P4", "## P5")))
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "placed_outside_the_table": {"tāt words at P 3sg / 2sg": {"words": tat, "reason": "no row for 7.1.35 tuhyos tātaṅṅ āśiṣy anyatarasyām in the table"}}}


def pg31() -> dict[str, Any]:
    text = (PG31 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0; causal = 0
    basic = section(text, "## P1", "## P3"); caus = section(text, "## P3", "## P4")
    groups: dict[tuple[str, str], list] = {}; ids: dict[tuple[str, str], list] = {}
    for m in re.finditer(r"\|(R\d\d)\|(\S+)\|([PA])\|(\d)\|[^|]*\|" + r"([^|]+)\|" * 9, basic):
        tup = [PMR.parse_set(x.strip()) for x in m.groups()[4:]]
        groups.setdefault((m.group(2), m.group(3)), []).append(tup); ids.setdefault((m.group(2), m.group(3)), []).append(m.group(1))
    for (root, pada), tuples in groups.items():
        rows += len(tuples); compare("+".join(ids[(root, pada)]), root, pada, "lṛṅ", tuples, st, br, und, opt, dis)
    causal = len(re.findall(r"\|R\d\d\|\S+\|[PA]\|\d\|", caus))
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "placed_outside_the_table": {"causal lṛṅ rows (P3)": {"rows": causal, "positions": causal * 9, "reason": "ṇic beyond the present system: the verbal table's ṇic is laṭ / laṅ / loṭ / liṅ only"}}}


def pg32() -> dict[str, Any]:
    text = (PG32 / "PARADIGMS.md").read_text(encoding="utf-8")
    st = Counter(); und = Counter(); opt = {}; dis = {}; br = {}; rows = 0
    def cell(x: str):
        x = x.strip()
        return {y.strip() for y in x.split("/")} if "/" in x else x
    for sec_name, lak, off, status in (("## P1", "luṅ", (), "replayed"), ("## P2", "luṅ", AUGMENT_ROWS, "replayed_under_6.4.74_augment_rows_withheld"), ("## P3", "laṅ", AUGMENT_ROWS, "replayed_under_6.4.74_augment_rows_withheld")):
        nxt = {"## P1": "## P2", "## P2": "## P3", "## P3": "## P4"}[sec_name]
        for m in re.finditer(r"\|(P\d\d)\|(\S+)\|([PA])\|([^|]+)\|" + r"([^|]+)\|" * 9, section(text, sec_name, nxt)):
            tup = [cell(x) for x in m.groups()[4:]]
            rows += 1; compare(m.group(1), m.group(2), m.group(3), lak, [tup], st, br, und, opt, dis, off=off, status=status)
    return {"rows_replayed": rows, "statuses": dict(sorted(st.items())), "roots_not_declared": dict(sorted(und.items())), "other_branch_of_an_option": opt, "to_adjudicate": dis, "branch_rows": br,
            "augment_rows_withheld_for_the_mang_rows": list(AUGMENT_ROWS), "placed_outside_the_table": {}}


def build_certificate() -> dict[str, Any]:
    r = {"PG23": pg23(), "PG25": pg25(), "PG31": pg31(), "PG32": pg32()}
    tot = Counter()
    for v in r.values():
        for k, n in v["statuses"].items():
            tot[k] += n
    adjudicated = {}
    for p, v in r.items():
        for k, d in list(v["to_adjudicate"].items()):
            if k in ADJUDICATED and ADJUDICATED[k]["written"] in d["written"] and ADJUDICATED[k]["ours"] == d["ours"]:
                adjudicated[f"{p}:{k}"] = {**d, **ADJUDICATED[k]}; del v["to_adjudicate"][k]
    tot["other_branch_of_an_option"] = sum(len(v["other_branch_of_an_option"]) for v in r.values()); tot["to_adjudicate"] = sum(len(v["to_adjudicate"]) for v in r.values()); tot["adjudicated"] = len(adjudicated)
    mixed = {f"{p}:{k}": v for p, pk in r.items() for k, v in pk["branch_rows"].items() if not v["uniform"]}
    tot["branch_rows"] = sum(len(v["branch_rows"]) for v in r.values()); tot["branch_rows_mixed"] = len(mixed)
    und = Counter()
    for v in r.values():
        und.update(v["roots_not_declared"])
    checks = {"replay_run_and_recorded": tot["replayed"] > 0, "pg23_rows_read": r["PG23"]["rows_replayed"] == 10 + 10, "pg25_rows_read": r["PG25"]["rows_replayed"] == 19 + 19,
              "pg31_basic_rows_read": r["PG31"]["rows_replayed"] == 32, "pg32_rows_read": r["PG32"]["rows_replayed"] == 26,
              "every_option_cell_names_its_sutra": all(any(o["option"].startswith(s) for s in SOURCES) for v in r.values() for o in v["other_branch_of_an_option"].values()),
              "augment_rows_are_rows_of_the_table": all(a in TIN.IDS for a in AUGMENT_ROWS), "every_adjudication_names_its_sutra": all(v["reason"].split(" ")[0] in SOURCES for v in adjudicated.values())}
    status = "PASS_PG_MODAL_REGISTERS_II_CANDIDATE" if all(checks.values()) else "FAIL_PG_MODAL_REGISTERS_II_CANDIDATE"
    return {"schema": "rkf.pg_modal_registers_ii_candidate.v1", "status": status, "checks": checks, "sources": SOURCES, "options": OPTIONS, "packets": r, "totals": dict(tot), "adjudicated": adjudicated,
            "roots_not_declared_by_the_verbal_table": dict(sorted(und.items())), "branch_rows_the_table_realises_mixed": mixed,
            "claim_boundary": {
                "proved_by_exact_finite_certificate": ["the explicit registers of PG23 §P1–P2, PG25 §P1–P3, PG31 §P1–P2 and PG32 §P1–P3 are read from the written files; every position on a declared root and pada is replayed by the verbal table (the māṅ rows with the two augment rows withheld, 6.4.74); the agreements, the other-branch cells (named by sūtra), the tuple-level branch uniformity and every disagreement (both forms) are listed; the undeclared roots and the positions outside the table are counted by reason"],
                "counted_not_claimed": ["the counts: on the packets in the repository at this commit"],
                "NOT_claimed": ["which reading is right where they differ", "the tāt forms (no 7.1.35 row), the causal lṛṅ (beyond the present system), the undeclared roots", "RH, YM"],
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
        for k, d in list(v["other_branch_of_an_option"].items())[:4]:
            print("        option:", k, d["ours"], d["written"])
    for k, v in cert["adjudicated"].items():
        print("    adjudicated:", k, v["written"], "→", v["ours"], "|", v["verdict"])
    print("    totals:", cert["totals"]); print("    undeclared:", cert["roots_not_declared_by_the_verbal_table"])
    for k, v in cert["branch_rows_the_table_realises_mixed"].items():
        print("    mixed branches:", k, v["branch_of_each_cell"], v["option"][:60])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
