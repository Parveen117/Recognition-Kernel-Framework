# SE45 proof scope and observer readings

13 October 2026 (Asia/Kolkata). Author: Monty.

## Written proof scope

[SE45](SE45_VARIABLE_JYA_CURVATURE_AND_TRACKING.md) proves six groups:

1. Variable-turn jya, the exact two-reading determinant and complementary
   repair at silent previous turns, with transported observer covectors.
2. Open-chain trivialization under free vertex frames, complete paired-path
   recovery and conjugacy of the closed return, and the general varying-step
   second-order identity.
3. The exact inhomogeneous counting flux for nabla_T=D_T and
   nabla_V=D_V+gJ, its horizontal-response orientation and mixed jya reading.
4. Finite refinement recovery of the full lifted scalar flux when each
   cell satisfies M area<Pi_Sigma, plus refinement independence and an
   explicit full-turn collision repaired by four cell readings.
5. Exact retention of a changing invertible source under an arbitrary
   invertible calibration correction, without assuming commutation.
6. Literal sine tracking with source advance, prediction and measurement
   error; an invariant branch, cubic-plus-disturbance and contraction
   bounds, vanishing-disturbance convergence and a sharp persistent-drift
   residual floor in the stated scalar sector.

These consume the previously derived counting algebra, radial completion,
Euler functions and native angle unit. The source, target, observation
bank and allowable changes remain declared data. They select no physical
connection, physical clock, unique thermodynamic motion or RH source sign.

## Finite recorded instances

[TVSP_VARIABLE_JYA_RESULT.json](../../proof_lab/TVSP_VARIABLE_JYA_RESULT.json)
and [tvsp_variable_jya.py](../../proof_lab/tvsp_variable_jya.py) contain
**36 exact controls, including 13 negative controls**:

- Six changing rational circular turns, including identity and half-turn
  steps, with seven full orbit-reading banks in different endpoint frames.
  Exact scalar rows and the reconstructed operators obey the variable law.
- A noncommuting four-step chain and a paired-path witness with distinct
  source/target frames. Complete serialized readings recover the path
  defect and the closed return.
- The polynomial count connection
  g=Lambda^2(x^2+xy)+Lambda^3 x. Its complete curvature bank is retained
  through unit degree 3, its horizontal return through degree 3 in each
  step, and its flux has an exact four-cell subdivision identity.
- Four curved-cell and four flat-cell phase banks. The curved source has
  constant f=q, each cell has unit area and bound |omega|<=q<Pi. Both
  coarse endpoints are I, while the decoded lifts are -4q and 0. This
  finite decoder is a quarter-sector instance of the more general proof.
- A noncommuting source-advance/calibration instance, including planted
  failures from dropping the calibration conjugation or source advance.
- Twelve scalar tracking updates from e_0=1 with constant disturbance
  delta=1/100. An independent 90-bisection outward bracket certifies its
  sharp floor S(e_delta)=delta; the final error interval is within 10^-27
  of that root bracket. Its decimal display is approximately
  0.010000166674167112, rather than neutral error.
- Thirty-two updates with disturbance (1/100)/2^n, whose final error is
  below 10^-10; four updates with exactly cancelled source advance,
  whose final error is below 10^-30. These are stated scalar instances,
  not universal iteration counts or improvements of RH eta.

Sine bounds use the SE44 rational alternating remainder and outward
128-bit dyadic rounding. Decimal displays are not proof inputs. The
read-only replay decodes detached banks and checks source-byte pins.

```bash
python3.12 -m proof_lab.tvsp_variable_jya --write
python3.12 -m proof_lab.tvsp_variable_jya --check
python3.12 -m proof_lab.tvsp_native_jya --check
python3.12 -m proof_lab.counting_curvature --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Executed results:

- SE45's 36 controls, local source pins and archive replay pass.
- Unchanged SE44 and SE42 replays pass: 32 and 30 controls respectively.
- All 8 mathematics-navigation tests pass.
- The required full-engine check fails at `tests/verify.cjs --check` with
  the same inherited mismatch recorded in SE41--SE44:

  ```text
  expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
  actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
  ```

The shared engine and previous source/certificate pins were not edited.
No full-engine PASS, independent review, proof-assistant verification or
physical detector validation is claimed. Source authentication, general
written proof and these finite observer readings have separate scopes.

## Boundaries that remain attached

An open chain with forgotten calibration cannot diagnose intrinsic
curvature. A paired return is a stronger target, but an identity-valued
finite loop does not certify flatness. The refined decoder requires a
genuine bound excluding cell-level aliases, or another independently
retained lift. It recovers the scalar integrated flux, not an arbitrary
pointwise curvature field from finitely many cell totals.

Scalar additive flux recovery applies to the declared common-J polynomial
family. General noncommuting sectors require ordered transported data;
no scalar-angle or unrecorded-seam replacement is made. The noncommuting
source-retention theorem is exact, while the analytic tracking theorem
has the specified scalar branch and disturbance hypotheses. A noise
bound or future-source predictor is not inferred from convergence.

Zero remains the typed Cut, distinct from neutral readings and identity
operators. Lambda is not eta. The actual RH source is unchanged: global
eta 1079/2000 with floor 1/492000, eta zero on V_16, and the universal
source sign still open. No mass-gap or universal physics claim follows.
