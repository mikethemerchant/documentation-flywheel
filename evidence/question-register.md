# Question Register

The running list of what is not known and who can answer it.

This is the collector that drives the flywheel. Gaps arrive here from
`gap-analysis.py`, from the insight register, and from conversations that
raised more than they closed. **Every one gets a name against it**, and the
names are what produce the next interview list — see
[processes/documentation-flywheel.md](../processes/documentation-flywheel.md).

> All data in this repository is fictional. Northwind Traders does not exist.

**The rule:** a question with no name against it does not get asked. If nobody
can be identified, that is itself a finding — record the *role* that would
know, and the search for that person becomes the open item.

---

## Who to talk to next

Ordered by what each conversation unblocks, not by how many questions are
waiting. The last column is the one that matters: the process depends on
attaching questions to a meeting that is happening anyway.

| # | Person | Unblocks | Open | Next opportunity | Brief |
|---|---|---|---|---|---|
| 1 | Dana Whitfield | **Assigning the plant boundary call** — which unblocks Q-008; whether a tested recovery target is distinguishable from a contracted one; retirement authority; path-level tiering | 5 | Monthly one-to-one | [ready](interviews/dana-whitfield.md) |
| 2 | Sofia Marchetti | Whether SSO trusts belong in the model, what stopping each flow actually costs, iPaaS modelling, what else bypasses the platform | 6 | Integration standup, weekly | [ready](interviews/sofia-marchetti.md) |
| 3 | Marcus Iwu | Legacy retirement date, T&E hosting and overlap, whether two standalone apps are genuinely standalone | 4 | Portfolio review, monthly | [ready](interviews/marcus-iwu.md) |
| 4 | Ken Oyelaran | Plant boundary (his half of it), SSO→HCM failover behaviour | 3 | Access review, monthly | not prepped |
| 5 | Tom Bergstrom | Shared-tenancy risk, what else bypasses the integration platform | 3 | DR review, quarterly — next in September | [ready](interviews/tom-bergstrom.md) |
| 6 | Alan Petrov | Who in the business owns Electronic Signature; whether it is genuinely standalone | 2 | Service desk sync, weekly | not prepped |
| 7 | Priya Raman | Whether tiering should apply to paths; who produces the legacy order file | 2 | Month-end close debrief | not prepped |
| 8 | Rachel Nkemdirim | SSO→HCM provisioning behaviour (jointly with Ken) | 1 | Payroll cutover review | not prepped |

Briefs live in [evidence/interviews/](interviews/) and are prepped for the next
round only — see
[prompt-prepare-interview.md](../templates/prompt-prepare-interview.md).
Four of eight is the intended state, not an unfinished one: a brief for a
meeting with no date is a document nobody reads.

**Tom has dropped from first to fifth in one seven-minute conversation**, which
is the register behaving correctly. Three of his five questions closed; what is
left is not urgent enough to wait for a September DR review. Dana takes his
place because the boundary question stopped needing evidence and started
needing somebody to assign an afternoon.

