# SE4 written audit and verification scope

11 October 2026. Owner: Monty Dabas.

## Mathematical audit

| Result | Written verification | Scope |
| --- | --- | --- |
| Gamma packet bound | Digamma difference upper bound 131 xi^2/8; exact derivative energy of u_+/- | Global upper bound, not a source lower floor |
| Prime packet bound | Half-line separation, full multiplier norm and infinite integral tail | Every omitted prime power covered |
| Negative sine witness | Norm-one odd packet, L=16, R=32, N=256; exact rational last comparison | SE3 two-sheet Gamma model only |
| Observer lower bound | Debt/mismatch ratio exceeds 11/6 | Rules out unit contraction; not a claim of infinite norm |
| Finite-complement obstruction | Weak native escape, bounded event energy and source-regular finite projection | Any fixed complement meeting the stated domain hypothesis |
| Central Gamma repair | Match Gamma, prime translations and odd boundary separately to T40 | Declared core normalization, not a new proof of the classical zero formula |
| Bounded source realization | Explicit estimates in the existing T35 graph norm | No source positivity assumed |
| Critical reserve | Equal positive limiting mismatch/debt energy and vanishing finite target | Excludes strict uniform slack; allows critical contraction |
| Boundary escape estimate | Exact Hardy vector tail gives exp(-2r)/2 | Raw boundary tail, not completed-source-relative tail |

The negative packet is H1 and belongs to the displayed source domains.
Odd smooth test-core approximations preserve its strict negative sign.
All proofs retain the declared native pairing, complete prime sum,
Gamma continuum and boundary orientation.

## Exact arithmetic replay

Python 3.12.14 standard-library Fraction arithmetic gives

```text
rho = 123639261423632984455084246171
      / 633825300114114700748351602688
rho < 1/5 < 1/4
rho - 3/2 < -5/4
```

The numerator and denominator are printed on separate lines for reading;
they define one rational number. Reproduce the decisive checks with:

```python
from fractions import Fraction as F
rho = F(655, 4096) + F(9, 256) + F(5, 2**49) + F(1179, 2**99)
assert rho < F(1, 5) < F(1, 4)
assert rho - F(3, 2) < -F(5, 4)
```

This replay verifies the final rational inequalities. The analytic
Gamma estimate, all-prime tail, admissibility and operator implications
are the written proof, not claims established by executing four terms.
No sampled eigenvalue, floating-point sign or new RH numerical
certificate is used.

## Repository validation

Python 3.12.14: all eight mathematics-navigation checks passed. The
13 source pins matched their exact parent blobs and SHA-256 values.
Eighty-seven local links across the new notes and navigation surfaces
resolved. All 21 equation tags were unique; math delimiters, environments,
whitespace and `git diff --check` passed. The exact witness comparison
was replayed with Fraction arithmetic and matched the printed rational.

The required operator check was attempted on Node v24.19.0. It failed
the unchanged first runtime-sensitive pin, as in SE1--SE3: actual
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`,
expected
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`.
The report includes process.version, while the documented engine runtime
is Node 22.16.0. This engine check is **not PASS**. No pins were changed
to bypass it, and no broader mathematical or remote CI success is claimed.

The 1,084 parent files outside the four navigation edits matched the
published SE3 tree byte for byte. The read-only commands were:

```sh
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The engine, original theorem archive and prior development proofs are
outside the write set. Source pins record their exact parent identities.

## Claim boundary

SE4 closes the failed SE3-model contraction search and proves the correct
full odd source factorization and its critical-reserve behavior. It does
not prove the repaired source positive or supply the full five-column
Feshbach sign. No Lean formalization, external review or remote CI PASS
is claimed.

See the [proof](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md) and
[source record](SE4_SOURCE_RECORD.md).
