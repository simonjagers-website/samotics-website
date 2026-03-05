# Navigation Specification

Main nav structure, dropdowns, mobile behaviour, CTAs, and breadcrumbs for samotics.com

**Document:** Navigation — Base
**Layer:** Architecture
**Owner:** Marketing
**Status:** Draft
**Date:** February 2026
**Dependencies:** Site Architecture, #12 User Journey Map, #3 Buying Scenario Framework
**Feeds Into:** Design System, Component Inventory, CMS Build

---

## How to Use This Document

This document defines exactly what appears in the site navigation — desktop and mobile. It covers the main nav bar, dropdown menus, the persistent CTA, breadcrumb logic, and footer navigation. Designers use it for wireframes. Developers use it for CMS nav configuration. Content leads use it to validate that every persona journey is reachable within two clicks from any page.

---

## Design Principles

The navigation must solve three problems simultaneously:

1. **Route by intent.** S1/S2 visitors (majority of traffic) arrive with a known problem. They need to reach technology and proof pages fast. The nav must not bury these behind generic labels.

2. **Support evaluation depth.** S3 visitors (CTO, Digital Lead) need security, integrations, and enterprise proof. These pages must be discoverable without cluttering the primary nav for the majority audience.

3. **Separate partner traffic.** S5 visitors (Channel Partners) have entirely different needs. A dedicated partner entry point prevents cross-contamination with end-user buyer journeys.

---

## Main Navigation (Desktop)

### Nav Bar Layout

```
[Logo]   Problem   Technology ▾   Platform ▾   Industries ▾   Proof   About   [Request a Demo]
```

The nav bar is fixed/sticky on scroll. Seven items plus the CTA. No more than seven — cognitive load matters.

### Nav Items and Dropdowns

#### 1. Problem
- **Type:** Direct link (no dropdown)
- **URL:** `/problem`
- **Rationale:** S1 and S2 visitors need this in one click. A dropdown would add friction to the highest-traffic path. The Proximity Penalty page is linked from within the Problem page, not from the nav.

#### 2. Technology ▾
- **Type:** Dropdown
- **Dropdown items:**

| Label | URL | Description (tooltip/subtitle) |
|-------|-----|-------------------------------|
| Electrical Signature Analysis | `/technology/esa` | The science behind SAM4 |
| How It Works | `/technology/how-it-works` | From sensor to insight |
| ESA vs Vibration | `/technology/esa-vs-vibration` | How ESA complements traditional monitoring |

- **Rationale:** Reliability Managers (S1) need ESA immediately. Separating ESA from "How It Works" lets them go directly to the science. The comparison page handles the #1 objection ("why not vibration?") and needs to be visible in the nav, not buried.

#### 3. Platform ▾
- **Type:** Dropdown
- **Dropdown items:**

| Label | URL | Description (tooltip/subtitle) |
|-------|-----|-------------------------------|
| SAM4 Platform | `/platform/sam4` | Dashboard, diagnostics, and service model |
| How It Installs | `/platform/how-it-installs` | <30 minutes, no downtime |
| Security & Compliance | `/platform/security` | SOC 2, ISO 27001, NIS2, cellular architecture |
| Integrations | `/platform/integrations` | CMMS, SCADA, and API connectivity |

- **Rationale:** Four items. SAM4 is the primary draw. Security and Integrations are critical for the Digital Lead (S3) — this persona has veto power and needs these pages discoverable without hunting. "How It Installs" removes the deployment objection for Reliability Managers and Ops Directors.

#### 4. Industries ▾
- **Type:** Dropdown
- **Dropdown items:**

| Label | URL | Phase |
|-------|-----|-------|
| Water & Wastewater | `/industries/water` | v1 |
| Oil & Gas | `/industries/oil-gas` | v1 |
| Metals & Mining | `/industries/metals-mining` | v1 |
| Chemicals | `/industries/chemicals` | v1 |
| Pulp & Paper | `/industries/pulp-paper` | v1 |

- **Rationale:** Industry pages are primary landing pages for organic search (S1, S2). Listing all five in the dropdown lets visitors self-select immediately. Phase 3 adds "Energy Efficiency" — when it ships, add it as the sixth item with a subtle "New" badge.
- **No section landing page in v1.** The dropdown links directly to individual industry pages. If a section landing is needed later (e.g., for SEO), build `/industries` as a routing page.

#### 5. Proof
- **Type:** Direct link (no dropdown)
- **URL:** `/proof`
- **Rationale:** The Proof hub is a filterable grid — it doesn't need sub-items in the nav. Every persona visits this page. Making it a single click from the nav (no dropdown) reduces friction. Individual case studies are reached from the hub, not the nav.

