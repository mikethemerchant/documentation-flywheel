<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Integration Platform (iPaaS)

Hosts the managed API integrations between cloud applications and the ERP. Owns retry, queueing, and replay for every flow that runs through it, which is what makes those flows stoppable during a core-system outage.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Sofia Marchetti |
| Technical owner | Sofia Marchetti |
| Manager | Marcus Iwu |
| Accountable team | Data & Integrations |

## Profile

| Field | Value |
|---|---|
| Vendor | Conduit |
| Capability | Integration & Middleware |
| Primary users | IT |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 1 - Critical |
| RTO | 4 hours |
| RPO | 1 hour |
| Recovery owner | Sofia Marchetti |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

_None._

## Notes

Appears as `middleware` on other integration records but has no integration records of its own, so the gap report lists it as unconnected. That is a true statement about the data and a false impression about the system — middleware is the path, not an endpoint. Worth a note in any walkthrough of the gap report, and an argument for modelling middleware as a first-class node one day.
Sole SME and sole technical owner are the same person, as on the EDI gateway. Flagged in insights-surfaced.md.

---

Source record: [`inventory/apps/data/integration-platform.yaml`](data/integration-platform.yaml)
