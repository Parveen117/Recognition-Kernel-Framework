# Rewrite Rules as Operators on the C_Σ Free Module (theorum/60's residue is a commutator)

Carrier: the free C_Σ-module spanned by the reachable states of a finite
rewrite system (theorum/60 carriers). A rule ρ is the exact 0/1 matrix
`R_ρ e_W = e_{ρ(W)}` if applicable, `e_W` otherwise (60's `step` semantics).
Verdicts: exact entries, column supports, cut-tail mass M_Σ. Nothing Hilbert.

## T1 Faithful realization
`(R_i R_j) e_W = e_{r_i r_j W}` for all reachable W, all pairs; sparse product
cross-checked against theorum/50's dense `star`.

## T2 Commutator support theorem
`colsupp [R_i,R_j] = {W : r_i r_j W ≠ r_j r_i W}` exactly, and
`M_Σ([R_i,R_j]) = 2·#(such W)` — the native mass of the commutator counts
order-dependence (sandhi carrier 167 states, word carriers 16/20 states, all
pairs). On the sandhi carrier the only nonzero commutator is [6.1.77, 6.1.101].

## T3 Conflict vs enabling — a nonzero commutator is not always a conflict
The commutator support splits exactly into **conflicts** (both rules
applicable) and **enabling dependencies** (one rule applicable only after the
other). Word carrier with memory: conflicts = ∅ (theorum/60's zero critical
pairs), enabling = {[7.3.77, 6.1.73], [6.1.73, 8.4.40]} (chaḥ enables tuk,
tuk enables ścutva). Without memory `[R_lopa, R_chaḥ] ≠ 0` on the OPEN states.
*Build note:* the draft claimed "all commutators zero with memory"; the
certificate refused it and taught the split.

## T4 theorum/57 binding
With anti-self-dagger parts `D_i = R_i − R_i†`, the Cayley loop residue on the
realized carrier has `Γ ⊙_S h² = [D_lopa, D_chaḥ]` (57 T1 re-run). Probed,
not assumed: on the sandhi carrier `[D_i,D_j]=0 ⟺ [R_i,R_j]=0` held for every
pair (data recorded; not claimed as a law — `[R−R†,S−S†]` contains `[R,S†]`).

## T5 Priority normal-form operator
On the sandhi carrier `N = (P_max)^k` stabilizes, `N² = N`, and the image of
N is exactly the set of normal forms — confluence under 1.4.2 is N being a
projector onto normal forms.

## Certificate
```text
python proof_lab/rewrite_rules_as_cut_module_operators.py
python -m unittest proof_lab.test_rewrite_rules_as_cut_module_operators -v
```
`PASS_REWRITE_RULES_AS_CUT_MODULE_OPERATORS_CANDIDATE`, SHA-256 `9a94b881415c5db9a9b1f47980bff829550d198bbd670336bcf353941280241f`.

## Claim boundary
```text
FAITHFUL 0/1 REALIZATION ON THE C_Σ FREE MODULE                          PROVED
colsupp[R_i,R_j] = ORDER-DEPENDENCE SET; M_Σ = 2·COUNT (all pairs)        PROVED
CONFLICT / ENABLING SPLIT; MEMORY ⇒ NO CONFLICTS                         PROVED
57 BINDING Γ ⊙ h² = [D_lopa, D_chaḥ] ON THE REALIZED CARRIER              PROVED
PRIORITY NF OPERATOR IDEMPOTENT, IMAGE = NORMAL FORMS (sandhi)           PROVED
[D_i,D_j]=0 ⟺ [R_i,R_j]=0 AS A LAW                                       NOT CLAIMED (held on this carrier)
INFINITE CARRIERS; HILBERT STRUCTURE ON THE MODULE                       NOT CLAIMED
RH, YM                                                                   UNTOUCHED
```
