<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Legacy Order Entry

In-house order capture application predating the current ERP. Retained for a handful of contract-pricing customers whose terms were never migrated. Scheduled for retirement with no date attached.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | **Unknown** |
| Technical owner | **Unknown** |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Internal |
| Capability | Order Management |
| Primary users | Sales |
| Lifecycle | Retiring |
| Hosting | On-Prem |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 3 - Standard |
| RTO | Best effort |
| RPO | Best effort |
| Recovery owner | **Unknown** |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Inbound | Flat File (Manual) | Manual | **Unknown** |

## Notes

Marked Retiring and still writing orders into the ERP through a manual flat file that nobody has characterized. Retiring is a status, not a state: the system is live, the flow is live, and the DR impact of that flow is Unknown.
The original developer has left and no source repository has been located. Retiring it needs the contract-pricing terms migrated first, which needs somebody to read them out of this system, which needs an owner — and that chain is why the date keeps moving.
This is the record to read first if you want to understand why the inventory exists. Flagged in insights-surfaced.md.

---

Source record: [`inventory/apps/data/legacy-order-entry.yaml`](data/legacy-order-entry.yaml)
