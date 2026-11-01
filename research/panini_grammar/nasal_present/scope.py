"""PG12 source view, preserving the earlier occurrence-bound compiler."""
from copy import deepcopy

from research.panini_grammar.lexical_present.scope import ReviewedScope as PG11Scope


class ReviewedScope(PG11Scope):
    def __init__(self, records, pg5, pg6, pg7, pg9, pg10, pg11, policies):
        super().__init__(records, pg5, pg6, pg7, pg9, pg10, pg11)
        for policy in policies:
            if policy["action"] != "supply":
                raise ValueError("PG12 only admits its reviewed supplied inheritance")
            frame = self.views[policy["target"]]
            for word in policy["terms"]:
                candidates = [t for t in self.frame(policy["source"])["own"] if t["term"] == word]
                if len(candidates) != 1 or any(t["term"] == word for t in frame["inherited"]):
                    raise ValueError("The supplied PG12 source occurrence is absent or duplicated")
                term = candidates[0]
                frame["inherited"].append({**deepcopy(term), "uid": policy["id"] + ":" + term["uid"],
                    "kind": "anuvrtti", "status": "COMMENTARY_SUPPLIED", "policy": policy["id"],
                    "evidence": deepcopy(policy["evidence"])})
            frame["decisions"].append({"policy": policy["id"], "action": "supply"})
