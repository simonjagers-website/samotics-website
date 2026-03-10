# Samotics Website Color System

*Design token specification for samotics.com — March 2026*
*Updated to match the component library design system (Storybook). All values are final unless noted.*

---

## Design Principle

Visual restraint signals engineering discipline. The primitive palette contains six hue scales plus neutrals. The website should feel like it uses five colors. Every color on a page must have a job. If it doesn't carry meaning, it doesn't appear.

---

## Color Architecture

The system has three layers:

1. **Primitives** — Raw color scales (50–950 per hue). Never referenced directly in components.
2. **Semantic tokens** — Functional aliases that map meaning to primitives. Components reference these.
3. **Component tokens** — Button, input, and card-level tokens that reference semantic tokens.

---

## Primitive Scales

Each hue runs from 50 (lightest) to 950 (darkest). Orange has a single value at 400.

### Dark Blue

The brand's primary dark hue. Dark Blue 950 is Space Cadet (`#1F1F33`).

| Step | Hex | CSS Variable |
|---|---|---|
| 50 | `#F2F5FB` | `--color-dark-blue-50` |
| 100 | `#E7ECF8` | `--color-dark-blue-100` |
| 200 | `#D4DCF1` | `--color-dark-blue-200` |
| 300 | `#BAC5E7` | `--color-dark-blue-300` |
| 400 | `#9EA7DB` | `--color-dark-blue-400` |
| 500 | `#8585CF` | `--color-dark-blue-500` |
| 600 | `#6C6CBF` | `--color-dark-blue-600` |
| 700 | `#5C5BA7` | `--color-dark-blue-700` |
| 800 | `#4C4D87` | `--color-dark-blue-800` |
| 900 | `#42436D` | `--color-dark-blue-900` |
| 950 | `#1F1F33` | `--color-dark-blue-950` |

### Blue

The interactive/action hue. Blue 600 is the primary action color.

| Step | Hex | CSS Variable |
|---|---|---|
| 50 | `#EFF6FF` | `--color-blue-50` |
| 100 | `#DBEAFE` | `--color-blue-100` |
| 200 | `#BFDBFE` | `--color-blue-200` |
| 300 | `#93C5FD` | `--color-blue-300` |
| 400 | `#60A5FA` | `--color-blue-400` |
| 500 | `#3B82F6` | `--color-blue-500` |
| 600 | `#005CBA` | `--color-blue-600` |
| 700 | `#004A9A` | `--color-blue-700` |
| 800 | `#003D80` | `--color-blue-800` |
| 900 | `#003066` | `--color-blue-900` |
| 950 | `#002040` | `--color-blue-950` |

### Orange

Single accent value. Used sparingly for highlights, overlines, and small graphic elements.

| Step | Hex | CSS Variable |
|---|---|---|
| 400 | `#FF5429` | `--color-orange-400` |

### Yellow

Warning and attention hue.

| Step | Hex | CSS Variable |
|---|---|---|
| 50 | `#FEFCE8` | `--color-yellow-50` |
| 100 | `#FEF9C3` | `--color-yellow-100` |
| 200 | `#FEF08A` | `--color-yellow-200` |
| 300 | `#FDE047` | `--color-yellow-300` |
| 400 | `#FACC15` | `--color-yellow-400` |
| 500 | `#EAB308` | `--color-yellow-500` |
| 600 | `#CA8A04` | `--color-yellow-600` |
| 700 | `#A16207` | `--color-yellow-700` |
| 800 | `#854D0E` | `--color-yellow-800` |
| 900 | `#713F12` | `--color-yellow-900` |
| 950 | `#422006` | `--color-yellow-950` |

### Red

Danger and error hue.

| Step | Hex | CSS Variable |
|---|---|---|
| 50 | `#FEF2F2` | `--color-red-50` |
| 100 | `#FEE2E2` | `--color-red-100` |
| 200 | `#FECACA` | `--color-red-200` |
| 300 | `#FCA5A5` | `--color-red-300` |
| 400 | `#F87171` | `--color-red-400` |
| 500 | `#EF4444` | `--color-red-500` |
| 600 | `#DC2626` | `--color-red-600` |
| 700 | `#B91C1C` | `--color-red-700` |
| 800 | `#991B1B` | `--color-red-800` |
| 900 | `#7F1D1D` | `--color-red-900` |
| 950 | `#450A0A` | `--color-red-950` |