#### 6. About
- **Type:** Direct link (no dropdown)
- **URL:** `/about`
- **Rationale:** CTO/VP Engineering (S3) uses this as a credibility check — they spend 30 seconds here. The ABB partnership page is linked from within About, not from the nav. Keeps the nav clean.
- **Phase 2 change:** When `/partners` launches, consider adding a dropdown: About ▾ → Company, Partners, ABB Partnership. Until then, keep it as a direct link.

#### 7. [Request a Demo] — Primary CTA
- **Type:** Button (visually distinct from nav links)
- **URL:** `/contact`
- **Style:** Filled button, brand accent colour (refer to colour system). Stands out from text nav items.
- **Rationale:** "Request a Demo" is the primary CTA for S1 (highest-urgency, highest-traffic scenario). It appears on every page via the nav. Other CTAs (Asset Audit, Talk to Us, Security Docs) appear contextually on individual pages — they don't compete in the nav.

---

## Dropdown Behaviour (Desktop)

| Behaviour | Specification |
|-----------|--------------|
| **Trigger** | Hover to open, click to navigate. Dropdown opens on hover with ~150ms delay to prevent accidental triggers. |
| **Close** | Closes on mouse-out with ~300ms delay. Closes immediately on click outside. |
| **Width** | Auto-width based on content. No mega-menu. Clean single-column list. |
| **Subtitles** | Each dropdown item has a short description line (grey, smaller text) beneath the label. Aids scanning. |
| **Active state** | Current page's nav item is visually highlighted (underline or bold). If on a child page, the parent dropdown label is highlighted. |
| **Keyboard** | Tab navigates through nav items. Enter opens dropdowns. Arrow keys navigate within dropdowns. Escape closes. |

---

## Mobile Navigation

### Trigger
- **Hamburger icon** on the right side of the mobile nav bar. Logo on the left. CTA button ("Request a Demo") visible next to the hamburger — it does NOT collapse into the menu.

### Mobile Nav Layout

```
[Logo]                    [Request a Demo]  [☰]
```

The CTA stays visible at all times on mobile. This is non-negotiable — S1 visitors on mobile (e.g., on the plant floor after a failure) must be able to convert without opening the menu.

### Menu Behaviour

| Behaviour | Specification |
|-----------|--------------|
| **Type** | Full-screen overlay or slide-in panel from right |
| **Animation** | Slide in, 200ms ease-out. No jarring snap. |
| **Sections with children** | Tap to expand/collapse (accordion). Arrow icon rotates on expand. |
| **Sections without children** | Tap navigates directly (Problem, Proof, About) |
| **Close** | X button in top-right corner of panel, or tap outside the panel |
| **Scroll** | Menu scrolls independently if content exceeds viewport height |

### Mobile Menu Structure

```
Problem                          → /problem
Technology                       [expand ▾]
    Electrical Signature Analysis    → /technology/esa
    How It Works                     → /technology/how-it-works
    ESA vs Vibration                 → /technology/esa-vs-vibration
Platform                         [expand ▾]
    SAM4 Platform                    → /platform/sam4
    How It Installs                  → /platform/how-it-installs
    Security & Compliance            → /platform/security
    Integrations                     → /platform/integrations
Industries                       [expand ▾]
    Water & Wastewater               → /industries/water
    Oil & Gas                        → /industries/oil-gas
    Metals & Mining                  → /industries/metals-mining
    Chemicals                        → /industries/chemicals
    Pulp & Paper                     → /industries/pulp-paper
Proof                            → /proof
About                            → /about
──────────────────────────────
Request a Demo                   → /contact
```

The bottom CTA in the menu is a secondary reinforcement. The primary mobile CTA lives in the nav bar itself (always visible).

---

## Sticky Nav / Scroll Behaviour

| Behaviour | Desktop | Mobile |
|-----------|---------|--------|
| **Sticky** | Yes — nav bar stays fixed at top on scroll | Yes — compact nav bar stays fixed |
| **Compact on scroll** | Nav bar reduces height slightly after first scroll (e.g., 80px → 60px). Logo scales down. | Nav bar stays compact throughout. |
| **CTA visibility** | Always visible in nav bar | Always visible in nav bar |
| **Shadow** | Subtle drop shadow appears on scroll to separate nav from content | Same |

---

## Breadcrumbs

### When to Show
Breadcrumbs appear on all pages except the Homepage. They sit below the nav bar, above the page hero/header.

### Format
```
Home > [Section] > [Page]
```

Each segment is a clickable link except the current page (displayed as plain text).

### Examples

