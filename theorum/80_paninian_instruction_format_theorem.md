# The Sūtra as an Instruction — Pāṇini's paribhāṣā instruction format compiles to the realized rules

1 November 2026. theorum/58, 60 and 61 realize Aṣṭādhyāyī rules as
hand-written functions on the recognized/memory carrier. If the grammar
is to serve as a programming language, a rule must instead be *read off
the sūtra*: which word is genitive, nominative, ablative, locative, which
markers it carries, which governing sūtra it sits under — and one
interpreter must turn that record into the rule. The interpreter is
Pāṇini's own: the paribhāṣā and saṁjñā sūtras quoted below. This capsule
builds that interpreter for the rules theorum/58 already realized and
certifies that the compiled rules coincide with the hand-coded ones
wherever the latter fire, and that where they differ the sūtras are
right and theorum/58's declared carrier was narrower.

## 1. Sources (quoted)

The instruction format:

```text
1.1.49  ṣaṣṭhī sthāneyogā              the genitive marks what is replaced (sthānin)
1.1.66  tasminn iti nirdiṣṭe pūrvasya  a locative term is the posterior; the operation hits what precedes it
1.1.67  tasmād ity uttarasya           an ablative term is the prior; the operation hits what follows it
6.1.84  ekaḥ pūrvaparayoḥ              (adhikāra over 6.1.85–111) one substitute for prior and posterior together
6.1.72  saṁhitāyām                     (adhikāra) sandhi acts only in close contact
1.1.69  aṇudit savarṇasya cāpratyayaḥ  an aṇ or u-marked term (not an affix) denotes its savarṇas as well
1.1.70  taparas tatkālasya             unless t-marked: then only that duration
1.1.52  alo 'ntyasya                   a substitute replaces the final sound of the sthānin
1.1.55  anekāl śit sarvasya            a multi-sound or ś-marked substitute replaces the whole
1.1.46  ādyantau ṭakitau               a ṭ-marked augment is prefixed, a k-marked one suffixed
1.3.10  yathāsaṅkhyam anudeśaḥ samānām lists of equal length correspond term by term
1.1.50  sthāne 'ntaratamaḥ             otherwise the closest substitute is chosen
1.1.51  ur aṇ raparaḥ                  an aṇ replacing ṛ (ḷ) is followed by r (l)
1.4.2   vipratiṣedhe paraṁ kāryam      when two rules conflict at one locus, the later acts
1.1.1   vṛddhir ādaic;  1.1.2  adeṅ guṇaḥ     the saṁjñās vṛddhi = {ā, ai, au}, guṇa = {a, e, o}
```

The rules compiled: **6.1.77 iko yaṇ aci**, **6.1.78 eco 'yavāyāvaḥ**,
**6.1.87 ād guṇaḥ**, **6.1.88 vṛddhir eci**, **6.1.101 akaḥ savarṇe
dīrghaḥ** (sandhi); **7.3.77 iṣugamiyamāṁ chaḥ**, **6.1.73 che ca** with
**6.1.71 hrasvasya piti kṛti tuk**, **8.4.40 stoḥ ścunā ścuḥ**, **7.3.84
sārvadhātukārdhadhātukayoḥ**, 6.1.78 word-internally.

## 2. The record and the interpreter

A sandhi sūtra is the record

```text
{ sid, sthānin = (name, sounds)  [genitive, 1.1.49],
  ādeśa = list | saṁjñā | dīrgha [nominative],
  left  = sounds | none          [ablative, 1.1.67],
  right = sounds | none          [locative, 1.1.66],
  ekādeśa ∈ {yes, no}            [6.1.84 adhikāra] }
```

whose sound sets are the pratyāhāras of theorum/78 (`ik = p(i, 1)`,
`ec = p(e, 3)`, `ac = p(a, 3)`, `ak = p(a, 1)`, `yaṇ = p(y, 5)`) expanded
by 1.1.69 unless t-marked (1.1.70). The interpreter applies a record to a
junction `(X, Y)`: under 6.1.84 the pair is replaced by one sound (the
ablative term is the prior, the sthānin the posterior, or — for 6.1.101 —
the posterior is a savarṇa of the prior); otherwise the locative term is
the posterior and the sthānin, the prior, is replaced whole (1.1.52 /
1.1.55). The substitute is chosen by 1.3.10 when the sthānin list and the
substitute list have equal length (a savarṇa follows its base), by 1.1.50
when the substitute is a saṁjñā (guṇa, vṛddhi), with 1.1.51 appended, and
is the long savarṇa for dīrgha.

**1.1.50 made exact.** With the traditional sthāna table — a: kaṇṭha;
i, y: tālu; u: oṣṭha; v: danta-oṣṭha; ṛ, r: mūrdhan; ḷ, l: danta; e, ai:
kaṇṭha-tālu; o, au: kaṇṭha-oṣṭha — *antaratama* is the candidate with the
largest Jaccard similarity of place sets, ties broken by the
simple/compound (sandhyakṣara) kind; a lawful selection has exactly one
winner.

## 3. Results

### T1 The sandhi sūtras compile; theorum/58 is the compiled language on short triggers

