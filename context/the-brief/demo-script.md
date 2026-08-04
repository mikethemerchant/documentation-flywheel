# Recording Script

For a screen-recorded demo video — YouTube, cut down for LinkedIn and the
personal site. Not a live talk: there is no room, no wifi risk, and **you can
retake anything**, so the script is written to be bolder than a stage version
would be.

Companion to [slides.html](slides.html) — arrows navigate, **F** fullscreen,
**O** overview.

**Target: 14–16 minutes.** Structure is *slides → live repo → slides*.

> Everything in the dataset is fictional. Do not name a real employer, a real
> colleague, or a real system on camera. The production experience is referable
> only as *"a mid-market manufacturer"* — same wording as the README.

---

## Shape of the video

| # | Segment | Screen | Target |
|---|---|---|---|
| 0 | Cold open — the hook | Terminal | 0:25 |
| 1 | Title + why documentation dies | Slides 1–3 | 2:00 |
| 2 | What it is | Slides 4–6 | 1:30 |
| 3 | **The repo, live** | Editor + terminal | 3:00 |
| 4 | **The pipeline, live** | Terminal + GitHub | 2:00 |
| 5 | **The flywheel, live** | Slides 10–11, then files | 2:30 |
| 6 | **Processing a transcript, live** | Slide 12, then assistant | 2:30 |
| 7 | The two payoffs | Slides 13–16 | 1:30 |
| 8 | Scale + close | Slides 17–19 | 0:45 |

**Record it in eight takes, one per segment.** Do not attempt one pass. Every
segment starts on a clean screen so cuts are invisible.

---

## Before you record

**Screen**

- Record at **1920×1080**. Set display scaling so the terminal is readable at
  1080p on a phone — roughly 18–20pt, which will feel comically large on your
  monitor. Check by recording ten seconds and watching it on your phone.
- Editor: same, ~16–18pt. Hide the minimap, the sidebar, and any file tree you
  are not actively pointing at.
- Browser: hide bookmarks bar. One window, one tab per segment.
- **Close everything else.** Notifications off, Slack quit, phone face down.
  A toast notification mid-take is a re-record.
- Hide any personal path, machine name, or account avatar that appears in a
  terminal prompt or a browser chrome. Simplify your prompt to something plain
  before recording.

**Repo**

```bash
git status                                   # must be clean
python automation/render-inventory.py --validate-only
python automation/render-diagrams.py --check
python automation/gap-analysis.py
```

- Work on a **scratch branch** — you break records on camera.
- Pre-bake a **red** Actions run from a deliberately bad value, so segment 4 can
  cut straight to it instead of waiting on CI.
- Deck open in a second browser window, fullscreen (**F**).

**Audio.** Fix this before anything else — viewers forgive a rough visual and
leave over bad audio. Record a test minute and listen on headphones.

---

## 0 · Cold open — 0:25

**No title card yet.** Open on the terminal, already run:

```bash
python automation/gap-analysis.py
```

Output on screen, scrolled to the summary line.

> "This is a list of everything an IT department doesn't know about its own
> systems. Which applications nobody owns. Which data flows nobody has ever
> characterised. It's generated — nobody wrote it.
>
> And it came out of recording meetings that were happening anyway.
>
> Let me show you how."

**Cut to slide 1.** Hard cut, no transition.

> The first fifteen seconds decide whether anyone watches the rest. Lead with
> the artifact, not with who you are or what the video is about. Do not say
> "in this video I'm going to."

---

## 1 · Why documentation dies — 2:00

*Slides 1 → 2 → 3.*

Title slide, then straight in.

> "Most architecture documentation dies the same way. Somebody writes it once,
> in a tool separate from the work. They become the only person who maintains
> it. They get busy. Six months later nobody trusts it, so nobody reads it, so
> nobody updates it."

*Slide 2 — the six steps. Let the amber step 3 sit for a beat.*

> "Nobody fails at step one. Everybody fails at step three."

*Slide 3.*

> "So the real constraint isn't tooling, and it isn't modelling skill. It's the
> attention of the people who actually know things.
>
> Any process that eventually asks a busy expert to *write* something stalls at
> exactly the point it starts being useful.
>
> So the design goal for this whole thing was: **no homework for the expert.**
> Everything else follows from that."

**Pause a full beat after that line.** In edit, this is where a one-second hold
earns its place — it is the thesis of the video.

---

## 2 · What it is — 1:30

*Slides 4 → 5 → 6.*

Three commitments, the folder map, and one-record-in-every-view-out. Keep it
moving; this is orientation, not the payoff.

> "Everything is a text file in one Git repo. Structured data gets *transformed*
> into every view anyone asks for, so nothing derived is maintained by hand. And
> the rules are enforced by the build, not by policy.
>
> Seventeen YAML records produce seven summary views, seventeen detail pages and
> a diagram. None of them are written — which means they can't disagree with
> each other. That's the thing a spreadsheet inventory can never give you."