### Green

Success and positive status hue.

| Step | Hex | CSS Variable |
|---|---|---|
| 50 | `#F0FDF4` | `--color-green-50` |
| 100 | `#DCFCE7` | `--color-green-100` |
| 200 | `#BBF7D0` | `--color-green-200` |
| 300 | `#86EFAC` | `--color-green-300` |
| 400 | `#4ADE80` | `--color-green-400` |
| 500 | `#22C55E` | `--color-green-500` |
| 600 | `#16A34A` | `--color-green-600` |
| 700 | `#15803D` | `--color-green-700` |
| 800 | `#166534` | `--color-green-800` |
| 900 | `#14532D` | `--color-green-900` |
| 950 | `#052E16` | `--color-green-950` |

### Neutral

UI chrome, borders, disabled states, muted text.

| Step | Hex | CSS Variable |
|---|---|---|
| White | `#FFFFFF` | `--color-neutral-white` |
| 50 | `#F9FAFB` | `--color-neutral-50` |
| 100 | `#F3F4F6` | `--color-neutral-100` |
| 200 | `#E5E7EB` | `--color-neutral-200` |
| 300 | `#D1D5DB` | `--color-neutral-300` |
| 400 | `#9CA3AF` | `--color-neutral-400` |
| 500 | `#6B6B7F` | `--color-neutral-500` |
| 600 | `#4B5563` | `--color-neutral-600` |
| 700 | `#374151` | `--color-neutral-700` |
| 800 | `#1F2937` | `--color-neutral-800` |
| 900 | `#111827` | `--color-neutral-900` |
| 950 | `#030712` | `--color-neutral-950` |
| Black | `#000000` | `--color-neutral-black` |

---

## Semantic Tokens — Actions

These map to the button component variants in the design system.

| Token | Resolves to | Hex | Usage |
|---|---|---|---|
| `--color-action-primary-default` | `blue-600` | `#005CBA` | Primary button default state |
| `--color-action-primary-hover` | `blue-700` | `#004A9A` | Primary button hover |
| `--color-action-primary-pressed` | `blue-800` | `#003D80` | Primary button active/pressed |
| `--color-action-secondary-default` | `neutral-white` | `#FFFFFF` | Outline button fill |
| `--color-action-disabled` | `neutral-100` | `#F3F4F6` | Disabled button background |
| `--color-action-danger-default` | `red-700` | `#B91C1C` | Danger button default state |

---

## Semantic Tokens — Text

| Token | Resolves to | Hex | Usage |
|---|---|---|---|
| `--color-text-default` | `dark-blue-950` | `#1F1F33` | Headings, body copy on light backgrounds |
| `--color-text-inverse` | `neutral-white` | `#FFFFFF` | Text on dark backgrounds |
| `--color-text-link` | `blue-600` | `#005CBA` | Inline links |
| `--color-text-disabled` | `neutral-500` | `#6B6B7F` | Disabled labels, placeholders |

---

## Semantic Tokens — Borders

| Token | Resolves to | Hex | Usage |
|---|---|---|---|
| `--color-border-default` | `neutral-200` | `#E5E7EB` | Card borders, input borders, dividers |
| `--color-border-focus` | `blue-500` | `#3B82F6` | Focus ring on interactive elements |

---

## Semantic Tokens — Status

| Token | Resolves to | Usage |
|---|---|---|
| Success | `green-600` / `green-50` bg | Healthy asset status, positive confirmations |
| Warning | `yellow-600` / `yellow-50` bg | Attention required, degraded performance |
| Error/Danger | `red-700` / `red-50` bg | Failure, critical alerts |
| Info | `blue-600` / `blue-50` bg | Informational, neutral status |

**Rule:** Color is never the only signal for status. Every semantic color must be paired with an icon, label, or pattern. This is a WCAG requirement and a practical one — dashboards are read on plant floor monitors in poor lighting.

---

## Background System

