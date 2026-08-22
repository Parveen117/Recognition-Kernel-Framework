from __future__ import annotations

"""Exact certificate (theorum/60): SEAM-COMPENSATED CONFLUENCE AS A VERDICT.

Source hint: Vedic repo 01_DERIVATIONS/Seam_Compensated_Confluence_Theorem.tex
(assumptions A1 termination, A2 every critical pair precedence-resolved /
Bindu-resolved / seam-compensated joinable, A3 lawful corrections preserve
winding mod ledger, A4 Lopa erases only after seam events are recorded; proof
by a "compensated Newman lemma").  Here the theorem is NOT proved by Newman's
induction (no classical import).  On a FINITE reachable carrier the statement
is a decidable verdict: enumerate, classify every local divergence, and check
the normal-form set modulo ledger.  Both directions are computed on instances.

Consumes: theorum/58 carrier (recognized/memory channels, canonical rules),
theorum/58 T2 as downgraded by the ladder audit (ambiguity ⊆ ∪ supp -- priority
is needed ONLY where a residue is nonzero), theorum/57 typing of "residue".

Definitions (executable):
  state        W = (recognized string, memory ledger)   [58]
  ledger-equiv W1 ~ W2  iff recognized strings agree AND ledgers agree after
               declared erasure (A4: the it-marker ledger is the record of
               seam events; equality of ledgers = equality mod L with L = 0)
  residue of a pair (r_i, r_j) at W:  r_i r_j W  vs  r_j r_i W  (order-0
               residue, the finite analogue of 57's first-visible jet)
  critical pair at W: both applicable and residue nonzero
  classification of a critical pair:
     PRIORITY_RESOLVED  a strict 1.4.2 winner exists (tie-free)
     LEDGER_ABSORBED    the two branches rejoin modulo ~ (joinable)
     OPEN               neither
  verdict: CONFLUENT_MOD_LEDGER iff no OPEN critical pair on the reachable set
           (and the system terminates on it).

Facts certified:
 T1  VERDICT THEOREM (both directions, on instances): the reachable graph of
     gam+Sap+tip and nI+Sap+tip under FREE application of the 58 pipeline
     (lopa included, memory carried) has a unique normal form modulo ledger
     and NO critical pair at all -- every rule pair commutes at every
     reachable state (memory makes the grammar abelian on this word).  With
     memory erased at lopa the pair (1.3.9 lopa, 7.3.77 chah) becomes OPEN;
     four normal forms mod exact ledger, two recognized strings
     {gamati, gacchati}: the verdict flips exactly at A4.
 T2  Sandhi junction carrier (58 T2): the only critical pairs are
     (6.1.77, 6.1.101) on {i+i, i+I, u+u, u+U}; under 1.4.2 they are
     PRIORITY_RESOLVED; with 1.4.2 switched off they are OPEN -> verdict
     NOT_CONFLUENT; containment ambiguity ⊆ ∪ supp re-confirmed on this run.
 T3  CONTAINMENT IS THE LAW, EQUALITY IS NOT: the audit's toy (r1:a->b,
     r2:a->c, r3:b->d, r4:c->d) has a nonzero residue at 'a' classified
     LEDGER_ABSORBED (rejoins), verdict CONFLUENT -- equality of ambiguity
     and support fails while the verdict theorem holds.  Conversely a planted
     system with an OPEN pair is refused.
 T4  A1 termination is CHECKED, not assumed: every reduction from every
     reachable state stops within the exploration bound; a planted
     non-terminating rule (a<->b) is refused with NON_TERMINATING.
 T5  Verdict is fail-closed: OPEN pairs are returned as witnesses
     (state, rule pair, both branches' normal forms).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_seam_calculus import (
    GAM,
    NI,
    PIPELINE,
    SANDHI,
    VOWELS,
    Word,
    it_lopa,
    recognized,
    sutra_key,
)

State = Any
Rule = tuple[str, Callable[[State], State | None]]  # returns new state or None if inapplicable


def step(r: Rule, W: State) -> State | None:
    out = r[1](W)
    return None if out is None or out == W else out


def explore(W0: State, rules: list[Rule], bound: int = 40) -> dict[str, Any]:
    """Reachable graph under free application; NON_TERMINATING if any path exceeds bound."""
    seen = {W0: 0}
    frontier = [W0]
    edges: dict[State, list[tuple[str, State]]] = {}
    while frontier:
        W = frontier.pop()
        edges[W] = []
        for r in rules:
            W2 = step(r, W)
            if W2 is not None:
                edges[W].append((r[0], W2))
                if W2 not in seen:
                    seen[W2] = seen[W] + 1
                    if seen[W2] > bound:
                        return {"terminating": False, "states": seen, "edges": edges}
                    frontier.append(W2)
    # cycle check (a terminating system has an acyclic reachable graph)
    color: dict[State, int] = {}

    def dfs(u) -> bool:
        color[u] = 1
        for _, v in edges.get(u, []):
            if color.get(v, 0) == 1 or (color.get(v, 0) == 0 and dfs(v)):
                return True
        color[u] = 2
        return False

    cyclic = any(color.get(u, 0) == 0 and dfs(u) for u in list(seen))
    return {"terminating": not cyclic, "states": seen, "edges": edges}


def normal_forms(W0: State, rules: list[Rule], graph: dict[str, Any]) -> set[State]:
    return {W for W in graph["states"] if not graph["edges"].get(W)}


def classify_pairs(rules: list[Rule], graph: dict[str, Any], equiv: Callable[[State, State], bool], priority: bool) -> list[dict[str, Any]]:
    pairs = []
    for W in graph["states"]:
        applicable = [(r, step(r, W)) for r in rules if step(r, W) is not None]
        for i in range(len(applicable)):
            for j in range(i + 1, len(applicable)):
                (ri, Wi), (rj, Wj) = applicable[i], applicable[j]
                # order-0 residue: r_i r_j W vs r_j r_i W (each may be inapplicable after the other)
                a = step(ri, Wj)
                b = step(rj, Wi)
                a = Wj if a is None else a
                b = Wi if b is None else b
                if a == b:
                    continue  # commuting: no residue
                if priority and sutra_key(ri[0]) != sutra_key(rj[0]):
                    cls = "PRIORITY_RESOLVED"
                else:
                    nfi = {nf for nf in normal_forms(Wi, rules, explore(Wi, rules))}
                    nfj = {nf for nf in normal_forms(Wj, rules, explore(Wj, rules))}
                    joinable = all(any(equiv(x, y) for y in nfj) for x in nfi) and all(any(equiv(x, y) for x in nfi) for y in nfj)
                    cls = "LEDGER_ABSORBED" if joinable else "OPEN"
                pairs.append({"state": repr_state(W), "pair": (ri[0], rj[0]), "class": cls})
    return pairs


def repr_state(W: State) -> str:
    if isinstance(W, tuple) and W and isinstance(W[0], tuple) and len(W[0]) == 2 and isinstance(W[0][1], frozenset):
        return recognized(W) + " | " + ";".join(",".join(sorted(f)) for _, f in W)
    return "".join(W) if isinstance(W, tuple) else str(W)


def verdict(W0: State, rules: list[Rule], equiv: Callable[[State, State], bool], priority: bool) -> dict[str, Any]:
    g = explore(W0, rules)
    if not g["terminating"]:
        return {"verdict": "NON_TERMINATING", "pairs": [], "normal_forms": []}
    if priority:
        # under 1.4.2 only the strict max rule fires at each state: restrict edges
        rules_p = [("PRIORITY", lambda W: _priority_step(W, rules))]
        g = explore(W0, rules_p)
    nfs = normal_forms(W0, rules_p if priority else rules, g)
    classes = {nf: None for nf in nfs}
    reps: list[State] = []
    for nf in nfs:
        if not any(equiv(nf, r) for r in reps):
            reps.append(nf)
    pairs = classify_pairs(rules, explore(W0, rules), equiv, priority)
    open_pairs = [p for p in pairs if p["class"] == "OPEN"]
    v = "CONFLUENT_MOD_LEDGER" if len(reps) == 1 and not open_pairs else "NOT_CONFLUENT"
    return {"verdict": v, "pairs": pairs, "open": open_pairs, "normal_forms_mod_ledger": [repr_state(r) for r in reps], "reachable": len(g["states"])}


def _priority_step(W: State, rules: list[Rule]) -> State | None:
    applicable = [r for r in rules if step(r, W) is not None]
    if not applicable:
        return None
    top = max(sutra_key(r[0]) for r in applicable)
    winners = [r for r in applicable if sutra_key(r[0]) == top]
    assert len(winners) == 1, "priority tie"
    return step(winners[0], W)


# ---------------------------------------------------------------- instances
def word_rules(carry_memory: bool) -> list[Rule]:
    return [("1.3.9", lambda W: it_lopa(W, carry_memory))] + [(s, f) for s, f in PIPELINE]


def word_equiv(W1: Word, W2: Word) -> bool:
    return W1 == W2  # recognized string and memory ledger both equal (L = 0)


def t1_word_carrier() -> dict[str, Any]:
    out = {}
    for name, W0 in (("gam", GAM), ("nI", NI)):
        v_mem = verdict(W0, word_rules(True), word_equiv, priority=False)
        v_nomem = verdict(W0, word_rules(False), word_equiv, priority=False)
        out[name] = {"with_memory": v_mem, "without_memory": v_nomem}
    gam_mem, gam_no = out["gam"]["with_memory"], out["gam"]["without_memory"]
    open_pair_is_lopa_chah = any(set(p["pair"]) == {"1.3.9", "7.3.77"} for p in gam_no["open"])
    checks = {
        "gam_with_memory_confluent_mod_ledger_unique_nf": gam_mem["verdict"] == "CONFLUENT_MOD_LEDGER" and gam_mem["normal_forms_mod_ledger"][0].startswith("gacchati"),
        # BUILD NOTE: first draft claimed "all critical pairs LEDGER_ABSORBED"; the certificate refused it --
        # with memory carried there are NO critical pairs at all: every rule pair commutes at every reachable state.
        "gam_with_memory_has_zero_critical_pairs_all_rules_commute": gam_mem["pairs"] == [] and gam_mem["reachable"] > 1,
        "nI_with_memory_confluent_nayati": out["nI"]["with_memory"]["verdict"] == "CONFLUENT_MOD_LEDGER" and out["nI"]["with_memory"]["normal_forms_mod_ledger"][0].startswith("nayati"),
        # BUILD NOTE: first draft expected exactly two normal forms without memory; there are FOUR mod exact ledger
        # (3.4.113 also becomes order-dependent) and exactly TWO recognized strings {gamati, gacchati}.
        "gam_without_memory_NOT_confluent_two_recognized_strings": gam_no["verdict"] == "NOT_CONFLUENT" and len({r.split(" | ")[0] for r in gam_no["normal_forms_mod_ledger"]}) == 2 and len(gam_no["normal_forms_mod_ledger"]) == 4,
        "verdict_flips_exactly_at_A4_open_pair_is_lopa_vs_chah": open_pair_is_lopa_chah,
    }
    return {"checks": checks, "gam_nfs_with_memory": gam_mem["normal_forms_mod_ledger"], "gam_nfs_without_memory": gam_no["normal_forms_mod_ledger"], "gam_pair_classes": sorted({p["class"] for p in gam_mem["pairs"]}), "reachable_gam": gam_mem["reachable"]}


def t2_sandhi_carrier() -> dict[str, Any]:
    rules = [(s, f) for s, f in SANDHI]
    eq = lambda a, b: a == b
    with_p = {j: verdict(j, rules, eq, priority=True) for j in ((x, y) for x in VOWELS for y in VOWELS)}
    no_p = {j: verdict(j, rules, eq, priority=False) for j in ((x, y) for x in VOWELS for y in VOWELS)}
    crit = {j for j, v in no_p.items() if v["pairs"]}
    ambiguous = {j for j, v in no_p.items() if v["verdict"] == "NOT_CONFLUENT"}
    checks = {
        "all_junctions_confluent_under_1_4_2": all(v["verdict"] == "CONFLUENT_MOD_LEDGER" for v in with_p.values()),
        "critical_pairs_only_6_1_77_vs_6_1_101_on_four_junctions": crit == {("i", "i"), ("i", "I"), ("u", "u"), ("u", "U")} and all(set(p["pair"]) == {"6.1.77", "6.1.101"} for j in crit for p in no_p[j]["pairs"]),
        "under_priority_those_pairs_PRIORITY_RESOLVED": all(p["class"] == "PRIORITY_RESOLVED" for j in crit for p in with_p[j]["pairs"]),
        "without_priority_OPEN_and_not_confluent": all(p["class"] == "OPEN" for j in crit for p in no_p[j]["pairs"]) and ambiguous == crit,
        "containment_ambiguity_subset_support": ambiguous <= crit,
    }
    return {"checks": checks}


def t3_containment_not_equality() -> dict[str, Any]:
    def mk(a, b):
        return (a, lambda w: (b,) if w == (a,) else None)
    toy = [("r1", mk("a", "b")[1]), ("r2", mk("a", "c")[1]), ("r3", mk("b", "d")[1]), ("r4", mk("c", "d")[1])]
    eq = lambda x, y: x == y
    v = verdict(("a",), toy, eq, priority=False)
    planted = toy[:3] + [("r4", lambda w: ("e",) if w == ("c",) else None)]
    vp = verdict(("a",), planted, eq, priority=False)
    checks = {
        "toy_nonzero_residue_but_LEDGER_ABSORBED_verdict_confluent": v["verdict"] == "CONFLUENT_MOD_LEDGER" and any(p["class"] == "LEDGER_ABSORBED" for p in v["pairs"]),
        "planted_open_pair_refused_with_witness": vp["verdict"] == "NOT_CONFLUENT" and vp["open"] and set(vp["open"][0]["pair"]) == {"r1", "r2"},
    }
    return {"checks": checks, "planted_witness": vp["open"]}


def t4_termination_checked() -> dict[str, Any]:
    loop_rules = [("r1", lambda w: ("b",) if w == ("a",) else None), ("r2", lambda w: ("a",) if w == ("b",) else None)]
    v = verdict(("a",), loop_rules, lambda x, y: x == y, priority=False)
    checks = {"planted_a_b_cycle_refused_NON_TERMINATING": v["verdict"] == "NON_TERMINATING"}
    return {"checks": checks}


def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_word_carrier": t1_word_carrier(),
        "t2_sandhi_carrier": t2_sandhi_carrier(),
        "t3_containment_not_equality": t3_containment_not_equality(),
        "t4_termination_checked": t4_termination_checked(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SEAM_COMPENSATED_CONFLUENCE_VERDICT_CANDIDATE" if all(checks.values()) else "FAIL_SEAM_COMPENSATED_CONFLUENCE_VERDICT_CANDIDATE"
    return {
        "schema": "rkf.seam_compensated_confluence_verdict_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "VERDICT THEOREM on finite reachable carriers: CONFLUENT_MOD_LEDGER iff terminating and no OPEN critical pair (every nonzero-residue pair PRIORITY_RESOLVED or LEDGER_ABSORBED); decided by enumeration, no Newman induction",
                "gam+Sap+tip and nI+Sap+tip under FREE application with memory: unique normal form mod ledger and ZERO critical pairs (all rule pairs commute); memory erased at lopa -> OPEN pair (1.3.9, 7.3.77), two recognized strings / four ledger-distinct normal forms: the Vedic note's A4 is exactly the flip point",
                "sandhi carrier: critical pairs only (6.1.77, 6.1.101) on four junctions; PRIORITY_RESOLVED under 1.4.2, OPEN without; ambiguity ⊆ support",
                "containment not equality: nonzero residue with rejoining branches is LEDGER_ABSORBED (confluent); planted OPEN pair refused with witness; planted cycle refused NON_TERMINATING",
            ],
            "NOT_claimed": [
                "the Vedic note's infinite/general statement (compensated Newman lemma) -- only finite reachable carriers are decided",
                "Bindu-resolution (phase selection) as a third resolver -- not present in these instances; ledger subgroup L is 0 here (exact ledger equality)",
                "coverage beyond the 58 rule set and the toy systems",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, default=list) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    body = canonical_bytes(payload)
    if args.output:
        args.output.write_bytes(body)
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
