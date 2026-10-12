# SE28 Circular calibration, TVSP flat specialization and faithful RH transport

12 October 2026. Owner: Monty.

This stage implements circular numerical readings with integer Smriti,
a whole moving cut line, a positive measurement unit and a resolved
zero-unit fibre. The existing TVSP response tetrad supplies a dimensionless
flat-sector coordinate. A declared native Cayley adapter turns this coordinate
into a phase; with the actual arithmetic prime labels, its infinite Euler
family recovers the Riemann zeta function exactly in the flat sector.
Its logarithmic derivative recovers the prime-power weights as well.

Separately, a unitary circle-and-sheet representation transports the entire
corrected RH source, including Gamma events, primes, pole and native graph
norm. The two operations have different roles: calibration transports the
same source; a nontrivial Euler phase changes its arithmetic data. No gain
in eta follows from calibration. SE27's global eta 1079/2000 remains the
strongest executed anchor. RH and eta zero are not proved here.

## 1. Existing native and TVSP inputs

Typed cuts, cut scalars, derived iota, lawful composition, targets and Smriti
precede the admitted representations. This application imports the canonical
`native_operator.cjs` and `native_paths.cjs`; it does not copy their engine.
An integer sheet records scalar turn memory. It does not replace the full
ordered residue history of a noncommutative path.

The thermodynamic response archive defines the uniformly entropy-scaled
tetrad Lambda=(lambda_p,lambda_v,lambda_s,lambda_t) and proves, on its
equilibrium constitutive charts,

\[
 I_{\rm th}=\frac{\lambda_p}{\lambda_v}
               \frac{\lambda_t}{\lambda_s}=1.
 \tag{SE28.1}
\]

Use its corrected channel types and normalized ratios. On the regular
response sector I_th>0 define

\[
 \lambda_\Sigma=r:=\frac{I_{\rm th}-1}{I_{\rm th}+1},\qquad
 \chi_r=\frac{1+\iota r}{1-\iota r}.
 \tag{SE28.2}
\]

This is an explicit adapter from the existing TVSP lambda data, rather than
an identification of the RH shift eta with a new scalar called lambda.
The choice of Cayley adapter is declared; uniqueness from the TVSP hierarchy
is not asserted. The zero of r agrees with the archive's log(I_th)=0.
Neither scalar is the entire connection-curvature tensor. General off-flat
tetrads below are regular response data, not asserted physical equations
of state satisfying all equilibrium constitutive relations.

**Theorem 1 (TVSP phase and calibration invariance).** In this sector,

\[
 |\chi_r|^2=1,\qquad
 \chi_r=1\ \Longleftrightarrow\ r=0
       \ \Longleftrightarrow\ I_{\rm th}=1.
 \tag{SE28.3}
\]

Common multiplication of the tetrad by a nonzero calibration leaves these
quantities unchanged. Reversing both ratio pairs sends I_th to its inverse,
r to -r and chi_r to its dagger.

**Proof.** The denominator has squared norm 1+r^2>0. Multiplying by its
dagger proves unitarity; chi_r=1 forces 2 iota r=0. Common scale cancels
in both ratios. Substitution of I_th^(-1) proves the reversal laws. QED.

Flat closure does not require the four response coordinates to vanish.
For example (-2,-4,-3,-6) has I_th=1. Raw all-zero response coordinates
make the ratios undefined; they are not a certificate of flat closure.

## 2. Numbers as lifted circular readings and a whole cut line

Work first in the admitted real-valued measurement chart. Let ell>0 be
the calibration unit and alpha a lifted cut angle in turns. A reading x
has the unique packet

\[
 N=x/\ell,\quad n=\lfloor N-\alpha\rfloor,\quad
 t=N-\alpha-n\in[0,1),\qquad
 x=\ell(n+\alpha+t).
 \tag{SE28.4}
\]

Its circle phase is exp(2 pi iota(alpha+t)); its integer sheet n remains
stored separately. The geometric cut is the whole line through the two
opposite phases alpha and alpha+1/2, with its ray/side label retained.
Explicitly, b=floor(2t) and u=2t-b give

\[
 N=n+\alpha+\frac{b+u}{2},\qquad b\in\{0,1\},\quad0\le u<1.
 \tag{SE28.5}
\]

The line, calibration, side and matching maps comprise the reference;
scalar zero is a separate typed object. Identifying the two sides of
the line would alias a half turn. Forgetting n would alias full turns.
Varying ell and the native state leaves a whole reference section, not
one privileged origin point. SE27's connected measurement planes can
be transported along with this chart.

**Theorem 2 (lift, transport and memory).** Equation (SE28.4) is reversible.
For an increment a, the new sheet and phase are

