"""Run one licensed PG13 causative cell or its nine-cell P paradigm."""
import argparse
import json
from pathlib import Path

from research.panini_grammar.causative_present.grammar import Grammar, CausativeRequest


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-root", required=True, type=Path)
    p.add_argument("--lexical-id", required=True)
    p.add_argument("--sense", required=True)
    p.add_argument("--pada", default="P", choices=["P", "A"])
    p.add_argument("--pada-licensed", action="store_true")
    p.add_argument("--causative-licensed", action="store_true")
    p.add_argument("--person", default="prathama", choices=["prathama", "madhyama", "uttama"])
    p.add_argument("--number", default="eka", choices=["eka", "dvi", "bahu"])
    p.add_argument("--all-forms", action="store_true")
    p.add_argument("--trace", action="store_true")
    a = p.parse_args()
    read = lambda f: json.loads((a.source_root / f).read_text(encoding="utf-8"))
    g = Grammar(read("sutraani/data.txt")["data"], read("dhatu/data.txt")["data"])
    slots = [(x, y) for x in ["prathama", "madhyama", "uttama"] for y in ["eka", "dvi", "bahu"]] if a.all_forms else [(a.person, a.number)]
    out = []
    for person, number in slots:
        r = CausativeRequest(a.lexical_id, a.sense, a.pada, person, number, a.pada_licensed,
                             causative_licensed=a.causative_licensed)
        v = g.derive(r)
        out.append(v if a.trace else {"person": person, "number": number, **{k: v[k] for k in ["status", "forms", "reason"] if k in v}})
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return int(any(x["status"] == "UNRESOLVED" for x in out))


if __name__ == "__main__":
    raise SystemExit(main())
