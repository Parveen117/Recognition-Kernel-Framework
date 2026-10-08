# O15 Foundational Audit v0.1

This Class F package audits the fifteen-object catalogue.  It uses only Python
3.11/3.12 standard-library exact integer and `Fraction` arithmetic.

It checks:

- all fifteen object IDs and fail-closed status entries;
- SHA-256 pins for the theorem, ledger, protocol and specification;
- the normalized seam-Jacobian magnitude identity;
- the rank-one winding-metric inverse and determinant identities;
- alternating-dimension cancellation for a finite cut complex;
- cyclic-tensor input invariance;
- finite prime-lattice injectivity;
- corrected cut-character zeros and weighted orthogonality coefficient;
- finite determinant product symmetry and zero detection;
- formal lambda-residue coefficient mixing;
- logarithmic Fourier translation exponents;
- winding additivity;
- seam-tangent normal divisibility;
- the Eye asymptotic extraction algebra;
- the order-two prime renormalization bound structure;
- seam-zeta exponential coefficients; and
- the original Grassmannian collapse and repaired divisor dimensions.

Negative controls must reject the source draft's incorrect/unproved promotions:
indefiniteness of `I+ww^T/h^2`, raw prime-series convergence, unit-weight
orthogonality, the original codimension-one Grassmannian claim, and promotion
of the Eye/RH statement.

Run from the repository root:

```text
python3 objects/certificates/O15_FOUNDATIONAL_AUDIT_V0_1/verify.py \
  --output objects/certificates/O15_FOUNDATIONAL_AUDIT_V0_1/result.json
```

Expected status:

```text
PASS_O15_NATIVE_OBJECT_FOUNDATIONAL_AUDIT
```

The result is a foundational consistency audit, not a numerical enclosure and
not a proof of any claim recorded as `OPEN`.
