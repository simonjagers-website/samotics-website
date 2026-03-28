# Industry Page CSS Conventions

CSS patterns established across all industry pages. Apply in the dist file's inline CSS. Industry-specific overrides use the `--{industry}` class modifier (e.g., `sam-hero--water`, `sam-hero--oilgas`).

For underlying design system rules (colours, typography, spacing, card interactions), load `samotics-design-system`.

---

## Table of contents

1. Dual token system
2. Background alternation
3. Hero overlay
4. Trust bar
5. Challenge cards (2x2)
6. Differentiator cards (2x2)
7. Asset cards (3-column)
8. Proof highlight + proof cards
9. Install grid
10. FAQ accordion
11. Terminal CTA
12. Section spacing and responsive
13. Build workflow

---

## 1. Dual token system

Two sets of CSS custom properties coexist in every industry page:

**Shared tokens (`--sam-` prefix):** Used by the header, footer, and any component shared across page types.
```css
:root {
  --sam-space-cadet: #1F1F33;
  --sam-orange: #FF5429;
  --sam-orange-dark: #D7411B;
  --sam-blue: #005CBA;
  --sam-white: #FFFFFF;
  --sam-seashell: #F8F5F2;
  --sam-comet: #6B6B7F;
  --sam-border-light: #E8E4E0;
  --sam-font: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --sam-header-h: 80px;
  --sam-header-h-compact: 64px;
  --sam-transition: 150ms ease-out;
}
```

**Page tokens (no prefix):** Used by page-specific content sections.
```css
:root {
  --space-cadet: #1F1F33;
  --white: #FFFFFF;
  --seashell: #F8F5F2;
  --orange: #FF5429;
  --comet: #6B6B7F;
  --border-grey: #E5E7EB;
  --blue-600: #005CBA;
  --font-primary: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-data: 'JetBrains Mono', 'Consolas', monospace;
  --radius-default: 4px;
  --radius-full: 9999px;
  --shadow-sm: 0 1px 3px rgba(31, 31, 51, 0.08);
  --motion-fast: 100ms;
  --motion-normal: 300ms;
  --max-width: 1120px;
  --max-width-wide: 1280px;
}
```

When referencing colours in page content, use the unprefixed tokens. When styling header/footer elements, use `--sam-` tokens. This separation prevents page styles from leaking into shared components.

---

## 2. Background alternation

The full 9-section sequence:

| Section | Background | CSS class |
|---|---|---|
| 1. Hero | Dark overlay on image | `sam-section--hero` |
| 2. Trust bar | Inherits | `sam-trust-bar` (not a section) |
| 3. Challenges | White | `sam-section--white` |
| 4. Why SAM4 | Seashell | `sam-section--seashell` |
| 5. Assets | White | `sam-section--white` |
| 6. Proof | Seashell | `sam-section--seashell` |
| 7. Installation | White | `sam-section--white` |
| 8. FAQ | Seashell | `sam-section--seashell` |
| 9. Terminal CTA | Dark | `sam-section--dark` |

**The rule:** No two consecutive content sections share the same background. If a section is removed, re-assign backgrounds to maintain alternation. Plan backgrounds before writing CSS.

```css
.sam-section--white { background: var(--white); }
.sam-section--seashell { background: var(--seashell); }
.sam-section--dark { background: var(--space-cadet); color: var(--white); }
```

---

## 3. Hero overlay

```css
.sam-section--hero {
  position: relative;
  background-size: cover;
  background-position: center;
  padding: 120px 0;
}

.sam-hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to right,
    rgba(31,31,51,0.88) 0%,
    rgba(31,31,51,0.35) 100%
  );
  z-index: 1;
}

.sam-section--hero .sam-section__inner {
  position: relative;
  z-index: 2;
}
```

Industry-specific hero images are set via `background-image` on the `.sam-section--hero` element, either inline or via an industry-specific class.

**Stats bar:**
```css
.sam-stats-bar {
  display: flex;
  gap: 48px;
  margin: 32px 0;
}
.sam-stat__value {
  font-family: var(--font-data);
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.1;
}
.sam-stat__label {
  font-size: 0.875rem;
  opacity: 0.8;
  margin-top: 4px;
}
```

**Measurement method box (hero variant):**
```css
.sam-measurement-method {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: var(--radius-default);
  padding: var(--space-4) var(--space-6);
  max-width: 640px;
  margin: 0 auto var(--space-8);
}
.sam-measurement-method p {
  font-size: 12px;
  color: rgba(255,255,255,0.7);
  line-height: 1.5;
  text-align: center;
  margin: 0;
}
```

