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
| Hosting | **TBD** |

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
Hosting is TBD because it is contested rather than unknown: it was commissioned by the controls integrator and it is not settled whether the box sits inside the plant network boundary or the corporate one. That answer changes who is accountable for patching it.

---

Source record: [`inventory/apps/data/plant-historian.yaml`](data/plant-historian.yaml)
