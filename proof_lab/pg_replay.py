from __future__ import annotations

"""Exact certificate (theorum/154): THE WRITTEN CONSTRUCTION REPLAYED — every attested form the grammar-construction
packets (research/panini_grammar/PG*, the written line) hold as a reference case is re-derived by the certified tables
(theorum/129's verbal table, theorum/125's nominal table, theorum/151's kṛt table) from the same lexical entry, and the
two answers compared; and every sūtra the packets' rule records cite is placed against the ledger (a row of a table, a
ledger entry, or neither).

The written construction is one reading of the grammar, made by hand with its sources; the tables are another, made
as code and certified against the independent generator. Where both derive the same word from the same root, they
can disagree only by a rule one of them lacks. This certificate counts the agreements and names every disagreement
and every case outside the tables' scope. It is the test the written line deferred ("grammar tests / replay"); it
tests the packets that are in the repository, and re-runs on each packet that arrives.

What is checked:
  R1  every reference case the tables can read (a declared root, a tense / voice / pada the tables carry) is replayed
      and the result recorded; the disagreements are listed, each with both forms;
  R2  every sūtra id in the packets' rule records is a record of the pinned edition (SUTRAPATHA.tsv) with the same
      Devanāgarī text;
  R3  the placement of those sūtras against the ledger is counted (rows / ledger / neither), with the 'neither' list.
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
from proof_lab import sup_rule_table_engine as SUP
from proof_lab import ting_rule_table_engine as TIN

ROOT = Path(__file__).resolve().parent.parent
PG = ROOT / "research" / "panini_grammar"
SUTRAPATHA = PG / "SUTRAPATHA.tsv"
SOURCES = {   # the sūtras named as the options the two lines realised on different branches — quoted from the pinned edition
    "3.4.84": "bruvaḥ pañcānām ādita āho bruvaḥ", "7.2.114": "mṛjer vṛddhiḥ", "3.1.82": "stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuś ca", "7.3.95": "turustuśamyamaḥ sārvadhātuke",
    "7.3.90": "ūrṇoter vibhāṣā", "6.4.115": "bhiyo 'nyatarasyām", "6.4.116": "jahāteś ca", "8.4.65": "jharo jhari savarṇe",
    "8.2.40": "jhaṣas tathor dho 'dhaḥ", "8.4.53": "jhalāṁ jaś jhaśi",   # theorum/160: the adjudication of indhe / inddhe
    "3.4.83": "vido laṭo vā",   # theorum/162: vid declared
}
OPTIONS = {   # lexical id → the sūtra whose option the two lines realised on different branches (both forms the grammar's)
    "1020039": "3.4.84 bruvaḥ pañcānām ādita āho bruvaḥ (āha / bravīti)", "1020061": "7.2.114 mṛjer vṛddhiḥ with the vārttika mṛjer vibhāṣā (mārjanti / mṛjanti)",
    "1090006": "3.1.82 stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuś ca (śnu / śnā)", "1090007": "3.1.82 (śnu / śnā)", "1090008": "3.1.82 (śnu / śnā)", "1090009": "3.1.82 (śnu / śnā)", "1090010": "3.1.82 (śnu / śnā)",
    "1020028": "7.3.95 tuś ca … the īṭ of ru / tu / stu optional (ravīti / rauti)", "1020029": "7.3.95 (tavīti / tauti)", "1020038": "7.3.95 (stavīti / stauti)", "1020034": "7.3.90 ūrṇoter vibhāṣā (ūrṇoti / ūrṇauti)",
    "1030002": "6.4.115 bhiyo 'nyatarasyām (bibhitaḥ / bibhītaḥ)", "1030009": "6.4.116 jahāteś ca (jahitaḥ / jahītaḥ)",
    "1070001": "8.4.65 jharo jhari savarṇe (runddhaḥ / rundhaḥ: the d before dh optionally dropped)", "1070006": "8.4.65 (kṣuntte / kṣunte)", "1070008": "8.4.65 (chṛntte / chṛnte)", "1070009": "8.4.65 (tṛntte / tṛnte)",
    "1070020": "8.4.65 (unttaḥ / untaḥ; und declared by theorum/160)",
    "1020059": "3.4.83 vido laṭo vā: the ṇal-series optional for vid in laṭ (veda / vetti, vidatuḥ / vittaḥ, viduḥ / vidanti, vettha / vetsi, vidathuḥ / vitthaḥ, vida / vittha, veda / vedmi, vidva / vidvaḥ, vidma / vidmaḥ — the written line realises the ṇal branch, the table the tiṅ branch; vid declared by theorum/162)",
}
ADJUDICATED = {   # a written reference form the table does not reproduce, adjudicated against the source (theorum/160); the kṣiṇoti case stays to adjudicate
    "snam_lat:1070011:A:0:50": {"written": "indhe", "ours": "inddhe", "verdict": "the table's form",
                                "reason": "8.2.40 jhaṣas tathor dho 'dhaḥ: the t of te → dh after the jhaṣ dh of indh (the śnam's a dropped by 6.4.111), then 8.4.53 jhalāṁ jaś jhaśi: dh → d before dh — inddhe; the written line's own 2pl of the same root is inddhve and its other 3sg case writes inddhe; the one case is a slip of the reference list"},
}
PERSON = {"prathama": "3", "madhyama": "2", "uttama": "1"}
NUMBER = {"eka": "s", "dvi": "d", "bahu": "p"}
TENSE = {"present": "laṭ", "past": "laṅ", "imperative": "loṭ", "optative": "liṅ", "future": "lṛṭ", "perfect": "liṭ", "aorist": "luṅ", "periphrastic_future": "luṭ", "benedictive": "āśīrliṅ", "conditional": "lṛṅ"}


def norm(rid: str) -> str:
    return re.sub(r"[a-z]+$", "", rid)


def same(a: str, b: str) -> bool:
    """The two lines write the anusvāra differently (ṁ / ṃ): one sound."""
    return a.replace("ṃ", "ṁ") == b.replace("ṃ", "ṁ")


def engine_roots_by_code() -> dict[str, list[str]]:
    """The verbal table's root keys by Dhātupāṭha code (research/panini_grammar/DHATUPATHA.tsv), with the pada they declare."""
    out: dict[str, list[str]] = {}
    for r, l, cs, pd in TIN.SUITE:
        if r in TIN.NASAL:
            up, g, pd0, _ = TIN.NASAL[r]
        else:
            up, pd0 = TIN.ROOTS[r]; g = TIN.GANA.get(r, 1)
        e = TIN.dhatu_entry(up, g)
        if e:
            out.setdefault(e[0], [])
            if r not in out[e[0]]:
                out[e[0]].append(r)
    return out


