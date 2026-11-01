"""PG10 source overlays on the frozen PG4–PG9 views."""
from copy import deepcopy

from research.panini_grammar.abhyasa_lat.scope import ReviewedScope as PG9Scope


class ReviewedScope(PG9Scope):
    def __init__(self, records, pg5, pg6, pg7, pg9, policies):
        super().__init__(records, pg5, pg6, pg7, pg9)
        for policy in policies:
            frame = self.views[policy["target"]]
            if policy["action"] == "supply":
                for term in policy["terms"]:
                    source = next(t for t in self.frame(policy["source"])["own"] if t["term"] == term)
                    if any(t["term"] == term and t["source"] == policy["source"] for t in frame["inherited"]):
                        raise ValueError("PG10 supplied inheritance already exists")
                    frame["inherited"].append({"uid": f"{policy['id']}:{source['uid']}",
                        "term": term, "source": policy["source"], "kind": "anuvrtti",
                        "status": "COMMENTARY_SUPPLIED", "policy": policy["id"],
                        "evidence": deepcopy(policy["evidence"])})
            else:
                matches = [t for t in frame["inherited"] if t["source"] == policy["source"]
                           and t["term"] == policy["raw_term"] and t["kind"] == policy["kind"]]
                if len(matches) != 1:
                    raise ValueError("PG10 scope decision no longer matches its annotation")
                term = matches[0]
                excluded = {**deepcopy(term), "status": "EXCLUDED_BY_COMMENTARY",
                            "policy": policy["id"], "evidence": deepcopy(policy["evidence"])}
                if policy["action"] == "exclude":
                    frame["inherited"].remove(term)
                elif policy["action"] == "split":
                    excluded["term"] = policy["excluded_term"]
                    term.update(term=policy["retained_term"], status="COMMENTARY_SPLIT", policy=policy["id"])
                else:
                    raise ValueError("Unknown PG10 scope policy")
                frame["excluded"].append(excluded)
            frame["decisions"].append({"policy": policy["id"], "action": policy["action"]})
