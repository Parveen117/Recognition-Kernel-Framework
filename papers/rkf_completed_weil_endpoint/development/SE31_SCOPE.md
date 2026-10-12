# SE31 scope and verification

12 October 2026. Owner: Monty.

Certification is the declared observer reading, interpreted for its
stated target. The archive records the full response coefficients,
retained unit layers and decoded operator for its supplied example.
Exact replay, source integrity and negative controls are records about
that reading, not independent mathematical certification conditions.

| Assertion | Evidence and exact scope |
| --- | --- |
| Normal order and incremental operator recovery | Theorem 1; the declared polynomial operator algebra on Q[Lambda,x] |
| Number of probes | p_0 through p_r for D-order at most r; each response is a complete polynomial |
| Sharpness | The supplied prefix fails without its last response; no universal scalar-measurement minimum is claimed |
| Typed operator cut | Theorem 2; degree-zero formula cut with kernel Lambda W_Lambda |
| Full family recovery | Retain through the declared Lambda-degree of the normal coefficients |
| Ordered Euler products | Theorem 3; formal coefficient identities, central factor preserved |
| Ordinary translation bridge | Theorem 4; locally finite polynomial action and regular logarithmic generator |
| Finite matrix windows | Theorem 5; explicit top-boundary defect and word-height guard |
| Curvature | Not used or developed |
| Actual RH source | SE27 eta=1079/2000 and native floor 1/492000 unchanged |

The five written theorems give the general arguments. The executable
application contains 27 exact checks, including ten negative controls.
It imports the unchanged canonical coefficient, Laurent and Pāṇinian
engines and SE30's existing counting operators. The presentation
DX -> XD+I and central Lambda rules have their critical pairs checked;
normalization is performed by the shared compiler, not a new engine.

Finite checks cover normal ordered powers through degree six; recovery
orders through five at four nonzero rational unit steps; a family with
unit-memory degree three; ordered exponential coefficients through
bidegree (6,6); formal loop coefficients modulo t^9; translation of
polynomials through degree nine; windows through N=8; and 252 guarded
word/input pairs of word length at most five. An exact full response
prefix reconstructs coefficients and predicts separately tested higher
probes. These tests do not replace the all-order proofs.

The negative controls expose missing last probes, unspecified operator
order, substitution of an ordinary product for the transported product,
lost unit layers, insufficient memory depth, invalid memory depth,
erased central ordering factors, counting-flow/translation confusion,
false finite Weyl representations and an unguarded top-boundary loss.

No bound on noisy-data amplification, recovery of arbitrary operators,
infinite-order tail control, bounded realization, analytic exponential
convergence, physical interpretation, proof-assistant verification or
external review is asserted. T55's EMK algebra and this counting Weyl
algebra retain different defining relations. The historical RH interval
archive is read and pinned, not recomputed; no new eta is supplied.

Reproduction uses Python 3.12.14 and Node v24.19.0:

```bash
node proof_lab/endpoint_counting_operator_recovery.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The application replay reproduces its archived JSON byte for byte and
checks the source manifest. All eight mathematics navigation tests pass.
Publication includes six new files and four navigation updates, with
inherited source pins checked and all other parent blobs preserved.

The required whole-engine run reproduces the inherited first-suite
failure in `tests/verify.cjs --check`: expected
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`,
actual
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`.
Later suites do not run. No engine source or certificate is repinned
to turn this into a PASS. This application exercises its stated engine
paths directly; the whole engine is not claimed to pass. That inherited
aggregate-gate failure is reported separately and does not block this
observer-reading packet's publication.
