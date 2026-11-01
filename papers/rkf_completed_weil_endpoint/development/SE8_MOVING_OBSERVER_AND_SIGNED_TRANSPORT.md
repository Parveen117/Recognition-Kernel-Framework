# SE8: Moving observer, actual dilation defect and a certified transition

12 October 2026. Owner: Monty Dabas.

The observer can use one fixed reference chart while the physical source
and its native pairing move through that chart. This stage writes the
actual prime, Gamma and pole transport, then certifies the nontrivial
scale change c=21/20. It obtains
\[
 \boxed{s[f]\ge\frac1{100000}\|Rf\|_2^2,\qquad
 s[f]\ge\frac1{1806251}\|f\|_X^2,
 \quad f\in X_{21/40}.}                              \tag{SE8.1}
\]
Every intermediate aperture between 1/2 and 21/40 is covered too. Their
exact local observers agree on shared event vectors. This is a genuine
transport segment, with a five-percent change in aperture, not all-scale
or global closure.

An actual operator comparison succeeds even though the scalar test
"old certified floor minus the norm of the change" fails. The change
has both positive and negative directions; its signs and mixed entries
are retained. The calculation concerns a proved lower comparison for
the corrected source, not an assumed sign for the full source.

## 1. What is reused and what is newly instantiated

[SE2](SE2_OBSERVER_PATH_OPERATOR_CERTIFICATE.md), Sections 6--7, already
proves the full defect cocycle, covariant observer equation, joined-Gram
criterion and cofinal observer limit. T28 already states a transported
finite-to-infinite completion contract. These general results are not
claimed as new here.

SE8 supplies their concrete specialization to the corrected SE4 source:
an admissible dilation, the transported native metric, every arithmetic
term of its defect, and a verified nonzero transition starting from
[SE7](SE7_FULL_PRIME_ACTIVE_APERTURE.md).

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti retain their native order. The T35 logarithmic Hilbert chart is
an admitted representation. A convenient fixed chart below is not an
absolute physical reference or a primitive metric.

## 2. An actual transport arrow and its native pairing

For an odd logarithmic core function g=Rf and c>0 define
\[
 (D_cg)(x)=c^{-1/2}g(x/c),\qquad
 \Phi_c=R^{-1}D_cR:X_A\longrightarrow X_{cA}.          \tag{SE8.2}
\]
The L2 map D_c is unitary. The native map Phi_c generally is not.
Its transported metric is exactly
\[
 \|\Phi_cf\|_X^2=
 \int e^{3c|y|}|g(y)|^2dy+
 \int(1+|G(t/c)|)|\widehat g(t)|^2\frac{dt}{2\pi}.
                                                        \tag{SE8.3}
\]
Thus a coordinate transpose or the L2 metric cannot replace the native
dagger. On compact apertures this arrow is bounded with bounded inverse.
Here is an explicit justification, rather than an assumed domain match.

The positive digamma series gives, for t>0,
\[
 tG'(t)=\sum_{k\ge0}
          \frac{4\beta_k t^2}{(\beta_k^2+t^2)^2}
       \le\frac52,\qquad \beta_k=2k+1/2.              \tag{SE8.4}
\]
For t<=1 the first term is at most 2, and the rest is at most
4[(5/2)^(-3)+(1/4)(5/2)^(-2)]<1/2. For t>=1 the summand as a function
of beta is nonnegative and unimodal. A mesh of spacing 2 has sum at
most one half its integral plus its maximum. These are respectively
1 and 3sqrt(3)/(4t)<3/2. To justify the mesh estimate, take a largest
sample: each preceding or following rectangle is bounded by the
integral over the adjacent interval toward that sample, leaving only
the largest sample unpaid. The endpoint t=0 follows by continuity.

Integration in log t yields
|G(t/c)-G(t)|<=(5/2)|log c|. With support |y|<=A, (SE8.3) therefore
gives the finite bound
\[
 \|\Phi_cf\|_X^2\le
 [e^{3(c-1)_+A}+(5/2)|\log c|]\|f\|_X^2.            \tag{SE8.5}
\]
The same argument for 1/c proves the inverse bound. Dilation carries
the odd compact core bijectively onto the corresponding core; continuity
extends it to their native completions. Also Phi_d Phi_c=Phi_(dc), with
the intermediate aperture understood.

## 3. The complete source moves inside the observer equation

Let A_* and L_* be the corrected mismatch and joint debt/pole target,
and set A_c=A_*Phi_c, L_c=L_*Phi_c. The transported source is
S_c=A_c^dagger A_c-L_c^dagger L_c. In reference coordinates its form is
\[
 \begin{split}
 s_c[g]:=s[\Phi_cf]
  ={}&\int G(t/c)|\widehat g(t)|^2\frac{dt}{2\pi}\\
 &-2\Re\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                        \langle g,T_{\log n/c}g\rangle\\
 &-2c\left|\int g(y)\sinh(cy/2)dy\right|^2.
 \end{split}                                           \tag{SE8.6}
\]
On a reference aperture A only log n<=2cA contributes. The prime
weights are not rescaled, while their reference positions move to
log n/c. Gamma moves to t/c. Both the argument and prefactor of the
pole move. Freezing any of these is a different source.

