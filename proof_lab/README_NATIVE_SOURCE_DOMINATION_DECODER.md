# Native Source-Domination Decoder Stage 3B

Stage 3B proves that a coefficientwise event-phase reconstruction is not needed
once the actual boundary is represented in the same native chart as an actual
Loewner lower bound for the source.

## Native chain

```text
complete event analysis Xi
+ actual common chart J
+ source symbol A with Xi*Xi >= J*A*J
+ actual boundary density b in the same chart
-> |L(f)|^2 <= beta_A ||Xi f||^2
-> canonical decoder c_partial in closure(Ran Xi)
-> cut covariance and relative reserve.
```

The scalar-floor corollary is

```text
A(x) >= s(x) I
-> beta_A <= integral ||b(x)||^2 / s(x).
```

This is orientation-safe only after the common-chart boundary identity is
proved. The tests include a source-blind boundary negative control.

## Files

```text
theorum/34_native_common_chart_decoder_transfer.md
proof_lab/native_source_domination_decoder.py
proof_lab/test_native_source_domination_decoder.py
proof_lab/NATIVE_SOURCE_DOMINATION_DECODER_EXPECTED.sha256
proof_lab/imported/NATIVE_WEIL_COMMON_CHART_SOURCE_PINS.json
```

## Exact calibration

```text
source-envelope burden       25/36
sharp source burden          13/36
canonical decoder energy     13/36
cellwise envelope            4591/27000
first-cut calibration        1/13050
```

The transferred T21 audit retains

```text
beta envelope upper          0.8290856201657449
relative reserve             0.1709143798342551
```

but remains fail-closed because the actual common-chart boundary pairing and its
Recognition-complete transport have not yet been displayed.

## Pull and run in Jupyter

```python
%cd "C:\Users\abc\Desktop\New Folder (2)\New folder\PROVISNAL RELATED\RH framework\Recognition-Kernel-Framework"

!git fetch origin
!git switch agent/cut-memory-spectral-isomorphism
!git pull --ff-only origin agent/cut-memory-spectral-isomorphism

!python -m unittest -v proof_lab.test_native_source_domination_decoder

!python -m proof_lab.native_source_domination_decoder \
    --output proof_lab/NATIVE_SOURCE_DOMINATION_DECODER_ACTUAL.json
```

Expected:

```text
Ran 7 tests
OK
PASS_NATIVE_SOURCE_DOMINATION_DECODER_STAGE3B
ACTUAL_WEIL_COMMON_CHART False
```

The final `False` is deliberate. It records the exact remaining domain theorem,
not a failed generalized stage.

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/NATIVE_SOURCE_DOMINATION_DECODER_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/NATIVE_SOURCE_DOMINATION_DECODER_ACTUAL.json"
    ).read_bytes()
).hexdigest()

print("HASH_STABLE", expected == actual)
print("EXPECTED", expected)
print("ACTUAL  ", actual)
```

Expected:

```text
HASH_STABLE True
```

Pinned hash:

```text
5cb373749c30343900fa1ac3ba74e2341d88618addef25f8d3192bb37f4ab527
```

## Next stage

Stage 3C is the Native Two-Sheet Boundary-Pairing Theorem. It must construct

```text
J_Weil : X3^- -> L2(R; C^2)
b_partial(xi)
```

from the already declared prime--Gamma cut analysis and prove

```text
L_partial(f) = integral <b_partial(xi), J_Weil f(xi)> dxi

||Xi_0 f||^2 >= integral <J_Weil f, Omega_0 J_Weil f> dxi.
```

After Recognition-Cauchy/Smriti-tail extension, the T21 envelope would generate
the actual completed-Weil decoder automatically.

## Claim boundary

A pass proves the universal common-chart theorem, the exact calibrations, and
the arithmetic/provenance audit. It does not yet prove the actual common-chart
pairing, completed-Weil cut covariance, or RH.