| Context | Value | Notes |
|---|---|---|
| Page default | `#FFFFFF` (neutral-white) | Primary background |
| Alternating sections | `#F8F5F2` (seashell) | Still used for section rhythm on the marketing site |
| Dark sections | `#1F1F33` (dark-blue-950) | Hero, footer, section dividers |
| Dark elevated | `#2A2A42` | Cards/elements on dark backgrounds |
| Disabled | `#F3F4F6` (neutral-100) | Disabled input/button backgrounds |

**Background alternation rule (marketing pages):** Dark → White → Seashell → White → Seashell. Never repeat the same background on consecutive sections.

---

## Border Radius Tokens

| Token | Value | Usage |
|---|---|---|
| `--border-radius-sm` | `4px` | Small elements, tags, badges |
| `--border-radius-md` | `8px` | Cards, inputs, standard containers |
| `--border-radius-lg` | `12px` | Large cards, modals, hero elements |
| `--border-radius-full` | `9999px` | Pills, avatars, circular elements |

**Note:** The previous "zero border-radius" direction has been replaced. All UI elements now use rounded corners per these tokens. Cards and buttons use `md` (8px) by default.

---

## Spacing Tokens

| Token | Value |
|---|---|
| `--space-0` | `0px` |
| `--space-1` | `4px` |
| `--space-2` | `8px` |
| `--space-3` | `12px` |
| `--space-4` | `16px` |
| `--space-5` | `20px` |
| `--space-6` | `24px` |
| `--space-7` | `28px` |
| `--space-8` | `32px` |
| `--space-9` | `36px` |
| `--space-10` | `40px` |
| `--space-11` | `44px` |
| `--space-12` | `48px` |
| `--space-13` | `52px` |
| `--space-14` | `56px` |
| `--space-15` | `60px` |
| `--space-16` | `64px` |
| `--space-17` | `68px` |
| `--space-18` | `72px` |
| `--space-19` | `76px` |
| `--space-20` | `80px` |

**Note:** This replaces the previous IBM Carbon Base-8 spacing system. The new scale is linear (4px increments) rather than geometric.

---

## Motion Tokens

| Token | Value | Usage |
|---|---|---|
| `--motion-duration-fast` | `100ms` | Micro-interactions, hover states |
| `--motion-duration-normal` | `300ms` | Transitions, expandable sections |
| `--motion-duration-slow` | `600ms` | Page-level animations, modals |
| `--opacity-40` | `0.4` | Disabled/muted overlays |

---

## Button Component States

The design system defines five button variants: primary, outline, danger, link, and ghost.

### Primary Button

| State | Background | Text | Border |
|---|---|---|---|
| Default | `blue-600` (`#005CBA`) | `neutral-white` | none |
| Hover | `blue-700` (`#004A9A`) | `neutral-white` | none |
| Pressed | `blue-800` (`#003D80`) | `neutral-white` | none |
| Focus | `blue-600` | `neutral-white` | `blue-500` focus ring |
| Disabled | `neutral-100` (`#F3F4F6`) | `neutral-500` (`#6B6B7F`) | none |

### Outline Button

| State | Background | Text | Border |
|---|---|---|---|
| Default | `neutral-white` | `blue-600` | `neutral-200` |
| Hover | `neutral-50` | `blue-700` | `neutral-300` |
| Pressed | `neutral-100` | `blue-800` | `neutral-400` |
| Focus | `neutral-white` | `blue-600` | `blue-500` focus ring |
| Disabled | `neutral-white` | `neutral-500` | `neutral-100` |

### Danger Button

| State | Background | Text | Border |
|---|---|---|---|
| Default | `red-700` (`#B91C1C`) | `neutral-white` | none |
| Hover | `red-800` | `neutral-white` | none |
| Pressed | `red-900` | `neutral-white` | none |
| Focus | `red-700` | `neutral-white` | `blue-500` focus ring |
| Disabled | `neutral-100` | `neutral-500` | none |

### Link Button

| State | Color |
|---|---|
| Default | `blue-600` |
| Hover | `blue-700` |
| Pressed | `blue-800` |
| Disabled | `neutral-500` |

### Ghost Button

| State | Background | Text |
|---|---|---|
| Default | `transparent` | `blue-600` |
| Hover | `neutral-50` | `blue-700` |
| Pressed | `neutral-100` | `blue-800` |
| Disabled | `transparent` | `neutral-500` |

