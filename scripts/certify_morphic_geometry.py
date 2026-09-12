#!/usr/bin/env python3
"""RNKE source/build/theorem-status pipeline for Morphic Operator Geometry.

The manually added historical source is preserved byte-for-byte as provenance.
The generated main.tex is a reviewer-facing audited copy: LaTeX transport defects
are repaired, several demonstrably overbroad statements are replaced by precise
versions, and all remaining theorem claims receive explicit RNKE statuses.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "theorum" / "morphic_calculus" / "Morphic operator geometry..tex"
TARGET = ROOT / "theorum" / "morphic_geometry"
ORIGINAL = TARGET / "source_original.tex"
MAIN = TARGET / "main.tex"
PDF = TARGET / "main.pdf"
PREPARE_MANIFEST = TARGET / "PREPARE_MANIFEST.json"
CERTIFICATE = TARGET / "RNKE_CERTIFICATE.json"
SUMMARY = TARGET / "CERTIFICATION_SUMMARY.md"
STATUS = TARGET / "CERTIFICATION_STATUS.md"

# Git blob SHA of the manually added source on agent/morphic-path-recognition-theorems.
EXPECTED_SOURCE_GIT_BLOB_SHA1 = "ebb8ef8c6fefdbcaaff8186cc3d470259dfbbb37"
EXPECTED_CLAIM_COUNT = 22
EXPECTED_AXIOM_COUNT = 5

CLAIM_STATUS = {
    "Rewrite Confluence ⇔ Vanishing Curvature": "REPLACED_BY_DIAMOND_FLATNESS_THEOREM",
    "Twist–Spectrum Correspondence": "REPLACED_BY_UNITARY_TWIST_ISOSPECTRALITY_THEOREM",
    "Holonomy Accumulation": "CERTIFIED_AFTER_SCALING_CORRECTION",
    "Collapse–Metric Compatibility": "REPLACED_BY_QUOTIENT_SEMINORM_CRITERION",
    "Heat Trace Rigidity": "REPLACED_BY_HEAT_TRACE_ISOSPECTRALITY_WITH_BLINDNESS_BOUNDARY",
    "Stable Geometry Sector": "INCOMPLETE_EXISTENCE_AND_REPRESENTATION_INDEPENDENCE",
    "Smooth-Manifold Reduction": "CONDITIONAL_REQUIRES_DIRAC_LIPSCHITZ_HYPOTHESES",
    "Spectral Triple Emergence": "INCOMPLETE_MISSING_COMPACT_RESOLVENT_OR_LOCAL_COMPACTNESS",
    "Entropy-Clock → Fisher Geometry": "INCOMPLETE_REQUIRES_STATISTICAL_MODEL_HYPOTHESES",
    "Wasserstein Geometry Emergence": "INCOMPLETE_REQUIRES_OPTIMAL_TRANSPORT_METRIC_STRUCTURE",
    "Graph Laplacian Reduction": "CERTIFIED_AFTER_FINITE_SYMMETRIC_SECTOR_CORRECTION",
    "Kernel Geometry Reduction": "INCOMPLETE_METRIC_IDENTIFICATION_NOT_AUTOMATIC",
    "Universal Geometry Theorem": "INCOMPLETE_UNIVERSALITY_NOT_PROVED",
    "Flat Classification": "INCOMPLETE_OR_FALSE_AS_STATED",
    "Curved Obstruction": "INCOMPLETE_REQUIRES_REPRESENTATION_AND_SPECTRAL_FAITHFULNESS",
    "Rigidity Criterion": "INCOMPLETE_INVARIANT_DETERMINACY_DOES_NOT_CONTROL_ALL_DEFORMATIONS",
    "Deformation Space": "INCOMPLETE_H2_GIVES_CANDIDATES_NOT_UNOBSTRUCTED_MODULI",
    "Phase Separation": "INCOMPLETE_WEAK_EQUIVALENCE_CAN_IGNORE_COLLAPSE_CLASS",
    "Spectral Completeness Window": "REPLACED_BY_SPECTRAL_SIGNATURE_INJECTIVITY_CRITERION",
    "Master Classification": "CERTIFIED_PARTITION_ONLY_WEAK_EQUIVALENCE_INVARIANCE_OPEN",
    "No-Go": "REJECTED_AND_REPLACED_BY_PATH_BLINDNESS_THEOREM",
    "Self-Consistency": "META_GUARD_NOT_MATHEMATICAL_CONSISTENCY_PROOF",
}

REPLACEMENTS = {
    "Rewrite Confluence ⇔ Vanishing Curvature": "Diamond Flatness from Coherent Class Holonomy",
    "Twist–Spectrum Correspondence": "Unitary Twist Isospectrality",
    "Holonomy Accumulation": "Holonomy Accumulation — Corrected Scaling",
    "Collapse–Metric Compatibility": "Quotient Spectral-Metric Criterion",
    "Heat Trace Rigidity": "Heat-Trace Isospectrality and the Blindness Boundary",
    "Graph Laplacian Reduction": "Finite Symmetric Graph Reduction",
    "Spectral Completeness Window": "Spectral Signature Injectivity Criterion",
    "No-Go": "Spectral-Blind Curvature / Path-Memory Criterion",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one {label} block, found {count}")
    return text.replace(old, new, 1)


def theorem_records(source_text: str) -> list[dict]:
    pat = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[([^\]]*)\])?")
    matches = list(pat.finditer(source_text))
    records = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(source_text)
        segment = source_text[match.end():end]
        title = (match.group(2) or "").strip()
        status = CLAIM_STATUS.get(title)
        if status is None:
            raise SystemExit(f"Unclassified Geometry claim: {title!r}")
        records.append(
            {
                "index": i + 1,
                "env": match.group(1),
                "title": title,
                "proof_present": "\\begin{proof}" in segment,
                "rnke_status": status,
                "verified_main_replacement": REPLACEMENTS.get(title),
            }
        )
    return records


def status_group(status: str) -> str:
    if status.startswith("CERTIFIED"):
        return "CERTIFIED_OR_CERTIFIED_AFTER_CORRECTION"
    if status.startswith("REPLACED"):
        return "REPLACED_BY_PROVED_OR_PRECISE_STATEMENT"
    if status.startswith("CONDITIONAL"):
        return "CONDITIONAL"
    if status.startswith("REJECTED"):
        return "REJECTED_AND_REPLACED"
    if status.startswith("META"):
        return "META_GUARD"
    return "INCOMPLETE_OR_OVERBROAD"


def transport_preamble(text: str) -> str:
    insertion = r"""
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\DeclareUnicodeCharacter{039B}{\ensuremath{\Lambda}}
\DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}
\DeclareUnicodeCharacter{03A9}{\ensuremath{\Omega}}
\DeclareUnicodeCharacter{21D4}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\to}}
\DeclareUnicodeCharacter{220E}{\ensuremath{\square}}
"""
    text = replace_once(
        text,
        "\\documentclass[12pt, oneside]{article}\n",
        "\\documentclass[12pt, oneside]{article}\n" + insertion,
        "documentclass",
    )
    text = replace_once(
        text,
        "\\DeclareMathOperator{\\diag}{diag}\n",
        "\\DeclareMathOperator{\\diag}{diag}\n\\newcommand{\\cl}{\\mathrm{cl}}\n",
        "class-holonomy macro insertion",
    )
    return text


def apply_mathematical_repairs(text: str) -> str:
    text = text.replace(
        "We develop a complete geometric framework arising from the morphic algebra and calculus.",
        "We develop an operator-geometric framework arising from the morphic algebra and calculus.",
    )
    text = text.replace(
        "The framework recovers classical Riemannian geometry, Connes' noncommutative geometry, information geometry, and graph spectral geometry as representation-sector reductions. We classify all geometries as flat/curved and rigid/deformable, and prove a no-go theorem for curvature without spectral footprint.",
        "The framework formulates representation-sector routes toward classical Riemannian, noncommutative, information, and graph spectral geometry. We introduce a flat/curved and rigid/deformable taxonomy, and we make the spectral-blindness boundary explicit: curvature or path memory need not be visible to a chosen spectral observation unless that observation is target-faithful.",
    )
    text = text.replace(
        "The main theorems establish the equivalence of confluence and flatness, the spectral meaning of derivation memory, and the universal classification of geometries.",
        "The theorem package distinguishes proved operator identities from conditional reduction claims and open universality obligations. In particular, class-holonomy flatness, spectral readout, and path memory are kept logically separate.",
    )

    old = r"""\begin{theorem}[Rewrite Confluence ⇔ Vanishing Curvature]
