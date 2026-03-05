# Samotics Typography System

*Design specification for samotics.com — February 2026*

---

## Design Intent

Samotics is building a new industrial category: Inaccessible Asset Monitoring. The typography must do two things at once. It must project the authority of an engineering standard — convincing reliability engineers, maintenance leads, and procurement teams that this category is real. And it must render complex technical data (sensor readings, ROI calculations, fault frequencies) with absolute clarity.

The system uses two typeface families. One for narrative. One for data. No exceptions.

---

## Type Families

### Primary: IBM Plex Sans (Variable)

**Role:** All narrative content — headlines, body copy, lead paragraphs, CTAs, navigation, UI elements.

**Why:** IBM Plex is a Grotesque sans-serif designed to express the relationship between human intent and machine output. It carries structural rigidity and neutrality — the visual language of global infrastructure — without the coldness of purely geometric fonts. It reads as "engineering standard," not "startup." That matters when your buyer is a 50-year-old reliability engineer deciding whether to trust your platform with a £2M asset.

**Key characteristics:**
- Tall x-height for screen legibility
- Open apertures for readability at small sizes
- Variable format: single file covers weights 100–700
- Full latin-ext character support for multilingual deployment (EN, DE, NL, FR, ES, IT)

### Secondary: JetBrains Mono (Variable)

**Role:** All technical and numeric content — data tables, sensor values, serial numbers, ROI figures, code snippets, CLI documentation, dashboard labels, hardware specs.

**Why:** JetBrains Mono was designed for people who stare at data all day. It has superior character disambiguation (1/l/I and 0/O are instantly distinguishable), excellent tabular figures for vertical column alignment, and variable weight support. It reads as a precision instrument — which is exactly how SAM4 data should feel.

**Key characteristics:**
- Purpose-built for technical readability
- Increased character height within the same bounding box (1.5× taller lowercase than most monospace fonts)
- Native tabular figures — no CSS overrides needed for column alignment
- Variable format: single file covers weights 100–800
- Ligature support (optional, disable for raw data display)

---

## Font File Manifest

All files are variable .woff2 format hosted on Google Fonts CDN.

| Family | Weight Range | Style | Format | URL |
|---|---|---|---|---|
| IBM Plex Sans | 100–700 | Normal | .woff2 | https://fonts.gstatic.com/s/ibmplexsans/v19/zYX9KVElMYYaJe8bpLHnCwDKjQ76AIFsdP3pB4dqzDjftXmSUWz_3A.woff2 |
| IBM Plex Sans | 100–700 | Italic | .woff2 | https://fonts.gstatic.com/s/ibmplexsans/v19/zYX7KVElMYYaJe8bpLHnCwDKhdzeDaVwdO_pB4dqzDjftXmSUWz_3KzXpg.woff2 |
| JetBrains Mono | 100–800 | Normal | .woff2 | https://fonts.gstatic.com/s/jetbrainsmono/v18/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKxTOlOTk6OThhvA.woff2 |
| JetBrains Mono | 100–800 | Italic | .woff2 | https://fonts.gstatic.com/s/jetbrainsmono/v18/tDbX2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO-Lf1OQk6OThhvAWV8.woff2 |

**Fallback stacks:**
- Sans: `'IBM Plex Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- Mono: `'JetBrains Mono', "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace`

---

## Desktop Typographic Scale

Scale ratio: 1.250 (Major Third). Base size: 16px (1rem).

| Style | Family | Weight | Size (px) | Size (rem) | Line Height | Letter Spacing | Max Width |
|---|---|---|---|---|---|---|---|
| H1 — Category Hero | Sans | 700 | 64 | 4.000 | 1.10 | −0.02em | 15 ch |
| H2 — Section | Sans | 600 | 48 | 3.000 | 1.20 | −0.01em | 25 ch |
| H3 — Feature | Sans | 600 | 32 | 2.000 | 1.30 | 0.00em | 40 ch |
| H4 — Sub-feature | Sans | 500 | 24 | 1.500 | 1.40 | 0.00em | 55 ch |
| H5 — Table Header | Sans | 600 | 20 | 1.250 | 1.40 | 0.01em | — |
| H6 — Metadata | Sans | 600 | 16 | 1.000 | 1.50 | 0.02em | — |
| Lead / Intro | Sans | 400 | 20 | 1.250 | 1.60 | 0.00em | 60 ch |
| Body Large | Sans | 400 | 18 | 1.125 | 1.60 | 0.00em | 65 ch |
| Body | Sans | 400 | 16 | 1.000 | 1.60 | 0.00em | 75 ch |
| Body Small | Sans | 400 | 14 | 0.875 | 1.50 | 0.01em | 70 ch |
| Caption / Footnote | Sans | 400 | 12 | 0.750 | 1.40 | 0.02em | — |
| Button / CTA | Sans | 600 | 16 | 1.000 | 1.00 | 0.02em | — |
| Overline | Sans | 600 | 16 | 1.000 | 1.00 | 0.10em | — |
| Data Table Cell | Mono | 400 | 14 | 0.875 | 1.50 | 0.00em | — |
| Data Table Header | Mono | 600 | 14 | 0.875 | 1.40 | 0.02em | — |
| Sensor Value / KPI | Mono | 700 | 32 | 2.000 | 1.10 | −0.01em | — |
| Dashboard Label | Mono | 500 | 12 | 0.750 | 1.00 | 0.05em | — |
| Code / CLI | Mono | 400 | 14 | 0.875 | 1.50 | 0.00em | — |
| Serial Number / Spec | Mono | 400 | 13 | 0.8125 | 1.40 | 0.02em | — |

