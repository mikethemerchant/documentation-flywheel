<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Identity Provider (SSO)

Single sign-on, multi-factor authentication, and lifecycle provisioning for every cloud application in the portfolio. Nothing else in the estate is a dependency of this many systems.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Ken Oyelaran |
| Technical owner | Ken Oyelaran |
| Manager | Dana Whitfield |
| Accountable team | Security |

## Profile

| Field | Value |
|---|---|
| Vendor | Northgate IT |
| Capability | Identity & Access Management |
| Primary users | IT / Enterprise |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 1 - Critical |
| RTO | 1 hour |
| RPO | 15 minutes |
| Recovery owner | Ken Oyelaran |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Human Capital Management (HCM) | Outbound | API (REST) | Direct (none) | **Unknown** |

## Notes

Only one integration is recorded — the provisioning feed to the HCM — but authentication dependencies run to almost every SaaS application here. Those are real couplings and they are not in the graph, because authentication was not treated as an integration when the records were written.
Whether an SSO trust belongs in the integration model is an open question and a good candidate for a decision record. Until it is decided, the landscape diagram understates this application's blast radius.

---

Source record: [`inventory/apps/data/identity-provider.yaml`](data/identity-provider.yaml)
