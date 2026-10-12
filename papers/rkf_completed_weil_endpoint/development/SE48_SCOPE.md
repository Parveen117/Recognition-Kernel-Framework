# SE48 proof scope and observer readings

13 October 2026 (Asia/Kolkata). Author: Monty.

## Written proof scope

[SE48](SE48_DIAGONAL_SPECTRAL_PENCIL.md) proves four theorem groups:

1. The actual source supplies J=S_N/4 and a second response form L.
   When both finite forms are positive, their acquired-metric operator
   has simple positive eigenvalues. Its rational response has positive
   residues, negative poles and exact value/derivative interpolation.
2. The same SE47 boundary-plus-four construction admits a spectral
   parameter, with an exact determinant identity and kernel lifting.
   Reference poles must cancel correctly. The full eta-zero reference
   is necessarily noncoercive by SE5's escaping sequence; a global
   bounded inverse is not an available endpoint premise.
3. Positivity at every order on a declared interior-accumulating probe
   sequence is equivalent to RH. Positive response residues give local
   boundedness and analytic convergence, which excludes off-axis poles.
   This proves the implication and equivalence, not the universal signs.
4. Complete complex Euler readings, an explicit Gamma-ratio tail,
   Cauchy remainder and a strict Rouche inequality certify one simple
   actual zeta zero per disk. Reflection then forces its real part to
   equal 1/2 exactly.

The classical analytic adapter is explicit: completed xi, its functional
equation and zero correspondence, complex analytic continuation, Cauchy
estimates, normal-family compactness and the argument principle. They
are applied to the native acquired source; they are not silently renamed
as primitive cuts. Lambda, eta and the new spectral parameter mu remain
distinct. No general novelty claim is made for Loewner realization,
Schur complements, Stieltjes approximation or Rouche's theorem.

## Finite actual-source evidence

[diagonal_spectral_pencil.py](../../../proof_lab/diagonal_spectral_pencil.py)
and [DIAGONAL_SPECTRAL_PENCIL_RESULT.json](../../../proof_lab/DIAGONAL_SPECTRAL_PENCIL_RESULT.json)
record **36 controls, including 8 negative controls**, using Python
3.12 and the standard library. All source intervals retain the unchanged
90-digit outward implementation and SE21's full prime, Gamma and pole
tails. No zero catalogue or assumed RH factorization is an input.

- L_N and J_N are strictly interval-positive for N=5,8,12,16.
  Their exact displacement identities have consistent interval readings.
  Positivity plus the written theorem locates all poles of each finite
  response on the negative real t axis, with nonzero positive residues.
- Signed interval LDL proves 30 disjoint pole-ordinate brackets of
  radius 1e-9: every pole for N=5,8,12, and the lowest five for N=16.
  Midpoint diagonalization only proposed the rational endpoints; it
  is not the evidence for their signs or counts.
- The narrow sixth N=16 bracket remains inconclusive with inherited
  precision. The failing pivot crosses zero. No source-sign failure
  or false high-precision pole enclosure is inferred from this.
- The exact rational controls cover value/derivative interpolation,
  recovery of a finite atomic source, nonunit residues, moving-probe
  covariance, the existing 1+4 characteristic identity, reference-pole
  cancellation and a symmetric off-line quartet hidden by five positive
  readings. A polynomial control shows why a centre and derivative
  alone cannot certify the zero count without the remainder.

The 16-state internal pencil still uses five output labels after SE47's
reduction. It is a meromorphic five-matrix family, not a claim that a
constant degree-five determinant contains infinitely many zeros.

## Five actual local zero certificates

The actual-zeta test consumes both complex components of the function
and derivative. It uses 320 Euler terms, a complete complex remainder
less than 1e-56, outer radius 1/4 and proved outer bound |zeta|<1000.
Outward scaled Taylor series compute every exponential. Exact rational
endpoints, enclosures and Rouche margins are in the archive.

| Centre ordinate | Disk radius | Proved lower Rouche margin |
| --- | --- | --- |
| 14.134725141735 | 1e-6 | greater than 7.67e-7 |
| 21.022039638772 | 1e-6 | greater than 1.09e-6 |
| 25.010857580146 | 1e-6 | greater than 1.27e-6 |
| 30.424876126791 | 1e-6 | greater than 1.10e-6 |
| 32.935061722570 | 1e-6 | greater than 8.86e-7 |

Each disk contains exactly one simple nontrivial zero, with real part
exactly 1/2 by uniqueness and reflection. The five disks are disjoint.
No count of all lower-height zeros is run, so these are not certified
as the first five zeros in a global ordering. Their certified ordinate
error is 1e-6, not the distinct 1e-9 pole-bracket radius or the number
of displayed centre digits. This is a local computational proof using
the stated analytic bounds, not new zero-discovery, formal Lean
verification or independent external review.

## Replay and execution record

```bash
python3.12 -m proof_lab.diagonal_spectral_pencil --write
python3.12 -m proof_lab.diagonal_spectral_pencil --check
python3.12 -m proof_lab.five_source_operator_repair --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

- The read-only replay passes all 36 controls, including 8 negative
  controls, and matches its saved archive. All 25 local pins match;
  the 20 inherited pinned source blobs match the published parent.
- The unchanged SE47 replay passes its 29 controls and archive comparison.
- All 8 mathematics-navigation tests pass. Every new SE48 local document
  link resolves. The source and actual-zero certificates retain their
  separate scopes as stated above.
- The required full-engine check was run and retains the inherited
  failure at `tests/verify.cjs --check`:

```text
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
```

The shared engine, historical sources and previous pins are unchanged.
No full-engine PASS is claimed.

## Remaining global condition

One must prove the actual positive-pencil condition at every refinement,
or establish an equivalent unconditional global source inequality.
The analytic convergence conclusion has been proved from that condition;
the condition itself has not. The interior-accumulating sequence used
in the written limit theorem differs from the finite integer-rate bank
used in the execution. The integer-rate all-order criterion remains
available through SE21/SE39.

Finite positive pencils, reflection symmetry, a matching comparison seam
and finitely many certified actual zeros do not establish this missing
all-order statement. The exact off-line control verifies that failure
of inference within the same finite observation architecture.

The full source remains at global eta=1079/2000 with floor 1/492000.
Eta-zero source positivity is still certified on V_16 only. RH and the
global eta-zero endpoint remain open. No mass-gap claim follows.
