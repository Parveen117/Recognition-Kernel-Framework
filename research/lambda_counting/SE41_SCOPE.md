# SE41 scope: native return feedback and retained source

13 October 2026 (Asia/Kolkata). Owner: Monty.

## Written results

The [theorem](SE41_ORDERED_RETURN_AND_MOVING_CUT_FEEDBACK.md) supplies five
derivation groups on the stated carriers:

1. Complete labelled cut/complement readings recover a finite return.
   On a rank-d complex cut module, d+1 distinct central phase calibrations
   contain an invertible Cayley chart. The actual source product is kept.
2. A unitary return has skew Cayley coordinate T. The rational correction
   is Psi(T)=-T^3(I-2T^2)^(-1), with norm at most r^3/(1+2r^2) for r=||T||.
   The observer calibration B learns the **unchanged** ordered return U_*,
   with BW=U_* at every step. It does not turn U_* into the identity.
3. The update intertwines with moving invertible frames and their transported
   pairings. A complete bank can use a different orthogonal cut at every
   step. The ordered word, chart record and winding lift remain distinct
   memory data. NT-6's complement-return formula is retained.
4. A skew-reading error epsilon bounds the next unitary residual error by
   epsilon. With a verified chart margin m>epsilon, Cayley-coordinate error
   is at most 2 epsilon/[m(m-epsilon)]. This is a one-step noise result,
   not convergence to an exact answer under persistent noisy readings.
5. For formal unit order at least m>=1, the next residue has order at least
   3m. With the cut calibration already known, 3^k m>N suffices for exact
   reconstruction at retained unit depth N. This is an algebraic statement,
   separate from numerical convergence at nonzero Lambda.

Native algebra and the positive response pairing precede the admitted
finite coordinate adapter. The norm estimate explicitly uses finite
positive spectral calculus. No ordinary Hilbert space or physical clock
is used as a primitive. The existing shared engine is unchanged.

## Observer readings executed

The Python 3.12 replay passes **26 exact controls, including 9 negative
controls**. The saved packet contains detached accepted and complementary
probe readings, their cut and frame, the ordered source word, evolving
calibration/residue pairs, exact bounds, branch-chart tests and formal
memory orders. Its decoder consumes those serialized readings.

The supplied noncommuting word uses the native R and central-iota K
generators in a faithful two-complex-channel representation. Its reverse
has the same spectral power traces and a different full return. Three
steps change both cut and observer frame while retaining the source.
The actual matrix inequalities are checked by exact rational inertia,
not a floating-point eigensolver. A two-channel return blocks the first
two phase charts and accepts the third, realizing the stated finite
candidate bound in this instance.

Other controls detect missing complement data, antipodal sine silence,
an omitted between-frame transport, a wrong calibration factor, the
NT-6 hidden-return cancellation, a nonunitary hyperbolic expansion,
and endpoint loss of winding. A noncommuting skew noise example verifies
the actual update order, residual error and chart-margin bound. The
formal witness has noncommuting coefficients at Lambda and Lambda^2;
its orders are 1,3,9 and then beyond retained depth ten.

These are supplied mathematical sensor fixtures, not physical instrument
measurements. The general proofs and finite replay scopes are distinct;
no proof-assistant verification or independent external review is claimed.
Source pins bind the local inputs and new proof/application/readings;
the external NT theorem is referenced at an immutable Git blob, not
downloaded as a runtime dependency or silently recertified.

## Reproduction

```bash
python3.12 -m proof_lab.ordered_return_feedback --write
python3.12 -m proof_lab.ordered_return_feedback --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Executed validation:

- The read-only replay matched all 18 local source pins and the saved
  observer readings: 26 exact controls, including 9 negative controls.
- The mathematics-navigation suite passed all 8 tests.
- The required full-engine check failed at `tests/verify.cjs --check`
  with the same inherited pin mismatch recorded by SE40:

  ```text
  expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
  actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
  ```

The engine and its certificate pins are unchanged. The complete engine
suite is not reported as passing; SE41's independent application replay
and the written theorem have the distinct scopes described above.

## Application boundary

The finite theorem requires a source return that is unitary in its
declared native positive pairing, available full readings or a proved
faithful decoder, and permission within the model to change the observer
calibration. General native nonunitary transport does not satisfy its
global contraction assertion; the hyperbolic negative control shows why.
The finite chart count supplies no dimension-free infinite-carrier
or noise-margin theorem. The bank is sufficient, not claimed minimal.
An exact full bank already permits direct calibration B<-BW=U_*.
The new result is the stated incremental update and its bounds; it
does not extract an unknown source from fewer observations.

For thermodynamics, the prior constitutive memory M and the algorithm's
learned calibration B have different roles. The source connection A-M
and its curvature stay fixed. A vanishing learned residue does not prove
physical flatness, erase a seam distribution, or convert one loop reading
into an entire curvature field. Identical endpoints still need retained
path/lift memory for targets distinguishing their histories.

The two uploaded notes are research motivation, not theorem dependencies.
Their false scalar d(d log)=curvature identification and integer-phase
exponential claim are not used. Atomic quantization is not established.

The RH source S_b is unchanged. SE27's global eta=1079/2000 with floor
1/492000 and SE21's V_16 eta-zero certificate remain the actual bounds.
SE39's universal positivity condition and SE40's actual all-order source
reading problem are still open. Lambda-memory order, return calibration
and the spectral shift eta are not identified.