---

## Icons

**Phosphor Icons** (regular variant only). Replaces the previous custom Samotics icon set.

Icon colors follow the same semantic token rules: `dark-blue-950` on light backgrounds, `neutral-white` on dark backgrounds, `blue-600` for interactive/action contexts.

---

## Shadows

| Token | Value | Use case |
|---|---|---|
| `--shadow-sm` | `0 1px 3px rgba(31,31,51,0.08)` | Cards, dropdowns |
| `--shadow-md` | `0 4px 12px rgba(31,31,51,0.10)` | Elevated cards, modals |
| `--shadow-lg` | `0 12px 32px rgba(31,31,51,0.14)` | Popovers, floating elements |

Shadow color is always derived from Space Cadet (`#1F1F33`), never pure black.

---

## Accessibility Rules (non-negotiable)

1. **Orange (`#FF5429`):** Never as standalone text on white. Use only for small graphic accents, overlines on dark backgrounds, or icon highlights. The orange value exists as a single primitive (400) — it has no accessible text pairing on white.
2. **Focus indicators:** Every interactive element must show a visible focus ring using `blue-500` (`#3B82F6`). Never remove outline on `:focus-visible`.
3. **Color is never the only signal.** Status indicators (success/warning/error) must include an icon or text label alongside color.
4. **Disabled states** use `neutral-100` background + `neutral-500` text. Both must be visually distinct from active states but do not need to meet AA contrast (WCAG allows reduced contrast for disabled elements).
5. **Text on dark backgrounds:** Use `neutral-white` for primary text on `dark-blue-950`. Muted text on dark uses `dark-blue-300` or lighter.

---

## Mapping from Previous System

For reference, key values that carried forward or shifted:

| Previous name | Previous hex | New token | New hex | Change |
|---|---|---|---|---|
| Space Cadet | `#1F1F33` | `dark-blue-950` | `#1F1F33` | Same value, new name |
| Samotics Orange | `#FF5429` | `orange-400` | `#FF5429` | Same value |
| Midnight Frequency | `#005CBA` | `blue-600` | `#005CBA` | Same value, now action-primary |
| Seashell | `#F8F5F2` | — | `#F8F5F2` | Preserved for marketing site sections |
| Near Black | `#111111` | — | — | **Removed.** Text default is now `dark-blue-950` (`#1F1F33`) |
| Comet | `#6B6B7F` | `neutral-500` | `#6B6B7F` | Same value |
| North Sea | `#0098AC` | — | — | **Removed from primitives.** Teal no longer in the token system. |
| North Sea Dark | `#006C6C` | — | — | **Removed.** |
| Roman Purple | `#BA0068` | — | — | **Removed.** Error is now `red-700`. |
| Resistor Gold | `#FAC91F` | — | — | **Removed.** Warning uses yellow scale. |
| Orange Dark (AA) | `#D7411B` | — | — | **Removed from primitives.** |

---

## CSS Custom Properties (complete token set)

