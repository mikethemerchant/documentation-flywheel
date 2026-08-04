# Prompt — Add or Update an Inventory Record

For application records in `inventory/apps/data/` and integration records in
`inventory/integrations/data/`.

---

You are working in the `documentation-flywheel` repository. Read `README.md`,
`meta/repo-conventions.md` (the Inventory Record Naming section),
`inventory/schema.yaml`, and two or three existing records before writing.

Add or update a record for:

> **<THE APPLICATION OR INTEGRATION, and where the facts came from — a
> transcript, a vendor document, a person>**

## Naming

- **The vendor goes in `vendor`, never in `name`.** `name: Warehouse Management
  (WMS)` + `vendor: Meridian Systems` — not `name: Meridian Warehouse
  Management`. A name carrying its vendor fights every filter built on top of it.
- Put the common short name or acronym in parentheses: `Product Name (Short)`.
  Omit it when there is no widely-used short form.
- Application filename: `kebab-case.yaml`, and **that slug is permanent**
  (`DEC-005`). Integration records reference it in `source` and `target`;
  renaming it breaks the graph. If the display name later changes, the slug
  does not follow — add a comment at the top of the record explaining the
  mismatch, or someone will helpfully "fix" it.
- Integration filename: `<source-slug>--<target-slug>.yaml`, full slugs on both
  sides.

## Fields

Every controlled field must use a value already in `inventory/schema.yaml`.

**If a value is missing, add it to the schema in the same change** — and say so
in your handover, because it needs approval per `context/decision-rights.md`.
Do not reach for a near-enough existing value to avoid the gate; that is
exactly the drift the gate exists to stop.

**Owners are people.** `it_sme`, `it_technical_owner`, `it_manager`, and
`recovery_owner` hold named individuals from the roster. A team name is
rejected by validation, and would answer nothing anyway — "Infrastructure owns
it" tells you nobody to call. Team-level accountability has its own field,
`it_team_accountable`. Where a role is genuinely shared, list everyone.

**Never invent a person into the roster.** If the source names an owner who is
not in `schema.yaml`, that is a schema change with an approver, not something
you add quietly.

**Prefer `Unknown` to a guess.** An unknown owner is a recorded finding that
`gap-analysis.py` will surface and someone will act on. A plausible name that
is wrong is worse than the gap, because nothing will ever catch it (`DEC-011`).

**Write `notes` for a reader, not a field.** Date anything that came from a
conversation, in the form already used in the records:
`2026-03-04 (integration review): ...`

## Integration records specifically

The fields that make this a graph rather than a list are the ones people rush.

- `direction` is **relative to the source system**. This is what makes "what
  writes into the ERP?" answerable, and it feeds the DR posture view.
- `failover_behavior` is free text and should be a real sentence about what
  happens to in-flight data, not a restatement of `dr_impact`. Compare the
  existing records: the good ones say who reconciles what, and when they find
  out.
- `dr_impact: Unknown` is legitimate and useful. "Not characterized" is a
  finding worth surfacing — see the legacy order path.
- `source` and `target` must resolve to existing app slugs. A dangling
  reference fails the build, deliberately.

## Validate

```bash
python automation/render-inventory.py --validate-only
python automation/render-inventory.py
python automation/gap-analysis.py
```

The gate names the file, the field, and the offending value. It is worth
breaking a record on purpose once to see what a failure looks like.

The full render regenerates the views, the per-app pages, and the landscape
diagram source. **Do not edit any of that output** — it is machine-written, and
the diff is there to show you the consequence of your change.

## After writing

- Add an insight row to `inventory/insights-surfaced.md` if the record exposed
  an ownership gap, a single point of failure, an unowned overlap, or a
  retirement with no date.
- Confirm you are not on `main`, then open a pull request. Do not merge.

## Constraints

Everything here is fictional. New applications, vendors, and people are
invented in keeping with the existing demo cast and vendor set — never a real
organization's data, and never a real-looking detail borrowed from one.

---

*Last updated: 2026-08-04*
