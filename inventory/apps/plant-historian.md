<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Plant Historian

Time-series capture of line and machine telemetry at the two manufacturing sites. Feeds throughput and downtime reporting into the data warehouse.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | **Unknown** |
| Technical owner | Tom Bergstrom |
| Manager | Tom Bergstrom |
| Accountable team | Infrastructure |

## Profile

| Field | Value |
|---|---|
| Vendor | Axiom Controls |
| Capability | Manufacturing Data Historian |
| Primary users | Manufacturing |
| Lifecycle | Active |
| Hosting | On-Prem |

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
| Enterprise Data Warehouse (EDW) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |

## Notes

Infrastructure keeps the server patched and backed up; nobody in IT can explain the tag configuration, the retention policy, or which of the downstream reports depend on which tags. The platform has an owner and the application does not, and the record shows both — which is the whole point of keeping those two fields apart.
2026-08-04 (infrastructure catchup): hosting resolved to On-Prem. It is a vendor appliance — a physical box in the plant electrical room, which Tom Bergstrom has stood next to. Closes Q-009.
The boundary dispute is unchanged and was never the same question. The field sat at TBD for five months because "where does it run" and "whose network is it on" had been collapsed into one unanswerable thing; the first took thirty seconds to answer once it was asked on its own. Whether the box sits inside the plant network boundary or the corporate one is still contested — Q-007, insight 7 — and that is what decides who patches it.

---

Source record: [`inventory/apps/data/plant-historian.yaml`](data/plant-historian.yaml)
