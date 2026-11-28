"""Finite context adapter for three lexemes written כתב in Modern Hebrew."""

from unicodedata import category, normalize


# Singular and plural forms. The hyphen joining a construct to its complement
# is outside these head forms.
ABSOLUTE_FORMS = {
    "verb": ("כָּתַב", "כָּתְבוּ"),
    "script": ("כְּתָב", "כְּתָבִים"),
    "reporter": ("כַּתָּב", "כַּתָּבִים"),
}
CONSTRUCT_FORMS = {
    "script": ("כְּתַב", "כִּתְבֵי"),
    "reporter": ("כַּתַּב", "כַּתָּבֵי"),
}
SLOTS = {None: tuple(ABSOLUTE_FORMS), "verb": ("verb",), "noun": tuple(CONSTRUCT_FORMS)}


def unpoint(form: str) -> str:
    # The fixture contains Hebrew base letters plus combining points only.
    return "".join(char for char in normalize("NFD", form) if category(char) != "Mn")


def contextual_readings(
    token: str,
    *,
    previous: str = "",
    following: tuple[str, ...] = (),
    slot: str | None = None,
) -> tuple[str, ...]:
    """Return admitted lexical candidates using a small set of written cues.

    `slot`, when supplied, is independently established context. No cue keeps
    all candidates in that slot. An incompatible cue gives the empty tuple.
    """
    admitted = SLOTS[slot]
    if token != "כתב":
        return ()

    cue = None
    next_word = following[0] if following else ""
    if next_word == "את":
        cue = "verb"
    elif next_word in {"יד", "עת", "העת"}:
        cue = "script"
    elif next_word == "העיתון" and (previous == "מדווח" or following[1:2] == ("מדווח",)):
        cue = "reporter"

    return admitted if cue is None else tuple(reading for reading in admitted if reading == cue)


def plural_outcomes(
    readings: tuple[str, ...], *, pointed: bool, construct: bool = False
) -> tuple[str, ...]:
    """Return distinct target spellings. The construct probe takes noun readings."""
    forms = CONSTRUCT_FORMS if construct else ABSOLUTE_FORMS
    plurals = (normalize("NFC", forms[reading][1]) for reading in readings)
    return tuple(dict.fromkeys(form if pointed else unpoint(form) for form in plurals))