def packets() -> list[Path]:
    return sorted(p for p in PG.iterdir() if p.is_dir() and (p / "REFERENCE_CASES.json").exists())


def lexical_index(p: Path) -> dict[str, dict]:
    f = p / "LEXICAL_ENTRIES.json"
    if not f.exists():
        return {}
    d = json.loads(f.read_text(encoding="utf-8"))
    return {e["id"]: e for e in d.get("entries", [])}


def expected_iast(p: Path) -> dict[str, list[str]]:
    f = p / "VERIFICATION_RESULT.json"
    if not f.exists():
        return {}
    d = json.loads(f.read_text(encoding="utf-8"))
    return {c["id"]: c.get("expected", []) for c in d.get("cases", []) if c.get("expected")}


def replay_case(case: dict, lex: dict, by_code: dict[str, list[str]]) -> dict[str, Any]:
    req = case.get("request") or {}
    lid = req.get("lexical_id"); e = lex.get(lid)
    if e is None:
        return {"status": "no_lexical_entry"}
    code = e.get("baseindex")
    roots = by_code.get(code, [])
    if not roots:
        return {"status": "root_not_declared", "code": code, "aupadeshik": e.get("aupadeshik")}
    if req.get("prefixes"):
        return {"status": "prefixed_not_in_tables"}
    tense = req.get("tense") or "present"; voice = req.get("voice") or "kartari"
    lak = TENSE.get(tense)
    if lak is None:
        return {"status": "tense_not_read", "tense": tense}
    pada = req.get("pada")
    if req.get("formation") == "causative" or req.get("causative_licensed") is not None:
        pada_code = {"P": "NP", "A": "NA"}.get(pada)
        if lak not in TIN.PRESENT or pada_code is None:
            return {"status": "causative_beyond_the_present_system", "tense": tense}
    elif voice == "karmani":
        if lak not in TIN.PRESENT:
            return {"status": "karmani_beyond_the_present_system", "tense": tense}
        pada_code = "K"
    elif voice == "kartari":
        pada_code = pada if pada in ("P", "A") else None
        if pada_code is None:
            return {"status": "pada_not_read", "pada": pada}
    else:
        return {"status": "voice_not_read", "voice": voice}
    cell = PERSON.get(req.get("person"), "?") + NUMBER.get(req.get("number"), "?")
    if "?" in cell:
        return {"status": "cell_not_read"}
    # the root key: the one declared with this pada, else the first (the tables declare one pada per ubhayapadin key)
    key = roots[0]
    for r in roots:
        pd0 = TIN.NASAL[r][2] if r in TIN.NASAL else TIN.ROOTS[r][1]
        if pd0 == pada or pd0 == "U":
            key = r; break
    try:
        ours = TIN.conjugate(key, lak, cell, pada=pada_code)[0]
    except Exception as ex:  # noqa: BLE001
        return {"status": "engine_error", "error": str(ex)[:120], "root": key, "lak": lak, "cell": cell}
    return {"status": "replayed", "root": key, "lak": lak, "cell": cell, "pada": pada_code, "ours": ours}


