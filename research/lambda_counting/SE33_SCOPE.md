# SE33 scope and verification

12 October 2026. Owner: Monty.

The certificate is the saved observer reading decoded for its stated
target. Replay and source records document those readings; they are
not independent mathematical certification conditions or permission
gates. Assumptions in a theorem specify which target it proves.

| Assertion | Scope of the written proof |
| --- | --- |
| Joint reading calculus | Theorem 1: arbitrary finite-output R-multilinear kernels on P, where R=Q[Lambda] and P has finite counting support |
| Joint composition | Exact finite expansion; outer tuples are obtained from recorded inner supports |
| Diagonal blindness | Theorem 2: the bilinear diagonal loses exactly the antisymmetric input-order part |
| Ordered recovery | An additional ordered-difference reading restores the missing part |
| Higher polarization | Specified homogeneous arity; an unsymmetric kernel yields its permutation average |
| Nonlinear response | Theorem 3: polynomial operations supplied by finite multilinear descriptions; coefficient response, finite Taylor and chain/product rules |
| Unit cut | Theorem 4: joint operations and response rules descend modulo Lambda^(q+1) |
| Nonlinear inverse | Theorem 5: each kernel output index lies below every input index; exact descending solution on every finite sector |
| Inverse response | Finite geometric inverse of the strictly lowering linear response on the specified sector |
| Inverse degree | Locally polynomial; the generated family has no global polynomial degree bound |

Five written proofs establish the general results. The executable
records 30 exact checks, including nine negative controls, using
unchanged canonical rational-cut arithmetic and expression normalization.
It is a counting-specific application, not a second shared engine.

The saved packets include:

- Joint composition on the four input pairs with indices zero and one,
  using six adaptively selected outer tuples.
- Diagonal and ordered-difference readings recovering T(p_1,p_2).
- Three rational-node readings recovering all coefficients of a
  constructed response of degree at most two.
- A complete two-input kernel bank on indices zero through three,
  its target p_3, the descending inverse trace and the recovered state.
- The inverse's linear response and the finite geometric sum target.

Each decoder accepts serialized response data rather than calling the
original operation. Further controls cover symmetric polarization at
arities two through four; generation of the kernel from existing
operators through index five; both nonlinear inverse identities on
mixed states through index three; a mixed quadratic/cubic example
through index two; unit cuts of orders zero through three; and inverse
response interpolation through degree eight.

Negative controls cover malformed/missing joint rows, an omitted
adaptive response, diagonal order blindness, unsymmetric polarization,
the invalid doubled single-slot product rule, unobserved polynomial
degree, independent unit/order information, output-lowering without
triangular dependency and incomplete/out-of-sector inverse targets.
The displayed finite ranges do not stand in for the written proofs.

The inverse theorem's dependency property is read directly in its
joint kernel. It is sufficient, not asserted necessary. Its failure
does not forbid another inversion method. A finite acquired bank
certifies the declared input sector; it does not identify an arbitrary
unknown global kernel. Polynomial interpolation uses a degree bound
derived from the constructed operation, never inferred from samples.

Zero remains the stated typed cut. Coordinate nulls are separately
typed additive neutrals. No infinite-state analytic derivative, metric
convergence, arbitrary nonlinear invertibility, uniform noisy-data
stability, physical quadrant identification, RH result or curvature
development is asserted. Elementary polarization and triangular
inversion carry no claim of novelty priority. Formal proof-assistant
verification and external review are not claimed.

Reproduction uses Python 3.12.14 and Node v24.19.0:

```bash
node proof_lab/lambda_joint_readings.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Read-only application replay reproduces the JSON archive byte for byte
and checks the SE33 source manifest. All eight mathematics navigation
tests pass. Publication adds seven files and updates four navigation
files. The pinned SE32 README stays unchanged; INDEX.md is the new
unpinned navigation surface.

The required unchanged whole-engine command reproduces its inherited
first-suite pin mismatch in tests/verify.cjs --check: expected
f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6,
actual
35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e.
Later aggregate suites do not run. No pin is changed to claim a PASS.
This aggregate issue is separately recorded and does not block the
present observer-reading development.

