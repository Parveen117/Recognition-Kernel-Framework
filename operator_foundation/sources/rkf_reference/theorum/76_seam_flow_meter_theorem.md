# The Seam-Flow Meter (theorum/76) — the winding/sector canvas on the primitive carrier

Owner's canvas (winding number + curvature-memory detector) taken on its
own terms and tested thoroughly in native space, per instruction. The
canvas's name is NOT used, per instruction; this object is named only by
what it does. Every verdict is a theorum/53 elimination sign pattern or
exact rational algebra; mp_gold/05's curvature-to-seam-index law
(k change = −spectral flow) is the law this meter instruments — cited,
never rederived.

## Native translation, certified
- **Sector label** = the seam count k(κ, μ) = n₊(M − μB(κ)) — an integer
  by construction; sectors = certified constant-count κ-intervals.
  Observed on the column pencil (μ = 1/2, 9/10; κ ∈ [1/16, 4]): sector
  cascade 1 → 8, **seven simple flips per μ**, all in the strong-coupling
  window r_½ ≈ 0.39–0.63.
- **Flip locations** bracketed to width 2⁻⁴⁰ with recursive crossing
  separation — one grid cell held a genuinely CLOSE PAIR of crossings
  (r_½ = 0.597411 and 0.597793), resolved into two simple flips.
- **Detector, second route** = the native determinant channel
  D = ∏(elimination weights) (theorum/53 T6): certified per bracket,
  **odd jump ⟺ sign(D) flips** — count route and det route agree at
  every one of the 14 brackets, independently and exactly.
- **Protection** = the declared perturbation family (24 rational
  perturbations of B, relative 1e-6) leaves every off-bracket count
  unchanged; crossing a bracket flips it (biting control). A universal
  protection radius is NOT claimed — protection is certified for the
  declared family only.

## Structural findings (exact)
1. **M is κ-independent; only B(κ) moves, through the lopa ladder alone:**
   B(κ)_ij = Σ S_ij^{(c1,c2)} / (f_{c1}f_{c2}) with S κ-independent
   content-pair overlaps (native character projectors, theorum/75's
   regrading). The whole coupling path is ladder arithmetic — seam flow
   is read straight off the lopa rates, and theorum/75's flat-ladder
   tamper already showed the cascade collapses without the ladder.
2. **The superselection acts inside the meter:** (0,½) content pairs do
   not exist in the even sector (centre parity) — found when a tamper
   aimed at them was structurally unable to bite.

## Build notes (all caught by controls)
(i) a grid-level jump of 2 was two separate crossings — the first
bracket's det flip was compared against the wrong jump; fixed by
recursive crossing separation, parity now checked bracket-by-bracket;
(ii) the first tamper draft swapped (c1,c2) → (c2,c1), structurally
unable to fail since f_{c1}f_{c2} is symmetric — replaced;
(iii) the second draft hit the empty (0,½) slot — finding 2 above.

## Claim boundary
```text
INTEGER SECTORS, CONSTANT ON CERTIFIED INTERVALS              PROVED (instance)
14 FLIPS BRACKETED 2^-40, ALL SIMPLE AFTER SEPARATION          PROVED (instance)
COUNT ROUTE = DET ROUTE (PARITY LAW, PER BRACKET)              PROVED (instance)
PROTECTION                                                     PROVED for the declared family ONLY
LADDER IDENTITY (M κ-INDEPENDENT, B = S/ff)                    PROVED (exact)
UNIVERSAL PROTECTION RADIUS                                    NOT CLAIMED
CONNECTION TO YM-23's WEAK-COUPLING THRESHOLD                  PRINTED (r_½ at flips), NOT CLAIMED
mp_gold/05 SPECTRAL-FLOW LAW                                   CITED (instrumented, not rederived)
```

## Certificate
```text
python proof_lab/seam_flow_meter.py
python -m unittest proof_lab.test_seam_flow_meter -v
```