**Not yet reachable** — see [people to identify](#people-to-identify) below.
Three open questions — Q-001, Q-004, and Q-006 — are blocked on finding a
person rather than on scheduling one, which is a different problem and the more
urgent of the two.

---

## Open questions

| Q | Question | Who can answer | Source | Raised | Status |
|---|---|---|---|---|---|
| Q-001 | Who in the business owns Electronic Signature? Nobody in IT can answer a question about it. | *Unidentified — Contracts* | `gap-analysis.py`, insight 1 | 2026-03-04 | **Blocked** — no person |
| Q-002 | Is Electronic Signature genuinely standalone, or connected by a path nobody has written down? | Alan Petrov | `gap-analysis.py` | 2026-03-04 | Open |
| Q-003 | Who is the SME for Legacy Order Entry now that it is retiring? | Marcus Iwu | `gap-analysis.py`, insight 1 | 2026-03-04 | Open |
| Q-004 | Who produces and loads the legacy order flat file, and what do they do when the ERP is down? | *Unidentified — Order Management* | `dr-posture.md`, insight 4 | 2026-03-04 | **Blocked** — no person |
| Q-005 | What is the retirement date for Legacy Order Entry, and who is authorized to set one? | Dana Whitfield, Marcus Iwu | insight 4 | 2026-03-04 | Open |
| Q-006 | Who moves the contract-pricing terms out of Legacy Order Entry, and what does it cost? It is the actual blocker on the retirement. | *Unidentified — Sales* | insight 4 | 2026-03-04 | **Blocked** — no person |
| Q-007 | Does the Plant Historian sit inside the plant network boundary or the corporate one? This decides who patches it. | Dana Whitfield — escalated 2026-08-04; positions held by Ken Oyelaran and Tom Bergstrom | insight 7 | 2026-03-04 | Open — **resolution path known**. Tom: inside the plant boundary, so plant. Ken: an IP on a corporate switch makes it Infrastructure. Tom, [2026-08-04](meetings/2026-08-04-infrastructure-catchup.md): "we're both partly right, which is the problem." Settling it means checking where the box physically terminates and someone making a call — an afternoon of work that nobody owns. No longer blocked on evidence; blocked on assignment |
| Q-008 | Who is the SME for the Plant Historian? | Blocked on Q-007 | `gap-analysis.py` | 2026-03-04 | **Blocked** — on Q-007 |
| Q-010 | What happens to SSO→HCM provisioning and deprovisioning during an outage — retried, replayed, or dropped? | Ken Oyelaran, Rachel Nkemdirim | `gap-analysis.py` | 2026-03-04 | Open |
| Q-011 | Should SSO trusts be integration records? Every SaaS app authenticates through the IdP and none of it is modelled. | Sofia Marchetti, Ken Oyelaran | insight 8 | 2026-03-04 | Open — needs a decision record |
| Q-012 | Is the Integration Platform correctly absent from the integration records, being a path rather than an endpoint? | Sofia Marchetti | `gap-analysis.py` | 2026-08-04 | Open — model question |
| Q-014 | Where will Travel & Expense run, and does it have planned integrations? | Marcus Iwu | `gap-analysis.py` | 2026-08-04 | Open |
| Q-015 | Was Travel & Expense evaluated against the expense management system already in production? | Marcus Iwu | insight 5, `capability-map.md` | 2026-03-04 | Open |
| Q-016 | Should criticality tiering apply to transaction paths rather than to applications? The tax engine is Tier 2 inside a Tier 1 path. | Dana Whitfield, Priya Raman | insight 6 | 2026-03-04 | Open — needs a decision record |
| Q-018 | Does the model need a way to express shared fate? ERP and WMS share a vendor tenancy; iPaaS and EDI share a vendor and an owner. | Tom Bergstrom, Sofia Marchetti | insight 9, `by-vendor.md` | 2026-03-04 | Open — model question. On Tom's brief 2026-08-04 and **not asked** |
| Q-019 | What does stopping each flow actually cost? `dr_impact` records whether a flow is stoppable, not what stopping it costs. | Sofia Marchetti | insight 10 | 2026-03-04 | Open — model question |
| Q-020 | What is the succession plan for the two systems where one person is sole SME, technical owner, and recovery owner? | Dana Whitfield | insight 2, `by-owner.md` | 2026-03-04 | Open |
| Q-021 | Is the carrier-rate tool the distribution centres use a separate application, a WMS module, or a vendor portal? Two or three tickets a month, routed to Priya, who resolves them and does not own it. | Alan Petrov, then Priya Raman | [2026-03-11 service desk sync](meetings/2026-03-11-service-desk-sync.md) | 2026-03-11 | Open — **not** in the inventory until it is known what it is |
| Q-022 | Is the "endpoint compliance dashboard" a separate application, a report in BI, or a vendor-side view? Named in passing as the consumer of the endpoint feed into the EDW. | Sofia Marchetti | [2026-08-04 infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md) | 2026-08-04 | Open — **not** in the inventory until it is known what it is, as Q-021 |
| Q-023 | Should the model distinguish a contractual recovery target from a tested one? Every `rto` and `rpo` in the inventory is a vendor or contract commitment, and none has been measured — but the records present both the same way. | Dana Whitfield, Tom Bergstrom | insight 13, [2026-08-04 infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md) | 2026-08-04 | Open — model question. Per `decision-rights.md`, RTO/RPO is Dana's approval |
| Q-024 | What other direct point-to-point flows bypass the integration platform and so never appear in the integration owner's view? Q-013 found one that had run for years unrecorded. | Sofia Marchetti, Tom Bergstrom | insight 11, [2026-08-04 infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md) | 2026-08-04 | Open |

---

## People to identify

Named in a conversation as "you'd have to ask…" and never resolved to an actual
person. **These are the most valuable rows in the file** — a question blocked
on scheduling gets asked eventually, and a question blocked on identifying
somebody sits here until someone goes looking.

A role here does **not** go in `inventory/schema.yaml`. The roster is the
controlled list of people who own records; this is a list of people to find.
They join the roster if and when they turn out to own something.

| Role described | Needed for | Who might know | Status |
|---|---|---|---|
| Whoever in Contracts administers Electronic Signature | Q-001, Q-002 | Alan Petrov — the ticket history will name them | **Asked 2026-03-11** — Alan agreed to pull the history; not done five months later |
| Whoever produces the legacy order flat file | Q-004 | Priya Raman, or the Order Management supervisor | Not started |
| A Sales contact who understands the legacy contract-pricing terms | Q-006 | Marcus Iwu | Not started |
| Plant controls engineer or plant manager | Q-007 | Tom Bergstrom | **On the brief 2026-08-04 and not asked.** Two rounds now: asked once in March with no name, briefed again in August and never raised. Less urgent than it was — Q-007 no longer needs a plant contact to answer it, it needs someone assigned to check where the box terminates — but a system neither side can name a contact for is its own finding |
| Meridian account manager | Q-018, shared-tenancy exposure | Marcus Iwu | Not started |

---

## Answered

Closed questions stay here with the conversation that closed them. Not deleted:
the point of a register is being able to show that a question was asked and
when, which is exactly what makes a two-year-old record still worth trusting.

| Q | Question | Answered by | Closed by | Result |
|---|---|---|---|---|
| Q-A01 | What actually happens to EDI documents arriving during an ERP outage? | Sofia Marchetti | [2026-03-04 integration review](meetings/2026-03-04-erp-integration-review.md) | Partners do not retry; documents are lost at the partner end. Recorded as `Cannot stop - data loss risk` on the EDI flow. |
| Q-A02 | Which application is the core transactional system of record? | — | 2026-03-18 | Not answered — *derived*. The renderer computes it from the integration records. See [DEC-007](../decisions/decision-log.md). |
| Q-A03 | Is the tax engine call synchronous inside order entry? | Priya Raman | [2026-03-04 integration review](meetings/2026-03-04-erp-integration-review.md) | Yes. Produced insight 6 and Q-016. |
| Q-009 | Where does the Plant Historian actually run? | Tom Bergstrom | [2026-08-04 infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md) | A vendor appliance — a physical box in the plant electrical room. `hosting` moved from TBD to On-Prem. It had been unanswered for five months because it was tangled with Q-007, which it turned out not to depend on. |
| Q-013 | Is Endpoint Management genuinely standalone? | Tom Bergstrom | [2026-08-04 infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md) | No. It pushes asset and compliance data into the EDW nightly over REST, direct, and has since implementation. Now recorded as an integration. Produced insight 11 and Q-024. |
| Q-017 | Have any of the recorded RTO and RPO values ever been tested end to end, or are they all contractual? | Tom Bergstrom | [2026-08-04 infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md) | None. One partial test on the pre-migration ERP, which he discounts because that system no longer exists. Every value came from a contract or a vendor commitment. **The numbers were deliberately left unchanged** — they are the commitment; what was missing was the fact that nobody has checked. Produced insight 13 and Q-023. |

---

## How rows get here

**From the machine:**

```bash
python automation/gap-analysis.py
```

Every gap it reports should have a row. If it does not, either add one or
record why the gap is acceptable.

**From a conversation.** While processing a transcript
([templates/prompt-process-transcript.md](../templates/prompt-process-transcript.md)),
anything the SME could not answer, deferred, or answered with "you'd have to
ask X" becomes a row. The open-questions section of a meeting summary and this
file should agree.

**From a person.** Anyone can add a row. The bar is a question and a name, not
a format.

## How rows reach a conversation

They do not, on their own. A register is a backlog, and a backlog that nobody
turns into a prepared question stays a backlog.

Each round, the rows for whoever has a meeting coming up are written into an
interview brief in [interviews/](interviews/) — the question as you would
actually say it out loud, what a good answer looks like, and what *not* to ask
because it is already recorded. That is the artifact somebody walks into a room
with. See
[prompt-prepare-interview.md](../templates/prompt-prepare-interview.md).

## How rows leave

1. A conversation answers it → move to **Answered**, link the summary that
   closed it, and update whatever record it was blocking.
2. It turns out to need a decision rather than an answer → write a decision
   record and close the row pointing at it.
3. It turns out to be a limitation of the model rather than missing data → it
   stays open and gets tagged *model question*. Three of these are open now, and
   collectively they are the strongest argument the schema has for changing.
4. It stops mattering → close it with a one-line reason. Do not delete it.

**Never close a row by filling the underlying field with a plausible guess.**
An unanswered question is a finding; a wrong record is a lie the pipeline
cannot catch. See [DEC-011](../decisions/decision-log.md).

---

*Last updated: 2026-08-04 — after the
[infrastructure catchup](meetings/2026-08-04-infrastructure-catchup.md)*
