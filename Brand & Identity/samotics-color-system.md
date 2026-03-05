# Samotics Website Color System

*Design token specification for samotics.com — February 2026*
*Input file for website generation. All values are final unless noted.*

---

## Design Principle

Visual restraint signals engineering discipline. The full brand palette contains 17 swatches. The website should feel like it uses 5. Every color on a page must have a job. If it doesn't carry meaning, it doesn't appear.

---

## Core Palette (use on every page)

| Role | Name | Hex | Usage |
|---|---|---|---|
| **Primary** | Space Cadet | `#1F1F33` | Hero sections, navigation, footer, primary headings on light backgrounds |
| **Accent** | Samotics Orange | `#FF5429` | Primary CTAs only. One per viewport. Never as text on white. |
| **Accent (AA-safe)** | Samotics Orange Dark | `#D7411B` | Orange text on white backgrounds, small orange UI elements |
| **Interactive** | Midnight Frequency | `#005CBA` | Links, interactive elements, info indicators |
| **Surface Primary** | White | `#FFFFFF` | Main page background, card surfaces |
| **Surface Secondary** | Seashell | `#F8F5F2` | Alternating sections, proof strips, subtle differentiation |
| **Text Primary** | Near Black | `#111111` | Body copy, headings on light backgrounds |
| **Text Secondary** | Comet | `#6B6B7F` | Captions, metadata, secondary labels, timestamps |

---

## Extended Palette (use only when carrying specific meaning)

| Role | Name | Hex | When to use |
|---|---|---|---|
| **Teal** | North Sea Main | `#0098AC` | Product feature sections, SAM4-specific UI elements |
| **Teal (AA-safe)** | North Sea AA | `#218291` | Teal text on white backgrounds |
| **Teal Dark** | North Sea Dark | `#006C6C` | Secondary CTAs (outline style), teal text needing higher contrast |
| **Teal Light** | North Sea Light | `#BAFFFF` | Teal tinted backgrounds (always with `#111111` text) |
| **Blue Light** | Midnight Frequency Light | `#B3DAFF` | Info callout backgrounds, technical highlight strips |
| **Blue Dark** | Midnight Frequency Dark | `#004179` | Deep blue for high-contrast technical sections |
| **Purple** | Roman Purple Main | `#BA0068` | Partner/co-brand moments, premium feature highlights |
| **Purple Light** | Roman Purple Light | `#FFD3F6` | Purple tinted backgrounds (always with `#111111` text) |
| **Purple Dark** | Roman Purple Dark | `#70003D` | Deep purple for high-contrast contexts |
| **Gold** | Resistor Gold Main | `#FAC91F` | Metric highlights, badges, attention markers |
| **Gold Light** | Resistor Gold Light | `#FDF1C1` | Gold tinted backgrounds (always with `#111111` text) |
| **Gold Dark** | Resistor Gold Dark | `#DF9300` | Gold labels and badges with `#111111` text |

---

## Semantic Colors

Map meaning to color. Components reference these tokens, never raw hex values.

| Token | Hex | Usage |
|---|---|---|
| `--color-success` | `#006C6C` | Healthy asset status, positive confirmations, success states |
| `--color-success-bg` | `#BAFFFF` | Success background tint (with `#111111` text) |
| `--color-warning` | `#DF9300` | Attention required, degraded performance, amber alerts |
| `--color-warning-bg` | `#FDF1C1` | Warning background tint (with `#111111` text) |
| `--color-error` | `#BA0068` | Failure, critical alerts, error states |
| `--color-error-bg` | `#FFD3F6` | Error background tint (with `#111111` text) |
| `--color-info` | `#005CBA` | Informational, links, help text, neutral status |
| `--color-info-bg` | `#B3DAFF` | Info background tint (with `#111111` text) |
| `--color-neutral` | `#6B6B7F` | Disabled, inactive, placeholder, secondary |
| `--color-neutral-bg` | `#F8F5F2` | Neutral background tint |

**Rule:** Color is never the only signal for status. Every semantic color must be paired with an icon, label, or pattern. This is a WCAG requirement and a practical one — dashboards are read on plant floor monitors in poor lighting.

---

## Background System

