# Structure report R3: cut split, observer completion, returning-memory mark

This is an additive research packet in the canonical Recognition-Kernel-Framework repository. It **uses** `operator_foundation/core/native_operator.cjs` unchanged and does not touch the v0.5 master certificate. Mathematics (`THEOREM.md`), engine (`structure_report.cjs`), named instances (`instances.cjs`), exact checks (`verify.cjs`), fault controls (`mutate.cjs`) and generated evidence (`RESULT.json`, `MUTATIONS.json`) belong together here.

**What it answers.** Supply a problem as finite data on the cut-complex carrier: an action catalogue `S`, an observer `C`, optionally a target `L`, an admitted cut `J` and thresholds. The report returns the structure of that encoding:

1. **Cut split** of every generator into even and odd parts (N01).
2. **Observer completion**: the minimum future-complete observer `D` and the exact number of channels it forces (`forward_extra`), then the same with the reversed catalogue (`dagger_extra`) (N03).
3. **The mark**: for each generator the leak `Q s P` out of the retained sector and its square, the N06 defect `Phi_P(s^dagger s) - Phi_P(s^dagger)Phi_P(s)`; its trace is the returning-memory energy `E_Sigma`. Even and odd leak masses are reported when a cut is declared.
4. **Factorization and reading**: the total mark `K` factored as weighted native squares (theorum/53) with rank, weights, Parseval and determinant channel; the seam-count `n_+(K - mu P)` at each declared threshold (theorum/76 shape).
5. **Verdict**: `VISIBLE_LOCAL`, `HIDDEN_LOCAL` or `GLOBAL_RETURNING_MEMORY`.

**Certified on the named instances:** the completed observer never leaks forward (`P s Q = 0`, R3-A); returning memory on the reversed path is present exactly when the reversed catalogue adds channels (R3-B, three routes agree on every instance); the total mark is a cut square with nonnegative turn-free weights and determinant channel equal to the weight product (R3-C); when the observer is a cut face, only odd generators leak (R3-D). Instance `cut_faces_two_strengths_4` shows two returning channels of energies 4 and 9 and a seam count stepping 2, 1, 1, 0, 0 across thresholds 1, 4, 6, 9, 10. Instance `turn_observer_2` shows that the native reversal, not a coordinate transpose, is load-bearing.

Run from the repository root, without dependencies or network:

```text
node research/structure_report/verify.cjs --check
node research/structure_report/mutate.cjs
```

A reviewed evidence change uses `--write`. The pinned evidence does not embed the runtime version string.

Use the engine directly:

```js
const {structureReport}=require('./research/structure_report/structure_report.cjs');
const report=structureReport({catalogue:{S:[[0,1],[0,0]]},observer:[[0,1]],thresholds:['1/2','1','3/2']});
// report.verdict === 'GLOBAL_RETURNING_MEMORY'; report.returning_memory.generators.S.leak_energy === 1
```

**Boundary.** Finite declared carrier; the encoding is supplied data; no primitive Hilbert space; theorum/28's outward certificate is not invoked. The report states what a supplied encoding permits and what must be tracked. It does not decide the supplied problem and claims no physical identification, RH, YM or continuum statement.
