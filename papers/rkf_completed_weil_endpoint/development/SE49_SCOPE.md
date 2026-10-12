# SE49 proof scope and observer readings

13 October 2026 (Asia/Kolkata). Author: Monty.

## Written scope

[SE49](SE49_OBSERVER_INNOVATION_AND_CONVERGENCE.md) proves four
theorem groups in the existing admitted representation:

1. Two scalar Schur innovations, alpha and beta, are necessary and
   sufficient for a new actual observation to preserve positivity of
   both acquired forms. The exact derivative window, response update
   and positive denominator bound retain all cross readings.
2. Each finite positive actual pencil has an explicit response-error
   bound against actual q on Re w>1, using the full Euler-product
   half-plane and the double interpolation zeros. No sign at later
   orders or RH premise is needed for this finite theorem.
3. On the actual integer-rate bank, positivity at all orders gives
   a locally uniform response limit on Re w>0 with an explicit
   finite-product tail. It is equivalent to RH. This is conditional
   on universal signs, not a proof of those signs. No interior
   accumulation point or bounded global reference inverse is needed.
4. An exact invertible triangular change of observation coordinates
   permits an outward sign certificate and recovery of the original
   scalar innovations. Midpoint arithmetic only proposes coordinates.
   This supplies the executed extension to V_24.

Native primitive order, the original Cut semantics, actual source,
boundary column and accepted four-space remain unchanged. Standard
Schur, Schwarz, complex continuation and congruence arguments are
explicit analytical adapters. They are not newly assumed native
axioms or a reason to erase an unobserved source sector.

## Executed complete-source evidence

[observer_innovation_convergence.py](../../../proof_lab/observer_innovation_convergence.py)
and [OBSERVER_INNOVATION_CONVERGENCE_RESULT.json](../../../proof_lab/OBSERVER_INNOVATION_CONVERGENCE_RESULT.json)
record **32 controls, including 9 negative controls**, under Python
3.12. All certificates use exact rational inputs and the unchanged
90-digit outward interval arithmetic. The 120-digit midpoint proposal
does not certify a sign.

- L_24 and J_24 are strictly positive, hence so are all their leading
  restrictions. The 48 original scalar innovations have strictly
  positive interval lower bounds. All 24 actual derivative enclosures
  lie strictly inside their paired admissibility windows.
- Eta-zero positivity on the actual source extends from V_16 to
  V_24. The old leading source box is byte-identical. Eight additional
  states use actual complete jets at s=19,...,26, with no prime,
  Gamma, pole or spatial truncation substituted for an analytic tail.
- Separate Gamma, prime and full-pole assembly agrees on every new
  mixed source entry. The complete arithmetic input includes a ninth
  new reading at s=27 for independent response verification.
- Direct interval elimination fails to decide L pivot 17 and J
  pivot 18. Both failures are retained. Outward congruence resolves
  them positively, with normalized row margins greater than
  0.9999999642 and 0.9999999997 respectively. These margins and the
  original pivots are not native spectral gaps.
- At the held-out s=27, all six N=5,8,12,16,20,24 fitted responses
  satisfy the independently evaluated analytic error bounds. The
  direct N=24 absolute q-error enclosure is below 8.905e-60; the
  wider written bound there is below 2.149e-27. These are single-point
  response errors. The last direct error interval straddles zero.
- SE47's written finite augmented congruence transfers S_24>0 to
  K_(5,24)(0)>0 with the same four accepted states and boundary
  column. This is a theorem consequence, not a new direct entrywise
  five-gap enclosure. The internal state count is 24; output labels
  remain five.

The nine negative controls cover separately violated L and J
innovations despite positive diagonals, moving a pencil without its
probe, replacing value/derivative interpolation by value-only data,
claiming decay on the diagonal boundary, assuming any unbounded node
bank suffices, crossing the half-plane domain, accepting a planted
negative direction, and mistaking inconclusive raw interval pivots
for negative source witnesses.

## Read-only validation and provenance

The archive is regenerated deterministically by:

```text
python3.12 -m proof_lab.observer_innovation_convergence --check
```

The local source manifest binds 31 files: 26 unchanged published inputs
and the five new stage files other than the manifest itself. The
inherited SE21 check verifies its 17 old pins. Read-only regeneration
matches the new archive, with all 32 controls passing. No old source
file or certificate is repinned to make a failing check pass.

The required mathematics navigation suite passes all eight tests:

```text
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The required shared-engine check was run:

```text
node operator_foundation/verify_all.cjs --check
```

It fails at the inherited `tests/verify.cjs --check` pin mismatch,
with expected SHA256
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`
and actual SHA256
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`.
These are the same pre-existing hashes reported in SE48. No shared
engine file is changed, no full-engine PASS is asserted, and the
failure is not repaired by overwriting a pin. Formal/Lean proof and
independent external review are not claimed.

## Unchanged global boundary

No all-order alpha/beta sign theorem, full eta-zero source sign,
RH proof or Yang--Mills mass-gap result is established. The global
source bound is still

\[
 S_b+(1079/2000)I_X\succeq(1/492000)I_X.
\]

The finite frontier is now V_24. The 24 positive pairs do not imply
the 25th pair or the infinite sequence. The explicit convergence rate
on Re w>0 requires the universal positive sequence to exist. The
unconditional finite comparison with actual q is on Re w>1 only.
Neither estimate is a uniform bound on the critical-line boundary.
SE48's noncoercive global reference and finite-data masking example
remain applicable. No new actual zero disks or global zero ordering
are certified here.