| Token | Hex | Use case |
|---|---|---|
| `--bg-primary` | `#FFFFFF` | Default page background, cards, modals |
| `--bg-secondary` | `#F8F5F2` | Alternating sections, sidebar, proof strips |
| `--bg-dark` | `#1F1F33` | Hero sections, footer, navigation overlays |
| `--bg-dark-elevated` | `#2A2A42` | Cards/elements on dark backgrounds (slight lift) |
| `--bg-accent` | `#FF5429` | CTA buttons only |
| `--bg-callout-info` | `#B3DAFF` | Technical callout boxes, info banners |
| `--bg-callout-success` | `#BAFFFF` | Positive result callouts |
| `--bg-callout-warning` | `#FDF1C1` | Warning callouts |
| `--bg-callout-error` | `#FFD3F6` | Critical alert callouts |
| `--bg-highlight` | `#FAC91F` | Metric badges, KPI highlights (small areas only) |

---

## Text Colors

| Token | Hex | Use case | Minimum background contrast |
|---|---|---|---|
| `--text-primary` | `#111111` | Body copy | Use on White, Seashell, all Light tints |
| `--text-lead` | `#1F1F33` | Lead/intro paragraphs and headings. Heavier than body copy — uses Space Cadet for visual hierarchy | 16.1:1 on White, 14.8:1 on Seashell |
| `--text-secondary` | `#6B6B7F` | Captions, metadata, timestamps, short labels. Never for paragraph-length body content — use `--text-primary` instead | Use on White, Seashell only (5.2:1) |
| `--text-tertiary` | `#9A9AAE` | Placeholder text, disabled labels | Use on White only, large text only (3.1:1) |
| `--text-on-dark` | `#FFFFFF` | All text on Space Cadet or dark backgrounds | 16.1:1 on Space Cadet |
| `--text-on-dark-muted` | `#B0B0C8` | Secondary text on dark backgrounds | 7.2:1 on Space Cadet |
| `--text-on-accent` | `#111111` | Text on Samotics Orange buttons | 5.9:1 on Orange |
| `--text-link` | `#005CBA` | Inline links on white/light backgrounds | 6.5:1 on White |
| `--text-link-on-dark` | `#B3DAFF` | Inline links on dark backgrounds | 8.9:1 on Space Cadet |

---

## Interaction States

All interactive elements follow this state progression. Shifts are consistent across the system.

### Buttons — Primary (Orange CTA)

| State | Background | Text | Border |
|---|---|---|---|
| Default | `#FF5429` | `#111111` | none |
| Hover | `#D7411B` | `#FFFFFF` | none |
| Active / Pressed | `#A33013` | `#FFFFFF` | none |
| Focus | `#FF5429` | `#111111` | `3px solid #005CBA` (focus ring) |
| Disabled | `#E0D8D4` | `#9A9AAE` | none |

### Buttons — Secondary (Outline)

| State | Background | Text | Border |
|---|---|---|---|
| Default | `transparent` | `#006C6C` | `2px solid #006C6C` |
| Hover | `#006C6C` | `#FFFFFF` | `2px solid #006C6C` |
| Active / Pressed | `#004D4D` | `#FFFFFF` | `2px solid #004D4D` |
| Focus | `transparent` | `#006C6C` | `3px solid #005CBA` (focus ring) |
| Disabled | `transparent` | `#9A9AAE` | `2px solid #E0D8D4` |

### Buttons — Ghost (on dark backgrounds)

| State | Background | Text | Border |
|---|---|---|---|
| Default | `transparent` | `#FFFFFF` | `2px solid rgba(255,255,255,0.4)` |
| Hover | `rgba(255,255,255,0.1)` | `#FFFFFF` | `2px solid rgba(255,255,255,0.8)` |
| Active / Pressed | `rgba(255,255,255,0.15)` | `#FFFFFF` | `2px solid #FFFFFF` |
| Focus | `transparent` | `#FFFFFF` | `3px solid #B3DAFF` (focus ring) |
| Disabled | `transparent` | `rgba(255,255,255,0.3)` | `2px solid rgba(255,255,255,0.15)` |

### Links

| State | Color on light | Color on dark |
|---|---|---|
| Default | `#005CBA` | `#B3DAFF` |
| Hover | `#004179` | `#FFFFFF` |
| Active | `#004179` | `#FFFFFF` |
| Visited | `#70003D` | `#FFD3F6` |
| Focus | `#005CBA` + `3px solid #005CBA` outline | `#B3DAFF` + `3px solid #B3DAFF` outline |

### Form Inputs

| State | Border | Background | Text |
|---|---|---|---|
| Default | `1px solid #C4C4D0` | `#FFFFFF` | `#111111` |
| Hover | `1px solid #6B6B7F` | `#FFFFFF` | `#111111` |
| Focus | `2px solid #005CBA` | `#FFFFFF` | `#111111` |
| Error | `2px solid #BA0068` | `#FFFFFF` | `#111111` |
| Disabled | `1px solid #E0D8D4` | `#F8F5F2` | `#9A9AAE` |
| Placeholder text | — | — | `#9A9AAE` |

