# Samotics Website — Sitemap Optimisation

**Document:** Sitemap Review & Recommendations
**Date:** 29 March 2026
**Status:** Executed — see implementation log below
**Supersedes:** samotics-sitemap-recommendation.md (earlier planning doc)
**Context:** Based on full audit of 180+ live pages in dist/, cross-referenced against site-architecture.md, navigation.md, and samotics-sitemap-recommendation.md

---

## Implementation Log (29 March 2026)

All core recommendations have been executed. Summary of changes:

| Change | Files affected | Status |
|--------|---------------|--------|
| Deleted duplicate campaign page (canned-motor-pumps-b) | 1 | ✅ Done |
| Created redirect: /problem/ → /blind-spot/ | 1 | ✅ Done |
| Created redirect: /proximity-penalty/ → /blind-spot/proximity-penalty/ | 1 | ✅ Done |
| Created redirect: /industries/energy-efficiency/ → /platform/sam4/ | 1 | ✅ Done |
| Created 36 case study redirects (/resources/case-studies/ → /proof/case-studies/) | 36 | ✅ Done |
| Updated internal case study links to avoid redirect chains | 183 files, 292 replacements | ✅ Done |
| Restructured header nav (removed Blind Spot dropdown, expanded Technology/Platform/Resources) | 183+ files | ✅ Done |
| Restructured footer nav to match header | 182 files | ✅ Done |
| Merged /platform/service-model/ content into /platform/sam4/#service-model | 1 merge + redirect + 359 link updates | ✅ Done |
| Merged /resources/business-case-toolkit/ into /resources/champion-enablement-kit/ | 1 merge + redirect | ✅ Done |
| Updated all /platform/service-model nav links to direct /platform/sam4/#service-model | 359 files | ✅ Done |

**Total redirects created:** 42 (all verified — every target page exists)
**Total files modified:** 183+ (nav, footer, internal links)

**Not yet executed:**
- /platform/scaling/ and /platform/sam4-x/ — exist in repo but not in new nav. Decision pending: are these live pages or drafts?
- /technology/how-it-works/ — may be redundant with /technology/how-sam4-works/. Already redirects.
- /industries/all/ — no nav path. Could serve as Industries dropdown landing page.

---

## Executive Summary

The site has grown beyond its original architecture. There are 223 published pages, but the navigation only surfaces ~25 of them. The result: dozens of substantive pages — blog posts, tools, enablement kits, case studies — have no primary navigation visibility and, in many cases, weak internal-link support.

Five structural problems need fixing:

1. **"The Blind Spot" occupies a top-level nav slot it doesn't earn.** It's a storytelling device, not a navigation category. First-time visitors don't know what it means.
2. **Resources is completely absent from the nav.** 130+ pages (blog, news, knowledge base, whitepapers, tools, enablement kits) have zero nav visibility.
3. **Duplicate pages exist at multiple URLs.** /problem/ and /blind-spot/ serve identical content. /proximity-penalty/ exists at two paths. 16 case studies are duplicated across /proof/ and /resources/.
4. **The Platform dropdown hides 4 substantive pages.** Integrations, Scaling, Service Model, and SAM4-X all have content but no nav path.
5. **Energy Efficiency still sits under Industries.** It's not an industry. This was flagged months ago.

---

## Current State

### Live Navigation (as built)

```
[Logo]  The Blind Spot ▾  Technology ▾  Assets ▾  Platform ▾  Industries ▾  Proof  About  [Asset Audit] [Request a Demo]
```

7 top-level items + 2 CTAs. The nav is consistent across all pages.

#### Dropdown contents (current)

**The Blind Spot** (3 items)
- The Blind Spot → /blind-spot
- The Visibility Layer → /blind-spot/visibility-layer
- The Proximity Penalty → /blind-spot/proximity-penalty

**Technology** (3 items)
- Electrical Signature Analysis → /technology/esa
- ESA & Vibration → /technology/esa-vs-vibration
- Technical Deep Dive → /technology/how-sam4-works

