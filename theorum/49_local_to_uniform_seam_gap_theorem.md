# Local-to-Uniform Seam Gap Theorem (product of cut-graded faces)

## 1. What was missing

The framework had a local cut calculus (theorum/41: every bounded generator
splits uniquely as `G = G_e + G_o` relative to its cut, with the exact flow
cut-square criterion (5.4)) and a finite-to-infinite bridge (theorum/28) whose
last hypothesis is an **outward seam margin** `u_n + e_n < 1`.  What it did
not have was a theorem turning **locality into uniformity**:

```text
every local piece (one face) is slightly bad  -- declared sup-weight W, mean f0
every local piece carries a smoothing          -- memory channel contracts by lambda
=>  the seam gap of the whole product does not depend on the number m of faces.
```

This capsule states and certifies that theorem in the framework's own
algebra.  No Perron–Frobenius, Dobrushin or transfer-operator result is
imported.  The only tools are the cut grading (theorum/41 (3.1)–(3.3)), the
exact cut-square criterion (theorum/41 (5.4)) and the outward certificate
rule (theorum/28 §9).

---

## 2. Native data

**Face.**  A face `i` is a finite carrier `H_i` with a cut `J_i = J_i^* = J_i^{-1}`,
recognized sheet `P_i = (I + J_i)/2` (rank one in every instance below),
memory sheet `Q_i = I − P_i`, and a transfer `L_i`.  The face's "badness" is
carried by two declared rationals, the sup-weight `W_i` and the recognized
mean `f0_i`; its smoothing by a declared contraction `λ_i`.  Write
`ρ_i = W_i λ_i / f0_i`.

**Hypotheses per face.**

```text
(H1)  seam compatibility     L_i P_i = f0_i P_i = P_i L_i
(H2)  memory contraction     || Q_i L_i Q_i || <= W_i λ_i = ρ_i f0_i,   ρ_i < 1
```

(H1) says the smoothing has already averaged the recognized channel to
exactly its mean, with no leakage in either direction.

### Lemma 2.1 (H1 is evenness)
(H1) holds iff `L_i` is `J_i`-even in the sense of theorum/41 (3.3)
(`J_i L_i J_i = L_i`) **and** `L_i P_i = f0_i P_i`.  Proof: evenness is
`P_i L_i Q_i = Q_i L_i P_i = 0` by (3.4)–(3.5); with the recognized value
fixed this is exactly (H1). ∎

(H2) is decided by theorum/41 (5.4): `(ρ_i f0_i)^2 Q_i − (Q_i L_i Q_i)^T(Q_i L_i Q_i) ≥ 0`,
verified by exact rational `LDL^T` inertia — no eigenvalue is approximated.

**Product.**  `H = ⊗ H_i`, `L = ⊗ L_i`, recognized-everywhere projector
`P = ⊗ P_i`, memory `Q = I − P`, global recognition cut `J_rec = 2P − I`.

### Lemma 2.2 (the tensor cut is not the recognition cut)
`⊗ J_i` is an involution whose `+` sheet is the span of the **even-parity**
words, which strictly contains `P` for `m ≥ 2`.  The `2^m` sheet projectors
`S_w = ⊗ (P_i or Q_i)` resolve the identity orthogonally, and `P = S_{+…+}`.
Certified (T1).  The recognition cut of a product is therefore `J_rec`, not
the tensor product of the local cuts.

---

## 3. The theorem

### Theorem 3.1 (local-to-uniform seam gap)
Let faces `1..m` satisfy (H1)–(H2) and put `ρ = max_i ρ_i < 1`,
`f0^m := ∏ f0_i`.  Then

```text
L P = f0^m P = P L            (L is J_rec-even with recognized value f0^m)
|| Q L Q || <= ρ · f0^m       (memory sheet contracts by ρ, for EVERY m)
```

so the normalized gap ratio `||Q L Q|| / f0^m ≤ ρ` is independent of `m`.

**Proof (sheet law).**  `L` is block-diagonal in the sheet resolution of
Lemma 2.2 because each `L_i` is block-diagonal in `P_i ⊕ Q_i` by (H1).  On
the sheet of a word with `k` minus signs the block is
`⊗ (f0_i P_i or Q_i L_i Q_i)`, whose norm is at most
`∏_{+} f0_i · ∏_{−} ρ_i f0_i ≤ ρ^k f0^m` by (H2).  The word `+…+` is `P`
with value exactly `f0^m`; every other word has `k ≥ 1`, hence norm
`≤ ρ f0^m`.  The memory sheet `Q` is the orthogonal sum of those words. ∎