---

## Gradients

Use sparingly. Gradients are reserved for hero sections and premium feature highlights. Never on body content areas.

| Name | CSS | Use case |
|---|---|---|
| **Hero Depth** | `linear-gradient(180deg, #1F1F33 0%, #2A2A42 100%)` | Hero section background — adds subtle depth to Space Cadet |
| **Hero Radial** | `radial-gradient(ellipse at 30% 50%, #004179 0%, #1F1F33 70%)` | Hero with subtle blue glow — signals technology/intelligence |
| **CTA Glow** | `linear-gradient(135deg, #FF5429 0%, #D7411B 100%)` | Primary CTA hover emphasis — subtle warmth shift |
| **Section Fade** | `linear-gradient(180deg, #FFFFFF 0%, #F8F5F2 100%)` | Transition from white section to seashell section |
| **Dark to Content** | `linear-gradient(180deg, #1F1F33 0%, #FFFFFF 100%)` | Transition from dark hero to white content — use over 120px+ height |
| **Tech Accent** | `linear-gradient(135deg, #005CBA 0%, #0098AC 100%)` | Technical feature highlights, small accent bars, chart headers |

**Gradient rules:**
- Never place text directly on a gradient without a solid-color fallback that meets contrast requirements.
- Never use gradients on callout or status backgrounds — those must be flat semantic colors.
- Maximum one gradient per viewport. More than that reads as decoration, not design.

---

## Border and Divider System

| Token | Value | Use case |
|---|---|---|
| `--border-light` | `1px solid #E8E4E0` | Card borders, section dividers on white |
| `--border-medium` | `1px solid #C4C4D0` | Input fields, table borders |
| `--border-strong` | `1px solid #6B6B7F` | Active/emphasized borders |
| `--border-on-dark` | `1px solid rgba(255,255,255,0.15)` | Dividers on dark backgrounds |
| `--border-accent` | `2px solid #FF5429` | Left-border accent on featured cards, pull quotes |
| `--border-focus` | `3px solid #005CBA` | Focus ring — all interactive elements |

---

## Shadow System

| Token | Value | Use case |
|---|---|---|
| `--shadow-sm` | `0 1px 3px rgba(31,31,51,0.08)` | Cards, dropdowns |
| `--shadow-md` | `0 4px 12px rgba(31,31,51,0.10)` | Elevated cards, modals |
| `--shadow-lg` | `0 12px 32px rgba(31,31,51,0.14)` | Popovers, floating elements |
| `--shadow-orange` | `0 4px 16px rgba(255,84,41,0.25)` | CTA hover glow effect |

