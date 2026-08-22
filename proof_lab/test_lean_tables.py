from __future__ import annotations

import re
import unittest
from pathlib import Path

from proof_lab.paninian_seam_calculus import GAM
from proof_lab.seam_compensated_confluence_verdict import explore, step, word_rules

LEAN = Path(__file__).resolve().parents[1] / "lean" / "CommutatorSupport.lean"


class LeanTablesPinnedToRealization(unittest.TestCase):
    def test_tables_match_python_realization(self) -> None:
        rules = word_rules(True)
        g = explore(GAM, rules)
        states = sorted(g["states"], key=repr)
        idx = {W: i for i, W in enumerate(states)}
        src = LEAN.read_text(encoding="utf-8")
        for sid, fn in rules:
            name = "r_" + sid.replace(".", "_")
            tab = [idx[step((sid, fn), W)] if step((sid, fn), W) is not None else idx[W] for W in states]
            m = re.search(rf"def {name}_tab : List \(Fin 16\) := \[(.*?)\]", src)
            self.assertIsNotNone(m, sid)
            self.assertEqual([int(x) for x in m.group(1).split(",")], tab, sid)


if __name__ == "__main__":
    unittest.main()
