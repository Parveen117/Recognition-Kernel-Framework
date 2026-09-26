# Odd Native-to-Classical Normalization Stage 3H

Stage 3H proves the term-by-term normalization interface between the strict
native odd completed-Weil form and the completed explicit-formula distribution
side on one logarithmic core.

## Native chain

```text
Stage 3G strict odd native positivity
-> q_(f,h)=f*h-sharp
-> q_(f,h)(t)=<f,T_t h>
-> q-hat_(f,h)(z)=f-hat(z) conjugate(h-hat(conjugate z))
-> exact boundary/Gamma/prime match
-> odd boundary = -L_partial*L_partial
-> multiplicative/logarithmic unitary match
-> pinned classical symmetric-zero-sum membrane.
```

Stage 3H does not rederive the classical explicit formula. The official paper
uses the full even-plus-odd Weil route, so a parity-restricted implication is an
optional audit rather than a load-bearing dependency.

## Files

```text
theorum/40_odd_native_classical_normalization_interface.md

proof_lab/odd_native_classical_normalization.py
proof_lab/test_odd_native_classical_normalization.py
proof_lab/ODD_NATIVE_CLASSICAL_NORMALIZATION_EXPECTED.sha256
proof_lab/imported/ODD_NATIVE_CLASSICAL_NORMALIZATION_PINS.json
```

## Exact audit

The executable packet uses Gaussian rational Laurent sequences. It verifies:

```text
correlation = convolution with h-sharp;
translation pairing at every discrete shift;
entire transform conjugate-reflection identity;
completion-boundary pole normalization;
Gamma multiplier normalization;
paired prime-power translation normalization;
odd negative-rank-one boundary reduction;
Mellin/Fourier sign reversal and logarithmic unitary equivalence;
Hermitian, reflection and Fourier-sign invariance;
weighted odd-core density calibration.
```

## Pull and run

Stage 3H requires a generated, hash-stable Stage 3G actual certificate. If
Stages 3F and 3G have not yet been run, execute their commands first.

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main
```

Generate Stage 3F if necessary:

```python
!python -m unittest -v proof_lab.test_native_compatibility_form_source_domination

!python -m proof_lab.native_compatibility_form_source_domination \
    --output proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json
```

Generate Stage 3G if necessary:

```python
!python -m unittest -v proof_lab.test_native_source_kernel_no_blindness

!python -m proof_lab.native_source_kernel_no_blindness \
    --stage3f-actual proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json \
    --output proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_ACTUAL.json
```

Run Stage 3H tests:

```python
!python -m unittest -v proof_lab.test_odd_native_classical_normalization
```

Expected:

```text
Ran 10 tests
OK
```

Generate the Stage 3H certificate:

```python
!python -m proof_lab.odd_native_classical_normalization \
    --stage3g-actual proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_ACTUAL.json \
    --output proof_lab/ODD_NATIVE_CLASSICAL_NORMALIZATION_ACTUAL.json
```

Expected:

```text
PASS_ODD_NATIVE_CLASSICAL_NORMALIZATION_STAGE3H
STAGE3G_HASH_VERIFIED True
BOUNDARY_TERM_MATCH True
GAMMA_TERM_MATCH True
PRIME_TERM_MATCH True
LOG_UNITARY_MATCH True
ACTUAL_ODD_NATIVE_CLASSICAL_INTERFACE True
CLASSICAL_ZERO_SUM_REDERIVED False
ODD_WEIL_IMPLICATION_CONSUMED False
RH_PROMOTION_ALLOWED False
```

The last three `False` values are deliberate. The classical explicit formula is
pinned rather than rederived; no optional odd-only theorem is consumed here;
and RH is not promoted by this standalone normalization cartridge.

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/ODD_NATIVE_CLASSICAL_NORMALIZATION_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/ODD_NATIVE_CLASSICAL_NORMALIZATION_ACTUAL.json"
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
f0d18ba798f6aa6bc058fe07d86f351419e2ebd475a02373cd218db4cb43df18
```

## Claim boundary

A Stage 3H pass proves the actual termwise odd native/classical normalization
interface. It does not reprove the classical explicit formula or, by itself,
prove RH. The manuscript's official terminal route combines the separately
proved even and odd restrictions and then consumes the standard full Weil
criterion.
