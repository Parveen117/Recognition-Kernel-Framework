"""PG4: executable scope views over pinned editorial annotations.

Raw Sanskrit scope inference is not supplied. Every inherited term retains its
source; the six PG2 adjudications act as explicit policies, not source edits.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.verification.source_audit import scope_graph, sutra_id

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def sid_tuple(sid):
    return tuple(map(int, sid.split(".")))


def parse_padaccheda(record):
    """Preserve all fields; the extra annotation column is not guessed away."""
    output = []
    for index, raw in enumerate(filter(None, record.get("pc", "").split("##"))):
        parts = raw.split("$")
        token = {"uid": f"{record['i']}:pc:{index}", "raw": raw, "term": parts[0],
                 "source": sutra_id(record["i"]), "kind": "own", "fields": parts[1:]}
        if len(parts) != 5:
            token["status"] = "UNRESOLVED_ANNOTATION_SHAPE"
        else:
            category, case, number, extra = parts[1:]
            token.update(category=category, case=case or None, number=number or None,
                         extra_case_field=extra or None)
            if category == "S" and case in {str(n) for n in range(8)} and number in {"0", "1", "2", "3"} and not extra:
                token["status"] = "EXPLICIT_CASE_ANNOTATION"
            else:
                token["status"] = "PRESERVED_UNINTERPRETED_FIELDS"
        output.append(token)
    return output


class ScopeIndex:
    def __init__(self, records, policies=None):
        self.records = {sutra_id(r["i"]): deepcopy(r) for r in records}
        if len(self.records) != len(records):
            raise ValueError("Duplicate sūtra identity")
        self.graph = scope_graph(records)
        self.policies = load("SCOPE_POLICIES.json")["policies"] if policies is None else deepcopy(policies)
        self.views = {sid: self._resolve(sid) for sid in self.records}

    def _resolve(self, sid):
        active, excluded, decisions = [], [], []
        for index, raw_edge in enumerate(self.graph["contexts"][sid]):
            edge = {**deepcopy(raw_edge), "uid": f"{sid}:inherited:{index}",
                    "raw_source": raw_edge["source"], "raw_term": raw_edge["term"],
                    "status": "EDITORIAL_ANNOTATION"}
            selected = []
            for policy in self.policies:
                if edge["kind"] != "adhikara" or edge["source"] != policy["source"]:
                    continue
                if policy.get("target") and sid != policy["target"]:
                    continue
                if policy.get("after") and sid_tuple(sid) <= sid_tuple(policy["after"]):
                    continue
                if policy.get("through") and sid_tuple(sid) > sid_tuple(policy["through"]):
                    continue
                selected.append(policy)
            if len(selected) > 1:
                raise ValueError(f"Overlapping unadjudicated policies for {edge}")
            if selected:
                policy = selected[0]
                edge.update(policy=policy["id"], evidence=deepcopy(policy["evidence"]))
                action = policy["action"]
                if action in {"quarantine", "exclude"}:
                    edge["status"] = "QUARANTINED" if action == "quarantine" else "EXCLUDED_BY_COMMENTARY"
                    excluded.append(edge)
                elif action == "split":
                    discarded = {**deepcopy(edge), "term": policy["exclude_term"], "status": "EXCLUDED_COMPONENT"}
                    edge.update(term=policy["retain_term"], status="COMMENTARY_SPLIT")
                    active.append(edge)
                    excluded.append(discarded)
                elif action == "correct_reference":
                    edge.update(source=policy["corrected_source"], status="COMMENTARY_CORRECTED_REFERENCE")
                    active.append(edge)
                elif action == "accept":
                    edge["status"] = "COMMENTARY_CONFIRMED"
                    active.append(edge)
                else:
                    raise ValueError(f"Unknown scope action: {action}")
                decisions.append({"uid": edge["uid"], "policy": policy["id"], "action": action})
            else:
                # Unreviewed structural anomalies cannot enter executable views.
                heading = self.graph["headings"].get(edge["source"])
                flagged = edge["kind"] == "adhikara" and (heading is None or not
                    sid_tuple(edge["source"]) <= sid_tuple(sid) <= sid_tuple(heading["end"]))
                if flagged:
                    edge["status"] = "UNRESOLVED_SCOPE"
                    excluded.append(edge)
                else:
                    active.append(edge)
        return {"sid": sid, "text": self.records[sid]["s"],
                "own": parse_padaccheda(self.records[sid]), "inherited": active,
                "excluded": excluded, "decisions": decisions,
                "semantic_status": "NOT_INFERRED_FROM_CASE_NUMBERS"}

    def frame(self, sid):
        return deepcopy(self.views[sid])

    def compile(self, record):
        """Bind reviewed term roles to the resolved frame, never an ancestor's action."""
        frame = self.frame(record["sid"])
        available = frame["own"] + frame["inherited"]
        bound, errors = [], []
        for requirement in record["terms"]:
            matches = [term for term in available if term["term"] == requirement["term"]
                       and term["source"] == requirement["source"]
                       and term["kind"] == requirement["kind"]]
            if len(matches) != 1:
                errors.append({"requirement": requirement, "reason": "missing or ambiguous inherited term"})
                continue
            term = matches[0]
            if requirement.get("case") and term.get("case") != requirement["case"]:
                errors.append({"requirement": requirement, "reason": "case annotation differs"})
                continue
            bound.append({**term, "role": requirement["role"]})
        required_keys = {(t["term"], t["source"], t["kind"]) for t in record["terms"]}
        unassigned = [t for t in available if (t["term"], t["source"], t["kind"]) not in required_keys]
        if unassigned:
            errors.append({"reason": "frame terms lack reviewed roles", "terms": unassigned})
        return {"sid": record["sid"], "text": frame["text"], "terms": bound,
                "opcode": record["opcode"], "parameters": deepcopy(record.get("parameters", {})),
                "requires": deepcopy(record.get("requires", {})),
                "status": "COMPILED_REVIEWED_RECORD" if not errors else "UNRESOLVED_RECORD",
                "errors": errors, "source_frame": frame}

    def summary(self):
        tokens = [t for frame in self.views.values() for t in frame["own"]]
        decisions = [d for frame in self.views.values() for d in frame["decisions"]]
        return {"sutra_records": len(self.records), "raw_scope_edges": len(self.graph["edges"]),
                "padaccheda_tokens": len(tokens), "token_status_counts": dict(Counter(t["status"] for t in tokens)),
                "nonstandard_annotation_shapes": [t for t in tokens if t["status"] == "UNRESOLVED_ANNOTATION_SHAPE"],
                "scope_policy_counts": dict(Counter(d["policy"] for d in decisions)),
                "active_inherited_terms": sum(len(f["inherited"]) for f in self.views.values()),
                "excluded_term_counts": dict(Counter(t["status"] for f in self.views.values() for t in f["excluded"])),
                "raw_sanskrit_scope_parser": False, "all_sutra_semantic_compilation": False}


def applicability(compiled, facts):
    if compiled["status"] != "COMPILED_REVIEWED_RECORD":
        return "UNRESOLVED"
    missing = [name for name in compiled["requires"] if name not in facts or facts[name] is None]
    if missing:
        return "UNRESOLVED"
    return "APPLICABLE" if all(facts[name] == value for name, value in compiled["requires"].items()) else "INAPPLICABLE"
