# Seam-Compensated Confluence as a Verdict

Source hint: Vedic repo `01_DERIVATIONS/Seam_Compensated_Confluence_Theorem.tex`
(A1 termination; A2 every critical pair precedence-resolved / Bindu-resolved /
seam-compensated joinable; A3 winding preserved mod ledger; A4 Lopa erases
surface markers only after seam events are recorded; proof via a "compensated
Newman lemma"). Newman is **not** imported. On a finite reachable carrier the
statement is decidable: enumerate, classify every local divergence, compare
normal forms modulo ledger. Built from the ladder audit's corrected law
(ambiguity ⊆ ∪ supp — priority needed *only* where a residue is nonzero).

## Definitions (executable)
- state W = (recognized string, memory ledger) — theorum/58 carrier
- W₁ ~ W₂ : recognized strings and ledgers equal (ledger subgroup L = 0)
- residue of (rᵢ,rⱼ) at W : rᵢrⱼW vs rⱼrᵢW (order-0 analogue of 57's first-visible jet)
- critical pair : both applicable, residue ≠ 0 → `PRIORITY_RESOLVED` (strict 1.4.2 winner) / `LEDGER_ABSORBED` (branches rejoin mod ~) / `OPEN`
- **verdict** : `CONFLUENT_MOD_LEDGER` ⟺ terminating ∧ no OPEN pair on the reachable set

## T1 Word carrier — A4 is the flip point
gam+śap+tip and nī+śap+tip under **free** application of the 58 pipeline:
- memory carried: unique NF mod ledger (`gacchati`, `nayati`) and **zero critical pairs** — every rule pair commutes at every reachable state (16 states). Memory makes this grammar abelian on the word.
- memory erased at lopa: pair (1.3.9, 7.3.77) is **OPEN**; 4 ledger-distinct normal forms, 2 recognized strings {gamati, gacchati}.

*Build notes:* the certificate refused two draft claims — "all pairs LEDGER_ABSORBED" (there are none) and "two normal forms without memory" (four; 3.4.113 also becomes order-dependent).

## T2 Sandhi carrier (58 T2 re-run through the verdict engine)
Critical pairs only (6.1.77, 6.1.101) on {i+i, i+ī, u+u, u+ū}; `PRIORITY_RESOLVED` under 1.4.2 (all 100 junctions confluent); `OPEN` without it (exactly those four not confluent). Containment ambiguity ⊆ support holds.

## T3 Containment is the law
Audit toy (r1:a→b, r2:a→c, r3:b→d, r4:c→d): nonzero residue at `a`, classified `LEDGER_ABSORBED`, verdict confluent — equality of ambiguity and support fails while the verdict theorem holds. Planted non-rejoining pair → `NOT_CONFLUENT` with witness (state, pair, class).

## T4 A1 is checked, not assumed
Reachable graph cycle-checked; planted a↔b refused `NON_TERMINATING`.

## Certificate
```text
python proof_lab/seam_compensated_confluence_verdict.py
python -m unittest proof_lab.test_seam_compensated_confluence_verdict -v
```
`PASS_SEAM_COMPENSATED_CONFLUENCE_VERDICT_CANDIDATE`, SHA-256
`5112f60ac5bfd85d4427d46d7b618c9d938a30f81ba1e8b7838e4da878c6fec8`.

## Claim boundary
```text
VERDICT THEOREM ON FINITE REACHABLE CARRIERS (enumeration, no Newman)      PROVED
WORD CARRIER: MEMORY ⇒ ZERO CRITICAL PAIRS; ERASED ⇒ OPEN (1.3.9, 7.3.77)   PROVED
SANDHI: PRIORITY_RESOLVED UNDER 1.4.2, OPEN WITHOUT; ambiguity ⊆ support    PROVED
CONTAINMENT ≠ EQUALITY (toy); OPEN PAIR AND CYCLE REFUSED WITH WITNESS      PROVED
VEDIC NOTE'S GENERAL (INFINITE) STATEMENT / COMPENSATED NEWMAN LEMMA        NOT CLAIMED
BINDU-RESOLUTION AS THIRD RESOLVER; LEDGER SUBGROUP L ≠ 0                   NOT PRESENT
RH, YM                                                                      UNTOUCHED
```
