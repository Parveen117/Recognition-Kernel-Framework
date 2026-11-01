# SE42 scope: counting curvature and observer memory

13 October 2026 (Asia/Kolkata). Author: Monty.

## The written result

The [theorem](SE42_COUNTING_CURVATURE_AND_OBSERVER_MEMORY.md) completes
the curvature step deferred in the SE30--SE38 counting chapter. Five
derivation groups establish:

1. All response lifts obeying the counting Leibniz law on B^r have the
   form D_i+A_i. Their mixed ordered-path reading is the B-linear
   curvature F_ij=D_i A_j-D_j A_i+[A_i,A_j]_bullet.
2. Curvature is the mixed coefficient of the full formal return. Flatness
   is equivalent to path independence in the stated formal additive
   protocol. A commuting curvature gives the exact central exponential;
   the noncentral example retains additional ordered coefficients.
3. Moving response frames, noncommuting counting-direction frames and
   the covariant Bianchi identity follow from the same product rules.
   The correction for the direction bracket is explicit.
4. A moving idempotent observation cut retains a complement-return
   curvature term. Complete accepted and complementary two-path readings
   decode the full curvature, even when the compressed curvature vanishes.
5. Labelled unit-memory cuts commute with curvature and formal return.
   All depths separate the complete formal curvature. Unit degree h of
   the connection coefficients gives sufficient curvature depth 2h;
   a two-channel example attains that worst-case bound for h>=1.

The definitions classify a supplied response transport on the derived
counting algebra. They do not select one unique connection. The unadorned
D_i transport is flat. The explicit D_1, D_2+c(Lambda)X_1 choice has
curvature c(Lambda)I. It is generated using the existing counting actions,
without a thermodynamic or Riemannian connection as a premise.

## Observer readings

The executable uses Python 3.12 standard-library rational arithmetic in
the admitted faithful counting-coefficient chart. It is a finite
application witness, not a second shared native engine. The source
engine and its pins are unchanged.

Thirty exact controls, including ten negative controls, pass the saved
read-only replay. The archive includes complete labelled two-path responses for:

- A third-order unit curvature, read at depths 0, 2 and 3. The first two
  banks are blind to the retained third-order response.
- A moving two-channel frame and moving cut. The compressed curvature
  vanishes, while complementary readings recover the nonneutral source.
- A three-slot connection with nonlinear polynomial coefficient profiles.
  A bounded-depth bank reconstructs the full selected curvature matrix.

The controls also check the actual falling-count adapter, the derived
product rule, formal loop coefficients, a noncentral exact return,
frame-derivative terms, a noncommuting but flat pure frame, the direction
bracket, Bianchi compatibility, unit-quotient products, sharp memory
depth and the finite count-window boundary response. Formal flows are
computed only through declared step degrees; no floating-point norm,
spectral decomposition or numerical exponential is used.

The saved decoder reads serialized path responses and their cut/depth
metadata. It does not obtain the curvature from a hidden connection
matrix. The independently supplied fixture connection is used by the
sensor and by the comparison that checks the decoded result.

## Reproduction and verification

```bash
python3.12 -m proof_lab.counting_curvature --write
python3.12 -m proof_lab.counting_curvature --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Executed validation:

- The read-only observer replay matched the saved archive and all 17
  local source pins: 30 exact controls, including 10 negative controls.
- All 8 mathematics-navigation tests passed.
- The required full-engine check failed at `tests/verify.cjs --check`,
  with the same inherited pin mismatch recorded in SE41:

  ```text
  expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
  actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
  ```

The engine and its pins were not altered. The full engine suite is not
reported as passing. The finite readings, written proofs, source
integrity and any external review are separate evidence classes.

## Boundaries

Zero continues to name the typed Cut. A neutral curvature value is an
element of its stated endomorphism module; it is not the Cut itself.
Cut-level flatness does not establish full flatness: c=Lambda^m is the
explicit counterexample. Conversely c=1 stays curved at the degree-zero
cut. Lambda is not identified with eta or with a physical curvature scale.

The response coefficients may be nonlinear counting polynomials, but
the connection acts linearly on its response module. General nonlinear
state evolution needs a separate lift and is not silently included.
No boundedness, metric, physical time, numerical flow convergence,
universal acquisition cost or noise stability theorem is asserted.
The bank uses whole polynomial/coefficient readings, not scalar samples.

The path-independence theorem concerns words of the declared formal
flows. It does not prove trivial global holonomy on an arbitrary
quotient space or erase independent winding memory. Covariant entries
need not be equal across frames; the full transported operator and its
vanishing are the invariant objects. No coordinate norm is imposed.

The standard algebraic curvature and gauge mechanisms are not claimed
as new to mathematics. The contribution is the completed derivation and
observer/memory interface for this counting construction. A finite PASS
is not proof-assistant verification or independent external review.

SE29, SE41, thermodynamic physical adapters and the actual RH source are
not redefined. The best global RH eta remains 1079/2000, with floor
1/492000; SE21's eta-zero result remains on V_16. Neither RH nor a new
Yang--Mills mass gap follows from this stage.
