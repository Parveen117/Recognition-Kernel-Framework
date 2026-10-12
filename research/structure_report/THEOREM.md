# Structure report R3: cut split, observer completion, and the returning-memory mark

Author: Monty Dabas. Development edition: 12 October 2026.
Status: written general arguments under the hypotheses below, with exact finite checks in `verify.cjs` and mutation controls in `mutate.cjs`. Finite PASS results prove the specified computations; they are not universal proofs.

## 0. What this packet does

A problem is supplied as finite declared data on the cut-complex carrier `C_Sigma^n`:

    S  = {s_1, ..., s_k}   action catalogue (what the problem can do),
    C  : C_Sigma^n -> C_Sigma^m   observer rows (what is seen),
    L  : optional target rows (what must be answered),
    J  : optional admitted cut, J = J^dagger = J^-1 (N01),
    mu : optional threshold list for the seam-count reading.

The report returns, in this order: the cut grading of every generator (N01), the minimum future-complete observer `D` (N03) together with the extra channels it forces, the mark that observation leaves (N06 on the completed observer), the cut-square factorization of the total mark (theorum/53), and a seam-count reading of the mark pencil (theorum/76 shape). It ends in one of three verdicts:

    VISIBLE_LOCAL            nothing hidden, nothing returns
    HIDDEN_LOCAL             channels must be added, then nothing returns
    GLOBAL_RETURNING_MEMORY  something returns on the reversed path; its energy and rank are the structure

The order is the one declared in theorum/31: cut-generated memory, target-relevant range, observer action, minimal faithful observer, and only then the finite seam matrix. The observer is completed before anything spectral is read.

## 1. Dependency order and terminology

Scalars are exact cut scalars `z = rad + iota turn` with `iota^2 = -1`, `z^dagger = rad - iota turn`, native norm `N(z) = z^dagger z = rad^2 + turn^2` (F00-E). Matrices over `C_Sigma` form the labelled finite path algebra `A_n` of N01; the dagger is path reversal, realized in coordinates as conjugate transpose. It is never the coordinate transpose: `mutate.cjs` plants that substitution and `verify.cjs` shows the wrong sign it produces on the turn instance.

`M_Sigma(a) = sum |rad| + |turn|` is cut-tail mass and `E_Sigma(a) = sum N(a_ij) = tr rad(a^dagger a)` is recognition energy, the two native verdicts of RH-Framework T01-A/B/C used throughout the operator ladder. No ordinary inner product, operator norm or eigenvalue is used as a primitive verdict.

For a set of rows `D` with independent rows, `D D^dagger` is nonsingular: if `(D D^dagger) y = 0` then `y^dagger D D^dagger y = E_Sigma(D^dagger y) = 0`, so `D^dagger y = 0`, and `D^dagger` is injective. This uses only the native norm law `N(z) = 0 => z = 0`. Define the **retained projector**

    P = D^dagger (D D^dagger)^-1 D,     Q = I - P.

Then `P^2 = P = P^dagger`, `ker P = ker D`, and `P` is the recovered memory projector of theorum/31 (`P_T = T^dagger T` for a coisometry `T`) written without a normalization step.

When the carrier is presented in a basis that is not a label set, the reversal is taken under a declared pairing `B` (a self-dagger cut square with positive weights): `a^sharp = B^-1 a^dagger B`, `P = B^-1 D^dagger (D B^-1 D^dagger)^-1 D`. `B = I` is the case treated below; the extension, its basis covariance and the first real encoding are in `r4/THEOREM.md`. Every proof below uses only `P = P^sharp`, `(ab)^sharp = b^sharp a^sharp` and `N(z) = 0 => z = 0`, so it holds verbatim with `dagger` read as `sharp`.

## 2. Stage 1: cut grading (N01)

For an admitted cut `J` and any generator `s`,

    s_even = (s + J s J)/2,   s_odd = (s - J s J)/2,
    J s_even J = s_even,   J s_odd J = -s_odd,   s = s_even + s_odd.

