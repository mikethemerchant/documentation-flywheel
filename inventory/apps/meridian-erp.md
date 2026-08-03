<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Enterprise Resource Planning (ERP)

Core transactional system of record — order to cash, procure to pay, finance, and inventory. Every other business application either feeds it or reads from it.

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
| Capability | Financial Management / Order Management / Inventory Management / Procurement |
| Primary users | Finance / Supply Chain / Sales |
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

| From | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Customer Relationship Management (CRM) | Inbound | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays |
| EDI Gateway | Inbound | EDI | EDI Gateway | Cannot stop - data loss risk |
| Expense Management | Inbound | File Transfer (SFTP) | Direct (none) | Stoppable - manual reconciliation |
| Human Capital Management (HCM) | Inbound | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays |
| Legacy Order Entry | Inbound | Flat File (Manual) | Manual | **Unknown** |
| Warehouse Management (WMS) | Bidirectional | Message Queue | Direct (none) | Stoppable - manual reconciliation |

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Data Warehouse (EDW) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |
| Tax Engine | Bidirectional | API (SOAP) | Direct (none) | Cannot stop - data loss risk |

## Notes

The most connected record in the portfolio. See the DR posture view for what has to be stopped, drained, or accepted as lost during a failover.
2026-03-04 (integration review): the manual order-entry path from the retiring legacy system is still active and is not characterized — flagged in insights-surfaced.md.

---

Source record: [`inventory/apps/data/meridian-erp.yaml`](data/meridian-erp.yaml)
