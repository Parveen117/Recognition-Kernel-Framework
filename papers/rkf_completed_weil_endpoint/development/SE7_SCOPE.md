# SE7 audit and verification scope

12 October 2026. Owner: Monty Dabas.

## What the combined proof and calculation establish

| Object | Evidence | Conclusion |
| --- | --- | --- |
| Corrected odd source on radius 1/2 | Exact support identity, full negative pole, Gamma envelope | The frequency minorant lies below the actual source |
| Forty-mode leading block | Enclosed 8-node quadrature, analytic error, forty positive interval LDL pivots | Exact integral block >= I/20000 |
| Entire discarded basis | Rational Bessel tails and mixed-block norm bounds | Comparison form >= I/25000 on all odd L2 states |
| Native source | SE6 graph inequality with the physical floor | S >= 2I/903127 on X_(1/2) |
| SE6 fifteen-moment Schur form | Exact minimizing identity and native orthogonality | F_15 >= 2I/903127; entries not calculated |
| Local joint observer | Full target, mismatch bound N_*<=11I/2 | Squared contraction reserve 4/9934397 on X_(1/2) |

The infinite-dimensional statement uses the analytic proof as well as
the finite arithmetic. A finite PASS alone is not presented as a
universal theorem. The carrier remains the admitted T35 representation
with native dagger and graph norm, not an independently chosen metric.

## Replay and controls

Run `python proof_lab/endpoint_full_aperture_certificate.py --check`.
It regenerates every enclosed matrix entry and all forty LDL pivots,
then requires exact equality with the archived matrix and result.
The matrix is SHA-256 bound in the result. `--write` is for creating a
new stage record, not for bypassing a failed read-only replay.

The four independent arithmetic controls exercise interval operations
against exact endpoint rationals, all sixteen Gauss moments, the
downward Bessel recurrence against the direct trigonometric j_1
formula, and rejection of positive diagonals with a negative Schur
coupling. They do not replace the analytic proof.

Under Python 3.12.14 the full read-only replay reproduces the archived
matrix and certificate exactly. All four arithmetic controls, eight
navigation tests and the preceding SE6 twenty-five rational checks
pass. Nineteen parent-source pins and four new arithmetic pins match.
The 1,098 parent blobs outside the four navigation edits are unchanged.

The required `node operator_foundation/verify_all.cjs --check` was run
and failed the existing first runtime-sensitive pin under Node v24.19.0:
actual 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e,
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The engine records process.version and documents Node 22.16.0, which
is unavailable here. This check is not PASS; no engine files or pins
were changed. Local checks are not remote CI or external review.

## Boundaries

The certificate covers all complex odd states of the radius-1/2 native
aperture, including the fifteen directions removed in SE6. Smaller
apertures inherit this bound. Larger apertures do not inherit it.

The all-aperture exhaustion, the global norm-one observer and eta=0
completed-source sign, the historical five-source endpoint, K0 and RH
remain unproved by this packet. No formal proof-assistant verification,
external mathematical review or remote CI success is claimed.

See the [proof](SE7_FULL_PRIME_ACTIVE_APERTURE.md),
[source record](SE7_SOURCE_RECORD.md) and [pins](SE7_SOURCE_PINS.json).