def r1_replay() -> dict[str, Any]:
    by_code = engine_roots_by_code(); out = {}; totals = Counter(); disagreements = {}; options = {}; undeclared = Counter(); adjudicated = {}
    for p in packets():
        cases = json.loads((p / "REFERENCE_CASES.json").read_text(encoding="utf-8"))["cases"]
        lex = lexical_index(p); exp = expected_iast(p); st = Counter(); agree = 0; replayed = 0
        for c in cases:
            if c.get("kind") not in ("derive", "attested_member"):
                st["not_a_form_case:" + str(c.get("kind"))] += 1; continue
            expected = exp.get(c["id"]) or []
            if not expected:
                st["no_iast_expectation"] += 1; continue
            r = replay_case(c, lex, by_code)
            st[r["status"]] += 1
            if r["status"] == "root_not_declared":
                undeclared[f"{r['code']} {r.get('aupadeshik')}"] += 1
            if r["status"] == "replayed":
                replayed += 1
                lid = (c.get("request") or {}).get("lexical_id")
                if any(same(r["ours"], e) for e in expected):
                    agree += 1
                elif lid in OPTIONS:
                    options[f"{p.name}:{c['id']}"] = {"ours": r["ours"], "written": expected, "option": OPTIONS[lid]}
                elif f"{p.name}:{c['id']}" in ADJUDICATED and ADJUDICATED[f"{p.name}:{c['id']}"]["written"] in expected and ADJUDICATED[f"{p.name}:{c['id']}"]["ours"] == r["ours"]:
                    adjudicated[f"{p.name}:{c['id']}"] = {"ours": r["ours"], "written": expected, "root": r["root"], "lak": r["lak"], "cell": r["cell"], **ADJUDICATED[f"{p.name}:{c['id']}"]}
                else:
                    disagreements[f"{p.name}:{c['id']}"] = {"ours": r["ours"], "written": expected, "root": r["root"], "lak": r["lak"], "cell": r["cell"], "pada": r["pada"]}
        out[p.name] = {"cases": len(cases), "replayed": replayed, "agree": agree, "statuses": dict(sorted(st.items()))}
        totals["cases"] += len(cases); totals["replayed"] += replayed; totals["agree"] += agree
    totals["other_branch_of_an_option"] = len(options); totals["to_adjudicate"] = len(disagreements); totals["adjudicated"] = len(adjudicated)
    return {"packets": out, "totals": dict(totals), "other_branch_of_an_option": options, "to_adjudicate": disagreements, "adjudicated": adjudicated, "roots_of_the_written_line_not_declared_by_the_tables": dict(sorted(undeclared.items()))}


def sutrapatha() -> dict[str, str]:
    out = {}
    for line in SUTRAPATHA.read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 3:
            out[parts[0]] = parts[2]
    return out


