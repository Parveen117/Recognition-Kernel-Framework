# Madhava–Smriti Bilateral Jet-Flow Certificate

This packet certifies the exact finite algebra behind Theorem 44.

It consumes the corrected-recursion grammar developed in the private
`Parveen117/Vedic` repository and realizes it on the bounded bilateral jet flow
from Theorem 43. The packet does not claim that one particular historical
Madhava formula has been reconstructed, and it does not yet assign Smriti to a
nuclear observable.

## Core identity

For corrected finite jet state `M`, recognized full flow `F`, signed Smriti
`Sigma`, and conventional tail `T=-Sigma`, the packet verifies

```text
M - F - Sigma = 0
M + T = F
```

At each refinement step, the next jet term moves exactly from the tail into the
finite state:

```text
M_next = M + q
T_next = T - q
Sigma_next = Sigma + q
```

The refinement seam and its composition cocycle remain zero.

## Exact fixture

```text
J = diag(1,-1,1,-1,1)
G = five-dimensional nilpotent shift, G^5 = 0
B = (1,0,0,0,0)
t = 2/3
```

The finite body begins at first order. Three correction steps successively
consume the remaining second-, third- and fourth-order terms. Intermediate
Smriti is nonzero and typed; the final tail vanishes exactly.

## Checks

The seven focused tests cover:

```text
corrected-recursion closure at every depth;
strict tail-energy descent in the canonical fixture;
exact correction-to-tail transfer;
bilateral cut transport of finite states and Smriti;
even/odd tail parity;
refinement cocycle;
correction–Smriti gauge invariance;
wrong-cut, dropped-tail and uncoupled-update negative controls;
fail-closed classifications;
deterministic certificate and pinned hash.
```

## Run

```bash
python -m unittest -v proof_lab.test_madhava_smriti_bilateral_jet_flow
python -m proof_lab.madhava_smriti_bilateral_jet_flow \
  --output proof_lab/MADHAVA_SMRITI_BILATERAL_JET_FLOW_ACTUAL.json
```

Expected status:

```text
PASS_MADHAVA_SMRITI_BILATERAL_JET_FLOW_CLOSURE_CANDIDATE
```

Expected SHA-256:

```text
2dc970d0b180e6ae0c679879ac9d0aabbb138c9315942f8bc8d2565e1a539c35
```