**Assets** (6 items)
- Pumps → /platform/what-we-monitor/pumps
- Compressors → /platform/what-we-monitor/compressors
- Fans & Blowers → /platform/what-we-monitor/fans-blowers
- Conveyors → /platform/what-we-monitor/conveyors
- Transmissions → /platform/what-we-monitor/transmissions
- All Assets & Motors → /platform/what-we-monitor

**Platform** (3 items)
- SAM4 Platform → /platform/sam4
- How It Installs → /platform/how-it-installs
- Security & Compliance → /platform/security

**Industries** (6 items)
- Water & Wastewater → /industries/water
- Oil & Gas → /industries/oil-gas
- Metals & Mining → /industries/metals-mining
- Chemicals → /industries/chemicals
- Pulp & Paper → /industries/pulp-paper
- Airports → /industries/airports

**Proof** — direct link → /proof
**About** — direct link → /about

### Planned Navigation (from site-architecture.md and navigation.md)

```
[Logo]  Problem  Technology ▾  Platform ▾  Industries ▾  Proof  About  [Request a Demo]
```

Key differences from what was built: Problem was a direct link (not a dropdown). Assets was under Platform (not separate). Resources was planned as a top-level dropdown in the sitemap recommendation but excluded from the navigation spec.

### Complete Page Inventory (180+ pages)

#### Pages IN the navigation (25 pages reachable via nav)

| Section | Pages in nav | Count |
|---------|-------------|-------|
| The Blind Spot | /blind-spot, /blind-spot/visibility-layer, /blind-spot/proximity-penalty | 3 |
| Technology | /technology/esa, /technology/esa-vs-vibration, /technology/how-sam4-works | 3 |
| Assets | /platform/what-we-monitor + 5 asset pages | 6 |
| Platform | /platform/sam4, /platform/how-it-installs, /platform/security | 3 |
| Industries | /industries/water, oil-gas, metals-mining, chemicals, pulp-paper, airports | 6 |
| Proof | /proof | 1 |
| About | /about | 1 |
| CTAs | /contact/asset-audit, /contact | 2 |

#### Pages NOT in the navigation (155+ pages with no primary nav visibility)

Note: "not in the navigation" means no primary nav link exists. Some of these pages may be reachable via hub pages, contextual links, or XML sitemap — but they lack the discoverability that nav placement provides. Pages marked with ★ are also weakly internally linked (few or no inbound links from other pages).

**Platform pages with substantive content (4 pages)**
- /platform/integrations (68 KB) — was in original nav plan
- /platform/scaling (68 KB) — fleet scaling story
- /platform/service-model (67 KB) — managed service explanation
- /platform/sam4-x (68 KB) — SAM4-X product page

**Technology pages (2 pages)**
- /technology/detection-boundaries (71 KB) — unique differentiation content
- /technology (hub, 49 KB) — section landing page

**Platform hub and industries hub**
- /platform (hub, 76 KB) — section landing
- /industries (hub, 73 KB) — section landing
- /industries/all (94 KB) — full asset matrix
- /industries/energy-efficiency (72 KB) — misplaced under industries

**Resources — entire section hidden (130+ pages)**
- /resources (hub, 76 KB)
- /resources/blog + 37 blog posts
- /resources/news + 31 news articles
- /resources/knowledge-base + 13 KB articles
- /resources/whitepapers
- /resources/case-studies + 34 case studies
- /resources/champion-enablement-kit (73 KB)
- /resources/engineering-faq (86 KB)
- /resources/engineering-proof-pack (73 KB)
- /resources/business-case-toolkit (74 KB)
- /resources/co-development (78 KB)
- /resources/roi-calculator (74 KB)

**Proof section — 50+ case studies and detection stories hidden**
- /proof/case-studies (hub) + 36 individual case studies
- /proof/southern-water, /proof/vitens, /proof/nyrstar, /proof/thyssenkrupp, /proof/schiphol (customer stories)
- 16 detection stories (inlet-screw-monitoring, cavitation-anolyte-pump, etc.)

**Tools**
- /tools (hub, 63 KB)
- /tools/coverage-calculator

**Other**
- /careers (52 KB)
- /partners + /partners/abb
- /campaigns/canned-motor-pumps, /campaigns/canned-motor-pumps-b