def r2_r3_rules() -> dict[str, Any]:
    sp = sutrapatha(); rows = {norm(i) for i in SUP.IDS} | {norm(i) for i in TIN.IDS} | {norm(i) for i in KRT.IDS}
    hand = {x for v in LED.HAND_CODED.values() for x in v}; meta = {x for v in LED.META.values() for x in v}; comp = {x for v in LED.COMPILED.values() for x in v}
    cited = {}; not_in_edition = []; text_mismatch = []
    for p in sorted(PG.iterdir()):
        f = p / "RULE_RECORDS.json"
        if not p.is_dir() or not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        for rec in d.get("records", []):
            sid = rec.get("sid"); skt = rec.get("sanskrit")
            if not sid:
                continue
            cited.setdefault(sid, set()).add(p.name)
            if sid not in sp:
                not_in_edition.append((p.name, sid))
            elif skt and skt.replace(" ", "") != sp[sid].replace(" ", ""):
                text_mismatch.append((p.name, sid, skt, sp[sid]))
    placement = Counter(); neither = []
    for sid in cited:
        if sid in rows:
            placement["row_of_a_table"] += 1
        elif sid in hand or sid in meta or sid in comp:
            placement["ledger_hand_meta_compiled"] += 1
        else:   # the ledger's 'cited' level is what the capsules mention and is not counted here, so that this certificate does not read its own capsule
            placement["neither"] += 1; neither.append(sid)
    return {"sutras_cited_by_the_packets": len(cited), "per_packet": {p: 0 for p in []} | dict(Counter(pk for v in cited.values() for pk in v)),
            "not_in_pinned_edition": not_in_edition, "text_mismatch": text_mismatch, "placement": dict(placement), "cited_by_the_packets_only": sorted(neither, key=lambda x: tuple(int(t) for t in x.split("."))),
            "checks": {"every_cited_sutra_in_the_pinned_edition": not not_in_edition, "every_cited_text_matches_the_pinned_edition": not text_mismatch}}


def build_certificate() -> dict[str, Any]:
    r1 = r1_replay(); r23 = r2_r3_rules()
    checks = {"r1_replay_run_and_recorded": r1["totals"].get("replayed", 0) > 0, **{f"r2_{k}": v for k, v in r23["checks"].items()}}
    status = "PASS_PG_REPLAY_CANDIDATE" if all(checks.values()) else "FAIL_PG_REPLAY_CANDIDATE"
    return {"schema": "rkf.pg_replay_candidate.v1", "status": status, "checks": checks, "sources": SOURCES, "options": OPTIONS, "replay": r1, "rules": r23,
            "claim_boundary": {
                "proved_by_exact_finite_certificate": ["R1: the counts of the written line's reference forms the tables replay and of the agreements; every disagreement listed with both forms, as the other branch of a named option (both forms the grammar's) or as a case to adjudicate", "R2: every sūtra the packets' rule records cite is a record of the pinned edition with the same text", "R3: the placement of every cited sūtra against the tables and the ledger's hand-coded / meta / compiled levels, the ones in neither listed"],
                "counted_not_claimed": ["the agreement rate: a count on the packets in the repository at this commit, re-run as packets arrive", "the cases outside the tables' scope, by reason"],
                "NOT_claimed": ["that either reading of the grammar is right where they differ: a disagreement names a rule one of them lacks, to be adjudicated against the source", "the packets' own verification results (their grammar.py); the refusal cases; anything about packets not in the repository; RH, YM"],
            }}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=sorted) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"]); print("    checks:", cert["checks"])
    for p, v in cert["replay"]["packets"].items():
        print(f"    {p}: {v['agree']} / {v['replayed']} of {v['cases']}  {v['statuses']}")
    print("    totals:", cert["replay"]["totals"])
    for k, v in list(cert["replay"]["to_adjudicate"].items())[:40]:
        print("      ", k, v["ours"], v["written"])
    print("    undeclared roots:", len(cert["replay"]["roots_of_the_written_line_not_declared_by_the_tables"]))
    r = cert["rules"]; print("    rules:", r["sutras_cited_by_the_packets"], r["placement"], "not in edition:", r["not_in_pinned_edition"][:5], "text mismatch:", len(r["text_mismatch"]))
    print("    cited by the packets only:", r["cited_by_the_packets_only"])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
