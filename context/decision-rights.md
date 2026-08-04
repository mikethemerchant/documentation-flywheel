# Decision Rights

Who is allowed to approve what. This is a map of **authority**, not a procedure
— the step-by-step for a given change belongs in
[processes/](../processes/), and the rules a change has to satisfy belong in
[standards/](../standards/).

It is here in `context/` because it is a fact about the world rather than an
instruction: an assistant drafting a change needs to know who signs it, and a
new starter needs to know who to ask before they need to know the form.

> Fictional, like everything else here.

---

## Approval matrix

| Decision | Approver | Consulted | Recorded as |
|---|---|---|---|
| New application entering the portfolio | Dana Whitfield | Marcus Iwu, Ken Oyelaran | Inventory record + decision record if it displaces something |
| Retiring an application | Dana Whitfield | Application SME, Marcus Iwu | `lifecycle_status` change + decision record |
| Architecture or integration pattern change | Dana Whitfield | Sofia Marchetti | Decision record |
| New or changed integration | Marcus Iwu | Sofia Marchetti | Integration record |
| Change to a Tier 1 system | Dana Whitfield | SME + Tom Bergstrom | Change record |
| Change to a Tier 2 or 3 system | Marcus Iwu | SME | Change record |
| Emergency change | Any two of Dana / Marcus / Tom | — | Retrospective change record within two business days |
| Access model or identity change | Ken Oyelaran | Dana Whitfield | Decision record if it changes the trust model |
| Recovery tier, RTO, or RPO | Dana Whitfield | Tom Bergstrom | Field change on the application record |
| Adding a controlled value to the schema | Marcus Iwu | — | Pull request touching `schema.yaml` |
| Documentation, process, or standard change | Dana Whitfield | Author's team lead | Pull request |
| Anything during the freeze window | Dana Whitfield only | Tom Bergstrom | Change record + explicit freeze exception |

---

## The freeze

Order volume roughly doubles between April and September, so **nothing touching
an order path changes between mid-March and early October** without a named
exception approved by the IT Director.

Three consequences worth knowing before proposing anything:

- The practical change window is five months, and it is crowded.
- Work that misses it slips a full year, not a quarter. This is why several
  records carry an intent with no date attached.
- Documentation changes are **not** frozen. Nothing in this repository moves
  production, so the flywheel keeps turning through the freeze — which is when
  the interviews are easiest to schedule anyway.

---

## Spend

| Amount | Approver |
|---|---|
| Under $5,000/yr | Team lead |
| $5,000 – $25,000/yr | Dana Whitfield |
| Over $25,000/yr | Dana Whitfield + CFO |
| Anything with a data-processing agreement | Dana Whitfield + Ken Oyelaran, regardless of amount |

---

## In this repository

Documentation authority mirrors the operating model, one level lighter.

| Change | Needs |
|---|---|
| Inventory record, integration record, insight row | One reviewer, plus the record's SME if a fact about their system changes |
| New controlled value in `schema.yaml` | Marcus Iwu — this is the roster gate and it is deliberately narrow |
| New or amended process, standard, or decision record | Dana Whitfield |
| Generated output | **Nobody.** It is written by the pipeline; a human editing it is a defect, not an approval question. |

Full mechanics in
[standards/pull-request-policy.md](../standards/pull-request-policy.md).

---

## Where this model leaks

Recorded because an approval matrix that only describes its intended paths is
describing fiction.

| Leak | Effect | Status |
|---|---|---|
| **Departmental purchasing is outside the matrix.** Software bought on a business card under the team-lead threshold reaches production without touching IT, security, or the inventory. | Electronic signature entered the portfolio this way, is now used across three business functions, and has no SME. It was catalogued only because a user filed a ticket. | Open — insight 1 |
| **Nobody owns retirement dates.** The matrix says who approves a retirement. It does not say who is responsible for proposing one, so nothing reaches the approver. | Legacy order entry has been Retiring long enough that the date is no longer discussed. | Open — insight 4 |
| **Contested plant boundary.** Whether plant-floor systems fall under Infrastructure or the plant means the approver for a change to the historian is genuinely undetermined. | Both teams believe patching is the other's. The record carries no SME and no hosting value. | Open — insight 7 |
| **Evaluations begin below the threshold.** A product evaluation costs nothing, so it starts without approval — and by the time it needs a signature it has a business sponsor and momentum. | The T&E evaluation started without anyone asking whether expense management already covered it. | Open — insight 5 |
| **Tiering approval is per application.** Nothing in the matrix approves the criticality of a *path*, so a Tier 2 system sits synchronously inside a Tier 1 transaction with every individual approval correctly given. | Tax engine inside order entry. | Open — insight 6 |

Every row above came out of a documentation interview rather than an audit.
That is the argument for the flywheel in one table: none of these are secrets,
and none of them were visible until somebody wrote the ordinary facts down in a
structured way.

Full register: [insights-surfaced.md](../inventory/insights-surfaced.md). What
is still open, and who could close it:
[question-register.md](../evidence/question-register.md).

**Three of the leaks above are blocked on a person, not a decision.** Nobody
knows who in Contracts administers electronic signature, who produces the
legacy order file, or who in Sales understands the contract-pricing terms that
are holding up a retirement. An approval matrix cannot help with any of that —
which is why the register tracks people to identify separately from questions
to ask.

---

*Last updated: 2026-08-04*