**Cut to screen.**

---

## 3 · The repo, live — 3:00

Screen: editor + terminal. No slides in this segment.

**Open the folder tree.**

> "Every folder is named for a question, not a document type. `decisions` answers
> *why is it like this*. `evidence` answers *show me what actually happened*."

**Open `inventory/apps/data/meridian-erp.yaml`.**

> "This is the entire source of truth for one application. Forty lines. Owner,
> criticality tier, recovery targets, hosting, what business capabilities it
> covers."

**Open `inventory/rendered/dr-posture.md`.**

> "And this is generated from those records. What writes into the core system,
> ordered by how badly it goes if the flow is interrupted. Nobody maintains
> this page — it's a projection of the data."

### The gate — the money shot of this segment

Edit `meridian-erp.yaml` on camera:

```yaml
it_sme: Applications        # was: Priya Raman
```

```bash
python automation/render-inventory.py --validate-only
```

Let the failure fill the screen. **Zoom in on it in the edit.**

> "A team name is a valid-looking answer that answers nothing. You can't call
> *Applications* at two in the morning.
>
> And here's the part that matters if you're pointing an AI at this: that list
> of people is controlled. An assistant drafting a record from a transcript
> **cannot** invent someone into it, because the build fails.
>
> I don't need the model to behave well. I need the gate."

Try an unapproved vendor too — same failure, different field. Then:

```bash
git checkout inventory/apps/data/meridian-erp.yaml
```

---

## 4 · The pipeline, live — 2:00

Screen: terminal, then GitHub Actions.

```bash
head -30 diagrams/source/integration-landscape.d2
```

> "This diagram source is *generated* from the integration records. Nobody draws
> it."

Edit or add an integration record, then:

```bash
python automation/render-inventory.py
python automation/render-diagrams.py
```

Open the redrawn SVG side by side with the old one.

> "One record changed — and the integration matrix, both endpoint pages, and the
> diagram all moved. Add a record, the picture redraws itself on merge."

**Cut to the Actions tab**, green run then the pre-baked red one.

> "Validation runs on every pull request and writes nothing. A bad value fails
> *there*, before merge — not as a comment in code review that someone argues
> with."

### The drift story — 45 seconds, and don't cut it

*Optionally flash slide 9 here, or stay on screen.*

> "First time this pipeline ran, it committed back a 284-line diff on a diagram
> nobody had touched. Same geometry, same viewBox to the pixel. The only
> difference was a CSS class name the diagram tool derives per-platform.
>
> My first fix was wrong. Looked right, cheap, plausible — and it failed again.
> Took a second failure and a byte-level comparison to find the real cause."

Open `decisions/decision-log.md` at DEC-008.

> "That wrong decision is still in the log. Unedited. Marked superseded.
>
> A log that quietly corrects itself can't tell you why you changed your mind —
> and the reasoning behind a reversal is usually worth more than the reversal."

**This is the segment that makes the rest believable.** A demo where nothing
ever went wrong reads as a sales pitch.

```bash
git checkout .
```

---

## 5 · The flywheel, live — 2:30

*Slide 10* — diagram and the three beats. Then cut to files.

> "Steps one to three are the assistant's prep, on a branch. Step four is a
> human approving. Five and six are the conversation and processing it — and
> step six *is* steps one to three for the next round.
>
> After the first turn it's three beats. Approve, talk, process."

> "The approval sits in the *middle* of the loop, not at the end. That's the one
> design decision I'd defend hardest. It means one pull request carries both the
> closeout of the last conversation and the prep for the next one — so the merge
> itself hands you a briefed interview, against documentation that's already
> current."

*Slide 11 — the state board.* Then open the real files.

> "Nobody here owns 'keeping the documentation current.' That job doesn't exist,
> and every time someone invents it, it gets dropped. What I own is the state of
> this board."

**Open `evidence/question-register.md`.** Scroll the queue, then the
people-to-identify table.

> "Twenty-one open questions, every one with a name against it. Three of them
> aren't waiting on a calendar — they're waiting on somebody going and finding
> out who a person *is*. A question waiting on scheduling gets asked eventually.
> A question waiting on a name sits forever, so it gets its own table."

**Open `evidence/interviews/tom-bergstrom.md`.**

> "And this is what I walk into the next meeting with. The questions written as
> I'd actually say them out loud. What a good answer sounds like, so I know when
> to stop pushing. And a *do not ask* section — because their time is the scarce
> resource, and asking someone something they answered in March is the one move
> that kills this."

> "Only three of the eight people in the queue have a brief, and that's correct,
> not unfinished. You brief the meetings that are actually happening."

---

## 6 · Processing a transcript, live — 2:30