**Hero actions:**
```css
.sam-hero-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}
```

---

## 4. Trust bar

```css
.sam-trust-bar {
  padding: 24px 0;
  border-bottom: 1px solid var(--border-grey);
}
.sam-trust-bar__inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}
.sam-trust-bar__label {
  font-size: 0.875rem;
  color: var(--comet);
  white-space: nowrap;
}
.sam-trust-bar__logos {
  display: flex;
  align-items: center;
  gap: 32px;
  flex-wrap: wrap;
}
.sam-trust-bar__logo img {
  height: 36px;
  width: auto;
  filter: grayscale(100%);
  opacity: 0.7;
  transition: all 0.3s ease;
}
.sam-trust-bar__logo img:hover {
  filter: grayscale(0%);
  opacity: 1;
}
```

---

## 5. Challenge cards (2x2)

```css
.sam-card-grid--2col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}
.sam-card {
  background: var(--white);
  border: 1px solid var(--border-grey);
  border-radius: var(--radius-default);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.sam-card__icon {
  width: 32px;
  height: 32px;
  color: var(--comet);
}
.sam-card__icon svg {
  width: 100%;
  height: 100%;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
}
.sam-card__title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--space-cadet);
}
.sam-card__body {
  font-size: 1rem;
  color: var(--comet);
  line-height: 1.6;
}
```

On seashell backgrounds, challenge cards use white backgrounds for contrast. On white backgrounds, cards can use seashell or white with border emphasis.

```css
.sam-section--seashell .sam-card {
  background: var(--white);
}
```

---

## 6. Differentiator cards (2x2)

Same card grid as challenges (`sam-card-grid--2col`). No icons — differentiator cards use bold titles and body text only.

**Contrast line below the grid:**
```css
.sam-section__contrast {
  text-align: center;
  font-size: 15px;
  color: var(--comet);
  max-width: 640px;
  margin: 0 auto;
}
```

---

## 7. Asset cards (3-column)

```css
.sam-card-grid--3col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

Asset cards are clickable — the entire card is an `<a>` tag (not a `<div>` with a link inside):

```css
a.sam-card {
  text-decoration: none;
  color: inherit;
  transition: box-shadow var(--motion-normal) ease-out;
}
a.sam-card:hover {
  box-shadow: var(--shadow-sm);
}
.sam-card__link {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--blue-600);
  margin-top: auto;
}
```

---

## 8. Proof highlight + proof cards

**Featured case study highlight:**
```css
.sam-proof-highlight {
  background: var(--white);
  border: 1px solid var(--border-grey);
  border-radius: var(--radius-default);
  padding: 48px;
  margin-bottom: 32px;
}
.sam-proof-highlight__overline {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--orange);
  margin-bottom: 12px;
}
.sam-proof-highlight__title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 16px;
}
.sam-proof-highlight__body {
  color: var(--comet);
  line-height: 1.6;
  margin-bottom: 24px;
}
.sam-proof-highlight__stats {
  display: flex;
  gap: 48px;
  margin-bottom: 24px;
}
```

**Proof cards (3-column):**
```css
.sam-proof-card {
  background: var(--white);
  border: 1px solid var(--border-grey);
  border-radius: var(--radius-default);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  text-decoration: none;
  color: inherit;
  transition: box-shadow var(--motion-normal) ease-out;
}
.sam-proof-card:hover {
  box-shadow: var(--shadow-sm);
}
.sam-proof-card__kpi {
  font-family: var(--font-data);
  font-size: 2rem;
  font-weight: 700;
  color: var(--space-cadet);
  line-height: 1.1;
}
.sam-proof-card__customer {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--comet);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.sam-proof-card__body {
  font-size: 1rem;
  color: var(--comet);
  line-height: 1.6;
  flex: 1;
}
.sam-proof-card__link {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--blue-600);
}
```

---

## 9. Install grid

```css
.sam-install-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}
.sam-install-step {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}
.sam-install-step__num {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--space-cadet);
  color: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
}
.sam-install-step__text strong {
  display: block;
  margin-bottom: 4px;
}
.sam-install-step__text span {
  color: var(--comet);
  font-size: 0.9375rem;
}
.sam-install-image img {
  width: 100%;
  border-radius: var(--radius-default);
  object-fit: cover;
}
```

On seashell backgrounds, step numbers use `background: var(--seashell)` with `color: var(--space-cadet)` and `border: 1.5px solid var(--space-cadet)`.

**Customer quote:**
```css
.sam-quote {
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--border-grey);
}
.sam-quote__text {
  font-size: 1.125rem;
  font-style: italic;
  color: var(--space-cadet);
  line-height: 1.6;
  margin-bottom: 8px;
}
.sam-quote__attr {
  font-size: 0.875rem;
  color: var(--comet);
}
```

---

## 10. FAQ accordion

New section — not present on current live pages. Add using this pattern:

```css
.sam-faq {
  max-width: 720px;
  margin: 0 auto;
}
.sam-faq__item {
  border-bottom: 1px solid var(--border-grey);
}
.sam-faq__item:first-child {
  border-top: 1px solid var(--border-grey);
}
.sam-faq__question {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 0;
  background: none;
  border: none;
  cursor: pointer;
  font-family: var(--font-primary);
  font-size: 1.0625rem;
  font-weight: 600;
  color: var(--space-cadet);
  text-align: left;
  line-height: 1.4;
}
.sam-faq__icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  margin-left: 16px;
  transition: transform var(--motion-normal) ease-out;
  color: var(--comet);
}
.sam-faq__item.is-open .sam-faq__icon {
  transform: rotate(45deg);
}
.sam-faq__answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--motion-normal) ease-out;
}
.sam-faq__item.is-open .sam-faq__answer {
  max-height: 500px;
}
.sam-faq__answer p {
  padding: 0 0 24px;
  color: var(--comet);
  line-height: 1.6;
  font-size: 1rem;
}
```

**JavaScript for accordion:**
```html
<script>
document.querySelectorAll('.sam-faq__question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.sam-faq__item');
    const isOpen = item.classList.contains('is-open');
    // Close all
    document.querySelectorAll('.sam-faq__item').forEach(i => i.classList.remove('is-open'));
    // Toggle clicked
    if (!isOpen) item.classList.add('is-open');
  });
});
</script>
```

**HTML structure:**
```html
<div class="sam-faq">
  <div class="sam-faq__item">
    <button class="sam-faq__question">
      Question text here
      <svg class="sam-faq__icon" viewBox="0 0 20 20">
        <path d="M10 4v12M4 10h12" stroke="currentColor" stroke-width="2" fill="none"/>
      </svg>
    </button>
    <div class="sam-faq__answer">
      <p>Answer text here.</p>
    </div>
  </div>
