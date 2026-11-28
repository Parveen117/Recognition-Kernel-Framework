"""Check the declared Tamil and Hebrew fixtures with exact recognition tools."""

from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from unicodedata import normalize

from proof_lab.morphic_recognition.guarded import (
    GuardedSystem,
    distinguishing_word,
    minimal_quotient,
    observe_word,
    retention_supports_updates,
)
from proof_lab.morphic_recognition.memory import Matrix, identity, rank, seam_repair

from .hebrew_context import (
    ABSOLUTE_FORMS,
    CONSTRUCT_FORMS,
    contextual_readings,
    plural_outcomes,
    unpoint,
)


def tamil_noun(
    singular: str, plural: str, singular_oblique: str
) -> GuardedSystem:
    forms = {"singular": singular, "plural": plural}
    transitions = {("singular", "PL"): "plural"}
    for number, oblique in (("singular", singular_oblique), ("plural", plural)):
        for case, mark in (("ACC", "ை"), ("LOC", "ில்")):
            state = f"{number} {case}"
            forms[state] = oblique.removesuffix("்") + mark
            transitions[number, case] = state
    return GuardedSystem(tuple(forms), ("PL", "ACC", "LOC"), forms, transitions)


def check_tamil() -> None:
    # The two lexically scoped stem changes precede the common case endings.
    tree = "மரம்"
    house = "வீடு"
    tree_stem = tree.removesuffix("ம்")
    house_stem = house.removesuffix("டு")
    for system, expected in (
        (tamil_noun(tree, tree_stem + "ங்கள்", tree_stem + "த்த்"),
         ("மரம்", "மரங்கள்", "மரத்தை", "மரத்தில்", "மரங்களை", "மரங்களில்")),
        (tamil_noun(house, house + "கள்", house_stem + "ட்ட்"),
         ("வீடு", "வீடுகள்", "வீட்டை", "வீட்டில்", "வீடுகளை", "வீடுகளில்")),
    ):
        words = ((), ("PL",), ("ACC",), ("LOC",), ("PL", "ACC"), ("PL", "LOC"))
        for word, form in zip(words, expected, strict=True):
            assert observe_word(system, "singular", word) == (True, form)
        for case in ("ACC", "LOC"):
            assert observe_word(system, "singular", (case, "PL")) == (False, None)


def class_projector(labels: tuple[str, ...]) -> Matrix:
    return Matrix(
        (tuple(Fraction(left == right, labels.count(left)) for right in labels)
         for left in labels),
        len(labels),
    )


def difference(left: Matrix, right: Matrix) -> Matrix:
    assert left.shape == right.shape
    return Matrix(
        (tuple(a - b for a, b in zip(left_row, right_row, strict=True))
         for left_row, right_row in zip(left.rows, right.rows, strict=True)),
        left.ncols,
    )


def check_hebrew() -> None:
    analyses = tuple(ABSOLUTE_FORMS)
    singulars = tuple(normalize("NFC", pair[0]) for pair in ABSOLUTE_FORMS.values())
    plurals = plural_outcomes(analyses, pointed=True)
    unpointed_inputs = tuple(map(unpoint, singulars))
    unpointed_plurals = tuple(map(unpoint, plurals))
    assert len(set(singulars)) == 3
    assert unpointed_inputs == ("כתב", "כתב", "כתב")
    assert unpointed_plurals == ("כתבו", "כתבים", "כתבים")

    inputs = tuple(f"pointed {analysis}" for analysis in analyses)
    hidden = tuple(f"unpointed {analysis}" for analysis in analyses)
    outputs = tuple(f"plural {analysis}" for analysis in analyses)
    transitions = {
        **{(source, "ERASE"): target for source, target in zip(inputs, hidden, strict=True)},
        **{(source, "PLURAL"): target for source, target in zip(hidden, outputs, strict=True)},
    }
    states = inputs + hidden + outputs
    visible = Matrix([[1, 1, 1]], 3)
    transport = identity(3)
    middle_cut = class_projector(unpointed_inputs)
    middle_memory = difference(transport, middle_cut)
    assert middle_cut @ middle_cut == middle_cut
    assert middle_memory @ middle_memory == middle_memory
    assert visible @ middle_memory == Matrix([[0, 0, 0]], 3)
    assert rank(middle_memory) == 2

    for terminal_forms, expected_memory in ((unpointed_plurals, 1), (plurals, 2)):
        system = GuardedSystem(
            states,
            ("ERASE", "PLURAL"),
            dict(zip(states, singulars + unpointed_inputs + terminal_forms, strict=True)),
            transitions,
        )
        _, retained = minimal_quotient(system)
        assert len({retained[state] for state in hidden}) == expected_memory + 1
        assert retention_supports_updates(system, retained)
        for state, expected_form in zip(inputs, terminal_forms, strict=True):
            assert observe_word(system, state, ("ERASE", "PLURAL")) == (True, expected_form)
        for left, right in combinations(range(3), 2):
            witness = distinguishing_word(system, hidden[left], hidden[right])
            expected = None if terminal_forms[left] == terminal_forms[right] else ("PLURAL",)
            assert witness == expected

        terminal_classes = tuple(dict.fromkeys(terminal_forms))
        target = Matrix(
            (tuple(int(label == form) for form in terminal_forms) for label in terminal_classes),
            3,
        )
        repair = seam_repair(visible, target, transport)
        assert repair.minimum_channels == expected_memory
        assert repair.repaired_decoder @ repair.repaired_basis == target
        assert any(target.apply((0, 1, -1))) == (expected_memory == 2)
        assert any(target.apply((1, -1, 0)))

        terminal_cut = class_projector(terminal_forms)
        assert terminal_cut @ terminal_cut == terminal_cut
        assert target @ terminal_cut == target
        visible_composition = (terminal_cut @ transport @ middle_cut) @ (middle_cut @ transport)
        residue = (terminal_cut @ transport @ middle_memory) @ (middle_memory @ transport)
        direct_composition = terminal_cut @ transport @ transport
        assert difference(direct_composition, visible_composition) == residue
        assert rank(residue) == expected_memory


