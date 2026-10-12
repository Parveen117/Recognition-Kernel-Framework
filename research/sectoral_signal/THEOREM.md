# SS1 SP–VT complementary measurement and signal recovery

Date: 12 October 2026. Programme author: Monty Dabas.
Status: written proofs under explicit finite-carrier hypotheses; exact finite
controls are separate. No external priority or proof-assistant verification claimed.

## 1. Native carrier and diagram adapter

Start with the established cut field, typed composition and dagger in
[N01–N06](../../operator_foundation/theory/01_NATIVE_ALGEBRA.md).
Let X,Y be finite free cut modules, M:X→Y a declared response morphism,
L:X→Z a recognition target, and C:X→E, D:Y→F actual readouts.
The retained Smriti packet contains both readings with their channel labels,
orientation, calibration and common source identifier. Composition is ordered.

For norm statements only, admit positive pairings and work in compatible
whitened coordinates; dagger then has its represented adjoint meaning.
Raw thermodynamic Hessians are not assumed positive metrics. None of these
assumptions selects a physical clock, physical detector or material.

The supplied tvsp.PNG has T at +y, V at +x, S at −y and P at −x.
Its blue path T→P→S and yellow path V→S→P share the SP angular sector
with opposite directions (their drawn radii differ). The complementary
paths T→V→S and V→T→P instead share TV. Those complementary paths are
our declared reconstruction, not a second supplied drawing. A T/V label
permutation alone does not establish this change of paths.

The measurement adapter uses x=(δS,δP), y=(δT,δV)=Mx. A VT readout
uses J y with J=[[0,1],[1,0]] and correspondingly calibrated D; this
output ordering changes no rank. All quantities in numerical controls are
dimensionless perturbations, not raw physical T,V,S,P values.

When H(S,P) is C² and its gradient is locally invertible,
y=∇H(x), F(y)=H(x(y))−y·x(y) satisfies ∇F=−x and
∇²F=−(∇²H)⁻¹ at corresponding points. This follows by differentiating
dF=−x·dy and y=∇H(x). At the tangent level M=∇²H.
This local inverse-chart statement is not needed for SS1 below, which
continues to work for singular M. The finite linear statements apply
exactly to a linear model or to tangent responses, not arbitrary finite
increments of a nonlinear constitutive law.

## 2. Complementary measurement theorem

Define the retained observation and positive Gram by

    A x = (C x, D M x),       G = C†C + M†D†D M.

Then:

1. ker A = ker C ∩ ker(DM).
2. L is exactly recoverable iff ker A ⊆ ker L.
3. The added independent reading rank is
   rank A − rank C = rank((DM)|ker C).
4. If A is injective, G>0 and the minimum-norm decoder is
   O=L G⁻¹ A†. Its squared norm is ||L G⁻¹ L†||.
5. If G≥γ I with γ>0, measured data d=Ax+e give
   ||G⁻¹A†d−x||≤||e||/√γ.

Proof. The first statement is the kernel of a direct sum. For the second,
define O(Ax)=Lx; it is well-defined exactly under the kernel inclusion.
Rank-nullity proves the third statement. Injectivity gives positive G.
The displayed decoder agrees with L on every state; it vanishes on
(ran A)⊥. Every other decoder has the same restriction to ran A, so its
norm is no smaller. Multiplication gives OO†=LG⁻¹L†. For L=I this
also proves the noise bound. QED.

This consumes the existing N03/SR-04 observer mechanism; the new work
here is its explicit SP–VT adapter and residual classification.
Two readings must refer to the same state, or a known transport must
be included in M. Postprocessing Cx cannot manufacture an unavailable
DMx: (Cx,RCx) has exactly the same kernel as C.

### Cross-sector recovery corollary

Write x=(s,p) and the measured output t=A₀s+Bp. If s and t are read,
then r=t−A₀s=Bp. The remaining invisible directions are exactly ker B.
If B has full column rank, p=(B†B)⁻¹B†r, with ordered products retained.
For errors e_s,e_t, the recovery error is

    δp=(B†B)⁻¹B†(e_t−A₀e_s).

For scalar B=b≠0, p=(t−as)/b and
|δp|≤(|e_t|+|a||e_s|)/|b|. A very small nonzero coupling may be
algebraically sufficient but badly conditioned. If B is rectangular,
(I−B(B†B)⁻¹B†)r detects inconsistency; noise in ran B remains
indistinguishable from a change in p without further information.

## 3. Recovery through a singular response chart

Consider the exact family

    M_ε = [[1,1],[1,1+ε]],       det M_ε=ε,
    C=[1,0],                    D=[1,0].