\[
 k=\lfloor t+a/\ell\rfloor,\quad n'=n+k,\quad
 t'=t+a/\ell-k.
 \tag{SE28.6}
\]

For a cut change alpha->beta, replace a/ell by alpha-beta in that formula.
For a unit change ell->ell', decode x and apply (SE28.4) with ell'.
These transformations preserve x, obey composition and invert on their
declared domains. Canonical native path composition adds integer sheet
memory even when the endpoint shadow returns to the same value.

**Proof.** The decomposition of a real number into its floor and fractional
part is unique. Apply that decomposition after adding the indicated
increment. Two successive translations or chart changes and their direct
composition have the same decoded x and final chart, hence identical
packets. The canonical path law adds sheet integers under admissible
composition. In particular, arrows with the same endpoints and sheets
one and two have identical endpoint shadows but are distinct paths. QED.

This is a faithful representation of real-valued readings in the admitted
chart, not a replacement axiom asserting that every native object is a
single real number. Each independent target keeps its own typed data.

## 3. Zero measurement unit with normalized data retained

**Theorem 3 (resolved zero calibration).** For a fixed normalized reading N,
the packet (ell,N) and map x=ell N extend to ell=0 while retaining N.
For ell>0, x/ell=N; the normalized limit as ell decreases to zero is N.
No division by zero is performed. The map (0,N)->0 is many-to-one, so
the raw zero does not determine the retained reading.

For a fixed regular tetrad shape Lambda_bar, the family
Lambda_ell=ell Lambda_bar likewise retains I_th, r and chi_r for ell>0.
Its resolved zero fibre stores Lambda_bar or its appropriate common-scale
class. The value of r there depends on the retained shape.

**Proof.** The product map (ell,N)->ell N is continuous at zero. Projection
onto N is already defined on the product and agrees with x/ell away from
zero. The same argument applies to a fixed tetrad shape, since its common
scale cancels in (SE28.1). Shapes (1,1,1,1) and (2,1,1,1) both collapse
to the raw zero vector, but have invariants one and two. Thus collapse
alone cannot select the flat shape. QED.

The measurement unit ell and TVSP's derived flat coordinate lambda_Sigma
are consequently retained as distinct data. A universal calibration law
relating time, energy and other physical quantities is not derived here.

## 4. The full RH carrier on cut circles with helical gluing

Use SE19/SE25's auxiliary H=L2(0,infinity), the odd isometry J and dense
native graph pullback J^(-1)X. For ell>0 define

\[
 (C_\ell h)(n,t)=\sqrt\ell\,h(\ell(n+t)),
 \quad n\ge0,\quad0\le t<1.
 \tag{SE28.7}
\]

**Theorem 4 (unitary circle/sheet source representation).** C_ell is a
unitary onto the countable sheet carrier l2(N;L2[0,1)). For continuous
core states the cut traces obey

\[
 H_n(1)=H_{n+1}(0).
 \tag{SE28.8}
\]

These are helical seam conditions. Independent periodicity on each sheet
would change the source domain. L2 states themselves have no point trace;
the trace statement is only asserted on the stated regular core.

**Proof.** Partition (0,infinity) into intervals [ell n,ell(n+1)). The
change of variable x=ell(n+t) gives

\[
 \sum_{n\ge0}\int_0^1|C_\ell h(n,t)|^2dt=\int_0^\infty|h(x)|^2dx.
\]

The inverse is h(x)=ell^(-1/2)H(floor(x/ell),{x/ell}); it proves
surjectivity. At the common endpoint of adjacent intervals the two core
values agree, yielding (SE28.8). QED.

On the full line the analogous unitary uses n in Z and x=ell(n+t+alpha),
so the reference cut can move. The odd subspace is transported exactly;
at alpha=0 its constraint is H(-n-1,1-t)=-H(n,t) almost everywhere.
For general alpha, use the inverse image of x->-x, retaining its sheet
carry. This full-line construction transports the same J^(-1)X states.

Define X_ell=C_ell J^(-1)X with the transported native norm

\[
 \|H\|_{X_\ell}:=\|J C_\ell^{-1}H\|_X.
 \tag{SE28.9}
\]

The simple unweighted sheet norm is not substituted for this graph norm.
Let v_ell=C_ell v, D_ell=C_ell D C_ell^(-1) and
W_ell(n,t)=W(exp(-ell(n+t)/2)). Then the exact SE25 source identity is

\[
\begin{split}
 s[J C_\ell^{-1}H]+\eta\|H\|_{X_\ell}^2
  ={}&\langle H,M_{W_\ell}H\rangle
 +(1-\eta)\langle H,D_\ell H\rangle\\
 &+D_P[J C_\ell^{-1}H]-4|\langle v_\ell,H\rangle|^2
 +\mathcal E_\eta[J C_\ell^{-1}H].
\end{split}
 \tag{SE28.10}
\]

