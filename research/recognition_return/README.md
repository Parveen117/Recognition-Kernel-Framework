# Native graded-aperture research result R1

This is an additive research packet in the single canonical Recognition-Kernel-Framework repository. It **uses** `operator_foundation/core` and does not fork the engine or change its v0.5 master certificate. The mathematics, tests and output belong together here.

Main example: `R^2=-1, K^2=1, KR=-RK`, opening coefficient `2R`, return coefficient `(3/5)K`, and native seam shifts `TS=1` with `ST!=1`. The full Neumann series and the boundary moment series diverge. Inverses on even finite apertures have a convergent boundary response, exactly `1+(2/3)KR`. No primitive Hilbert space or positive pairing is used.

The practical solver iterates `d_(k+1)=q/(1+q*d_k)` and returns an exact rational bracket. The main example reaches error below `10^-12` at refinement index 34, using the corners of heights 68 and 70. Its infinite limit follows from the proof, not from these two finite numbers.

A joint strong-coupling/aperture result is

    mass((1+d_k KR)/2 - (1+KR)/2) <= q/k + 1/(4q).

The order of limits matters. Increasing coupling with a fixed aperture can give a wrong limit or an unbounded result. The theorem states precisely how refinement prevents that failure.

Run from the repository root, without dependencies or network:

```text
node research/recognition_return/verify.cjs --check
node research/recognition_return/return_solver.cjs
```

Read `THEOREM.md` for the proofs and the exact input family, `LINEAGE.json` for immutable source pins, and `RESULT.json` for the freshly generated evidence. A deliberate reviewed evidence change uses `--write` instead of `--check`.

The standalone research companion has the same repository-relative layout and includes only the two unchanged canonical core files needed by this packet. It is not a replacement for the full workbench and does not contain private historical sources. No existing mathematical source is modified by this research result.

The result solves a declared boundary-response problem, not the full infinite source equation. It is a breakthrough candidate for the framework's recognition-first programme, not a claim of external priority for Catalan or continued-fraction methods or a physical quantum-gravity result.
