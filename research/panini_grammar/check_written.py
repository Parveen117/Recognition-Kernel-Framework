"""Check the written-stage register and its recorded changes in coverage."""

import json
import re
import sys
from pathlib import Path

GRAMMAR = Path(__file__).resolve().parent
ROOT = GRAMMAR.parents[1]
STAGE = re.compile(r"^# PG([1-9][0-9]*)\b")
COUNTS = {
    "finite_positions": "finite_position_delta",
    "nominal_positions": "nominal_position_delta",
    "nominal_readings": "nominal_reading_delta",
}


def check():
    assert sys.version_info[:2] == (3, 12), "Python 3.12 is required"
    work = (GRAMMAR / "CURRENT_WORK.md").read_text()
    latest = int(re.search(r"\bPG(\d+)\b", work.splitlines()[0])[1])
    stages = {}
    for readme in [GRAMMAR / "README.md", *GRAMMAR.glob("*/README.md")]:
        with readme.open() as source:
            match = STAGE.match(source.readline())
        if match:
            number = int(match[1])
            if number in stages:
                raise ValueError(f"Duplicate PG{number} at {readme} and {stages[number]}")
            stages[number] = readme
    if sorted(stages) != list(range(1, latest + 1)):
        raise ValueError(f"Stage register has a gap or disagrees with CURRENT_WORK PG{latest}")

    handoffs = sorted(GRAMMAR.glob("WORK_SESSION_????_??_??.md"))
    for nav in [GRAMMAR / "CURRENT_WORK.md", GRAMMAR / "README.md", ROOT / "MATHEMATICS_INDEX.md",
                GRAMMAR / "WRITTEN_BACKLOG.md", handoffs[-1]]:
        link = stages[latest].relative_to(nav.parent).as_posix()
        if not any(f"PG{latest}" in line and f"]({link})" in line for line in nav.read_text().splitlines()):
            raise ValueError(f"{nav.name} lacks the PG{latest} stage link")

    previous = {}
    checked = 0
    # PG53 introduced STATE.json. PG1–PG52 publish evidence in earlier formats.
    for number in range(53, latest + 1):
        file = stages[number].with_name("STATE.json")
        state = json.loads(file.read_text())
        label = f"PG{number}"
        if state.get("stage", label) != label or type(state["finite_positions"]) is not int:
            raise ValueError(f"{file}: stage identity or finite count")
        baseline = state.get("baseline")
        if isinstance(baseline, str):
            target = file.parent / baseline
            if target.resolve() != stages[number - 1].with_name("STATE.json").resolve():
                raise ValueError(f"{label} baseline does not point to PG{number - 1}")
        elif isinstance(baseline, dict) and "path" in baseline:
            name = Path(baseline["path"])
            if name.is_absolute() or not any((base / name).is_file() for base in (ROOT, GRAMMAR, file.parent)):
                raise ValueError(f"{label} missing published baseline {name}")
        current = {}
        for field, delta_field in COUNTS.items():
            if field not in state:
                continue
            total = state[field]
            if type(total) is not int or total < 0:
                raise ValueError(f"{label} invalid {field}")
            current[field] = total
            # Corrections can withdraw or restore previously counted keys.
            delta = state.get(delta_field, state.get("new_" + field))
            if delta is not None and field in previous:
                if type(delta) is not int or total != previous[field] + delta:
                    raise ValueError(f"{label} {field}: {previous[field]} + {delta} != {total}")
                checked += 1
        # Only the immediately preceding, present counter values cross the stage boundary.
        previous = current
        del state, baseline
    print(f"PG1–PG{latest}: {len(stages)} stages, {latest - 52} state records, "
          f"{checked} published changes reconciled. Latest " +
          ", ".join(f"{key}={previous[key]}" for key in COUNTS))


if __name__ == "__main__":
    check()
