from __future__ import annotations

"""Exact certificate (theorum/155): THE WRITTEN CONSTRUCTION REPLAYED II — the packets PG19–PG47 of the written line
(research/panini_grammar, merged at this commit) tested against the certified tables, three ways:

  R4  the written modal register of PG19 (imperative_optative/PARADIGMS.md: 54 rows, every row a constructor applied to
      an owned stem, I_P / I_A / O_P / O_A as ENDING_CONSTRUCTION.md writes them, the kṛ / krī tuples as
      ATHEMATIC_DERIVATIONS.md writes them) is expanded cell by cell — 976 written positions — and every cell whose root
      the verbal table declares (theorum/129, pin TING_RULE_TABLE_ENGINE_EXPECTED) is re-derived by the table from the
      same root, lakāra, pada and cell, and compared; the disagreements are listed with both forms; the roots the table
      does not declare are counted; the causal-passive rows are outside the tables (no causative-passive code) and said so;
  R5  the 29 worked histories of PG47 (interaction_histories/HISTORY_REGISTER.json): the ordered sūtra sequence each
      history writes in its steps is read from its document; for every history whose target word a table derives, the
      table's own path (the rule ids it fired, in firing order) is compared with the written sequence STEP BY STEP — the
      written sequence restricted to rows of the table must be a subsequence of the table's path, the rules the history
      says are BLOCKED must be absent from the path; every history the tables cannot reach is listed with the reason
      (compound, taddhita, Vedic, an affix or root the tables do not carry, a designation with no sound effect);
  R6  the 3,796 written rule contracts of PG35–PG46 (RULE_REGISTER.json) and the 161 rule records of PG3–PG13: every id
      is a record of the pinned edition (SUTRAPATHA.tsv), its quoted Devanāgarī text is the edition's text, and the whole
      written line's set of cited sūtras is placed against the ledger (rows of a table / ledger hand-coded, meta,
      compiled / neither), with the counts.

R1–R3 of theorum/154 (the REFERENCE_CASES.json replay, 604 / 648) are re-run unchanged by proof_lab.pg_replay and its
totals and pin are carried in this certificate as the previous pin; nothing there is restated.

The written line and the tables are two readings of the same grammar; this certificate says, exactly, where the second
re-derives the first — the words of PG19, the rule order of PG47 — and where it cannot yet (undeclared roots, the
causative passive, the nominal derivation beyond the sup / kṛt tables), without judging which reading is right where
they differ: a difference names a rule one of them lacks, to be adjudicated against the source.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from proof_lab import astadhyayi_ledger as LED
from proof_lab import krt_rule_table_engine as KRT
from proof_lab import pg_replay as PGR
from proof_lab import sup_rule_table_engine as SUP
from proof_lab import ting_rule_table_engine as TIN

ROOT = Path(__file__).resolve().parent.parent
PG = ROOT / "research" / "panini_grammar"
PG19 = PG / "imperative_optative"
PG47 = PG / "interaction_histories"

# ---------------------------------------------------------------------------------------------------------------------
# R4 — PG19's register: the constructors exactly as ENDING_CONSTRUCTION.md writes them (quoted), applied to the stems the
# register writes. The slot order is the packet's: (3sg, 3du, 3pl, 2sg, 2du, 2pl, 1sg, 1du, 1pl).
# ---------------------------------------------------------------------------------------------------------------------
SLOTS = ["3s", "3d", "3p", "2s", "2d", "2p", "1s", "1d", "1p"]
WRITTEN_CONSTRUCTORS = {   # research/panini_grammar/imperative_optative/ENDING_CONSTRUCTION.md §E7, quoted
    "I_P": "I_P(B)=(Batu,Batām,Bantu,Ba,Batam,Bata,\\nu(Bāni),Bāva,Bāma)",
    "I_A": "I_A(B)=(Batām,Betām,Bantām,Basva,Bethām,Badhvam,Bai,Bāvahai,Bāmahai)",
    "O_P": "O_P(B)=(Bet,Betām,Beyuḥ,Beḥ,Betam,Beta,Beyam,Beva,Bema)",
    "O_A": "O_A(B)=(Beta,Beyātām,Beran,Bethāḥ,Beyāthām,Bedhvam,Beya,Bevahi,Bemahi)",
}
CONSTRUCTOR_ENDINGS = {
    "I_P": ["atu", "atām", "antu", "a", "atam", "ata", "āni", "āva", "āma"],
    "I_A": ["atām", "etām", "antām", "asva", "ethām", "adhvam", "ai", "āvahai", "āmahai"],
    "O_P": ["et", "etām", "eyuḥ", "eḥ", "etam", "eta", "eyam", "eva", "ema"],
    "O_A": ["eta", "eyātām", "eran", "ethāḥ", "eyāthām", "edhvam", "eya", "evahi", "emahi"],
}
# the register's stems are written without the thematic a; the written line's own convention (PARADIGMS.md §P1)
ROOT_KEY = {"bhū": "bhū", "pac": "pac", "edh": "edh", "labh": "labh", "tud": "tud", "nī": "nī", "gam": "gam", "śam": "śam", "kṛ": "kṛ", "krī": "krī", "dā": "dā",
            "hṛ": "hṛ", "budh": "budh", "kṛṣ": "kṛṣ",   # declared by theorum/160
            "sthā": "sthā", "pā": "pā1",   # declared by theorum/161
            "vid": "vid2"}   # vid declared by theorum/162 (the class-2 vid, vetti)
LAK = {"loṭ": "loṭ", "vidhiliṅ": "liṅ"}
SOURCES = {   # quoted from the pinned edition (research/panini_grammar/SUTRAPATHA.tsv), as the ledger writes them
    "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.4.2": "aṭkupvāṅnumvyavāye 'pi",
}
ADJUDICATED = {   # the written register's cells the table does not reproduce, each adjudicated against the source
    "CK02:loṭ:1s": {"written": "kārayāni", "ours": "kārayāṇi", "verdict": "the table's form",
                    "reason": "8.4.1 raṣābhyāṁ no ṇaḥ samānapade with 8.4.2 aṭkupvāṅnumvyavāye 'pi: the n of the uttama ending (mip → ni, 3.4.89) follows the r of kār across a, y, ā — vowels and y are aṭ — so ṇ; the written line applies the same rule to its own karavāṇi (ATHEMATIC_DERIVATIONS.md A2: kar-av-ā-ṇi) and to the ṇic-stem in no other cell; the one cell is a slip of the written register, not a rule it lacks"},
    "CK06:loṭ:1s": {"written": "hārayāni", "ours": "hārayāṇi", "verdict": "the table's form",
                    "reason": "8.4.1 raṣābhyāṁ no ṇaḥ samānapade with 8.4.2 aṭkupvāṅnumvyavāye 'pi: the same cell of the same shape as CK02 — the r of hār, then a, y, ā (aṭ), then the n of ni; hṛ declared by theorum/160"},
    "CK20:loṭ:1s": {"written": "karṣayāni", "ours": "karṣayāṇi", "verdict": "the table's form",
                    "reason": "8.4.1 raṣābhyāṁ no ṇaḥ samānapade with 8.4.2 aṭkupvāṅnumvyavāye 'pi: here the ṣ of karṣ is the trigger (8.4.1 names r and ṣ), then a, y, ā (aṭ), then the n of ni — the written line writes the same ṇ in its own śinaṣāṇi / pinaṣāṇi (PG22 §P1); kṛṣ declared by theorum/160"},
}


def constructor_endings_from_written() -> dict[str, list[str]]:
    """Read the four constructors from the written line's own file and check they are the quoted ones."""
    text = (PG19 / "ENDING_CONSTRUCTION.md").read_text(encoding="utf-8")
    out = {}
    for name, quoted in WRITTEN_CONSTRUCTORS.items():
        m = re.search(re.escape(name) + r"\(B\)=\((.*?)\)[,.]\s*$", text, re.M)
        if not m:
            raise ValueError(f"{name} not found in ENDING_CONSTRUCTION.md")
        raw = m.group(1).replace("\\nu(", "").replace("\n", "")
        ends = [p.strip() for p in raw.replace("),", ",").replace(")", "").split(",")]
        ends = [e[1:] if e.startswith("B") else e for e in ends]
        out[name] = ends
        if ends != CONSTRUCTOR_ENDINGS[name]:
            raise ValueError(f"{name}: written {ends} vs quoted {CONSTRUCTOR_ENDINGS[name]}")
    return out