**Duplicate URLs (identical content at two paths)**
- /problem (68 KB) = /blind-spot (68 KB)
- /proximity-penalty (72 KB) = /blind-spot/proximity-penalty (72 KB)

**Legacy redirect**
- /technology/how-it-works (491 bytes) → redirects to /technology/how-sam4-works

**Duplicate case studies (16 pages exist under both /proof/ and /resources/)**
- aeration-blowers-energy-waste-reduction-case-study
- booster-pump-energy-optimization-case-study
- heated-godet-roll-fault-detection-case-study
- hot-strip-mill-degrading-rollers
- how-arcelormittal-prevented-31-hours-of-downtime
- how-vitens-increased-operational-efficiency
- how-zinc-smelter-nyrstar-got-800-roi
- identifying-and-fixing-a-broken-sine-wave-filter-in-esps
- improving-baggage-handling-reliability-at-london-stansted
- improving-submersible-pump-efficiency-at-sabesp
- oxidation-ditch-rotor-fault-detection-case-study
- prevent-exhaust-fan-failure-in-wood-manufacturing
- reducing-wastewater-inlet-station-energy-costs
- rightsizing-booster-pumps-to-save-wasted-energy
- southern-waters-success-story
- (plus 2 partial overlaps with different slugs for same story)

---

## Recommendations

### 1. Remove "The Blind Spot" from Top-Level Navigation

**Problem:** "The Blind Spot" is a category-creation narrative, not a navigation destination. Industrial buyers scanning the nav for "do you monitor my pumps?" or "how does ESA work?" won't click it — they don't know what it means yet. It serves awareness-stage visitors, but nav should serve evaluation-stage visitors who are already on the site.

**Recommendation:** Remove as a top-level menu item. Three options for where the content lives:

| Option | How it works | Pros | Cons |
|--------|-------------|------|------|
| **A. Nest under Technology** | Add "The Monitoring Blind Spot" as first item in Technology dropdown. It becomes the "why" that leads to the "how" (ESA, How SAM4 Works). | Preserves discoverability. Mirrors buyer journey: problem → technology → platform. | Technology dropdown grows to 5 items. |
| **B. Homepage + contextual links only** | Blind spot narrative lives on homepage hero and gets linked from technology/industry pages. Pages still exist, just no nav feature. | Cleanest nav. Forces the homepage to do its job. | Three substantive pages lose direct nav access. |
| **C. Footer link** | "Why Samotics" or "The Problem" link in footer. | Discoverable for interested visitors. Low-friction change. | Footer links get low traffic. |

**Recommended:** Option A. Nest under Technology as the opening item.

**What happens to duplicate URLs:**
- /problem/ → 301 redirect to /blind-spot/
- /proximity-penalty/ (root) → 301 redirect to /blind-spot/proximity-penalty/
- Keep /blind-spot/, /blind-spot/visibility-layer/, /blind-spot/proximity-penalty/ as canonical URLs

### 2. Add Resources to Top-Level Navigation

**Problem:** 130+ content pages have no nav path. Blog, news, knowledge base, whitepapers, engineering FAQ, champion enablement kit, business case toolkit, ROI calculator — all invisible. This is your entire SEO foundation and mid-funnel content.

**Recommendation:** Add Resources as a top-level dropdown.

**Resources dropdown contents:**

| Label | URL | Why it earns a slot |
|-------|-----|-------------------|
| Blog | /resources/blog | 37 posts. SEO foundation. Top-of-funnel. |
| Knowledge Base | /resources/knowledge-base | 11 technical articles. Mid-funnel education. |
| News & Press | /resources/news | 36 articles. Credibility signal. |
| Engineering FAQ | /resources/engineering-faq | Engineers click FAQs. High-trust format. |
| Tools & Calculators | /tools | Coverage calculator + ROI calculator. Lead gen. |

**Pages that stay off the dropdown but get linked from the Resources hub page:**
- /resources/champion-enablement-kit — link from Resources hub + post-demo follow-up emails
- /resources/engineering-proof-pack — link from Resources hub + Proof page
- /resources/business-case-toolkit — link from Resources hub + industry pages
- /resources/co-development — link from Resources hub + Partners page
- /resources/whitepapers — link from Resources hub (gated content section)