---

## Mobile Typographic Scale

Scale ratio: 1.200 (Minor Third). Base size: 16px (1rem).

| Style | Family | Weight | Size (px) | Size (rem) | Line Height | Letter Spacing |
|---|---|---|---|---|---|---|
| H1 — Category Hero | Sans | 700 | 40 | 2.500 | 1.20 | −0.01em |
| H2 — Section | Sans | 600 | 32 | 2.000 | 1.20 | −0.01em |
| H3 — Feature | Sans | 600 | 24 | 1.500 | 1.30 | 0.00em |
| H4 — Sub-feature | Sans | 600 | 20 | 1.250 | 1.40 | 0.00em |
| H5 — Table Header | Sans | 600 | 18 | 1.125 | 1.40 | 0.00em |
| H6 — Metadata | Sans | 600 | 16 | 1.000 | 1.40 | 0.00em |
| Lead / Intro | Sans | 400 | 18 | 1.125 | 1.50 | 0.00em |
| Body Large | Sans | 400 | 16 | 1.000 | 1.60 | 0.00em |
| Body | Sans | 400 | 16 | 1.000 | 1.60 | 0.00em |
| Body Small | Sans | 400 | 14 | 0.875 | 1.50 | 0.01em |
| Caption / Footnote | Sans | 400 | 12 | 0.750 | 1.40 | 0.02em |
| Button / CTA | Sans | 600 | 16 | 1.000 | 1.00 | 0.02em |
| Overline | Sans | 600 | 14 | 0.875 | 1.00 | 0.08em |
| Data Table Cell | Mono | 400 | 13 | 0.8125 | 1.50 | 0.00em |
| Data Table Header | Mono | 600 | 13 | 0.8125 | 1.40 | 0.02em |
| Sensor Value / KPI | Mono | 700 | 24 | 1.500 | 1.10 | −0.01em |
| Dashboard Label | Mono | 500 | 11 | 0.6875 | 1.00 | 0.05em |
| Code / CLI | Mono | 400 | 13 | 0.8125 | 1.50 | 0.00em |

---

## Numeric Display Rules

Technical data is the primary content type for SAM4 users. Numbers must be unambiguous and scannable.

### Tabular alignment

All numeric data in tables, dashboards, and KPI displays uses tabular figures so values align vertically. JetBrains Mono provides this natively. No CSS override required — but for defensive consistency, apply:

```css
.data-table, .kpi-value, .sensor-reading {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums lining-nums;
}
```

### Character disambiguation

JetBrains Mono distinguishes 1/l/I and 0/O by default. For serial numbers and critical hardware specs where absolute clarity is required, also enable the slashed zero:

```css
.serial-number, .hardware-spec {
  font-family: var(--font-mono);
  font-feature-settings: "zero" 1;
}
```

### Ligatures

JetBrains Mono includes coding ligatures (e.g., `>=` renders as a single glyph). Disable ligatures in raw data display contexts where each character must be individually legible:

```css
.raw-data, .sensor-output {
  font-variant-ligatures: none;
}
```

Keep ligatures enabled in code documentation and CLI examples where they aid readability.

### Units and values

Always set the numeric value in Mono and keep the unit attached without a line break:

- ✓ `296 W` · `3.43 W/kg` · `€3,500/year` · `20+ kHz`
- ✗ Do not set units in Sans while the number is in Mono. Keep the full expression in one family.

---

## CSS Implementation

