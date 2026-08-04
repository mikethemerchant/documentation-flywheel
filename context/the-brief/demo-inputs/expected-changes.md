# Demo Inputs — and what each one should produce

Three unprocessed Teams transcripts, staged for the live segment of the
recording. **None of them has a summary, and none has been processed** — that
is the point. They are the only transcripts in the repository in that state.

> They live here rather than in `evidence/meetings/` on purpose. The repo's own
> rule is that a transcript without a summary has not been processed, so an
> unprocessed one sitting in `evidence/` would contradict it. **Copy the one you
> are using into `evidence/meetings/` on camera** — "here's what came off Teams
> this morning" — and process it from there.

This file is your answer key. Read it before recording so you can narrate
confidently and spot it if the assistant gets something wrong on camera.

> All three are fictional, consistent with the existing dataset and the briefs
> in `evidence/interviews/`.

---

## Which one to use

| File | Length | Best for | Diagram changes? |
|---|---|---|---|
| **[`2026-08-04-infrastructure-catchup.vtt`](2026-08-04-infrastructure-catchup.vtt)** | 50 cues, 7 min | **The flagship.** Produces a new integration record, so the landscape diagram visibly redraws. | **Yes** |
| [`2026-08-04-access-review.vtt`](2026-08-04-access-review.vtt) | 35 cues, 5 min | A field change with real teeth — a security finding hiding in a low-stakes-looking flow. | No |
| [`2026-08-04-legacy-order-entry-followup.vtt`](2026-08-04-legacy-order-entry-followup.vtt) | 31 cues, 4 min | **The gate.** Names a person who isn't on the roster, so `schema.yaml` must change in the same PR. | No |

**If you record one, record the infrastructure catch-up.** It is the only one
that redraws a picture, and a diagram changing on its own is the single most
convincing thing in the demo.

All three are dated 2026-08-04 — the same day the briefs in
`evidence/interviews/` were prepared. That is deliberate and worth saying on
camera: **prep, approve, talk, process, all in one day.** The infrastructure
catch-up even opens with Marcus saying he isn't waiting until September, which
is exactly what Tom's brief told him to do.

---

## A · `2026-08-04-infrastructure-catchup.vtt`

**Marcus Iwu + Tom Bergstrom, 7 minutes.** Marcus pulls Tom aside rather than
waiting for the September DR review, taking three questions off
[`evidence/interviews/tom-bergstrom.md`](../../../evidence/interviews/tom-bergstrom.md).

### Expected changes

**1. A new integration record** — the headline.

`inventory/integrations/data/endpoint-management--enterprise-data-warehouse.yaml`

```yaml
name: Endpoint Management → Enterprise Data Warehouse (EDW)
source: endpoint-management
target: enterprise-data-warehouse
direction: Outbound
connection_type: API (REST)
middleware: Direct (none)

dr_impact: Stoppable - no data loss
failover_behavior: >
  Nightly push of device inventory, patch state, and encryption status. The
  endpoint tool is the system of record for its own data and sends full state
  each run, so a missed night leaves a stale compliance dashboard and nothing
  else.
```

**2. `inventory/apps/data/plant-historian.yaml`** — `hosting: TBD` → `hosting: On-Prem`
(a vendor appliance in the plant electrical room). Tom is certain about the box
and still not certain whose it is, so **the SME stays `Unknown`.**

**3. An insight row** — the RTO/RPO values are contractual commitments, never
tested. Tom's line is the one to quote: *"It worries me more that they're
written down in a way that looks like they've been proven."*

**4. Register updates** — Q-013 and Q-009 close; Q-017 closes as a finding
rather than a data change; Q-007 stays open with better detail on what would
settle it.

### What you should see on screen

| Before | After |
|---|---|
| `12 open gap(s)` | **`10 open gap(s)`** |
| Applications with no integration records: **4** | **3** — Endpoint Management drops off |
| Hosting not yet determined: **2** | **1** — Plant Historian drops off |
| Endpoint Management floating unconnected on the landscape diagram | **Connected to the EDW** — the diagram redraws |

```bash
python automation/gap-analysis.py          # before: 12
# ...process the transcript...
python automation/render-inventory.py      # regenerates views + the .d2
python automation/render-diagrams.py       # redraws the SVG
python automation/gap-analysis.py          # after: 10
```

**Do not change the RTO numbers.** Tom explicitly says not to — *"the numbers
are what we're owed, just say nobody's checked."* If the assistant edits an
`rto` field, that is a miss worth catching on camera.

---

## B · `2026-08-04-access-review.vtt`

**Marcus Iwu + Ken Oyelaran, 5 minutes.** The SSO→HCM failover question, plus
the plant boundary from the other side of the dispute.

### Expected changes

**1. `inventory/integrations/data/identity-provider--human-capital-management.yaml`**

