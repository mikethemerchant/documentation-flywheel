<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Travel & Expense (T&E)

Combined travel booking and expense capture, under evaluation as a possible replacement for the standalone expense tool. No production data and no integrations yet.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Marcus Iwu |
| Technical owner | — |
| Manager | Dana Whitfield |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Quill |
| Capability | Expense Management |
| Primary users | Finance / Enterprise |
| Lifecycle | Evaluating |
| Hosting | **TBD** |

## Recovery

| Field | Value |
|---|---|
| Criticality | — |
| RTO | — |
| RPO | — |
| Recovery owner | — |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

_None._

## Notes

Hosting is genuinely undecided rather than unrecorded — the vendor offers both a shared and a dedicated tenancy and the choice sits with the evaluation. TBD is the correct value here and should not be cleaned up.
No criticality tier or recovery target: an application in evaluation has not been through tiering, and inventing one would make the DR view claim more than anybody has actually decided.

---

Source record: [`inventory/apps/data/travel-and-expense.yaml`](data/travel-and-expense.yaml)
