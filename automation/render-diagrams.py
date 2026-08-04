#!/usr/bin/env python3
"""Render every D2 source to SVG, deterministically.

Why this exists rather than a bare `d2 in.d2 out.svg`:

D2 scopes each SVG's CSS with a generated class name — `d2-1681756903` and so
on — so that several diagrams embedded on one page cannot restyle each other.
The number is derived per-platform. The same source rendered on Windows and on
a Linux CI runner produces two SVGs whose geometry is identical to the pixel
(the viewBox matches exactly) and whose class names do not.

That is invisible to a reader and very visible to git. Because the pipeline
commits rendered output back, it meant every push to `main` produced an
auto-render commit rewriting a file nobody had touched — the derived-file drift
this repository exists to argue against, happening in the repository itself.

`--salt` does not fix it. It changes the number without making it
platform-independent; both platforms just land somewhere new.

So the id is replaced with one derived from the diagram's filename. It is
stable across platforms because nothing about the machine feeds into it, and
still unique per diagram, which is the property D2 wanted from the hash in the
first place.

This is part of generation, not a hand-edit of generated output: it is applied
by this script, on every render, identically.

    python automation/render-diagrams.py            # render all
    python automation/render-diagrams.py --check    # parse only, write nothing

Requires the `d2` binary on PATH. No Python dependencies.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "diagrams" / "source"
RENDERED = REPO / "diagrams" / "rendered"

# D2's generated scope, e.g. "d2-1681756903". Six or more digits so a literal
# like "d2-1" in a diagram label can never be mistaken for one.
SCOPE = re.compile(rb"d2-\d{6,}")


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def normalize(svg: Path, diagram: str) -> None:
    """Rewrite D2's generated CSS scope to one derived from the filename.

    Read and written as bytes so the file passes through untouched apart from
    the id itself — no re-encoding, no line-ending translation.
    """
    data = svg.read_bytes()
    found = SCOPE.search(data)
    if not found:
        # Newer D2 may stop emitting a scope id, in which case there is
        # nothing to pin and the output is already deterministic.
        return
    svg.write_bytes(data.replace(found.group(), f"d2-{diagram}".encode()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true",
        help="prove every source parses; write nothing to diagrams/rendered/",
    )
    args = parser.parse_args()

    if not shutil.which("d2"):
        return fail("d2 is not on PATH — see https://d2lang.com")

    sources = sorted(SOURCE.glob("*.d2"))
    if not sources:
        return fail(f"no .d2 files found in {SOURCE.relative_to(REPO).as_posix()}")

    if not args.check:
        RENDERED.mkdir(parents=True, exist_ok=True)

    failed = 0
    for source in sources:
        diagram = source.stem
        if args.check:
            # Render to a throwaway path purely to prove the source parses.
            with tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / "check.svg"
                result = subprocess.run(
                    ["d2", str(source), str(target)],
                    capture_output=True, text=True,
                )
        else:
            target = RENDERED / f"{diagram}.svg"
            result = subprocess.run(
                ["d2", str(source), str(target)],
                capture_output=True, text=True,
            )

        if result.returncode != 0:
            # GitHub Actions renders this as an annotation on the file itself.
            print(f"::error file={source.relative_to(REPO).as_posix()}::"
                  f"D2 source failed to parse", file=sys.stderr)
            print(result.stderr.strip(), file=sys.stderr)
            failed += 1
            continue

        if args.check:
            print(f"  ok    {source.relative_to(REPO).as_posix()}")
        else:
            normalize(target, diagram)
            print(f"  {source.relative_to(REPO).as_posix()} -> "
                  f"{target.relative_to(REPO).as_posix()}  [scope: d2-{diagram}]")

    if failed:
        return fail(f"{failed} diagram(s) failed to render")
    return 0


if __name__ == "__main__":
    sys.exit(main())
