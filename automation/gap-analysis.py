#!/usr/bin/env python3
"""Report what the inventory does not know yet.

This is the other half of the flywheel. `render-inventory.py` publishes what
is known; this prints what is missing, and that list is what the next
conversation with an SME is for.

It exits 0 even when it finds gaps. Gaps are the normal state of an honest
inventory — a portfolio with none has either been finished or been tidied,
and the second is far more likely. The schema gate in `render-inventory.py`
is the thing that fails a build; this is a to-do list.

Only dependency is PyYAML.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

# Windows consoles still default to a legacy code page, and integration names
# carry arrows. Without this the report crashes on the first one, which is a
# confusing way to learn that your terminal is the problem and not your data.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent
APP_DATA = REPO / "inventory" / "apps" / "data"
INTEGRATION_DATA = REPO / "inventory" / "integrations" / "data"

# The values that mean "we looked and we do not know", as opposed to a field
# left blank because it does not apply. Only the first kind is a gap.
UNKNOWN = "Unknown"
TBD = "TBD"


def load(folder: Path) -> dict[str, dict]:
    return {
        p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in sorted(folder.glob("*.yaml"))
    }


def as_list(value) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def section(title: str, why: str, rows: list[str]) -> int:
    """Print one finding group. Returns how many gaps it held."""
    print(f"\n{title}")
    print("-" * len(title))
    print(f"{why}\n")
    if not rows:
        print("  (none)")
    for row in rows:
        print(f"  {row}")
    return len(rows)


def main() -> int:
    apps = load(APP_DATA)
    integrations = load(INTEGRATION_DATA)

    print("=" * 72)
    print("INVENTORY GAP ANALYSIS")
    print(f"{len(apps)} applications, {len(integrations)} integrations")
    print("=" * 72)

    total = 0

    total += section(
        "Applications with no SME recorded",
        "Nobody to call. This is the gap that matters most, because every\n"
        "other unknown is answerable by the person who is missing here.",
        [
            f"{apps[s]['name']:<42} ({s})"
            for s in sorted(apps, key=lambda s: apps[s]["name"].lower())
            if UNKNOWN in as_list(apps[s].get("it_sme"))
        ],
    )

    total += section(
        "Applications with hosting not yet determined",
        "Where it runs is unsettled. Until it is, nobody can say who patches\n"
        "it, whose network boundary it sits inside, or what recovering it means.",
        [
            f"{apps[s]['name']:<42} ({s})"
            for s in sorted(apps, key=lambda s: apps[s]["name"].lower())
            if apps[s].get("hosting") == TBD
        ],
    )

    total += section(
        "Integrations with unknown DR impact",
        "What happens to this data flow during a core-system outage has not\n"
        "been characterized. Each one is a decision that will get made under\n"
        "pressure instead of in advance.",
        [
            f"{integrations[s]['name']}"
            for s in sorted(integrations, key=lambda s: integrations[s]["name"].lower())
            if integrations[s].get("dr_impact") == UNKNOWN
        ],
    )

    connected = {r["source"] for r in integrations.values()}
    connected |= {r["target"] for r in integrations.values()}
    total += section(
        "Applications with no integration records",
        "Either genuinely standalone, or connected by a path nobody has\n"
        "written down. The inventory cannot tell the difference — a human has\n"
        "to look at each one and say which it is.",
        [
            f"{apps[s]['name']:<42} ({s})"
            for s in sorted(apps, key=lambda s: apps[s]["name"].lower())
            if s not in connected
        ],
    )

    # Cross-cutting: a retiring application still moving data is not one gap,
    # it is a combination of otherwise-reasonable records. Only a query across
    # both files finds it, which is the argument for holding the inventory as
    # a graph rather than as two lists.
    retiring_but_live = []
    for slug in sorted(apps, key=lambda s: apps[s]["name"].lower()):
        if apps[slug].get("lifecycle_status") not in ("Retiring", "Retired"):
            continue
        for record in integrations.values():
            if slug in (record.get("source"), record.get("target")):
                retiring_but_live.append(
                    f"{apps[slug]['name']} — {record['name']} "
                    f"[DR impact: {record.get('dr_impact') or 'not recorded'}]"
                )
    total += section(
        "Applications on their way out that still move data",
        "Marked Retiring or Retired, and still carrying live integrations.\n"
        "Retiring is a status, not a state.",
        retiring_but_live,
    )

    print("\n" + "=" * 72)
    print(f"{total} open gap(s). Each one is a question for a person, not a task.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
