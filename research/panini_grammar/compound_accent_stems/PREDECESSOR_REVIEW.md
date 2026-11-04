# PG39 — PG38 integrity and targeted semantic review

Author: Monty. 4 November 2026.

The construction baseline is PG38 commit
[`82ac8dc97be7bd59660546cd0c085775395529da`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/82ac8dc97be7bd59660546cd0c085775395529da).
Its packet remains frozen. The checks below support continuation of the
written specification; they are not a replay or an exhaustive linguistic
validation of PG38.

|Check actually performed|Result|Evidence boundary|
|---|---|---|
|352 register rows against original authored lines|All six fields match|Transcription integrity|
|1,095 literal fields against pinned primary edition|All match|Archive fidelity, including damaged text|
|28 source/predecessor/companion/authored file identities|Byte sizes and SHA-256 match|Pinned file integrity at baseline commit|
|Eight full Kāśikā fields compared with existing rows|No new mismatch in these boundaries|Targeted semantic review only|

|ID|Boundary read for this continuation|
|---|---|
|5.4.151|Qualified कप् membership; singular inflected gaṇa entries do not automatically cover dual/plural|
|6.1.85|Both-origin constituent membership does not transfer every sound-dependent operation|
|6.1.86|Earlier view is query-specific, with explicit सम्प्रसारण/ङि/इट् exceptions|
|6.2.28|Three apparent accent placements belong to dependent branches/source policies|
|6.2.33|अव्ययीभाव accent depends on actual exclusion/time relation; later वन exception retained|
|6.2.48|INSTR first-member preservation requires कर्म-denoting क्त|
|6.2.49|Immediate गति, कर्म क्त and outer कारक priority remain separate gates|
|6.2.54|ईषत् option does not override the independently admitted कृत् accent|

No changes to these frozen rows were needed. PG39 separately writes its
new overlap contracts and excludes their IDs from the appropriate new-credit
sets. These checks do not establish every lexical extension or priority
intersection; no grammar suite, independent generator or certificate replay
was run.
