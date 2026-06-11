#!/usr/bin/env python3
"""Generate public/index.html from slide deck front matter."""

import os
from pathlib import Path
from datetime import date

import frontmatter

ROOT = Path(__file__).parent.parent
SLIDES_DIR = ROOT / "slides"
OUTPUT = ROOT / "public" / "index.html"


def load_decks():
    decks = []
    for md_file in sorted(SLIDES_DIR.glob("*/slides.md")):
        deck_name = md_file.parent.name
        post = frontmatter.load(md_file)
        decks.append({
            "slug": deck_name,
            "title": post.get("title", deck_name.replace("-", " ").title()),
            "author": post.get("author", ""),
            "date": str(post.get("date", "")),
            "description": post.get("description", ""),
        })
    decks.sort(key=lambda d: d["date"] or "0000-00-00", reverse=True)
    return decks


def card_html(deck):
    slug = deck["slug"]
    title = deck["title"]
    author = deck["author"]
    date_str = deck["date"]
    description = deck["description"]
    meta_parts = [p for p in [author, date_str] if p]
    meta_line = " · ".join(meta_parts)
    return f"""
    <div style="background:#fff;border:1px solid #dce3ef;border-radius:8px;padding:24px 28px;display:flex;flex-direction:column;gap:12px;">
      <div>
        <h2 style="margin:0 0 4px;font-size:1.15rem;color:#1B3A6B;">{title}</h2>
        {f'<p style="margin:0;font-size:0.85rem;color:#555;">{meta_line}</p>' if meta_line else ""}
      </div>
      {f'<p style="margin:0;font-size:0.95rem;color:#333;line-height:1.5;">{description}</p>' if description else ""}
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;">
        <a href="slides/{slug}/" style="display:inline-block;padding:7px 18px;background:#1B3A6B;color:#fff;text-decoration:none;border-radius:5px;font-size:0.9rem;font-weight:600;">View Slides</a>
        <a href="slides/{slug}/slides.pdf" style="display:inline-block;padding:7px 18px;background:#fff;color:#1B3A6B;text-decoration:none;border-radius:5px;font-size:0.9rem;font-weight:600;border:2px solid #1B3A6B;">PDF</a>
        <a href="slides/{slug}/slides.pptx" style="display:inline-block;padding:7px 18px;background:#fff;color:#1B3A6B;text-decoration:none;border-radius:5px;font-size:0.9rem;font-weight:600;border:2px solid #1B3A6B;">PPTX</a>
      </div>
    </div>"""


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    decks = load_decks()
    cards = "\n".join(card_html(d) for d in decks)
    built_date = date.today().isoformat()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Presentations</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Calibri, 'Segoe UI', system-ui, sans-serif;
      background: #f5f7fb;
      color: #1B3A6B;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: #1B3A6B;
      color: #fff;
      padding: 36px 40px 28px;
    }}
    header h1 {{
      margin: 0;
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: -0.5px;
    }}
    main {{
      flex: 1;
      max-width: 860px;
      width: 100%;
      margin: 0 auto;
      padding: 36px 24px;
    }}
    .deck-grid {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    footer {{
      text-align: center;
      padding: 20px;
      font-size: 0.82rem;
      color: #888;
      border-top: 1px solid #dce3ef;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Presentations</h1>
  </header>
  <main>
    <div class="deck-grid">
{cards}
    </div>
  </main>
  <footer>Built with <a href="https://github.com/baggiponte/colloquium" style="color:#1B3A6B;">Colloquium</a> · {built_date}</footer>
</body>
</html>
"""
    OUTPUT.write_text(html)
    print(f"Index written to {OUTPUT} ({len(decks)} deck(s))")


if __name__ == "__main__":
    build()
