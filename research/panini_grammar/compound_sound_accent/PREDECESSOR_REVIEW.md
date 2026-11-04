# PG38 — PG37 continuation integrity and targeted reread

Author: Monty. 4 November 2026.

The baseline is PG37 commit
[`864ddd6d152d5d31279e1a679f1ab0ca5491989f`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/864ddd6d152d5d31279e1a679f1ab0ca5491989f).
Its packet remains frozen. This review supports continuation at the same
written-contract layer; it is not an independent verification of all PG37
grammar or a replay of its earlier suites.

|Check|Observed result|What it establishes|
|---|---|---|
|321 register rows against authored locations|All six fields match|No transcription drift in the predecessor register|
|988 literal source fields against pinned primary keys|All match|Archive fidelity, including damaged readings|
|29 primary/predecessor/companion/authored file identities|Sizes and SHA-256 match|Pinned source/document integrity at PG37 commit|
|Eight relevant semantic boundaries|No new mismatch found in the checked clauses|Targeted source-relative interpretation review only|

The targeted reread compared each full Kāśikā field and its existing row:

|ID|Boundary checked for this continuation|
|---|---|
|5.3.98|Human resemblance name with actual selected कन् and लुप्; supports the 6.1.204 accent distinction|
|5.4.68|Added समासान्त remains part of the compound and retains its class|
|5.4.69|Praise सु/अति prohibition ends before बहुव्रीहि family, not every praise modifier|
|5.4.71|Negative restriction belongs to actual तत्पुरुष, not every नञ् compound|
|5.4.72|पथिन् makes that prohibition optional; not blanket optionality|
|5.4.74|धुर् axle qualifier does not distribute to every listed base; ऋच् usage qualified|
|5.4.76|दर्शन denotes the living eye, not every aperture one sees through|
|5.4.85|अध्वन् needs actual prefix identity; परम/उत्तम do not qualify|

These results justify retaining the previous rows without rewriting their
frozen source packet. They do not prove every semantic annotation, gaṇa
member, accent or later intersection correct. PG38's new overlap rows add
explicit bounded specifications without counting an existing ID again.
No grammar execution, generator comparison or certificate replay was run.
