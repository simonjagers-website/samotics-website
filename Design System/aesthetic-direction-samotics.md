# Aesthetic Direction: SAM4 Digital Experience

*Aligned to the Samotics Layout Rules (IBM Carbon Grid) and Samotics Color System.*
*Where this document and the layout rules or color system conflict, the layout rules and color system take precedent.*

---

## 1. The Overall Vibe: "The Invisible Standard"

The feeling is **inevitable authority.** Visitors don't feel sold a gadget. They feel like they've found the operating system for their most critical, inaccessible assets.

Three emotional registers drive every design decision:

**Engineering Truth.** The site feels grounded in physics and electrical engineering. No generic "AI brain" icons. Show clean, high-fidelity spectral analysis graphs. Show the math. Show the signal processing. Show the result, not the magic.

**Operational Peace.** Inaccessible assets cause high-stress failures. The website is the antidote. The macro spacing scale (128–160px between sections), the restrained color palette, and the structured grid create calm. Organized. Structurally sound.

**Scale & Permanence.** The design feels heavy in a premium way. Like a piece of ABB or Siemens hardware, it belongs in a multi-billion dollar facility. The 16-column Carbon grid, sharp 90-degree corners, and Space Cadet (`#1F1F33`) dark sections deliver this weight.

---

## 2. Visual Principles

### The "No-Sensor" Aesthetic

The goal is to frame legacy approaches (sensors on assets) as a failure. Imagery avoids close-ups of stick-on sensors or handheld vibration tools.

**Focus on the Motor Control Center (MCC).** This is your throne. Imagery highlights the clean, safe, accessible environment of the cabinet versus the dark, dangerous, inaccessible asset.

**"Inside-Out" visualization.** Show electricity flowing from the cabinet to the distant pump or fan as a stream of data. This is the visual metaphor for Electrical Signature Analysis — monitoring from a distance, through the signal itself.

### High-Fidelity Data as Design Element

No stock photos of blue tech lines. No glowing neural networks.

**SAM4 UI as hero content.** Use actual product screenshots — dark-mode dashboards, torque ripple curves, harmonic distortion graphs — as primary visual elements within hero and feature sections. These sit naturally in the Space Cadet (`#1F1F33`) hero blocks defined in the layout rules. Treat them as the "flight deck" of industrial reliability.

**Engineer recognition test.** If a Reliability Engineer sees a specific spectral signature on the homepage, they should think: *"These people actually understand my motor."* Data visualizations must be technically accurate, not decorative.

### Architecture-First Layout

The 16-column Carbon grid is the backbone. Every component snaps to grid lines. No exceptions.

**Asymmetric compositions.** Use the grid to create tension — a 10-column headline next to a 5-column data card with an empty column between them. This suggests precision and logic without needing to explain it.

**Section rhythm.** Page body sections use light backgrounds only (`--bg-primary` / `--bg-secondary`), alternating between White and Seashell. Dark sections (`--bg-dark`, `#1F1F33`) are reserved exclusively for the hero (as a photo overlay), header (Samotics Orange), and footer. Content sections never use dark backgrounds — the calm, clean surface palette creates natural visual breaks without relying on colour contrast. The `--gradient-section-fade` handles transitions between light surfaces.

**Typography.** Professional, utilitarian, highly legible. Bold headers that state truths, not questions. Declarative language only.

---

## 3. How the Color System Serves the Aesthetic

The Samotics color system enforces the aesthetic through constraint.

### Industrial Monotone + Signal

The full palette has 17 swatches. The website feels like it uses 5. This is the design principle stated in the color system, and it directly serves the "Category Leader" positioning.

| Role | Execution |
|------|-----------|
| **Machine Grey** | Space Cadet (`#1F1F33`) — hero overlay and footer only. Never used as a background for body content sections. The structural anchor, used sparingly. |
| **Clean Surface** | White (`#FFFFFF`) and Seashell (`#F8F5F2`) — content sections. Alternating backgrounds create rhythm without adding color. |
| **Signal Color** | Samotics Orange (`#FF5429`) — primary CTAs only. One per viewport. Never decorative. This is the single element that draws the eye on any screen. |
| **Utility Blue** | Midnight Frequency (`#005CBA`) — links, interactive elements, focus rings. Functional, not aesthetic. |
| **Data Ink** | Space Cadet (`#1F1F33`) for lead/intro paragraphs and headings — creates visual hierarchy above body text. Near Black (`#111111`) for body paragraphs and descriptive sentences. Comet (`#6B6B7F`) strictly for captions, metadata, timestamps, and short secondary labels — never for paragraph-length content. Maximum legibility, zero personality. |

