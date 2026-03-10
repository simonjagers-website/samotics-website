# Samotics Typography System

*Design specification for samotics.com — March 2026*
*Updated to match the component library design system (Storybook). All values are final unless noted.*

---

## Design Intent

Samotics is building a new industrial category: Inaccessible Asset Monitoring. The typography must project the authority of an engineering standard while rendering complex technical data with absolute clarity.

The system uses one typeface family. One font. Two weights. No exceptions.

---

## Type Family

### Aeonik

**Role:** Everything — headlines, body copy, lead paragraphs, CTAs, navigation, UI elements, data tables, KPI displays, code references.

**Why:** Aeonik is a geometric sans-serif with strong industrial character. It carries structural clarity and neutrality — the visual language of precision engineering — while maintaining warmth at reading sizes. The single-family approach eliminates font-pairing complexity and keeps the brand voice unified across all contexts. It reads as "modern engineering standard," which matters when your buyer is a reliability engineer deciding whether to trust your platform with a critical asset.

**Key characteristics:**

- Clean geometric letterforms with humanist touches
- Strong readability at small sizes (data tables, labels)
- Works across all contexts — narrative, data, UI — without family switching
- Two weights only: Regular (400) and Bold (700)

**Weights:**

| Token | Value | Usage |
|---|---|---|
| `--font-weight-regular` | `400` | Body copy, labels, inputs, captions, data cells |
| `--font-weight-bold` | `700` | Headings, CTAs, emphasized text, KPI values |

No light, medium, semibold, or extra-bold. Two weights enforce hierarchy through size and spacing, not weight variation.

---

## Type Scale

The scale uses named tokens rather than a mathematical ratio. Seven sizes cover all use cases.

### Headings

| Token | Size (px) | CSS Variable | Weight | Usage |
|---|---|---|---|---|
| Heading Large | 24 | `--font-size-heading-lg` | 700 | Page titles, hero headings, section headers |
| Heading Medium | 20 | `--font-size-heading-md` | 700 | Sub-section headings, card titles |
| Heading Small | 16 | `--font-size-heading-sm` | 700 | Feature labels, table headers, sidebar headings |
| Heading XS | 14 | `--font-size-heading-xs` | 700 | Overlines, tag labels, small section titles |

### Body

| Token | Size (px) | CSS Variable | Weight | Usage |
|---|---|---|---|---|
| Body Large | 16 | `--font-size-body-lg` | 400 | Lead paragraphs, prominent body copy |
| Body Medium | 14 | `--font-size-body-md` | 400 | Default body copy, descriptions, form labels |
| Body Small | 12 | `--font-size-body-sm` | 400 | Captions, footnotes, metadata, timestamps |

### Scale Summary

```
heading-lg   24px  Bold
heading-md   20px  Bold
heading-sm   16px  Bold
heading-xs   14px  Bold
body-lg      16px  Regular
body-md      14px  Regular
body-sm      12px  Regular
```

Note: `heading-sm` and `body-lg` share the same pixel size (16px). They are distinguished by weight (700 vs 400). This is intentional — it keeps the scale compact while maintaining clear hierarchy through weight contrast.

---

## Mapping to HTML Elements

| Element | Token | Size | Weight | Notes |
|---|---|---|---|---|
| `h1` | heading-lg | 24px | 700 | Page title. One per page. |
| `h2` | heading-md | 20px | 700 | Section headings |
| `h3` | heading-sm | 16px | 700 | Sub-section, card titles |
| `h4` | heading-xs | 14px | 700 | Overlines, small headings |
| `p` (default) | body-md | 14px | 400 | Standard paragraph |
| `p.lead` | body-lg | 16px | 400 | Lead/intro paragraphs |
| `small`, `.caption` | body-sm | 12px | 400 | Captions, footnotes |
| `button`, `.cta` | heading-sm | 16px | 700 | Button labels |
| `label` | body-md | 14px | 400 | Form labels |
| `.overline` | heading-xs | 14px | 700 | Uppercase, tracked out |

---

## Line Height and Spacing

| Context | Line Height | Notes |
|---|---|---|
| Headings (all sizes) | 1.2–1.3 | Tight for compact headers |
| Body copy | 1.5–1.6 | Relaxed for readability |
| UI elements (buttons, labels) | 1.0 | Precise control for components |
| Captions / metadata | 1.4 | Slightly tighter than body |

Letter spacing guidance:

- Headings: `0` to `-0.01em` (default or slightly tight)
- Body: `0` (default)
- Overlines: `0.06em–0.08em` (tracked out, uppercase)
- Buttons: `0.01em–0.02em` (slightly tracked)

