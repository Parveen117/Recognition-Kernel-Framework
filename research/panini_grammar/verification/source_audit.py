"""PG2 read-only source census. Annotation parsing is not raw-sūtra parsing."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


SOURCE_COMMIT = "5744762f010d677cfb43f347a42d02796cf615d6"
SOURCE_FILES = (
    "README.md", "sutraani/data.txt", "sutraani/kashika.txt",
    "sutraani/balamanorama.txt", "sutraani/tattvabodhini.txt",
    "dhatu/data.txt", "ganapath/data.txt", "unaadi/data.txt",
    "paribhashendushekhar/data.txt",
)
MODULES = (
    "paninian_seam_calculus", "sup_vibhakti_resolver_ladder",
    "ting_lat_parasmaipada", "stem_classes_gayatri_coverage",
    "lat_atmanepada", "pada_to_line_external_sandhi",
    "karaka_vibhakti_carrier", "paninian_instruction_format",
)
SID = re.compile(r"([1-8])\.([1-4])\.([1-9][0-9]*)([a-z]*)$")


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sutra_id(key: str) -> str:
    if not re.fullmatch(r"[1-8][1-4][0-9]{3}", key) or int(key[2:]) == 0:
        raise ValueError(f"Invalid source key: {key!r}")
    return f"{key[0]}.{key[1]}.{int(key[2:])}"


def scope_graph(records: list[dict]) -> dict:
    """Keep each borrowed term and its source; never import an ancestor's action."""
    keys = {record["i"] for record in records}
    if len(keys) != len(records):
        raise ValueError("Duplicate sūtra identity")
    edges = []
    headings = {}
    contexts = {}
    for record in records:
        key = record["i"]
        sid = sutra_id(key)
        context = []
        for field in ("an", "ad"):
            for raw in filter(None, record.get(field, "").split("##")):
                parts = raw.split("$")
                expected = 2 if field == "an" else 4
                if len(parts) != expected or not parts[0]:
                    raise ValueError((sid, field, "malformed annotation", raw))
                term = parts[0]
                ref = parts[1] if field == "an" else parts[1] + parts[2] + parts[3].zfill(3)
                source = sutra_id(ref)
                if ref not in keys:
                    raise ValueError((sid, field, "missing source", ref))
                edge = {"target": sid, "source": source, "term": term,
                        "kind": "anuvrtti" if field == "an" else "adhikara",
                        "evidence": "publisher_annotation", "raw": raw}
                edges.append(edge)
                context.append(edge)
        contexts[sid] = context
        for raw in filter(None, record.get("type", "").split("##")):
            parts = raw.split("$")
            if parts[0] == "AD":
                if len(parts) != 3 or parts[2] not in keys:
                    raise ValueError((sid, "heading endpoint needs review", raw))
                headings[sid] = {"name": parts[1], "end": sutra_id(parts[2])}
    # The chosen witness happens to have backward anuvṛtti edges. We report
    # that property; it is not imposed as a universal grammatical axiom.
    key_of = lambda sid: tuple(map(int, sid.split(".")))
    forward = [e for e in edges if key_of(e["source"]) > key_of(e["target"])]
    self_an = [e for e in edges if e["kind"] == "anuvrtti" and e["source"] == e["target"]]
    outside = []
    non_headings = []
    for edge in edges:
        if edge["kind"] != "adhikara":
            continue
        source, target = edge["source"], edge["target"]
        if source not in headings:
            non_headings.append(edge)
        elif not key_of(source) <= key_of(target) <= key_of(headings[source]["end"]):
            outside.append(edge)
    return {"edges": edges, "contexts": contexts, "headings": headings,
            "forward_edges": forward, "self_anuvrtti": self_an,
            "edges_outside_declared_heading_range": outside,
            "scope_sources_without_AD_tag": non_headings}


