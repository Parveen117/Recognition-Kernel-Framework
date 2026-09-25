# Theorum 02: Seam Integer and Single-Sector Terminal Reduction

## Source provenance

```text
source repository: Parveen117/MP
primary PRs:       #235, #242, #247, #255, #277
main objects:      K_eta, B_eta, k_Sigma(eta), threshold holonomy, odd five-label packet
```

## Global seam integer

The native completed-Weil sign decision is represented by a compact seam response. For positive eta, the representation uses a compact relative operator

```text
K_eta = K_(+,eta) direct_sum K_(3,eta)^sharp
```

and the seam charge

```text
k_Sigma(eta) = rank 1_(1,infinity)(K_eta).
```

The global relation is

```text
k_Sigma(eta)=0
iff shifted completed packet is nonnegative.
```

For a cofinal sequence `eta_j downarrow 0`, the eta-chain version of this statement becomes the endpoint sign reformulation.

## Rank-at-most-five adverse packet

The representation-complete reduction isolates the remaining fixed-shift adverse source as a finite Birman-Schwinger obstruction:

```text
F_(3,eta)^times = S_(eta,-) - V_eta V_eta*
rank(V_eta) <= 5
B_eta = V_eta* S_(eta,-)^(-1) V_eta
k_Sigma(eta) = N_+(B_eta - I).
```

Thus the terminal sign is tracked by a Hermitian matrix of rank at most five, not by an uncontrolled infinite observer cascade.

## Common five-matrix covariance

For a positive source operator `S` and five-column source map `V`, set

```text
B = V* S^(-1) V in M_5(C).
```

Faithful carrier transport by a unitary does not change the represented obstruction:

```text
S^U = U S U*
V^U = U V
(V^U)* (S^U)^(-1) V^U = B.
```

Changing the five labels by a unitary only conjugates the matrix:

```text
B' = U_5* B U_5.
```

Therefore the following data are representation invariant:

```text
spectrum;
threshold projection;
seam charge;
sign decision.
```

## Prime-torus and threshold-holonomy avatars

The arithmetic Bohr/prime-torus chart transports the same native source and same five columns. Therefore

```text
B_eta^prime-torus = B_eta^native.
```

The matrix, seam and holonomy statements become

```text
B_eta <= I
iff k_Sigma(eta)=0
iff H_threshold(eta)=I
iff shifted completed parity/Feshbach packet is nonnegative,
```

where

```text
H_threshold(eta) = I - 2 1_(1,infinity)(B_eta).
```

This makes threshold holonomy an avatar of the same finite obstruction, not an independent RH route.

## One-sector sufficiency after reduction

The upstream bilateral carrier still represents both parity sectors. The single-sector conclusion is more delicate:

```text
even sector remains represented upstream;
common pure-source sign and favorable even boundary remove an independent even terminal gate;
finite endpoint diagnostic follows only the odd five-label source packet.
```

So the lawful sentence is:

```text
One sector is terminally sufficient only after the seam-integer / source-sign / favorable-even reduction.
```

The even sector is not deleted. It becomes non-terminal after the reduction.

## Fixed-node evidence

The common five-matrix update records the fixed node

```text
eta=.01 centre top             0.43597867312210625
outward matrix error upper     0.40291149063402765
native top upper               0.8388901637561339
threshold reserve              0.1611098362438661
k_Sigma(.01)                   PROVED ZERO
```

This is a closed shifted node, not by itself eta-zero completion.

## Claim boundary

```text
representation-complete bilateral framework    PROVED
native seam integer                            PROVED
rank-at-most-five fixed-shift reduction         PROVED
common five-matrix covariance                   PROVED
prime-torus matrix transport                    PROVED
threshold holonomy <=> seam charge              PROVED
fixed eta=.01 seam zero                         PROVED
single-sector terminal focus                    VALID AFTER REDUCTION

controlled eta_j downarrow 0                    SEPARATE GATE UNLESS T03 APPLIED
UGD terminal holonomy = threshold holonomy       ASSUMED WHERE STATED
unconditional RH from this capsule alone         NOT CLAIMED
```

## Use in the framework

The theorem should be consumed as the finite obstruction adapter:

```text
completed-Weil sign problem
-> compact seam response
-> seam integer k_Sigma
-> rank-at-most-five B_eta
-> odd five-label terminal packet after source/even reduction
```
