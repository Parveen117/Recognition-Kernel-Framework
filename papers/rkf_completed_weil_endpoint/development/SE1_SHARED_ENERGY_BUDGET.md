# SE1: native graph energy and a shared endpoint residual budget

Date: 2026-10-11. Development in the existing Recognition endpoint paper.
Base: RKF main at `e8e3089745bf7dc0532d01c62a5f660f5658c6f0`.

The result is a sharper **conditional chart estimate**, together with a
five-column residual theorem. It does not certify the completed-Weil source,
the sign of \(K_0\), or RH.

## 1. Place in the native route

Typed cuts, cut scalars, derived iota, lawful composition and declared target
and residue precede the representation. We use the metric graph already
derived in [T35](../../../theorum/35_native_metric_graph_boundary_pairing.md),
not a new primitive metric. Native adjoints are transported only through the
declared adapters. In this admitted chart the following energy argument is
ordinary Hilbert-space analysis.

The relevant route is:

1. Native metric graph and its actual odd boundary state, T35.
2. Complete prime--Gamma source with its diagonal debt, [T36](../../../theorum/36_native_prime_gamma_debt_source_adapter.md).
3. A common source lower chart and the boundary or residual pairing in that
   same chart.
4. Shared energy estimate, then a five-dimensional reserve comparison.

Step 3 is an explicit hypothesis of this note. In particular, the statement
in [T38, section 4](../../../theorum/38_native_compatibility_form_range_source_domination.md)
that its displayed symbol is already debt-paid is not used as proof of this
step. Section 6 below records the unresolved accounting.

