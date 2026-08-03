<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Customer Relationship Management (CRM)

Accounts, contacts, opportunities, and quoting for the outside sales team. Quotes accepted here become sales orders in the ERP.

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
| Vendor | Halcyon Cloud |
| Capability | Sales & Customer Management |
| Primary users | Sales |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 2 - Important |
| RTO | 24 hours |
| RPO | 4 hours |
| Recovery owner | Tom Bergstrom |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Inbound | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays |

## Notes

No technical owner recorded, and correctly so — pure SaaS with no infrastructure to own. The optional field is left off rather than filled with a placeholder, because a blank reads as "not applicable" and a placeholder reads as "answered".

---

Source record: [`inventory/apps/data/customer-relationship-mgmt.yaml`](data/customer-relationship-mgmt.yaml)