Everything else in the extended palette (teal, purple, gold) earns its place through specific semantic meaning or stays off the page.

### Elevation and Depth

The shadow system (`--shadow-sm` through `--shadow-lg`) provides functional elevation for UI elements that genuinely float: dropdowns, modals, tooltips, and elevated cards. This is not decoration — it signals interactive hierarchy.

The CTA glow (`--shadow-orange`) reinforces the "Signal Color" role of Samotics Orange on hover. Use it on primary CTAs only. It must feel like a controlled indicator light, not a neon sign.

For structural separation of on-page content blocks, prefer `--border-light` (`#E8E4E0`) hard borders. These mimic technical blueprints and reinforce the utilitarian feel. Shadows and borders serve different purposes — don't substitute one for the other.

### Borders as Blueprint Lines

All structural borders use 1px hard lines from the border token system. Zero border-radius on cards, buttons, and primary UI elements. 90-degree corners only. The interface should feel bolted together, not smoothed over.

---

## 4. Anti-Examples

To maintain category dominance, steer away from these patterns:

| Element | Avoid ("Scale-up" Look) | Aim For ("Category Leader" Look) |
|---------|------------------------|----------------------------------|
| **Color** | Neon blues, "save the planet" greens, generic tech-purple | Industrial monotone (Space Cadet + White/Seashell) with one Signal Color (Samotics Orange) for CTAs only |
| **Imagery** | Stock photos of smiling engineers pointing at tablets in clean factories | Macro-photography of industrial power cables, MCC internals, crisp technical CAD-style 3D renders |
| **Language** | "Revolutionizing," "Disrupting," "The Power of AI" | Declarative and structural: "Eliminating blind spots," "The Architecture for Inaccessible Assets," "Standardizing Reliability" |
| **Interaction** | Playful animations, bouncy scrolls, "fun" micro-interactions | Tool-like precision: fast load times, snap transitions (150–250ms, CSS transforms only), zero scroll-triggered animation delays |
| **AI representation** | Glowing brains, digital webs connecting nodes | The black box opened: show the spectral analysis, the signal processing, the diagnostic result |
| **Elevation** | Heavy drop shadows on every card, floating everything | Shadows for functional elevation only (dropdowns, modals). Borders for structural separation |

---

## 5. Interaction & Motion

The aesthetic doc and layout rules align on this: the site should feel like an expert tool, not a brochure.

**Transition duration:** 150–250ms. No slower.

**Easing:** Linear or ease-out. No bounce. No spring physics.

**Technique:** CSS transforms and opacity only. No layout-triggering animations (no animating width, height, margin, or padding).

**Scroll behavior:** Content is immediately visible. No scroll-triggered fade-ins, slide-ups, or parallax effects that delay content visibility. The engineer is here to evaluate, not to be entertained.

**Page transitions:** Snap. Instant navigation. If a skeleton loader is needed, it should feel like a loading state in a monitoring dashboard — a brief placeholder, not a choreographed reveal.

**Hover states:** Defined in the Samotics color system interaction states (buttons, links, form inputs). Follow those specs exactly. No additional hover effects on cards or images unless specifically defined.

---

## 6. The "Trust at Depth" Signature

Every major page should include a section that provides technical ground truth for the engineer. This prevents the site from feeling like a marketing shell.

Examples of trust-at-depth content: downloadable cybersecurity whitepapers, API documentation links, failure mode coverage maps, JSON schema references for integration, or specification comparison tables.

These sections use the standard layout rules — typically on `--bg-secondary` (`#F8F5F2`) to visually separate them from marketing content above. Card grids for downloadable assets use `--border-light` borders and the micro spacing scale (`spacing-05` to `spacing-06`) for tight, data-dense presentation.

The point: the bottom of the page is where the engineer validates the claims made at the top. Make it easy.
