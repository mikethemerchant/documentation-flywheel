#!/usr/bin/env python3
"""Validate the application inventory and render every derived view from it.

Two jobs, in this order:

1. **Gate.** Every app and integration record is checked against
   `inventory/schema.yaml`. A value that is not in the schema is a hard
   failure, not a warning — that is the whole reason the schema exists. Run
   with `--validate-only` in CI on a pull request to fail before merge.

2. **Render.** Everything downstream of the records is generated: the summary
   views, one page per application, and the integration landscape diagram
   source. None of it is maintained by hand, so none of it can drift out of
   agreement with the records or with itself.

Only dependency is PyYAML.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

# Windows consoles still default to a legacy code page. Every file this script
# writes is explicitly UTF-8; make the progress output match so a record with a
# non-ASCII name fails validation loudly rather than crashing the reporter.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent
SCHEMA_FILE = REPO / "inventory" / "schema.yaml"
APP_DATA = REPO / "inventory" / "apps" / "data"
INTEGRATION_DATA = REPO / "inventory" / "integrations" / "data"
RENDERED = REPO / "inventory" / "rendered"
APP_PAGES = REPO / "inventory" / "apps"
D2_SOURCE = REPO / "diagrams" / "source" / "integration-landscape.d2"

# schema.yaml keeps one flat `fields:` namespace covering both record types,
# because a reader wants to see the whole controlled vocabulary in one place.
# These four lists are the only thing that knows which field belongs to which
# record — keep them in step with the schema when adding a field.
APP_CONTROLLED = [
    "vendor", "capability", "primary_users", "it_sme", "it_technical_owner",
    "it_manager", "it_team_accountable", "lifecycle_status", "hosting",
    "criticality_tier", "recovery_owner",
]
APP_FREETEXT = ["name", "purpose", "rto", "rpo", "notes"]
INTEGRATION_CONTROLLED = ["direction", "connection_type", "middleware", "dr_impact"]
INTEGRATION_FREETEXT = ["name", "source", "target", "failover_behavior", "notes"]

# Free-text fields the schema cannot express a requirement for.
APP_REQUIRED_FREETEXT = ["name", "purpose"]
INTEGRATION_REQUIRED_FREETEXT = ["name", "source", "target"]

# Values that mean "we looked and we do not know". Rendered as gaps rather
# than as answers, and reported by gap-analysis.py.
GAP_VALUES = {"Unknown", "TBD"}

HEADER = (
    "<!-- GENERATED FILE — DO NOT EDIT.\n"
    "     Written by automation/render-inventory.py from the YAML records in\n"
    "     inventory/apps/data/ and inventory/integrations/data/.\n"
    "     Edit the source records and re-render; edits here are overwritten. -->\n\n"
)

D2_HEADER = (
    "# GENERATED FILE — DO NOT EDIT.\n"
    "# Written by automation/render-inventory.py from the integration records\n"
    "# in inventory/integrations/data/. This diagram is derived from data, not\n"
    "# drawn: add an integration record and the picture redraws itself.\n"
    "# Every other .d2 file in this folder is hand-authored.\n\n"
)


# ── Loading ───────────────────────────────────────────────────────────────

def load_yaml(path: Path) -> dict:
    """Parse one YAML file, turning a parse error into a violation-shaped exit."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"{rel(path)}: YAML did not parse — {exc}")
    if not isinstance(data, dict):
        fail(f"{rel(path)}: expected a mapping at the top level")
    return data


def load_records(folder: Path) -> dict[str, dict]:
    """Load every .yaml in a folder, keyed by slug (the filename stem)."""
    return {p.stem: load_yaml(p) for p in sorted(folder.glob("*.yaml"))}


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


# ── Validation ────────────────────────────────────────────────────────────

