# Organizational Context

The world this documentation operates in. Read this before proposing a change
to a process, a standard, or the inventory model — most of the design choices
in this repository only make sense against these constraints.

> All data in this repository is fictional. Northwind Traders does not exist.

---

## The company

Northwind Traders is a mid-market distributor of building products — lumber,
millwork, roofing, and fasteners — with a single millwork plant that does light
manufacturing to order.

| | |
|---|---|
| Employees | ~1,200 |
| Sites | Head office, three distribution centres, one millwork plant |
| Revenue | ~$450M |
| Customers | Contractors and regional builders; ~40% of order volume arrives by EDI |
| Seasonality | Order volume roughly doubles between April and September |

The seasonality matters more than the size does. Anything that changes an order
path is frozen from mid-March to early October, which compresses every
significant system change into a five-month window and is the reason several
records in the inventory carry a retirement intent and no date.

---

## The IT function

Fourteen people, no dedicated enterprise architect, no one whose full-time job
is documentation.

| Team | Headcount | Owns |
|---|---|---|
| Applications | 5 | ERP, WMS, CRM, HCM, payroll, finance systems |
| Data & Integrations | 3 | Integration platform, EDI gateway, warehouse, reporting |
| Infrastructure | 3 | Hosting, network, endpoints, plant-adjacent systems |
| Security | 1 | Identity, access, endpoint security |
| Service Desk | 2 | Support tooling, tier 1 |

The shape of that table explains most of the risk in the portfolio. Teams of
three and one produce single points of failure by arithmetic, not by neglect —
see rows 2 and 3 of [insights-surfaced.md](../inventory/insights-surfaced.md).

---

## Constraints

These are fixed. A proposal that requires one of them to change is a proposal to
do something else.

| Constraint | Consequence |
|---|---|
| **No budget for an EA or CMDB tool** | The documentation system has to be built from things already paid for. Git, text files, and CI. |
| **No full-time documentation owner** | Anything that requires a person to remember to update it will not be updated. This is the load-bearing constraint. |
| **Change freeze, mid-March to early October** | Roughly half the year is unavailable for anything touching order flow. |
| **Vendor-hosted ERP** | The ERP's recovery position is contractual, not operational. Northwind does not control its RTO; it holds a number in an agreement. |
| **One security person** | Access reviews, patch policy, and identity all queue behind the same individual. |
| **Small enough to be informal** | Everyone can still ask everyone. That is why undocumented knowledge survives here without visibly hurting — until someone leaves. |

---

## Assumptions

Stated so they can be argued with rather than inherited silently.

- **The application is the right unit of record.** Not the server, not the
  business process. Servers churn and processes cross too many systems to be a
  useful primary key.
- **The inventory is a decision-support tool, not an audit artifact.** It exists
  to answer "who do I call", "what breaks if this stops", and "do we already own
  something that does this". It is not trying to be complete for its own sake.
- **A recorded gap is worth more than a filled field.** `Unknown` in an owner
  field is a finding. A team name in the same field is a finding that has been
  hidden. See [DEC-004](../decisions/decision-log.md).
- **Nobody will maintain a second copy.** Every view has to be generated from
  the records, or it will disagree with them within a quarter.
- **The people who know are busy.** Any process that creates homework for an SME
  will stall. The flywheel is designed around this — see
  [processes/documentation-flywheel.md](../processes/documentation-flywheel.md).

---

## Non-goals

What this system deliberately does not try to do. These are settled; reopening
one needs a decision record, not a pull request.

| Not doing | Why |
|---|---|
| Infrastructure-level modelling | Servers, VLANs, and storage are below the altitude this answers questions at. The infrastructure team tracks those elsewhere. |
| Cost and licence tracking | Finance owns spend. Duplicating it here creates a second number that will be wrong. |
| Lifecycle workflow and approvals in-tool | Approvals happen in the change process and in pull requests. A workflow engine is a product, and this is a repository. |
| Business process modelling | The inventory records what systems exist and how they connect, not how work flows through them. |
| Being the system of record for identity or access | The identity provider is that. This records that the dependency exists. |
| Completeness for its own sake | ~17 applications is the portfolio that matters. Cataloguing every browser plugin would bury the signal. |

---

## Known gaps in this picture

The context above is itself incomplete, and these are the parts known to be
missing. This section is about the *operating model*; gaps the documentation
surfaced in the **portfolio** live in
[insights-surfaced.md](../inventory/insights-surfaced.md).

| Gap | Status |
|---|---|
| **No agreed boundary for plant systems.** Whether the millwork plant's systems sit inside the corporate perimeter or the plant one has never been decided, so patching accountability for the historian is contested. | Open — insight 7 |
| **Departmental purchasing is not in the approval path.** Software bought on a business card arrives in production without touching IT. At least one application in the inventory got in this way. | Open — insight 1; see [decision-rights.md](decision-rights.md) |
| **No retirement authority.** Nothing in the process says who is allowed to set a retirement date, so nothing gets one. | Open — insight 4 |
| **Recovery targets are aspirational.** RTO and RPO values are recorded and have never been tested end to end. They are intentions, and should be read that way. | Open |
| **Tiering is per application, not per path.** A Tier 2 system sits synchronously inside a Tier 1 transaction. The model cannot currently express that. | Open — insight 6 |

---

*Last updated: 2026-08-04*
