# Lopa-Ledger Contraction (theorum/74) — contraction to silence with the 1.1.62 ledger

Owner's direction: build the YM upper-bound tools with the Pāṇini seam
calculus and the mantra operators. Canvas definitions honored (standing
rule): **silence = lopa**, the 1.3.9 zero-operator, ker of the odd
generator (theorum/62); **ledger = 1.1.62** pratyayalope pratyayalakṣaṇam
(theorum/58); **vibration = the Euler circular flow** on the odd
generator (theorum/62 T2, F00E). Finite control instance: the one-column
space transfer of the two-rail chain fabric (Publications YM-37, pin
`ad598ee5…`, distilled self-contained; even conjugation-invariant sector,
dim 8; declared rationals printed in the certificate). Every verdict is a
theorum/53 elimination sign pattern, the cut-square inequality, or exact
algebra.

## Certified

- **T1 Silence factorization (exact).** τ = C ∘ M_K with C exactly
  diagonal on the content grading; ladder f₀ > f_½ > f₁ strict — the
  per-content **lopa rates**. The silence channel span{1} is structural:
  defined on every carrier, any content cutoff, no eigenvectors, no
  iteration. Planted content-mixing C′ detected.
- **T2 Ledger 1.1.62 (exact).** Elision is not erasure: the silence-row
  matrix elements decompose exactly into per-λ-channel fusion
  contributions — every content of the state is read by the verdict
  (adarśanam with lakṣaṇam). Killing the λ_½ channel changes the row.
- **T3 Contraction to silence (the tool).** With w = the silence vector
  (not a Krylov iterate): defect exactly B-orthogonal; restricted
  doubled ceiling σ_sil by ONE sign check; outward certificate
  **β_sil < 1** (theorum/28 §9) with ball invariance and declared
  geometric Smriti tail; the full uniformity assembly
  `|ρ(m,p) − ρ_c| ≤ A(β^{j−p₀}+β^{j_c−p₀})` verified on exact rows for
  all m, interior p. **Measured:** β_sil/L_Krylov ≈ 1.75–1.85 only
  (σ_sil numerically equal to the Krylov ceiling) — the draft expected
  ~20× loss; the arithmetic said otherwise.
- **T4 Vibration tie.** The exchange part conserves cut-square energy
  (theorum/51); contraction is the lopa ladder silencing what exchange
  moves out. Certified one-sided law: **β_sil < r_½ = f_½/f₀ strictly**
  at every grid κ (β/r = 0.082, 0.165, 0.337). *Build note:* the
  draft's two-sided window [r/4, 4r] was refused from below — β is
  better than the window; only the one-sided law is claimed.

## Candidate names (owner's rule: names after certification)
"Silence channel" = span{1} (lopa reading); "lopa rates" = f_c/f₀;
"vibration exchange" = the theorum/51 unitary part. CANDIDATE until the
owner's audit.

## Certificate
```text
python proof_lab/lopa_ledger_contraction.py
python -m unittest proof_lab.test_lopa_ledger_contraction -v
```

## Claim boundary
```text
SILENCE FACTORIZATION, STRICT LOPA LADDER                     PROVED (instance, exact)
LEDGER 1.1.62 CHANNEL DECOMPOSITION                           PROVED (instance, exact)
STRUCTURAL CONTRACTION beta_sil < 1, OUTWARD CERTIFICATE      PROVED (instance)
UNIFORMITY WITH SILENCE DEFLATION, ALL m, INTERIOR p          PROVED (instance)
beta_sil < r_half (ONE-SIDED)                                 PROVED (grid); two-sided window REFUSED
TRANSFER TO UNTRUNCATED COLUMN (INFINITE CONTENT)             NOT CLAIMED — theorum/75 (content-tail budgets)
OPERATOR UPPER BOUND FOR THE CHAIN GAP (E4D-C)                OPEN
```
