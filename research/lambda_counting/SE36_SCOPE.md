# SE36 scope and verification

12 October 2026. Owner: Monty.

The certificate is the saved observer reading decoded for its stated
target. The observer applies only the supplied probes or catalogue
words to the unknown input and records the sensor readings. Each
decoder reads only those recorded readings, the supplied sensors and
actions, and the derived response matrices. Replay and source records
document the readings; they are not independent certification conditions.

| Assertion | Scope of the written proof |
| --- | --- |
| Restricted signature | Theorem 1: for a supplied polynomial of degree at most d, the probe grid {0,...,d-1}^k determines every restricted translated reading; its fibres need not be cosets |
| Affine catalogue closure | Theorem 2: the response span stabilizes within (SE36.9) strict increases; the basis protocols and descended matrices (SE36.11) determine every future allowed reading |
| Separating word | Corollary: the first closure stage separating a supplied pair gives a shortest separating word |
| Synthesized translations | Theorem 3: available reversible linear actions conjugate translations into the stable span H_* within n-dim H_0 increases |
| Nonlinear actions with affine cut | Theorem 4: E_(d,q,b) is preserved and the retained closure is finite at each unit depth, within (SE36.20) |
| Moving observer | (SE36.26)-(SE36.27), and transport of the update by a response basis change |

Four written derivations establish the general results. The executable
records 30 exact checks, including 9 negative controls. Coefficients
are exact canonical fractions arranged by retained unit degree; readings
are archived as counting states whose label is the output channel and
whose unit degree is the retained layer. The SE35 bank construction is
used unchanged for full-translation blind subspaces. It is a
counting-specific application, not a second shared engine.

The saved observer certificates are:

- The restricted signature of u^2+v^2 under horizontal probes,
  decoded to u and v^2.
- The cubic response u^3+v under unit u-shifts: three recorded basis
  protocols, their descended matrix, and predictions of the readings after
  3, 7 and 11 shifts, which match the recorded readings; u is decoded
  linearly and v by the polynomial decoder F-u^3.
- The swap-and-shift catalogue: the readings F(x), F(Tx), F(TJx),
  decoded to both coordinates (SE36.17), and the separating witness word.
- Synthesized translation directions for a three-cycle permutation.
- The unit action g=x+Lambda x^2 at q=2: recorded basis protocols and
  predictions after 3, 4, 7 and 12 repetitions.
- The sign branch for F=x^2 separated by the next unit coefficient.

A final check re-decodes the archived certificates from their saved JSON.

Further positive checks cover the restricted fibre {(u,v),(u,-v)}
against SE35's null full-translation blind subspace; off-grid prediction
for a three-coordinate, two-output, two-direction probe family and the
k=0 signature; equality of retained readings exactly when future readings
agree; closure of the swap-and-shift catalogue to the full state; the
conjugation identity (SE36.13) and JTJ as vertical translation; the
stated matrix (SE36.22); the closure dimension 9 equal to (SE36.20);
preservation of E_(d,q,b) by a two-coordinate action with b=3; the
iterate formula (SE36.24) for N=0..12; moving and held calibration
updates for the affine and nonlinear examples; and basis change S M S^-1.

Negative controls cover fibres that are not cosets of a fixed line;
omitted or duplicated probe rows; x^2 and x^3 recovering x without a
polynomial decoder; no finite closure for the nonlinear cut x->x^2; the
shift-only catalogue failing to separate the sign pair; refusal to use
an unavailable inverse; the iterate formula failing before the cut;
the initial sensor missing the sign; and a held observer without its
calibration correction.

Rational amplitudes belong to the translation protocol of Theorem 1.
Unit multiples of a recorded reading are formed from that same reading.
No unavailable action, inverse or extra detector is added. The section 7
connection to SE34 and SE35 is a written remark relying on those
certificates; it is not separately replayed here.

No closure for actions with nonlinear cut, single finite observer for
the infinite unit tower, minimum nonlinear observer, global experimental
budget or noisy-data recovery is asserted. Zero remains the stated
typed cut; coordinate nulls are separately typed additive neutrals. No
primitive metric, RH result or curvature development is asserted.
Pullbacks, invariant-span closure and conjugated translations carry no
claim of novelty priority. Formal proof-assistant verification and
external review are not claimed.

Reproduction uses Python 3.12 and Node v22.22.0:

```bash
node proof_lab/lambda_action_closure.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Read-only application replay reproduces the JSON archive byte for byte
and checks the SE36 source manifest. The whole-engine command result is
recorded in the source record.