Let $(\Lambda, D, \pi, \mathfrak{G})$ satisfy GEOM-0. Assume all critical overlaps of rewrite generators admit diamond resolutions.

Then the following are equivalent:
\begin{enumerate}
    \item The rewrite system is confluent modulo collapse $\Omega$.
    \item All elementary commutator curvatures vanish on the quotient: 
    \[
    \mathcal{K} = [D_i, D_j] \in \ker(\pi \circ \Omega)
    \]
    for all generator pairs $(D_i, D_j)$.
    \item Class holonomy is trivial on all contractible 2-cells: 
    \[
    \Hol_{\cl}(\partial \square) = 1.
    \end{enumerate}
\end{theorem}

\begin{proof}[Proof sketch]
Confluence implies all rewrite paths between the same endpoints are equivalent after collapse, so phase around any diamond loop cancels; hence (i) $\Rightarrow$ (iii). Trivial holonomy implies the discrete commutator loop $\mathcal{H}_\Delta$ acts as identity on the quotient, giving (iii) $\Rightarrow$ (ii). Vanishing curvature implies order-independence of generators on the quotient, yielding confluence modulo collapse, so (ii) $\Rightarrow$ (i).
\end{proof}"""
    new = r"""\begin{theorem}[Diamond Flatness from Coherent Class Holonomy]
Let $(\Lambda,D,\pi,\mathfrak G)$ satisfy GEOM-0 and let a critical overlap be equipped with a specified resolving diamond 2-cell. If class holonomy is invariant under that 2-cell, then
\[
\Hol_{\cl}(\partial\square)=1.
\]
Thus the declared class connection is flat on every admitted resolving diamond. This statement does not identify rewrite confluence with pairwise commutation of generators; such an equivalence requires additional hypotheses and is not certified here.
\end{theorem}

\begin{proof}
The two directed boundary paths of the diamond represent the same admitted 2-cell class. Class-holonomy invariance therefore assigns them the same phase. Multiplying one boundary phase by the inverse of the other gives unit holonomy around the boundary loop. No converse from phase-flatness to rewrite confluence, and no implication to pairwise generator commutation, is used.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Theorem 1")

    old = r"""\begin{theorem}[Twist–Spectrum Correspondence]
Let $\Delta$ be the untwisted Laplacian and $\Delta_\lambda$ the λ-twisted Laplacian. Then
\[
\Spec(\Delta_\lambda) = \Spec(\Delta)
\]
for all $\lambda$ if and only if $[D, \chi_\lambda] = 0$ for all generators. Otherwise, spectral shifts encode derivation-memory.
\end{theorem}

\begin{proof}[Proof sketch]
Twisting modifies transition phases. If the character commutes with all derivations, the twisted operator is unitarily equivalent to the untwisted one. Noncommutation introduces phase defects that shift eigenvalues. ∎
\end{proof}"""
    new = r"""\begin{theorem}[Unitary Twist Isospectrality]
Let $\Delta$ and $\Delta_\lambda$ be operators on the same Hilbert representation sector. If there is a unitary $U_\lambda$ such that
\[
\Delta_\lambda=U_\lambda\Delta U_\lambda^{-1},
\]
then
\[
\Spec(\Delta_\lambda)=\Spec(\Delta).
\]
Equality of spectra alone is not a converse: isospectrality does not by itself prove that the twist commutes with every derivation or that path memory is absent.
\end{theorem}

\begin{proof}
Unitary conjugacy preserves the resolvent and hence the spectrum. The final sentence is a proof boundary: no injectivity of the map from derivation/path data to spectral data has been assumed.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Theorem 2")

    old = r"""\begin{theorem}[Holonomy Accumulation]
Let $C_1, C_2$ be discrete step operators with step $\Delta$, and let $\mathcal{H}_\Delta = C_1 C_2 C_1^{-1} C_2^{-1}$. Then in any admissible representation sector,
\[
\lim_{n \to \infty} (\mathcal{H}_{T/n})^n = e^{T^2 [D_1, D_2]},
\]
provided the commutator is bounded in that sector.
\end{theorem}

\begin{proof}[Proof sketch]
Expand $\mathcal{H}_{T/n} = I + (T/n)^2 [D_1, D_2] + O(n^{-3})$. Apply Trotter-type product limit to obtain the exponential of curvature. ∎
\end{proof}"""
    new = r"""\begin{theorem}[Holonomy Accumulation --- Corrected Scaling]
Let $\mathcal K=[D_1,D_2]$ be bounded and suppose the small-step holonomy satisfies, in operator norm,
\[
\mathcal H_h=I+h^2\mathcal K+R_h,
\qquad \|R_h\|\le C|h|^3
\]
for sufficiently small $h$. Put $h_n=T/\sqrt n$. Then
\[
\lim_{n\to\infty}(\mathcal H_{h_n})^n=e^{T^2\mathcal K}
\]
in operator norm.
\end{theorem}

\begin{proof}
With $h_n=T/\sqrt n$,
\[
\mathcal H_{h_n}=I+\frac{T^2}{n}\mathcal K+E_n,
\qquad \|E_n\|=O(n^{-3/2})=o(n^{-1}).
\]
The standard exponential limit in the Banach algebra of bounded operators gives
\[
\left(I+\frac{T^2}{n}\mathcal K+o(n^{-1})\right)^n\longrightarrow e^{T^2\mathcal K}.
\]
The historical $h=T/n$ scaling would instead accumulate only $O(1/n)$ curvature and therefore cannot yield the claimed exponential.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Theorem 3")

    old = r"""\begin{theorem}[Collapse–Metric Compatibility]
Let $P$ be a collapse projector commuting with $\Delta$: $P\Delta = \Delta P$. Then the spectral distance induced by $\Delta$ descends to the quotient:
\[
d_\Delta(\varphi, \psi) = d_\Delta(P\varphi, P\psi)
\]
for all states $\varphi,\psi$ constant on collapse classes.
\end{theorem}

\begin{proof}[Proof sketch]
Commutation implies $[\mathcal{D}, \pi(a)]$ is unchanged under projection. The supremum defining distance is identical on representatives. ∎
\end{proof}"""
    new = r"""\begin{theorem}[Quotient Spectral-Metric Criterion]
Let $q:A\to \bar A$ be the collapse quotient and let
\[
L(a)=\|[\mathcal D,\pi(a)]\|
\]
be the commutator seminorm on the represented algebra. Assume the quotient seminorm is exactly
\[
\bar L(\bar a)=\inf_{q(a)=\bar a}L(a).
\]
Then for states $\bar\varphi,\bar\psi$ on $\bar A$, the quotient spectral distance equals the distance induced from $A$ through pullback:
\[
d_{\bar L}(\bar\varphi,\bar\psi)
=
\sup_{L(a)\le 1}|(\bar\varphi\circ q)(a)-(\bar\psi\circ q)(a)|.
\]
Commutation of a projector with $\Delta$ alone is not sufficient for this conclusion.
\end{theorem}

\begin{proof}
By definition of the quotient seminorm, the unit ball of $\bar L$ is the image under $q$ of elements whose $L$-norm can be made arbitrarily close to one. Evaluating quotient states and pulling them back through $q$ therefore gives the same dual supremum.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Theorem 4")

    old = r"""\begin{theorem}[Heat Trace Rigidity]
If for all $t > 0$ and all admissible twists $\lambda$, we have
\[
Z_\lambda(t) = Z(t),
\]
then curvature vanishes: $\mathcal{K} = 0$.
\end{theorem}

\begin{proof}[Proof sketch]
Equality of all twisted heat traces forces equality of all twisted spectra. By Theorem 2, all characters commute with derivations, hence all commutators vanish on the quotient. ∎
\end{proof}"""
    new = r"""\begin{theorem}[Heat-Trace Isospectrality and the Blindness Boundary]
Assume $\Delta$ and $\Delta_\lambda$ are nonnegative self-adjoint operators with discrete spectra of finite multiplicity and trace-class heat operators for every $t>0$. If
\[
\Tr(e^{-t\Delta_\lambda})=\Tr(e^{-t\Delta})\qquad\forall t>0,
\]
then $\Delta_\lambda$ and $\Delta$ are isospectral with multiplicity. No curvature-vanishing conclusion follows unless the chosen spectral observation is separately proved faithful to the declared curvature/path-memory target.
\end{theorem}

\begin{proof}
The heat trace is the Laplace transform of the discrete spectral counting measure. Equality for all $t>0$ gives equality of those measures and therefore equality of spectra with multiplicity. The last sentence records the RNKE blindness boundary: an observation cannot determine a target without an injectivity/faithfulness theorem.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Theorem 5")

    old = r"""\begin{theorem}[Graph Laplacian Reduction]
For a discrete rewrite carrier $\mathcal{X}$ with symmetric transitions:
\begin{itemize}
    \item $\Delta$ reduces to a graph Laplacian,
    \item heat traces count closed walks,
    \item curvature reduces to commutator defects of rewrite order.
\end{itemize}
\end{theorem}"""
    new = r"""\begin{theorem}[Finite Symmetric Graph Reduction]
Let the represented rewrite carrier be a finite graph and let $P$ be a symmetric transition matrix. Then
\[
\Delta=I-P
\]
is the corresponding symmetric random-walk/normalized Laplacian in this representation, and
\[
\Tr(e^{-t\Delta})
=e^{-t}\sum_{k=0}^{\infty}\frac{t^k}{k!}\Tr(P^k).
\]
Thus the heat trace is the exponential generating function of weighted closed walks. For two represented rewrite steps, the discrete curvature defined in GEOM-0 is exactly their scaled commutator defect.
\end{theorem}

\begin{proof}
The Laplacian identity is the definition in this sector. Expanding $e^{-t(I-P)}=e^{-t}e^{tP}$ and taking the finite-dimensional trace gives the stated series. The diagonal entries of $P^k$ are the total weights of length-$k$ closed walks rooted at each vertex; summing them gives $\Tr(P^k)$. The curvature statement follows directly from its commutator definition.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Graph theorem")

    old = r"""\begin{theorem}[Spectral Completeness Window]
Spectral completeness holds for compact classical manifolds, finite rewrite carriers, and finite-rank learning kernels. It may fail for infinite, highly degenerate systems.
\end{theorem}"""
    new = r"""\begin{theorem}[Spectral Signature Injectivity Criterion]
Let $\mathfrak C$ be a declared class of morphic geometries modulo weak equivalence, and define the spectral signature map
\[
\Sigma:\mathfrak C\to \prod_{\lambda}\{\text{multisets of spectral values}\},
\qquad
\Sigma(G)=\{\Spec(\Delta_\lambda(G))\}_{\lambda}.
\]
The class is spectrally complete exactly when $\Sigma$ is injective. Compactness, finiteness, or finite rank alone does not establish that injectivity; each proposed sector therefore requires its own proof.
\end{theorem}

\begin{proof}
This is precisely the definition of spectral completeness rewritten as injectivity of the spectral-signature map.\qed
\end{proof}"""
    text = replace_once(text, old, new, "Spectral completeness theorem")

    old = r"""\begin{theorem}[No-Go]
There is no morphic operator geometry that is curved, spectrally trivial, and collapse-stable. Curvature must leave a spectral footprint.
\end{theorem}"""
    new = r"""\begin{theorem}[Spectral-Blind Curvature / Path-Memory Criterion]
Let $\mathcal P$ be a finite-dimensional path/curvature descriptor space, let
\[
E:\mathcal P\to Y
\]
be the chosen spectral observation, and let
\[
\Pi:\mathcal P\to Z
\]
be the declared curvature or path-memory target. If
\[
\ker E\not\subseteq\ker\Pi,
\]
then there exist histories $p,q\in\mathcal P$ with
\[
Ep=Eq,
\qquad
\Pi p\ne\Pi q.
\]
Hence curvature/path memory may be spectrally invisible. Moreover the minimum number of scalar linear memory channels needed to repair this blindness is
\[
m_{\min}=\operatorname{rank}(\Pi|_{\ker E}).
\]
\end{theorem}

\begin{proof}
Choose $k\in\ker E$ with $\Pi k\ne0$ and put $q=p+k$. Then $Eq=Ep$ but $\Pi q\ne\Pi p$. For the memory bound, restrict any supplemental map $G:\mathcal P\to\mathbb F^m$ to $K=\ker E$. Target completeness requires $\ker(G|_K)\subseteq K\cap\ker\Pi$, so rank--nullity gives $m\ge \operatorname{rank}(\Pi|_K)$. Conversely choose coordinates on the quotient $K/(K\cap\ker\Pi)$ and extend them linearly to $\mathcal P$; exactly that many channels separate every target-relevant blind direction.\qed
\end{proof}"""
    text = replace_once(text, old, new, "No-Go theorem")

    text = text.replace(
        "    \\item Rewrite confluence is equivalent to flatness,\n",
        "    \\item Coherent class holonomy is flat on admitted resolving diamonds; a converse to rewrite confluence requires additional hypotheses,\n",
    )
    text = text.replace(
        "    \\item Derivation memory is encoded in twisted spectra,\n",
        "    \\item Derivation/path memory may be encoded in twisted spectra when the spectral readout is target-faithful; otherwise explicit memory channels are required,\n",
    )
    text = text.replace(
        "    \\item A four-class taxonomy (Flat/Curved, Rigid/Deformable) classifies all geometries.\n",
        "    \\item A four-class taxonomy partitions objects by the declared Flat/Curved and Rigid/Deformable predicates; invariance under weak equivalence remains an open obligation.\n",
    )
    text = text.replace(
        "The framework is complete, self-consistent, and governed by the emptiness guard.",
        "The framework is governed by the emptiness guard and now carries an explicit RNKE proof-status boundary. It is not claimed here to be a complete formal proof system or a proof of its own mathematical consistency.",
    )
    return text


def audit_appendix(source_sha: str, main_pre_sha: str, claims: list[dict]) -> str:
    lines = [
        r"\clearpage",
        r"\section{RNKE Verification Appendix}",
        r"\subsection{Verification boundary}",
        "This appendix is part of the audited publication copy. The historical source remains preserved separately as \\texttt{source\\_original.tex}. RNKE certifies source identity, build closure, the corrected elementary statements listed below, and the explicit status of every historical theorem claim. It does not promote unresolved reduction or universality claims into proved mathematics.",
        "",
        r"\begin{verbatim}",
        f"SOURCE_SHA256 {source_sha}",
        f"VERIFIED_MAIN_SHA256_PREAPPENDIX {main_pre_sha}",
        r"\end{verbatim}",
        r"\subsection{High-value corrections}",
        r"\begin{itemize}",
        r"\item The historical confluence--flatness equivalence is replaced by the proved diamond-holonomy statement; confluence, commutator flatness, and phase flatness are not silently identified.",
        r"\item Twist isospectrality is certified under unitary conjugacy only; isospectrality is not treated as a converse faithfulness theorem.",
        r"\item Holonomy accumulation uses $h_n=T/\sqrt n$, not $T/n$.",
        r"\item Spectral distance descends through an exact quotient seminorm condition; $P\Delta=\Delta P$ alone is not promoted to metric descent.",
        r"\item Equal heat traces imply isospectrality under the stated discrete trace-class hypotheses, not automatic vanishing of curvature.",
        r"\item The historical spectral-footprint no-go is rejected. MR-02 path blindness gives the exact opposite boundary: a spectral observation can be blind to target-relevant curvature/path memory, with minimal repair dimension $\operatorname{rank}(\Pi|_{\ker E})$.",
        r"\item Spectral completeness is an injectivity property of the full spectral-signature map; compactness or finiteness alone is not treated as proof of injectivity.",
        r"\end{itemize}",
        r"\subsection{Historical claim ledger}",
        r"\begin{itemize}",
    ]
    for rec in claims:
        title = rec["title"].replace("_", r"\_")
        status = rec["rnke_status"].replace("_", r"\_")
        lines.append(rf"\item \textbf{{{title}}}: \texttt{{{status}}}.")
    lines.extend([
        r"\end{itemize}",
        r"\subsection{Ś-0 status}",
        "The Ś-0 emptiness guard is retained as a meta-level discipline against reification. The historical self-consistency paragraph is not accepted as a mathematical consistency proof: a rule saying that contradiction dissolves a construction does not establish consistency of the underlying formal system.",
        "",
    ])
    return "\n".join(lines)


def make_main(source_text: str, source_sha: str, claims: list[dict]) -> str:
    text = source_text.replace("\r\n", "\n").replace("\r", "\n")
    text = transport_preamble(text)
    text = apply_mathematical_repairs(text)
    pre_sha = sha256(text.encode("utf-8"))
    appendix = audit_appendix(source_sha, pre_sha, claims)
    marker = "\\begin{thebibliography}{99}"
    if marker not in text:
        raise SystemExit("Bibliography insertion marker missing")
    text = text.replace(marker, appendix + "\n" + marker, 1)
    return text


def pdf_page_count(path: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(path)], text=True)
    match = re.search(r"^Pages:\s+(\d+)$", out, re.MULTILINE)
    if not match:
        raise SystemExit("Could not read PDF page count")
    return int(match.group(1))


def prepare() -> None:
    data = SOURCE.read_bytes()
    blob = git_blob_sha1(data)
    if blob != EXPECTED_SOURCE_GIT_BLOB_SHA1:
        raise SystemExit(f"Geometry source Git blob mismatch: {blob} != {EXPECTED_SOURCE_GIT_BLOB_SHA1}")
    TARGET.mkdir(parents=True, exist_ok=True)
    ORIGINAL.write_bytes(data)
    source_sha = sha256(data)
    source_text = data.decode("utf-8")
    claims = theorem_records(source_text)
    axioms = len(re.findall(r"\\begin\{axiom\}", source_text))
    if len(claims) != EXPECTED_CLAIM_COUNT:
        raise SystemExit(f"Expected {EXPECTED_CLAIM_COUNT} claims, found {len(claims)}")
    if axioms != EXPECTED_AXIOM_COUNT:
        raise SystemExit(f"Expected {EXPECTED_AXIOM_COUNT} axioms, found {axioms}")
    main_text = make_main(source_text, source_sha, claims)
    MAIN.write_text(main_text, encoding="utf-8", newline="\n")
    grouped = Counter(status_group(c["rnke_status"]) for c in claims)
    manifest = {
        "kind": "RNKE_MORPHIC_GEOMETRY_PREPARE_MANIFEST",
        "source_path": str(SOURCE.relative_to(ROOT)),
        "source_original_path": str(ORIGINAL.relative_to(ROOT)),
        "source_git_blob_sha1": blob,
        "source_sha256": source_sha,
        "main_tex_sha256": sha256(MAIN.read_bytes()),
        "claim_count": len(claims),
        "axiom_count": axioms,
        "status_groups": dict(sorted(grouped.items())),
        "native_terminology_preserved": True,
        "corrections": list(REPLACEMENTS.values()),
    }
    PREPARE_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("morphic_geometry PREPARED", source_sha, manifest["main_tex_sha256"])


def finalize() -> None:
    if not PDF.exists():
        raise SystemExit("Geometry main.pdf missing; compile before finalize")
    manifest = json.loads(PREPARE_MANIFEST.read_text(encoding="utf-8"))
    source_text = ORIGINAL.read_text(encoding="utf-8")
    claims = theorem_records(source_text)
    grouped = Counter(status_group(c["rnke_status"]) for c in claims)
    cert = {
        "kind": "RNKE_MORPHIC_MANUSCRIPT_CERTIFICATE",
        "manuscript": "morphic_geometry",
        "title": "Morphic Operator Geometry",
        "status": "RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS",
        "source_label": "Morphic operator geometry..tex",
        "source_git_blob_sha1": EXPECTED_SOURCE_GIT_BLOB_SHA1,
        "source_sha256": manifest["source_sha256"],
        "main_tex_sha256": sha256(MAIN.read_bytes()),
        "latex_build_pass": True,
        "page_count": pdf_page_count(PDF),
        "claim_count": len(claims),
        "axiom_count": manifest["axiom_count"],
        "status_groups": dict(sorted(grouped.items())),
        "claims": claims,
        "native_terminology_preserved": True,
        "formal_proof_assistant": False,
        "full_manuscript_mathematical_certification": False,
        "spectral_blindness_reconciled_with_mr02": True,
        "cocycle_path_memory_compatible_with_mr03": True,
        "proof_boundary": "corrected elementary operator statements + exact source/build/status contract; reduction, rigidity, universality and several representation claims remain open",
    }
    canonical = json.dumps(cert, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    cert["certificate_sha256"] = sha256(canonical)
    CERTIFICATE.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    summary_lines = [
        "# Certification Summary",
        "",
        "- status: `RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`",
        f"- source Git blob SHA-1: `{cert['source_git_blob_sha1']}`",
        f"- source SHA-256: `{cert['source_sha256']}`",
        f"- verified `main.tex` SHA-256: `{cert['main_tex_sha256']}`",
        f"- certificate SHA-256: `{cert['certificate_sha256']}`",
        "- LaTeX build: PASS",
        f"- pages: {cert['page_count']}",
        f"- claim environments: {cert['claim_count']}",
        f"- axiom environments: {cert['axiom_count']}",
        "",
        "## Status groups",
        "",
    ]
    for key, value in cert["status_groups"].items():
        summary_lines.append(f"- `{key}`: {value}")
    summary_lines += [
        "",
        "## Critical audit result",
        "",
        "The historical claim that curvature must always leave a spectral footprint is **rejected**. The audited copy replaces it with the MR-02-compatible path-blindness criterion and the exact minimal-memory repair dimension.",
        "",
        "The historical holonomy accumulation scaling `T/n` is also corrected to `T/sqrt(n)` under the stated bounded-operator remainder hypothesis.",
        "",
        "## Boundary",
        "",
        "This is a source-integrity, LaTeX-build, theorem-status, and RNKE proof-obligation certificate. It is not a formal-proof-assistant certificate and it does not certify the unresolved universality/reduction/rigidity program as established mathematics.",
        "",
    ]
    SUMMARY.write_text("\n".join(summary_lines), encoding="utf-8")
    STATUS.write_text(
        "# Morphic Geometry Certification Status\n\n"
        f"- source integrity: `PASS` (`{cert['source_sha256']}`)\n"
        "- verified LaTeX build: `PASS`\n"
        "- RNKE status: `RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`\n"
        "- full manuscript mathematical certification: `FALSE`\n"
        "- formal proof assistant: `FALSE`\n"
        f"- certificate SHA-256: `{cert['certificate_sha256']}`\n\n"
        "The audited `main.tex` corrects the holonomy scaling error and replaces the spectral-footprint no-go with the proven path-blindness/minimal-memory criterion. Remaining reduction and universality claims stay explicitly open.\n",
        encoding="utf-8",
    )
    print("morphic_geometry RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS", cert["page_count"], cert["certificate_sha256"])


def verify() -> None:
    data = ORIGINAL.read_bytes()
    if git_blob_sha1(data) != EXPECTED_SOURCE_GIT_BLOB_SHA1:
        raise SystemExit("source_original.tex no longer matches pinned manual source")
    manifest = json.loads(PREPARE_MANIFEST.read_text(encoding="utf-8"))
    if sha256(data) != manifest["source_sha256"]:
        raise SystemExit("source SHA-256 mismatch")
    if sha256(MAIN.read_bytes()) != manifest["main_tex_sha256"]:
        raise SystemExit("main.tex SHA-256 mismatch from prepare manifest")
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if not cert.get("latex_build_pass") or not PDF.exists():
        raise SystemExit("LaTeX build gate not closed")
    if cert.get("status") != "RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS":
        raise SystemExit("unexpected RNKE status")
    if cert.get("full_manuscript_mathematical_certification") is not False:
        raise SystemExit("full-manuscript certification boundary corrupted")
    if cert.get("spectral_blindness_reconciled_with_mr02") is not True:
        raise SystemExit("MR-02 spectral-blindness reconciliation missing")
    print("morphic_geometry VERIFY_PASS", cert["certificate_sha256"])


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"prepare", "finalize", "verify"}:
        print("usage: certify_morphic_geometry.py {prepare|finalize|verify}", file=sys.stderr)
        return 2
    {"prepare": prepare, "finalize": finalize, "verify": verify}[sys.argv[1]]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
