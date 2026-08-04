# Prompt — Generate or Update a Diagram

For hand-authored D2 diagrams in `diagrams/source/`.

**Check first whether the diagram should be generated instead.** If the picture
can be derived from the inventory records, it should be — nobody draws
`integration-landscape.d2`, and nobody should. Hand-authoring is for diagrams
of things that are not in the record model: a process, a boundary, a proposed
future state.

---

You are working in the `documentation-flywheel` repository. Read `README.md`,
`meta/repo-conventions.md` (the Diagrams section), and an existing hand-authored
`.d2` in `diagrams/source/` before writing.

Produce or update a diagram showing:

> **<WHAT THE DIAGRAM SHOULD SHOW, and the one question a reader should be able
> to answer after looking at it>**

## Before you write

1. **Should this be generated?** If every fact in it lives in
   `inventory/apps/data/` or `inventory/integrations/data/`, extend
   `automation/render-inventory.py` instead. A hand-drawn version of derivable
   data will disagree with the data within a quarter.
2. **Is it one question?** A diagram answering three questions answers none.
   Draw three.
3. **Does it already exist?** Check `diagrams/source/`.

## Writing it

- Filename: `kebab-case.d2` in `diagrams/source/`. Never in `rendered/`.
- Open with a comment block: what it shows, that it is hand-authored, and which
  document it belongs to. Say which is authoritative if the two disagree.
- Include a `legend` markdown block explaining any visual convention you use —
  a dashed edge, a bold box, a colour. Follow the pattern in the existing
  diagrams.
- **Label the edges.** A line between two boxes with nothing on it says only
  that they are related, which the reader already assumed. Say what travels
  along it.
- Use containers for teams and boundaries — but see the layout note below
  before reaching for one to control *shape*.
- **Aim for 2:1; treat "wider than it is tall" as the floor.** A diagram taller
  than it is wide gets scaled down to the page width and becomes unreadable.
  For a long step-by-step loop, 2:1 may not be reachable — get it past 1:1 and
  stop.

### Layout, the hard way

Learned by losing an afternoon to it. All three of these are true of D2 v0.7.1
with the default engine:

- **`direction` is global, not per-container.** Dagre applies one direction to
  the whole diagram, so a nested `direction: right` inside a container is
  silently ignored. Containers laid out to control shape only add padding.
  Switching to `layout: elk` does not fix this either.
- **Grid layouts (`grid-columns`, `grid-rows`) drop every edge.** They give you
  exactly the arrangement you asked for and draw no connections at all. For a
  diagram whose point is the handoffs, that costs far more than the shape buys.
- **The lever that actually works is label width.** A column of narrow boxes is
  tall; the same column with wide single-line labels is short and wide. Writing
  a label as `A — B` on one line instead of stacked over three does more for
  aspect ratio than any layout directive.

If a diagram will not come out the right shape, the answer is usually fewer
boxes with wider labels, not a cleverer container structure.
- **No tooltips, no animations, no links.** Many markdown renderers strip them,
  so anything conveyed that way is invisible to some readers. Put the context
  in the legend or in the process document.

## Rendering

```bash
python automation/render-diagrams.py            # render every .d2 to SVG
python automation/render-diagrams.py --check    # parse only, write nothing
```

**Never call `d2` directly.** D2 scopes each SVG's CSS with a generated class
name derived per-platform, so a bare render produces a file with identical
geometry and different class names — which lands in the diff looking like a
change nobody made. The wrapper pins that id to the diagram's filename. Recorded
as [DEC-009](../decisions/decision-log.md).

Never edit a rendered SVG. It is overwritten on the next merge.

## Embedding

Reference it from the document it belongs to, with a relative path:

```markdown
![Alt text describing what it shows](../diagrams/rendered/your-diagram.svg)
```

Every `.d2` must produce an `.svg` — the pipeline fails the build if one does
not, which is deliberate: a source file with no output is a diagram someone
believes exists.

## After writing

- Render, and check the SVG opens and reads at the size it will be embedded at.
- Confirm `git status` shows only your new diagram and its SVG. If an unrelated
  SVG also changed, you rendered with bare `d2` — see above.
- Branch, pull request, do not merge.

---

*Last updated: 2026-08-04*
