# MP Gold 01: Method Seeds

## Source PRs

```text
MP PR #30  exact theta recoupling and controlled Fredholm gap candidate
MP PR #31  winding, dagger and topological index theorem
MP PR #32  arithmetic Fredholm and Euler determinant realization
```

## Why this is gold

These are not terminal RH theorems. They are reusable method seeds that later reappear inside RKF as Fredholm control, index bookkeeping, determinant shadowing and arithmetic carrier discipline.

## PR #30: Fredholm / exact recoupling seed

Useful content:

```text
exact coupled SU(2) spin-network basis;
Wilson kinetic transfer diagonalization;
trace-class theta transfer with explicit factorial tail;
exact sparse multiplication through Wigner 6j and 9j symbols;
controlled fixed-graph Fredholm gap candidate;
face identities and Hermiticity tests.
```

Reusable principle:

```text
When a basis is overcomplete, replace it by an exact representation basis before asking spectral questions.
```

This is the method ancestor of later RKF insistence on source restriction, target visibility and same-carrier Gram identities.

## PR #31: winding / dagger / index seed

Useful content:

```text
determinant winding;
unitary spectral flow;
Toeplitz cut index;
dagger index reversal;
gauge-conjugation invariance;
additivity;
homotopy stability.
```

Reusable principle:

```text
A seam integer is lawful only when winding, spectral flow and index are typed in one sign convention.
```

This is the ancestor of the later threshold holonomy / seam charge equivalence.

## PR #32: arithmetic Euler-Fredholm seed

Useful content:

```text
H = ell^2(primes);
K(s)e_p = p^(-s)e_p;
K(s) trace-class for Re(s)>1;
det(I-K(s)) = product_p(1-p^(-s)) = 1/zeta(s);
-log det(I-K(s)) = sum_{m>=1} Tr(K(s)^m)/m;
exact prime-power Euler expansion.
```

Reusable principle:

```text
The Euler determinant is exact in its lawful half-plane, but it does not by itself supply analytic continuation, completion, reflection or RH.
```

This prevents the old mistake of promoting a diagonal Euler carrier beyond its domain.

## Claim boundary

```text
Fredholm / recoupling method seed        USEFUL
winding / dagger / index theorem         USEFUL
arithmetic Euler determinant             USEFUL IN Re(s)>1
completed critical carrier               NOT SUPPLIED HERE
RH                                        NOT CLAIMED
```
