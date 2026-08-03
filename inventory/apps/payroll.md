<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Payroll

Payroll calculation, tax filing, and payment disbursement for salaried and hourly staff. Consumes employee and time data from the HCM; posts summary journals to finance by hand at period close.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Rachel Nkemdirim |
| Technical owner | — |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Beacon Payroll |
| Capability | Payroll |
| Primary users | Human Resources / Finance |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

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
| Human Capital Management (HCM) | Outbound | File Transfer (SFTP) | Direct (none) | Stoppable - no data loss |

### Flows out — this application is the source

_None._

## Notes

RTO is stated as 24 hours, but the real constraint is the pay calendar rather than the clock — an outage is survivable for days mid-period and unsurvivable for hours during a run. Tiering does not capture that shape, and a fixed RTO on a calendar-driven system is worth revisiting.
The journal post to finance is manual and has no integration record. That is accurate, not an omission: nothing automated connects them.

---

Source record: [`inventory/apps/data/payroll.yaml`](data/payroll.yaml)