</div>
```

---

## 11. Terminal CTA

```css
.sam-terminal-cta {
  text-align: center;
  padding: 120px 0;
}
.sam-terminal-cta .sam-section__title {
  color: var(--white);
  max-width: 640px;
  margin: 0 auto 16px;
}
.sam-terminal-cta .sam-section__subtitle {
  color: rgba(255,255,255,0.75);
}
```

Uses the same `sam-hero-actions` flex layout for the CTA pair.

---

## 12. Section spacing and responsive

**Desktop (>1024px):**
```css
.sam-section { padding: 96px 0; }
.sam-section--hero, .sam-section--dark { padding: 120px 0; }
.sam-section__inner { max-width: var(--max-width); margin: 0 auto; padding: 0 24px; }
.sam-section__inner--wide { max-width: var(--max-width-wide); }
```

**Tablet (768-1024px):**
```css
@media (max-width: 1024px) {
  .sam-section { padding: 64px 0; }
  .sam-section--hero, .sam-section--dark { padding: 80px 0; }
  .sam-card-grid--2col,
  .sam-card-grid--3col { grid-template-columns: 1fr; }
  .sam-install-grid { grid-template-columns: 1fr; }
  .sam-stats-bar { flex-direction: column; gap: 24px; }
}
```

**Mobile (<768px):**
```css
@media (max-width: 768px) {
  .sam-section { padding: 48px 0; }
  .sam-section--hero, .sam-section--dark { padding: 64px 0; }
  .sam-section__inner { padding: 0 16px; }
  .sam-proof-highlight { padding: 24px; }
  .sam-proof-highlight__stats { flex-direction: column; gap: 16px; }
}
```

---

## 13. Build workflow

1. **Write the source HTML fragment** in `pages/industries/{page}.html` (canonical content source).
2. **Rebuild the dist file** at `dist/industries/{page}/index.html`. Full HTML with inline CSS. No build tooling — rebuild manually via Python.
3. **Commit and push** to main. Cloudflare deploys automatically.
4. **Cache-bust** by appending `?v=N` when testing changes live.

**Known issues:**
- Edit tool fails on dist files (>500 lines). Use Python to read/modify/write in a single operation.
- Background alternation breaks when sections are removed. Always check before committing.
- Hero needs both `sam-section--hero` (shared) + the industry background image.
