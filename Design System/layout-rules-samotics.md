# Layout Rules: IBM Carbon Grid × Samotics Color System

Design system for samotics.com. Structural foundation from IBM Carbon's 16-column grid. Color and visual execution from the Samotics color system. Where the two conflict, the Samotics color system wins.

---

## 1. Breakpoints & Max Width

Carbon's fluid breakpoint system, unchanged.

| Token | Width | Target |
|-------|-------|--------|
| `sm`  | 320px | Mobile |
| `md`  | 672px | Tablet |
| `lg`  | 1056px | Small laptop |
| `xlg` | 1312px | Standard desktop |
| `max` | 1584px | Large monitor |

**Max content width:** `1584px`. All text, cards, and forms stay within this container.

**Bleed exception:** Background colors, hero sections, and full-width imagery break out to `100vw`. Hero sections use a full-width background photograph with a dark overlay gradient (Space Cadet at 88–35% opacity, left-to-right) to ensure text legibility. Content is left-aligned over the overlay. Product photography and 3D renders pop against the light content sections below.

---

## 2. Grid System

**16-column grid** across all desktop breakpoints.

### Columns by Breakpoint

| Breakpoint | Columns |
|------------|---------|
| `sm` | 4 |
| `md` | 8 |
| `lg` / `xlg` / `max` | 16 |

### Gutters

| Breakpoint | Gutter |
|------------|--------|
| `sm`, `md` | 16px |
| `lg`, `xlg`, `max` | 32px (fixed) |

### Outer Margins

| Breakpoint | Margin |
|------------|--------|
| `sm`, `md` | 16px or 5% |
| `lg`+ | 5% (scales dynamically up to 1584px max, then centers) |

### Asymmetric Layout Rule

Use the 16 columns to create architectural, asymmetric compositions. Example: a heading spanning columns 1–10, a UI card or video in columns 12–16, column 11 empty for visual tension. This asymmetry gives the "engineering precision" feel that matches the Samotics design principle of visual restraint.

---

## 3. Spacing Scale (Padding & Margin)

Carbon's **Base-8 spacing scale**. Vast spacing between sections. Tight spacing within components.

### Token Scale

| Token | Value |
|-------|-------|
| `spacing-01` | 2px |
| `spacing-02` | 4px |
| `spacing-03` | 8px |
| `spacing-04` | 12px |
| `spacing-05` | 16px |
| `spacing-06` | 24px |
| `spacing-07` | 32px |
| `spacing-08` | 48px |
| `spacing-09` | 64px |
| `spacing-10` | 96px |
| `spacing-11` | 128px |
| `spacing-12` | 160px |

### Application Rules

**Macro spacing (section to section):** `spacing-11` (128px) or `spacing-12` (160px). Generous whitespace between distinct page sections. When transitioning between `--bg-primary` and `--bg-secondary` sections, use `--gradient-section-fade` over this gap rather than a hard cut.

**Meso spacing (heading to content):** `spacing-08` (48px) or `spacing-09` (64px). Separates section titles from card grids or body content.

**Micro spacing (within components):** `spacing-05` (16px) or `spacing-06` (24px). Internal padding for cards, forms, inputs.

---

## 4. Header & Navigation

Sticky, unobtrusive. Hero imagery dominates.

### Dimensions

| Property | Desktop | Mobile |
|----------|---------|--------|
| Height | 80px | 64px |
| Layout | 16-column grid | Hamburger menu (far right) |

### Background States

| State | Treatment |
|-------|-----------|
| Initial (over hero) | Solid Samotics Orange (`#FF5429`). No glassmorphism, no transparency. |
| Scrolled (over content) | Solid Samotics Orange (`#FF5429`) with subtle shadow `0 2px 8px rgba(255, 84, 41, 0.15)` |

**Note:** The header is always Samotics Orange. Nav text and logo use `--text-on-dark` (`#FFFFFF`) in both states. The CTA button uses Space Cadet background (`#1F1F33`) with white text for contrast against the orange header.

### Grid Distribution (Desktop)

| Region | Columns | Content |
|--------|---------|---------|
| Left | 1–3 | Company logo (white variant, always — header is always orange) |
| Center | 4–12 | Primary nav links. 15px medium weight. Color: `--text-on-dark` (`#FFFFFF`) always — no state change on scroll |
| Right | 13–16 | Primary CTA "Request a Demo": Space Cadet (`#1F1F33`) background with `#FFFFFF` text for contrast against the orange header |

### CTA Button

Samotics Orange (`#FF5429`) with `#111111` text. One primary CTA per viewport. On hover: `#D7411B` with `#FFFFFF` text. Focus ring: `3px solid #005CBA`. Follow full button state spec from the Samotics color system.

---

## 5. Footer Structure

The footer anchors the page on Space Cadet. Dark, structured, authoritative.

### Pre-Footer CTA Block

A CTA section bridging content to footer. Uses a light background to stay consistent with the no-dark-sections rule.

| Property | Value |
|----------|-------|
| Background | `--bg-secondary` (`#F8F5F2`) — continues the white/seashell alternation from the preceding Trust section |
| Layout | Full container width, centred |
| Heading | Large typography in `--color-primary` (`#1F1F33`). E.g., "See what your motors are telling you" |
| Sub-text | `--text-primary` (`#111111`) — descriptive sentence supporting the CTA; not metadata |
| Primary CTA | `--bg-accent` (`#FF5429`) with `--text-on-accent` (`#111111`) |
| Secondary CTA | Secondary outline button (North Sea Dark `#006C6C`) |

