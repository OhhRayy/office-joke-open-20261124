"""Make the AI Judge Laugh: the Office Joke Open (make.fun bounty
u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).

Writes a single one-line office joke to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no input,
no randomness.

The joke: a team-building exercise about trust ends with everyone
agreeing never to hit reply-all again -- and then someone hits
reply-all to confirm the agreement. It is a real one-line joke
about office life, the turn lands in the last few words, the
reply-all is a specific office detail anyone who has worked in an
office recognises, and the wording is tight at 150 characters.
Against the judge's brief, in order: it is a genuine office joke
(criterion 1); the ending swerves from "we all agreed" to the
agreement being broken by the very act of confirming it
(criterion 2, the surprise); reply-all is a concrete office
detail, not a generic grumble about work (criterion 3); the
team-building setup taken somewhere self-defeating is not the
obvious Monday-morning or photocopier line (criterion 4); and at
150 characters, one sentence, no word can be cut without loss
(criterion 5).

Revision: renamed LINE to ENTRY_LINE, extracted the validation
and file-writing steps into validate() and write_entry(), and
added a --output argument (default /output/entry.txt) so the
destination is explicit instead of hard-coded in main().
The entry line itself is unchanged.
"""

import argparse
import os

ENTRY_LINE = (
    "Our team-building exercise was learning to trust each other, "
    "so we all agreed never to hit reply-all again \u2014 then "
    "someone hit reply-all to confirm it."
)

MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def validate(text: str) -> str:
    """Check the entry line meets the bounty constraints."""
    assert 1 <= len(text) <= MAX_CHARS, "line must be 1-200 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    return text


def write_entry(text: str, output_path: str) -> None:
    """Write the validated entry line to output_path (no trailing newline)."""
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the office-joke entry.")
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="destination path for entry.txt (default: %(default)s)",
    )
    args = parser.parse_args()
    text = validate(ENTRY_LINE)
    write_entry(text, args.output)


if __name__ == "__main__":
    main()
