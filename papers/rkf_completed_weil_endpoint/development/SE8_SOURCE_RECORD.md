# SE8 sources and contribution boundary

12 October 2026. Owner: Monty Dabas.

## Native results reused

The canonical home and native primitive order, T35 native graph pairing,
T40 odd normalization, T28 transported completion, MP Gold 06 and SE2--SE7
are preserved. SE2 already supplies general transport, covariance, joins
and the cofinal observer limit. SE4 fixes the source, SE6 supplies scalar
Gamma/graph bounds, and SE7 supplies the seed comparison and its interval
arithmetic. None is replaced by another operator engine.

The new work explicitly transports the corrected prime--Gamma--pole
source by an admissible dilation, carries its native metric and certifies
the scale 21/20 in the fixed seed chart. An indefinite comparison defect
passes as a full operator although its norm exceeds the old scalar floor.
The resulting coherent observer family covers the whole intermediate
segment by physical subspace inclusion.

## Primary literature checked

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2), Sections
2--6, remains method-level prior art for frequency minorants, Legendre
comparison matrices and tail/coupling certification. No larger-window
certificate or unpublished numerical archive from that paper is imported.
The actual SE8 matrix and constants are recomputed locally.

[Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3)
provides the localized Weil-operator context. Its general results do
not make a finite collection of moving charts a global sign theorem.
The classical special-function identities and their primary NIST sources
remain listed in [SE7's source record](SE7_SOURCE_RECORD.md).

The elementary dilation identities, logarithmic Gamma derivative bound,
native metric estimate, exact pole scaling, interval constants and
observer consistency argument are derived in the SE8 proof. The generic
cocycle and local-to-global principle are explicitly attributed to the
existing repository results, rather than counted again as discoveries.

## Arithmetic provenance

The SE7 matrix is consumed only after its explicit SHA-256 matches the
pinned value. The seed was also fully regenerated under an ambient
90-digit Decimal context. This makes the imported Bessel helper's unary
negation of its at-most-90-digit tail exact; the default 28-digit ambient
context need not preserve every digit when negating a Decimal.

The guarded regeneration produced exactly the same archived seed matrix,
all interval bounds and result. Thus no earlier constants or pins are
changed. SE8 fixes the ambient precision for every replay and uses
copy_negate for its own interval-endpoint sign change. The read-only
`--audit-seed` option reproduces the guarded seed check. This is an
explicit arithmetic audit, not a claim of proof-assistant verification.

Preliminary scipy calculations proposed c=21/20. Only the outward-rounded
replay, analytic quadrature bound and complete infinite-tail estimates
support the stated lower bounds.

See the [proof](SE8_MOVING_OBSERVER_AND_SIGNED_TRANSPORT.md),
[audit](SE8_SCOPE.md) and [pins](SE8_SOURCE_PINS.json).