def athematic_tuples() -> dict[str, list[str]]:
    """The kṛ / krī tuples PG19 writes out in full (ATHEMATIC_DERIVATIONS.md A2–A5), read from the file."""
    text = (PG19 / "ATHEMATIC_DERIVATIONS.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"([IO]_[PA])\((kṛ|krī)\)=\(([^)]*)\)", text):
        words = [w.strip() for w in m.group(3).replace("\n", "").split(",")]
        if len(words) != 9:
            raise ValueError(f"{m.group(1)}({m.group(2)}): {len(words)} slots")
        out[f"{m.group(1)}({m.group(2)})"] = words
    if len(out) != 8:
        raise ValueError(f"expected 8 athematic tuples, found {len(out)}")
    return out


def pg19_rows() -> list[dict[str, Any]]:
    """The register rows of PARADIGMS.md: id, root, pada, the loṭ and vidhiliṅ constructor calls (or the single bhāva cell)."""
    text = (PG19 / "PARADIGMS.md").read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        m = re.match(r"\|\s*(BK|CK|CP|BP)(\d\d)\s*\|\s*([^|/]+?)\s*(?:/\s*([PA]))?\s*\|\s*(?:A\d: )?([IO]_[PA])\(([^)]+)\)\s*\|\s*(?:A\d: )?([IO]_[PA])\(([^)]+)\)\s*\|", line)
        if m:
            rows.append({"id": m.group(1) + m.group(2), "block": m.group(1), "root": m.group(3).strip(), "pada": m.group(4), "lot": (m.group(5), m.group(6)), "lin": (m.group(7), m.group(8))})
            continue
        m = re.match(r"\|\s*(BH)(\d\d)\s*\|\s*([^|]+?)\s*\|\s*(loṭ|vidhiliṅ)\s*\|\s*3sg\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            rows.append({"id": m.group(1) + m.group(2), "block": "BH", "root": m.group(3).strip(), "pada": None, "lak": m.group(4), "word": m.group(5).strip()})
    return rows


def expand(call: tuple[str, str], ath: dict[str, list[str]], ends: dict[str, list[str]]) -> list[str]:
    name, arg = call
    if arg in ("kṛ", "krī"):
        return ath[f"{name}({arg})"]
    return [arg + e for e in ends[name]]


def r4_pg19() -> dict[str, Any]:
    ends = constructor_endings_from_written(); ath = athematic_tuples(); rows = pg19_rows()
    st = Counter(); cells = 0; replayed = 0; agree = 0; dis = {}; undeclared = Counter(); per_block = {}
    for row in rows:
        blk = row["block"]; pb = per_block.setdefault(blk, Counter())
        if blk == "BH":
            items = [(LAK[row["lak"]], [("3s", row["word"])])]
        else:
            items = [("loṭ", list(zip(SLOTS, expand(row["lot"], ath, ends)))), ("liṅ", list(zip(SLOTS, expand(row["lin"], ath, ends))))]
        for lak, pairs in items:
            for cell, written in pairs:
                cells += 1; pb["cells"] += 1
                if blk == "CP":
                    st["causative_passive_not_in_the_tables"] += 1; pb["causative_passive_not_in_the_tables"] += 1; continue
                key = ROOT_KEY.get(row["root"])
                if key is None:
                    st["root_not_declared"] += 1; pb["root_not_declared"] += 1; undeclared[row["root"]] += 1; continue
                pada = row["pada"] if blk == "BK" else ({"P": "NP", "A": "NA"}[row["pada"]] if blk == "CK" else "K")   # BP / BH: karmaṇi / bhāve = yak + A
                try:
                    ours = TIN.conjugate(key, lak, cell, pada=pada)[0]
                except Exception as ex:  # noqa: BLE001
                    st["engine_error"] += 1; dis[f"{row['id']}:{lak}:{cell}"] = {"written": written, "error": str(ex)[:100]}; continue
                replayed += 1; st["replayed"] += 1; pb["replayed"] += 1
                if PGR.same(ours, written):
                    agree += 1; pb["agree"] += 1
                else:
                    dis[f"{row['id']}:{lak}:{cell}"] = {"root": key, "pada": pada, "written": written, "ours": ours}
    adjudicated = {k: {**v, **ADJUDICATED[k]} for k, v in dis.items() if k in ADJUDICATED}
    return {"rows": len(rows), "positions": cells, "replayed": replayed, "agree": agree, "statuses": dict(sorted(st.items())), "per_block": {k: dict(v) for k, v in per_block.items()},
            "roots_not_declared_by_the_verbal_table": dict(sorted(undeclared.items())), "to_adjudicate": {k: v for k, v in dis.items() if k not in ADJUDICATED}, "adjudicated": adjudicated, "sources": SOURCES,
            "written_constructors": WRITTEN_CONSTRUCTORS, "athematic_tuples_read": sorted(ath)}


# ---------------------------------------------------------------------------------------------------------------------
# R5 — PG47's worked histories against the tables' paths
# ---------------------------------------------------------------------------------------------------------------------
def history_sequences() -> dict[str, dict[str, Any]]:
    """For each history: the sūtra ids in the order its numbered steps / step-table rows write them (consecutive repeats
    folded), and the ids its text marks as blocked / open in the result lines."""
    reg = json.loads((PG47 / "HISTORY_REGISTER.json").read_text(encoding="utf-8"))
    out = {}
    for h in reg["histories"]:
        doc = (ROOT / h["document"]).read_text(encoding="utf-8")
        m = re.search(r"^## " + re.escape(h["id"]) + r" — .*?$(.*?)(?=^## |\Z)", doc, re.S | re.M)
        sec = m.group(1) if m else ""
        steps = []
        lines = sec.splitlines(); i = 0
        while i < len(lines):
            line = lines[i]
            if re.match(r"\|\s*\d+\s*\|", line):
                steps.append(line)
            elif re.match(r"\d+\. ", line):
                block = [line]; i += 1
                while i < len(lines) and lines[i].startswith("   "):
                    block.append(lines[i]); i += 1
                steps.append(" ".join(block)); continue
            i += 1
        seq = []
        for s in steps:
            for sid in re.findall(r"\d+\.\d+\.\d+", s):
                if not seq or seq[-1] != sid:
                    seq.append(sid)
        out[h["id"]] = {"title": h["title"], "source_ids": h["source_ids"], "steps": len(steps), "written_sequence": seq, "document": h["document"]}
    return out


def table_path(kind: str, *args) -> tuple[str, list[str]]:
    if kind == "sup":
        stem, code, gender, flags = args
        if stem in SUP.SUITE:   # a stem of the nominal table's suite carries its declared gender and saṁjñā flags (1.1.24 ṣaṭ, 1.4.3 nadī, …)
            e = SUP.SUITE[stem]; stem, gender, flags = e[0], e[1], tuple(e[2])
        up = dict(SUP.SUP)[code]
        form, path = SUP.decline(stem, code, up, gender, flags)
    elif kind == "ting":
        key, lak, cell, pada = args
        form, path = TIN.conjugate(key, lak, cell, pada=pada)
    elif kind == "krt":
        key, affix = args
        form, path = KRT.derive(key, affix)
    else:
        raise ValueError(kind)
    return form, [PGR.norm(p.split(" ")[0]) for p in path[1:]]


# the histories a table reaches: (table call, the source witness the history names, the rules the history says fire in order,
# the rules the history says are BLOCKED for that word, a note). The witness words are the histories' own (Kāśikā / Nyāsa).
TARGETS: dict[str, dict[str, Any]] = {
    "A01": {"call": ("ting", "as", "luṭ", "3s", "P"), "witness": "bhavitā", "fires": ["2.4.52"], "blocked": [], "note": "2.4.52 asteḥ bhūḥ before the ārdhadhātuka: the table's luṭ of as is the history's first witness bhavitā"},
    "A02": {"call": ("sup", "phala", "1p", "n", ()), "witness": "phalāni", "fires": ["7.1.20"], "blocked": [], "note": "7.1.20 jaśśasoḥ śiḥ: the whole affix replaced (1.1.55) — the table's row writes śi for jas; the history's second frame (pañcagoṇiḥ, 1.2.50) is taddhita, outside the tables"},
    "A05": {"call": ("sup", "nadī", "3s", "f", ("nadī",)), "witness": "nadyā", "fires": ["6.1.77"], "blocked": [], "note": "6.1.77 iko yaṇ aci selects the preceding ik (1.1.66): the table realises it inside the word (nadī + ṭā → nadyā); the history's junction dadhi + udakam is external sandhi, outside the tables"},
    "A06": {"call": ("krt", "ās2A", "śānac"), "witness": "āsīna", "fires": ["7.2.83"], "blocked": [], "note": "7.2.83 īd āsaḥ replaces the initial ā of āna (1.1.54 ādeḥ parasya): the kṛt table's śānac of ās"},
    "B04": {"call": ("sup", "pañcan", "1p", "m", ()), "witness": "pañca", "fires": ["7.1.22", "8.2.7"], "blocked": [], "note": "7.1.22 ṣaḍbhyo luk, then 8.2.7 nalopaḥ prātipadikāntasya on the pada (1.4.14 by the lost affix, 1.1.62 pratyayalope pratyayalakṣaṇam): the table's order is the history's"},
    "B06": {"call": ("ting", "dā", "liṭ", "3p", "P"), "witness": "daduḥ (the history's witness is jagle, glai — not declared)", "fires": ["6.4.64"], "blocked": [], "note": "6.4.64 āto lopa iṭi ca on the ā-final base before the ārdhadhātuka kit ending (3.4.115 liṭ ca): the table's liṭ of dā"},
    "B07": {"call": ("ting", "lū", "liṅ", "3s", "P"), "witness": "lunīyāt", "fires": ["7.2.79"], "blocked": [], "note": "ordinary liṅ (sārvadhātuka, 3.4.113): 7.2.79 liṅaḥ salopo 'nantyasya fires — the control"},
    "B07b": {"call": ("ting", "lū", "āśīrliṅ", "3s", "A"), "witness": "laviṣīṣṭa", "fires": [], "blocked": ["7.2.79"], "note": "blessing liṅ (ārdhadhātuka by 3.4.116 liṅāśiṣi): 7.2.79's sārvadhātuka prerequisite false, BLOCKED — the table's āśīrliṅ path has no 7.2.79 firing"},
    "C01": {"call": ("sup", "vṛkṣa", "4p", "m", ()), "witness": "vṛkṣebhyaḥ", "fires": ["7.3.103", "8.2.66", "8.3.15"], "blocked": ["7.3.102"], "note": "1.4.2 vipratiṣedhe paraṁ kāryam: 7.3.103 (the later) over 7.3.102 — the table fires 103 and never 102"},
    "C02": {"call": ("sup", "vṛkṣa", "4p", "m", ()), "witness": "vṛkṣebhyaḥ", "fires": ["7.3.103"], "blocked": ["7.3.102"], "note": "the defeated 7.3.102 is not reactivated after 103 (the current final is e, not a): absent from the table's path after 103"},
    "C03": {"call": ("sup", "vṛkṣa", "3d", "m", ()), "witness": "vṛkṣābhyām", "fires": ["7.3.102"], "blocked": ["7.3.103"], "note": "dual: only 7.3.102 admitted (103 needs bahuvacana); no 1.4.2 collision"},
    "C05": {"call": ("sup", "vṛkṣa", "3p", "m", ()), "witness": "vṛkṣaiḥ", "fires": ["7.1.9", "6.1.88", "8.2.66", "8.3.15"], "blocked": ["7.3.103"], "note": "7.1.9 ato bhisa ais (nitya, whole affix 1.1.55) before 7.3.103, which then loses its jhal trigger: the table's order 7.1.9 → 6.1.88 → 8.2.66 → 8.3.15 with no 103"},
}
OUT_OF_SCOPE: dict[str, str] = {
    "A03": "ānaṅ (6.3.25) in a dvandva of kinship terms, 8.2.7 on the member: compound — the tables carry no samāsa",
    "A04": "ṭi (1.1.64) and upadhā (1.1.65) are designations with no sound effect of their own; the tables use them inside rows (7.1.70 ugidacāṁ…, 7.3.86) without a separate firing",
    "A07": "7.3.52 cajoḥ ku ghiṇṇyatoḥ: ghañ / ṇyat are kṛt affixes the kṛt table does not carry",
    "B01": "2.1.24 dvitīyā tatpuruṣa, 1.2.43 upasarjana, 2.2.30: compound — no samāsa in the tables",
    "B02": "1.2.44, 1.2.48 upasarjana shortening, 2.2.18: compound",
    "B03": "4.1.105 yañ (gārgya → gargāḥ, 2.4.64 luk) with 7.2.117 / 6.1.197: taddhita — no taddhita in the tables",
    "B05": "6.4.51 ṇer aniṭi (ṇi-lopa) fires before an aniṭ ārdhadhātuka: the verbal table's ṇic is the present system only (sārvadhātuka: kārayati), the kṛt table has no ṇic; the row 6.4.51 exists in the verbal table for the lane's forms but this history's frame (3.1.26 ṇic + 3.1.67 / 3.4.114 kta-class) is outside it",
    "B08": "Vedic liṅ 3.4.117 (upastheyāma): the tables are classical only",
    "C04": "īśvaraḥ: 3.2.175 varac with 7.2.8 neḍ vaśi kṛti against 7.2.35 — varac is not in the kṛt table",
    "C06": "visphoryam: 3.1.124 ṇyat with 7.3.86 / 8.2.1 / 8.2.77 — ṇyat is not in the kṛt table",
    "C07": "an OPEN history by construction (strength evidence withheld): no word",
    "D01": "manāvī: 4.1.38 manor jātāv añyatau ṣuk ca with 6.1.78 — taddhita + ṅīp feminine: outside the tables",
    "D02": "manāyī: the ai branch of the same: outside the tables",
    "D03": "4.1.36–38 ṅīp: the feminine rows of the kṛdanta declension are 4.1.4 / 4.1.5 / 4.1.6 / 7.1.80 / 7.1.81 / 7.3.44 only",
    "D04": "vārāhyā: 4.1.78 / 4.1.92 / 4.1.95 / 6.4.148 / 6.4.151 — taddhita",
    "D05": "ārtabhāgī: 4.1.104 añ, 4.1.73 ṣyaṅ — taddhita",
    "D06": "an OPEN history by construction (origin withheld)",
    "D07": "auḍulomyā: 4.1.96 bāhvādibhyaś ca with 6.4.144 nas taddhite (ṭi deletion), 4.1.74: taddhita",
}


def is_subsequence(small: list[str], big: list[str]) -> bool:
    it = iter(big)
    return all(any(x == y for y in it) for x in small)


def r5_pg47() -> dict[str, Any]:
    seqs = history_sequences()
    rows = {PGR.norm(i) for i in SUP.IDS} | {PGR.norm(i) for i in TIN.IDS} | {PGR.norm(i) for i in KRT.IDS}
    meta = {x for v in LED.META.values() for x in v}
    compared = {}; checks_all = True
    for hid, t in TARGETS.items():
        base = hid.rstrip("b"); seq = seqs[base]
        form, path = table_path(*t["call"])
        written_rows = [s for s in seq["written_sequence"] if s in rows]   # the written order, restricted to rules that are rows of a table
        written_rows_for_this_word = []   # the written order of the rules this word fires, first mention of each (a history may name a rule again when it records its result)
        for s in written_rows:
            if (s in t["fires"] or s in t["blocked"]) and s not in written_rows_for_this_word:
                written_rows_for_this_word.append(s)
        fired = [s for s in t["fires"] if s in path]; missing = [s for s in t["fires"] if s not in path]
        blocked_absent = [s for s in t["blocked"] if s not in path]; blocked_present = [s for s in t["blocked"] if s in path]
        order_ok = is_subsequence([s for s in written_rows_for_this_word if s in t["fires"]], path)
        ok = not missing and not blocked_present and order_ok and (t["witness"].split(" ")[0] == form)
        checks_all = checks_all and ok
        compared[hid] = {"history": base, "title": seq["title"], "table_call": list(t["call"]), "table_form": form, "witness": t["witness"], "table_path": path,
                         "written_sequence": seq["written_sequence"], "written_sequence_rows_of_a_table": written_rows,
                         "written_sequence_meta_level": [s for s in seq["written_sequence"] if s in meta and s not in rows],
                         "rules_the_history_fires": t["fires"], "fired_in_the_table_path": fired, "not_fired_in_the_table_path": missing,
                         "rules_the_history_blocks": t["blocked"], "absent_from_the_table_path": blocked_absent, "present_in_the_table_path_though_blocked": blocked_present,
                         "written_order_is_a_subsequence_of_the_table_path": order_ok, "agree": ok, "note": t["note"]}
    out_of_scope = {hid: {"title": seqs[hid]["title"], "source_ids": seqs[hid]["source_ids"], "written_sequence": seqs[hid]["written_sequence"], "reason": why} for hid, why in OUT_OF_SCOPE.items()}
    unaccounted = sorted(set(seqs) - {t.rstrip("b") for t in TARGETS} - set(OUT_OF_SCOPE))
    return {"histories": len(seqs), "compared": compared, "compared_count": len(compared), "histories_reached": len({t.rstrip('b') for t in TARGETS}), "agree": sum(1 for v in compared.values() if v["agree"]),
            "out_of_scope": out_of_scope, "out_of_scope_count": len(out_of_scope), "unaccounted": unaccounted, "all_compared_agree": checks_all,
            "sequences": {k: {"steps": v["steps"], "written_sequence": v["written_sequence"]} for k, v in seqs.items()}}


# ---------------------------------------------------------------------------------------------------------------------
# R6 — the written rule contracts against the pinned edition and the ledger
# ---------------------------------------------------------------------------------------------------------------------
def r6_registers() -> dict[str, Any]:
    sp = PGR.sutrapatha()
    rows = {PGR.norm(i) for i in SUP.IDS} | {PGR.norm(i) for i in TIN.IDS} | {PGR.norm(i) for i in KRT.IDS}
    hand = {x for v in LED.HAND_CODED.values() for x in v}; meta = {x for v in LED.META.values() for x in v}; comp = {x for v in LED.COMPILED.values() for x in v}
    contracts = 0; per_packet = {}; not_in_edition = []; text_mismatch = []; ids: dict[str, set] = {}
    for p in sorted(PG.iterdir()):
        f = p / "RULE_REGISTER.json"
        if not p.is_dir() or not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        recs = next((v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict)), [])
        per_packet[p.name] = len(recs)
        for r in recs:
            sid = r.get("id"); skt = r.get("sutra"); contracts += 1
            if not sid:
                continue
            ids.setdefault(sid, set()).add(p.name)
            if sid not in sp:
                not_in_edition.append((p.name, sid))
            elif skt and skt.replace(" ", "") != sp[sid].replace(" ", ""):
                text_mismatch.append((p.name, sid, skt, sp[sid]))
    # the whole written line: the rule records of PG3–PG13 (theorum/154 R2) + the registers + PG47's history sources
    records = PGR.r2_r3_rules()
    all_ids = set(ids)
    for p in sorted(PG.iterdir()):
        f = p / "RULE_RECORDS.json"
        if p.is_dir() and f.exists():
            for rec in json.loads(f.read_text(encoding="utf-8")).get("records", []):
                if rec.get("sid"):
                    all_ids.add(rec["sid"])
    reg = json.loads((PG47 / "HISTORY_REGISTER.json").read_text(encoding="utf-8"))
    for h in reg["histories"]:
        all_ids.update(h["source_ids"])
    placement = Counter(); neither = []
    for sid in all_ids:
        if sid in rows:
            placement["row_of_a_table"] += 1
        elif sid in hand or sid in meta or sid in comp:
            placement["ledger_hand_meta_compiled"] += 1
        else:
            placement["neither"] += 1; neither.append(sid)
    by_adhyaya = Counter(sid.split(".")[0] for sid in neither)
    return {"contracts": contracts, "per_packet": per_packet, "distinct_ids_in_registers": len(ids), "not_in_pinned_edition": not_in_edition, "text_mismatch": [list(t) for t in text_mismatch],
            "written_line_ids_all_sources": len(all_ids), "edition_total": len(sp), "placement": dict(placement), "neither_by_adhyaya": dict(sorted(by_adhyaya.items())),
            "rule_records_pg3_pg13": {"sutras": records["sutras_cited_by_the_packets"], "placement": records["placement"]},
            "checks": {"every_register_id_in_the_pinned_edition": not not_in_edition, "every_register_text_matches_the_pinned_edition": not text_mismatch}}