This continues the endpoint energy projection and finite reserve identity in
[MP PR 283](https://github.com/Parveen117/MP/pull/283), pinned at
`3d2bd5c11dfffb0548ef990a4f904cf95bbe1cc9`. The active development is here;
the MP note is a provenance reference, not a runtime dependency.

## 2. A quarter-energy identity for the native graph

Let \(C:\operatorname{Dom}C\subset H\to K\) be closed and densely defined,
let \(q\in H\), and set \(r=(I+C^*C)^{-1}q\). The requirement \(q\in H\)
is stronger than merely being a continuous functional for the graph norm.
It holds for the T35 boundary seed used below.

Since \(r\in\operatorname{Dom}(C^*C)\) and \(q=r+C^*Cr\),

\[
 \boxed{\quad
 \|Cr\|^2=\operatorname{Re}\langle q,r\rangle-\|r\|^2
 =\frac14\|q\|^2-\|r-q/2\|^2
 \le\frac14\|q\|^2.\quad}                                      \tag{SE1.1}
\]

This proves the assertion for unbounded \(C\) as well. The constant is sharp
for the class of graph operators: take \(C=I\). This is a completion-of-the-
square identity; no novelty of the general identity is asserted.

In the T35 chart, write the unitary Fourier transform as
\(\mathcal Ff=(2\pi)^{-1/2}\widehat f\), and put

\[
 m(x)=e^{-3|x|/2},\qquad
 Cf=\sqrt{1+|G|}\,\mathcal F(mf),\qquad
 b_q=\mathcal F(mr).
\]

Plancherel and \(1+|G|\ge1\) give

\[
 \boxed{\int_{\mathbb R}|b_q(\xi)|^2\,d\xi
       =\|mr\|^2\le\|Cr\|^2\le\|q\|^2/4.}                       \tag{SE1.2}
\]

For the actual seed \(q_b=\sqrt2\,m(x)\sinh(x/2)\),

\[
 \|q_b\|^2
 =2\int_0^\infty e^{-3x}(\cosh x-1)\,dx=\frac1{12}.
\]

Thus the total normalized Fourier mass is at most **\(1/48\)**, improving
the previously used \(1/12\). This bounds the frequency component of the
graph state. It does not say that this component alone represents the full
native boundary functional.

Assume the T35 reflection covariance. For odd \(q\), \(r\) and \(mr\) are
odd. Also \(\|r\|\le\|q\|\), because \(I+C^*C\ge I\). Consequently

\[
 \begin{split}
 |\widehat{mr}(\xi)|
 &\le|\xi|\int_{\mathbb R}|x|m(x)|r(x)|\,dx\\
 &\le|\xi|\left(\int_{\mathbb R}x^2e^{-3|x|}\,dx\right)^{1/2}\|q\|
 =|\xi|\sqrt{4/27}\,\|q\|.
 \end{split}                                                   \tag{SE1.3}
\]

The integrability and zero constant moment follow from Cauchy--Schwarz;
\(|e^{-ix\xi}-1|\le|x\xi|\) proves the first inequality. For \(q_b\)
this is the T35 bound \(|\widehat{mr}(\xi)|\le|\xi|/9\).
For a rational outward estimate we relax \(1/\sqrt{2\pi}\le1\):

\[
 |b_{q_b}(\xi)|^2\le\xi^2/81.
\]

All frequency integrals in this note use Lebesgue measure on the **whole
real line**. Folding into two sheets on a half-line must carry its unitary
normalization and the corresponding factor of two explicitly.

## 3. One energy budget shared by the active region and the tail

Let \(s>0\) almost everywhere, \(0\le\rho\le a\), and
\(\int\rho\le M\). For every \(\tau\ge0\),

\[
 \boxed{\int\frac{\rho}{s}
 \le \tau M+\int a(\xi)\bigl(s(\xi)^{-1}-\tau\bigr)_+\,d\xi.}     \tag{SE1.4}
\]

Proof: write \(s^{-1}=\tau+(s^{-1}-\tau)\), discard the negative part
in the second integral, and apply the two bounds on \(\rho\). The same
argument applies by monotone truncation if either side initially has
improper endpoints. No existence of an optimizing density is needed.

The old separate estimate charges the active envelope and then charges the
entire mass \(M\) again in the tail. Equation (SE1.4) instead charges
\(\tau M\) once; active cells pay only their excess above \(\tau\).
This is an elementary positive-part bound, not a claim of a new general
optimization theorem.

For the pinned T21 profile use

\[
 h=1/200,\quad N=2400,\quad c=\gamma_0/2,\quad
 \tau=1/s_{\rm far},\quad a(\xi)=\alpha\xi^2.
\]

The supplied lower profile has \(s(\xi)\ge c\xi^2\) for
\(0<|\xi|\le h\), \(s(\xi)\ge s_i\) on
\(ih\le|\xi|\le(i+1)h\), \(1\le i<N\), and
\(s(\xi)\ge s_{\rm far}\) on \(|\xi|\ge12\).
The upstream \([12,13]\) floor exceeds the far floor, so using the latter
there is an allowed weakening. These are consumed profile inequalities,
not inequalities regenerated by this replay.

The exact data satisfy \(\tau c h^2\le1\). Therefore (SE1.4) gives

\[
 \boxed{
 B(M,\alpha)=\tau M+
 2\alpha\left(\frac h c-\frac{\tau h^3}{3}\right)
 +\frac{2\alpha}{3}\sum_{i=1}^{N-1}
 \left(((i+1)h)^3-(ih)^3\right)(s_i^{-1}-\tau)_+ .}              \tag{SE1.5}
\]

The seam contribution is the exact integral of
\(\alpha\xi^2((c\xi^2)^{-1}-\tau)\). There is no inverse at \(\xi=0\);
the odd first moment makes the improper integral finite. The tail has zero
excess. Of the 2,399 non-seam active cells, only 20 have positive excess.

## 4. Exact replay on the supplied 2,400-cell profile

The [replay](../../../proof_lab/endpoint_shared_energy_budget.py) decodes the
pinned IEEE-754 entries directly into rational numbers. No floating-point
summation enters the comparisons. Decimals below display those fractions;
the strict rational comparisons are the certificate.

| Estimate | Display of the computed upper bound |
| --- | ---: |
| Old separate estimate, coarse moment, exact rational replay | 0.863914786444721 |
| Separate estimate, sharp moment | 0.787529136133652 |
| Sharp moment and shared mass, \(M=1/12\) | 0.531510718404385 |
| Graph quarter-energy and shared mass, \(M=1/48\) | **0.133004924860525** |

The old separate estimate uses moment square \(1/9\) and amplitude square
\(1/16\), the rational coarse envelope of the upstream reaudit. The second
uses \(1/81\) and \(1/18\). Both separate estimates use upper cell endpoints.
The new shared estimate integrates the quadratic envelope exactly.

In exact arithmetic,

\[
 B(1/48,1/81)<2/15,\qquad 1-B(1/48,1/81)>13/15.                 \tag{SE1.6}
\]

The numerator/denominator binary hash of \(B(1/48,1/81)\) is
`0ec6d69323360c302af45675dc78d725762ac265094c05fd7ac6d871c987111a`.
The [stored result](../../../proof_lab/ENDPOINT_SHARED_ENERGY_RESULT.json)
records the three charges and the full boundary of the claim.

The historical T21 decimal `0.8290856201657449` is preserved as provenance.
It is not substituted for the old **exact rational** comparison above.
These numbers concern a supplied chart profile and envelope; they are not
measurements of the actual completed-source decoder norm.

## 5. Five-column version and its endpoint use

Let \(Q:\mathbb C^5\to H\) have odd columns and define
\(B_Q(\xi)z=\mathcal F[m(I+C^*C)^{-1}Qz](\xi)\).
Applying (SE1.2)--(SE1.3) to every \(Qz\) proves the matrix inequalities

\[
 \int B_Q^*B_Q\preceq\tfrac14 Q^*Q,\qquad
 B_Q(\xi)^*B_Q(\xi)\preceq\tfrac4{27}\xi^2Q^*Q.
\]

Equation (SE1.4), again tested on every \(z\), yields

\[
 \boxed{\int\frac{B_Q(\xi)^*B_Q(\xi)}{s(\xi)}\,d\xi
 \preceq \kappa Q^*Q,\qquad
 \kappa=B(1/4,4/27)=12B(1/48,1/81)<8/5.}                       \tag{SE1.7}
\]

This retains all cross-column entries. Five separate diagonal estimates are
not substituted for the Gram matrix.

Here is the exact attachment hypothesis needed to turn (SE1.7) into a
source-energy tail. Let \(S\ge0\) be the actual self-adjoint source on its
declared native carrier \(\mathcal H_{\rm nat}\), and let
\(R:\mathbb C^5\to\mathcal H_{\rm nat}\) be the actual residual. Suppose a
common chart \(J\) satisfies, for all \(z\) and all \(f\) in a form core
whose form closure includes the full source domain,

\[
 \begin{split}
 \|S^{1/2}f\|^2&\ge\int s(\xi)\|Jf(\xi)\|^2\,d\xi,\\
 \langle Rz,f\rangle_{\rm nat}
 &=\int\langle B_Q(\xi)z,Jf(\xi)\rangle\,d\xi .
 \end{split}                                                   \tag{SE1.8}
\]

These are statements about the **same** chart, measure, metric, residual
and completed source. A two-sheet identification must preserve the
integral and pointwise estimates above, or recompute their constants.

Weighted Cauchy--Schwarz gives

\[
 |\langle Rz,f\rangle|^2
 \le\kappa\|Qz\|^2\|S^{1/2}f\|^2.
\]

Thus this functional extends continuously to
\(\overline{\operatorname{Ran}S^{1/2}}\), annihilates \(\ker S\), and has
a representing vector of norm at most \(\sqrt\kappa\|Qz\|\).
Equivalently \(Rz\in\operatorname{Ran}S^{1/2}\), and its minimum-energy
representative is \(S^{\dagger/2}Rz\). This proves

\[
 \boxed{E^*E\preceq\kappa Q^*Q\preceq\tfrac85 Q^*Q,\qquad
 E=S^{\dagger/2}R.}                                            \tag{SE1.9}
\]

No global positive floor for \(S\) or vector \(S^{-1}Rz\) is required.
The positive-support inverse is not permission to erase a kernel residue.
This is the form-norm argument underlying Douglas-type range/factorization
results; the proof here also states the needed form-domain condition.

For the five-label endpoint require \(W\mathbb C^5\perp\ker S\) and
\(W\mathbb C^5\subset\operatorname{Dom}S^{\dagger/2}\). Put
\(T=S^{\dagger/2}W\), so \(W=S^{1/2}T\) and \(T\) is on positive support.
Let
\(G=\operatorname{diag}(1,A_3)>0\), and \(K_0=G-T^*T\).
For trial columns \(X\in\operatorname{Dom}S\), set

\[
 R=W-SX,\qquad Q_X=W^*X+X^*W-X^*SX.
\]

The MP PR 283 completion-of-the-square identity is
\(T^*T=Q_X+E^*E\). Hence (SE1.8), an outward Gram bound
\(Q^*Q\preceq D_{\rm hi}\), and outward finite matrix bounds imply

\[
 \boxed{
 G_{\rm lo}-Q_{\rm hi}-\tfrac85D_{\rm hi}\succeq0
 \quad\Longrightarrow\quad K_0\succeq0.}                        \tag{SE1.10}
\]

This is a usable nonzero residual allowance. Each ledger entry need not
vanish. The actual residual seeds \(Q\) and their Gram bound have not been
computed in this packet.

Native sine exhaustion provides trial columns and monotone energy
approximation as in MP PR 283. It does not by itself prove that the
corresponding seeds converge in the stronger \(L^2\) norm used in
(SE1.9). The next computation must obtain actual residual seeds or a direct
source flux; simply increasing the sine cutoff is not an error certificate.

## 6. Source accounting that remains open

T36 keeps the completed source and mismatch Gram distinct:

\[
 S_{0,-}^{\rm full}=M_{\rm mis}-d_0I,\qquad
 \Xi_0=\mathcal A_{\rm mis}(I-d_0M_{\rm mis}^{-1})^{1/2}.
\]

T38 displays
\[
 A_0=(G+m_\Gamma+m_{\rm p})I_2-\mathcal Q.
\]
In the common unnormalized two-sheet symbol convention of the
[pinned prime--Gamma factorization](https://github.com/Parveen117/MP/blob/25ba21cc5148a10ada96faec721f00df419ea869/proof_lab/clock_free_recognition/NATIVE_PRIME_GAMMA_RESPONSE_FACTORIZATION.md),
the completed symbol is
\(\Omega_0=GI_2-\mathcal Q\), with \(d_0=m_\Gamma+m_{\rm p}\).
Thus the displayed \(A_0=\Omega_0+d_0I_2\) accounts for the **mismatch**
symbol in that convention. A change of carrier could change the written
identity; it must be exhibited rather than inferred from the name \(A_0\).
Under pullback the chart identity term becomes \(d_0J^*J\), not
automatically \(d_0I\) in the native metric.

Accordingly this note does not transport a lower bound for \(A_0\) to
\(\Xi_0^*\Xi_0\). It also does not identify the frequency component \(Cr\)
with the full graph state \((r,Cr)\), or identify the full odd carrier with
the odd Feshbach complement.

A scalar control shows why the distinction matters. Mismatch \(2\),
debt \(3/2\), and boundary square \(3/4\) give a mismatch burden \(3/8<1\),
but completed-source burden \(3/2>1\). Improving the first bound alone
does not certify the second.

The remaining sufficient tasks for this route are concrete:

1. Establish (SE1.8) for the debt-paid source on the endpoint carrier,
   including any Feshbach projection, or supply an alternate actual-source
   flux estimate.
2. Construct the five residual seeds for the chosen sine trial columns and
   enclose their entire Gram \(Q^*Q\).
3. Verify the outward \(5\times5\) comparison (SE1.10).

These are sufficient tasks for this route, not universal necessary
conditions imposed on every possible endpoint proof.

## 7. Provenance, literature and verification

The local profile and its upstream record are documented in the
[data README](../../../proof_lab/imported/endpoint_shared_energy/README.md).
[Source pins](SOURCE_PINS.json) identify the exact unchanged RKF theorem
inputs and upstream commits. The replay checks compressed and binary hashes,
all 2,401 stored floors, the 2,400-cell count, 78,734 event count, and the
two source/export commit identities. It does not rerun Arb or verify all
upstream analytic inequalities.

Relevant primary sources:

- R. G. Douglas, *On majorization, factorization, and range inclusion of
  operators on Hilbert space*, Proc. AMS 17 (1966), 413--415,
  [original paper](https://galaxy.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf).
  Theorem 1 relates a bounded-operator quadratic bound to range inclusion
  and a minimum-norm factorization. It supplies general lineage, not the
  arithmetic source attachment (SE1.8).
- T. Vejchodský, *Flux reconstructions in the Lehmann--Goerisch method for
  lower bounds on eigenvalues*, [arXiv:1801.02561](https://arxiv.org/abs/1801.02561).
  Source-compatible flux reconstruction motivates the alternate residual
  route in MP PR 283. This paper treats elliptic eigenproblems; its
  hypotheses have not been verified for the present source.
- L. Boulton and A. Hobiny, *On the quality of complementary bounds for
  eigenvalues*, [arXiv:1311.5181v2](https://arxiv.org/abs/1311.5181v2).
  Its stated compact-resolvent setting is not assumed here and its
  eigenvalue enclosure theorem is not imported as an endpoint certificate.

Read-only reproduction from the repository root:

```sh
python -m unittest proof_lab.test_endpoint_shared_energy_budget -v
python -m proof_lab.endpoint_shared_energy_budget --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The finite controls test the quarter-energy constant, shared-budget
sharpness in a finite model, seam integration, matrix homogeneity,
correlated columns, old exact replay, profile corruption, and debt
non-promotion. Written proofs, exact finite execution, source provenance,
formal verification and external review remain separate. No new Lean
proof or external review is claimed.

The [validation record](VALIDATION.md) reports the actual local runs,
including the unchanged operator engine's runtime-sensitive pin failure.
