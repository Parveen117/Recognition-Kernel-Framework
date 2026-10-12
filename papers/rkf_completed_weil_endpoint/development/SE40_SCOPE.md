# SE40 claim and validation scope

12 October 2026 (UTC). Owner: Monty.

## Written mathematics

The [proof](SE40_CYCLIC_OBSERVER_AND_ANALYTIC_MEMORY.md) contains five
theorem groups on the existing admitted native graph carrier:

1. An explicit odd weighted Green action A_tau, with norm at most
   1/(tau-9/4), its whole-carrier resolvent identity and exact transport
   between any positive-rate calibrations.
2. A cyclic state family A_tau^n v_tau whose finite spans are dense in
   X, with an exact polynomial recurrence and norm-convergent local
   Taylor interpretation.
3. A Hankel reading rule: N tower directions have their full mixed
   Gram determined by 2N-1 scalar response coefficients, and
   A_tau^dagger S_b=S_b A_tau. Positivity is not a premise or conclusion
   of this source-symmetry identity.
4. Geometric state and mixed-source truncation bounds, plus a finite
   coefficient-error budget retaining all mixed terms.
5. Actual constants ||A_(25/4)||<=1/4, ||v_(25/4)||<2 and
   ||S_b||<43/12, together with moving-calibration coefficient transport
   and explicit tails. A supplied formal unit series therefore admits
   analytic evaluation inside its proved disk.

The tail bounds apply to declared analytic probes and their coefficient
budgets. They do not uniformly approximate the identity on the X unit
ball, locate the optimal eta, or convert an arbitrary finite positive
bank into global positivity. The 2N-1 count is algebraic response data,
not a universal bound on measurement shots, derivative acquisition
cost, conditioning or noisy reconstruction.

## Executed readings

The Python 3.12 application records sixteen exact controls. They include
eight actual state polynomials and 32 independent rational Fourier
readings, seven coefficients decoding a four-by-four mixed model Gram,
moving-calibration tails, overlap transport, finite measurement error,
and negative controls for source positivity. The response models are
explicitly supplied polynomials; they are not new actual xi derivative
certificates. No new actual xi Hankel minor is claimed positive.

The written arguments establish the universal identities within their
stated carrier. The finite controls check specified readings and
normalizations, not those universal proofs. No formal proof-assistant
verification or independent external review is claimed.

## Reproduction and checks

```bash
python3.12 -m proof_lab.endpoint_cyclic_observer_controls --write
python3.12 -m proof_lab.endpoint_cyclic_observer_controls --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The application and its read-only replay pass all sixteen controls;
the saved readings agree exactly. All eight mathematics-navigation
tests pass. The full engine check fails at the inherited
`tests/verify.cjs --check` pin mismatch:

```text
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
```

The engine and its pins are unchanged. This failure is recorded
separately from the successful new controls; no global engine PASS
is inferred.

## Unchanged endpoint

SE39 and the dense cyclic family imply RH is equivalent to positivity
of every actual Hankel Gram. That universal sign remains unproved.
SE27's global eta=1079/2000, native floor 1/492000 and SE21's finite
V_16 eta-zero certificate remain unchanged. This new tower's first
sixteen directions are not V_16; the old certificate is not transferred
to them. The canonical SE29 curvature norm remains 1/2, and the
historical five-label attachment retains its previous boundary.

No Lambda-to-eta identification, RH proof, global eta-zero certificate,
new full-engine PASS or automatic promotion of earlier formal counting
results is asserted. Existing certificates and pins are preserved.
