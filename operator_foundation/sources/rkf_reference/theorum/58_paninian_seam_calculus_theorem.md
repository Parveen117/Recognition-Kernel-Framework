# Pāṇinian Seam Calculus (canonical sūtras; recognized/memory channels; priority = commutator support)

Source: six owner canvases uploaded Aug 23 2026 (R–A–S semigroup, First-5,
Next-10, Index/Numbering map, Pāṇinian Engine meta-canvas, Prime Operator
Engine).  Read as **hints** (theorum/56 discipline).  Upgrades theorum/56 B2
(toy alphabet, generic rule shapes, one hard-coded `True`) to real
Aṣṭādhyāyī rules under their **canonical A.P.S numbers**, on a two-channel
carrier.  Nothing Hilbert; the carrier is combinatorial (see boundary).

> **Audit note (ladder audit 50–59, Aug 23 2026).** T2(i) 'ambiguity set EQUALS union of commutator supports' is an instance property, not a law (toy: r1:a→b, r2:a→c, r3:b→d, r4:c→d has [r1,r2]≠0 yet unique NF). Lawful statement: ambiguity ⊆ ∪supp — priority is needed ONLY where a residue is nonzero, not EXACTLY where. Determinacy checks were vacuous (isinstance); now tie-refusing + terminating + membership; re-pinned.
> **Gap found Aug 23 (owner's challenge).** The resolver uses only 1.4.2 *vipratiṣedhe paraṃ kāryam* (same-locus conflicts). Pāṇini's tripādī ordering **8.2.1 pūrvatrāsiddham** (rules 8.2–8.4 are asiddha to earlier rules) was missing. Certified in theorum/62: on both word carriers 8.4.40 never fires before 6.1.73, so no certified output changes — but the claim boundary is corrected: 1.4.2 resolves conflicts, 8.2.1 orders the tripādī. Apavāda/utsarga, nitya/anitya, antaraṅga/bahiraṅga are still NOT modelled.

## Carrier
A word is a sequence of morphemes `(recognized phones, memory features)`.
- recognized channel = the phoneme string (what is heard);
- memory channel = it-marker features retained after lopa (1.3.9) — the
  executable content of **1.1.62 pratyayalope pratyayalakṣaṇam** ("when an
  affix is elided, its characteristic effects remain").
This is the framework's P/Q (recognized/memory) split in Pāṇini's own
vocabulary: *anubandha* = memory, *lopa* = cut, *lakṣaṇa* = Smriti tail.

## T1 Vowel-strength semilattice (1.1.1, 1.1.2, 1.1.3)
With the saṃjñā tables as maps `G` (guṇa), `V` (vṛddhi) on the vowel set:
`G² = G`, `V² = V`, `GV = VG = V`, and both are the identity off *ik* (1.1.3
*iko guṇavṛddhī*).  `{id, G, V}` is a 3-element commutative idempotent
monoid, `id ≤ G ≤ V`.  Canvas readings "nonlinear gain", "harmonic
averaging", "basis transformation", "derivative" (First-5 canvas) — **refused**:
the only algebra present is this semilattice; 1.1.1/1.1.2 are *names*, consumed
later by 6.1.87/6.1.88/7.3.84.

## T2 Priority is the commutator-support resolver (binding to theorum/57)
Carrier: all 100 junctions `X+Y` over ten vowels; rules 6.1.77 *iko yaṇ aci*,
6.1.78 *eco'yavāyāvaḥ*, 6.1.87 *ād guṇaḥ*, 6.1.88 *vṛddhir eci*, 6.1.101
*akaḥ savarṇe dīrghaḥ*.  Computed:
```text
free-application ambiguity set  =  ∪ supp[ρ_i, ρ_j]   (exactly: {i+i, i+I, u+u, u+U})
the only non-vanishing commutator is [6.1.77, 6.1.101]
disjoint-trigger pairs commute on every junction
1.4.2 vipratiṣedhe paraṃ kāryam ⇒ exactly ONE normal form per junction   (COMPUTED)
i+i → ī (6.1.101 over 6.1.77); a+i → e; a+e → ai; i+a → ya; e+a → aya
```
Reading: Pāṇini's priority is invoked **exactly** where the first-visible
residue of two rule flows is nonzero (theorum/57: residue ⊙ h² = bracket);
where the bracket vanishes no priority is needed.  theorum/56-B2's
`precedence_restores_unique_normal_form: True` was hard-coded — here it is
an exhaustive verdict.

## T3 The memory channel is load-bearing (1.1.62)
```text
gam + śap + tip → gacchati   1.3.8/1.3.3/1.3.9 it-lopa; 7.3.77 chaḥ (Śit-conditioned);
                             6.1.73 tuk (āgama); 8.4.40 ścutva
nī  + śap + tip → nayati     it-lopa; 3.4.113 sārvadhātuka (saṃjñā); 7.3.84 guṇa; 6.1.78 ayādi
```
Controls (all computed): memory erased at lopa → `gamati`, `nīati` (Śit-
conditioned rules go silent); every pipeline rule load-bearing by ablation
(`gachati`, `gatchati`, `gamati`, `neati`, `nīati`); **lopa order is free iff
memory is carried** — without memory, lopa-last still yields `gacchati`
(the rule reads the undeleted Ś-phone) while lopa-first yields `gamati`:
order becomes content (EMK-T2 shape), and 1.1.62 is exactly what removes
that order-dependence.  Conservation: it-phones deleted = memory features
added (theorum/44 "no discarded tail").
*Build note:* the first draft listed 3.4.113 as load-bearing for *gacchati*;
the certificate refused it — 7.3.77 reads Śit directly, sārvadhātuka is
consumed only by 7.3.84.

## T4 The R–A–S canvas "theorems"
```text
DETERMINACY   DISPROVED under free application (i+i: yi vs ī)
              PROVED under 1.4.2 on the enumerated carrier
SOUNDNESS / COMPLETENESS   NOT CLAIMABLE — no oracle for "valid Sanskrit" in the repo
```

## Numbering audit of the canvases (owner action)
Only 1.1.1 and 1.1.2 of the "First-5" are correctly numbered.  The rest
carry wrong addresses (canonical in brackets; verify against a printed
Aṣṭādhyāyī before any further citation):
eco'yavāyāvaḥ [6.1.78], "aico yaṇ aci" = *iko yaṇ aci* [6.1.77], hal antyam
[1.3.3], tasya lopaḥ [1.3.9], upadeśe'janunāsika it [1.3.2], pratyayaḥ
[3.1.1], "tiṅśit sārvanāmasthāne" = *tiṅśit sārvadhātukam* [3.4.113],
sārvadhātukam apit [1.2.4], kṛt-taddhita-samāsāś ca [1.2.46], sarvādīni
sarvanāmāni [1.1.27], anudāttaṅita ātmanepadam [1.3.12], suptiṅantaṃ padam
[1.4.14], svaujas… [4.1.2], tiṅ endings [3.4.78], prātipadikam [1.2.45],
pratyayalakṣaṇam [1.1.62], vibhāṣā [1.1.44], vipratiṣedhe paraṃ kāryam
[1.4.2].  The actual 1.1.3–1.1.35 are different sūtras (1.1.3 *iko
guṇavṛddhī*, 1.1.4 *na dhātulopa ārdhadhātuke*, 1.1.5 *kṅiti ca*, …).  The
Index canvas's seed table must not be used as an address book.

## Refusal: Prime Operator Engine canvas — SUPERSEDED by theorum/59
> Owner correction (same day): the refusal below is a Hilbert-layer verdict (eigenvalues, ladder adjoints). On the primitive carrier the operator is lawful — see theorum/59, where A1/A2/A4 are certified natively and A3/A5/L1–L4 stay open. The text below is kept as the record of the derived-layer view.

Not a definition.  "Ψ̂ψ_p = pψ_p" with "awareness" undefined; the stated
ladder relations `[a_p, a_q†] = 0` and `a_p a_q† = a_{pq}†` are mutually
inconsistent; L1–L4 are restatements of targets, not derivations.  The
framework already has native primes and the Euler product **proved**
(F00H/F00I); nothing in this canvas adds a theorem.  Filed as REFUSAL.

## Certificate
```text
python proof_lab/paninian_seam_calculus.py
python -m unittest proof_lab.test_paninian_seam_calculus -v
```
`PASS_PANINIAN_SEAM_CALCULUS_CANDIDATE`, SHA-256
`7966cc7271302338487eb41b88a6f3e2da61e35c7d9ed72afc350cfb3c0387ad`.

## Claim boundary
```text
VOWEL-STRENGTH SEMILATTICE {id,G,V}, GV=VG=V                          PROVED
FREE AMBIGUITY SET = ∪ COMMUTATOR SUPPORTS; 1.4.2 ⇒ UNIQUE NF (computed) PROVED (10-vowel carrier)
gacchati / nayati CANONICAL DERIVATIONS; MEMORY CHANNEL LOAD-BEARING    PROVED
LOPA ORDER-FREE ⟺ MEMORY CARRIED (1.1.62 executable)                   PROVED
R–A–S DETERMINACY                                DISPROVED free / PROVED under 1.4.2
R–A–S SOUNDNESS, COMPLETENESS                                         NOT CLAIMED
COVERAGE BEYOND 18 SŪTRAS / 2 DERIVATIONS; 3,959-RULE ENGINE           DECLARED PROTOCOL (56 boundary)
RULES AS MATRICES ON A C_Σ FREE MODULE                                 NOT DONE
CANVAS OPERATOR READINGS OF 1.1.1–1.1.5                               REFUSED
PRIME OPERATOR ENGINE                          Hilbert-layer refusal; native home in theorum/59
RH, YM                                                                UNTOUCHED
```