def check_hebrew_context() -> None:
    pooled = contextual_readings("כתב")
    nouns = contextual_readings("כתב", slot="noun")
    verb = contextual_readings("כתב", following=("את",))
    script = contextual_readings("כתב", following=("העת",))
    reporter = contextual_readings("כתב", previous="מדווח", following=("העיתון",))
    assert pooled == ("verb", "script", "reporter")
    assert nouns == ("script", "reporter")
    assert verb == ("verb",) and script == ("script",) and reporter == ("reporter",)
    assert contextual_readings("כתב", following=("יד",)) == script
    assert contextual_readings("כתב", following=("העיתון", "מדווח")) == reporter
    assert contextual_readings("כתב", following=("העיתון",)) == pooled
    assert contextual_readings("כתב", following=("אישום",)) == pooled
    assert contextual_readings("כתב", following=("את",), slot="noun") == ()
    assert contextual_readings("מכתב", following=("את",)) == ()
    assert plural_outcomes((), pointed=False) == ()
    assert plural_outcomes(nouns, pointed=False) == ("כתבים",)
    assert tuple(unpoint(pair[0]) for pair in CONSTRUCT_FORMS.values()) == ("כתב", "כתב")
    assert plural_outcomes(nouns, pointed=False, construct=True) == ("כתבי",)
    assert tuple(map(unpoint, plural_outcomes(nouns, pointed=True, construct=True))) == ("כתבי", "כתבי")

    for readings, construct, expected_channels in (
        (pooled, False, (1, 2)),
        (nouns, False, (0, 1)),
        (nouns, True, (0, 1)),
        (verb, False, (0, 0)),
        (script, True, (0, 0)),
        (reporter, True, (0, 0)),
    ):
        count = len(readings)
        for pointed, expected in zip((False, True), expected_channels, strict=True):
            target_labels = tuple(plural_outcomes((reading,), pointed=pointed, construct=construct)[0]
                                  for reading in readings)
            target = Matrix(
                (tuple(int(label == output) for label in target_labels)
                 for output in dict.fromkeys(target_labels)),
                count,
            )
            repair = seam_repair(Matrix([[1] * count], count), target, identity(count))
            assert repair.minimum_channels == expected
            assert len(plural_outcomes(readings, pointed=pointed, construct=construct)) == expected + 1


def audit_htb(directory: Path) -> None:
    # Read surface tokens, including original fused spellings in multiword rows.
    # The target POS tag is read only when scoring an already selected candidate.
    sources = {
        "dev": ("4c7fcc2df3eeec7e0e06841cd2027d2c6f0fe7519758f56a8775ba0a5c6c6640", 1, {}),
        "test": ("026fcebd2e953776fe9e954ae5506a2c9d1a7449266ce0cbe76b3297ed793ce7", 12,
                 {"script": 8}),
        "train": ("85438a480ff81ddc78cbfc14813b4670ea25b98286990a9211cff382f1eb58d7", 23,
                  {"verb": 1, "script": 1, "reporter": 2}),
    }
    for split, (digest, expected_total, expected_hits) in sources.items():
        data = (directory / f"he_htb-ud-{split}.conllu").read_bytes()
        assert sha256(data).hexdigest() == digest, f"unexpected HTB {split} revision"
        total = 0
        hits: Counter[str] = Counter()
        for sentence in data.decode().split("\n\n"):
            surface = []
            fused_through = 0
            for line in sentence.splitlines():
                if not line or line.startswith("#"):
                    continue
                columns = line.split("\t")
                token_id, form = columns[:2]
                if "-" in token_id:
                    fused_through = int(token_id.split("-")[1])
                elif not token_id.isdecimal() or int(token_id) <= fused_through:
                    continue
                if form not in {"-", "־"}:
                    surface.append((form, columns[3]))
            for index, (form, gold_pos) in enumerate(surface):
                if form != "כתב":
                    continue
                total += 1
                previous = surface[index - 1][0] if index else ""
                following = tuple(word for word, _ in surface[index + 1:index + 3])
                readings = contextual_readings(form, previous=previous, following=following)
                if len(readings) == 1:
                    reading, = readings
                    assert gold_pos == ("VERB" if reading == "verb" else "NOUN")
                    hits[reading] += 1
        assert total == expected_total and hits == expected_hits
        print(f"HTB {split}: {hits.total()}/{total} resolved, {total - hits.total()} open.")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run the benchmark without optimization so assertions execute")
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--htb", type=Path, help="optional checkout of the pinned Hebrew treebank")
    args = parser.parse_args()
    check_tamil()
    check_hebrew()
    check_hebrew_context()
    print("Tamil: 12 forms and 4 reverse-order refusals across two nouns and two cases.")
    print("Hebrew: 2 unpointed classes / 1 channel, 3 pointed classes / 2 channels.")
    print("Hebrew: exact T24 residue ranks 1 unpointed and 2 pointed.")
    print("Hebrew: noun context reduces additional channels to 0 unpointed / 1 pointed.")
    if args.htb is not None:
        audit_htb(args.htb)
