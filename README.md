# Presentations

Markdown-first slide decks built with [Colloquium](https://github.com/baggiponte/colloquium).
Every deck in `slides/` is automatically compiled to HTML (GitHub Pages), PDF, and PPTX on push to `main`.

## Adding a new deck

1. Create `slides/my-deck/slides.md` with front matter:
   ```yaml
   ---
   title: "My Talk"
   author: "Your Name"
   date: "2026-01-01"
   description: "Short description shown on the index page."
   ---
   ```
2. Add images to `slides/my-deck/assets/`.
3. Run `make build` — the deck appears in `public/` automatically.

No config files need updating; the Makefile discovers all decks via `$(wildcard slides/*/slides.md)`.

## Local development

```bash
# Live-reload preview (default deck: example)
make serve

# Preview a specific deck
make serve DECK=my-deck
```

## Build locally

Requires: **uv**, **LibreOffice**, **Chromium** (via Playwright).

```bash
# Install deps (first time)
uv sync
uv run playwright install --with-deps chromium

# Full build
make build

# Individual steps
make html     # Markdown → HTML
make pdf      # Markdown → PDF  (requires Playwright/Chromium)
make pptx     # PDF → PPTX      (requires LibreOffice)
make index    # Generate public/index.html

# Clean
make clean
```

> **Note — PDF locally:** `colloquium export` uses a headless Chromium browser. If Playwright
> is not installed you will see an error. Run `uv run playwright install --with-deps chromium`
> once to install it. PDF generation always works in CI.
>
> **Note — PPTX quality:** LibreOffice converts the PDF by rasterising each slide as an image
> inside a PPTX container. Slides are not editable as native shapes. This is a known limitation
> of the PDF→PPTX path and is acceptable for download/distribution purposes.

## Deploy

Push to `main`. GitHub Actions builds everything and deploys `public/` to GitHub Pages via the
`gh-pages` branch.

Enable GitHub Pages in your repo settings: **Settings → Pages → Source: Deploy from branch → gh-pages**.

## Colloquium syntax cheatsheet

### Layouts

```markdown
<!-- layout: title-sidebar -->   # Title + sidebar layout
<!-- layout: section-break -->   # Full-bleed section divider
```

### Columns and rows

```markdown
<!-- columns: 45/55 -->
Left column content
|||
Right column content

<!-- rows: 35/65 -->
Top row content
===
<!-- row-columns: 50/50 -->
Left in bottom row
|||
Right in bottom row
```

### Vertical alignment

```markdown
<!-- valign: center -->
```

### Box component

````markdown
```box
tone: accent
```
Highlighted callout text.
```
````

Tones: `accent`, `info`, `warning`, `danger`.

### Conversation component

````markdown
```conversation
A: Hello, how are you?
B: I'm doing well, thanks!
```
````

### Citation (right-aligned)

```markdown
> "Quote text."

<!-- cite-right -->
— Author, *Source*
```