Every Gamma remainder, prime tail and graph energy stays in this identity.
It follows by unitary substitution on the auxiliary carrier and exact
transport of the native norm. The SE27 source certificate therefore gives

\[
 s[J C_\ell^{-1}H]+\frac{1079}{2000}\|H\|_{X_\ell}^2
 \ge\frac1{492000}\|H\|_{X_\ell}^2
 \quad\text{for every }\ell>0.
 \tag{SE28.11}
\]

This is a theorem transferring the published bound, not a new smaller
anchor or a rerun of its 63496-cell interval certificate. Moving the full
line cut alpha changes only the unitary chart and yields the same conclusion.

## 5. Explicit prime carries, Gamma sheets and pole

For a full-line prime event m with displacement a=log(m), the translated
coordinate x-a at x=ell(n+t+alpha) has

\[
 k=\lfloor t-a/\ell\rfloor,\qquad
 n'=n+k,\qquad t'=t-a/\ell-k.
 \tag{SE28.12}
\]

Thus the phase and the turn carry together reproduce every prime-power
translation. No reduction of log(m)/ell modulo one is used on its own.
The exact prime event from SE19.8 transforms, with F the full-line packet
of f=Jh and y=x-log(m), to

\[
 \sqrt{a_m m_0(x)m_0(y)q_P(x)q_P(y)}
 \left(\frac{F(n,t)}{q_P(x)}-
       \frac{F(n',t')}{q_P(y)}\right),
 \quad a_m=\Lambda(m)/\sqrt m.
 \tag{SE28.13}
\]

Here m_0 denotes the source's multiplication weight, not the event index.
The factor sqrt(ell) in the event-space transform cancels the inverse
factor in f. Applying the same change of variables to both Gamma event
arguments x=ell(n+t), y=ell(j+u) gives the unscaled Gamma analysis

\[
 \sqrt{\frac\ell2 k_\beta^-(x,y)q_G(x)q_G(y)}
 \left(\frac{H(n,t)}{q_G(x)}-
       \frac{H(j,u)}{q_G(y)}\right).
 \tag{SE28.14}
\]

The pole vector is exactly

\[
 v_\ell(n,t)=\frac{\sqrt\ell}{2}
 \left(e^{-\ell(n+t)}-e^{-2\ell(n+t)}\right).
 \tag{SE28.15}
\]

The change of variables proves preservation of all three targets and their
full mixed pairings. At ell=2a log(2), positive integer a, each monomial
pair z^p,z^q has first-M-sheet mass and remaining mass

\[
 \frac{2}{p+q}(1-2^{-aM(p+q)}),\qquad
 \frac{2}{p+q}2^{-aM(p+q)}.
 \tag{SE28.16}
\]

Their sum is the original half-line pairing. The replay applies this
identity to every entry of SE27's actual three-direction event Gram,
with all polynomial cross terms retained, and to the nonzero Gamma-blind
pole pairing 45607/433125. Outward logarithm intervals additionally
certify concrete carries for eighteen actual prime-power translations.
A crossing interval straddling a cut is rejected, not rounded to one side.

## 6. A zero-unit limit cannot discard the infinite sheet direction

**Theorem 5 (fixed-state escape).** For a fixed nonzero h in H,
C_ell h converges weakly to zero as ell decreases to zero on the fixed
sheet carrier, but has no strong limit there. For every fixed M,

\[
 \sum_{n=0}^{M-1}\int_0^1|C_\ell h(n,t)|^2dt
 =\int_0^{M\ell}|h(x)|^2dx\longrightarrow0,
 \qquad\|C_\ell h\|=\|h\|>0.
 \tag{SE28.17}
\]

**Proof.** Absolute continuity of the integral proves the finite-sheet
limit. Finite-sheet test vectors are dense in the sheet carrier and the
norms are uniformly bounded, proving weak convergence to zero. A strong
limit would equal that weak limit and have norm zero, contradicting
unitarity. QED.

This does not contradict Theorem 3. A fixed normalized number has x=ell N
shrinking with ell; a fixed physical source state instead spreads into
arbitrarily large sheet indices. Identification by C_ell^(-1) retains the
same source exactly, whereas deleting high sheets loses its information.
Neither limiting procedure improves eta by itself.

## 7. Infinite zeta family from the TVSP flat-sector phase

Supply the existing arithmetic prime labels and positive lengths log(p).
These are the same arithmetic data already present in the RH source;
they are not claimed to be generated by TVSP geometry. For ell>0 define
L_p=ell log(p) and the spectral argument sigma=s/ell. For real r from
(SE28.2), set

