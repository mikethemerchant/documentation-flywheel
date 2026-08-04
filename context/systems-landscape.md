# Systems Landscape

The shape of the portfolio in prose — what the systems are for, how they came
to be here, and where the structural risk sits.

**This file carries no data.** Every fact about a specific application lives in
[inventory/apps/data/](../inventory/apps/data/) and is rendered into
[all-applications.md](../inventory/rendered/all-applications.md) and the other
views. Nothing here restates a field value, because a restated field value is a
second copy that will eventually be wrong. What is here is the narrative the
records cannot hold: history, intent, and the reasons the graph looks the way
it does.

> All applications, vendors, and integrations below are fictional.

---

## The centre

The **ERP** is the transactional system of record — order to cash, procure to
pay, finance, inventory. Every other business system either feeds it or reads
from it, which the integration records show without anyone asserting it: the
[DR posture view](../inventory/rendered/dr-posture.md) derives the core system
by counting what writes into what, rather than reading it from a config value
([DEC-007](../decisions/decision-log.md)).

It moved to vendor hosting two years ago. That migration is the reason recovery
targets across the portfolio are contractual rather than operational — the
numbers came out of an agreement, and nothing has been tested against them
since.

Around it sit two chains that behave very differently under failure:

- **The finance chain** — ERP, tax engine, expense export. The tax engine is
  called *synchronously* during order entry and invoicing, so it cannot be
  stopped without stopping order entry. It is tiered Important while sitting
  inside a Critical path, which is the clearest example in the dataset of a
  model that classifies applications when the thing that matters is the path.
- **The warehouse chain** — ERP and WMS over a durable queue. Stoppable, but
  only in the sense that the warehouse keeps working on what it already holds
  and the two stock positions diverge until someone reconciles them by hand.

---

## The two doors

Everything commercial that arrives from outside comes through one of two
systems, and both are owned by one person.

| Path | Carries | Owner |
|---|---|---|
| **EDI gateway** | ~40% of order volume, from contractor and builder trading partners | Sofia Marchetti |
| **Integration platform (iPaaS)** | Everything API-based between internal systems | Sofia Marchetti |

Both come from the same vendor. Both are Tier 1. Both name the same individual
as SME, technical owner, and recovery owner. Nothing about that arrangement is
recorded as a risk anywhere in the portfolio data — it only becomes visible
when the records are grouped by owner, which is precisely the argument for
generating [by-owner.md](../inventory/rendered/by-owner.md) rather than
maintaining an owner list by hand.

The EDI path has the harshest failure mode in the estate: trading partners
transmit on their own schedule and do not retry a rejected connection, so
documents arriving during an outage are lost at the partner end. It is the one
flow in the inventory marked *cannot stop — data loss risk* that is genuinely
outside Northwind's control.

**The iPaaS is not an endpoint.** It shows up in the gap report as an
application with zero integration records, which is true of the data and
misleading about the system — it is the path, not a destination. That is worth
pointing at rather than tidying away.

---

## Vendor concentration

Ten vendors for seventeen applications, and the overlaps are not evenly spread.

| Vendor | Supplies | Why it matters |
|---|---|---|
| **Meridian Systems** | ERP and WMS | Two Tier 1 systems, one vendor, one hosting tenancy. A vendor-side outage takes both. The DR plan treats them as independent. |
| **Conduit** | iPaaS and EDI gateway | Both integration paths, one vendor, one owner. |
| **Halcyon Cloud** | CRM, HCM, expense management | Three systems across three business functions; the largest SaaS relationship by user count. |
| **Lumen Analytics** | EDW and BI | The reporting stack, end to end. |
| **Northgate IT** | Identity provider and endpoint management | Includes the identity provider, which everything else authenticates through. |
| **Quill** | Electronic signature and the T&E system under evaluation | Both arrived from outside the normal approval path. |

The Meridian and Conduit rows are the same failure shape at different layers,
and neither is expressible in the current record model — there is no field for
"these two share a fate". They are visible only through
[by-vendor.md](../inventory/rendered/by-vendor.md).

---

## The reporting stack

EDW pulls nightly from the ERP against a read replica, the plant historian
pushes aggregated tag data into the same warehouse, and BI reads live from it.
Nothing in this chain writes back, so the whole thing is stoppable with no data
loss — the only part of the landscape where that is cleanly true.

The plant historian is the odd member. It is the one system with a foot in the
operational-technology world, and whether it sits inside the plant network
boundary or the corporate one has never been settled. That question decides who
patches it, and both teams currently believe it is the other's. It is also
carrying `hosting: TBD` and no SME, which is less an oversight than a symptom:
an unowned boundary produces an unowned system.

---

## Identity

Every SaaS application authenticates through the identity provider. **None of
those dependencies exist as integration records**, because authentication was
never treated as an integration — the model started from data flows, and a
trust relationship does not move data in the sense the model had in mind.

The consequence is that the landscape diagram understates the identity
provider's blast radius severely. On the picture it has one connection. In
reality, if it is down, most of the portfolio is unreachable regardless of
whether those systems are themselves healthy.

Whether an SSO trust belongs in the integration model is an open question, not
a settled one. It is the clearest live example of the model shaping what can be
seen: nothing is missing from the data, and something important is missing from
the picture.

---

## The edges

**Legacy order entry** is the headline case, and worth understanding as a
pattern rather than a record. It is marked Retiring, has no owner, and still
writes orders into the ERP through a flat file produced and loaded by hand
whose failure behaviour has never been characterized. The blocker is that
contract-pricing terms for a handful of long-standing customers exist only
inside the system being retired, and nobody has costed moving them. It has been
Retiring for longer than anyone volunteers.

A spreadsheet inventory would show this as `Retiring` and stop. It takes the
integration records to show that a retiring system with no owner is still on a
live path into the core.

**Expense capture is covered twice.** An expense management system is in
production, and a T&E product from a different vendor is under evaluation for
overlapping ground. The evaluation started without anyone asking whether the
first already did the job — which is the question the
[capability map](../inventory/rendered/capability-map.md) exists to force, and
the reason `capability` is a controlled field rather than free text.

**Electronic signature** is used across three business functions, was bought on
a departmental card, and has no SME. Nobody in IT can answer a question about
it. It is in the inventory because a user filed a ticket about it.

---

## What this landscape is not

The portfolio is deliberately small — around seventeen applications — so the
generated diagrams stay legible and the whole thing can be read in one sitting.
A real mid-market estate is several hundred records. The structural problems do
not change with scale; they get harder to see, which is the argument for
generating the views rather than drawing them.

---

*Last updated: 2026-08-04*
