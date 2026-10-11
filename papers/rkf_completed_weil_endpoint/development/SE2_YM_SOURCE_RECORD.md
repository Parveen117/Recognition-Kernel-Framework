# SE2: exact Yang–Mills source record

11 October 2026. This record identifies the existing operator-path results
used by [SE2](SE2_OBSERVER_PATH_OPERATOR_CERTIFICATE.md). It is a reading
record and source crosswalk, not a new execution of their certificates.

## Sources actually read

| Packet | Repository-relative path | Local Git revision |
| --- | --- | --- |
| YC57 | `physics/yc57/YC57_MOVING_OBSERVER_EQUATION.md` | `e5f393044a8f4ab80ce7c95833f1ad189c05bd54` |
| YC57 companion | `physics/yc57/ADAPTIVE_OBSERVER_AND_PHYSICAL_DEFECT.md` | `e5f393044a8f4ab80ce7c95833f1ad189c05bd54` |
| YC58 | `physics/yc58/YC58_REFERENCE_INDEPENDENT_RECORD.md` | `dbeedb1a14af51b337d75a45b2acd8a565e7dfff` |
| YC58 scope | `physics/yc58/SCOPE_RECORD.md` | `dbeedb1a14af51b337d75a45b2acd8a565e7dfff` |

These are in local Git history for `Parveen117/extra-ideas`, inspected
through a checkout at `1e5d8c11978453ff61f227db057decbfa4f10d4d`.
Source hashes and blob identifiers are in [SE2_SOURCE_PINS.json](SE2_SOURCE_PINS.json).
The GitHub integration returned 404 when asked for the YC58 commit.
The record therefore does not represent that revision as a verified
remote publication. No attempt was made to push or modify another repo.

## YC57: observer in the equation

For a declared bounded evolution \(\dot\psi=L\psi+f\) and norm-C1
orthogonal \(P\), \(Q=I-P\), write \(x=P\psi,\ y=Q\psi\). YC57 derives

\[
 \dot x=(\dot P+PL)Px+(\dot P+PL)Qy+Pf.
\]

The complement has its own equation. The moving frame includes
\(\Gamma=W^\dagger\dot W\); eliminating the hidden block retains
initial hidden states, hidden forcing and the chronological kernel
\(B(t)V_D(t,r)C(r)\). It is not just an instantaneous Schur matrix.

Under simultaneous frame transport, the propagator obeys
\(T'(t,s)=U(t)T(t,s)U(s)^\dagger\). Endpoint sources and every port
must move with it. The source-history reading is then unchanged,
although neither endpoint coordinate is fixed.

The companion isolates the finite-column defect
\(E=Q(LJ-\dot J)\), and on its supplied seed obtains
\(E^\dagger E=V^\dagger D_{hh}V+R_h^\dagger R_h\).
An adaptive velocity can remove the within-seed term without
eliminating outside-seed physical action. SE2 uses that distinction:
changing the observer does not authorize setting its physical residual
to zero.

## YC58: the full record, pairing and routes

The source record is
\[
 Z_v(w)=B_v^\dagger W_{w,v}B_v,
 \qquad
 K_v(u,w)=B_v^\dagger W_{u,v}^\dagger W_{w,v}B_v.
\]

All source entries and ordered words are kept. Equality of the full
dagger-closed record determines a unique source/word-preserving unitary
on the reached sector, not on arbitrary unseen summands.

Route errors compose after labels and pairings are aligned. Different
composite alignment maps must either agree or retain their holonomy.
This is the basis for SE2's exact operator-defect composition law.
SE2's single sign form is a narrower target than YC58's complete record;
equal sign forms alone do not imply equal future observations.

## Other inputs and scope

RKF N03/N06/N09/N10/N11 and WC5 were read in the unchanged canonical
`operator_foundation`. EMK-C1 was read in the Publications source
checkout, with revision and hash recorded separately.

YC55's seam-transformed join, YC61's transported count-module joins,
DS1's diagonal/mirror discussion, and the RH-to-YM transfer map were
consulted for context. Their physical lattice gap, scale, cost and
continuum results are not hypotheses silently transferred to RH.
In particular, DS1's older quoted T34--T39 numbers are not used to
override the source-accounting boundary identified in SE1.

The carried method is: full operator before compression; complete
source and complementary pairing; observer connection inside the
equation; typed source transport; preserve mixed terms. It does not
identify RH and Yang–Mills as the same physical problem.
