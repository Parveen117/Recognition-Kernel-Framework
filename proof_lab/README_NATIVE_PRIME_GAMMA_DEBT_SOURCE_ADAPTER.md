# Native Prime--Gamma--Debt Source Adapter Stage 3D

Stage 3D closes the actual source-adapter construction and leaves only the
two-sheet source/boundary attachment open.

## Native chain

```text
prime mismatch + Gamma mismatch
-> mismatch analysis A_mis
-> diagonal debt d_0
-> compatibility defect D_comp
-> Xi_0=A_mis D_comp
-> native graph J_X
-> canonical adapter D_Sigma^0=Xi_0 J_X^*
-> graph-null adapter family
-> two-sheet domination / decoder gate.
```

The actual adapter is now constructed:

```text
ACTUAL_SOURCE_ADAPTER True
```

The actual decoder bound remains fail-closed:

```text
ACTUAL_DECODER_BOUND False
```

That `False` is deliberate. It means the direct unshifted envelope has not yet
been attached to the actual source and boundary in one two-sheet chart.

## Files

```text
theorum/36_native_prime_gamma_debt_source_adapter.md

proof_lab/native_prime_gamma_debt_source_adapter.py
proof_lab/test_native_prime_gamma_debt_source_adapter.py
proof_lab/NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_EXPECTED.sha256
proof_lab/imported/NATIVE_PRIME_GAMMA_DEBT_ADAPTER_PINS.json
```

## Exact calibration

```text
mismatch Gram                       diag(169,225,400)
diagonal debt                       144
compatibility defect                diag(5/13,3/5,4/5)
source Gram                         diag(25,81,256)
minimum decoder burden              361/900
relative reserve                    539/900
```

The packet also verifies:

```text
canonical adapter recovers Xi;
canonical adapter kills graph-null memory;
all alternate adapters differ by E(I-JJ*);
boundary recognition class is adapter invariant;
event-coordinate rotations preserve source and decoder;
cut covariance is positive definite.
```

## Pull and run in Jupyter

```python
%cd "C:\Users\abc\Desktop\New Folder (2)\New folder\PROVISNAL RELATED\RH framework\Recognition-Kernel-Framework"

!git fetch origin
!git switch agent/cut-memory-spectral-isomorphism
!git pull --ff-only origin agent/cut-memory-spectral-isomorphism
```

Run the tests:

```python
!python -m unittest -v proof_lab.test_native_prime_gamma_debt_source_adapter
```

Expected:

```text
Ran 9 tests
OK
```

Generate the certificate:

```python
!python -m proof_lab.native_prime_gamma_debt_source_adapter \
    --output proof_lab/NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_ACTUAL.json
```

Expected:

```text
PASS_NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_STAGE3D
ACTUAL_SOURCE_ADAPTER True
ACTUAL_DECODER_BOUND False
```

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_ACTUAL.json"
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
871337671eed453743464e2bfd9bc126e75f55a78d26139be01db064a17e79c6
```

## Robust attachment budget

For the direct T21 envelope

```text
beta_env = 0.8290856201657449
```

the exact reserve is

```text
1-beta_env = 0.1709143798342551.
```

If the source chart is exact, the allowed source-relative boundary residual is

```text
delta_partial < 0.0894586115031646185...
```

With five percent source loss, the remaining boundary residual budget is

```text
delta_partial < 0.0658042467246887...
```

With ten percent source loss, it is

```text
delta_partial < 0.0402051028325867...
```

## Next stage

Stage 3E is the Native Two-Sheet Source-Domination Attachment Theorem. It must
prove, on the actual completed-Weil carrier,

```text
||Xi_0 f||^2
  >= integral <J_2sh f, A_0 J_2sh f>;

L_partial(f)
  = integral <b_partial, J_2sh f>.
```

Exact identities are ideal, but the robust residual budget above also permits a
directed enclosure.

## Claim boundary

A pass proves the source-adapter theorem, graph-null classification, exact
generalized calibration and robust attachment budget. It does not yet prove
the actual two-sheet domination, actual completed-Weil decoder, completed-Weil
cut covariance, or RH.
