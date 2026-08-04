# Native Compatibility Form-Range and T21 Source Domination Stage 3F

Stage 3F corrects the over-strong ambient compatibility-range gate from Stage
3E and attaches the direct T21 cut ledger to the actual prime--Gamma--debt
source.

## Main correction

For an infinite-dimensional compatibility defect `C`,

```text
b orthogonal to ker(C)
```

implies only

```text
b in closure(Ran(C*))
```

unless the range is closed. The actual completed-Weil endpoint does not require
an attained source-inverse vector.

The correct condition is

```text
b_partial in Dom(S_(0,-)^full dagger/2).
```

The T21 direct burden proves this inverse-half form-range condition and
constructs the minimum source decoder in the recognition completion.

## Native chain

```text
prime/Gamma mismatch
-> diagonal debt
-> physical two-sheet source symbol A_0
-> cumulative T21 lower branch
-> physical boundary recognition class
-> inverse-half form-range decoder
-> actual decoder bound
-> actual odd cut covariance.
```

## Files

```text
theorum/38_native_compatibility_form_range_source_domination.md

proof_lab/native_compatibility_form_source_domination.py
proof_lab/test_native_compatibility_form_source_domination.py
proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_EXPECTED.sha256
proof_lab/imported/NATIVE_COMPATIBILITY_FORM_SOURCE_PINS.json
```

## Actual result attached by this stage

```text
T21 beta upper       0.8290856201657449
relative reserve     0.1709143798342551
active cells         2400
prime-power events   78734
```

Hence

```text
S_(0,-)^full - L_partial*L_partial
  >= 0.1709143798342551 S_(0,-)^full
  >= 0.
```

The strict odd theorem remains separate until `ker S_(0,-)^full={0}` is
attached on the same carrier.

## Pull and run in Jupyter

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main

!python -m unittest -v proof_lab.test_native_compatibility_form_source_domination

!python -m proof_lab.native_compatibility_form_source_domination \
    --output proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json
```

Expected:

```text
Ran 8 tests
OK

PASS_NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_STAGE3F
ACTUAL_FORM_RANGE_TRANSFER True
ACTUAL_SOURCE_DOMINATION True
ACTUAL_DECODER_BOUND True
ACTUAL_CUT_COVARIANCE True
ACTUAL_STRICT_ODD_POSITIVITY False
```

The final `False` is deliberate. Stage 3F closes nonnegativity and the actual
decoder bound; Stage 3G must attach source-kernel injectivity to obtain strict
odd positivity.

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json"
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
528b0010db6898cb5594921daf12edef48a732f23edc8c70b76fc034bef6a484
```

## Exact calibrations

```text
completed nonattained decoder burden      1/4
formal source-inverse energy              4N/25 -> infinity
two-sheet symbol burden                   419/7200
recognition-class minimum burden          2/3
cellwise cut burden                       41/400
```

## Claim boundary

A pass closes the actual form-range transfer, T21 source domination, minimum
decoder bound and odd cut covariance. It does not yet prove source-kernel
injectivity, strict odd positivity, the odd classical normalization interface,
or RH.