`dr_impact: Unknown` → **`Cannot stop - data loss risk`**, with
`failover_behavior` rewritten: deprovisioning events fire once, are not queued
and are not retried, so an offboarding during an HCM outage leaves an account
enabled downstream with nothing to signal it. Detected at the quarterly access
review — *"somewhere between one day and three months later."*

**2. An insight row** — a flow that reads as low-stakes carries a standing
access exposure. The classification hid it: `Unknown` looked like an
unimportant gap rather than an uninvestigated one.

**3. Register** — Q-010 closes. Q-007 gains Ken's position and, more usefully,
the fact that both leads agree on the *question* and not the answer. Q-011
(SSO trusts in the model) is raised again and stays open — Ken asks for it on
the record specifically because it keeps getting deferred.

### What you should see on screen

| Before | After |
|---|---|
| `12 open gap(s)` | **`11 open gap(s)`** |
| Integrations with unknown DR impact: **2** | **1** |
| `dr-posture.md` → "Unknown — not characterized" holds 2 flows | **1** |

No diagram change — the integration already existed; only its fields moved.

**The good beat here:** the answer makes the estate look *worse*, not better.
That is what an honest documentation pass does, and it is worth pointing out.

---

## C · `2026-08-04-legacy-order-entry-followup.vtt`

**Marcus Iwu + Priya Raman, 4 minutes.** Priya has asked around and found the
person who produces the legacy order file.

### Expected changes

**1. `inventory/schema.yaml`** — `Dermot Walsh` added to the `it_sme` values.
**This is the demo.** The assistant cannot add him to a record without adding
him to the controlled list in the same change, and adding to the list is what
needs a human approval.

**2. `inventory/apps/data/legacy-order-entry.yaml`** — `it_sme: Unknown` →
`it_sme: Dermot Walsh`, plus a dated note that he is in Order Management, not
IT, which is why four years of ownership never surfaced in anything IT was
looking at.

**3. `inventory/integrations/data/legacy-order-entry--meridian-erp.yaml`** —
`dr_impact: Unknown` → **`Stoppable - manual reconciliation`**, with
`failover_behavior` describing what actually happens: he holds the file and
reloads it the following morning; orders land a day late; he rings the customer
if it is urgent. Happened about three times.

**4. Register** — Q-003 and Q-004 close. **Q-005 and Q-006 stay open** — the
retirement date is still blocked on nobody having costed the pricing move, and
Dermot knows the terms exist but not who owns them commercially.

### What you should see on screen

| Before | After |
|---|---|
| `12 open gap(s)` | **`10 open gap(s)`** |
| Applications with no SME: **3** | **2** |
| Integrations with unknown DR impact: **2** | **1** |
| Retiring apps still moving data: **1** | **1** — unchanged, and correctly so |

### The beat to hit

Try it **without** the schema change first:

```bash
python automation/render-inventory.py --validate-only
```

It fails, naming the file, the field, and `Dermot Walsh` as a value not in the
approved roster. Then add him to `schema.yaml` and it passes.

> *"The model didn't get to decide that a new person exists. It had to ask."*

That is the whole trust argument in fifteen seconds of terminal output, and this
transcript exists to produce it.

---

## Running the loop properly on camera

Whichever you use, the full pass is:

```bash
# 1 · state before
python automation/gap-analysis.py

# 2 · the transcript lands
cp context/the-brief/demo-inputs/<file>.vtt evidence/meetings/

# 3 · process it — templates/prompt-process-transcript.md
#     ...which also preps the next round: templates/prompt-prepare-interview.md

# 4 · validate, render, redraw
python automation/render-inventory.py --validate-only
python automation/render-inventory.py
python automation/render-diagrams.py

# 5 · state after
python automation/gap-analysis.py
git status
```

Step 5 is the payoff shot. `git status` after one seven-minute conversation
shows a changed record, a new record, a rewritten view, a redrawn diagram, a
new summary, an updated register and a refreshed brief — none of which anybody
typed.

### Resetting between takes

```bash
git checkout . && git clean -fd evidence/meetings inventory diagrams
```

Check `git status` is clean before the next take. The generated files are
committed, so a half-reset leaves a diff that will confuse the "after" shot.

---

## If the assistant gets it wrong

Leave it in. Catching a miss on camera and correcting it is the most credible
thirty seconds you will record — it is the human-review step doing its job in
public rather than being described.

The likeliest misses, in order:

1. **Editing the RTO numbers in transcript A** despite Tom saying not to.
2. **Adding Dermot Walsh to the record but not to `schema.yaml`** — validation
   catches this, which is the demo.
3. **Over-reading the boundary dispute as resolved.** Neither A nor B settles
   it; both add detail. If a summary says it is decided, that is wrong.
4. **Manufacturing an insight row** where the conversation only restated
   something already recorded.

---

*Last updated: 2026-08-04*
