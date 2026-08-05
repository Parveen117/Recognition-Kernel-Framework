# Canonical Connection and Physical-Flux Intertwiner Theorem

## 1. Canonical effect projection

Let \(0<A<I\) on a finite-dimensional accepted response space \(E\), and put

\[
S_A=(A-A^2)^{1/2}.
\]

On \(E\oplus E\), define

\[
P_A=
\begin{pmatrix}
A&S_A\\
S_A&I-A
\end{pmatrix},
\qquad
\Gamma=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\]

Then \(P_A=P_A^*=P_A^2\).

## 2. Constant non-Abelian connection

Define skew-Hermitian connection coefficients

\[
\mathcal A_r=\frac{i}{2}\Gamma,
\qquad
\mathcal A_\tau=iP_A.
\]

Their constant mixed curvature is

\[
\mathcal F_{r\tau}^{\mathrm{gauge}}
=[\mathcal A_r,\mathcal A_\tau]
=-\frac12[\Gamma,P_A].
\]

Define the self-adjoint information flux

\[
\boxed{
\mathcal F_A=rac1{2i}[\Gamma,P_A]
=i\mathcal F_{r\tau}^{\mathrm{gauge}}.
}
\]

## 3. Accepted curvature amplitude

Let \(I_+z=(z,0)\) and let \(\pi_-\) project onto the second component. Then

\[
\boxed{
\mathfrak F_A^{\mathrm{acc}}
:=\pi_-\mathcal F_AI_+
=iS_A.
}
\]

Hence

\[
\boxed{
(\mathfrak F_A^{\mathrm{acc}})^*
\mathfrak F_A^{\mathrm{acc}}
=A-A^2.
}
\]

## 4. Physical stacked leakage

Let \(C:E\to\mathcal H_C\) and suppose

\[
R=A-A^2-C^*C\ge0.
\]

Put

\[
L=R^{1/2},
\qquad
\mathcal L_{C,R}=\binom{C}{L}.
\]

Then

\[
\mathcal L_{C,R}^*\mathcal L_{C,R}=A-A^2=S_A^2.
\]

Define

\[
U_{\mathrm{flux}}=\mathcal L_{C,R}S_A^{-1}.
\]

## Theorem 4.1 (physical curvature intertwiner)

\[
\boxed{U_{\mathrm{flux}}^*U_{\mathrm{flux}}=I_E}
\]

and

\[
\boxed{
\mathcal L_{C,R}
=-iU_{\mathrm{flux}}\mathfrak F_A^{\mathrm{acc}}.
}
\]

### Proof

Using \(\mathcal L_{C,R}^*\mathcal L_{C,R}=S_A^2\),

\[
U_{\mathrm{flux}}^*U_{\mathrm{flux}}
=S_A^{-1}S_A^2S_A^{-1}=I.
\]

Since \(\mathfrak F_A^{\mathrm{acc}}=iS_A\),

\[
-iU_{\mathrm{flux}}\mathfrak F_A^{\mathrm{acc}}
=U_{\mathrm{flux}}S_A
=\mathcal L_{C,R}.
\]

QED.

Thus one canonical curvature amplitude splits isometrically into ordinary complement leakage \(C\) and information-curvature completion \(L\).

## Claim boundary

```text
CANONICAL EFFECT PROJECTION                   PROVED
NON-ABELIAN CONNECTION CURVATURE              PROVED
ACCEPTED CURVATURE GRAM = A-A^2               PROVED
PHYSICAL STACKED-LEAKAGE INTERTWINER          PROVED
ORDINARY / INFORMATION FLUX SPLITTING         PROVED
CONTINUUM RESPONSE POSITIVITY                 OPEN
CONTINUUM SEAM-FLATNESS                       OPEN
```