\[
 Z_r(s)=\prod_p\left(1-\chi_r e^{-(s/\ell)L_p}\right)^{-1}
       =\prod_p(1-\chi_r p^{-s})^{-1}.
 \tag{SE28.18}
\]

**Theorem 6 (flat zeta specialization and prime-power recovery).** For
Re(s)>1, the product and logarithmic series converge absolutely, locally
uniformly in s and uniformly in real r. They obey

\[
 Z_r(s)=\sum_{n\ge1}\frac{\chi_r^{\Omega(n)}}{n^s},\qquad
 \log Z_r(s)=\sum_p\sum_{k\ge1}\frac{\chi_r^k}{k p^{ks}},
 \tag{SE28.19}
\]

where Omega counts prime factors with multiplicity, and

\[
 -\frac{Z_r'(s)}{Z_r(s)}
 =\sum_p\sum_{k\ge1}\frac{\chi_r^k\log p}{p^{ks}}.
 \tag{SE28.20}
\]

Consequently

\[
 I_{\rm th}=1\quad\Longrightarrow\quad r=0,\ \chi_r=1,\quad
 Z_0(s)=\zeta(s),\quad
 -Z_0'/Z_0=\sum_{m\ge2}\Lambda(m)m^{-s}.
 \tag{SE28.21}
\]

**Proof.** On Re(s)>=1+epsilon, |chi_r|=1 bounds the absolute logarithmic
series by sum_p p^(-1-epsilon)/(1-p^(-1-epsilon)), in turn bounded by a
constant times the convergent integer series sum_{n>=2} n^(-1-epsilon).
The same argument with log(p), on any slightly smaller right half-plane,
justifies termwise differentiation. Expansion of each geometric factor
and unique prime factorization give the coefficients chi_r^Omega(n).
Equations (SE28.3) and the Euler product identify the flat member.
The factor k from differentiating p^(-ks) cancels its logarithmic-series
denominator, leaving log(p), not k log(p), at a prime power. QED.

The classical identity used for the final identification is recorded in
[NIST DLMF 25.2.1 and 25.2.11](https://dlmf.nist.gov/25.2).
Only that arithmetic analytic chart is imported; no RH premise is used.
The finite controls verify all coefficients through n=256, the full
prime-multiplicity convolution for the logarithmic derivative, and an
exact rational tail control at s=2. They do not replace this infinite proof.

At the flat member the conventional analytic continuation of zeta, and
the T40 Gamma/pole completion, can be retained. No analytic continuation
of every nonflat Z_r through Re(s)<=1 is asserted. In particular, (SE28.20)
is not evaluated as an absolutely convergent series on the critical line.

The unit ell cancels from (SE28.18) for ell>0. Its normalized resolved
zero fibre retains the same factors; substituting ell=0 into the raw
lengths while holding the unnormalized spectral argument fixed is a
different, generally singular operation. In the unnormalized argument,
the logarithmic derivative must also be divided by ell before comparison
with (SE28.20). No source amplitude is gained by changing its units.

## 8. What flatness does and does not establish

The flat specialization (SE28.21) is now a proved statement about the
specified TVSP-derived scalar phase family, conditional only on its declared
regular response and arithmetic inputs. It is not a theorem equating RH
with the whole native connection's flatness.

**Theorem 7 (two necessary distinctions).** Vanishing local connection
curvature need not give trivial circle holonomy. Trivial reference transport
need not give positivity of an independent source.

**Proof.** On a circle coordinate t modulo one, A=iota pi dt has dA+A wedge
A=0, but holonomy exp(-iota pi)=-1. It is therefore flat locally with a
nontrivial return. For the second statement use a constant identity
reference and self-adjoint source diag(1,-1). The negative unit vector
persists under every joint unitary transport of source and state. QED.

Accordingly the remaining RH problem needs a source-specific theorem
connecting the required native flatness/recognition condition to the complete
unshifted prime-Gamma-pole form and then to the exact RH criterion. The
current corrected-source and historical K0 boundaries remain in force.
The arithmetic identification of Z_0 supplies the function; it does not
locate its nontrivial zeros. No claim that all prior physics or index
theorems have been subsumed is imported here.

The [source replay](../../../proof_lab/endpoint_circular_calibration_certificate.py),
[native application controls](../../../proof_lab/endpoint_circular_calibration.cjs),
[result](../../../proof_lab/ENDPOINT_CIRCULAR_CALIBRATION_RESULT.json),
[scope](SE28_SCOPE.md), [source record](SE28_SOURCE_RECORD.md) and
[pins](SE28_SOURCE_PINS.json) separate the written theorems, exact controls,
inherited certificate and remaining source-identification obligations.