For every real ε, including ε=0,

    A = [[1,0],[1,1]],
    A⁻¹ = [[1,0],[-1,1]],
    G = [[2,1],[1,1]] ≥ (1/3)I.

Indeed det(G−I/3)=1/9 and both diagonal entries are positive.
Thus observing s and t=s+p recovers p=t−s, uniformly as the full
inverse M_ε⁻¹ becomes singular. The target p has squared decoder
norm 2, not at most 1. Recovery is not contractivity.

This proves a concrete distinction: failure of the output-only inverse
need not be failure of a complementary observer. A direct input channel
supplies the information missing from the singular output map. It does
not recover missing information from output data alone, and does not
remove any established RH source singularity.

## 4. Exact decomposition of the complete signal

For complete measured input/output packet z=(u,v)∈X⊕Y set

    U=[I;M],       N=[−M,I],
    G₀=I+M†M,      H₀=I+MM†,
    x̂=G₀⁻¹(u+M†v),     r=v−Mu.

For every M, including rectangular and singular ones,

    z = U x̂ + N†H₀⁻¹r,
    ⟨U x̂,N†H₀⁻¹r⟩=0,
    ||u||²+||v||² = ⟨x̂,G₀x̂⟩ + ⟨r,H₀⁻¹r⟩.

Proof. NU=0, U†U=G₀ and NN†=H₀. These last two matrices are
positive definite, since their quadratic forms are ||w||²+||Mw||²
or ||w||²+||M†w||². U and N† have orthogonal ranges with dimensions
dim X and dim Y, so they exhaust X⊕Y. Their orthogonal projections
are UG₀⁻¹U† and N†H₀⁻¹N. Apply the projection identity to z and use
Pythagoras. QED.

The two sectors are the signal compatible with the declared response
graph and the incompatibility residue. They are orthogonal after the
declared metric normalization. This is not automatic orthogonality of
raw caloric, mechanical, cut-parity and curvature labels. Complex
amplitudes are kept until after projection; their phases are not erased.

Complete u,v data are required for this formula. For partial data use
the corresponding ran A projection; do not invent unmeasured channels.

### What a zero residual does and does not certify

If the actual map is M+E and sensor errors are e_x,e_y, then

    r=Ex+e_y−M e_x.

This is an exact separation of model mismatch and sensor contribution,
but those terms cannot be individually identified from r alone.
For any h, the coherent error (e_x,e_y)=(h,Mh) has r=0 while the
decoded state is x+h. Thus closed-cycle consistency is not proof of
zero measurement error. A model-generated output v=Mu passes this
check identically and is not an independent confirming measurement.
No component here is called curvature without a declared connection
and the required transport/commutator identity.

## 5. Source-preserving use in certificates

Suppose an existing source has an exact decomposition

    Q = Q₀ + R†R − L†L.

In the same admitted pairing, choose an actual orthogonal projection P
on the residual event carrier. Then exactly

    Q = Q₀ + (PR)†PR + ((I−P)R)†((I−P)R) − L†L.

If Q₀>0, the lower comparison Q₀+(PR)†PR−L†L is nonnegative iff

    ||L (Q₀+(PR)†PR)⁻¹ L†|| ≤ 1.

Proof. Orthogonality cancels the two cross terms. For B=Q₀+(PR)†PR,
conjugate B−L†L by B⁻¹/²; nonnegativity is equivalent to the squared
norm of LB⁻¹/² being at most one. QED.

This is the lawful route for turning previously unmeasured residual
energy into a better certificate, consistent with SE19/SE23. Duplicating
a coordinate or adding an independent positive Gram without subtracting
its cost from the retained source changes Q and is not a proof improvement.
This stage does not select a new actual RH residual coordinate or execute
a smaller-eta source certificate. No eta improvement is claimed.

## 6. Status and lineage

- Written finite-module recovery and graph-decomposition proofs: supplied.
- Exact declared controls and planted-fault rejection: see RESULT.json.
- N03/SR-04 supply observer repair; Thermo-10 supplies positive metric
  cut-square context. Standard finite linear algebra is not claimed new.
- No empirical sensor, arbitrary nonlinear/global inverse, full continuum,
  RH eta-zero or Yang–Mills mass-gap conclusion is established.
- No inference that SP–VT path overlap alone fixes M or the noise law.
- The canonical operator engine and historical source pins are unchanged.

Sources: [native algebra](../../operator_foundation/theory/01_NATIVE_ALGEBRA.md),
[sensor repair](../../theorum/stratified_recognition/04_physical_observer_minimum_sensor_repair.md),
[cut-square response](../../theorum/thermodynamics/10_thermodynamic_cut_square_response_decomposition.md),
[thermodynamic exclusions](../../theorum/thermodynamics/09_scope_exclusions.md).
