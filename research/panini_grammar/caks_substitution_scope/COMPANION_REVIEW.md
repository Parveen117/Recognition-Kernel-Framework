# PG57 — T162 scope adjudication and implementation handoff

Author: Monty. 4 November 2026.

The development base is 24b429719cc54baca68de2df03772b66ce4bad4d.
The companion branch was checked once for this stage and remains
**cc7b39bb70aec81579fefa27c8aac5db89480da5**, T162. No new companion
commit is claimed. [PG56's review](../shyan_marker_accent/COMPANION_REVIEW.md)
supplies the already reviewed suite results and evidence limits; those
executions were not repeated.

## The source decision

T162's §3 grouped 144 reported verbal cells and nine kṛt keys into one
153-cell unresolved scope question. Its stated premise that all the kṛt
affixes in that lane are आर्धधातुक needs correction: शानच् is शित्.

|Reported group|T162 size|PG57 written result|Execution status|
|---|---:|---|---|
|Simple passive with यक्|36|The qualified inner यक् is आर्धधातुक; H01 derives ख्यायते|No 36-cell replay|
|Causative णिच्|72|The qualified inner णिच् triggers replacement; H02 derives ख्यापयति/ख्यापयते|No 72-cell replay|
|Desiderative सन्|36|3.1.7's सन् is आर्धधातुक; H03 derives चिख्यासति/चिख्यासते with pada premises|No 36-cell replay|
|क्त, क्तवतु, तव्य, तुमुन्, क्त्वा, तृच्, अनीयर्, ण्वुल्|8|H04 gives the eight ख्या-based written targets|No executable kṛt repair|
|Simple-root present शानच्|1|H07 retains चक्ष् and derives चक्षाण; its सार्वधातुक designation blocks this trigger|Not an omitted 2.4.54 application|

Thus **144 + 8 + 1 = 153** is the reported-scope partition; **144 + 8 = 152**
identifies targets affected by the qualified source decision, not a claim
that 152 outputs were executed, independently checked or fully enumerated.
The disagreement cannot be closed by calling all 153 oracle outputs wrong.
The gate and representative derivations are resolved under the stated
source/sense policy; implementation, all agreement slots and alternative
source branches still require work.

## Concrete code boundary

At the pinned companion commit, `proof_lab/ting_rule_table_engine.py` has
the 2.4.54 guard on `root == "cakṣ"`, with the disjunction of an
ārdhadhātuka lakāra, `karmani`, `hetu`, or `san`, followed by a global
`lak != "liṭ"`. It changes the current letters and adds a `khyā` flag.
The bounded re-read here covers that guard and its nearby causative rows;
it is not a new audit of the entire engine.

The three formation shortcuts reach the appropriate source decision on
the ordinary frames just written. A complete adapter must still retain
the actual prescription and host, exclude the stated lexical/register
exceptions, recognize the new ञ् and query pada with the relevant
conditions. An outer perfect must not suppress a substitution already
licensed while building an inner णिच्/सन् host. This is an identified
guard-design obligation; no nested perfect output was run here.

The pinned kṛt table still lacks 2.4.54, as already recorded by T162 and
PG56. Integrate it before old-root-dependent suffix selection or cluster
rules, while preserving the शानच् control. The explicit आख्येयम्
example in H05 shows why adding a final spelling replacement after choosing
ण्यत् would be insufficient.

## Handoff order

1. Add the source-qualified, affix-addressed substitution decision with its
   exception/open channels. Use the original root for provenance and the
   substitute for its own marker, sound and selected अनिट् profile.
2. Add H04's eight kṛt targets and retain H07's शानच् control. Keep the
   कृत् युक् and causative पुक् owned by their different prescriptions.
3. Carry voice and actor-benefit data into pada admission. Treat the direct
   simple-root perfect option separately from inner formations followed by
   a later लिट्.
4. Develop the alternative ख्शा/क्शा visibility history before claiming
   complete source-branch coverage. Then implement and perform the deferred
   Python 3.12 grammar checks and replay on the changed scope.

No code, expected output, certificate pin or reported lane total is modified
by PG57. The prior expected-set membership and PG19 metadata-merge evidence
limits remain as recorded; they were not re-audited. No message was sent to
the companion. This file is the reviewable handoff.