*Slide 12*, then the assistant. **The centrepiece.**

**Use an unprocessed transcript from
[`demo-inputs/`](demo-inputs/expected-changes.md)** — those three are the only
ones in the repo with no summary, so the run genuinely produces new output
rather than redoing work.

**Read `demo-inputs/expected-changes.md` before recording.** It is the answer
key: exactly which files should change, the gap count before and after, and the
four most likely places the assistant gets it wrong.

Default pick: **`2026-08-04-infrastructure-catchup.vtt`** — the only one that
produces a new integration record, so the landscape diagram redraws on camera.

```bash
python automation/gap-analysis.py     # 12 open gaps — show this first
cp context/the-brief/demo-inputs/2026-08-04-infrastructure-catchup.vtt evidence/meetings/
```

> "That's what came off Teams this morning. Straight off Teams — cue IDs,
> timestamps, speaker tags. Seven minutes of me catching our infrastructure
> lead rather than waiting six weeks for the DR review.
>
> Notice it mangles proper nouns. We leave those in — a transcript is evidence,
> and correcting it edits the record of what was said."

**Run it.** Fresh assistant session, paste
`templates/prompt-process-transcript.md` with the transcript path.

**In the edit: speed this up 4–8×** with the narration over the top. Nobody
watches a model think in real time.

> "It reads the repo first — the README, the meta files, the context — then the
> transcript, then the records the transcript touches. It has to separate
> genuinely new information from a restatement of something already recorded."

**Stop at the proposal step. Slow back to real time here.**

> "It proposes before it writes: file paths, what changes in each, and the quote
> that justifies it. This is where I correct an *intent* rather than a pile of
> edits — much cheaper. And it's where I catch it misreading something. Which
> happens."

Let it finish, then run the pipeline and show the state change:

```bash
python automation/render-inventory.py --validate-only
python automation/render-inventory.py
python automation/render-diagrams.py
python automation/gap-analysis.py     # 10 open gaps
git status
```

**The `git status` is the payoff shot.** Hold on it.

> "One seven-minute conversation. A changed record, a brand new integration
> record, four rewritten views, a redrawn diagram, a summary, an updated
> register and a refreshed brief. I typed none of that.
>
> And the diagram — endpoint management was floating on its own on that picture
> five minutes ago. Nobody drew that line. It came out of a record that came
> out of a sentence Tom said."

> "It doesn't come out perfect. It comes out eighty per cent right in ninety
> seconds — and eighty per cent in ninety seconds is transformative when the
> alternative is a blank page and a busy person."

Reset between takes:

```bash
git checkout . && git clean -fd evidence/meetings inventory diagrams
```

**Land on slide 12's table.** Open `inventory/insights-surfaced.md` beside it.

> "We set out to build a catalog. This is what fell out — and it's the part
> people actually act on.
>
> Nobody set out to discover that one person is sole SME, sole technical owner
> *and* sole recovery owner for both integration paths — every commercial order
> that enters the business.
>
> None of this was secret. Everyone knew their own piece. It wasn't *visible*
> until the ordinary facts got written down in a structured way."

---

## 7 · The two payoffs — 1:30

*Slides 13 → 14 → 15 → 16.* Back to slides for the wrap.

> "So that's payoff one: documentation people trust, because it's generated,
> reviewed and validated — not because someone promised to keep it current.
>
> Payoff two is the one I actually care about."

*Slide 14 — the comparison.*

> "The limit on enterprise AI right now isn't model capability. It's that the
> model has no idea what your systems are, who owns them, or why they're like
> that.
>
> Ask a general assistant about your DR posture and you get best practices.
> Correct, generic, useless. Ask it here and you get: *the EDI path can't be
> stopped, partners don't retry, and forty per cent of order lines arrive that
> way* — sourced to the conversation where somebody said it.
>
> Same model. Different context."

*Slide 15.*

> "And the two assets feed each other. Every turn produces documentation *and*
> better context. Better context means sharper drafting, better questions,
> richer records. The loop gets more useful the longer it runs — which is the
> exact opposite of how documentation normally ages."

*Slide 16.*

> "The AI reads messy prose and drafts structure. That's where it's cheap and
> genuinely good. It doesn't decide, approve, or publish. A human does all
> three — and the schema stops it inventing a person even when nobody's
> watching."

---

## 8 · Scale and close — 0:45

*Slides 17 → 18 → 19.*

> "Once the structure existed: forty-five interviews in six days. A few hundred
> applications and their integrations, out of people's heads and into validated
> YAML. The structuring is a one-time cost. The interviews parallelise — they're
> just conversations.
>
> The only thing that didn't scale was me.
>
> This isn't an EA tool or a CMDB. If you need lifecycle workflows and cost
> modelling and a hundred stakeholders in a UI, buy something. This is for when
> you have none of that and need the answers anyway."