def scope_report(records: list[dict]) -> dict:
    graph = scope_graph(records)
    edges = graph["edges"]
    selected = {}
    for sid in ("3.1.1", "3.1.2", "3.1.91", "6.4.1", "1.4.13"):
        dependents = [e["target"] for e in edges if e["kind"] == "adhikara" and e["source"] == sid]
        selected[sid] = {"heading": graph["headings"].get(sid),
                         "declared_scope_members": len(set(dependents)),
                         "first_members": dependents[:3], "last_members": dependents[-3:]}
    return {
        "status": "ANNOTATION_STRUCTURE_AUDITED_NOT_RAW_TEXT_COMPILATION",
        "records": len(records), "edge_counts": dict(Counter(e["kind"] for e in edges)),
        "edges_sha256": digest(edges), "heading_count": len(graph["headings"]),
        "forward_edges": graph["forward_edges"], "self_anuvrtti": graph["self_anuvrtti"],
        "heading_self_edges": sum(e["kind"] == "adhikara" and e["source"] == e["target"] for e in edges),
        "edges_outside_declared_heading_range": graph["edges_outside_declared_heading_range"],
        "scope_sources_without_AD_tag": graph["scope_sources_without_AD_tag"],
        "selected_headings": selected,
        "review_contexts": {sid: graph["contexts"][sid] for sid in (
            "1.3.3", "1.3.5", "1.3.6", "1.3.7", "1.3.8",
            "3.1.68", "6.1.78", "6.1.87", "6.1.97", "7.3.84")},
    }


