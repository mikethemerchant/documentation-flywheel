# People

Who is who, what they own, and how they think about it.

The last column is the useful one. Knowing that Priya answers in transaction
paths and Tom answers in recovery windows tells you which of them to ask a
question to — and tells an AI assistant drafting a summary whose framing to
expect in a transcript.

> Every person in this repository is fictional. These names exist to make the
> demonstration dataset coherent, and nothing more.

The names below are the same controlled roster enforced by
[inventory/schema.yaml](../inventory/schema.yaml). An owner field cannot hold a
name that is not on this list — that is the mechanism, described in
[DEC-004](../decisions/decision-log.md).

---

## The roster

| Name | Role | Team | Appears in the inventory as |
|---|---|---|---|
| Dana Whitfield | IT Director | — | Approver on decisions and process changes |
| Marcus Iwu | Applications Manager | Applications | `it_manager` on business applications |
| Priya Raman | ERP Analyst | Applications | `it_sme` on ERP, WMS, finance systems |
| Sofia Marchetti | Data & Integrations Lead | Data & Integrations | `it_sme` on iPaaS, EDI, EDW, BI |
| Tom Bergstrom | Infrastructure Lead | Infrastructure | `it_technical_owner` and `recovery_owner` on most of the portfolio |
| Ken Oyelaran | Security Lead | Security | Owner of identity and endpoint security |
| Rachel Nkemdirim | HR Systems Analyst | Applications | `it_sme` on HCM and payroll |
| Alan Petrov | Service Desk Lead | Service Desk | Owner of service-management tooling |

---

## How each of them thinks

### Dana Whitfield — IT Director

Decides. Approves architecture decisions, process changes, and anything with a
contract attached.

Thinks in **exposure and defensibility**: what would be hard to explain to the
CFO or an auditor after the fact. Will approve an imperfect thing that is
written down over a better thing that lives in someone's head, and says so
often enough that it has become the team's shorthand. Pushes back hardest on
proposals that add a step someone has to remember — the standard question is
*"what happens when whoever does this is on holiday?"*

Reads the insight register before the inventory.

### Marcus Iwu — Applications Manager

Owns the business application portfolio and the relationships with the people
who use it.

Thinks in **who is accountable**. Where others describe a system, Marcus
describes the person who will be called when it breaks, and gets visibly
uncomfortable when that answer is a team name. Was the origin of the
person-not-team rule. Tends to know the commercial history of a record — what
it cost, who championed it, which director will defend it — which makes him the
right person to ask why something nobody uses is still live.

Wary of consolidation proposals that underestimate how much a small user group
will fight for its tool.

### Priya Raman — ERP Analyst

The deepest single well of knowledge in the portfolio, and the largest single
point of failure in it.

Thinks in **transaction paths**, not applications. Asked about the tax engine,
she answers about order entry, because the tax engine is a step inside it.
This is why she surfaced the tiering problem that nobody else saw: she does not
naturally think of a system as a thing that can be tiered on its own. Precise
about sequence and timing, impatient with diagrams that show a line between two
boxes without saying what travels along it or when.

If a record needs to know what actually happens at period close, she is the
answer.

### Sofia Marchetti — Data & Integrations Lead

Everything commercial that arrives from outside passes through systems she owns
alone.

Thinks in **flows, failure modes, and replay**. Instinctively asks what happens
to in-flight data, which is why the `dr_impact` field exists and why the
failover behaviour notes are as specific as they are. Also the person most
likely to say "that isn't modelled" — the observation that SSO trusts are
missing from the integration records is hers.

Skeptical of anything that adds a hop without an owner. Built and maintains the
render pipeline, and treats a pipeline that commits a file nobody edited as a
defect rather than noise.

### Tom Bergstrom — Infrastructure Lead

Named as recovery owner on nearly everything, which is itself a finding.

Thinks in **recovery windows and blast radius**. Converts every question into
"how long until it's back and what else goes with it". Was the one who noticed
the ERP and WMS share a vendor tenancy and are treated as independent in the DR
plan. Holds the contractual RTOs and is careful to distinguish a number in an
agreement from a number that has been tested — will correct that distinction
every time it is blurred.

Dry about it. The correction usually arrives as a question.

### Ken Oyelaran — Security Lead

A team of one, which shapes everything about how he works.

Thinks in **trust relationships and standing access**. Sees the portfolio as a
graph of who can get into what, and finds the application-centric view slightly
beside the point — from where he sits, the identity provider is not one
application among seventeen, it is the thing all seventeen depend on. Triages
ruthlessly because he has to, and is explicit that anything not on this
quarter's list is not being worked on.

The plant boundary question is his open dispute and he will raise it unprompted.

### Rachel Nkemdirim — HR Systems Analyst

Owns HCM and payroll, the two systems with the least tolerance for being late.

Thinks in **calendars and cutoffs**. Everything is positioned relative to a pay
run: what has to be true by Wednesday, what can be fixed after. Brings the
sharpest instinct in the group for data quality, because a bad record in her
world becomes someone's incorrect pay rather than a dashboard that looks odd.

Cautious about integration changes, and asks for a dry run more often than
anyone else. This has never once been the wrong call.

### Alan Petrov — Service Desk Lead

Sees the portfolio through tickets, which means he sees the parts of it nobody
else does.

Thinks in **what people actually contact us about**. The first to know when an
application exists that is not on the list, because a user eventually files a
ticket about it. Good source for the difference between what a system is for
and what it is used for. Practical and unsentimental — measures a system by how
often it generates work.

Asks the question that most often produces an insight register row: *"who do I
route this to?"*

---

## Using this file

When drafting from a transcript, use this to tell restatement from new
information: if Tom says something is Tier 1 and back in four hours, that is
him repeating a known contractual position, not new evidence. If Tom says he
has *tested* it, that is new.

When a name needs to be added to the roster, it goes in
[schema.yaml](../inventory/schema.yaml) in the same pull request — the friction
is intentional and is described in [DEC-003](../decisions/decision-log.md).

**This roster is not everyone who matters.** It is everyone who owns a record.
People named in conversations as "you'd have to ask whoever does that" — and
never resolved to an actual person — live in the people-to-identify table in
[question-register.md](../evidence/question-register.md), and they do not
belong in `schema.yaml` until they turn out to own something. There are five of
them right now, and they are blocking more than the scheduling backlog is.

---

*Last updated: 2026-08-04*
