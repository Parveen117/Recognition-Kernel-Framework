"""PG11 source overlays; every predecessor view remains unchanged."""
from copy import deepcopy

from research.panini_grammar.present_expansion.scope import ReviewedScope as PG10Scope


class ReviewedScope(PG10Scope):
    def __init__(self, records, pg5, pg6, pg7, pg9, pg10, policies):
        super().__init__(records, pg5, pg6, pg7, pg9, pg10)
        for policy in policies:
            frame = self.views[policy["target"]]
            if policy["action"] == "supply":
                for word in policy["terms"]:
                    term = next(t for t in self.frame(policy["source"])["own"] if t["term"] == word)
                    if any(t["term"] == word and t["source"] == policy["source"] for t in frame["inherited"]):
                        raise ValueError("PG11 inheritance was already supplied")
                    frame["inherited"].append({"uid": f"{policy['id']}:{term['uid']}",
                        "term": word, "source": policy["source"], "kind": "anuvrtti",
                        "status": "COMMENTARY_SUPPLIED", "policy": policy["id"],
                        "evidence": deepcopy(policy["evidence"])})
            elif policy["action"] == "exclude":
                matches = [t for t in frame["inherited"] if t["source"] == policy["source"]
                           and t["term"] == policy["raw_term"] and t["kind"] == policy["kind"]]
                if len(matches) != 1:
                    raise ValueError("PG11 exclusion no longer matches its source annotation")
                term = matches[0]
                frame["inherited"].remove(term)
                frame["excluded"].append({**deepcopy(term), "status": "EXCLUDED_BY_COMMENTARY",
                    "policy": policy["id"], "evidence": deepcopy(policy["evidence"])})
            else:
                raise ValueError("Unknown PG11 scope policy")
            frame["decisions"].append({"policy": policy["id"], "action": policy["action"]})

    def compile(self, record):
        """Bind repeated words to their own source occurrences and cases.

        The two bruvaḥ tokens of 3.4.84 have different grammatical roles.
        A case or semantic role is reviewed data, never inferred from position.
        """
        frame = self.frame(record["sid"])
        available = frame["own"] + frame["inherited"]
        bound, errors = [], []
        for requirement in record["terms"]:
            matches = [t for t in available if all(t[k] == requirement[k]
                       for k in ("term", "source", "kind"))]
            if requirement.get("occurrence_uid"):
                matches = [t for t in matches if t["uid"] == requirement["occurrence_uid"]]
            if len(matches) != 1:
                errors.append({"requirement": requirement, "reason": "missing or ambiguous source occurrence"})
                continue
            term = matches[0]
            if requirement.get("case") and requirement["case"] != term.get("case"):
                errors.append({"requirement": requirement, "reason": "case annotation differs"})
                continue
            bound.append({**term, "role": requirement["role"]})
        ids = [t["uid"] for t in bound]
        if len(set(ids)) != len(ids):
            errors.append({"reason": "a source occurrence was assigned twice"})
        missing = [t for t in available if t["uid"] not in ids]
        if missing:
            errors.append({"reason": "frame occurrences lack reviewed roles", "terms": missing})
        return {"sid": record["sid"], "text": frame["text"], "terms": bound,
                "opcode": record["opcode"], "parameters": deepcopy(record.get("parameters", {})),
                "requires": deepcopy(record.get("requires", {})),
                "status": "UNRESOLVED_RECORD" if errors else "COMPILED_REVIEWED_RECORD",
                "errors": errors, "source_frame": frame}
