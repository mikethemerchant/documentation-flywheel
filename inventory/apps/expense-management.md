<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Expense Management

Employee expense capture, receipt handling, and approval routing. Approved expenses are exported to the ERP for reimbursement through accounts payable.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Priya Raman |
| Technical owner | — |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Halcyon Cloud |
| Capability | Expense Management |
| Primary users | Finance / Enterprise |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 3 - Standard |
| RTO | 72 hours |
| RPO | 24 hours |
| Recovery owner | Tom Bergstrom |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Inbound | File Transfer (SFTP) | Direct (none) | Stoppable - manual reconciliation |

## Notes

Shares the Expense Management capability with the Travel & Expense product currently under evaluation. The capability map surfaces the pair; whether that is a duplication or a deliberate replacement has not been decided, and the evaluation started without the question being asked.

---

Source record: [`inventory/apps/data/expense-management.yaml`](data/expense-management.yaml)
