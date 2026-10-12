# SE48 source and development record

13 October 2026 (Asia/Kolkata). Author: Monty.

Parent: `15626d322dd0a66fd8407f34c9fe845d486bc404`, branch
`agent/rh-source-energy-tail`, Recognition-Kernel-Framework.

## Decision

The user proposed that all zeta zeros should lie on the framework's
diagonal and asked to try completing RH. The first distinction was
between SE47's comparison-kernel zero and an actual zero of xi. The
development therefore attaches a spectral parameter to the actual
logarithmic-derivative response and retains SE47's existing 1+4 output.

The finite positive pencil supplies prospective pole locations. A
separate complete complex-zeta evaluation and a strict local zero-count
test then verify five actual zeros. The same construction identifies
the missing universal condition and proves a controlled limit theorem
under it. This makes a concrete source-to-zero pipeline without assuming
that finite poles already equal all zeros of xi.

No new zero catalogue, new discovery of low-height zeros or mathematical
priority for standard interpolation/Schur/argument-principle mechanisms
is claimed. The contribution is their explicit attachment and executed
observer readings in this programme, with the global limitation retained.

## Native sources consumed

| Source | Use |
| --- | --- |
| [Primitive order](../../../operator_foundation/theory/NATIVE_PRIMITIVE_ORDER.md) and [native algebra](../../../operator_foundation/theory/01_NATIVE_ALGEBRA.md) | Declared pairings and matrix charts follow typed Cut, derived scalars and lawful composition. |
| [SE1](SE1_SHARED_ENERGY_BUDGET.md) | Existing inverse-half energy-domain alternative when a bounded endpoint inverse is unavailable. |
| [SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md) | Corrected bounded source and actual weakly escaping sequence. It proves that the new full-complement eta-zero reference cannot be coercive. |
| [SE21](SE21_COMPLETE_LAPLACE_GRAM.md) | Complete source S_N, positive-real q data, Euler/Mellin remainder and integer-rate density. |
| [SE21 replay](../../../proof_lab/endpoint_zero_shift_laplace_certificate.py), [archive](../../../proof_lab/ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json), [pins](SE21_SOURCE_PINS.json) | Authenticated full arithmetic input. Its 17 inherited source pins are checked by the replay. No zero-location premise enters these data. |
| [SE39](SE39_DIRECT_RH_BRIDGE_AND_ZERO_SECTORS.md) | The actual xi adapter, entire function of t=(s-1/2)^2, exact zero sectors and universal source/RH equivalence. |
| [SE47](SE47_FIVE_SOURCE_OPERATOR_REPAIR.md), [scope](SE47_SCOPE.md), [replay](../../../proof_lab/five_source_operator_repair.py) and [readings](../../../proof_lab/FIVE_SOURCE_OPERATOR_REPAIR_RESULT.json) | Fixed accepted E=span(f_2,...,f_5), bounded moment complement, actual boundary, acquired metric and augmented-source identity. The parameterized family agrees at mu=0. |

The canonical index, preserved register, operator home and exact active
claim boundaries were retained. The shared engine remains solely in
`operator_foundation/`; no historical MP engine was resumed. Old source
and certificate files are preserved. The interval and exact rational
helpers listed in the pins are reused unchanged.

## External primary sources and analytic adapter

1. [Clay Mathematics Institute: Riemann Hypothesis](https://www.claymath.org/millennium/riemann-hypothesis/)
   and its [official problem description by E. Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
   fix the global target: every nontrivial zero has real part 1/2.
   They do not identify our finite comparison seam with that zero set.
2. Mark Embree and A. Cosmin Ionita,
   [Pseudospectra of Loewner Matrix Pencils](https://arxiv.org/html/1910.12153v1)
   (2019), introduction and Section 2. The primary text distinguishes
   exact system recovery from model reduction and displays the Loewner
   and shifted-Loewner construction. This is the established context
   for the finite interpolatory realization; its stability is not
   inferred from midpoint eigenvalues here.
3. [NIST DLMF 5.8.3](https://dlmf.nist.gov/5.8.E3) supplies the Gamma
   modulus product. SE48 splits it at 128 and derives a rational bound
   for the entire complex Euler remainder on the stated disks.
4. [NIST DLMF 1.10](https://dlmf.nist.gov/1.10), Taylor expansion,
   analytic continuation and the phase/argument principle, supplies
   standard complex-analysis context. The local zero-count inference
   is the explicit homotopy proof of Rouche's theorem given in SE48.
   Cauchy bounds and analytic compactness are admitted analytic inputs.

These sources were browsed during the development. The inaccessible
arXiv PDF was not treated as read; its primary HTML text was inspected.
The new derivations are written out rather than justified by a citation
to a broad method. No external review or exhaustive priority search
is asserted.

## Numerical choices and independence

An exploratory 110-digit Decimal Jacobi calculation, on midpoints of
the acquired source matrices, proposed rational pole-bracket endpoints.
Those endpoints are untrusted candidates in the final script. Their
validation uses outward signed LDL inertia only. The runtime needs
Python 3.12 and the standard library; no mpmath, numerical zero table,
complex Gamma routine or floating-point eigensolver is evidence.

The five local zeta centres are the lowest five N=16 pencil candidates.
Their 1e-6 disks are tested independently using the full complex Euler
series, not by comparing against stored known zero values. The proof
uses two different radii: 1/4 for analytic majorants and 1e-6 for the
zero count. The narrower 1e-9 spectral-pole brackets certify a different
object and are not advertised as actual zero-error bounds.

The general convergence proof uses an interior-accumulating node bank,
where interpolation plus local boundedness gives analytic identification.
The executed finite source bank uses the earlier integer rates. These
two roles are explicit; finite execution does not supply all-order signs
for either bank.

The polynomial masking control retains functional-equation and
conjugation symmetry, as well as five positive acquired pencil readings,
but has an off-line quartet. It isolates the logical gap; it is not
presented as a counterexample to the arithmetic zeta function. See
[scope](SE48_SCOPE.md) for execution and the unchanged global frontier.
