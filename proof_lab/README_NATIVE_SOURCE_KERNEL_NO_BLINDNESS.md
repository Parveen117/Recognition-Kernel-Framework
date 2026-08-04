# Native Source-Kernel No-Blindness Stage 3G

Stage 3G attaches source-kernel injectivity to the exact Stage 3F completed odd
source and upgrades the relative cut covariance from nonnegative to strictly
positive on every nonzero odd state.

## Native chain

```text
Stage 3F actual decoder and cut covariance
-> T21 source lower chart positive away from the zero cut
-> injective native two-sheet chart
-> ker Xi_0 = ker S_(0,-)^full = {0}
-> strict odd completed-Weil positivity.
```

The theorem gives

```text
beta_partial^cut <= 0.8290856201657449
relative reserve >= 0.1709143798342551
```

and therefore

```text
<f,W_3^- f>
  >= 0.1709143798342551 <f,S_(0,-)^full f>
  > 0
```

for every nonzero odd native state.

This is strict quadratic-form positivity, not a uniform ambient spectral gap.
The source floor vanishes at the cut and may accumulate at zero without
possessing a nonzero null vector.

## Files

```text
theorum/39_native_source_kernel_no_blindness_strict_odd.md

proof_lab/native_source_kernel_no_blindness.py
proof_lab/test_native_source_kernel_no_blindness.py
proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_EXPECTED.sha256
proof_lab/imported/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_PINS.json
```

## Exact calibrations

```text
odd-polynomial active determinant               720
source Gram determinant                         518400
decoder burden                                  61/144
relative reserve                                83/144
strict cut-covariance determinant               298800

negative control blind polynomial               x(4-5x^2+x^4)
third active-node detection                     120

noncoercive relative reserve                    1/5
minimum source floor at N=12                    1/12
minimum strict floor at N=12                    1/60
```

## Pull and run

First generate and verify Stage 3F if it has not yet been run:

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main

!python -m unittest -v proof_lab.test_native_compatibility_form_source_domination

!python -m proof_lab.native_compatibility_form_source_domination \
    --output proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json
```

Expected Stage 3F status:

```text
PASS_NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_STAGE3F
ACTUAL_FORM_RANGE_TRANSFER True
ACTUAL_SOURCE_DOMINATION True
ACTUAL_DECODER_BOUND True
ACTUAL_CUT_COVARIANCE True
ACTUAL_STRICT_ODD_POSITIVITY False
```

Then run Stage 3G:

```python
!python -m unittest -v proof_lab.test_native_source_kernel_no_blindness

!python -m proof_lab.native_source_kernel_no_blindness \
    --stage3f-actual proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json \
    --output proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_ACTUAL.json
```

Expected:

```text
Ran 8 tests
OK

PASS_NATIVE_SOURCE_KERNEL_NO_BLINDNESS_STAGE3G
STAGE3F_HASH_VERIFIED True
ACTUAL_SOURCE_KERNEL_INJECTIVITY True
ACTUAL_XI0_INJECTIVITY True
ACTUAL_STRICT_ODD_POSITIVITY True
ACTUAL_ODD_CLASSICAL_INTERFACE False
RH_PROMOTION_ALLOWED False
```

The final two `False` values are deliberate. Stage 3G closes the native odd
sign only. It does not silently consume the classical explicit formula or a
parity-restricted Weil theorem.

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_ACTUAL.json"
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
551c3e5bd4e8406032dcffcd017660442897f7e9be4ddb5206a3acbf6c195fd2
```

## Next stage

Stage 3H is the Odd Native-to-Classical Normalization Interface. It must prove,
on one logarithmic test core and in one Fourier convention, the term-by-term
identity between the native odd form and the odd restriction of the classical
completed explicit-formula Weil form.

It must match:

```text
completion-boundary term;
Gamma term;
prime-power term;
reflection/conjugation convention;
logarithmic/multiplicative unitary normalization;
test-core density.
```

Only after that theorem is proved may a parity-restricted classical Weil
implication be consumed.

## Claim boundary

A Stage 3G pass proves the actual source-kernel injectivity, Xi_0 injectivity,
strict odd native completed-Weil positivity and injectivity of the cut-covariance
bridge. It does not prove the classical normalization interface or RH.
