# R4: the repair step and the first real encoding (YM-37 pencil)

Author: Monty Dabas. Development edition: 12 October 2026.
Status: written general arguments under the hypotheses below, exact finite checks in `verify.cjs`, mutation controls in `mutate.cjs`. Extends `../THEOREM.md` (R3). Finite PASS results prove the specified computations; they are not universal proofs.

## 0. What R4 adds

R3 reports the mark an observation leaves: the returning memory `Q s P` of the completed observer `D`, its energy and its rank. R4 answers the next question of the programme — what the mark tells the observer to do — and shows that on a finite carrier the answer is one step:

    repair:  observer  <-  D^#  (completion under the reversed catalogue S ∪ S^sharp)

After the repair there is no mark, nothing hidden remains, and repairing again changes nothing. The cost is exactly `dagger_extra` channels — the channels the mark named. R4 also carries the structure report onto its first real framework object, the YM-37 column pencil, under that pencil's own declared pairing.

## 1. Declared pairing (extension of R3 §1)

N01's labelled face carries the coordinate dagger. When a carrier is presented in a basis that is not a label set — YM-37's monomial basis `x0^a y0^b <vx,vy>^c` of the even invariant sector — the native pairing is a declared self-dagger cut square `B = C^dagger Dg C` with strictly positive weights (theorum/53), and the native reversal is

    a^sharp = B^-1 a^dagger B.

`B = I` recovers the coordinate dagger exactly; every R3 instance reproduces its pinned numbers under the extended engine. The retained projector becomes `P = B^-1 D^dagger (D B^-1 D^dagger)^-1 D`, with `P^2 = P = P^sharp` and `ker P = ker D`; the mark of a generator is `leak^sharp leak = B^-1 (leak^dagger B leak)`, whose coordinate form `leak^dagger B leak` is the cut square that theorum/53 factors; its trace is the returning energy under the pairing. The reversed-catalogue completion uses `S ∪ S^sharp`. Every proof of R3 goes through with `dagger` read as `sharp`, because they use only `P = P^sharp`, `(ab)^sharp = b^sharp a^sharp` and `N(z) = 0 => z = 0`.

**Basis covariance (checked exactly).** Under a change of basis `x -> G x`, the data move as `s -> G s G^-1`, `C -> C G^-1`, `L -> L G^-1`, `J -> G J G^-1`, `B -> G^-dagger B G^-1`. Verdict, forward and reversed ranks, every leak energy, the rank of the mark and the seam counts are unchanged (`declared_pairing_verdicts_are_basis_covariant`, five instances with turn-carrying `G`). The coordinate dagger alone is not covariant: the same move changes the returning energy of `one_way_flow_2` (`coordinate_dagger_is_not_basis_covariant`). This is the precise sense in which the pairing is part of the encoding and the transpose is not a verdict.

## 2. Theorems

### R4-A (repair kills the mark)

Let `D^#` be the N03 completion of the seed under `S ∪ S^sharp`. Then the structure report of `(S, D^#, B)` has `forward_extra = 0`, `dagger_extra = 0`, every leak zero, `K = 0`, verdict `VISIBLE_LOCAL`.

**Proof.** `row(D^#)` is right-invariant under every `s` and `s^sharp`, so its forward completion is itself (`forward_extra = 0`) and its reversed completion is itself (`dagger_extra = 0`). By R3-B (3 => 1) every leak vanishes, hence `K = 0`. QED.

### R4-B (minimality of the repaired observer)

Among observers `E` whose rows contain the seed, which descend the catalogue (`row(E)` right-invariant under `S`) and which carry no mark, `rank(E) >= rank(D^#)`, and `D^#` attains the bound.

**Proof.** Descending makes `E` its own forward completion, so R3-B applies to `E`: no mark implies `row(E)` is right-invariant under `S^sharp` as well. A row space containing the seed and invariant under `S ∪ S^sharp` contains the stabilized closure `row(D^#)`. QED.

The finite probe in `repairReport` removes one basis row of `D^#` at a time (keeping the seed) and confirms on every instance that the reduced observer either regrows to `rank(D^#)` or carries a mark; a smaller mark-free descending observer never appears.

### R4-C (one step)

Repairing `D^#` returns `D^#`: the repair is idempotent. **Proof.** Both completions of `row(D^#)` are itself (R4-A). QED.

Consequently the "learn how to learn" loop of the programme closes in one step on a finite declared carrier: report the mark, add exactly the channels it names, and the next report is clean. The whole history of the repair is the rank ladder `rank(C) -> rank(D) -> rank(D^#)` with the mark `K` recorded between the last two.

## 3. First real encoding: the YM-37 column pencil

Source, consumed by pin (`LINEAGE.json`): Publications `papers/yang-mills-certified-benchmark/certificates/ym37_space_transfer.py`, `build_pencil(2, u0, k0)` with the exactly validated rational coefficients `u0 = {1, 1/3, 1/10}`, `k0 = {1, 2/5, 1/10}` (YM-37 control C1 against the YM-33 engine). The data are the symmetric rational matrices `M`, `N`, `B` on the 8-dimensional even invariant sector `V_inv^+` (t = 2), the transfer `tau = B^-1 M`, and the constant monomial `e0`.

Encoding: catalogue `{tau}`, observer `C = e0^T M` (the boundary readout of `z(m) = <1, M tau^(m-1) 1>`), target `L = e0^T N` (the insertion readout), pairing `B`.

Facts certified exactly:

1. `tau^sharp = tau` under `B` (YM-37 T2: the pencil `(M, B)` is symmetric), while `tau^dagger != tau` in coordinates.
2. Under the declared pairing the report is `HIDDEN_LOCAL`: the boundary observer with the insertion target completes along the ladder `2 -> 4 -> 6`; six channels of the eight carry everything the readouts can ever see, two directions of `V_inv^+` are invisible to them; no returning memory; repair costs nothing.
3. The constant-coefficient readout `e0^T` alone completes to rank 7; again no returning memory.
4. Under the coordinate dagger — the wrong reversal for this basis — the same encoding reports `GLOBAL_RETURNING_MEMORY` with one extra channel and a mark of energy `1618373069/1180672000000`; the repair then costs one channel. This is a control, labelled as such in the evidence: the spurious obstruction is created by applying a label-set reversal to a non-label basis.

What this says and does not say. It says that, as an observation problem on the finite YM-37 column pencil, the boundary readouts are future-complete and reversal-closed after completion — the structure of the sector seen from the boundary is local, six-dimensional, with two invisible directions — and that the pencil's own pairing is load-bearing for that verdict. It does not say anything about the mass gap, the t-direction, the continuum or the Haar–Φ_Σ dictionary; those boundaries (Publications NG-1, YM-42 onward) are untouched.

## 4. Scope and lineage

- Finite declared carriers only; theorum/28's outward certificate is not invoked.
- The pairing is admitted only as a declared cut square with positive weights; no ordinary Hilbert space is a primitive. The reversal `a^sharp = B^-1 a^dagger B` is the dagger of the pairing, not a transpose.
- R4-A/B/C consume R3-A/B and N03 applied to the enlarged catalogue; the covariance statement is a direct computation. The YM-37 data are consumed by pin and not rederived.
- Not claimed: a universal solver, a Yang–Mills gap or continuum statement, any physical identification, external priority for invariant-subspace or congruence methods.