*Slide 19.*

> "Everything I showed you is one MIT-licensed repo — link in the description.
> Clone it and it runs.
>
> If you want this built against your estate, message me. The structuring is the
> hard part, and it only has to be done once."

**Stop talking.** No sign-off ramble, no "thanks for watching." Cut on the last
word.

---

## Editing notes

| Where | Do |
|---|---|
| Everywhere | Cut every pause, every "um", every command mistype. Dense beats polished. |
| Terminal output | Zoom to 130–150% on the failing validation and the gap report. Text that is readable on your monitor is not readable on a phone. |
| The assistant running | Speed up 4–8× with narration over it. Return to real time for the proposal step. |
| Slide transitions | Hard cuts. No dissolves. |
| Segment joins | A half-second of silence between segments reads as a breath, not a mistake. |
| Captions | Burn them in, or at minimum upload an SRT. Most LinkedIn viewing is muted. |
| First 15 seconds | Watch it back cold. If it doesn't earn the next 15, re-record the cold open. |

**LinkedIn cut:** pull a 60–90 second version from segment 0 + the gate failure
in segment 3 + the closing line. Post that natively with a link to the full
video — LinkedIn suppresses outbound links, and a native clip does the
persuading.

---

## YouTube chapters

Adjust timestamps after the edit; the labels are what matter.

```
0:00  What your documentation doesn't know
0:25  How documentation always dies
2:25  What this actually is
3:55  The repository
5:15  The schema gate — an AI that can't invent a person
6:55  The pipeline, and the day it caught me
8:55  The flywheel
10:10 Running it: the question register and the briefs
11:25 Live: a Teams transcript becomes validated records
13:55 What we found that nobody asked for
14:30 Why this is really a context problem
15:45 45 interviews in 6 days
```

## Description — draft

Edit the first two lines; they are the only ones shown before "more".

```
Most architecture documentation dies because one person owns it and gets busy.
This is a working system where nobody owns it — and it stays current anyway.

A public reference implementation: architecture decisions, process docs, system
diagrams and an application inventory, all as plain text in one Git repo,
validated by CI and published automatically. Meetings you were already having
get recorded; an AI drafts the updates; a human approves; the pipeline publishes.

The demonstration data is fictional. The method runs in production at a
mid-market manufacturer, where the first pass produced 45 interviews in 6 days.

Repo (MIT): <link>
Written version: <link>

Chapters below.
```

## LinkedIn post — draft

```
Documentation doesn't die because people are lazy. It dies because one person
becomes its owner, and then they get busy.

So I built the loop the other way round: the expert never writes anything. They
have a meeting they were already having, it gets recorded, an AI drafts the
records and diagrams, a human approves, and CI publishes.

Two things came out of it that I didn't expect.

The first is the insight register — the byproduct. We set out to build a
catalog and ended up with a list of things the organisation didn't know about
itself. One person solely owning every inbound commercial data path. A Tier 2
system sitting inside a Tier 1 transaction. None of it secret; none of it
visible until the ordinary facts were written down in a structured way.

The second is that this turns out to be a context engineering project wearing a
documentation hat. The limit on enterprise AI isn't the model — it's that the
model has no idea what your systems are or who owns them. Fix that and the same
model gets specific and checkable.

Full walkthrough + the repo (MIT, clone it and it runs): <link>
```

---

## Objections worth pre-empting

These land in the comments. Answering one or two on camera is stronger than
letting them accumulate; the rest are pinned-comment material.

| Objection | Answer |
|---|---|
| *How do you stop the AI making things up?* | You don't — you make it fail loudly. Controlled vocabularies, a build that rejects unknown values, a human on every merge. **Shown on camera in segment 3.** |
| *Doesn't this just move the maintenance burden?* | The burden was writing. That's gone. What's left is approving a diff and turning up to meetings you were already in. |
| *What if people won't be recorded?* | Ask at the top and say why. Nobody has objected. Not asking is how you get someone who does. |
| *Does this replace our EA tool?* | No. It answers a specific set of questions the tool probably also answers, for nothing, in text you own. |
| *Which model?* | Whatever you have. The gate does the work, not the model. |
| *What about sensitive data?* | It doesn't go in. Cut it before committing; record that it exists and where it lives, not the detail. |

---

## Do not

- **Do not** name a real employer, colleague or system on camera — check the
  recording for a stray browser tab, a terminal path, or an avatar.
- **Do not** present the fictional numbers as real ones. Say "the demo data is
  invented" once, early, and move on.
- **Do not** hide the model getting something wrong. Leave it in and correct it.
  It is the most credible thirty seconds in the video.
- **Do not** open with who you are or what the video will cover. Open with the
  artifact.
- **Do not** try to record it in one take.

---

*Last updated: 2026-08-04*
