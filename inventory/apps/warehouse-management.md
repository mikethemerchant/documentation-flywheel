<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Warehouse Management (WMS)

Receiving, put-away, picking, and shipping across the three distribution centres. Holds the authoritative bin-level stock position; the ERP holds the financial one, and the two reconcile continuously.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Priya Raman |
| Technical owner | Tom Bergstrom |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Meridian Systems |
| Capability | Warehouse Operations / Inventory Management |
| Primary users | Supply Chain |
| Lifecycle | Active |
| Hosting | Cloud (Hosted) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 1 - Critical |
| RTO | 4 hours |
| RPO | 15 minutes |
| Recovery owner | Tom Bergstrom |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Bidirectional | Message Queue | Direct (none) | Stoppable - manual reconciliation |

## Notes

Same vendor and same hosting tenancy as the ERP, which means a vendor-side outage takes both out together. That correlation is not visible anywhere in the DR plan and is worth a decision record.

---

Source record: [`inventory/apps/data/warehouse-management.yaml`](data/warehouse-management.yaml)
