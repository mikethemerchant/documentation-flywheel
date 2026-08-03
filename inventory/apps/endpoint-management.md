<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Endpoint Management

Device enrolment, patching, software deployment, and remote support for laptops and warehouse handhelds. The service desk's primary working tool.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Alan Petrov |
| Technical owner | Tom Bergstrom |
| Manager | Tom Bergstrom |
| Accountable team | Infrastructure |

## Profile

| Field | Value |
|---|---|
| Vendor | Northgate IT |
| Capability | Endpoint Management |
| Primary users | IT |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 2 - Important |
| RTO | 24 hours |
| RPO | 8 hours |
| Recovery owner | Tom Bergstrom |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

_None._

## Notes

The person who uses it daily and the person who owns the platform are different people on purpose. Collapsing those into one field would lose the distinction between "who do I call about a policy" and "who do I call when the tenant is down".

---

Source record: [`inventory/apps/data/endpoint-management.yaml`](data/endpoint-management.yaml)
