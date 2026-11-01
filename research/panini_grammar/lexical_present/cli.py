"""Inspect PG11's owned lexical present derivations and optional endings."""
import argparse
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.lexical_present.grammar import Grammar, Request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root",type=Path,required=True)
    parser.add_argument("--lexical-id",required=True)
    parser.add_argument("--sense",required=True)
    parser.add_argument("--pada",choices=["P","A"],required=True)
    parser.add_argument("--pada-licensed",action="store_true")
    parser.add_argument("--person",choices=["prathama","madhyama","uttama"],default="prathama")
    parser.add_argument("--number",choices=["eka","dvi","bahu"],default="eka")
    parser.add_argument("--all-forms",action="store_true")
    parser.add_argument("--trace",action="store_true")
    args=parser.parse_args()
    data=lambda name:json.loads((args.source_root/name).read_text(encoding="utf-8"))["data"]
    grammar=Grammar(data("sutraani/data.txt"),data("dhatu/data.txt"))
    req=Request(args.lexical_id,args.sense,args.pada,args.person,args.number,args.pada_licensed)
    requests=[req] if not args.all_forms else [replace(req,person=p,number=n)
        for p in grammar.review["ending_order"]["persons"] for n in grammar.review["ending_order"]["numbers"]]
    rows=[]
    for item in requests:
        value=grammar.derive(item)
        if not args.trace:
            value={"person":item.person,"number":item.number,"status":value["status"],
                   **({"forms":value["forms"]} if "forms" in value else {"reason":value["reason"]})}
        rows.append(value)
    print(json.dumps(rows,ensure_ascii=False,indent=2))
    return int(any(not r["status"].startswith("COMPLETE_IN_REVIEWED_") for r in rows))


if __name__=="__main__":raise SystemExit(main())