---

## Numeric Display

With a single font family, numeric data no longer switches to a monospace face. Instead, use tabular figures to maintain column alignment:

```css
.data-table, .kpi-value, .sensor-reading {
  font-family: var(--font-family-default);
  font-variant-numeric: tabular-nums lining-nums;
}
```

### KPI / Sensor Values

KPI values use `heading-lg` (24px) at Bold (700) weight. For extra-large hero KPIs, scale up to 32–40px using custom sizing — but keep the same family and weight.

```css
.kpi-value {
  font-family: var(--font-family-default);
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-lg); /* 24px baseline */
  font-variant-numeric: tabular-nums lining-nums;
}

.kpi-value--hero {
  font-size: 40px; /* Override for hero-level KPIs */
}
```

### Units and Values

Keep the full numeric expression (value + unit) in Aeonik. No font switching mid-string:

- ✓ `296 W` · `3.43 W/kg` · `€3,500/year` · `20+ kHz`

---

## Fallback Stack

```css
:root {
  --font-family-default: 'Aeonik', -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

If Aeonik fails to load, the fallback renders through the standard system font stack. The metrics are close enough that layout shift is minimal.

---

## CSS Implementation

```css
/* ================================================
   1. Font Declaration
   ================================================ */

/* Note: Aeonik is a commercial font. Host the .woff2 files
   on the Samotics CDN or include via the font provider's
   embed code. Replace the src URL below with the actual
   hosted path. */

@font-face {
  font-family: 'Aeonik';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/fonts/aeonik-regular.woff2') format('woff2');
}

@font-face {
  font-family: 'Aeonik';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('/fonts/aeonik-bold.woff2') format('woff2');
}

/* ================================================
   2. Design Tokens
   ================================================ */

:root {
  /* Family */
  --font-family-default: 'Aeonik', -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;

  /* Weights */
  --font-weight-regular: 400;
  --font-weight-bold:    700;

  /* Heading scale */
  --font-size-heading-lg: 24px;
  --font-size-heading-md: 20px;
  --font-size-heading-sm: 16px;
  --font-size-heading-xs: 14px;

  /* Body scale */
  --font-size-body-lg: 16px;
  --font-size-body-md: 14px;
  --font-size-body-sm: 12px;

  /* Line Heights */
  --lh-tight:   1.2;
  --lh-snug:    1.3;
  --lh-normal:  1.4;
  --lh-relaxed: 1.5;
  --lh-loose:   1.6;

  /* Letter Spacing */
  --tracking-tight:   -0.01em;
  --tracking-normal:  0;
  --tracking-wide:    0.02em;
  --tracking-overline: 0.08em;

  /* Max Line Widths */
  --measure-narrow: 45ch;
  --measure-base:   65ch;
  --measure-wide:   75ch;
}

/* ================================================
   3. Base Styles
   ================================================ */

body {
  font-family: var(--font-family-default);
  font-weight: var(--font-weight-regular);
  font-size: var(--font-size-body-md);  /* 14px */
  line-height: var(--lh-relaxed);
  color: var(--color-text-default, #1F1F33);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ================================================
   4. Heading Hierarchy
   ================================================ */

h1 {
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-lg);  /* 24px */
  line-height: var(--lh-tight);
  letter-spacing: var(--tracking-tight);
}

h2 {
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-md);  /* 20px */
  line-height: var(--lh-snug);
  letter-spacing: var(--tracking-normal);
}

h3 {
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-sm);  /* 16px */
  line-height: var(--lh-snug);
  letter-spacing: var(--tracking-normal);
}

h4 {
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-xs);  /* 14px */
  line-height: var(--lh-normal);
  letter-spacing: var(--tracking-normal);
}

/* ================================================
   5. Body & Supporting Styles
   ================================================ */

.lead {
  font-weight: var(--font-weight-regular);
  font-size: var(--font-size-body-lg);  /* 16px */
  line-height: var(--lh-loose);
  max-width: var(--measure-base);
}

.body-small, small {
  font-size: var(--font-size-body-sm);  /* 12px */
  line-height: var(--lh-normal);
}

.caption {
  font-size: var(--font-size-body-sm);  /* 12px */
  line-height: var(--lh-normal);
  letter-spacing: var(--tracking-wide);
  color: var(--color-text-disabled, #6B6B7F);
}

.overline {
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-xs);  /* 14px */
  line-height: 1.0;
  letter-spacing: var(--tracking-overline);
  text-transform: uppercase;
}

.cta, button {
  font-family: var(--font-family-default);
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-sm);  /* 16px */
  line-height: 1.0;
  letter-spacing: var(--tracking-wide);
}

