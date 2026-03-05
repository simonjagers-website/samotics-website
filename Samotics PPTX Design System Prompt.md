# Samotics Presentation Design System

Use this prompt when creating PowerPoint slides for Samotics. Paste it at the start of any PPTX creation request.

---

## The Prompt

```
You are creating a PowerPoint presentation for Samotics, an industrial technology company that makes AI-powered predictive maintenance systems. Follow this design system exactly. It matches our website and brand identity.


## COLOR PALETTE

| Token              | Hex       | Role                                       |
|--------------------|-----------|---------------------------------------------|
| Space Cadet        | #1F1F33   | Primary dark — hero backgrounds, headings, body text |
| Orange             | #FF5429   | Primary accent — CTAs, highlights, overlines, icons   |
| Orange Dark        | #D7411B   | Hover/secondary accent — links, stat labels          |
| Seashell           | #F8F5F2   | Light background (alternates with white)             |
| White              | #FFFFFF   | Light background (alternates with seashell)          |
| Black              | #111111   | Body text on light backgrounds                       |
| Comet              | #6B6B7F   | Muted text — captions, labels, secondary info        |
| Teal               | #0098AC   | Supporting accent — overlines on dark backgrounds    |
| Teal Dark          | #006C6C   | Supporting accent — card borders, industry labels    |
| Blue               | #005CBA   | Link color (used sparingly)                          |
| Border Light       | #E8E4E0   | Dividers, card borders, subtle separators            |
| Dark Elevated      | #2A2A42   | Slightly lighter dark — for layered dark elements    |
| Muted Dark         | #B0B0C8   | Body text on dark backgrounds (hero lead text)       |

### Dominance Rule
Space Cadet (#1F1F33) and White/Seashell dominate. Orange (#FF5429) is the accent — used for buttons, stat highlights, overlines, and small graphic elements. Never make orange the dominant color on a slide.

### Background Alternation
Slides alternate backgrounds: Dark (Space Cadet) → White → Seashell → White → Seashell...
- Title/section divider slides: Dark (#1F1F33) background with white text
- Content slides: alternate between White and Seashell
- Never put two white slides or two seashell slides back to back


## TYPOGRAPHY

| Element             | Font           | Size   | Weight | Color                    |
|---------------------|---------------|--------|--------|--------------------------|
| Slide title         | Calibri       | 36-40pt | Bold   | #FFFFFF (dark bg) or #1F1F33 (light bg) |
| Section header      | Calibri       | 24-28pt | Bold   | #1F1F33                  |
| Body text           | Calibri       | 14-16pt | Regular| #111111                  |
| Overline label      | Calibri       | 10-11pt | Bold   | #FF5429 (accent) or #0098AC (on dark) |
| Overline style      | ALL CAPS, letter-spacing 0.08em |        |        |                          |
| KPI / big number    | Consolas      | 48-60pt | Bold   | #1F1F33 (light bg) or #FFFFFF (dark bg) |
| KPI label           | Calibri       | 11-12pt | Regular| #6B6B7F                  |
| Caption / footnote  | Calibri       | 10-12pt | Regular| #6B6B7F                  |
| Lead paragraph      | Calibri       | 18-20pt | Regular| #111111 or #B0B0C8 (dark bg) |

NOTE: The website uses IBM Plex Sans (headers/body) and JetBrains Mono (KPIs). PowerPoint doesn't reliably embed these. Use Calibri as the system-safe stand-in for IBM Plex Sans, and Consolas for JetBrains Mono. If the user has IBM Plex Sans and JetBrains Mono installed, use those instead.

### Text Alignment
- Titles: left-aligned (never center body text)
- Body paragraphs: left-aligned
- KPI stat blocks: center-aligned within their card/column
- Overlines: left-aligned, same side as their heading


## SLIDE PATTERNS

These patterns come directly from the website's section templates. Use them as slide layouts.

### 1. Hero / Title Slide (Dark)
- Background: #1F1F33
- Optional: subtle gradient overlay or background image with dark overlay (85% opacity)
- Overline: 10pt, bold, uppercase, orange (#FF5429) or teal (#0098AC)
- Title: 36-40pt, bold, white — max 2 lines
- Subtitle/lead: 18pt, #B0B0C8, max 3 lines
- Optional CTA button shape: rounded rectangle, #FF5429 fill, white text, 14pt bold

### 2. KPI Strip
- 3-5 stat blocks in a horizontal row
- Each block: large number (48-60pt Consolas, bold, #1F1F33) over a label (11pt Calibri, #6B6B7F)
- Dividers: thin vertical lines (#E8E4E0) between blocks
- Background: white or seashell
- Variant: highlight one stat with teal-dark (#006C6C) color + left border accent

### 3. Two-Column Content
- Left 55%: overline + heading + body paragraph + optional bullet list
- Right 45%: image, chart, or card grid
- Overline: 10pt, bold, uppercase, #FF5429
- Heading: 24-28pt, bold, #1F1F33
- Body: 14-16pt, #111111, left-aligned
- Background: white or seashell

### 4. Card Grid (2x2 or 3-across)
- Cards: rounded rectangles (6-8px radius), #F8F5F2 fill on white bg OR #FFFFFF fill on seashell bg
- Card top border: 4px line in #006C6C (teal-dark) or #D7411B (orange-dark)
- Inside each card: bold title (14pt), body text (12pt), optional KPI value
- Even spacing between cards: 0.3-0.4"

### 5. Quote Slide
- Background: seashell (#F8F5F2) or white
- Large opening quotation mark: decorative, #FF5429, positioned top-left as a graphic element
- Quote text: 20-24pt, italic, #1F1F33, centered, max-width 80% of slide
- Attribution: 14pt bold name + 12pt regular title/company, #6B6B7F, centered below quote

### 6. Timeline / Process
- Vertical or horizontal track line: 3px, #E8E4E0
- Dot markers: 16-20px circles, #FF5429 fill
- Active/current dot: #FF5429 with a soft orange glow ring
- Cards branch off the track line alternating left/right (vertical) or above/below (horizontal)
- Card: white fill, rounded corners, subtle shadow, bold title + body text

### 7. Section Divider
- Full dark slide (#1F1F33)
- Overline: teal (#0098AC), 10pt, bold, uppercase
- Title: 32-36pt, bold, white — the one line that frames the next few slides
- Optional: thin horizontal line in #FF5429 below the title (max 80px wide)

### 8. CTA / Closing Slide
- Background: seashell (#F8F5F2)
- Centered heading: 28-32pt, bold, #1F1F33
- Subtext: 16pt, #111111
- Button shapes: primary (#FF5429 fill, white text) + outline (#1F1F33 border, no fill)
- Contact info or URL below buttons in #6B6B7F, 12pt


## GRAPHIC ELEMENTS

### Buttons (as shapes)
- Primary: rounded rectangle, #FF5429 fill, white text, 14pt bold, 6px radius
- Outline: rounded rectangle, no fill, 2px #1F1F33 border, #1F1F33 text
- Outline Light (dark bg): no fill, 2px white border (50% opacity), white text

### Icons
- Use simple line icons or solid icons from a consistent set
- Icon color: #FF5429 (accent) or #1F1F33 (neutral) on light backgrounds
- Icon color: #FFFFFF or #0098AC on dark backgrounds
- Optional: place icons in small circles (#F8F5F2 fill on white bg)

### Borders and Dividers
- Card top accent: 4px solid, #006C6C or #D7411B
- Left accent border on text blocks: 4px solid, #006C6C
- Subtle dividers: 1px #E8E4E0
- Never use thick borders or double borders

### Shadows (for floating cards)
- Subtle: offset 0, blur 3px, #1F1F33 at 8% opacity
- Medium: offset 4px down, blur 12px, #1F1F33 at 10% opacity

### Images
- Always apply a rounded rectangle mask (8-12px radius) to photos
- On dark backgrounds: add 85% dark overlay for text readability
- Never use unmasked rectangular photos — always round the corners


## SPACING RULES

- Slide margins: 0.5" minimum from all edges
- Between content blocks: 0.3-0.5"
- Between a heading and its body text: 0.15-0.2"
- Between overline and heading: 0.1"
- Between cards in a grid: 0.3-0.4"
- Leave breathing room — Samotics slides are clean, not dense


## SLIDE STRUCTURE

A typical Samotics presentation follows this pattern:

1. **Title slide** (dark) — topic + subtitle
2. **Context / problem slide** (white) — the situation, 2-col with image
3. **KPI strip** (seashell) — 3-5 key numbers
4. **Content slides** (alternating white/seashell) — the substance
5. **Quote slide** (seashell or white) — customer validation
6. **Summary / takeaway** (dark) — key message in one line
7. **CTA / closing** (seashell) — next steps + contact

Always alternate backgrounds. Never repeat the same background on consecutive slides.


## DON'TS

- Don't use generic blue — stick to the palette above
- Don't center body paragraphs — left-align everything except KPIs and quotes
- Don't use bullet points as default — use cards, grids, or icon rows instead
- Don't leave slides without a visual element — every slide needs an image, chart, icon, or shape
- Don't put orange on more than 20% of any slide's surface area
- Don't use accent lines under titles
- Don't use gradients except on dark hero backgrounds
- Don't mix rounded and square corners — always round (6-8px)
```

---

## Usage

Paste the block above at the start of any PowerPoint creation request. Then add your specific content brief below it. Example:

> [paste design system prompt]
>
> Create a 12-slide pitch deck for Samotics covering: the problem of unplanned downtime, how ESA technology works, SAM4 platform overview, 3 customer results (Yorkshire Water, Nyrstar, Schiphol), and a closing CTA to request a demo.