### 3. Expand the Platform Dropdown

**Problem:** Platform shows 3 items. But 4 additional pages with substantive content (65–68 KB each) are invisible: Integrations, Service Model, Scaling, SAM4-X.

**Recommendation:** Add Integrations and Service Model to the dropdown. Keep Scaling and SAM4-X as links from the Platform hub page (dropdown shouldn't exceed 5–6 items).

**Revised Platform dropdown:**

| Label | URL | Why |
|-------|-----|-----|
| SAM4 Platform | /platform/sam4 | Primary platform page |
| How It Installs | /platform/how-it-installs | Removes deployment objection |
| Security & Compliance | /platform/security | CTO/Digital Lead gatekeeper page |
| Integrations | /platform/integrations | Enterprise evaluation (CMMS, SCADA, API). Was in original nav. |
| Service Model | /platform/service-model | Explains managed service. Key for Operations Directors. |

**Linked from Platform hub (not in dropdown):**
- /platform/scaling — Fleet scaling story. Relevant but secondary.
- /platform/sam4-x — SAM4-X product variant. Niche audience.

### 4. Expand the Technology Dropdown

**Problem:** Detection Boundaries is a unique differentiation page (71 KB of content) with no nav path. If The Blind Spot is nested here per Recommendation 1, Technology becomes the problem-to-proof narrative section.

**Revised Technology dropdown:**

| Label | URL | Why |
|-------|-----|-----|
| The Monitoring Blind Spot | /blind-spot | Problem framing. "Why" before "how". |
| Electrical Signature Analysis | /technology/esa | Core science page. |
| ESA & Vibration | /technology/esa-vs-vibration | #1 objection handler. |
| How SAM4 Works | /technology/how-sam4-works | End-to-end data flow. |
| Detection Boundaries | /technology/detection-boundaries | What ESA can and can't detect. Honesty signal. |

5 items. Acceptable for a dropdown. The Technology hub page (/technology/) links to all of these plus the Blind Spot sub-pages (Visibility Layer, Proximity Penalty).

### 5. Consider Moving About to Footer Only (Testable)

**Problem:** About is a credibility-check page, not a primary destination. The navigation spec itself says CTOs "spend 30 seconds here." It doesn't obviously earn a top-level nav slot when Resources — serving all funnel stages — has none.

**However:** Samotics sells to enterprise industrial buyers in a high-trust category. About carries more weight here than in typical SaaS — it signals company scale, ABB partnership, and funding maturity. Removing it from the nav could slightly hurt brand trust for first-time visitors, particularly if the Proof and Technology pages don't adequately convey company credibility.

**Recommendation:** Testable option, not a clear-cut change. Two paths:

| Path | Nav structure | Trade-off |
|------|-------------|-----------|
| **A. Remove About from nav** | 6 top-level items + 2 CTAs. Cleanest nav. | Risk: slight credibility loss for cold visitors. Mitigate by ensuring Proof and Technology pages surface company scale. |
| **B. Keep About in nav** | 7 top-level items + 2 CTAs. At the cognitive limit but workable. | Safer for trust. Costs one nav slot. |

If About stays, the nav becomes:

```
[Logo]  Technology ▾  Platform ▾  Assets ▾  Industries ▾  Proof  Resources ▾  About  [Asset Audit] [Request a Demo]
```

7 items + 2 CTAs. Still functional, and every item maps to a buyer need.

**How to decide:** Check click-through data on the current About nav link. If it's in the bottom 2 by clicks, the footer is fine. If it's mid-pack or higher, keep it. If no data is available, keep it — the cost of one extra nav slot is lower than the cost of losing trust signal.

### 6. Consolidate Case Studies Under One Path

**Problem:** Case studies exist under both /proof/case-studies/ (37 pages) and /resources/case-studies/ (35 pages), with 16 duplicates. This dilutes link equity, confuses internal linking, and doubles maintenance.

**Recommendation:**
- **Canonical location:** /proof/case-studies/ — case studies are proof, not resources
- **Action:** 301 redirect all /resources/case-studies/* URLs to /proof/case-studies/* equivalents
- **Unique-to-resources studies (16 pages):** Move to /proof/case-studies/ with new slugs matching the proof naming convention
- **Total after consolidation:** ~53 unique case studies under /proof/case-studies/

**Implementation warning — avoid redirect chains:** When setting up 301 redirects from /resources/case-studies/* to /proof/case-studies/*, also update all internal links that point to the old /resources/ URLs. This includes links within the 37 blog posts, knowledge base articles, and industry pages. If you only create redirects without updating source links, you create redirect chains (page A links to old URL → 301 → new URL) which slow crawl speed and leak marginal link equity. Run a grep for `/resources/case-studies/` across all HTML files and update links to point directly to /proof/case-studies/.

### 7. Remove /industries/energy-efficiency/

**Problem:** Energy efficiency is not an industry. It confuses the Industries section. Flagged in the original sitemap recommendation months ago.

**Recommendation:** 301 redirect to /platform/sam4 (energy analytics is a SAM4 feature). Alternatively, create /use-cases/energy-efficiency/ if the content warrants a standalone page outside Industries.

Remove from the Industries dropdown and the /industries/ hub page.

### 8. Clarify /industries/all/ vs /platform/what-we-monitor/

**Problem:** Two pages serve a similar purpose — showing the full asset matrix.

**Recommendation:** Evaluate whether these serve different audiences. If /industries/all/ is an industry-lens view (assets by sector) and /platform/what-we-monitor/ is an asset-lens view (assets by type), keep both but clarify the distinction in the content. If they substantially overlap, redirect /industries/all/ → /platform/what-we-monitor/.

### 9. Add Missing Footer Links

**Current footer status:** Not fully audited, but the following pages should be in the footer if they aren't already:

| Column | Links |
|--------|-------|
| **Technology** | Electrical Signature Analysis, ESA & Vibration, How SAM4 Works, Detection Boundaries |
| **Platform** | SAM4 Platform, What We Monitor, How It Installs, Security, Integrations |
| **Industries** | Water, Oil & Gas, Metals & Mining, Chemicals, Pulp & Paper, Airports |
| **Resources** | Blog, Knowledge Base, News, Engineering FAQ, Tools |
| **Company** | About, Partners, Careers, Contact |
| **Legal** | Privacy, Terms, Cookies |

### 10. Pages That Are Missing (to build)

| Page | Purpose | Priority |
|------|---------|----------|
| Custom 404 page | Branded error page with search + key links | Medium |
| /resources/webinars/ | On-demand webinar hub (if content exists) | Low |

The original sitemap recommendation called for /contact/partner-inquiry/ and /resources/whitepapers/ as gated content. Both are Phase 2.

---

## Decision Matrix

| Decision | Recommended | Alternative | Main trade-off | Confidence |
|----------|-------------|-------------|----------------|------------|
| Remove Blind Spot from top nav | Yes — nest under Technology | Keep as top-level item | Category storytelling vs nav clarity for evaluation-stage visitors | High |
| Add Resources to top nav | Yes — as dropdown | Keep hidden; rely on footer/hub links | Nav slot cost vs surfacing 130+ orphaned pages | High |
| Expand Platform dropdown | Yes — add Integrations + Service Model | Keep at 3 items; rely on hub page | Dropdown density vs discoverability of enterprise evaluation pages | High |
| Add Detection Boundaries to Technology | Yes | Keep off nav; link from Technology hub | Dropdown grows to 5 items vs surfacing unique differentiation content | High |
| Move About to footer | Testable — check click data first | Keep in nav | Trust signal vs nav economy. Enterprise industrial buyers value About more than SaaS buyers. | Medium |
| Proof format | Direct link (no dropdown) | Dropdown: Customer Stories / Case Studies / Detection Stories | Simplicity vs discoverability. Works only if Proof hub is well-designed and filterable. | Medium |
| Case study canonical path | /proof/case-studies/ | /resources/case-studies/ | Proof-first logic vs content-library logic. Proof is stronger for this audience. | High |
| Energy Efficiency placement | Remove from Industries; redirect to /platform/sam4 | Create /use-cases/energy-efficiency/ | Clean taxonomy vs preserving dedicated energy content | High |
| Assets as top-level nav | Keep separate from Platform | Merge back under Platform (original plan) | One extra nav slot vs one-click access to "do you monitor my equipment?" — the #1 buyer question | High |
| Tools placement | Under Resources dropdown | Standalone top-level or under Platform | Cleaner nav vs direct access to lead-gen tools | Medium |

---

## Recommended Sitemap (Full Hierarchy)

### Navigation-Accessible Pages

```
HOME /

TECHNOLOGY (Education — "Why ESA")
├── /blind-spot — The Monitoring Blind Spot (awareness entry point)
│   ├── /blind-spot/visibility-layer — The Visibility Layer
│   └── /blind-spot/proximity-penalty — The Proximity Penalty
├── /technology/esa — Electrical Signature Analysis
├── /technology/esa-vs-vibration — ESA & Vibration
├── /technology/how-sam4-works — How SAM4 Works
└── /technology/detection-boundaries — Detection Boundaries

PLATFORM (Evaluation — "What you get")
├── /platform/sam4 — SAM4 Platform
├── /platform/how-it-installs — How It Installs
├── /platform/security — Security & Compliance
├── /platform/integrations — Integrations
├── /platform/service-model — Service Model
├── /platform/scaling — Scaling (hub-linked, not in dropdown)
└── /platform/sam4-x — SAM4-X (hub-linked, not in dropdown)

ASSETS (Evaluation — "Do you monitor my equipment?")
├── /platform/what-we-monitor — All Assets & Motors (hub)
├── /platform/what-we-monitor/pumps
├── /platform/what-we-monitor/compressors
├── /platform/what-we-monitor/fans-blowers
├── /platform/what-we-monitor/conveyors
├── /platform/what-we-monitor/transmissions
├── /platform/what-we-monitor/esps
├── /platform/what-we-monitor/mv-motors
├── /platform/what-we-monitor/lv-motors
├── /platform/what-we-monitor/canned-motor-pumps
├── /platform/what-we-monitor/agitators-mixers
└── /platform/what-we-monitor/archimedes-screws

INDUSTRIES (Evaluation — "It works for my sector")
├── /industries — Hub
├── /industries/water
├── /industries/oil-gas
├── /industries/metals-mining
├── /industries/chemicals
├── /industries/pulp-paper
└── /industries/airports

PROOF (Validation — "Prove it")
├── /proof — Hub (filterable grid)
├── /proof/southern-water — Customer story
├── /proof/vitens — Customer story
├── /proof/nyrstar — Customer story
├── /proof/thyssenkrupp — Customer story
├── /proof/schiphol — Customer story
├── /proof/case-studies — Case study archive (hub)
│   └── ~53 individual case studies
└── 16 detection stories (e.g., /proof/cavitation-anolyte-pump)

RESOURCES (All stages — SEO, education, lead gen)
├── /resources — Hub
├── /resources/blog + 37 posts
├── /resources/knowledge-base + 13 articles
├── /resources/news + 31 articles
├── /resources/whitepapers (Phase 2, gated)
├── /resources/engineering-faq
├── /resources/champion-enablement-kit
├── /resources/engineering-proof-pack
├── /resources/business-case-toolkit
├── /resources/co-development
└── /resources/roi-calculator

TOOLS
├── /tools — Hub
└── /tools/coverage-calculator
```

### Footer-Only Pages

```
COMPANY (footer; About also in primary nav if kept — see Rec 5)
├── /about
├── /partners
├── /partners/abb
├── /careers
└── /contact
    └── /contact/asset-audit

LEGAL
├── /privacy
├── /terms
└── /cookies

CAMPAIGNS (no nav, no footer — landing pages for ads/email)
├── /campaigns/canned-motor-pumps
└── /campaigns/canned-motor-pumps-b
```

### Redirects Required

| From | To | Type | Reason |
|------|----|------|--------|
| /problem | /blind-spot | 301 | Duplicate content |
| /proximity-penalty | /blind-spot/proximity-penalty | 301 | Duplicate content at root level |
| /industries/energy-efficiency | /platform/sam4 | 301 | Not an industry |
| /resources/case-studies/* (all 34) | /proof/case-studies/* (matching slugs) | 301 | Consolidate under Proof |
| /technology/how-it-works | /technology/how-sam4-works | Keep | Already a redirect (491-byte stub) |

---

## Recommended Navigation (Final)

### Primary Nav (Desktop)

```
[Logo]   Technology ▾   Platform ▾   Assets ▾   Industries ▾   Proof   Resources ▾   About   [Asset Audit] [Request a Demo]
```

7 top-level items + 2 CTAs (if About is kept — see Recommendation 5 for the data-driven test to decide)

### Technology ▾

| Label | URL | Subtitle |
|-------|-----|----------|
| The Monitoring Blind Spot | /blind-spot | Why 30–40% of critical assets go unmonitored |
| Electrical Signature Analysis | /technology/esa | The science behind SAM4 |
| ESA & Vibration | /technology/esa-vs-vibration | How ESA and vibration work together |
| How SAM4 Works | /technology/how-sam4-works | Detection accuracy, methodology, and performance |
| Detection Boundaries | /technology/detection-boundaries | What ESA can and can't detect |

### Platform ▾

| Label | URL | Subtitle |
|-------|-----|----------|
| SAM4 Platform | /platform/sam4 | Dashboard, diagnostics, and analytics |
| How It Installs | /platform/how-it-installs | <60 minutes, back online same shift |
| Security & Compliance | /platform/security | ISO 27001, ISO 9001, NIS2 aligned, cellular |
| Integrations | /platform/integrations | CMMS, SCADA, and API connectivity |
| Service Model | /platform/service-model | Managed monitoring, not just software |

### Assets ▾

| Label | URL | Subtitle |
|-------|-----|----------|
| Pumps | /platform/what-we-monitor/pumps | Centrifugal, submersible, borehole, and canned motor |
| Compressors | /platform/what-we-monitor/compressors | Reciprocating, screw, and centrifugal |
| Fans & Blowers | /platform/what-we-monitor/fans-blowers | Axial, centrifugal, and process air |
| Conveyors | /platform/what-we-monitor/conveyors | Belt, screw, and chain conveyors |
| Transmissions | /platform/what-we-monitor/transmissions | Gearboxes, couplings, and belt drives |
| All Assets & Motors | /platform/what-we-monitor | Full detection matrix by asset type |

### Industries ▾

| Label | URL |
|-------|-----|
| Water & Wastewater | /industries/water |
| Oil & Gas | /industries/oil-gas |
| Metals & Mining | /industries/metals-mining |
| Chemicals | /industries/chemicals |
| Pulp & Paper | /industries/pulp-paper |
| Airports | /industries/airports |

### Proof

Direct link → /proof (no dropdown)

### Resources ▾

| Label | URL | Subtitle |
|-------|-----|----------|
| Blog | /resources/blog | Industry insights and detection stories |
| Knowledge Base | /resources/knowledge-base | Technical articles and guides |
| News & Press | /resources/news | Announcements and partnerships |
| Engineering FAQ | /resources/engineering-faq | Common technical questions answered |
| Tools & Calculators | /tools | Coverage calculator, ROI calculator |

---

## Implementation Priority

| # | Action | Pages affected | Impact | Effort |
|---|--------|---------------|--------|--------|
| 1 | Set up 301 redirects for duplicates | /problem, /proximity-penalty, /resources/case-studies/* | SEO hygiene. Eliminates duplicate content penalty risk. | Low |
| 2 | Add Resources to nav | 1 nav change, surfaces 130+ pages | Biggest single improvement. Unlocks entire content library. | Low |
| 3 | Remove The Blind Spot from top-level nav; nest under Technology | 1 nav change | Frees slot for Resources. Better buyer journey alignment. | Low |
| 4 | Decide on About: keep in nav or move to footer (testable — see Rec 5) | 1 nav change + footer check | Data-dependent. Check click-through rates first. | Low |
| 5 | Expand Platform dropdown (add Integrations, Service Model) | 1 nav change | Surfaces key enterprise evaluation pages. | Low |
| 6 | Add Detection Boundaries to Technology dropdown | 1 nav change | Surfaces differentiation content. | Low |
| 7 | Redirect /industries/energy-efficiency | 1 redirect | Cleans up Industries section. | Low |
| 8 | Consolidate case studies (redirect /resources/case-studies/* → /proof/case-studies/*) | 34 redirects | Clean content architecture. Single source of truth. | Medium |
| 9 | Update footer nav (add Careers, Partners, full link set) | Footer template change | Professional completeness. | Low |
| 10 | Build custom 404 page | 1 new page | UX polish. | Medium |

Items 1–7 are all nav/redirect changes with high impact and low effort. They should ship together as a single update.

---

## Success Criteria

After rollout, the site architecture should pass these tests:

**Navigation completeness**
- Every strategic section (Technology, Platform, Assets, Industries, Proof, Resources) has a primary nav path
- No section with 10+ pages is absent from the navigation

**Internal linking**
- Every non-campaign page has at least one internal-link path from a hub page, index page, or contextual module
- No page requires more than 3 clicks from the homepage to reach

**Duplicate elimination**
- No two URLs serve identical or near-identical content
- Every page has a self-referencing canonical tag
- Zero redirect chains (every internal link points to the canonical URL, not a redirect)

**Taxonomy discipline**
- Each top-level nav item maps to a distinct buyer question (Technology = "How does it work?", Platform = "What do I get?", Assets = "Do you monitor my equipment?", Industries = "Does it work in my sector?", Proof = "Prove it.", Resources = "Help me learn / build the case.")
- No page sits in a section whose taxonomy contradicts its function (e.g., no outcomes listed as industries)

**Measurable outcomes (track after 90 days)**
- Pages per session: increase vs baseline (more content discoverable = deeper visits)
- Bounce rate on hub pages: decrease vs baseline
- Organic impressions on blog/news/KB pages: increase (nav inclusion improves crawl frequency)
- Click-through rate on Resources nav item: establishes baseline for future optimisation

---

## Appendix: Page Count Summary

| Category | Current pages | In nav | Hidden | Action |
|----------|--------------|--------|--------|--------|
| Homepage | 1 | 1 | 0 | — |
| Blind Spot / Problem | 5 (3 unique + 2 duplicates) | 3 | 2 dupes | Redirect dupes. Nest under Technology. |
| Technology | 6 (5 unique + 1 redirect) | 3 | 2 + 1 redirect | Add Detection Boundaries to nav. Keep redirect. |
| Platform | 8 (7 unique + 1 hub) | 3 | 5 | Add Integrations + Service Model to nav. Hub-link others. |
| Assets | 12 (11 unique + 1 hub) | 6 | 6 | Nav covers main 5 + hub. ESPs, MV/LV motors, canned motor pumps, agitators, Archimedes screws linked from hub. |
| Industries | 9 (7 unique + 1 hub + 1 misplaced) | 6 | 3 | Remove energy-efficiency. Hub-link /industries/all/. |
| Proof | 44 (hub + 5 customer stories + 1 detection accuracy + 37 case studies) | 1 | 43 | All discoverable via Proof hub. No nav change needed. |
| Resources | 130+ (hub + 37 blog + 31 news + 13 KB + 36 case studies + tools + enablement) | 0 | 130+ | Add Resources dropdown. Biggest gap. |
| Tools | 2 (hub + calculator) | 0 | 2 | Surface via Resources dropdown. |
| Company | 4 (about, partners, partners/abb, careers) | 1 | 3 | Footer links. |
| Contact | 2 (contact + asset-audit) | 2 (CTAs) | 0 | — |
| Legal | 3 | 0 | 3 | Footer links (likely already there). |
| Campaigns | 2 | 0 | 2 | Intentionally hidden (ad landing pages). |
| **Total** | **~223 pages (some duplicates)** | **~25** | **~198** | |

After implementing these recommendations, approximately 45 pages will be directly nav-accessible (up from 25), and all remaining pages will have at least one internal link path via hub pages, footer, or contextual links.
