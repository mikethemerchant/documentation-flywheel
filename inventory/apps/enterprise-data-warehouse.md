<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Enterprise Data Warehouse (EDW)

Consolidates transactional data from the ERP and process data from the plant historian into a reporting model. Read-only downstream of everything; it writes to nothing operational.

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
| Capability | Data Warehousing |
| Primary users | Finance / Supply Chain / Manufacturing |
| Lifecycle | Active |
| Hosting | Cloud (Hosted) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 2 - Important |
| RTO | 24 hours |
| RPO | 24 hours |
| Recovery owner | Tom Bergstrom |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

| From | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Endpoint Management | Outbound | API (REST) | Direct (none) | Stoppable - no data loss |
| Enterprise Resource Planning (ERP) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |
| Plant Historian | Outbound | Database Link | Direct (none) | Stoppable - no data loss |

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Business Intelligence (BI) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |

## Notes

Every flow into and out of this system is stoppable with no data loss, because the sources remain authoritative and the loads are re-runnable. That property is why it sits at Tier 2 despite feeding every executive report in the business.
2026-08-04 (infrastructure catchup): a third inbound feed was recorded — endpoint asset and compliance data, pushed nightly by the endpoint management vendor. The `purpose` field above names only the ERP and the historian and is now incomplete; left as it stands rather than reworded here, because a purpose statement listing every source will go stale the same way. The integration records are the answer to what feeds it.

---

Source record: [`inventory/apps/data/enterprise-data-warehouse.yaml`](data/enterprise-data-warehouse.yaml)
