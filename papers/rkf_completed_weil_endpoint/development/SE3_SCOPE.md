# SE3 written audit and verification scope

11 October 2026. Owner: Monty Dabas.

## Mathematical audit

| Construction | Check in the written proof | Remaining condition |
| --- | --- | --- |
| Two-sheet compatibility | Parseval isometry; pointwise rank-one projector; full cross-sheet entries | Declared Hardy representation |
| Odd evaluation vector | Direct Fourier evaluation, projection minimality and exact integral | Its chart norm is not a source norm |
| Return to T35 | Native graph Riesz pairing gives B-dagger b = M_X inverse q_b | No graph/Hardy metric identification assumed |
| Arithmetic event analysis | Prime outer products and Gamma oscillator integrals reproduce the pinned mismatch | All events kept; no finite event certificate generated |
| Native debt | Exact pullback d0 B-dagger B, bounded by 2 d0 | Legacy source equality still needs its own normalization |
| Prime translation action | Positive-exponent Fourier translation and confinement factors checked | Weights cannot be discarded after exposing Lambda(n)/sqrt(n) |
| Unbounded domains | Closed compositions, natural domains and explicit common-domain density hypothesis | Endpoint restriction must carry its own domain |
| Regularized observer | Polar decomposition gives a bounded map for every epsilon>0 | No uniform small-epsilon bound assumed |
| Recovery and stabilization | Exact residual; finite-boundary norm convergence; full-target Gram derivative | Joint contraction still open |
| Endpoint equivalence | Uniform contraction on a sequence implies source-relative recovery by the SE2 extension argument | A single positive-epsilon check is insufficient |
| Moving references | Simultaneous unitary covariance of observer and target Gram | Epsilon is not physical time or the eta shift |

The constructed minimum boundary vector and arithmetic rows are explicit
functions, not fitted source coefficients. The other four Feshbach
columns are not evaluated. Source positivity after debt is not used to
define the observer family and is not proved by this stage.

## Numerical sanity check

One independent standard-library Simpson quadrature was used while
auditing the exact boundary integral: 20,000 panels on [0,20], followed
by even reflection, gave 0.08100101247977375. Direct evaluation of the
closed expression gave 0.08100101247977382. This ordinary floating-point
agreement is a normalization sanity check, not an outward enclosure or
an RH certificate. The theorem rests on the analytic integral calculation.
No new numerical test suite or certificate pins were added.

## Repository validation

Python 3.12.14: all eight mathematics-navigation tests passed. Twelve
unchanged local source pins matched the published parent tree and their
SHA-256 records. Seventy-seven local links resolved across the new notes
and navigation surfaces. Twenty SE3 equation tags were unique; math
delimiters, environments and whitespace checks passed. `git diff --check`
also passed.

The required engine check was attempted on Node v24.19.0. It failed at
the unchanged first certificate pin, as in SE1 and SE2: actual
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`,
expected
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`.
That report includes `process.version`; the documented engine runtime is
Node 22.16.0. The engine check is **not PASS** and its pins were not
rewritten. No broader mathematical suite or remote CI run is claimed.

```sh
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The prior 1,084 repository blobs were checked against the published SE2
tree before navigation edits; all matched. Original source and engine
files remain outside this stage's write set.

## Evidence boundary

Written mathematical proofs, repository checks, source provenance,
outward arithmetic, formal verification and external review remain
separate. No new Lean proof, remote CI result, source-floor bound,
five-by-five endpoint sign, RH solution or Yang--Mills mass gap is claimed.

The [main proof](SE3_HARDY_COMPATIBILITY_OBSERVER.md) and
[source record](SE3_SOURCE_RECORD.md) state the exact application scope.
