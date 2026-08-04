# Native Two-Sheet Compatibility Attachment Stage 3E

Stage 3E attaches the actual completion-boundary evaluation to the native
two-sheet Hardy chart and isolates the remaining source attachment as transport
through the compatibility defect.

## Native chain

```text
Hardy strip S_(3/2)
-> two boundary sheets
-> exact Cauchy evaluation density
-> physical odd boundary L_partial
-> raw prime--Gamma mismatch chart
-> compatibility defect C_comp
-> transformed boundary density
-> T21 source domination
-> contractive source decoder.
```

## Files

```text
theorum/37_native_two_sheet_hardy_compatibility_attachment.md

proof_lab/native_two_sheet_compatibility_attachment.py
proof_lab/test_native_two_sheet_compatibility_attachment.py
proof_lab/NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_EXPECTED.sha256
proof_lab/imported/NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_PINS.json
```

## Exact calibrations

```text
strip kernel sheet masses                  1/4 and 1/2
strip evaluation-kernel mass               3/4
sqrt(2)-scaled full mass                    3/2
compatibility-transferred burden            397/5184
zero-cut supported burden                   97/1296
```

The packet also verifies that a boundary component on the zero support of the
compatibility defect is rejected and that a wrong sheet orientation changes the
physical boundary despite preserving scalar masses.

## Pull and run in Jupyter

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main

!python -m unittest -v proof_lab.test_native_two_sheet_compatibility_attachment

!python -m proof_lab.native_two_sheet_compatibility_attachment \
    --output proof_lab/NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_ACTUAL.json
```

Expected:

```text
Ran 8 tests
OK
PASS_NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_STAGE3E
ACTUAL_TWO_SHEET_BOUNDARY_ATTACHMENT True
ACTUAL_COMPATIBILITY_TRANSFER False
ACTUAL_SOURCE_DOMINATION False
ACTUAL_DECODER_BOUND False
```

The three final `False` values are deliberate. The boundary is now on the actual
two-sheet chart. What remains is to transport its density through the actual
compatibility defect and attach the T21 profile to the resulting source chart.

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_ACTUAL.json"
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
21dc9870ba3fd392d99a6bd2704b99956002d530175dc37e182fea98a782eead
```

## Next stage

Stage 3F is the Native Compatibility-Range and Cut-Source Domination Theorem. It
must prove

```text
b_partial,2sh in Ran(C_comp*)
b_tilde_partial=C_comp^{dagger,*} b_partial,2sh
```

and then attach the T21 source profile to the actual completed source on this
transformed chart. The robust theorem permits either an exact identity or a
combined source-loss/boundary-residual enclosure below the pinned budget.

## Claim boundary

A pass proves the Hardy-strip boundary attachment, compatibility-transfer
mechanism, support gate, exact generalized calibrations and robust numerical
budget. It does not yet prove the actual compatibility transfer, T21 source
domination, completed-Weil decoder bound, completed-Weil cut covariance, or RH.