On theorum/58's 100 junctions (ten vowels squared) the compiled rule of
each of the five sūtras **equals the hand-coded rule wherever the latter
fires**, and fires in addition on **exactly 24 junctions**: 6.1.77 on
`ī/ū + any vowel` (20) and 6.1.87 on `a/ā + ī/ū` (4) — the savarṇa
triggers that 1.1.69 grants (`nadī + ā → nadyā`, `mahā + īśa → maheśa`)
and that theorum/58's declaration left out. 6.1.78, 6.1.88 and 6.1.101
coincide everywhere. theorum/58's verdicts stand on its declared carrier;
the compiled rules are the sūtras' own extension of it.

### T2 Antaratama reproduces every table, and coincides with yathāsaṅkhya

1.1.50 with the sthāna table selects, uniquely in every case used,
`ik → yaṇ` as `i→y, u→v, ṛ→r, ḷ→l`; guṇa as `i→e, u→o, ṛ→ar, ḷ→al` (with
1.1.51); vṛddhi as `i→ai, u→au, ṛ→ār, ḷ→āl, e→ai, o→au, ai→ai, au→au` —
exactly theorum/58's `GUNA`, `VRDDHI` and 6.1.88 tables. On 6.1.77 the
place selection **coincides with the positional correspondence** of
1.3.10 on the Māheśvara order (`i u ṛ ḷ ↔ y v r l`).

**Corollary (the ṛ ḷ pin).** theorum/79 T2 found Māheśvara sūtra 2 (*ṛ
ḷ*) free under the interval code (both orders preserve every used
pratyāhāra). Requiring 1.3.10 and 1.1.50 to agree on 6.1.77 admits only
*ṛ* before *ḷ*: of the 2304 code-preserving orders, 1152 are coherent
with the two selection laws.

### T3 The compiled sandhi is confluent under 1.4.2

Free application of the compiled rules is ambiguous on exactly
`{i, ī}² ∪ {u, ū}²` (eight junctions: theorum/58's four and their
savarṇa images); the only conflicting pair is 6.1.77 vs 6.1.101; under
1.4.2 every junction has a unique normal form and each conflict goes to
the later sūtra 6.1.101 (`i + ī → ī`). theorum/58 T2's "priority is
commutator support" survives the extension unchanged.

### T4 The word rules compile and agree on every reachable state

- **7.3.77** — genitive plural sthānin `{iṣ, gam, yam}`, nominative
  substitute `ch`, locative `śiti` by anuvṛtti (read from the memory
  channel after 1.3.9, theorum/58 T3); 1.1.52: the final sound is
  replaced.
- **6.1.73 with 6.1.71** — `tuk` is an augment whose `k` is an it
  (1.3.3), so by 1.1.46 it is suffixed to the short vowel before `ch`.
- **8.4.40** — `stu` (s + the ta-varga, u-marked, 1.1.69) in contact
  with `ścu`: `s → ś` by 1.3.10 across the two lists, and a stop goes to
  the ca-varga stop of its own **manner row** by 1.1.50 — read off
  theorum/79's grid: `t→c, th→ch, d→j, dh→jh, n→ñ`.
- **7.3.84** — an aṅga (6.4.1) ending in ik gets guṇa before a
  sārvadhātuka/ārdhadhātuka affix, substitute by 1.1.50 + 1.1.51.
- **6.1.78** word-internally as in T1.

Each compiled rule equals theorum/58's hand-coded function on **all 40
reachable states** of the gam and nī derivations (theorum/60's graph,
with and without memory), and the compiled pipeline reaches *gacchati*
and *nayati*.

## 4. Certificate

```text
python proof_lab/paninian_instruction_format.py
python -m unittest proof_lab.test_paninian_instruction_format -v
```
Status `PASS_PANINIAN_INSTRUCTION_FORMAT_CANDIDATE`, SHA-256
`8ac53de2a233fbe94d7d6f3f9e3806ade7bd2f68c759faba81882119ae87bccb`
(`proof_lab/PANINIAN_INSTRUCTION_FORMAT_EXPECTED.sha256`). Consumes
theorum/58's carrier, tables and functions, theorum/60's reachable graph,
theorum/78's pratyāhāras and theorum/79's manner grid. Exact; no
floating point, no Hilbert structure.

## 5. Claim boundary

```text
CASE-STRUCTURED RECORDS + QUOTED PARIBHĀṢĀS COMPILE THE FIVE SANDHI SŪTRAS           PROVED
COMPILED = theorum/58 WHEREVER 58 FIRES; +24 LONG-ī/ū JUNCTIONS BY 1.1.69            PROVED (58's carrier narrower, not wrong)
ANTARATAMA (sthāna table) REPRODUCES yaṇ / guṇa / vṛddhi TABLES UNIQUELY              PROVED
1.3.10 = 1.1.50 ON 6.1.77; ṛ BEFORE ḷ PINNED; 2304 → 1152 COHERENT ORDERS              PROVED
COMPILED SANDHI CONFLUENT UNDER 1.4.2; CONFLICTS = 6.1.77 vs 6.1.101 ON 8 JUNCTIONS   PROVED
WORD RULES 7.3.77, 6.1.73, 8.4.40, 7.3.84, 6.1.78 COMPILE; = 58 ON 40 REACHABLE STATES PROVED
ścutva TABLE FROM THE MANNER GRID (1.3.10 ACROSS LISTS, 1.1.50 WITHIN)                 PROVED
GENERAL AṢṬĀDHYĀYĪ INTERPRETER; ADHIKĀRA PARSING                                        NOT CLAIMED (spans declared)
ṝ ḹ, PLUTA                                                                             OUTSIDE THE DECLARED CARRIER
RH, YM                                                                                 UNTOUCHED
```