Equation (SE8.6) follows directly from the Fourier, correlation and
boundary transformations under D_c. It holds for complex odd states
and extends by the native continuity already proved. In particular
"no preferred coordinate" does not imply zero physical transport defect.

With S_A the native compression, define the actual signed defect
\[
 \Delta_{c;A}=\Phi_c^\dagger S_{cA}\Phi_c-S_A.
                                                        \tag{SE8.7}
\]
Subtracting (SE8.6) at c and 1 displays every term of this operator.
SE2's exact cocycle now becomes the source-specific identity
\[
 \Delta_{dc;A}=\Delta_{c;A}
       +\Phi_c^\dagger\Delta_{d;cA}\Phi_c.              \tag{SE8.8}
\]
The notation S_c for a pulled-back form and S_(cA) for a physical
compression must not be confused. Neither endpoint of (SE8.8) is
privileged; changing the reference transports the pairing as well.

## 4. A signed comparison that can actually be replayed

Use the reference interval [-1/2,1/2] and c_*=21/20. Throughout
1<=c<=c_*, only prime 2 is active: log 2<1 and
log 3>2[1/2+(1/2)^3/3+(1/2)^5/5]=263/240>21/20.
Define
\[
 \Psi_c(t)=G(t/c)-\sqrt2\log2\cos(t\log2/c),\quad
 h_c(y)=\sqrt c\sinh(cy/2),\quad b=1/5.
                                                        \tag{SE8.9}
\]
For |t|>=48, t/c>=48/c_*>24, so the SE6 Gamma bound gives
Psi_c(t)>b. Let F_48 be Fourier restriction to the symmetric band,
with measure dt/(2pi). The bounded comparison is
\[
 K_c=bI+F_{48}^*M_{\Psi_c-b}F_{48}-2h_c\otimes h_c,
 \qquad s_c[g]\ge\langle g,K_cg\rangle_{L^2}.          \tag{SE8.10}
\]
The star in this displayed L2 formula is explicitly the L2 adjoint;
the subsequent native transport uses (SE8.3), not this metric as a
replacement. Odd parity allows the band integral to be written over
[0,48] with factor 1/pi, as in SE7.

The signed comparison defect is
\[
 E_c=K_c-K_1
   =F_{48}^*M_{\Psi_c-\Psi_1}F_{48}
                -2(h_c\otimes h_c-h_1\otimes h_1).     \tag{SE8.11}
\]
This is not asserted to equal the full source defect (SE8.7): the
discarded nonnegative high-frequency excess also changes. Positivity
of K_c nevertheless proves positivity of the actual transported source.

SE7 proves K_1>=I/25000. Thus K_1 has a bounded inverse and an exact
operator transport test can be written
\[
 K_c=K_1^{1/2}
       [I+K_1^{-1/2}E_cK_1^{-1/2}]K_1^{1/2}.           \tag{SE8.12}
\]
The bracket must be nonnegative. No inverse of the unknown global
completed source is assumed here. The inverse in (SE8.12) need not be
numerically constructed: the following direct enclosure of K_(c_*)
verifies the same sign without replacing E_c by a scalar norm loss.

## 5. Executed endpoint certificate, including the entire tail

Retain exactly SE7's forty reference Legendre modes
phi_n(y)=sqrt(2n+1)P_n(2y), n=1,3,...,79, and their real Fourier
coefficients v_n(t). At c_* the finite integral block is
\[
 A^{(c_*)}_{nm}=b\delta_{nm}+
   \frac1\pi\int_0^{48}(\Psi_{c_*}(t)-b)v_n(t)v_m(t)dt
          -2c_*\sqrt{(2n+1)(2m+1)}
                         i_n(c_*/4)i_m(c_*/4).         \tag{SE8.13}
\]
The reference basis does not move; every physical term does. The
[replay](../../../proof_lab/endpoint_observer_transport_certificate.py)
uses the pinned SE7 interval primitives, its eight-node Gauss rule,
384 panels and analytic ellipse estimate. Division by c_* contracts
the complex t-plane used in SE7, so its integrand bound 100 and
per-entry quadrature error remain valid. All point evaluations are
enclosed afresh; no floating-point eigenvalue is used in the proof.

For discarded odd orders n>=81 retain SE7's bound
d_n=24^n/(2n-1)!! on v_n. The pole vector now has entries
sqrt(c_*)sqrt(2n+1)i_n(c_*/4), bounded by
e_n=4(c_*/4)^n/(2n-1)!! because sqrt(c_*)<2 and exp(c_*/4)<2.
Set
\[
 a_f=\frac{d_{81}}{1-576/(163\cdot165)},\qquad
 a_h=\frac{e_{81}}{1-(c_*/4)^2/(163\cdot165)}.
                                                        \tag{SE8.14}
\]
The leading Fourier-vector norm is below 7. The leading pole-vector
norm is below one: its full squared norm is sinh(c_*/2)-c_*/2<1.
Therefore the complete tail and coupling satisfy
\[
 \tau_D=1600a_f^2+2a_h^2<10^{-20},\qquad
 \tau_B=11200a_f+2a_h<10^{-20}.                        \tag{SE8.15}
\]
These are exact rational comparisons in the replay.