| Page | Breadcrumb |
|------|-----------|
| `/technology/esa` | Home > Technology > Electrical Signature Analysis |
| `/technology/how-it-works` | Home > Technology > How It Works |
| `/platform/security` | Home > Platform > Security & Compliance |
| `/industries/water` | Home > Industries > Water & Wastewater |
| `/proof/yorkshire-water` | Home > Proof > Yorkshire Water |
| `/problem/proximity-penalty` | Home > Problem > The Proximity Penalty |
| `/contact/asset-audit` | Home > Contact > Asset Audit |
| `/about` | Home > About |
| `/proof` | Home > Proof |

### Breadcrumb Rules

| Rule | Specification |
|------|--------------|
| **Schema markup** | Every breadcrumb trail uses `BreadcrumbList` structured data (JSON-LD) for SEO |
| **Separator** | `>` character with spacing. Not `/` or `→`. |
| **Mobile** | Breadcrumbs display on mobile but truncate to show only the immediate parent: `< Technology` (back-link style). Full breadcrumb trail accessible if tapped. |
| **Section landing pages** | Even if no dedicated section landing page exists (e.g., `/technology` redirects or doesn't exist), the breadcrumb still shows "Technology" as a clickable link. It links to the first child page or the dropdown anchor. |

---

## Footer Navigation

The footer serves as a complete sitemap for users who scroll to the bottom. It also provides legal links and secondary CTAs.

### Footer Layout

```
[Logo]

Technology              Platform                Industries             Proof            Company
  ESA Technology          SAM4 Platform           Water & Wastewater     Case Studies     About
  How It Works            How It Installs         Oil & Gas              Results          Partners (Phase 2)
  ESA vs Vibration        Security & Compliance   Metals & Mining                         Blog
                          Integrations            Chemicals                               Contact
                                                  Pulp & Paper

──────────────────────────────────────────────────────────────────────────────────
[Request a Demo]                                    Privacy  |  Terms  |  Cookies
                                                    © 2026 Samotics
```

### Footer Rules

| Rule | Specification |
|------|--------------|
| **Columns** | 5 columns on desktop. Collapse to accordion on mobile. |
| **CTA** | "Request a Demo" button in footer. Same URL as nav CTA (`/contact`). |
| **Social links** | LinkedIn icon. No other social platforms unless active. |
| **Legal links** | Privacy, Terms, Cookies — bottom row, separated by pipes. |
| **Copyright** | `© 2026 Samotics` — updates automatically by year. |
| **Phase 2 additions** | Add "Partners" and "Partner Programme" under Company column when `/partners` ships. |

---

## Nav CTA Strategy

The nav carries a single CTA. Page-level CTAs vary by persona and scenario. This separation is deliberate.

| Context | CTA | Rationale |
|---------|-----|-----------|
| **Nav bar (global)** | Request a Demo | Highest-traffic scenario (S1) drives the persistent CTA. Universal enough for S2/S3 visitors too. |
| **Problem page** | Start Your Asset Audit | S2 visitors need a lower-commitment entry than a demo. |
| **Platform/Security page** | Request Security Docs | Digital Lead (S3) needs downloadable docs — this is their conversion point. |
| **About page** | Talk to Us | CTO/VP (S3) wants an executive conversation, not a demo. |
| **Industry pages** | Request a Demo | S1 visitors land here from search — match the urgency. |
| **Proof / Case studies** | Request a Demo + PDF Download | Both the conversion CTA and the shareable asset. |
| **Partners/ABB (Phase 2)** | Discuss Partnership | S5 visitors need a partnership conversation. |

The nav CTA does not change per page. It stays as "Request a Demo" everywhere. Contextual CTAs live in the page content and hero sections.

---

## Accessibility Requirements

| Requirement | Specification |
|-------------|--------------|
| **ARIA roles** | `<nav role="navigation">` with `aria-label="Main navigation"`. Dropdowns use `aria-expanded` and `aria-haspopup`. |
| **Focus management** | Visible focus indicators on all nav items. Skip-to-content link as first focusable element. |
| **Keyboard navigation** | Full keyboard support: Tab, Enter, Escape, Arrow keys. |
| **Screen readers** | Current page announced with `aria-current="page"`. Dropdown state announced on toggle. |
| **Contrast** | Nav text meets WCAG 2.1 AA contrast ratios against the nav background. CTA button meets AA for both text and background. |
| **Touch targets** | Mobile nav items have minimum 44×44px touch targets. |
| **Reduced motion** | Dropdown and mobile menu animations respect `prefers-reduced-motion`. |

---

## Phase Roadmap for Navigation

| Phase | Change |
|-------|--------|
| **v1** | Ship nav as specified above. 7 items + CTA. No partner section in nav. |
| **Phase 2** | Add "Partners" to nav. About becomes dropdown: Company / Partners / ABB Partnership. Add `/contact/partner-inquiry` to contact routing. |
| **Phase 3** | Add "Energy Efficiency" to Industries dropdown. Evaluate whether industries dropdown needs restructuring (6 items is the limit before it feels heavy). |