Shadow color is always derived from Space Cadet (#1F1F33), never pure black. This keeps shadows warm and consistent with the palette.

---

## Accessibility Rules (non-negotiable)

1. **Samotics Orange (#FF5429):** Never as text on white. Never as background with white text at normal size. Use `#D7411B` for AA-safe orange text on white.
2. **North Sea Main (#0098AC):** Same rules as orange. Use `#218291` for AA-safe teal text on white.
3. **Resistor Gold Main (#FAC91F):** Background use only, always with `#111111` text. Never as text on any background.
4. **All Light tints:** Background only, always with `#111111` text. Never place white text on light tints.
5. **Comet (#6B6B7F):** As text on white: AA-compliant (5.2:1). As background with white text: only for large text (3.6:1). Do not use for normal body text on Comet backgrounds.
6. **Focus indicators:** Every interactive element must show a visible focus ring (`3px solid #005CBA` on light, `3px solid #B3DAFF` on dark). Never remove outline on `:focus-visible`.
7. **Color is never the only signal.** Status indicators (success/warning/error) must include an icon or text label alongside color.

---

## Page Composition Reference

Typical page structure using this system:

```
┌─────────────────────────────────────────────┐
│  NAVIGATION          bg: #FFFFFF            │
│  text: #111111       links: #005CBA         │
│  CTA: bg #FF5429, text #111111              │
├─────────────────────────────────────────────┤
│  HERO                bg: #1F1F33            │
│  H1: #FFFFFF         Lead: #B0B0C8          │
│  Primary CTA: bg #FF5429, text #111111      │
│  Ghost CTA: border rgba(255,255,255,0.4)    │
├─────────────────────────────────────────────┤
│  SOCIAL PROOF        bg: #F8F5F2            │
│  Logos/stats: #111111                        │
│  Card: bg #FFFFFF, border #E8E4E0           │
├─────────────────────────────────────────────┤
│  FEATURES            bg: #FFFFFF            │
│  H2: #1F1F33         Body: #111111          │
│  Accent bar: #FF5429 (left border, 2px)     │
│  Links: #005CBA                              │
├─────────────────────────────────────────────┤
│  TECHNICAL CALLOUT   bg: #B3DAFF            │
│  Icon: #005CBA       H3: #004179            │
│  Body: #111111                               │
├─────────────────────────────────────────────┤
│  CASE STUDY          bg: #FFFFFF            │
│  Metric highlight: bg #FAC91F, text #111111 │
│  Quote accent: left border #BA0068          │
├─────────────────────────────────────────────┤
│  CTA SECTION         bg: #1F1F33            │
│  H2: #FFFFFF         Body: #B0B0C8          │
│  Primary CTA: bg #FF5429, text #111111      │
├─────────────────────────────────────────────┤
│  FOOTER              bg: #1F1F33            │
│  Text: #B0B0C8       Links: #B3DAFF         │
│  Dividers: rgba(255,255,255,0.15)           │
└─────────────────────────────────────────────┘
```

---

## CSS Custom Properties (complete token set)

```css
:root {
  /* Core */
  --color-primary:         #1F1F33;
  --color-accent:          #FF5429;
  --color-accent-safe:     #D7411B;
  --color-accent-deep:     #A33013;
  --color-interactive:     #005CBA;
  --color-interactive-dark:#004179;

  /* Extended */
  --color-teal:            #0098AC;
  --color-teal-safe:       #218291;
  --color-teal-dark:       #006C6C;
  --color-teal-light:      #BAFFFF;
  --color-purple:          #BA0068;
  --color-purple-light:    #FFD3F6;
  --color-purple-dark:     #70003D;
  --color-gold:            #FAC91F;
  --color-gold-light:      #FDF1C1;
  --color-gold-dark:       #DF9300;
  --color-blue-light:      #B3DAFF;

  /* Semantic */
  --color-success:         #006C6C;
  --color-success-bg:      #BAFFFF;
  --color-warning:         #DF9300;
  --color-warning-bg:      #FDF1C1;
  --color-error:           #BA0068;
  --color-error-bg:        #FFD3F6;
  --color-info:            #005CBA;
  --color-info-bg:         #B3DAFF;

  /* Backgrounds */
  --bg-primary:            #FFFFFF;
  --bg-secondary:          #F8F5F2;
  --bg-dark:               #1F1F33;
  --bg-dark-elevated:      #2A2A42;

  /* Text */
  --text-lead:             #1F1F33;
  --text-primary:          #111111;
  --text-secondary:        #6B6B7F;
  --text-tertiary:         #9A9AAE;
  --text-on-dark:          #FFFFFF;
  --text-on-dark-muted:    #B0B0C8;
  --text-on-accent:        #111111;
  --text-link:             #005CBA;
  --text-link-hover:       #004179;
  --text-link-on-dark:     #B3DAFF;
  --text-link-visited:     #70003D;

  /* Borders */
  --border-light:          #E8E4E0;
  --border-medium:         #C4C4D0;
  --border-strong:         #6B6B7F;
  --border-focus:          #005CBA;
  --border-focus-on-dark:  #B3DAFF;
  --border-accent:         #FF5429;

  /* Disabled */
  --color-disabled-bg:     #E0D8D4;
  --color-disabled-text:   #9A9AAE;
  --color-disabled-border: #E0D8D4;

  /* Shadows (Space Cadet base, never pure black) */
  --shadow-sm:  0 1px 3px rgba(31,31,51,0.08);
  --shadow-md:  0 4px 12px rgba(31,31,51,0.10);
  --shadow-lg:  0 12px 32px rgba(31,31,51,0.14);
  --shadow-cta: 0 4px 16px rgba(255,84,41,0.25);

  /* Gradients */
  --gradient-hero:         linear-gradient(180deg, #1F1F33 0%, #2A2A42 100%);
  --gradient-hero-radial:  radial-gradient(ellipse at 30% 50%, #004179 0%, #1F1F33 70%);
  --gradient-cta:          linear-gradient(135deg, #FF5429 0%, #D7411B 100%);
  --gradient-section-fade: linear-gradient(180deg, #FFFFFF 0%, #F8F5F2 100%);
  --gradient-dark-to-light:linear-gradient(180deg, #1F1F33 0%, #FFFFFF 100%);
  --gradient-tech:         linear-gradient(135deg, #005CBA 0%, #0098AC 100%);
}
```

---

*Seven functional colors. Everything else earns its place or stays off the page.*
