from pathlib import Path
from subprocess import run


def check(exercise: Path) -> tuple[bool, str]:
    result = run(args=["mypy", "--strict", exercise], capture_output=True, check=False, text=True)

    if result.returncode != 0:
        return False, result.stdout + result.stderr

    return True, "Well done!"