The rational midpoint matrix minus (18/10^6)I has forty strictly
positive enclosed LDL pivots. The sum of point-evaluation and
quadrature errors is below 10^{-6}, and is explicitly smaller than
18/10^6-1/60000. Consequently the exact integral block obeys
\[
 A^{(c_*)}\ge I/60000,\qquad
 K_{c_*}\ge[\min(1/60000,b-\tau_D)-\tau_B]I
           \ge I/100000.                              \tag{SE8.16}
\]
The [matrix archive](../../../proof_lab/ENDPOINT_OBSERVER_TRANSPORT_MATRIX.json)
and [result](../../../proof_lab/ENDPOINT_OBSERVER_TRANSPORT_RESULT.json)
record the forty pivot intervals, exact tails, source bounds and hashes.

### Actual signed directions explain the scalar-ledger failure

Using the independently pinned SE7 matrix and both complete entry
errors, the replay also proves
\[
 \langle\phi_1,E_{c_*}\phi_1\rangle<-3/50,\qquad
 \langle\phi_7,E_{c_*}\phi_7\rangle>1/25.              \tag{SE8.17}
\]
Thus this actual comparison defect is indefinite and has norm exceeding
3/50. Subtracting that norm from the old certified floor 1/25000 gives
a negative bound, while the complete transported comparison is positive
by (SE8.16). A failed scalar sufficient test therefore does not block
this transition. The conclusion concerns E_c of the comparison forms;
it is not a numerical enclosure of the full source defect Delta_c.

## 6. Native observer family on the entire segment

For A<=21/40, exact exponential and cosh-series budgets give
e^(3A)<5 and beta_A=2(sinh A-A)<1/16. Prime cost p_A<1 and
m_Gamma<11/2 remain unchanged. The SE6 graph estimate yields
\[
 \|f\|_X^2\le s[f]+\frac{289}{16}\|Rf\|_2^2.
                                                        \tag{SE8.18}
\]
Combining this with the physical floor 1/100000 proves the native
floor in (SE8.1). Since N_*<=11I/2, the full target satisfies
\[
 \boxed{\|\mathcal L_*f\|^2\le
       \left(1-\frac2{19868761}\right)\|A_*f\|^2,
       \qquad f\in X_{21/40}.}                        \tag{SE8.19}
\]
The exact local observer is A_*f -> L_*f on its closed event range,
extended by zero on its orthogonal complement. Its existence and
contractivity follow from the SE2 recovery theorem, with the full
debt and boundary retained.

For every c in [1,c_*], X_(c/2) is a native subspace of X_(21/40), so
the same source and observer bounds hold there. Let Y_c=A_*(X_(c/2))
and let O_* be the just-constructed observer at c_*. Then
\[
 O_c=O_*P_{Y_c},\qquad
 O_cA_*f=\mathcal L_*f\quad(f\in X_{c/2}).             \tag{SE8.20}
\]
The local observers agree on shared event vectors; changing reference
frames transports both the equation and pairing under SE2. This is
coherence of the actual target, not an arbitrary match of scalar readings.
As c increases to c_*, compact-core density gives O_c -> O_* strongly.
No differentiability or operator-norm continuity of this projection path
is asserted.

The intermediate source bounds use native inclusion. They do not claim
that every intermediate comparison K_c was separately factorized, or
that K_c is monotone in c.

## 7. What would make this transport global

The existing global condition has an equivalent moving-chart statement:
on one fixed reference aperture, certify the full transported source
(SE8.6) for a cofinal, unbounded set of scales. Every odd compact test
then fits in one of the physical images. Native continuity extends the
sign to X. Conversely a global positive source makes all those pullbacks
positive. No scale-independent strictly positive reserve is required.

More general connected chart families may replace dilations, but their
certified modules must cover every finite combination in the core, with
all mixed pairings retained. A merely connected graph or agreement on
overlaps does not give this directed coverage. For example, a matrix
with diagonal 1 and all off-diagonal entries -3/4 has positive two-by-two
principal blocks, but its quadratic value on (1,1,1) is -3/2. Every pair
passes while the joined triple fails. SE2's accumulated-Gram condition,
rather than isolated pair tests, prevents this error.

SE8 establishes the actual transport segment [1,21/20]. It does not
cross the next prime event at c=log 3 in this reference chart, establish
a repeatable rule through all later prime events, or prove the needed
cofinal family. Those are the remaining global obligations; a change
of coordinates moves them into the source equation without deleting them.

See the [source record](SE8_SOURCE_RECORD.md),
[verification scope](SE8_SCOPE.md) and [pins](SE8_SOURCE_PINS.json).
