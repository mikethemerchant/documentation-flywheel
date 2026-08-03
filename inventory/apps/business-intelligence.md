<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Business Intelligence (BI)

Dashboards and self-service reporting over the data warehouse. Operational reporting stays in the source systems; this is where cross-system questions get answered.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Sofia Marchetti |
| Technical owner | Tom Bergstrom |
| Manager | Marcus Iwu |
| Accountable team | Data & Integrations |

## Profile

| Field | Value |
|---|---|
| Vendor | Lumen Analytics |
| Capability | Analytics & Reporting |
| Primary users | Finance / Sales / Supply Chain / Enterprise |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 3 - Standard |
| RTO | 72 hours |
| RPO | 24 hours |
| Recovery owner | Tom Bergstrom |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

| From | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Data Warehouse (EDW) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |

### Flows out — this application is the source

_None._

## Notes

Tier 3 by recovery priority, but the first thing anyone notices is missing. That mismatch between criticality and visibility is normal and is exactly what the tier is for — restoring dashboards ahead of order entry would be the wrong call however loudly it is asked for.

---

Source record: [`inventory/apps/data/business-intelligence.yaml`](data/business-intelligence.yaml)
