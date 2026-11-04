# PG34 — Completed written block and implementation handoff

Author: Monty. 4 November 2026, Asia/Calcutta.

This stage continues PG33 at `2c391cb1492e96bee8f7281a3b8dcfc9fc6fa78a`.
The latest checked the theorem branch head is unchanged T152,
`751dddec31988299cdd5003ebffcbf701b1b0126`. Reuse PG32's static
review and PG33's interface contract; no fresh execution or independent
implementation audit of that unchanged head is claimed.

## H1. Runtime contract supplied by the written construction

| Input/operation | Required behaviour |
|---|---|
|Admission|ordinary admitted luṅ; exact expression/role frame; original A3sg ta|
|Other karma slots|outside this ciṇ constructor; route to other luṅ work rather than reject Sanskrit|
|Affix|actual cli→ciṇ, not a ciṇvat flag on sic|
|i ownership|distinguish ciṇ-i, ṇic-i, augments and original A1sg ending|
|Causal lopa|6.4.51 removes ṇic on an iṭ-free actual-ciṇ input; no retained-ay option|
|Ending-luk|6.4.104 removes ta while retaining its source and controller|
|Śam/gam|read original accent and basic/causal formation; causal mit choice needs ṇic|
|Labh|couple num to the changed upadhā guard; exactly alābhi/alambhi here|
|Result|word, original ending, lexical/role evidence, affix owners, branch and lopa events|

Implementation should distinguish Accepted, Open, and OutsideThisConstructor.
Never implement the original-ta guard by re-reading the final i. Do not
delete the nearest “i affix” without its owner. No runtime code is added
by this handoff, and no external message or agent was dispatched.

## H2. Actual work and checks

Read the relevant PG18/32/33 construction interfaces and targeted primary
passages. Resolve actual ciṇ versus ciṇvat, ta-luk, original-accent
guard, optional labh num, and causal ṇic/mit branches. The complete word
register adds **30 positions /33 readings**; cumulative positions are
**11,552**. The combined rule union adds **3.1.66, 6.4.104, 7.1.69**,
reaching **734/3,983**. Other operative rules are reused or deepen an
already companion-labelled entry. COVERAGE records the exact written delta.

The independent-written inventory reaches **381**: seven newly explicit
rule constructions plus restored 7.3.32, whose ciṇ-model exception was
already written in PG18 R4 but missing from that inventory. The restored
entry is not credited as a new rule construction; predecessor files stay
frozen. The seven new written entries are 1.1.60, 1.1.61, 3.1.66,
6.4.104, 7.1.64, 7.1.69 and 7.3.34.

The publication helper only copies pinned source fields, transcribes the
already authored word table, computes file identities and counts, and
compares rule-ID inventories. It does not run a morphology engine or
generate Sanskrit. Publication checks cover JSON, links, literal source
identity, table accounting and Git diff integrity.

**Grammar tests, independent generators, certificate replay, navigation
tests and operator suites remain deferred.** Runtime code, shared engine,
frozen evidence and predecessor packets are unchanged. No main merge,
hosted-CI result, proof-assistant validation or external review is claimed.

## H3. Next frontier

The remaining eight karma luṅ slots need their own sic/ciṇvat or other
eligible affix constructions. Ksa, aṅ and causal caṅ, their lexical
exceptions, general contextual precedence and wider nominal/compound
coverage remain open. The A3sg ciṇ branch does not fill those obligations.