def as_list(value) -> list:
    """Normalize scalar-or-list into a list. Multi-valued fields accept both."""
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def validate_record(slug, record, kind, schema, app_slugs) -> list[str]:
    """Check one record against the schema. Returns a list of problem strings.

    Every message names the file, the field, and the offending value, because
    a schema failure is only useful if the person reading the build log can
    fix it without opening the validator.
    """
    if kind == "app":
        controlled, freetext = APP_CONTROLLED, APP_FREETEXT
        required_freetext, folder = APP_REQUIRED_FREETEXT, APP_DATA
    else:
        controlled, freetext = INTEGRATION_CONTROLLED, INTEGRATION_FREETEXT
        required_freetext, folder = INTEGRATION_REQUIRED_FREETEXT, INTEGRATION_DATA

    where = rel(folder / f"{slug}.yaml")
    problems = []

    for key in record:
        if key not in controlled and key not in freetext:
            problems.append(
                f"{where}: unknown field '{key}' — not defined for {kind} records"
            )

    for field in required_freetext:
        if not record.get(field):
            problems.append(f"{where}: required field '{field}' is missing or empty")

    for field in controlled:
        definition = schema["fields"][field]
        value = record.get(field)

        if definition.get("required") and not value:
            problems.append(f"{where}: required field '{field}' is missing or empty")
            continue
        if value is None:
            continue

        if isinstance(value, list) and not definition.get("multi"):
            problems.append(
                f"{where}: field '{field}' holds a list but is single-valued"
            )
            continue

        # A field with no `values:` list is free text by design (rto, rpo, and
        # recovery_owner). Nothing to check beyond its shape.
        allowed = definition.get("values")
        if not allowed:
            continue

        for item in as_list(value):
            if item not in allowed:
                problems.append(
                    f"{where}: field '{field}' has value '{item}', which is not in "
                    f"the schema. Allowed: {', '.join(map(str, allowed))}"
                )

    # A dangling source or target is what silently breaks the graph, so it is
    # a build failure rather than a node quietly missing from the diagram.
    if kind == "integration":
        for field in ("source", "target"):
            ref = record.get(field)
            if ref and ref not in app_slugs:
                problems.append(
                    f"{where}: field '{field}' points at '{ref}', which is not an "
                    f"application record in inventory/apps/data/"
                )

    return problems


def validate_all(apps, integrations, schema) -> list[str]:
    problems = []
    for slug, record in apps.items():
        problems += validate_record(slug, record, "app", schema, set(apps))
    for slug, record in integrations.items():
        problems += validate_record(slug, record, "integration", schema, set(apps))
    return problems


# ── Model helpers ─────────────────────────────────────────────────────────

def find_core_system(apps, integrations) -> str:
    """The application the most other systems write into.

    Derived rather than configured. Hard-coding a slug here would mean the
    renderer stops being true the moment the portfolio changes, and "which
    system is the core one" is a fact the integration records already carry.
    """
    writes_into = defaultdict(int)
    for record in integrations.values():
        if record.get("direction") in ("Inbound", "Bidirectional"):
            writes_into[record["target"]] += 1
    if not writes_into:
        return ""
    return max(sorted(writes_into), key=lambda slug: writes_into[slug])


def neighbourhood(slug, integrations):
    """Integrations touching one app, split by which end it sits on."""
    inbound = {k: v for k, v in integrations.items() if v.get("target") == slug}
    outbound = {k: v for k, v in integrations.items() if v.get("source") == slug}
    return inbound, outbound


def display(apps, slug) -> str:
    return apps.get(slug, {}).get("name", slug)


def joined(value, empty="—") -> str:
    items = as_list(value)
    return " / ".join(str(i) for i in items) if items else empty


def cell(text) -> str:
    """Flatten a value for a markdown table cell."""
    if text is None:
        return "—"
    flat = " ".join(str(text).split())
    return flat.replace("|", "\\|") or "—"


def link(slug, apps) -> str:
    """Link from a rendered view to an application's detail page."""
    return f"[{display(apps, slug)}](../apps/{slug}.md)"


def gap(value) -> str:
    """Mark a known-unknown so it reads as a gap rather than as an answer."""
    return f"**{value}**" if str(value) in GAP_VALUES else str(value)


def write(path: Path, body: str, header: str = HEADER) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header + body.rstrip() + "\n", encoding="utf-8")
    print(f"  wrote {rel(path)}")


