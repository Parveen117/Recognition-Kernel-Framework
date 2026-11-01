# PG1 worked derivations and blocked alternatives

Author: Monty. 1 November 2026.

These are reviewed, bounded grammatical explanations, not executions of a
new engine. The source is the Aṣṭādhyāyī with the Kāśikā readings registered
in [SOURCES.md](SOURCES.md). Lexical and semantic premises are stated rather
than inferred from spelling. Accent is outside the output domain of these
examples; its source features must still be retained when they condition a
grammatical choice.

## 1. It-lopa: śap → a, tip → ti, but am retains m

| Teaching-form input | Designation | Lopa under 1.3.9 | Retained information |
|---|---|---|---|
| Non-taddhita affix śap, शप् | Initial ś by 1.3.8; final p by 1.3.3 | अ, a | Affix identity, śit/pit provenance and their separately licensed effects |
| Tiṅ ending tip, तिप् | Final p by 1.3.3 | ति, ti | Tiṅ identity, person/number and marker history |
| Sup ending am, अम् | Final m is protected from 1.3.3 by 1.3.4 in the vibhakti domain | अम्, am | Inflectional identity and the actually pronounced m |

**Blocked alternative:** removing the last consonant of every suffix would
turn *am* into *a*. That violates the explicit category-sensitive exception.
The grammatical diagnosis is independent of whether a particular final word
could coincidentally be repaired by another erroneous rule.

**Attribution:** these are it-designation/lopa cases, not entire-affix lopa
under 1.1.62. In particular, śap still has its pronounced a. Marker history
is valuable to a software model without changing which sūtra licenses the
linguistic operation.

## 2. भू → भवति, bhū → bhavati

Premises: Dhātupāṭha entry **01.0001**, publisher record **1010001**, *bhū*,
*sattāyām*, bhvādi; present-time kartari use, parasmaipada, Sanskrit
prathama-person singular. The chosen lexical/pada conditions and residual
selection under 1.3.78 are supplied. English calls this third-person singular.
This is a classical, unaccented output task, not a derivation of every bhū form.

| Step | State / fact | License and retained condition |
|---|---|---|
| 1 | bhū + laṭ | 1.3.1 root identity; 3.2.123 present-time laṭ |
| 2 | bhū + tip | 3.4.77–78 lakāra substitution; 1.4.101–102 and 1.4.108 select the stated person/number |
| 3 | tip is sārvadhātuka | It is a tiṅ ending, 3.4.113; agent expression belongs to the semantic input and 3.4.69 context |
| 4 | bhū + śap + tip | 3.1.68, with inherited sārvadhātuke from 3.1.67 and the root/affix headings |
| 5 | bhū + a + ti | 1.3.8 / 1.3.3 designate ś and p; 1.3.9 elides them. The śap identity remains available |
| 6 | śap is sārvadhātuka | 3.4.113 also applies through śit; erasing the surface ś did not turn śap into an unidentified a |
| 7 | bho + a + ti | 7.3.84 with its aṅga context; 1.1.3 and the source-supported guṇa correspondence ū → o |
| 8 | bhav + a + ti → भवति | 6.1.78, o → av before a vowel, with aci inherited from 6.1.77 |

The Kāśikā on 3.1.68 explicitly gives *bhavati* and explains why the ś marker
is present. This trace makes the needed inherited and lexical facts visible.
It does not assert that the displayed linear ordering is the only legitimate
ordering of independent designation events.

**Blocked alternatives:** do not apply 7.3.84 to every final ū without the
affix domain; do not treat *kartari* as a required following phoneme; do not
replace every o with av outside the inherited vowel context.

## 3. भू → भवन्ति, bhū → bhavanti: an earlier exception

Use the same root, time, voice and pada, changing number to plural. Select
*jhi* from 3.4.78 with 1.4.101–102; prescribe śap as above. Under 7.1.3 the
jh element of the ending receives *ant*, giving *anti*. After marker lopa,
root guṇa and ayādi, the relevant structured junction is:

`bhav + a(śap) + anti → bhava + anti`.

The short a of the vikaraṇa is **not pada-final**. Both the general long-vowel
possibility in 6.1.101 and the specialized 6.1.97 reading must be considered.
6.1.97 inherits *apadāntāt* and *pararūpam*; its Kāśikā entry explicitly
identifies the exception to the savarṇa-dīrgha rule. The two a sounds receive
the latter form, a, in the ekādeśa scope of 6.1.84:

`bhava + anti → bhavanti → भवन्ति`.

**Blocked alternative:** sorting only by sūtra number chooses 6.1.101 and
gives **\*bhavānti**. The asterisk marks the rejected form for these premises.

