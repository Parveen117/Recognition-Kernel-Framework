# Selective Release of the Content Tail (theorum/75)

Owner's source: RV 7.59.12 read as an operator law (no canvas exists;
the text itself is the source, per the standing rule; reading confirmed
by the owner). NATIVE CARRIER ONLY, per the owner's instruction: rational
cut-squares (T50 E_Σ shape), cut-tail mass, seam counts as theorum/53
elimination sign patterns, the cut-square inequality. No inner-product
axioms, no eigenvectors, no completion: the infinite step goes ONLY
through theorum/28's proved machinery (Def 3.1, §4, Thm 5.1, §8, §9),
whose hypotheses this certificate delivers. The rational moment table is
exact; its Φ_Σ identification is the one declared shadow (RH T01-E5C/E6).

## Dictionary (candidate names, per the owner's rule)
bandhana = the truncation bond (content-≤1 column ↔ higher-content tail);
urvārukam iva = ripeness = the §9 outward certificate, unripe ⇒ refusal;
mṛtyu = the decaying memory channel, contents ≥ 3/2; amṛta = exact
retention (seam count, recognized floor); tryambaka = triple witness
(mass, energy, count per release step); sugandhiṁ puṣṭi-vardhanam =
the stationary growing floor θ_sil.

## Certified (instance: the two-rail one-column recognition transfer,
Wilson face ladder, declared rung kernel; levels Λ = 1, 3/2, 2; grid
κ = 1/8, 1/4, 1/2)

- **T1 Ladder law at every content (proved).** Termwise on the positive
  series: term_k(ν+1) = (κ/2)/(k+ν+1)·term_k(ν) ≤ (κ/2)/(ν+1)·term_k(ν)
  since k ≥ 0 — so f_{c+½}/f_c ≤ κ/(2(2c+2)) for EVERY c. Checked on
  enclosures for c ≤ 3/2 at every κ; the general step is one line of
  exact fraction algebra, recorded. The §4 tail is therefore a declared
  geometric form with a **proved** ratio.
- **T2 Stationarity (ρ_rec = 0 exactly).** Refinement only borders the
  pencil: every low-block entry, the silence row, and θ_sil are
  unchanged entry-by-entry across Λ. A planted face perturbation breaks
  it (control).
- **T3 Ripeness and release.** Seam-count **integer equality**
  k(Λ, μ) = k(1, μ) at two thresholds per κ, at Λ = 3/2 and 2 — the
  released blocks carry no positive weight (Haynsworth additivity
  realized by the elimination). Triple witness per step: border
  cut-tail mass and border energy within printed budgets, plus the
  count equality. Contraction transfers: σ_sil drift 1→2 is 8.6e-8 /
  1.4e-6 / 2.3e-5 (within one lopa rate, certified), β_sil < 1 at every
  level. The UNRIPE refusal path exists and is exercised in the code.
- **T4 Outward certificate for the full column.** u = β_sil(Λ=2),
  e = declared geometric tail with the T1-proved ratio q = κ/12:
  **u + e < 1 at every grid κ** (0.00259 / 0.01051 / 0.04357).

## Claim boundary
```text
LADDER LAW f_{c+1/2}/f_c <= kappa/(2(2c+2)), ALL c              PROVED
STATIONARITY OF THE LOW BLOCK, SILENCE ROW, FLOOR               PROVED (exact)
SEAM-COUNT RETENTION AT Λ = 3/2, 2 (INTEGER EQUALITY)           PROVED (instance; native grading)
CONTRACTION TRANSFER, β_sil < 1 AT EVERY INSTANTIATED LEVEL     PROVED (instance)
OUTWARD CERTIFICATE u + e < 1 FOR THE FULL COLUMN               PROVED, WITH THE LEVELS > 2
                                                                ENTERING ONLY VIA §4's DECLARED
                                                                TAIL (T1-justified ratio; the
                                                                Gram-uniformity of levels > 2 is
                                                                the recorded DECLARED component)
OPERATOR UPPER BOUND FOR THE CHAIN GAP (E4D-C)                  OPEN (this is the tool, not the wall)
```

## Standing correction — RESOLVED (same day)
The owner's provenance challenge found the content grading built from the
classical Laplacian's nullspace (load-bearing for B); T3/T4 were demoted
to ANCHORED. **Resolved by the native regrading:** the grading is now
DEFINED by the character ladder (`chi_of_u`, the native three-term
recurrence) composed with convolution (rational moments) —
`rail_cinv_native`. Its projector laws (reassembly, idempotence,
cross-orthogonality) are **certified on the carrier as exact rational
identities** (`certify_native_grading`), cited from nothing. The
Laplacian construction is retained ONLY as an independent cross-check
control and reproduces **identical rationals** on every monomial. Every
number in this certificate is unchanged. T3/T4 restored to PROVED.
See `AUDIT_74_75.md`.

## Build notes
The draft asserted ∫x₀⁴x₁⁴ = 3/128; the moment table refused it (3/640).
The tryambaka mass budget is coarse and printed, not hidden.

## Certificate
```text
python proof_lab/selective_release.py
python -m unittest proof_lab.test_selective_release -v
```