```css
/* ================================================
   1. Font Declarations
   ================================================ */

@font-face {
  font-family: 'IBM Plex Sans';
  font-style: normal;
  font-weight: 100 700;
  font-display: swap;
  src: url('https://fonts.gstatic.com/s/ibmplexsans/v19/zYX9KVElMYYaJe8bpLHnCwDKjQ76AIFsdP3pB4dqzDjftXmSUWz_3A.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193,
    U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: 'IBM Plex Sans';
  font-style: italic;
  font-weight: 100 700;
  font-display: swap;
  src: url('https://fonts.gstatic.com/s/ibmplexsans/v19/zYX7KVElMYYaJe8bpLHnCwDKhdzeDaVwdO_pB4dqzDjftXmSUWz_3KzXpg.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193,
    U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: 'JetBrains Mono';
  font-style: normal;
  font-weight: 100 800;
  font-display: swap;
  src: url('https://fonts.gstatic.com/s/jetbrainsmono/v18/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKxTOlOTk6OThhvA.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193,
    U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: 'JetBrains Mono';
  font-style: italic;
  font-weight: 100 800;
  font-display: swap;
  src: url('https://fonts.gstatic.com/s/jetbrainsmono/v18/tDbX2o-flEEny0FZhsfKu5WU4xD-IQ-PuZJJXxfpAO-Lf1OQk6OThhvAWV8.woff2') format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193,
    U+2212, U+2215, U+FEFF, U+FFFD;
}

/* ================================================
   2. Design Tokens
   ================================================ */

:root {
  /* Families */
  --font-sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: 'JetBrains Mono', "SFMono-Regular", Consolas,
    "Liberation Mono", Menlo, Courier, monospace;

  /* Weights */
  --weight-light: 300;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;

  /* Line Heights */
  --lh-tight: 1.1;
  --lh-snug: 1.2;
  --lh-normal: 1.4;
  --lh-relaxed: 1.6;

  /* Letter Spacing */
  --tracking-tight: -0.02em;
  --tracking-snug: -0.01em;
  --tracking-normal: 0;
  --tracking-wide: 0.02em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.10em;

  /* Max Line Widths */
  --measure-narrow: 40ch;
  --measure-base: 65ch;
  --measure-wide: 75ch;
}

/* ================================================
   3. Base Styles
   ================================================ */

body {
  font-family: var(--font-sans);
  font-weight: var(--weight-regular);
  font-size: 1rem;            /* 16px */
  line-height: var(--lh-relaxed);
  color: #1a1a1a;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ================================================
   4. Heading Hierarchy
   ================================================ */

h1 {
  font-weight: var(--weight-bold);
  font-size: 4rem;            /* 64px */
  line-height: var(--lh-tight);
  letter-spacing: var(--tracking-tight);
}

h2 {
  font-weight: var(--weight-semibold);
  font-size: 3rem;            /* 48px */
  line-height: var(--lh-snug);
  letter-spacing: var(--tracking-snug);
}

h3 {
  font-weight: var(--weight-semibold);
  font-size: 2rem;            /* 32px */
  line-height: 1.3;
  letter-spacing: var(--tracking-normal);
}

h4 {
  font-weight: var(--weight-medium);
  font-size: 1.5rem;          /* 24px */
  line-height: var(--lh-normal);
  letter-spacing: var(--tracking-normal);
}

h5 {
  font-weight: var(--weight-semibold);
  font-size: 1.25rem;         /* 20px */
  line-height: var(--lh-normal);
  letter-spacing: 0.01em;
}

h6 {
  font-weight: var(--weight-semibold);
  font-size: 1rem;            /* 16px */
  line-height: 1.5;
  letter-spacing: var(--tracking-wide);
}

/* ================================================
   5. Body & Supporting Styles
   ================================================ */

.lead {
  font-weight: var(--weight-regular);
  font-size: 1.25rem;
  line-height: var(--lh-relaxed);
  color: var(--text-lead, #1F1F33); /* Space Cadet — heavier than body for visual hierarchy */
  max-width: 60ch;
}

.body-large {
  font-size: 1.125rem;
  line-height: var(--lh-relaxed);
  max-width: 65ch;
}

.body-small {
  font-size: 0.875rem;
  line-height: 1.5;
  letter-spacing: 0.01em;
}

.caption {
  font-size: 0.75rem;
  line-height: var(--lh-normal);
  letter-spacing: var(--tracking-wide);
}

.overline {
  font-weight: var(--weight-semibold);
  font-size: 0.875rem;
  line-height: 1.0;
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
}

.cta, button {
  font-family: var(--font-sans);
  font-weight: var(--weight-semibold);
  font-size: 1rem;
  line-height: 1.0;
  letter-spacing: var(--tracking-wide);
}

/* ================================================
   6. Technical Data Styles (JetBrains Mono)
   ================================================ */

.data-table td,
.data-table th {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  line-height: 1.5;
  font-variant-numeric: tabular-nums lining-nums;
}

.data-table th {
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-wide);
}

.data-table td {
  font-weight: var(--weight-regular);
}

.kpi-value, .sensor-value {
  font-family: var(--font-mono);
  font-weight: var(--weight-bold);
  font-size: 2rem;
  line-height: var(--lh-tight);
  letter-spacing: var(--tracking-snug);
  font-variant-numeric: tabular-nums lining-nums;
}

.dashboard-label {
  font-family: var(--font-mono);
  font-weight: var(--weight-medium);
  font-size: 0.75rem;
  line-height: 1.0;
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
}

code, .code-block, .cli {
  font-family: var(--font-mono);
  font-weight: var(--weight-regular);
  font-size: 0.875rem;
  line-height: 1.5;
}

.serial-number, .hardware-spec {
  font-family: var(--font-mono);
  font-weight: var(--weight-regular);
  font-size: 0.8125rem;
  line-height: var(--lh-normal);
  letter-spacing: var(--tracking-wide);
  font-feature-settings: "zero" 1;
}

/* ================================================
   7. Responsive Scale (Mobile: ≤768px)
   ================================================ */

@media (max-width: 768px) {
  h1 { font-size: 2.5rem; line-height: var(--lh-snug); letter-spacing: var(--tracking-snug); }
  h2 { font-size: 2rem; }
  h3 { font-size: 1.5rem; }
  h4 { font-size: 1.25rem; font-weight: var(--weight-semibold); }
  h5 { font-size: 1.125rem; }
  h6 { font-size: 1rem; }
  .lead { font-weight: var(--weight-regular); font-size: 1.125rem; line-height: 1.5; }
  .kpi-value, .sensor-value { font-size: 1.5rem; }
  .dashboard-label { font-size: 0.6875rem; }
  .data-table td, .data-table th { font-size: 0.8125rem; }
  code, .code-block, .cli { font-size: 0.8125rem; }
}
```