**Boundary control:** the Kāśikā contrasts an external/pada-boundary example
*daṇḍa + agram → daṇḍāgram*. The *apadāntāt* requirement blocks use of 6.1.97
on that junction. Thus the pair of vowel letters alone cannot choose the rule.

**Model control:** T64 detected the earlier exception on its nominal/verbal
sample. T66 then showed that extending the sample makes simple domain
containment inadequate, and records a declared bādhaka relation. PG1 adopts
the source-supported relation, not a theorem that every exception can be
inferred from those finite sets.

## 4. रामः, rāmaḥ, at pause: technical ru is not a spoken u

Premises: masculine a-stem *rāma*, singular nominative, in a context licensed
by 2.3.46, followed by explicit avasāna (1.4.110). The stem and gender are
lexical input, not derived from the following steps.

| Step | Structured state | License |
|---|---|---|
| 1 | rāma + su | 4.1.1–2 nominal affix domain and singular nominative; the teaching form is सुँ with its nasalized marker vowel |
| 2 | rāma + s | 1.3.2 designates the upadeśa vowel as it; 1.3.9 removes it |
| 3 | sup-ending pada | 1.4.14; the partially pronounced ending remains identifiable |
| 4 | rāma + r(u-it) | 8.2.66, pada-final s receives the technical ru substitute |
| 5 | rāmar | The substitute's marker u is designated/elided under 1.3.2/9; it is not pronounced as a new syllable |
| 6 | रामः, rāmaḥ | 8.3.15 in the declared pause context |

The marker interpretation of the teaching forms is explicit input; it cannot
be recovered reliably by deleting characters from the compact spelling of
4.1.2. A future implementation must also apply the appropriate operation-time
interpretation of saṃjñā/paribhāṣā discussed under 8.2.1, rather than blocking
all marker interpretation merely because ru arose in the Tripādī.

**Blocked alternative:** applying visarga at every word boundary is wrong.
For the already supplied pada *savitur* before *vareṇyam*, the following v is
not *khar* and there is no pause. 8.3.15 does not justify **\*savituḥ
vareṇyam**. This boundary control is also explicit in T67; it does not claim
to derive all the individual padas of the Gāyatrī.

## 5. Same surface, different grammatical entitlement

Compare two legitimate affix records:

- Śap from 3.1.68 loses initial ś and final p and has surface **a**. Its
  retained śit designation licenses the corresponding 3.4.113 branch.
- Ac, one of the affixes prescribed in 3.1.134, loses final c by 1.3.3/9 and
  also has surface **a**. It is not śit and is not a tiṅ ending. It does not
  acquire the same 3.4.113 designation merely because it is written a.

Let `surface(m)` forget affix identity and let `Q(m)` ask whether the record
has the śit property relevant to this branch of 3.4.113. Then

`surface(śap-after-lopa) = surface(ac-after-lopa) = a`,

while the two Q values differ. Consequently no function of that surface
alone can reproduce Q on both records: such a function would have to assign
two different values to a. This is an elementary information-loss argument
on the declared records, not a universal philosophical identification of
lopa and forgetting. The surrounding derivations of these affixes need not
be identical for this counterexample to a surface-only **affix record**.

Keeping the affix/marker identity repairs this particular loss. It does not
by itself solve anuvṛtti, lexical interpretation, visibility or the whole
grammar. The full-family specialization contract in the specification
therefore retains those fields too.

## 6. An asiddha view is not the current string

Take the local final-stop situation discussed in T65: a pada ending in d at
pause, with the relevant jaś result already established. The optional pause
operation in 8.4.56 can give the t variant. If 8.2.39 then reads this new t as
an ordinary fresh input, it would restore d and discard the licensed option.
Under 8.2.1 the later effect is asiddha to the earlier rule. The history can
record that the t variant was produced while the earlier rule's view does
not use that t as a newly available trigger.

This is a local visibility control, not a full derivation of every form of
*tad*. T65 encodes that particular pair; it does not implement all of 8.2.1.
The Ābhīya region requires a different review: the Kāśikā on 6.4.22 uses
*edhi* and *śādhi* to explain why an original consonantal condition can remain
relevant despite a replacement, subject to the same-support condition.
Those examples motivate a separate visibility obligation; PG1 does not
pretend to have completed their entire verbal derivations here.

## 7. Result status

The packet now has four explicit derivational examples, the surface-record
counterexample, and a local visibility control. These distinguish a correct
form, a licensed path, and a retained source explanation. The source checks
are textual; only the imported T78–T80 computations were executed in this
integration. No grammar-wide soundness, completeness, confluence or unique
analysis theorem follows from these examples.
