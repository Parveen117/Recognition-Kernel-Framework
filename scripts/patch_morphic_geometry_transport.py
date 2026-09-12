#!/usr/bin/env python3
"""Complete pdflatex Unicode transport for the audited Morphic Geometry copy.

This does not alter source_original.tex. It only adds explicit LaTeX mappings to
the generated main.tex and rebinds the prepare-manifest hash to that audited copy.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "theorum" / "morphic_geometry" / "main.tex"
MANIFEST = ROOT / "theorum" / "morphic_geometry" / "PREPARE_MANIFEST.json"

DECLARATIONS = r"""\DeclareUnicodeCharacter{1E41}{\.{m}}
\DeclareUnicodeCharacter{1E43}{\d{m}}
\DeclareUnicodeCharacter{1E63}{\d{s}}
\DeclareUnicodeCharacter{0101}{\={a}}
\DeclareUnicodeCharacter{012B}{\={i}}
\DeclareUnicodeCharacter{016B}{\={u}}
\DeclareUnicodeCharacter{015A}{\'{S}}
\DeclareUnicodeCharacter{1E47}{\d{n}}
\DeclareUnicodeCharacter{1E5B}{\d{r}}
\DeclareUnicodeCharacter{1E6D}{\d{t}}
\DeclareUnicodeCharacter{1E0D}{\d{d}}
"""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    text = MAIN.read_text(encoding="utf-8")
    if "\\DeclareUnicodeCharacter{1E41}" not in text:
        needle = "\\usepackage{lmodern}\n"
        if text.count(needle) != 1:
            raise SystemExit(f"Expected one lmodern insertion point, found {text.count(needle)}")
        text = text.replace(needle, needle + DECLARATIONS, 1)
        MAIN.write_text(text, encoding="utf-8", newline="\n")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["main_tex_sha256"] = sha256(MAIN.read_bytes())
    manifest["transport_patch"] = "explicit IAST/Sanskrit Unicode declarations for pdflatex"
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("morphic_geometry TRANSPORT_PATCHED", manifest["main_tex_sha256"])


if __name__ == "__main__":
    main()