---

## Usage Decision Tree

**Is the content a number, measurement, code snippet, or machine-generated value?**
→ Yes: JetBrains Mono. Apply tabular figures. Check if slashed zero is needed.
→ No: IBM Plex Sans.

**Is it a headline, paragraph, CTA, or navigation label?**
→ IBM Plex Sans. Always.

**Is it a data table?**
→ Headers and cell values in JetBrains Mono. Table captions and footnotes in IBM Plex Sans.

**Is it a dashboard KPI or sensor reading?**
→ JetBrains Mono at 700 weight. Large size (32px desktop, 24px mobile). The number is the content — make it dominant.

**Is it a mixed sentence with an inline number?**
→ Keep the full sentence in IBM Plex Sans. Only switch to Mono for standalone numeric displays, tables, and data-first contexts. Inline numbers within body copy stay in Sans for reading flow.

---

## Quality Checklist

Before shipping any page or component, verify:

- [ ] Body text does not exceed 75 characters per line on desktop
- [ ] The character `1` is visually distinct from `l` and `I` in all Mono contexts
- [ ] The character `0` is visually distinct from `O` in serial number displays
- [ ] Numbers in data tables align vertically (tabular figures active)
- [ ] H1 through H6 create a clear hierarchy when scanned without reading
- [ ] Lead paragraphs at 300 weight render crisply on Windows (check ClearType)
- [ ] CTAs at 600 weight are immediately distinguishable from body text
- [ ] No page loads more than 4 font files (2 Sans + 2 Mono, variable format)
- [ ] Fallback stack renders acceptably if web fonts fail to load
- [ ] All text meets WCAG 2.1 AA contrast ratio (4.5:1 body, 3:1 large text)
- [ ] KPI/sensor values in Mono are the most visually prominent element on dashboards
- [ ] Non-Latin characters (é, ö, ñ, ß) render correctly in all contexts

---

## What This System Does Not Cover

- **Color palette and brand colors.** Defined in brand guidelines, not here.
- **Logo typography.** The Samotics wordmark has its own typeface. This system governs the website and documentation only.
- **Print materials.** This spec is optimized for screen. Print may require optical size adjustments.
- **Icon and illustration style.** Separate specification.

---

*Two fonts. Sans for what people read. Mono for what people scan. That's the system.*
