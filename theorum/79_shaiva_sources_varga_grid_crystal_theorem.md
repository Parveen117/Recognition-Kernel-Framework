# Śaiva Sources II — the varga/manner grid of the Māheśvara code and the crystal theorem of recognition

1 November 2026. Second quoted-source batch after
[theorum/78](78_shaiva_sources_maheshvara_spanda_pratyabhijna_theorem.md),
on the same two carriers: the 43-token order of the fourteen Māheśvara
sūtras read through 1.1.71 (recognized initial, remembered marker), and
the [MR-03](morphic_recognition/03_cocycle_lifted_path_recognition.md)
memory lift. As before, the Sanskrit supplies definitions, the certificate
supplies verdicts; what has no certified object is refused by name.

## 1. Sources (quoted)

**S1 — Śiva-sūtra 3.19** (Vasugupta): *kavargādiṣu māheśvaryādyāḥ
paśumātaraḥ* — in the ka-varga and the other groups of letters reside the
mothers of bound souls, Māheśvarī and the rest. The vargas are the
place-of-articulation classes of the stops; Pāṇini names them with the
*u*-marker of **1.1.69 aṇudit savarṇasya cāpratyayaḥ** (*ku, cu, ṭu, tu,
pu*). Which mother presides over which varga is **not** used.

**S2 — Īśvara-pratyabhijñā-kārikā 1.5.11** (Utpaladeva):

> svabhāvam avabhāsasya vimarśaṁ vidur anyathā |
> prakāśo 'rthoparakto 'pi sphaṭikādijaḍopamaḥ ||

— reflective awareness (*vimarśa*) is the very nature of manifestation;
otherwise light, though coloured by its objects, would be inert like a
crystal.

**S3 — Vijñāna-bhairava 26**: *na vrajen na viśec chaktir marudrūpā
vikāsite | nirvikalpatayā madhye tayā bhairavarūpatā* — when the power in
the form of breath neither goes out nor comes in, in the middle, …

**S4 — Taittirīya Āraṇyaka 10.45 (Aghora)**: *aghorebhyo 'tha ghorebhyo
ghoraghoratarebhyaḥ | sarvebhyaḥ sarvaśarvebhyo namaste astu
rudrarūpebhyaḥ*; **Taittirīya Saṁhitā 4.5.8** (Śatarudrīya): *namaḥ
śivāya ca śivatarāya ca*.

## 2. Results

### T1 The varga/manner grid: place is udit, manner is pratyāhāra

Read the 25 stops of the Māheśvara order as a 5 × 5 grid: rows by manner
(nasal; voiced aspirate; voiced; voiceless aspirate; voiceless), columns
by varga (*ka, ca, ṭa, ta, pa*). Certified:

- stop ↦ (manner row, varga column) is a bijection;
- **no varga is an interval** of the Māheśvara order and no varga equals
  any of the 294 pratyāhāra sets: the udit device of 1.1.69 is not
  expressible by 1.1.71 — place and manner are two different codes;
- the manner rows **are** pratyāhāras: nasal = `ñam`, voiced aspirate =
  `jhaṣ`, voiced = `jaś`, voiceless = `cay`; the voiceless aspirates alone
  are **no** pratyāhāra — only their union with the voiceless row (`khay`)
  and the cross-cut `chav = ch ṭh th c ṭ t` (8.3.7) are;
- the stops are listed manner-major, and sūtras 7, 8–9, 10 share one varga
  permutation (*ca, pa, ka, ṭa, ta*), while sūtra 11 uses (*ka, pa, ca,
  ṭa, ta*) and sūtras 11–12 end with (*ca, ṭa, ta, ka, pa*).

### T2 The code's freedom: exactly 2304 orders, leaders forced, the shared permutation not

**Theorem.** Fix the fourteen sūtra boundaries and markers. Among all
reorderings of the sound tokens *within* their sūtras, exactly **2304**
leave every one of the 42 used pratyāhāra sets unchanged. Sūtras 1, 3, 4,
5, 6, 8 and 14 are rigid; sūtra 2 (*ṛ ḷ*), sūtra 7's tail (*ṇ n*), sūtra
12 (*k p*) and sūtra 13's tail (*ṣ s*) each admit 2 orders; sūtra 11
admits 4 (*kh ph* and *ṭh th* and *ṭ t* in pairs, with *ch* and *c*
pinned); sūtras 9 (*gh ḍh dh*) and 10's tail (*g ḍ d*) admit all 6.
Wherever a used pratyāhāra starts, its initial is forced to lead the
sūtra (*a, e, ai, h, l, ñ, jh, j, kh, ś*).

**Proof.** Enumerated sūtra by sūtra (the sets of different sūtras are
independent once boundaries are fixed, because a pratyāhāra is determined
by the position of its initial inside its own sūtra and by the marker's
sūtra); 2 · 2 · 6 · 6 · 4 · 2 · 2 = 2304. ∎

