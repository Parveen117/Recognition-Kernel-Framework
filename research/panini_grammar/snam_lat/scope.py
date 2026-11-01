"""PG7 scope decisions on the unchanged PG4–PG6 source views."""
from copy import deepcopy

from research.panini_grammar.non_thematic_lat.scope import ReviewedScope as PG6Scope


class ReviewedScope(PG6Scope):
    def __init__(self, records, pg5_policies, pg6_policies, policies):
        super().__init__(records, pg5_policies, pg6_policies)
        for policy in policies:
            frame = self.views[policy["target"]]
            matches = [t for t in frame["inherited"] if t["source"] == policy["source"]
                       and t["term"] == policy["raw_term"] and t["kind"] == policy["kind"]]
            if policy["action"] != "exclude" or len(matches) != 1:
                raise ValueError("PG7 scope decision no longer matches the pinned annotation")
            term = matches[0]
            frame["inherited"].remove(term)
            frame["excluded"].append({**term, "status": "EXCLUDED_BY_COMMENTARY",
                "policy": policy["id"], "evidence": deepcopy(policy["evidence"])})
            frame["decisions"].append({"policy": policy["id"], "action": policy["action"]})
