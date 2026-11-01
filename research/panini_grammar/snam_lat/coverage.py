"""Static inventory audit, with evidence grades kept separate.

Reads frozen predecessor reports; never executes their verifiers. This is not
a complete audit of every historical hand-coded grammar function in the repo.
"""
from collections import Counter
import json
from pathlib import Path

GRAMMAR = Path(__file__).resolve().parent.parent


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_coverage(records, roots, pg7_comparison):
    pg2 = read(GRAMMAR / "verification/VERIFICATION_RESULT.json")
    pg4 = read(GRAMMAR / "scoped_derivations/VERIFICATION_RESULT.json")
    concurrent = read(GRAMMAR / "snam_lat/CONCURRENT_THEOREM_SNAPSHOT.json")
    legacy = concurrent["baseline_ledger"]
    per_stage, ids = {}, set()
    for stage in ("scoped_derivations", "vikarana_lat", "non_thematic_lat", "snam_lat"):
        rows = read(GRAMMAR / stage / "RULE_RECORDS.json")["records"]
        per_stage[stage] = [r["sid"] for r in rows]
        ids.update(per_stage[stage])
    sources = {f"{r['a']}.{r['p']}.{int(r['n'])}" for r in records}
    if not ids <= sources or len(sources) != len(records):
        raise ValueError("A rule ID is not uniquely present in the source inventory")
    if concurrent["concurrent_branch"]["ledger"]["counts"]["astadhyayi_total"] != len(records):
        raise ValueError("The recorded companion ledger uses a different edition total")
    root_count = pg2["lexical"]["dhatu_root_entries"]
    if len(roots) != pg2["lexical"]["dhatu_records"]:
        raise ValueError("Lexical denominator changed")
    stages, all_entries = [], []
    for stage, mode in (("vikarana_lat", "thematic_lat"), ("non_thematic_lat", "non_thematic_lat"), ("snam_lat", "snam_lat")):
        entries = [e for e in read(GRAMMAR / stage / "LEXICAL_ENTRIES.json")["entries"] if e["derivation"] == mode]
        cmp = pg7_comparison if stage == "snam_lat" else read(GRAMMAR / stage / "VERIFICATION_RESULT.json")["implementation_comparison"]
        if len(entries) != cmp["lexemes"]:
            raise ValueError("Lexical manifest and stage comparison disagree")
        stages.append({"stage": stage, "root_ids": [e["id"] for e in entries],
                       **{k: cmp[k] for k in ("lexemes", "paradigms", "cells", "branches")},
                       "evidence": "new PG7 direct check" if stage == "snam_lat" else "frozen report read; not replayed"})
        all_entries.extend(entries)
    completed = {e["id"] for e in all_entries}
    if len(completed) != len(all_entries):
        raise ValueError("Overlapping complete-form IDs must be deduplicated, not added")
    return {"schema": "rkf.panini.pg7.coverage.v1", "author": "Monty",
        "overall_grammar_completion_percent": None,
        "why_no_overall_percent": "No exhaustive rule-domain closure rubric exists. Text, source-bound records, lexical preprocessing and word generation have different denominators.",
        "text_inventory": {"records": len(records), "chapters": len({r['a'] for r in records}),
            "padas": len({(r['a'], r['p']) for r in records}), "status": "CATALOGUED_NOT_SEMANTICALLY_COMPILED",
            "legacy_declared_total": legacy["counts"]["astadhyayi_total"],
            "concordance_to_legacy_total": "Companion ledger now uses the pinned edition total; full cross-edition variant concordance is not asserted"},
        "pg4_to_pg7_source_bound_records": {"definitions": sum(map(len, per_stage.values())), "distinct_sutra_ids": len(ids),
            "source_ids_without_a_record_in_these_four_packets": len(sources - ids),
            "per_stage_ids": per_stage, "distinct_ids": sorted(ids, key=lambda s: tuple(map(int, s.split('.')))),
            "meaning": "bounded term/opcode contracts; includes reviewed visibility obligations and re-used sūtras, not full implementations",
            "excludes": "PG1 reading notes, PG2/PG3 local contracts, and historical hand-coded/theorem modules"},
        "historical_ledger": {"counts": legacy["counts"], "commit": legacy["commit"],
            "status": "BASELINE_SNAPSHOT_NOT_CURRENT_COMPANION_BRANCH_OR_ADDITIVE_VERIFIED_COVERAGE"},
        "companion_theorem_branch": concurrent["concurrent_branch"],
        "scope": {"publisher_edges": sum(pg2["scope"]["edge_counts"].values()),
            "edge_counts": pg2["scope"]["edge_counts"], "raw_sanskrit_scope_inference": False,
            "general_priority_and_visibility_resolver": False},
        "lexical_preprocessing": {"root_entries": root_count, "ganasutra_directives": pg2["lexical"]["dhatu_ganasutra_directives"],
            "frozen_pg4_diagnostic": pg4["root_diagnostic"]["counts"], "status": "HEADWORD_COMPARISON_NOT_CONJUGATION_COVERAGE"},
        "complete_lat_profile": {"root_entries": len(completed), "root_entry_denominator": root_count,
            "root_entry_percent": round(100 * len(completed) / root_count, 3),
            "root_entries_without_complete_PG5_PG7_path": root_count - len(completed),
            "gana_root_counts": dict(sorted(Counter(e["gana"] for e in all_entries).items(), key=lambda p: int(p[0]))),
            "paradigms": sum(s["paradigms"] for s in stages), "cells": sum(s["cells"] for s in stages),
            "branches": sum(s["branches"] for s in stages), "stages": stages,
            "domain": "identified roots; exact lexical labels and supplied pada license; unprefixed classical present kartari at pause; documented spelling/option profile",
            "meaning": "root-entry fraction for this narrow generator, not percent of Sanskrit grammar verified"},
        "remaining_packages": [
            {"area": "Present verbs", "open": "Class 2 adādi, class 3 juhotyādi/reduplication, bhuj/tṛh and remaining root-specific paths, sense/pada and prefix interactions"},
            {"area": "Other verbal systems", "open": "Other lakāras, passive/bhāva, iṭ/augments, sanādi, causatives and desideratives beyond existing fragments"},
            {"area": "Nominals", "open": "Full stem classes, genders, pronouns, numerals and irregular paradigms beyond historical bounded examples"},
            {"area": "Derivation and syntax", "open": "Kṛt, taddhita, samāsa, kāraka/agreement and semantic selection"},
            {"area": "Global interpretation", "open": "Raw Sanskrit scope inference; general apavāda/nitya/antaraṅga; 1.1.56–59 and 6.4.22 visibility; full phonetic exceptions"},
            {"area": "Sources and validity", "open": "Gaṇa/Uṇādi semantics, independent edition/corpus validation, accent/Vedic domains, full Sanskrit soundness/completeness"}],
        "native_operator_and_quantum_lift": "OPEN_SEPARATE_OBLIGATION"}
