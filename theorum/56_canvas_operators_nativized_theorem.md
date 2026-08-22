# Canvas Operators Nativized (Bindu–Lopa, Pāṇini, Operator-Universe, Aghora, OM, projector sectors)

> **Filing note.** Built in a parallel session and originally filed as theorum/50; renumbered to 56 to resolve the collision with `50_native_seam_gap_odd_sector_covariance_theorem.md`. Content unchanged.
>
> **Cross-reference (B4).** The Aghora refusal below is a **derived-layer (Hilbert/PSD) verdict**: it consumes Theorem 49's PSD machinery, so "G ≥ 0" there means inner-product positivity. On the primitive carrier the anticommuting object is the odd (turn) channel of the cut square — indefinite by construction, never PSD, yet carried and transported: theorum/50 (A1–A6), theorum/51 (exchange law), theorum/55 (EMK dock). The refusal and the repair are the same fact seen from the two layers.

## 1. Source and scope

Twelve owner canvases (Aghora, Asato Mā, Aṣṭādhyāyī, Māṇḍūkya/Līlā/Sāṅkhya,
OM eigenmode, OM λ-heat, Operator Universe, Pāṇini 1.1.1–1.1.15, Pāṇinian
engine, Bindu–Lopa recursion, Operator Combination Generator) were read as
**hints**.  No canvas is a source of theorems.  Everything below is either a
theorem in the framework's own cut algebra (theorum/41 grading, UGD-1 seam
alphabet and projection blindness, EMK-T2 order-is-content, Theorem 49) with an
exact certificate, or an explicit refusal.  No interpretation is claimed.

## 2. Results

**B1 Bindu–Lopa (⊙ = phase lift, 𝓛 = seam projection).**
- `[⊙,𝓛]` is **chart content**: in the Cartesian chart it is nonzero
  (`z=(3,4)`: `𝓛⊙z=(3/5,0)`, `⊙𝓛z=(1,0)`); in the native additive chart
  (F00G `Log_Σ` / UGD digit: scale ⊕ phase) ⊙ and 𝓛 are complementary
  commuting projections and the canvas's `R=⊙+𝓛−𝓛⊙` is exactly `I`.
- `C=𝓛⊙` iterated twice lands in the **UGD seam alphabet** `{−1,0,+1}`
  (UGD-1) and is stationary thereafter (`C³=C²`); fixed points of `C` are
  exactly `±1` and the declared cut-zero (`⊙0:=0`, UGD-1 T5).
- Canvas claim "`R` idempotent" in the Cartesian chart: **not certified**
  (no rational witness exists).

**B2 Pāṇinian rewrite algebra** (toy alphabet `{a,i,u,e,o,y,v,K}`; guṇa,
yaṇ, marker-gated yaṇ, lopa of `K`).
- lopa (1.1.6/1.1.15) is an idempotent zero map on the marker sector and the
  identity on the visible sector.
- Rewrite operators do not commute (`aia`: guṇa-then-yaṇ `ea`, yaṇ-then-guṇa
  `aya`); free application is **not confluent** on six strings; a declared
  precedence (*vipratiṣedhe paraṁ kāryam*) restores a unique normal form —
  precedence is the framework's order-is-content (EMK-T2).
- **Anubandha = projection blindness** (UGD-1 T4): `Kiu → yu` (marker fires,
  then elided) and `yu` have identical visible output and different ledgers;
  act-then-elide `yu` ≠ elide-then-act `iu`.

**B3 Operator-Universe tower IS theorum/41's grading.**  With `A²=A`,
`J=2A−I`: `R:=[A,[A,G]]` equals the **odd grade** of `G`; `[A,R]=D` (period
two); `D=[A,G]` is cut-odd; `D=0 ⟺ G even` ("no interaction → no time" =
seam compatibility).  Verified on 7,542 rational `G`.

**B4 Aghora — REFUSAL.**  Axioms `A²=I`, `AGA=−G`, `G≥0` (square-sourced)
force `G=0` (exhaustive on a rational grid: the only PSD anticommuting `G`
is zero); the canvas's additional `[A,G]=0` forces `G=0` a second way.
Lawful repair: anticommuting `G` are exactly the **cut-odd signed** forms
(theorum/41 (3.3)); a nonzero one is indefinite, never PSD.

**B5 OM / λ-heat.**  On the EMK carrier `Δ=−ωI+αR`: decay is even, spin is
odd, cut-loop curvature `[G_e,G_o]=0`, so the binomial power law holds
exactly (n≤6 — the algebraic content of `e^{tΔ}=e^{−ωt}e^{αtR}`, no
exponential evaluated); control: even part `−ωI+K` breaks it.  Holonomy
commutes.  **OM gap on an m-torus** = Theorem 49 instance with faces
`diag(1,ρ)`: memory contracts by `ρ` for `m=1..4`, independent of `m`.

**B6 Projector sectors.**  Product of projectors is a projector iff they
commute (both witnesses; 3-4-5 tilt for non-commuting); every projector is a
cut-square contraction; the Māṇḍūkya four-sector sum is a resolution of the
identity (sheet lattice; Turiya = recognized sheet); Līlā `κ=‖[A,U]‖=0 ⟺ H`
even (U a polynomial in H).

## 3. Certificate

```text
python proof_lab/canvas_operators_nativized.py
python -m unittest proof_lab.test_canvas_operators_nativized -v
```
Status `PASS_CANVAS_OPERATORS_NATIVIZED_CANDIDATE`, SHA-256
`df4c77161f37e874b4fd22d0a8af3d3e1e65a263d4e9afbd4dea14f9bdf9ea68`.
Consumes `proof_lab/local_to_uniform_seam_gap.py` (Theorem 49) for the exact
PSD/norm machinery and product carrier.

## 4. Claim boundary

```text
BINDU-LOPA COMMUTATOR IS CHART CONTENT                         PROVED
C^2 IN SEAM ALPHABET, C^3=C^2, FIXED POINTS ±1 + CUT-ZERO      PROVED
PANINI: LOPA ZERO MAP, NON-COMMUTATION, NON-CONFLUENCE,
        PRECEDENCE, ANUBANDHA = PROJECTION BLINDNESS           PROVED (toy alphabet)
OPERATOR-UNIVERSE TOWER = theorum/41 GRADING                   PROVED
AGHORA AXIOMS FORCE G=0 (two routes); ODD-SIGNED REPAIR        PROVED / REFUSAL
OM: ZERO CUT-LOOP CURVATURE, EXACT FACTORIZATION, m-TORUS GAP  PROVED
PROJECTOR PRODUCT IDEMPOTENT IFF COMMUTE; LILA κ=0 IFF EVEN    PROVED

R=⊙+𝓛−𝓛⊙ IDEMPOTENT (CARTESIAN)                              NOT CERTIFIED
FULL ASHTADHYAYI ENGINE (3,959 rules)                          DECLARED PROTOCOL
CONTINUUM LAPLACIAN / TORUS EIGENMODES                         NOT CLAIMED
ANY INTERPRETIVE CONTENT OF THE CANVASES                       NOT CLAIMED
RH, YM, OTHER GATES                                            UNTOUCHED
```