The certificate does **not** assemble the bound from sheets: T2 verifies
`||Q L Q|| ≤ ρ f0^m` on the full product matrix (dimension up to 72) by one
exact cut-square decision; T3 then verifies the sheet law word by word and
exhibits attainment on a diagonal instance.

### Corollary 3.2 (theorum/28 §9 delivered uniformly)
Normalize `L̃ = L / f0^m`.  Then the recognized floor is exactly `1`, the
outward top of the memory sheet is `u = ρ`, the finite-`m` refinement error
is `e = 0`, and `u + e = ρ < 1` is a lawful outward certificate — the same
number for every `m`.  Certified (T5) for `m = 1..4`.

### Proposition 3.3 (interacting faces)
If a coupling `E` lives on the memory sheet only (`P E = E P = 0`) with
certified `||E|| ≤ β f0^m`, then the recognized value is untouched and
`||Q (L+E) Q|| ≤ (ρ + β) f0^m`.  Hence `ρ + β < 1` suffices.  Certified (T6)
with a nearest-neighbour coupling at `m = 3`; a coupling that touches `P`
moves the recognized value (control).  **The `m`-uniformity of `β` is a
declared hypothesis for interacting faces; it is not derived here.**

---

## 4. Controls (T7)

```text
C1  a face with W λ >= f0 (ρ >= 1) is never repaired by adding faces:
    no ρ < 1 certifies the memory sheet at m = 1..4;
C2  grading against the tensor cut ⊗J_i: its + sheet is NOT an exact
    recognized sheet (P_par L P_par != f0^m P_par) -- Lemma 2.2 is load-bearing;
C3  a face violating co-invariance (P L Q != 0) makes the product non-even
    and creates a nonzero memory-to-recognized block -- (H1) is load-bearing.
```

Tests plant negatives: halving an admitted contraction fails (H2); a
smaller-than-true `ρ` (5/16 against a binding 3/8) is refused on the full
product; a wrong sheet bound is refused.

---

## 5. Exact rational certificate

```text
python proof_lab/local_to_uniform_seam_gap.py
python -m unittest proof_lab.test_local_to_uniform_seam_gap -v
```

Expected status: `PASS_LOCAL_TO_UNIFORM_SEAM_GAP_CANDIDATE`

Expected SHA-256:

```text
d75992cd8fea4ed9b4b1d10a0dd5defe22651ba749b1c3b888be1ebd91a4ccb8
```

Arithmetic: `fractions.Fraction` only; "`e^κ`" never evaluated — `W` is the
declared rational sup-weight.

---

## 6. Claim boundary

```text
GLOBAL RECOGNITION CUT J_rec = 2⊗P_i − I; 2^m ORTHOGONAL SHEETS      PROVED
TENSOR CUT ⊗J_i ≠ RECOGNITION CUT (m ≥ 2)                              PROVED
(H1) ⟺ J_i-EVEN WITH RECOGNIZED VALUE f0                               PROVED
(H2) DECIDED BY EXACT CUT-SQUARE (theorum/41 (5.4))                     PROVED
THEOREM 3.1  ||QLQ|| ≤ ρ f0^m, ρ = max W_iλ_i/f0_i, UNIFORM IN m       PROVED (finite product)
SHEET LAW ρ^k f0^m, ATTAINMENT ON DIAGONAL INSTANCE                    PROVED
theorum/28 §9 OUTWARD CERTIFICATE u+e = ρ < 1 DELIVERED m-UNIFORMLY    PROVED
MEMORY-ONLY COUPLING: ρ → ρ+β, RECOGNIZED VALUE UNTOUCHED              PROVED
EXACT RATIONAL CERTIFICATE                                  IMPLEMENTED / USER RUN REQUIRED

INFINITE-FACE LIMIT m → ∞ (theorum/28 §11 hypotheses 1–5)              NOT BUILT
m-UNIFORMITY OF THE COUPLING NORM β                                    DECLARED, NOT DERIVED
LEAKING (NON-SEAM-COMPATIBLE) FACES                                    NO CLAIM
W = exp(κ) IDENTIFICATION                                              NOT CLAIMED
RH, YANG–MILLS, ANY OTHER GATE                                         UNTOUCHED
```

This is the first framework theorem whose conclusion is a bound that is
**the same number for every size**.  It closes theorum/28's hypothesis 6
for product carriers; hypotheses 1–5 remain the next obligations.
