# SE44 source comparison and development record

13 October 2026 (Asia/Kolkata). Author: Monty.

RKF parent: `3420719c074d146b242d159baa82410b6fe8bbf5`, branch
`agent/rh-source-energy-tail`.

## The specific step developed

The user requested counting-native lines and theta after the curvature
construction, followed by a TVSP version of the Surya Siddhanta mechanism.
F00-E already constructs native sine and cosine and their addition and
differential laws. Its Corollary 5.5 and final boundary explicitly defer
existence and normalization of a fundamental period. SE44 supplies this
normalization through the rational quarter-turn and a native integral.
The earlier factorial construction is consumed, not duplicated.

The new interface consists of counting lines, their formal response lifts,
the normalized native angle, a jya recurrence with transported observer
calibrations, and an explicit attachment to an actual SE42 curvature
family. Literal sine correction is proved separately, with its branch,
source reconstruction and winding record retained. The standard integral,
translation, Cayley and recurrence mechanisms carry no claim of external
priority. The comparison establishes a specific deferred step in the
inspected sources, not absence of all related mathematics elsewhere.

## Supplied notes and compass actually inspected

The two supplied TeX notes were read in full. The compass image was
visually inspected. Their raw contents are not included in this packet.

| Supplied source | SHA-256 | Role |
| --- | --- | --- |
| `surya sidhanta and curvature.tex` | `740dc601314b843011a622ae91ccfd815c9611c44fc126b3568540cf4d3d98d3` | Proposed sine correction and curvature interpretation; motivation rather than an operative proof. |
| `surya sidhanta and curvature eqvivalence.tex` | `3328ebd15153551a71c4a402f07342786a536e205c23c96dc5edcaf64896a8ec` | Proposed broader equivalences; none is assumed in the new theorem. |
| `tvsp.PNG` | `319b81422dd77143b9127f46bc86065e468cfbd60bfdf70089879a891a1a1bbf` | T above, V right, S below, P left; the declared T,V basis makes T -> V the clockwise quarter-turn. |

The existing [SE41 source audit](SE41_SOURCE_RECORD.md) already separates
the useful correction idea from invalid scalar exterior-derivative and
phase claims in the drafts. SE44 does not use scalar d(d log) as nonzero
curvature or identify every physical curvature with sine. Nor does it
infer movement laws merely from the compass drawing. Its counting
translations, pairing, response connection and retained path data are
explicitly declared. The normalized direction coordinates are not raw
dimensionful thermodynamic variables.

## Historical comparison

The consulted primary translation is Bapu Deva Sastri (1861),
[Surya Siddhanta, Chapter II, verses 15--16, printed page 15](https://en.wikisource.org/wiki/Page:English_translation_of_the_Surya_Siddhanta_and_the_Siddhanta_Siromani_by_Sastri,_1861.djvu/25).
It presents a sine-table difference/cumulative mechanism with radius
3438 and a fixed angular increment. The displayed OCR has transcription
limitations; none of SE44's algebra depends on trusting its equations.

The exact coefficient is derived here from the actual native turn:
kappa=2(1-c)=4r^2/(1+r^2). The rational replay uses r=1/3 and the radius
3438 as a calibration; its angle is not the historical table increment.
In particular a fixed approximate divisor cannot be used for every
turn. The historical passage is not evidence for attributing the
separate iteration theta -> theta+Sin(theta) to that text.

## Operative native sources

| Source | Reused result |
| --- | --- |
| [Primitive order](../../operator_foundation/theory/NATIVE_PRIMITIVE_ORDER.md) and [native algebra](../../operator_foundation/theory/01_NATIVE_ALGEBRA.md) | Typed Cut, derived scalars and observer contracts precede the finite representation. |
| [F00-E](../../theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md) | Completed radial field, factorial Euler construction, native sine/cosine, addition, norm and differential laws. The fundamental period was deferred. |
| [SE30](../../papers/rkf_completed_weil_endpoint/development/SE30_CONSTANT_LAMBDA_COUNTING_AND_CUT.md) and [SE34](SE34_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY.md) | Constant marked unit, counting formula algebra and retained formal unit completion. |
| [SE41](SE41_ORDERED_RETURN_AND_MOVING_CUT_FEEDBACK.md) | Complete response acquisition, moving calibration and source reconstruction. Its rational feedback differs from the literal sine update now proved. |
| [SE42](SE42_COUNTING_CURVATURE_AND_OBSERVER_MEMORY.md) | Counting connections, formal ordered returns, central-commutator return and mixed-coefficient observer. |
| [SE43](SE43_COUNTING_TO_EMK_SEAM_TRANSPORT.md) | Product-preserving count translations, compatible seams and noncircular integer-memory example. |
| [T51](../../theorum/51_odd_channel_exchange_law_theorem.md) | Existing Cayley exchange algebra. Reversal-odd response in SE44 is not identified with the different EMK cut grading. |
| [RT-03](../../theorum/recognition_topology/03_principal_holonomy_blindness_and_lifted_memory.md) | Principal-phase blindness and separately retained winding. SE44 derives the native angular normalization before using its period unit. |

The finite Python 3.12 replay reuses the existing rational matrix,
counting polynomial and detached observer adapters. It creates no second
operator engine. Pi and sine enclosures use exact rational remainders
and outward dyadic rounding, not floating-point transcendental values.

Source pins bind local byte identity and the replay inputs. Supplied-source
hashes and the historical reference are provenance, not extra observer
measurements. Live navigation stays unpinned. See [scope](SE44_SCOPE.md)
for the distinction between written proofs, finite readings and the
inherited whole-engine pin failure.
