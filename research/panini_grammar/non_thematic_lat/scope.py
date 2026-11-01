"""PG6 attributed scope overlays, applied after the frozen PG5 overlay."""
from copy import deepcopy

from research.panini_grammar.vikarana_lat.scope import ReviewedScope as PG5Scope


class ReviewedScope(PG5Scope):
    def __init__(self, records, prior_policies, policies):
        super().__init__(records, prior_policies)
        for policy in policies:
            frame = self.views[policy["target"]]
            if policy["action"] == "supply":
                for term in policy["terms"]:
                    source_terms = self.frame(policy["source"])["own"]
                    source = next(t for t in source_terms if t["term"] == term)
                    if any(t["term"] == term and t["source"] == policy["source"] for t in frame["inherited"]):
                        raise ValueError("Supplied inheritance already exists; re-review the source")
                    frame["inherited"].append({"uid": f"{policy['id']}:{source['uid']}", "source": policy["source"],
                        "term": term, "kind": "anuvrtti", "status": "COMMENTARY_SUPPLIED",
                        "evidence": deepcopy(policy["evidence"]), "policy": policy["id"]})
            else:
                matches = [t for t in frame["inherited"] if t["source"] == policy["source"] and t["term"] == policy["raw_term"]]
                if len(matches) != 1:
                    raise ValueError("Scope overlay no longer matches its source")
                term = matches[0]
                excluded = deepcopy(term)
                excluded.update(status="EXCLUDED_BY_COMMENTARY", evidence=deepcopy(policy["evidence"]), policy=policy["id"])
                if policy["action"] == "split":
                    excluded["term"] = policy["excluded_term"]
                    term.update(term=policy["retained_term"], status="COMMENTARY_SPLIT", policy=policy["id"])
                elif policy["action"] == "exclude":
                    frame["inherited"].remove(term)
                else:
                    raise ValueError("Unknown PG6 scope policy")
                frame["excluded"].append(excluded)
            frame["decisions"].append({"policy": policy["id"], "action": policy["action"]})
