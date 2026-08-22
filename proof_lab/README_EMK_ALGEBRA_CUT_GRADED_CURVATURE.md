# EMK Algebra Cut-Graded Curvature (theorum/48)

Connects two previously separate pieces of certified work:

- `theorum/42_cut_graded_lambda_jacobian_tower_theorem.md` (this repo) —
  abstract cut involution `J_E`, even/odd grading, cut-loop curvature
  `F_st = [G_e, G_o]`. Leaves "physical T-V-S-P cut and response-fibre
  involution" and "operator curvature -> response two-form adapter" OPEN.
- Publications repo `papers/emk-ugd-algebra/` EMK-1/EMK-2 — a certified
  primitive algebra `{I,K,R,RK}` with `K^2=I`, `R^2=-I`, `RK=-KR`, and a
  proved `Z/2` grading (`{I,K}` even, `{R,RK}` odd).

This capsule shows the EMK algebra is a concrete, exactly-computable
instantiation of theorum/42's abstract axioms: `J_E := K` satisfies the
involution axiom, the induced grading matches EMK-2's grading exactly
(re-derived here from scratch, not imported), and the cut-loop curvature
of the representative pair `(G_e, G_o) = (K, R)` is available in **exact
closed form**, `F_st = -2 RK`, with a general closed form
`[aI+bK, cR+dRK] = -2b(dR+cRK)` verified on a grid of rational points.

It does **not** claim the physical adapter of theorum/42 Eq. (6.7), and
does **not** claim this is *the* correct involution for the physical
T-V-S-P lambda map. See the theorem file's claim boundary for exactly
what is and is not closed.

## Reproduce

```bash
python proof_lab/emk_algebra_cut_graded_curvature.py
python -m pytest proof_lab/test_emk_algebra_cut_graded_curvature.py -v
```

Expected status: `PASS_EMK_ALGEBRA_CUT_GRADED_CURVATURE_CANDIDATE`
Expected SHA-256: see `EMK_ALGEBRA_CUT_GRADED_CURVATURE_EXPECTED.sha256`.