The report records `M_Sigma(s_even)`, `M_Sigma(s_odd)` and whether a generator is purely even or purely odd. This is the cut grading of N01 and T41; it is not the radial/turn split and not the self/skew-dagger split (T55 distinction retained).

## 3. Stage 2: observer completion (N03)

`D` is the stabilized row closure of `row(C) + row(L)` under right multiplication by the catalogue, computed by the canonical `rowClosure`. N03 proves `D` is the minimum-rank refinement of `C` that recovers `L` and descends every generator: `D s = s_bar D`. The report records

    forward_extra = rank(D) - rank(C),
    dagger_extra  = rank(D^#) - rank(D),

where `D^#` is the same closure with the reversed catalogue `S ∪ S^dagger` included. N03 already notes that including daggers is an additional contract that may raise the rank. Section 5 shows that `dagger_extra` is exactly the returning memory.

## 4. Stage 3: the mark (N06 on the completed observer)

### Theorem R3-A (forward closure of the completed observer)

Let `D` be the N03 completion and `P` its retained projector. Then for every `s` in `S`

    P s Q = 0,

and consequently, for every pair of words `a, b` in the generators (forward words, no daggers),

    Phi_P(a b) = Phi_P(a) Phi_P(b),     Phi_P(x) = P x P.

**Proof.** `ker D` is invariant under every generator: if `D x = 0` then `D s x = s_bar D x = 0`. Since `ker P = ker D` and `Q` maps into `ker D`, `D s Q = 0`, hence `P s Q = D^dagger (D D^dagger)^-1 D s Q = 0`. For a word `w = s w'`, insert `I = P + Q`: `P w Q = P s P w' Q + P s Q w' Q = P s (P w' Q)`, which vanishes by induction on the length of `w'`. The N06 identity `Phi_P(ab) - Phi_P(a) Phi_P(b) = P a Q b P` then vanishes because `P a Q = 0`. QED.

So the completed observer compresses the forward word algebra homomorphically: nothing that leaves the retained sector ever returns on a forward path. That is the exact content of "future-complete". The raw observer does not have this property (`verify.cjs`, `raw_observer_is_not_forward_closed`): the EMK observer `C = (1,0)` leaks forward under `R`.

### Definition (returning memory, the mark)

For each generator `s` define its **leak** `leak_s = Q s P` and its **mark** `leak_s^dagger leak_s`. By N06 in a self-dagger idempotent,

    Phi_P(s^dagger s) - Phi_P(s^dagger) Phi_P(s) = leak_s^dagger leak_s.

The left side is the syringe test: observe `s^dagger s` as one event, or observe `s` and `s^dagger` separately through the retained sector and multiply. The difference is a square. Its trace is `E_Sigma(leak_s)`, the returning-memory energy of `s`. The **returning-memory form** is

    K = sum_s leak_s^dagger leak_s,      K Q = Q K = 0.

### Theorem R3-B (returning memory is dagger incompleteness)

The following are equivalent:

1. `leak_s = 0` for every `s` in `S`;
2. `P` commutes with every `s` and every `s^dagger`;
3. `dagger_extra = 0`, that is, the forward completion `D` is already closed under the reversed catalogue.

**Proof.** (1 => 2) `Q s P = 0` and `P s Q = 0` (R3-A) give `s P = P s P = P s`; taking daggers with `P = P^dagger` gives `s^dagger P = P s^dagger`. (2 => 3) `P s^dagger = s^dagger P` makes `ker P = ker D` invariant under `s^dagger`, so every row functional of `D` composed with `s^dagger` vanishes on `ker D` and lies in `row(D)`; the dagger closure adds nothing. (3 => 1) If `row(D)` is right-invariant under `s^dagger`, then `ker D` is invariant under `s^dagger`, so `P s^dagger Q = 0`; taking daggers, `Q s P = 0`. QED.

The report computes all three routes independently (`leak_free`, `projector_commutes_with_catalogue`, `dagger_extra_zero`) and refuses if they disagree. On every named instance they agree. The fault control `forward_leak_mistaken_for_the_mark` replaces `Q s P` by `P s Q` and is rejected: the mark lives in `Q s P`.

### Theorem R3-C (the mark is a cut square)

`K` is self-dagger and square-sourced, so by theorum/53 T1 it factors exactly as `K = C^dagger Dg C` with turn-free nonnegative weights; its rank is the number of independent returning channels; by T53 T2, `tr rad(K) = sum_s E_Sigma(leak_s) = sum_k d_k E_Sigma(c_k)`; by T53 T6, `prod d_k = det K`, which the report confirms by an independent elimination determinant. `K = 0` exactly in the local cases of R3-B.

**Proof.** Each summand is `leak^dagger leak`. The congruence elimination of `congruenceDiagonalize` is theorum/53's exact elimination with native scalar inverses; when a diagonal pivot vanishes with a nonzero row, the congruence `u = e_k + c e_t`, `c = K_kt`, produces the new pivot `K_kt c^dagger + c K_tk = 2 N(K_kt) > 0`, so the elimination never needs a square root or an eigenvalue. Negative weights are refused for squares (T53 T3) and returned with an exact witness `v` with `v^dagger T v` equal to the weight otherwise. QED.

### Theorem R3-D (cut-aligned observer: all returning memory is odd)

If the completed observer is a `J`-face, `P = (I + J)/2`, then for every generator `leak(s_even) = 0` and `leak(s) = leak(s_odd)`.

**Proof.** `s_even` commutes with `J`, hence with `P` and `Q`, so `Q s_even P = s_even Q P = 0`. Linearity of the leak gives the rest. QED.

When the observer is not a face, even generators can leak as well; the report then records the even and odd leak masses separately. Instance `cut_misaligned_observer_3` shows an even leak of mass 2 beside an odd leak of mass 3 on the same report.

## 5. Stage 4: factorization and seam-count reading

The report factors `K` (R3-C) and, for each declared threshold `mu`, computes the exact inertia of the pencil `K - mu P` (theorum/76 shape: a sector label `n_+(M - mu B)`). `n_+` is non-increasing in `mu` because `P >= 0` on its range. No law relating the T53 weights to pencil thresholds is claimed: instance `turn_observer_2` has `K = P` exactly, weights `(1/3, 0)` and a single flip at `mu = 1`, consistent with theorum/53's boundary "weights = eigenvalues NOT CLAIMED".

## 6. The trichotomy

    forward_extra = 0 and K = 0   VISIBLE_LOCAL
    forward_extra > 0 and K = 0   HIDDEN_LOCAL
    K != 0                        GLOBAL_RETURNING_MEMORY   (equivalently dagger_extra > 0 by R3-B)

`HIDDEN_LOCAL` is a genuine information-losing but decomposing quotient (N03's block control, `block_local_3`). `GLOBAL_RETURNING_MEMORY` is where a global condition lives: the retained sector cannot be closed under reversal, the obstruction is the square `K`, its energy is `sum_s E_Sigma(leak_s)`, its rank is the number of returning channels, and the generators carrying it are named in the report. Nothing in this verdict decides whether the supplied problem has a solution; it says what the supplied encoding permits and what must be tracked.

## 7. Scope and lineage

- Finite declared carrier only. The finite-to-infinite outward certificate of theorum/28 is not invoked and no infinite statement is made.
- The encoding `(S, C, L, J)` is supplied data; N01's scope sentence applies unchanged: no theorem here selects the catalogue, the observation or the cut for nature.
- `R3-A` consumes N03 and N06. `R3-B` is new in this form; its ingredients are N03's invariance statement and N06's commuting criterion. `R3-C` consumes theorum/53 T1/T2/T3/T6. `R3-D` is a two-line consequence of N01. Finite row closure, invariant-subspace arguments and congruence diagonalization are standard mechanisms; no external priority is claimed for them.
- Verified exactly: 9 named instances, random cut-square factorizations, planted indefinite and zero-diagonal forms, transpose-versus-dagger control, 7 mutation controls.
- Continued in `r4/`: the repair step (R4-A/B/C), declared pairings and their basis covariance, and the YM-37 column pencil as the first real encoding.
- Not claimed: a universal problem solver, a decision procedure for the supplied problem, any physical identification, RH, YM, or continuum statements.
