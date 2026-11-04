# PG40 — PG39 integrity and selected boundary review

Author: Monty. 4 November 2026.

Baseline: [`97bdbeb8c3a0352660c5571dc9c7b56feab4493a`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/97bdbeb8c3a0352660c5571dc9c7b56feab4493a).
The existing PG39 packet remains frozen. These checks support continuation
of the specification, not exhaustive validation of every interpretation.

|Check|Result and limit|
|---|---|
|329 register rows against original authored lines|Six-field transcription integrity|
|1,047 literal fields against pinned primary edition|Exact archive fidelity, including damaged/displaced fields|
|29 source/predecessor/companion/authored file identities|Byte length and SHA-256 at the baseline commit|
|Eight full Kāśikā fields compared with PG39 rows|No new mismatch found at these selected boundaries|

|ID|Boundary reviewed for PG40|
|---|---|
|6.3.43|Original ङी, multi-vowel base and same-sense masculine usage; suffix versus following-member identity|
|6.3.45|Shortening and masculine-treatment routes remain different histories|
|6.3.61|Qualified shortening excludes इयङ्/उवङ्, indeclinables and named lexical cases|
|6.3.94|तिरि branch depends on absence of the later अञ्च् vowel loss|
|6.3.139|सम्प्रसारण-based length does not reopen already displaced optional shortening|
|6.4.19|तुक्-bearing छ् and व् map separately; source policies on क्ङित् remain labelled|
|6.4.22|Same आश्रय, भ inclusion and named वुक्/युट् visibility exceptions|
|6.4.37|Original accent, nasal-final class and exact क्तिन्/क्तिच् distinction|

No frozen row was edited. Current overlap contracts are written anew and
their IDs excluded from the appropriate new-credit sets. Grammar suites,
independent generators and certificate replay were not run.