def code_census(root: Path) -> dict:
    """Static source inspection; does not execute or replay predecessor suites."""
    routines = []
    registrations = []
    semantic_ids = set()
    record_ids = []
    files = {}
    for module in MODULES:
        path = root / "proof_lab" / f"{module}.py"
        source = path.read_text(encoding="utf-8")
        files[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
        tree = ast.parse(source)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                m = re.search(r"(?:^|_)([1-8])_([1-4])_([0-9]+)(?:_|$)", node.name)
                if m:
                    routines.append({"sid": ".".join(m.groups()), "module": module,
                                     "function": node.name, "line": node.lineno})
                if module == "karaka_vibhakti_carrier" and node.name in ("assign", "abhihita"):
                    for child in ast.walk(node):
                        if isinstance(child, ast.Constant) and isinstance(child.value, str) and SID.fullmatch(child.value):
                            semantic_ids.add(child.value)
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            names = [t.id for t in (node.targets if isinstance(node, ast.Assign) else [node.target]) if isinstance(t, ast.Name)]
            if set(names) & {"RULES", "NEW", "SANDHI"}:
                for child in ast.walk(node.value):
                    if not isinstance(child, ast.Tuple) or len(child.elts) < 2:
                        continue
                    first = child.elts[0]
                    if isinstance(first, ast.Constant) and isinstance(first.value, str) and (m := SID.fullmatch(first.value)):
                        no_action = isinstance(child.elts[1], ast.Lambda)
                        registrations.append({"sid": ".".join(m.groups()[:3]), "label": first.value,
                                              "module": module, "line": child.lineno,
                                              "kind": "declared_guard_placeholder" if no_action else "registered_routine"})
            if module == "karaka_vibhakti_carrier" and set(names) & {"SANJNA", "VIBHAKTI"}:
                for child in ast.walk(node.value):
                    if isinstance(child, ast.Constant) and isinstance(child.value, str) and SID.fullmatch(child.value):
                        semantic_ids.add(child.value)
            if module == "paninian_instruction_format" and "SANDHI_RECORDS" in names:
                for record in node.value.elts:
                    fields = {k.value: v for k, v in zip(record.keys, record.values)}
                    record_ids.append(fields["sid"].value)
    ids = {r["sid"] for r in routines} | {r["sid"] for r in registrations if r["kind"] == "registered_routine"} | semantic_ids | set(record_ids)
    word = [r for r in routines if r["module"] == "paninian_instruction_format" and r["function"].startswith("c_")]
    return {"status": "STATIC_ID_PRESENCE_NOT_RULE_COMPLETENESS", "source_sha256": files,
            "record_interpreted_sandhi_ids": record_ids,
            "specialized_T80_word_routines": word,
            "T80_distinct_operation_ids": sorted(set(record_ids) | {r["sid"] for r in word}),
            "identified_operation_or_semantic_ids": sorted(ids, key=lambda x: tuple(map(int, x.split(".")))),
            "identified_id_count": len(ids), "named_routines": routines,
            "registrations": registrations, "semantic_mapping_ids": sorted(semantic_ids),
            "minimum_distinct_demonstrated_root_names": ["bhū", "gam", "nī", "edh", "labh"],
            "limitations": ["Embedded predicates and source mentions are not independent complete rules.",
                            "A registry entry is evidence of code presence, not valid-Sanskrit soundness.",
                            "Root names are not a complete sense/gaṇa-indexed Dhātupāṭha."]}


def lexical_report(source_root: Path) -> dict:
    sutra_ids = {sutra_id(r["i"]) for r in load(source_root / "sutraani/data.txt")["data"]}
    roots = load(source_root / "dhatu/data.txt")["data"]
    root_entries = [r for r in roots if r.get("tags") != "ganasutra"]
    directives = [r for r in roots if r.get("tags") == "ganasutra"]
    ganas = load(source_root / "ganapath/data.txt")["data"]
    unadi = load(source_root / "unaadi/data.txt")["data"]
    paribhasa = load(source_root / "paribhashendushekhar/data.txt")["data"]
    root_ids = Counter(r["i"] for r in roots)
    homonyms = defaultdict(list)
    for root in root_entries:
        homonyms[root["dhatu"]].append({k: root.get(k) for k in ("i", "baseindex", "gana", "pada", "settva")})
    missing = [r["i"] for r in root_entries if any(not r.get(k) for k in ("dhatu", "aupadeshik", "gana", "pada", "settva"))]
    gana_ids = Counter(str(r["ind"]) for r in ganas)
    unadi_ids = Counter(r["i"] for r in unadi)
    return {
        "status": "DATA_SCHEMA_AUDITED_NOT_LEXICAL_OR_DERIVATIONAL_CLOSURE",
        "dhatu_records": len(roots), "dhatu_duplicate_ids": [k for k, n in root_ids.items() if n > 1],
        "dhatu_root_entries": len(root_entries), "dhatu_ganasutra_directives": len(directives),
        "dhatu_missing_core_fields": missing,
        "root_unknown_core_field_ids": [r["i"] for r in root_entries if any(r.get(k) == "-" for k in ("aupadeshik", "gana", "pada", "settva"))],
        "dhatu_pada_tag_counts": dict(Counter(r["pada"] for r in root_entries)),
        "dhatu_settva_tag_counts": dict(Counter(r["settva"] for r in root_entries)),
        "supplied_pada_and_settva_are_not_derived_from_marker_audit": True,
        "distinct_root_spellings": len(homonyms), "homonymous_spellings": sum(len(v) > 1 for v in homonyms.values()),
        "homonym_examples": {s: homonyms[s] for s in ("भू", "कृ", "मिद्", "नी")},
        "gana_records": len(ganas), "gana_duplicate_ids": [k for k, n in gana_ids.items() if n > 1],
        "gana_tag_counts": dict(Counter(r.get("type", "") for r in ganas)),
        "gana_untyped_ids": [r["ind"] for r in ganas if not r.get("type")],
        "gana_missing_core_field_ids": [r["ind"] for r in ganas if any(not r.get(k) for k in ("name", "sutra", "words"))],
        "gana_invalid_sutra_links": [{"id": r["ind"], "sutra": r.get("sutra")} for r in ganas if r.get("sutra") not in sutra_ids],
        "gana_richtext_membership_records": sum("<" in r.get("words", "") for r in ganas),
        "gana_member_text_is_not_a_flat_word_list": True,
        "unadi_records": len(unadi), "unadi_duplicate_ids": [k for k, n in unadi_ids.items() if n > 1],
        "unadi_missing_affix_fields": [r["i"] for r in unadi if not r.get("pratyay")],
        "unadi_missing_text_or_commentary_ids": [r["i"] for r in unadi if not r.get("sutra") or not r.get("sk")],
        "unadi_sample": [{k: r.get(k) for k in ("i", "sutra", "pratyay")} for r in unadi[:3]],
        "paribhasa_records": len(paribhasa),
        "selected_paribhasa": [{"id": r["num"], "text": r["paribhasha"]} for r in paribhasa if r["num"] in {"42", "43", "44", "45", "46", "49", "50", "51", "57", "58", "59"}],
    }
