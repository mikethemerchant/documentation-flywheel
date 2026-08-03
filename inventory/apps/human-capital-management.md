<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Human Capital Management (HCM)

System of record for people — hires, transfers, terminations, org structure, and benefits enrolment. Employee identity originates here and propagates to payroll, the ERP, and the identity provider.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Rachel Nkemdirim |
| Technical owner | Ken Oyelaran |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Halcyon Cloud |
| Capability | Human Resources Management |
| Primary users | Human Resources / Enterprise |
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

| From | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Identity Provider (SSO) | Outbound | API (REST) | Direct (none) | **Unknown** |

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Inbound | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays |
| Payroll | Outbound | File Transfer (SFTP) | Direct (none) | Stoppable - no data loss |

## Notes

Termination events here drive access revocation downstream, which is why the security lead holds the technical ownership rather than the applications team. A delay in this feed is a security finding, not a data-quality one.

---

Source record: [`inventory/apps/data/human-capital-management.yaml`](data/human-capital-management.yaml)
