# SE43 scope: counting movement, seam descent and retained memory

13 October 2026 (Asia/Kolkata). Author: Monty.

## Written development

The [theorem](SE43_COUNTING_TO_EMK_SEAM_TRANSPORT.md) has five groups:

1. The lawful counting translation is U translation U^(-1), preserving
   the formula product. Raw x-translation fails that product law by
   exactly -Lambda L in the quadratic example.
2. A matrix-valued semilinear seam g tau preserves a counting connection
   exactly when D_i g+A_i g=g tau(A_i). The connection and both seam
   endpoint frames transform together.
3. Two scalar periods admit the stated Z^2 lift exactly when their
   ordered seam defect Delta=g_1 tau_1(g_2)-g_2 tau_2(g_1) is neutral.
   This condition is frame-independent and is not supplied by F=0 alone.
4. Explicit polynomial moving frames retain a nonidentity cyclic seam.
   A flat three-channel example retains central integer memory in an
   MR-03/Heisenberg extension and fails the ordinary commuting-period
   relation. It is not falsely certified as a flat torus bundle.
5. Complete accepted/complementary ordered readings recover Delta.
   Labelled unit cuts preserve the decoder. Degree-h seam matrices
   give sufficient depth 2h, attained by an exact three-channel example.

An additional source audit corrects the deck/forward-lift distinction in
the public EMK-G3 T2 compensator. It is a scoped correction with an exact
-4/5 scale witness. The earlier source is preserved.

The local curvature mechanism is reused from SE42/EMK-C1; no duplicate
universal curvature result is claimed. The integer extension consumes
MR-03. The circle/cylinder/torus dictionary is conditional on an explicit
product circle fibre. The complete TVSP or double-helical identification
is not proved merely by matching these names.

## Observer evidence and reproduction

The [replay](../../proof_lab/counting_emk_seam.py) reuses SE42's exact
polynomial evaluator under Python 3.12. It records five full seam-reading
banks: a noncommuting flat seam, its moving-frame/moving-cut version, and
a degree-two unit seam pair at retained depths 0, 3 and 4. Two further
integer word records recover their path labels from two response columns.
The decoder takes serialized responses, cut metadata and word orientation,
not a hidden seam matrix. Connection/seam fixtures are only used by the
acquisition procedure and its independent expected-target comparison.

Thirty-two exact controls pass, including twelve negative controls.
They include the raw-translation mismatch, omitted endpoint/derivative
terms, a wrong semilinear inverse, local-flat/global-order nonclosure,
accepted-channel blindness, shallow-unit blindness and the source deck
sign. General proofs and these finite instances have separate scopes.

```bash
python3.12 -m proof_lab.counting_emk_seam --write
python3.12 -m proof_lab.counting_emk_seam --check
python3.12 -m proof_lab.counting_curvature --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Executed checks:

- SE43's 32 controls and saved observer replay pass with local source pins.
- SE42's unchanged replay passes: 30 controls, including 10 negative controls.
- All 8 mathematics-navigation tests pass.
- The required full-engine check fails at `tests/verify.cjs --check`
  with the inherited mismatch already recorded in SE42:

  ```text
  expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
  actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
  ```

The engine and its pins were not changed. No full-engine PASS, external
review, proof-assistant verification or fresh execution of the entire
EMK geometry suite is claimed. Public source blobs are provenance pins;
the offline replay checks local pins and the saved new readings.

## Boundaries

The supplied seam rules are data, not consequences of counting alone.
This stage gives an explicit algebraic non-Abelian memory instance, not
a universal classification of TVSP motion. A central extension retains
a failed quotient relation; it does not make that relation the identity.
Local flatness, matrix seam return, integer memory and metric curvature
are distinct targets. The frame invariants are the transported objects
and their vanishing conditions, not numerical equality of arbitrary
matrix entries across frames.

Formal unit completion is not evaluation at a numerical unit or physical
time. No arbitrary numerical connection exponential is used. Constant
shifts commute with unit cuts; more general unit-dependent or singular
movement adapters are outside the stated finite-degree result. The
sharp depth 2h applies to the additive ordered defect, not a general
inverse series. Full labelled coefficient readings are not finitely
many scalar point observations.

Zero names the typed Cut, separately from neutral endomorphisms and
identity maps. The source S_b and all RH certificates remain unchanged:
global eta 1079/2000 with floor 1/492000, eta zero on SE21's V_16, and
the universal source sign still open. No RH proof, new mass gap or
physical thermodynamic conclusion follows from this geometry bridge.
