"""Check the declared Tamil and Hebrew fixtures with exact recognition tools."""

from fractions import Fraction
from itertools import combinations
from unicodedata import category, normalize

from proof_lab.morphic_recognition.guarded import (
    GuardedSystem,
    distinguishing_word,
    minimal_quotient,
    observe_word,
    retention_supports_updates,
)
from proof_lab.morphic_recognition.memory import Matrix, identity, rank, seam_repair


def check_tamil() -> None:
    singular = "மரம்"
    stem = singular.removesuffix("ம்")
    plural = stem + "ங்கள்"
    singular_accusative = stem + "த்தை"
    plural_accusative = plural.removesuffix("ள்") + "ளை"
    system = GuardedSystem(
        ("singular", "plural", "singular accusative", "plural accusative"),
        ("PL", "ACC"),
        {
            "singular": singular,
            "plural": plural,
            "singular accusative": singular_accusative,
            "plural accusative": plural_accusative,
        },
        {
            ("singular", "PL"): "plural",
            ("singular", "ACC"): "singular accusative",
            ("plural", "ACC"): "plural accusative",
        },
    )
    assert observe_word(system, "singular", ("PL",)) == (True, "மரங்கள்")
    assert observe_word(system, "singular", ("ACC",)) == (True, "மரத்தை")
    assert observe_word(system, "singular", ("PL", "ACC")) == (True, "மரங்களை")
    assert observe_word(system, "singular", ("ACC", "PL")) == (False, None)


def unpoint(form: str) -> str:
    # The fixture contains Hebrew letters plus combining points only.
    return "".join(char for char in normalize("NFD", form) if category(char) != "Mn")


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
    analyses = ("verb", "script", "reporter")
    singulars = tuple(normalize("NFC", word) for word in ("כָּתַב", "כְּתָב", "כַּתָּב"))
    plurals = tuple(normalize("NFC", word) for word in ("כָּתְבוּ", "כְּתָבִים", "כַּתָּבִים"))
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


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run the benchmark without optimization so assertions execute")
    check_tamil()
    check_hebrew()
    print("Tamil: plural then accusative passes, reverse order fails its guard.")
    print("Hebrew: 2 unpointed classes / 1 channel, 3 pointed classes / 2 channels.")
    print("Hebrew: exact T24 residue ranks 1 unpointed and 2 pointed.")
