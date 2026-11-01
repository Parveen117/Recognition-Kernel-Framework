# SE30 scope and verification

12 October 2026. Owner: Monty.

| Assertion | Evidence and scope |
| --- | --- |
| Positive constant-unit counting | Theorem 1; nonempty strings, concatenation and repeated grouping |
| No primitive empty count or geometric cut | Definition of the initial carrier; later completions are explicit |
| Neutral class and rational ratios | Theorem 2; difference pairs and ratio pairs, distinct from the cut operator |
| Primes and factorization | Theorem 2; elementary proof and transport under faithful unit changes |
| Zero means the cut operator in this packet | Theorem 3; explicit graded map, kernel, target, marked lift and idempotent representative |
| Counts survive the cut | Theorem 3; n Lambda maps to n u in degree one |
| Quantity products survive with their degree | Theorem 3; cut degree adds under multiplication |
| Counting operators and polynomial identities | Theorem 4; lowering, raising, conjugacy and transported product |
| Exponential family and its cut member | Theorem 5; formal coefficient proof, no numerical division at the cut |
| New curvature or RH sign | None; this stage follows the requested arithmetic-first order |
| Best inherited global RH certificate | SE27 eta=1079/2000, native floor 1/492000, unchanged |

Five written theorems contain the universal arguments. There are 31
exact application checks, including eight negative controls. Arithmetic
controls factor all positive counts through 512 and check preservation
by the marked-unit cut. Polynomial controls use four nonzero rational
steps, the falling basis through degree 10, ordered-choice counts through
12, and formal exponential jets through order 10. Separate coefficient-
cut controls verify powers, differentiation and exponential coefficients.
The finite checks do not stand in for the written all-degree proofs.

The controls reject empty primitive counts, implicit mixing of unit
labels, confusing a count product with a quantity product, numerical
annihilation as a replacement for the cut, dropping the unit degree,
below-degree inputs, an incorrect ordinary Leibniz rule, and cutting
away the step response before removing its unit factor. The application
imports the canonical coefficient and Laurent engines directly; it
does not create a second shared arithmetic engine.

The statement that counting starts without an additive identity is
limited to its initial positive carrier. The later ring contains the
neutral class derived in Theorem 2. The cut operator has its own domain
and retained target. No identification between those types is claimed.
The formula deformation is the declared ordered-choice construction;
no uniqueness of all possible deformations is asserted. Infinite
analytic evaluations require additional convergence and domain data.

Reproduction uses Python 3.12.14 and Node v24.19.0:

```bash
node proof_lab/endpoint_lambda_counting.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The inherited RH archive is read and source-pinned; the expensive global
interval computation is not rerun. No new eta, global eta-zero result,
universal physical constant, complete replacement of mathematics,
proof-assistant check or external review is claimed.

The read-only replay reproduced the complete archived JSON byte for byte,
passed all 31 checks and verified 95 source pins. All eight mathematics
navigation tests passed. The publication check compares inherited pinned
blobs with the parent and preserves all non-navigation parent blobs.
The packet contains six new files and four navigation updates.

The required unchanged whole-engine gate was executed and reproduced its
inherited first-suite failure in `tests/verify.cjs --check`: expected
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`,
actual
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`.
Later suites did not execute. No engine source or pin was changed to
make that gate pass. Scoped direct coefficient/Laurent controls pass;
whole-engine PASS is not claimed.
