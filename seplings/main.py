from typer import Typer, Argument
from pathlib import Path
from random import choice
from importlib.resources import files
from shutil import copytree

from seplings.validators import check

app = Typer()


@app.command()
def init() -> None:
    source = Path(files(anchor="seplings")) / "exercises"
    destination = Path.cwd() / "exercises"

    try:
        copytree(src=source, dst=destination)
    except FileExistsError:
        print("\n ❌ Seplings already copied!\n")
        exit(1)

    print(f"\n ✅ Seplings are available in {destination}!\n")


@app.command()
def run(module: str = Argument(..., help="Exercise module to run.")) -> None:
    module_path = Path.cwd() / "exercises" / module

    compliments = [
        "Nice work!",
        "Well done!",
        "Great job!",
        "Excellent!",
        "Looking good!",
        "That's awesome!",
        "Brilliant!",
        "Fantastic!",
        "Perfect!",
        "Impressive!",
        "Nicely done!",
        "Smooth!",
        "Spot on!",
        "Love it!",
        "You're on fire!",
        "Keep it up!",
        "Nailed it!",
        "Outstanding!",
    ]

    insults = [
        "Sad times.",
        "Have you tried turning it off and on again?",
        "You will be an excellent vibe coder!",
        "Perhaps consider a different line of work.",
        "Never don't give up.",
        "Your failure will inspire others.",
        "Confidence was not the issue.",
        "An educational experience.",
        "Reality intervened.",
        "That could have gone better.",
        "Hope was temporary.",
        "You found another way not to.",
        "Excellence was unavailable.",
        "Task failed successfully.",
        "Your optimism was misplaced.",
        "You fought the odds. The odds won.",
        "You have a unique relationship with success.",
        "You almost exceeded expectations.",
        "We ran out of encouraging things to say."
    ]

    try:
        exercises = sorted([item for item in module_path.iterdir() if item.is_file()])
    except FileNotFoundError:
        print(" ❌ Invalid exercise module!")
        exit(1)

    for i, exercise in enumerate(exercises):
        success, details = check(exercise=exercise)

        if not success:
            print(f"\n ❌ Exercise {i + 1}: {choice(insults)} \n")
            print(details)
            exit(1)
        else:
            print(f"\n ✅ Exercise {i + 1}: {choice(compliments)}")


if __name__ == "__main__":
    app()