```css
:root {
  /* ================================================
     Primitives — Color Scales
     ================================================ */

  /* Orange (single value) */
  --color-orange-400: #FF5429;

  /* Dark Blue */
  --color-dark-blue-50:  #F2F5FB;
  --color-dark-blue-100: #E7ECF8;
  --color-dark-blue-200: #D4DCF1;
  --color-dark-blue-300: #BAC5E7;
  --color-dark-blue-400: #9EA7DB;
  --color-dark-blue-500: #8585CF;
  --color-dark-blue-600: #6C6CBF;
  --color-dark-blue-700: #5C5BA7;
  --color-dark-blue-800: #4C4D87;
  --color-dark-blue-900: #42436D;
  --color-dark-blue-950: #1F1F33;

  /* Blue */
  --color-blue-50:  #EFF6FF;
  --color-blue-100: #DBEAFE;
  --color-blue-200: #BFDBFE;
  --color-blue-300: #93C5FD;
  --color-blue-400: #60A5FA;
  --color-blue-500: #3B82F6;
  --color-blue-600: #005CBA;
  --color-blue-700: #004A9A;
  --color-blue-800: #003D80;
  --color-blue-900: #003066;
  --color-blue-950: #002040;

  /* Yellow */
  --color-yellow-50:  #FEFCE8;
  --color-yellow-100: #FEF9C3;
  --color-yellow-200: #FEF08A;
  --color-yellow-300: #FDE047;
  --color-yellow-400: #FACC15;
  --color-yellow-500: #EAB308;
  --color-yellow-600: #CA8A04;
  --color-yellow-700: #A16207;
  --color-yellow-800: #854D0E;
  --color-yellow-900: #713F12;
  --color-yellow-950: #422006;

  /* Red */
  --color-red-50:  #FEF2F2;
  --color-red-100: #FEE2E2;
  --color-red-200: #FECACA;
  --color-red-300: #FCA5A5;
  --color-red-400: #F87171;
  --color-red-500: #EF4444;
  --color-red-600: #DC2626;
  --color-red-700: #B91C1C;
  --color-red-800: #991B1B;
  --color-red-900: #7F1D1D;
  --color-red-950: #450A0A;

  /* Green */
  --color-green-50:  #F0FDF4;
  --color-green-100: #DCFCE7;
  --color-green-200: #BBF7D0;
  --color-green-300: #86EFAC;
  --color-green-400: #4ADE80;
  --color-green-500: #22C55E;
  --color-green-600: #16A34A;
  --color-green-700: #15803D;
  --color-green-800: #166534;
  --color-green-900: #14532D;
  --color-green-950: #052E16;

  /* Neutral */
  --color-neutral-white: #FFFFFF;
  --color-neutral-50:  #F9FAFB;
  --color-neutral-100: #F3F4F6;
  --color-neutral-200: #E5E7EB;
  --color-neutral-300: #D1D5DB;
  --color-neutral-400: #9CA3AF;
  --color-neutral-500: #6B6B7F;
  --color-neutral-600: #4B5563;
  --color-neutral-700: #374151;
  --color-neutral-800: #1F2937;
  --color-neutral-900: #111827;
  --color-neutral-950: #030712;
  --color-neutral-black: #000000;

  /* ================================================
     Semantic Tokens — Actions
     ================================================ */

  --color-action-primary-default:   var(--color-blue-600);
  --color-action-primary-hover:     var(--color-blue-700);
  --color-action-primary-pressed:   var(--color-blue-800);
  --color-action-secondary-default: var(--color-neutral-white);
  --color-action-disabled:          var(--color-neutral-100);
  --color-action-danger-default:    var(--color-red-700);

  /* ================================================
     Semantic Tokens — Text
     ================================================ */

  --color-text-default:  var(--color-dark-blue-950);
  --color-text-inverse:  var(--color-neutral-white);
  --color-text-link:     var(--color-blue-600);
  --color-text-disabled: var(--color-neutral-500);

  /* ================================================
     Semantic Tokens — Borders
     ================================================ */

  --color-border-default: var(--color-neutral-200);
  --color-border-focus:   var(--color-blue-500);

  /* ================================================
     Spacing
     ================================================ */

  --space-0:  0px;
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-7:  28px;
  --space-8:  32px;
  --space-9:  36px;
  --space-10: 40px;
  --space-11: 44px;
  --space-12: 48px;
  --space-13: 52px;
  --space-14: 56px;
  --space-15: 60px;
  --space-16: 64px;
  --space-17: 68px;
  --space-18: 72px;
  --space-19: 76px;
  --space-20: 80px;

  /* ================================================
     Border Radius
     ================================================ */

  --border-radius-sm:   4px;
  --border-radius-md:   8px;
  --border-radius-lg:   12px;
  --border-radius-full: 9999px;

  /* ================================================
     Motion
     ================================================ */

  --opacity-40: 0.4;
  --motion-duration-fast:   100ms;
  --motion-duration-normal: 300ms;
  --motion-duration-slow:   600ms;

  /* ================================================
     Shadows (Space Cadet base, never pure black)
     ================================================ */

  --shadow-sm: 0 1px 3px rgba(31,31,51,0.08);
  --shadow-md: 0 4px 12px rgba(31,31,51,0.10);
  --shadow-lg: 0 12px 32px rgba(31,31,51,0.14);
}
```

---

*Six hue scales. Semantic tokens for everything a component touches. Primitives stay in the system — never in your markup.*