/* ================================================
   6. Data Display Styles
   ================================================ */

.data-table td,
.data-table th {
  font-family: var(--font-family-default);
  font-size: var(--font-size-body-md);  /* 14px */
  line-height: var(--lh-relaxed);
  font-variant-numeric: tabular-nums lining-nums;
}

.data-table th {
  font-weight: var(--font-weight-bold);
}

.data-table td {
  font-weight: var(--font-weight-regular);
}

.kpi-value, .sensor-value {
  font-family: var(--font-family-default);
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-heading-lg);  /* 24px */
  line-height: var(--lh-tight);
  font-variant-numeric: tabular-nums lining-nums;
}

/* ================================================
   7. Responsive Scale (Mobile: ≤768px)
   ================================================ */

/* The scale is already compact (24px max heading).
   On mobile, reduce heading-lg to 20px and shift
   body-md to 14px (unchanged). Minimal adjustment needed. */

@media (max-width: 768px) {
  h1 { font-size: var(--font-size-heading-md); }  /* 20px */
  h2 { font-size: var(--font-size-heading-sm); }  /* 16px */
  h3 { font-size: var(--font-size-heading-xs); }  /* 14px */
  .kpi-value, .sensor-value { font-size: var(--font-size-heading-md); }  /* 20px */
}
```

---

## Mapping from Previous System

| Previous | New | Notes |
|---|---|---|
| IBM Plex Sans (all weights 100–700) | Aeonik Regular (400) | Single sans-serif family |
| IBM Plex Sans Bold (700) | Aeonik Bold (700) | Same weight value |
| IBM Plex Sans Semibold (600) | Aeonik Bold (700) | Collapsed — no semibold in new system |
| IBM Plex Sans Medium (500) | Aeonik Regular (400) or Bold (700) | Choose by context |
| IBM Plex Sans Light (300) | Aeonik Regular (400) | Collapsed — no light weight |
| JetBrains Mono (all contexts) | Aeonik + tabular figures | No more monospace family |
| H1 at 64px | heading-lg at 24px | Dramatically smaller scale |
| H2 at 48px | heading-md at 20px | Dramatically smaller scale |
| Body at 16px | body-md at 14px | Slightly smaller default |
| Body Large at 18px | body-lg at 16px | Slightly smaller |
| KPI at 32px (Mono) | heading-lg at 24px (Aeonik) | Smaller, same family |
| Major Third ratio (1.250) | Fixed token sizes | No mathematical scale |
| 4 font files (2 Sans + 2 Mono) | 2 font files (Regular + Bold) | Smaller payload |

---

## Usage Decision Tree

**Is it a heading, section title, or button label?**
→ Aeonik Bold (700). Choose size from heading-lg through heading-xs.

**Is it body copy, a description, or a form label?**
→ Aeonik Regular (400). Choose size from body-lg through body-sm.

**Is it a data table, KPI, or numeric display?**
→ Aeonik Bold (700) for values. Regular (400) for labels. Apply `tabular-nums lining-nums`.

**Is it an overline?**
→ Aeonik Bold (700) at heading-xs (14px). Uppercase. Letter-spacing 0.08em.

**Is it a caption or footnote?**
→ Aeonik Regular (400) at body-sm (12px).

---

## Quality Checklist

Before shipping any page or component, verify:

- [ ] Body text does not exceed 75 characters per line on desktop
- [ ] Headings create a clear hierarchy when scanned without reading
- [ ] Buttons are immediately distinguishable from body text (Bold vs Regular)
- [ ] Data tables use tabular figures for vertical alignment
- [ ] Aeonik loads in both weights (400 and 700) — check network tab
- [ ] Fallback stack renders acceptably if Aeonik fails to load
- [ ] All text meets WCAG 2.1 AA contrast ratio (4.5:1 body, 3:1 large text)
- [ ] KPI values are the most visually prominent element on dashboards
- [ ] Non-Latin characters (é, ö, ñ, ß) render correctly in all contexts
- [ ] No semibold, medium, or light weights appear anywhere — only 400 and 700

---

## What This System Does Not Cover

- **Color palette and brand colors.** Defined in samotics-color-system.md.
- **Logo typography.** The Samotics wordmark has its own typeface.
- **Print materials.** This spec is optimized for screen.
- **Icon style.** Phosphor Icons (regular variant). Separate from typography.
- **PPTX presentations.** Presentations use Calibri (stand-in for Aeonik) + Consolas. See the PPTX Design System.

---

*One font. Two weights. Size and spacing do the rest. That's the system.*