### Main Footer

| Property | Value |
|----------|-------|
| Background | `--bg-dark` (`#1F1F33`) |
| Top padding | `spacing-10` (96px) |
| Bottom padding | `spacing-08` (48px) |

### Footer Grid (16 columns)

| Columns | Content | Text Color |
|---------|---------|------------|
| 1–4 | Brand logo (white variant) + short mission statement | `--text-on-dark-muted` (`#B0B0C8`) |
| 5–8 | Nav Block 1: Platform, Hardware, Software | Primary links: `--text-on-dark` (`#FFFFFF`) |
| 9–12 | Nav Block 2: Industries | Links: `--text-on-dark-muted` (`#B0B0C8`), hover: `--text-on-dark` |
| 13–16 | Contact info, social links | `--text-link-on-dark` (`#B3DAFF`) for clickable elements |

### Bottom Bar

| Property | Value |
|----------|-------|
| Divider | `--border-on-dark` (`1px solid rgba(255,255,255,0.15)`) |
| Padding | `spacing-06` (24px) top and bottom |
| Left | Copyright in `--text-on-dark-muted` (`#B0B0C8`) |
| Right | Privacy Policy, Accessibility in `--text-link-on-dark` (`#B3DAFF`) |

---

## 6. Color Application by Section Type

Mapping the Samotics color system to the Carbon grid layout. Reference the full Samotics color system spec for interaction states, accessibility rules, and semantic tokens.

### Light Sections (Features, Case Studies, Content)

| Element | Token | Hex |
|---------|-------|-----|
| Background | `--bg-primary` | `#FFFFFF` |
| Headings | `--color-primary` | `#1F1F33` |
| Lead / intro paragraphs (including section subtitles below h2) | `--text-lead` | `#1F1F33` |
| Body text | `--text-primary` | `#111111` |
| Secondary text | `--text-secondary` | `#6B6B7F` |
| Links | `--text-link` | `#005CBA` |
| Card borders | `--border-light` | `#E8E4E0` |
| Card shadows | `--shadow-sm` | `0 1px 3px rgba(31,31,51,0.08)` |
| Featured card accent | `--border-accent` | `2px solid #FF5429` (left border) |

### Alternating Sections (Social Proof, Proof Strips)

| Element | Token | Hex |
|---------|-------|-----|
| Background | `--bg-secondary` | `#F8F5F2` |
| All text | Same as light sections | — |
| Transition in | `--gradient-section-fade` | White → Seashell |

### Dark Sections (Hero overlay and Footer only)

**Important:** Dark backgrounds are reserved for the hero section (as a semi-transparent overlay on photography) and the footer. Content sections on pages (features, platform, CTA blocks, trust signals, etc.) must use light backgrounds (`--bg-primary` or `--bg-secondary`). This keeps pages clean, scannable, and avoids a heavy appearance.

| Element | Token | Hex |
|---------|-------|-----|
| Background | `--bg-dark` | `#1F1F33` |
| Elevated elements | `--bg-dark-elevated` | `#2A2A42` |
| Primary text | `--text-on-dark` | `#FFFFFF` |
| Secondary text | `--text-on-dark-muted` | `#B0B0C8` |
| Links | `--text-link-on-dark` | `#B3DAFF` |
| Dividers | `--border-on-dark` | `rgba(255,255,255,0.15)` |
| Primary CTA | `--bg-accent` | `#FF5429` with `--text-on-accent` `#111111` |
| Ghost button | See Samotics ghost button spec | White border, white text |

### Technical Callout Sections

| Element | Token | Hex |
|---------|-------|-----|
| Background | `--bg-callout-info` | `#B3DAFF` |
| Heading | `--color-interactive-dark` | `#004179` |
| Body text | `--text-primary` | `#111111` |
| Icons | `--color-interactive` | `#005CBA` |

---

## 7. Design Principles (Merged)

These combine Carbon's structural discipline with the Samotics color system's philosophy.

**Visual restraint = engineering discipline.** The full palette has 17 swatches. The website should feel like it uses 5. Every color on a page must have a job.

**Grid alignment is non-negotiable.** Every component snaps to the 16-column grid lines.

**Architectural borders.** Use `--border-light` (`#E8E4E0`) for structural separation on light backgrounds. Use `--border-on-dark` on dark backgrounds. Hard 1px lines, not fuzzy shadows, for primary structural division. Shadows (`--shadow-sm`, `--shadow-md`) are permitted for elevation (cards, modals, dropdowns) — but not as a substitute for grid-based layout.

**Sharp geometry.** Zero border-radius on cards and primary UI elements. 90-degree corners reinforce the utilitarian, industrial aesthetic. Exception: pill-shaped elements (tags, badges) may use full rounding where the Samotics design system requires it.

**One orange CTA per viewport.** Samotics Orange (`#FF5429`) is reserved for primary calls to action. Never decorative. Never as text on white. If a second action is needed in the same viewport, use the secondary outline button (North Sea Dark `#006C6C`).

**Photography carries the color.** Product photography and 3D renders provide the visual weight. The UI framework stays restrained — monochrome on light sections, Space Cadet on dark sections, with orange reserved for the single most important action.
