# PG61 — T165 static review and implementation handoff

Author: Monty. 5 November 2026.

Companion branch: `shaiva-sources-maheshvara-spanda-pratyabhijna`.
Reviewed head: `bf1228fd5262baf9f3257de19547aab51eb260cc`, parent
`d5194a743663c6f1afd63ed848a6d6e33d48cf91` (PG60's reviewed T164 head).
One new commit was observed. The complete T165 capsule and selected
changed engine declarations/guards were read; lanes, generators and
certificates were not executed here. [Pins](SOURCE_PINS.json) bind the
exact files. No message was sent to the companion author.

## Reported implementation progress, attributed to T165

T165 declares 65 divādi and 103 tudādi roots plus six earlier residues,
for 174 additions and 233 lane-only declarations in total. It reports
the existing suite at 1,072/1,072 and 266 rule rows; its pinned digest is
`843d6a5ab98a0d2bda793ee1d1bf6274542e826b6dcea3dd2299c575d09268b9`.
These are the companion's reported finite checks against its declared
Vidyut oracle, not PG61 tests or independent primary-source proofs.

The capsule reports open 12,750/12,752; ārdhadhātuka 26,011/26,065;
karmaṇi 16,272/16,344; ṇic 32,472/32,616; san 19,836/20,052;
kṛt 4,074/4,119; and kṛdanta 116,690/120,268. Its recorded replays
737/679 and 742/739 are retained as stated, with the capsule's
undeclared-root/placement qualifications, not relabelled as all-pass
fractions. Its inventory of 159 remaining divādi/tudādi entries is
planning evidence, not additional written coverage in this packet.

## New guards compared with the written construction

| Selected code at T165 | Source assessment | Integration boundary |
|---|---|---|
| `7.3.56`: `up_root == "hi"`, an existing `ab`, root-initial h and no `"caṅ"` flag; `7.3.56s` repeats the san-time application. | The root target and explicit caṅ exclusion agree with H02/H03. | Preserve which stage supplied ab and do not infer yaṅ/ṇic-san completeness from the two observed paths. |
| `7.4.70n`: liṭ, `ab == ["a"]`, root beginning ṛ followed by a consonant, no augment or ām flag; writes `["ā", "n"]` into ab. | Repairs the root-initial-a guard that would miss H05; K 7.4.71 explicitly licenses the weak ṛdh forms. | Keep a separate provenance event for nuṭ owned by the following aṅga. The implementation's storage of n in ab is not its grammatical ownership. |
| `PU_LIST` now includes dhṝ and blī. | These are named membership additions, consistent with the selected short-root paths. | Membership does not establish every other source or register condition. |
| `7.3.80` now requires śit with the n-initial vikaraṇa, gaṇa 9, non-karmaṇi, membership and final ū/ṝ/ī; its stripped-upadeśa arm excludes śṝñ. | The branch is effectively restricted to śnā and selected vowels. The numbered source rule says śit. | This is finite implemented scope, not a complete restatement of 7.3.80. PG60's ec/heṭh and named broad-profile obligations remain. |

The code's `root` is the declaration key, while `up_root` is the
teaching. Thus the selected `śṝ9b` declaration does not regain the
`PU_LIST` branch through the bare key. The declaration tuple carries
`("śṝñ", "U", 9, "09.0015")`; hi and ṛdh carry their 05.0012/05.0027
identities. Retain those identities through marker loss and source
selection rather than merging roots with equal pronounced bases.

## The śṝñ source conflict remains explicit

T165 justifies a long śīrṇāti/śīrṇīte profile by the position of the
ñ-marked entry in its root list. PG60's independently inspected
Kṣīrataraṅgiṇī page 280, entry 17 gives **शॄञ् हिंसायाम् । शृणाति,
शृणीते ।** Its archived image SHA-256 is
`ec3cdc996bb731992334b6bb48bfe7aa9051eafcbf25fb4981693a8716900dff`.
The modern 1090015 variant note explicitly points to that work.

Therefore T165's “closed” status does not close the named
`KSHIRA_SHRNJ_1090015` profile. Preserve PG60's short P/A paradigms.
A long profile requires its own positive source; it must not silently
replace the pinned witness. This is a source/identity discrepancy,
not merely an optional spelling assigned by a root-wide mismatch list.
The old image is reused by pin; it was not downloaded or recollated.

T165 separately leaves svṝ/śṝñ loṭ 2sg open: its svūrāṇa/śīrāṇa
against Vidyut's svūrṇīhi/śīrṇīhi. Whether 3.1.83 can see the r of
the ir/ur substitution requires source adjudication and the retained
1.1.56 view. PG61 has not settled that issue. The śṝñ comparison also
needs the source-profile choice above before comparing its cells.

## Concrete handoff

1. Admit the four H07 paradigms by lexical ID, derivation kind, P
   license and context. Compare 36 positions/47 distinct readings,
   retaining the two same-string ṛdh 1sg ṇit histories separately.
2. Keep root h and copied h addresses apart. Implement the explicit
   actual-caṅ exclusion, then separately qualify yaṅ and ṇic-san
   against H04; the latter uses a local jñāpaka, not generic propagation.
3. Split ṛdh san at the 7.2.49 iṭ decision before kit, root-vowel,
   copying and lopa guards. The source pair is ardidhiṣati/īrtsati.
   Do not route its iṭ branch through the perfect's ā/nuṭ construction.
4. Preserve the 7.4.70/71 event order and the rule-relative r-component
   predicate. Record nuṭ as aṅga-initial even if a compact runtime
   stores its string next to the abhyāsa.
5. Carry PG60's short śṝñ source policy, broad/narrow pvādi policies
   and register gates. Resolve ṛkṣi's base/present-word discrepancy
   before admitting its wider paradigms; do not delete ciri/jiri's i.

This is an implementation handoff document, not a statement that the
companion has incorporated it. Earlier PG57–PG60 integration duties
and the separate PG19 metadata concern remain inherited. All grammar
tests, generators, replay and navigation/operator suites remain deferred
to the companion work; only Python 3.12 document/source checks run here.
