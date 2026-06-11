.PHONY: all build html pdf pptx index serve clean

DECKS := $(patsubst slides/%/slides.md,%,$(wildcard slides/*/slides.md))

all: build

build: html pdf pptx index

# ── HTML ──────────────────────────────────────────────────────────────────────

html: $(DECKS:%=public/slides/%/index.html)

public/slides/%/index.html: slides/%/slides.md
	@mkdir -p public/slides/$*
	uv run colloquium build $< -o public/slides/$*/
	@# Rename output to index.html if colloquium wrote a different filename
	@if [ ! -f public/slides/$*/index.html ]; then \
		mv public/slides/$*/*.html public/slides/$*/index.html 2>/dev/null || true; \
	fi
	@# Copy assets directory if it exists
	@if [ -d slides/$*/assets ]; then \
		cp -r slides/$*/assets public/slides/$*/assets; \
	fi

# ── PDF ───────────────────────────────────────────────────────────────────────

pdf: $(DECKS:%=public/slides/%/slides.pdf)

public/slides/%/slides.pdf: slides/%/slides.md
	@mkdir -p public/slides/$*
	uv run colloquium export $< -o public/slides/$*/slides.pdf

# ── PPTX ──────────────────────────────────────────────────────────────────────

pptx: $(DECKS:%=public/slides/%/slides.pptx)

public/slides/%/slides.pptx: public/slides/%/slides.pdf
	/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --infilter="impress_pdf_import" --convert-to pptx:"Impress MS PowerPoint 2007 XML" $< --outdir public/slides/$*/

# ── INDEX ─────────────────────────────────────────────────────────────────────

index: public/index.html

public/index.html: $(wildcard slides/*/slides.md) scripts/build_index.py
	@mkdir -p public
	uv run python scripts/build_index.py

# ── SERVE ─────────────────────────────────────────────────────────────────────

DECK ?= example

serve:
	uv run colloquium serve slides/$(DECK)/slides.md

# ── CLEAN ─────────────────────────────────────────────────────────────────────

clean:
	rm -rf public/
