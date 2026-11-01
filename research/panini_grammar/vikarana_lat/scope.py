"""PG5 commentary overlay; the pinned PG4 scope parser is unchanged."""
from copy import deepcopy

from research.panini_grammar.scoped_derivations.scope import ScopeIndex


class ReviewedScope(ScopeIndex):
    def __init__(self, records, policies):
        super().__init__(records)
        for policy in policies:
            frame = self.views[policy["target"]]
            matches = [edge for edge in frame["inherited"]
                       if edge["source"] == policy["source"]
                       and edge["term"] == policy["raw_term"]
                       and edge["kind"] == policy["kind"]]
            if len(matches) != 1:
                raise ValueError("Commentary policy no longer matches its source edge")
            edge = matches[0]
            frame["excluded"].append({**deepcopy(edge), "term": policy["excluded_term"],
                                      "status": "EXCLUDED_COMPONENT",
                                      "evidence": deepcopy(policy["evidence"])})
            edge.update(term=policy["retained_term"], status="COMMENTARY_SPLIT",
                        policy=policy["id"], evidence=deepcopy(policy["evidence"]))
            frame["decisions"].append({"uid": edge["uid"], "policy": policy["id"],
                                       "action": "split_anuvrtti"})
