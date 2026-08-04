# Meeting Summary Template

Copy this into `evidence/meetings/YYYY-MM-DD-description.md` alongside the
transcript it summarizes. Add `-ai` to the filename for AI working sessions.

**Every transcript gets one.** A transcript without a summary has not been
processed — it is a recording somebody hopes to get to.

Delete the guidance in italics as you fill it in.

---
---

# <Title — what the conversation was about, not "Meeting Notes">

**Date:** YYYY-MM-DD
**Participants:** <names and roles>
**Transcript:** [`YYYY-MM-DD-description.vtt`](YYYY-MM-DD-description.vtt) — N minutes

---

## Purpose

*Two or three sentences. Why the conversation happened — including if it
happened for its own reasons and the documentation questions were asked
alongside, which is the normal case.*

---

## Key topics

*One table per topic. Tables, because a reader is scanning for one fact rather
than reading the whole thing.*

### <Topic>

| Question | Answer | Source |
|---|---|---|
| <what was asked> | <what was said> | <who said it> |

*Record what was said, not what you concluded from it. Where an answer was
hedged, keep the hedge — "Tom thought roughly four hours but has not tested it"
carries information that "RTO: 4 hours" destroys.*

---

## Decisions

*Only things actually decided by someone with the authority to decide them,
per [decision-rights.md](../../context/decision-rights.md). "We should
probably" belongs under action items.*

| Decision | Decided by | Recorded as |
|---|---|---|
| | | [DEC-NNN](../../decisions/decision-log.md) |

*Delete this section if nothing was decided. Most conversations decide nothing,
and that is fine.*

---

## Insights surfaced

*What the conversation revealed about the organization rather than about the
systems. Rows added to
[insights-surfaced.md](../../inventory/insights-surfaced.md).*

| Category | Insight |
|---|---|
| | |

---

## Action items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | | | Open |

*Owners are named individuals. "The team" is not an owner — same rule as the
inventory, and for the same reason.*

---

## Documents updated as a result

*The proof the transcript was mined. If this list is empty, either the
conversation contained nothing new — say so explicitly — or it has not actually
been processed.*

- `path/to/file.md` — what changed
- `inventory/apps/data/example.yaml` — which field and why

---

## Questions closed

*Which rows from [question-register.md](../question-register.md) this
conversation answered. Move them to the register's Answered table too — this
section is the snapshot, the register is the durable copy.*

| Q | Question | Answer |
|---|---|---|
| Q-NNN | | |

---

## Open questions

*The input to the next turn of the flywheel, and the most valuable section
here. Each question gets a name against it — a question with no owner does not
get asked.*

**Every row here must also be appended to
[question-register.md](../question-register.md).** The summary is read once;
the register is what survives to drive the next interview.

| Q | Question | Who can answer |
|---|---|---|
| Q-NNN | | |

*If someone was named only as a role — "you'd have to ask whoever runs that" —
put them in the register's people-to-identify table. Finding the person is the
open item, and nothing else in the repository will surface it.*

---

*Last updated: YYYY-MM-DD*