def table(headings, rows) -> str:
    """Build a markdown table. Returns an em dash line if there are no rows."""
    if not rows:
        return "_None._\n"
    out = ["| " + " | ".join(headings) + " |",
           "|" + "|".join("---" for _ in headings) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def grouped(apps, field):
    """Group app slugs by a single- or multi-valued field."""
    groups = defaultdict(list)
    for slug, record in sorted(apps.items(), key=lambda kv: kv[1]["name"].lower()):
        values = as_list(record.get(field)) or ["Not recorded"]
        for value in values:
            groups[value].append(slug)
    return dict(sorted(groups.items()))


# ── Views ─────────────────────────────────────────────────────────────────

def render_all_applications(apps, integrations):
    rows = []
    for slug, record in sorted(apps.items(), key=lambda kv: kv[1]["name"].lower()):
        inbound, outbound = neighbourhood(slug, integrations)
        rows.append([
            link(slug, apps),
            cell(record.get("vendor")),
            cell(joined(record.get("capability"))),
            cell(record["lifecycle_status"]),
            cell(record.get("it_team_accountable")),
            cell(gap(joined(record.get("it_sme")))),
            cell(gap(record.get("hosting", "—"))),
            cell(record.get("criticality_tier")),
            str(len(inbound) + len(outbound)),
        ])
    body = (
        f"# All Applications\n\n"
        f"{len(apps)} application records, rendered from `inventory/apps/data/`.\n\n"
        + table(
            ["Application", "Vendor", "Capability", "Lifecycle", "Team",
             "SME", "Hosting", "Tier", "Integrations"],
            rows,
        )
        + "\nBold values are recorded gaps — see `automation/gap-analysis.py`.\n"
    )
    write(RENDERED / "all-applications.md", body)


def render_by_vendor(apps):
    sections = []
    for vendor, slugs in grouped(apps, "vendor").items():
        rows = [[link(s, apps), cell(apps[s]["lifecycle_status"]),
                 cell(apps[s].get("it_team_accountable")),
                 cell(gap(joined(apps[s].get("it_sme"))))] for s in slugs]
        sections.append(
            f"## {vendor}\n\n_{len(slugs)} application(s)._\n\n"
            + table(["Application", "Lifecycle", "Team", "SME"], rows)
        )
    body = (
        "# Applications by Vendor\n\n"
        "Concentration is the thing to look for here: a vendor holding several "
        "records is a single commercial relationship carrying more of the "
        "estate than its individual records suggest.\n\n"
        + "\n".join(sections)
    )
    write(RENDERED / "by-vendor.md", body)


def render_by_owner(apps):
    """Person-centric rather than application-centric.

    "What does this person hold?" is the question actually asked — at
    handover, during an incident, and when somebody resigns — and it is the
    one an application-ordered list answers worst.
    """
    roles = {
        "it_sme": "SME",
        "it_technical_owner": "Technical owner",
        "it_manager": "Manager",
        "recovery_owner": "Recovery owner",
    }
    held = defaultdict(lambda: defaultdict(list))
    for slug, record in apps.items():
        for field, label in roles.items():
            for person in as_list(record.get(field)):
                held[person][slug].append(label)

    sections = []
    for person in sorted(held, key=lambda p: (p in GAP_VALUES, p)):
        rows = []
        for slug in sorted(held[person], key=lambda s: apps[s]["name"].lower()):
            rows.append([link(slug, apps), ", ".join(held[person][slug]),
                         cell(apps[slug]["lifecycle_status"]),
                         cell(apps[slug].get("criticality_tier"))])
        heading = f"## {person}"
        if person in GAP_VALUES:
            heading += "\n\n_Not a person. These records have no owner recorded " \
                       "for the roles listed._"
        sections.append(
            f"{heading}\n\n_{len(rows)} record(s)._\n\n"
            + table(["Application", "Role(s)", "Lifecycle", "Tier"], rows)
        )
    body = (
        "# Applications by Owner\n\n"
        "Every named role across the portfolio, per person. A person holding a "
        "long list of Tier 1 records is a concentration risk that no single "
        "application record shows.\n\n"
        + "\n".join(sections)
    )
    write(RENDERED / "by-owner.md", body)


def render_by_team(apps):
    sections = []
    for team, slugs in grouped(apps, "it_team_accountable").items():
        rows = [[link(s, apps), cell(apps[s].get("vendor")),
                 cell(apps[s]["lifecycle_status"]),
                 cell(gap(joined(apps[s].get("it_sme")))),
                 cell(apps[s].get("criticality_tier"))] for s in slugs]
        sections.append(
            f"## {team}\n\n_{len(slugs)} application(s)._\n\n"
            + table(["Application", "Vendor", "Lifecycle", "SME", "Tier"], rows)
        )
    body = (
        "# Applications by Accountable Team\n\n"
        "Team-level accountability, which is a different question from who to "
        "call. The people are in `by-owner.md`.\n\n"
        + "\n".join(sections)
    )
    write(RENDERED / "by-team.md", body)


def render_capability_map(apps):
    """The overlap view — what do we already own that does this?

    Asked before a purchase, this is the single most expensive question the
    inventory answers. It only works because `capability` is a controlled
    value: as free text, two records covering the same ground describe it
    differently and never collide.
    """
    groups = grouped(apps, "capability")
    overlaps = {c: s for c, s in groups.items() if len(s) > 1}

    overlap_rows = [
        [cell(capability), str(len(slugs)),
         ", ".join(link(s, apps) for s in slugs)]
        for capability, slugs in overlaps.items()
    ]

    sections = []
    for capability, slugs in groups.items():
        rows = [[link(s, apps), cell(apps[s].get("vendor")),
                 cell(apps[s]["lifecycle_status"]),
                 cell(apps[s].get("it_team_accountable"))] for s in slugs]
        marker = "  ⚠ covered by more than one application" if len(slugs) > 1 else ""
        sections.append(
            f"## {capability}{marker}\n\n"
            + table(["Application", "Vendor", "Lifecycle", "Team"], rows)
        )

    body = (
        "# Capability Map\n\n"
        "What the portfolio can do, and what covers each capability. The "
        "question this exists to answer is **\"what do we already own that "
        "does this?\"** — asked before a purchase, not after one.\n\n"
        "## Capabilities covered more than once\n\n"
        "Overlap is not automatically waste. Some of these are deliberate "
        "complements and some are duplication nobody has noticed; the map "
        "cannot tell them apart, and the point is that somebody now has to "
        "look.\n\n"
        + table(["Capability", "Applications", "Covered by"], overlap_rows)
        + "\n---\n\n"
        + "\n".join(sections)
    )
    write(RENDERED / "capability-map.md", body)


def render_integration_matrix(apps, integrations, core):
    connected = sorted(
        {r["source"] for r in integrations.values()}
        | {r["target"] for r in integrations.values()},
        key=lambda s: apps[s]["name"].lower(),
    )
    index = {slug: n for n, slug in enumerate(connected, start=1)}

    # Column headers are indexes so the grid stays narrow enough to read. The
    # legend directly above it carries the names.
    headings = ["→ target"] + [str(n) for n in index.values()]
    grid = []
    for slug in connected:
        row = [f"**{index[slug]}.** {display(apps, slug)}"]
        for target in connected:
            match = [
                r for r in integrations.values()
                if r["source"] == slug and r["target"] == target
            ]
            reverse = [
                r for r in integrations.values()
                if r["source"] == target and r["target"] == slug
                and r.get("direction") == "Bidirectional"
            ]
            if match:
                row.append("●" if match[0].get("direction") != "Bidirectional" else "◆")
            elif reverse:
                row.append("◆")
            else:
                row.append("")
        grid.append(row)

    detail = [
        [link(r["source"], apps), link(r["target"], apps), cell(r.get("direction")),
         cell(r.get("connection_type")), cell(r.get("middleware")),
         cell(gap(r.get("dr_impact", "—")))]
        for _, r in sorted(integrations.items(), key=lambda kv: kv[1]["name"].lower())
    ]

    unconnected = sorted(
        (s for s in apps if s not in index), key=lambda s: apps[s]["name"].lower()
    )

    body = (
        "# Integration Matrix\n\n"
        f"{len(integrations)} integration records across {len(connected)} of "
        f"{len(apps)} applications.\n\n"
        "## Grid\n\n"
        "Rows are sources, columns are targets. ● is a one-way flow, ◆ is "
        "bidirectional.\n\n"
        + table(headings, grid)
        + "\n## Every integration\n\n"
        "`Direction` is stated relative to the core transactional system of "
        f"record ({display(apps, core)}) — **Inbound** means it writes into "
        "that system.\n\n"
        + table(["Source", "Target", "Direction", "Connection", "Middleware",
                 "DR impact"], detail)
        + "\n## Applications with no integration records\n\n"
        "Either genuinely standalone, or connected by something nobody has "
        "recorded yet. The inventory cannot tell you which, and that is worth "
        "saying out loud rather than rendering as an empty row.\n\n"
        + table(["Application", "Lifecycle", "Team"],
                [[link(s, apps), cell(apps[s]["lifecycle_status"]),
                  cell(apps[s].get("it_team_accountable"))] for s in unconnected])
    )
    write(RENDERED / "integration-matrix.md", body)


def render_dr_posture(apps, integrations, core):
    """What writes into the core system, and what happens when it is down."""
    severity = {
        "Cannot stop - data loss risk": 0,
        "Unknown": 1,
        "Stoppable - manual reconciliation": 2,
        "Stoppable - queued, replays": 3,
        "Stoppable - no data loss": 4,
    }

    def rank(record):
        return (severity.get(record.get("dr_impact"), 9), record["name"].lower())

    writes = sorted(
        (r for r in integrations.values()
         if r["target"] == core and r.get("direction") in ("Inbound", "Bidirectional")),
        key=rank,
    )
    write_rows = [
        [cell(display(apps, r["source"])), cell(r.get("connection_type")),
         cell(r.get("middleware")), cell(gap(r.get("dr_impact", "—"))),
         cell(r.get("failover_behavior"))]
        for r in writes
    ]

    by_impact = defaultdict(list)
    for record in integrations.values():
        by_impact[record.get("dr_impact") or "Not recorded"].append(record)
    impact_sections = []
    for impact in sorted(by_impact, key=lambda i: severity.get(i, 9)):
        rows = [[cell(r["name"]), cell(r.get("connection_type")),
                 cell(r.get("failover_behavior"))]
                for r in sorted(by_impact[impact], key=lambda r: r["name"].lower())]
        marker = " — not characterized" if impact in GAP_VALUES else ""
        impact_sections.append(
            f"### {impact}{marker}\n\n"
            + table(["Flow", "Connection", "Failover behaviour"], rows)
        )

    tier_order = {"Tier 1 - Critical": 0, "Tier 2 - Important": 1,
                  "Tier 3 - Standard": 2}
    recovery_rows = [
        [link(s, apps), cell(r.get("criticality_tier")), cell(r.get("rto")),
         cell(r.get("rpo")), cell(gap(joined(r.get("recovery_owner"))))]
        for s, r in sorted(
            apps.items(),
            key=lambda kv: (tier_order.get(kv[1].get("criticality_tier"), 9),
                            kv[1]["name"].lower()),
        )
    ]

    # A retiring application still moving data is the class of problem this
    # view exists to catch: the lifecycle field says it is on the way out and
    # the integration records say it is still load-bearing.
    live_but_retiring = []
    for slug, record in sorted(apps.items()):
        if record["lifecycle_status"] not in ("Retiring", "Retired"):
            continue
        inbound, outbound = neighbourhood(slug, integrations)
        for key, flow in sorted({**inbound, **outbound}.items()):
            live_but_retiring.append([
                link(slug, apps), cell(record["lifecycle_status"]), cell(flow["name"]),
                cell(gap(flow.get("dr_impact", "—"))),
                cell(gap(joined(record.get("it_sme")))),
            ])

    body = (
        "# DR Posture\n\n"
        f"The core transactional system of record is **{display(apps, core)}**, "
        "derived from the integration records as the application the most other "
        "systems write into — not configured anywhere.\n\n"
        f"## What writes into {display(apps, core)}\n\n"
        "Ordered by how badly it goes if the flow is interrupted. This is the "
        "list you want in front of you before a failover, and the one that is "
        "hardest to reconstruct under pressure.\n\n"
        + table(["Source", "Connection", "Middleware", "DR impact",
                 "Failover behaviour"], write_rows)
        + "\n## Flags\n\n"
        "Applications on their way out that still carry live data flows.\n\n"
        + table(["Application", "Lifecycle", "Flow", "DR impact", "SME"],
                live_but_retiring)
        + "\n## Every flow, by impact\n\n"
        + "\n".join(impact_sections)
        + "\n## Application recovery targets\n\n"
        + table(["Application", "Tier", "RTO", "RPO", "Recovery owner"],
                recovery_rows)
    )
    write(RENDERED / "dr-posture.md", body)


def render_app_pages(apps, integrations, core):
    for slug, record in sorted(apps.items()):
        inbound, outbound = neighbourhood(slug, integrations)

        def flow_rows(flows, other_end):
            return [
                [cell(display(apps, r[other_end])), cell(r.get("direction")),
                 cell(r.get("connection_type")), cell(r.get("middleware")),
                 cell(gap(r.get("dr_impact", "—")))]
                for _, r in sorted(flows.items(), key=lambda kv: kv[1]["name"].lower())
            ]

        ownership = table(["Role", "Who"], [
            ["SME (who to call)", cell(gap(joined(record.get("it_sme"))))],
            ["Technical owner", cell(gap(joined(record.get("it_technical_owner"))))],
            ["Manager", cell(gap(joined(record.get("it_manager"))))],
            ["Accountable team", cell(record.get("it_team_accountable"))],
        ])
        profile = table(["Field", "Value"], [
            ["Vendor", cell(record.get("vendor"))],
            ["Capability", cell(joined(record.get("capability")))],
            ["Primary users", cell(joined(record.get("primary_users")))],
            ["Lifecycle", cell(record["lifecycle_status"])],
            ["Hosting", cell(gap(record.get("hosting", "—")))],
        ])
        recovery = table(["Field", "Value"], [
            ["Criticality", cell(record.get("criticality_tier"))],
            ["RTO", cell(record.get("rto"))],
            ["RPO", cell(record.get("rpo"))],
            ["Recovery owner", cell(gap(joined(record.get("recovery_owner"))))],
        ])

        body = (
            f"# {record['name']}\n\n"
            f"{' '.join(str(record['purpose']).split())}\n\n"
            "## Ownership\n\n" + ownership
            + "\n## Profile\n\n" + profile
            + "\n## Recovery\n\n" + recovery
            + "\n## Integration neighbourhood\n\n"
            "`Direction` below is stated relative to the core transactional "
            f"system of record ({display(apps, core)}), which is why an arrow "
            "into this application can still read as Outbound.\n\n"
            "### Flows in — this application is the target\n\n"
            + table(["From", "Direction", "Connection", "Middleware", "DR impact"],
                    flow_rows(inbound, "source"))
            + "\n### Flows out — this application is the source\n\n"
            + table(["To", "Direction", "Connection", "Middleware", "DR impact"],
                    flow_rows(outbound, "target"))
        )
        if record.get("notes"):
            body += "\n## Notes\n\n" + str(record["notes"]).strip() + "\n"
        body += (
            f"\n---\n\nSource record: "
            f"[`inventory/apps/data/{slug}.yaml`](data/{slug}.yaml)\n"
        )
        write(APP_PAGES / f"{slug}.md", body)


# ── The generated diagram ─────────────────────────────────────────────────

def d2_id(text: str) -> str:
    """D2 keys are safest as bare word characters; labels carry the real text."""
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()


def render_landscape_d2(apps, integrations, core):
    """Write the integration landscape as D2 source, from the records.

    Nobody draws this diagram. Nodes are grouped by the team accountable for
    them, edges are styled by direction, and a write into the core system of
    record is drawn distinctly because that is the class of flow somebody is
    usually looking for when they open it.
    """
    # Legend lines are kept short on purpose: a D2 markdown block clips rather
    # than wraps, so a long line loses its tail in the rendered SVG silently.
    lines = [
        # Down beats right here: it keeps the aspect ratio near 2:1 and lets
        # the team containers sit side by side, so the flows converging on the
        # core system stay the thing you notice first.
        "direction: down",
        "",
        "legend: |md",
        "  ### Integration landscape",
        "",
        f"  Generated from {len(integrations)} integration",
        "  records, grouped by accountable team.",
        "",
        "  - **Red edge** — writes into the core",
        "    system of record",
        "  - **Dashed edge** — no middleware in the",
        "    path to hold a message",
        "  - **Dashed box** — retiring or retired",
        "  - **?** — DR impact not characterized",
        "|",
        "",
    ]

    for team, slugs in grouped(apps, "it_team_accountable").items():
        lines.append(f'{d2_id(team)}: "{team}" {{')
        lines.append("  style.fill: transparent")
        for slug in slugs:
            record = apps[slug]
            label = record["name"]
            if record["lifecycle_status"] != "Active":
                label += f"\\n[{record['lifecycle_status']}]"
            lines.append(f'  {d2_id(slug)}: "{label}" {{')
            lines.append("    shape: rectangle")
            if record["lifecycle_status"] in ("Retiring", "Retired"):
                lines.append("    style.stroke-dash: 4")
                lines.append("    style.opacity: 0.7")
            if slug == core:
                lines.append("    style.bold: true")
                lines.append("    style.stroke-width: 3")
            lines.append("  }")
        lines.append("}")
        lines.append("")

    node = {
        slug: f"{d2_id(record.get('it_team_accountable') or 'Not recorded')}."
              f"{d2_id(slug)}"
        for slug, record in apps.items()
    }

    lines.append("# ── Flows ────────────────────────────────────────────────")
    for _, record in sorted(integrations.items(), key=lambda kv: kv[1]["name"].lower()):
        source, target = record["source"], record["target"]
        arrow = "<->" if record.get("direction") == "Bidirectional" else "->"
        writes_into_core = (
            target == core and record.get("direction") in ("Inbound", "Bidirectional")
        )
        label = record.get("connection_type") or record.get("direction") or ""

        lines.append(f'{node[source]} {arrow} {node[target]}: "{label}" {{')
        if writes_into_core:
            lines.append('  style.stroke: "#b3352b"')
            lines.append("  style.stroke-width: 3")
            lines.append("  style.bold: true")
        else:
            lines.append('  style.stroke: "#5a6b7c"')
            lines.append("  style.stroke-width: 2")
        # No middleware means nothing between the two systems that can hold a
        # message — worth seeing at a glance next to the DR posture view.
        if record.get("middleware") in ("Direct (none)", "Manual"):
            lines.append("  style.stroke-dash: 3")
        if record.get("dr_impact") in GAP_VALUES:
            lines.append('  target-arrowhead.label: "?"')
        lines.append("}")

    lines += [
        "",
        "# Notes (kept as comments — tooltips do not survive markdown renderers)",
        f"#   Core system of record: {display(apps, core)} ({core}) — derived as",
        "#   the application the most other systems write into.",
        "#   A '?' on an arrowhead means the DR impact of that flow is not known.",
        "#   Dashed node border means the application is Retiring or Retired.",
    ]
    write(D2_SOURCE, "\n".join(lines), header=D2_HEADER)


# ── Entry point ───────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--validate-only", action="store_true",
        help="check every record against the schema and write nothing",
    )
    args = parser.parse_args()

    schema = load_yaml(SCHEMA_FILE)
    apps = load_records(APP_DATA)
    integrations = load_records(INTEGRATION_DATA)

    if not apps:
        fail(f"no application records found in {rel(APP_DATA)}")

    problems = validate_all(apps, integrations, schema)
    if problems:
        print(
            f"Schema validation FAILED — {len(problems)} problem(s):\n",
            file=sys.stderr,
        )
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        print(
            "\nFix the record, or add the value to inventory/schema.yaml in the "
            "same change.",
            file=sys.stderr,
        )
        return 1

    print(
        f"Schema validation passed: {len(apps)} applications, "
        f"{len(integrations)} integrations."
    )
    if args.validate_only:
        return 0

    core = find_core_system(apps, integrations)
    print(f"Core system of record derived as: {display(apps, core)} ({core})")

    render_all_applications(apps, integrations)
    render_by_vendor(apps)
    render_by_owner(apps)
    render_by_team(apps)
    render_capability_map(apps)
    render_integration_matrix(apps, integrations, core)
    render_dr_posture(apps, integrations, core)
    render_app_pages(apps, integrations, core)
    render_landscape_d2(apps, integrations, core)
    print("Render complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
