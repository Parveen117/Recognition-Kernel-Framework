# SE21 source and route record

12 October 2026. Owner: Monty.

Parent commit: `e612cc0ad48d7fcd023268f279fad235836b0838` on
`agent/rh-source-energy-tail`; parent tree
`1ec591ec7af8d7b4ba1cbc40512149c8d949b96c`.
The latest user instruction explicitly asks for certification; this
stage resumes numerical verification after the SE19--SE20 written work.

## Decision and actual development

SE20 excludes reaching eta zero by the selected fixed-Gamma diagonal
seed, and excludes any fixed uncompensated prime cutoff on the whole
carrier. This stage therefore retains the complete source and evaluates
its signed cancellations on unbounded-support Laplace observations.
The aim is direct eta-zero evidence with every mixed reading and tail
attached. No decimal shift tuning is promoted as endpoint completion.

The added results are the exact source matrix in terms of the positive
real logarithmic derivative of xi, native-graph density of the discrete
integer-rate observation family, a proved Euler-transform derivative
remainder, and an executed sixteen-direction zero-shift certificate.
The all-order matrix condition is equivalent to the old source sign;
its reformulation is not a solution of that condition. A finite matrix
PASS does not provide the unobserved complement's Schur sign.

## Consumed repository mathematics

| Source | Use |
| --- | --- |
| T35 and T40 through SE4 | Unchanged admitted graph, complete odd source and Fourier normalization |
| SE4.3, SE4.15--SE4.17 | Gamma bound and bounded native source |
| SE5.1--SE5.2 | Native pairing and distinction between mismatch positivity and source positivity |
| SE13.5 and its native core argument | Dense compact odd core; no uniform finite-observer conclusion |
| SE16.4 and SE20.7 | Complete digamma series and odd Gamma kernels |
| SE20.2, SE20.5--SE20.10 | Exact pole, all-prime event measure and complete continuous-reference cancellation |
| SE20.17--SE20.22 | Open universal arithmetic condition and finite-cutoff obstruction |
| SE7 interval primitives | Immutable outward Decimal arithmetic, Machin pi and logarithm enclosures |
| SE15 integer_log | Immutable binary logarithm range reduction |
| SE11 refined_constants | Independent older constant enclosure used only as a test oracle |

Earlier theorem and result files are preserved. New source pins bind
the added proof, replay, result and controls to the consumed files.

## Classical references and no priority claim

The following primary NIST DLMF pages were inspected on 12 October 2026:

- [25.2](https://dlmf.nist.gov/25.2), equations 25.2.3, 25.2.6--7 and
  25.2.11: alternating zeta, derivative series and the Euler product.
- [25.4.4](https://dlmf.nist.gov/25.4.E4): normalization of xi.
- [5.7](https://dlmf.nist.gov/5.7): digamma series.
- [5.8.3](https://dlmf.nist.gov/5.8.E3): the exact Gamma modulus product
  used in the Cauchy remainder estimate.
- [5.11](https://dlmf.nist.gov/5.11): digamma asymptotics and real-positive
  remainder bounds; the conservative bound used here is also justified
  directly by its periodic-Bernoulli integral.
- [25.5](https://dlmf.nist.gov/25.5): Mellin integral context.

Euler acceleration, divided-difference kernels, Gamma recurrences,
Cauchy derivative estimates and interval LDL are classical methods.
Their exact attachment to this source and the executed packet are the
contributions claimed here. No priority for a general Loewner/xi or
RH criterion is asserted. Searches also returned purported RH proofs;
none is adopted or used as evidence.

## Reproduction

From the repository root under Python 3.12:

```bash
python -m proof_lab.endpoint_zero_shift_laplace_certificate --check
python -m unittest proof_lab.test_endpoint_zero_shift_laplace_certificate -v
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The source replay and Python tests pass; the final engine command
retains its pre-existing pin-mismatch failure, documented in
[SE21_SCOPE.md](SE21_SCOPE.md). No engine files or old pins are changed.
No proof-assistant or independent external review is claimed.