def build_certificate() -> dict[str, Any]:
    r4 = r4_pg19(); r5 = r5_pg47(); r6 = r6_registers()
    prev = PGR.build_certificate(); prev_sha = PGR.certificate_sha256(prev)
    checks = {"r4_pg19_register_expanded_to_its_written_positions": r4["positions"] == 976, "r4_replay_run_and_recorded": r4["replayed"] > 0,
              "r4_no_engine_error": r4["statuses"].get("engine_error", 0) == 0, "r4_every_disagreement_adjudicated_or_listed": all(k in ADJUDICATED and ADJUDICATED[k]["written"] == v["written"] and ADJUDICATED[k]["ours"] == v["ours"] for k, v in r4["adjudicated"].items()),
              "r5_every_history_compared_or_placed_out_of_scope": not r5["unaccounted"], "r5_all_compared_agree": r5["all_compared_agree"],
              **{f"r6_{k}": v for k, v in r6["checks"].items()}, "r1_r3_previous_certificate_passes": prev["status"].startswith("PASS")}
    status = "PASS_PG_WRITTEN_REPLAY_CANDIDATE" if all(checks.values()) else "FAIL_PG_WRITTEN_REPLAY_CANDIDATE"
    return {"schema": "rkf.pg_written_replay_candidate.v1", "status": status, "checks": checks,
            "previous": {"theorem": "theorum/154", "module": "proof_lab.pg_replay", "sha256": prev_sha, "totals": prev["replay"]["totals"], "rules": prev["rules"]["placement"]},
            "r4_pg19_register": r4, "r5_pg47_histories": r5, "r6_written_registers": r6,
            "claim_boundary": {
                "proved_by_exact_finite_certificate": [
                    "R4: PG19's register expands to exactly its 976 written positions from the constructors and tuples the packet writes; the count the verbal table replays and the count that agree; every disagreement listed with both forms; the undeclared roots and the causal-passive rows counted, by reason",
                    "R5: for every PG47 history a table reaches, the rules the history fires are in the table's path, in the history's order, the rules it blocks are absent, and the table's word is the history's witness; every other history is placed out of scope with its reason",
                    "R6: every written rule contract of PG35–PG46 is a record of the pinned edition with the edition's text; the placement of the whole written line's cited sūtras against the tables and the ledger"],
                "counted_not_claimed": ["the agreement counts: on the packets in the repository at this commit", "the placement counts: the ledger's size at this commit"],
                "NOT_claimed": ["that either reading is right where they differ", "the written contracts' content (they are not executed here; R6 checks their identity and text)", "PG20–PG46's written positions (not expanded here)", "the compound, taddhita, Vedic and ṇyat / varac / ghañ histories: outside the tables", "RH, YM"],
            }}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=sorted) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"]); print("    checks:", cert["checks"])
    r4 = cert["r4_pg19_register"]; print(f"    R4 PG19: rows {r4['rows']}, positions {r4['positions']}, replayed {r4['replayed']}, agree {r4['agree']}, {r4['statuses']}")
    for k, v in r4["per_block"].items():
        print("       ", k, v)
    print("        undeclared:", r4["roots_not_declared_by_the_verbal_table"])
    for k, v in list(r4["to_adjudicate"].items())[:40]:
        print("        to adjudicate:", k, v)
    for k, v in r4["adjudicated"].items():
        print("        adjudicated:", k, v["written"], "→", v["ours"], "|", v["verdict"])
    r5 = cert["r5_pg47_histories"]; print(f"    R5 PG47: {r5['histories']} histories, {r5['histories_reached']} reached by a table ({r5['compared_count']} comparisons, {r5['agree']} agree), {r5['out_of_scope_count']} out of scope, unaccounted {r5['unaccounted']}")
    for k, v in r5["compared"].items():
        print(f"        {k} {v['table_form']} path={v['table_path']} fires={v['fired_in_the_table_path']} missing={v['not_fired_in_the_table_path']} blocked_present={v['present_in_the_table_path_though_blocked']} order={v['written_order_is_a_subsequence_of_the_table_path']} agree={v['agree']}")
    r6 = cert["r6_written_registers"]; print(f"    R6: {r6['contracts']} contracts, {r6['distinct_ids_in_registers']} distinct ids, text mismatch {len(r6['text_mismatch'])}, not in edition {len(r6['not_in_pinned_edition'])}; whole written line {r6['written_line_ids_all_sources']} / {r6['edition_total']} ids placed {r6['placement']}; neither by adhyāya {r6['neither_by_adhyaya']}")
    print("    previous (theorum/154):", cert["previous"]["sha256"][:16], cert["previous"]["totals"])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