Consequence: the varga permutation (*ca, pa, ka, ṭa, ta*) that sūtras 7,
8–9 and 10 share is **not** forced by Pāṇini's use of the code — in sūtras
9 and 10 the code forces only the leaders *jh/bh* and *j, b* and leaves
the remaining three stops free. The uniform permutation is a regularity
of the sūtras beyond their function as an interval code; S1 is cited for
the varga partition, nothing about the presiding mothers is claimed.

### T3 The crystal theorem (IPK 1.5.11)

**Theorem.** Let the base be a commutative monoid of arrows and let
`ω_B(b, a) = bᵀ B a` be a bilinear memory cocycle (theorum/78 T4). Then

1. every coboundary `δα(b, a) = α(a + b) − α(a) − α(b)` of a 1-cochain is
   **symmetric**;
2. a symmetric bilinear cocycle `S` is the coboundary of
   `α(a) = S(a, a)/2` over `Q`;
3. a nonzero antisymmetric bilinear cocycle is never a coboundary;
4. hence `ω_B` is recognition-blind on reorderings (theorum/78 T4) **iff**
   `B` is symmetric **iff** `ω_B` is a coboundary over `Q` — its class is
   zero.

**Proof.** (1) `a + b = b + a`. (2) `α(a+b) − α(a) − α(b) =
½(S(a+b, a+b) − S(a,a) − S(b,b)) = S(a, b)` by bilinearity and symmetry.
(3) A coboundary is symmetric by (1); an antisymmetric one is then equal
to its own negative, hence zero. (4) Theorem 78 T4 gives blind ⟺ the
antisymmetric part vanishes ⟺ `B` symmetric; (2) and (3) identify this
with the coboundary condition over `Q`. ∎

Certified on arrows `(p, q)`, `p, q ≤ 3`: three explicit 1-cochains give
symmetric coboundaries satisfying the cocycle identity; an explicit
symmetric `S` equals `δ(S(a,a)/2)`; a nonzero antisymmetric `A` exists;
and on six sample cocycles "blind on all reorderings of multisets of up to
four generators" coincides exactly with "symmetric". S2's crystal is the
class-zero case: *prakāśa* with a memory that is pure gauge carries no
*vimarśa*; recognition "sa evāyam" between histories needs a nonzero
class, which on this base is exactly the turn part.

### Cited, not claimed; refused

- **S3 (madhya).** "Neither going out nor coming in, in the middle" names
  the same two zero-turn orbit states certified in theorum/78 T3; the
  breath identification is cited only.
- **S4 (Aghora ladder, śiva/śivatara).** The three-rung *a-ghora / ghora /
  ghora-tara* and the comparative *śiva / śiva-tara* have no certified
  object on the primitive carrier. **Refused.** theorum/50's odd-sector
  law (the lawful repair of the Aghora canvas, theorum/56 B4) remains the
  only certified Aghora statement.

## 3. Certificate

```text
python proof_lab/shaiva_sources_varga_crystal.py
python -m unittest proof_lab.test_shaiva_sources_varga_crystal -v
```
Status `PASS_SHAIVA_SOURCES_VARGA_CRYSTAL_CANDIDATE`, SHA-256
`4440bf2f0e4f941ba8c7a1e83d7ed63a558c756efddd360a69fe5ef3ce3b37ca`
(`proof_lab/SHAIVA_SOURCES_VARGA_CRYSTAL_EXPECTED.sha256`). Consumes
theorum/78's token order, pratyāhāra map and bilinear memory lift. Exact
rationals only; no Hilbert structure.

## 4. Claim boundary

```text
STOP GRID: ROWS = PRATYĀHĀRA (ñam, jhaṣ, jaś, cay), COLUMNS = udit, NEVER INTERVALS   PROVED
VOICELESS ASPIRATES ARE NO PRATYĀHĀRA; khay, chav ARE                                PROVED
ROWS 7, 8-9, 10 SHARE (ca, pa, ka, ṭa, ta)                                           PROVED
EXACTLY 2304 SET-PRESERVING WITHIN-SŪTRA ORDERS; LEADERS FORCED                       PROVED
SHARED VARGA PERMUTATION NOT FORCED BY THE CODE                                       PROVED
CRYSTAL THEOREM: BLIND ⟺ SYMMETRIC ⟺ COBOUNDARY OVER Q                                PROVED
PRESIDING MOTHERS OF THE VARGAS (Śiva-sūtra 3.19)                                     CITED, NOT CLAIMED
MADHYA (Vijñāna-bhairava 26) BEYOND theorum/78 T3                                     CITED, NOT CLAIMED
AGHORA LADDER (TA 10.45), śiva/śivatara (TS 4.5.8)                                    REFUSED
RH, YM                                                                                UNTOUCHED
```
