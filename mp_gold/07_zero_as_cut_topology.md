# MP Gold 07: Zero as Cut, Not Joint

## Source provenance

```text
source repository: Parveen117/MP
primary PRs:       #249, #250, #259
main objects:      zero cut, cut/join projector algebra, prime-torus memory cycle, spectral-flow cut memory
```

## Why this belongs in RKF

The positive-eta path theorem proves that normalization and eta-continuation commute while `eta>0`.  It does not say that the endpoint `eta=0` is an ordinary positive-eta point.  The zero-as-cut theorem explains why the endpoint must be treated as a cut/support problem rather than as a harmless substitution.

This is a conceptual support theorem for the zero-cut T03 endpoint.  It is not the terminal sign theorem by itself.

## Abstract cut-join torus theorem

The cut-first ontology is:

```text
zero = first cut
pre-cut carrier = circle
post-cut carrier = torus with independent memory cycle
```

The homology ledger is

```text
H_1(S^1; Z) = Z gamma_pi
H_1(T^2; Z) = Z gamma_pi + Z mu_cut
```

The geometric cycle carries the pi calibration.  The second cycle carries irreversible cut memory.

On the ordered basis `(gamma_pi, mu_cut)`, define

```text
P_joint = diag(1,0)
P_cut   = diag(0,1)
```

Then

```text
P_cut P_joint = 0.
```

Therefore any mode satisfying both

```text
P_cut u = u
P_joint u = u
```

must vanish.  A nonzero endpoint obstruction cannot be both a pure cut state and a complete joint state on the same carrier.

## Join projection defect

For the join projection and uncut-circle section

```text
J = [1,0]
S = [1,0]^T
```

we have

```text
J S = I_1
S J = P_joint != I_2
rank(SJ)=1 < 2=rank(I_2)
```

Thus visible circle return does not imply full post-cut state return.  The exact memory defect is

```text
I_2 - S J = P_cut.
```

## State witness

For the one-winding, one-cut class `(1,1)`, the geometric cycle returns but cut memory survives:

```text
pi before join                    pi
pi after geometric join           pi
cut charge before                 1
cut charge after full-circle lift 0
surviving memory                  (0,1)
```

So geometric closure is not state closure.

## Finite critical response evidence

The finite critical response pair in PR #250 is not a pure cut mode or pure joint mode.  It splits into a geometric-joint coordinate and surviving cut-memory coordinate:

```text
g_c = (r_c + j_c)/sqrt(2)
m_c = (r_c - j_c)/sqrt(2)
```

The user-local run recorded:

```text
eta_c                              7.628008053037797e-08
corrected critical target norm     1.1026210470914484e-18
joint component norm               4.137400474477719e-05
cut-memory component norm          4.137400474477719e-05
relative cut memory                0.7071067811865472
complete state return              False
pure cut mode                      False
pure joint mode                    False
```

This supports the warning that endpoint return must be tested as full state return, not merely visible geometric return.

## Gauge-invariant spectral-flow formulation

PR #259 gives a finite gauge-invariant meaning to `zero itself is a cut`.  For

```text
K_eta = I_5 - B_eta,
```

a moving unitary frame may rotate eigenvectors, but the negative inertia can change only through zero.  The sampled cut memory is

```text
m_cut = N_-(K_eta_final) - N_-(K_eta_initial).
```

A transverse crossing changes negative inertia and creates cut memory.  A tangential zero contact is recorded separately because it reaches zero without a net inertia change.

## Claim boundary

```text
abstract cut/join projector contradiction       PROVED
visible return != full state return             PROVED IN MODEL
finite critical cut-memory packet               USER-LOCAL PASS WITH LINEAGE QUALIFIER
spectral-flow cut-memory definition             IMPLEMENTED
sampled positive-eta zero-cut ledger            RUN-DEPENDENT / NOT TERMINAL
native critical cut identification              OPEN IN SOURCE PR #249
native complete-joint identification            OPEN IN SOURCE PR #249
RH from zero-as-cut alone                        NOT CLAIMED
```

## Use in the paper

Use this theorem as an endpoint-discipline lemma:

```text
positive eta path equality
-> no path ambiguity before endpoint;
zero as cut
-> eta=0 is a support/memory cut, not ordinary continuation;
zero-cut T03
-> performs the actual endpoint source-Gram completion.
```

The theorem belongs near the T03 section or in the appendix as the conceptual reason why the endpoint is named a zero-cut endpoint.
