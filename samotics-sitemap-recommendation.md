# Samotics Website — Recommended Sitemap

## Goals
1. **Position Samotics as the global leader in ESA**
2. **Raise credibility as an enterprise-ready solution**
3. **Lead generation**

---

## Buyer Journey Stages

The sitemap maps to five stages of the B2B industrial buyer journey:

| Stage | Buyer question | Site section |
|-------|---------------|--------------|
| **Awareness** | "I have a reliability / monitoring problem" | Problem |
| **Education** | "What is ESA? How does it compare?" | Technology |
| **Evaluation** | "Does it work for my industry? Is it enterprise-grade?" | Platform, Industries |
| **Validation** | "Prove it. Show me numbers and names." | Proof |
| **Action** | "I want to start." | Contact, Tools |

Resources and Blog serve all stages — top-of-funnel SEO, mid-funnel education, bottom-funnel business case support.

---

## Recommended Sitemap

Legend:
- ✅ = Exists with Bricks content
- 🔲 = Page exists but empty / needs content
- 🆕 = New page needed
- ❌ = Remove / merge

```
HOME ✅

PROBLEM (Awareness)
├── /problem/ — The Reliability Blind Spot ✅
└── /proximity-penalty/ — The Proximity Penalty ✅

TECHNOLOGY (Education — "Why ESA")
├── /technology/ — Hub: Why ESA Matters 🔲 needs content
├── /technology/esa/ — Electrical Signature Analysis ✅
├── /technology/how-it-works/ — From Signal to Insight ✅
└── /technology/esa-vs-vibration/ — ESA vs Vibration Analysis ✅

PLATFORM (Evaluation — "What you get")
├── /platform/ — Hub: SAM4 Overview 🔲 needs content
├── /platform/sam4/ — The SAM4 Platform ✅
├── /platform/what-we-monitor/ — Assets We Monitor ✅
├── /platform/how-it-installs/ — How It Installs ✅
├── /platform/integrations/ — Integrations ✅
└── /platform/security/ — Security & Compliance ✅

INDUSTRIES (Evaluation — "It works for me")
├── /industries/ — Hub: Industries Overview 🔲 needs content
├── /industries/water/ — Water & Wastewater ✅
├── /industries/oil-gas/ — Oil & Gas ✅
├── /industries/metals-mining/ — Metals & Mining ✅
├── /industries/chemicals/ — Chemicals ✅
├── /industries/pulp-paper/ — Pulp & Paper ✅
└── /industries/airports/ — Airports 🆕

PROOF (Validation — "It works, period")
├── /proof/ — Hub: Customer Results ✅
├── /proof/yorkshire-water/ — Yorkshire Water ✅
├── /proof/southern-water/ — Southern Water 🔲
├── /proof/vitens/ — Vitens 🔲
├── /proof/nyrstar/ — Nyrstar 🔲
├── /proof/thyssenkrupp/ — thyssenkrupp 🔲
├── /proof/schiphol/ — Schiphol Airport 🔲
└── /proof/case-studies/ — Case Study Archive 🆕
    └── (35 individual case study posts, imported from old site)

RESOURCES (All stages — SEO + lead gen)
├── /resources/ — Hub: Resource Centre 🔲 needs content
├── /resources/blog/ — Blog 🔲
│   └── (36 blog posts + 12 KB articles, imported)
├── /resources/whitepapers/ — Whitepapers & Guides 🆕 (gated)
├── /resources/webinars/ — Webinars 🔲
│   └── (7 webinar posts, imported)
└── /resources/news/ — News & Press 🆕
    └── (36 news posts, imported)

TOOLS (Evaluation + Lead gen)
├── /tools/ — Hub 🔲 needs content
├── /tools/coverage-calculator/ — Coverage Calculator ✅
├── /tools/asset-audit/ — Asset Audit ✅ (move from /contact/)
└── /tools/roi-calculator/ — ROI Calculator 🆕

ABOUT (Credibility)
├── /about/ — Company ✅
├── /about/partners/ — Partners ✅ (move from /partners/)
└── /about/abb/ — ABB Partnership ✅

CONTACT (Action)
├── /contact/ — Request a Demo ✅
└── /contact/partner-inquiry/ — Partner Inquiry ✅

LEGAL (Footer only)
├── /privacy-policy/ 🔲
├── /cookie-policy/ 🔲
└── /terms-of-use/ 🔲
```

---

## What's New vs Current

### Pages to ADD (6)

| Page | Why | Goal served |
|------|-----|-------------|
| `/industries/airports/` | Requested. Growing vertical with Schiphol + Stansted proof. | Credibility |
| `/proof/case-studies/` | Archive page for 35 imported case studies. Proof at scale. | Credibility, SEO |
| `/resources/whitepapers/` | Gated content (email capture). Business case guides, ROI frameworks, technical briefs. | Lead gen |
| `/resources/news/` | Press releases, partnership announcements. 36 existing posts to import. | Credibility, SEO |
| `/tools/roi-calculator/` | Interactive tool. Captures email in exchange for custom ROI report. High-intent lead magnet. | Lead gen |
| 404 page | Custom branded 404 with search + key links. | UX |

### Pages to REMOVE or MERGE (4)

| Page | Action | Why |
|------|--------|-----|
| `/industries/energy-efficiency/` | Move to `/platform/sam4/` as a feature section, or merge into a use-case CTA block on the SAM4 page | Not an industry. Confuses the nav. The energy efficiency story belongs under what SAM4 does. |
| `/resources/esg-reporting/` | Same — move to a feature/use-case section on SAM4 or a blog post | Not a resource page. It's a use case. |
| `/resources/downloads/` | Merge into `/resources/whitepapers/` | Redundant. One gated content hub is cleaner. |
| Duplicate `energy-efficiency` pages (2 exist) | Delete one | Two published pages with same slug in different parents. |

### Pages to MOVE (re-parent for clean URLs)

| Current URL | Target URL | Issue |
|-------------|------------|-------|
| `/industries__trashed/chemicals/` | `/industries/chemicals/` | Trashed parent in URL |
| `/industries__trashed/oil-gas/` | `/industries/oil-gas/` | Same |
| `/industries__trashed/metals-mining/` | `/industries/metals-mining/` | Same |
| `/industries__trashed/pulp-paper/` | `/industries/pulp-paper/` | Same |
| `/industries__trashed/water/` | `/industries/water/` | Same |
| `/technology__trashed/esa/` | `/technology/esa/` | Same |
| `/technology__trashed/esa-vs-vibration/` | `/technology/esa-vs-vibration/` | Same |
| `/technology__trashed/how-it-works/` | `/technology/how-it-works/` | Same |
| `/proof__trashed/yorkshire-water/` | `/proof/yorkshire-water/` | Same |
| `/proof__trashed/*` (all proof children) | `/proof/*` | Same |
| `/contact/asset-audit/` | `/tools/asset-audit/` | Better fit under Tools |
| `/partners/` | `/about/partners/` | Group under About |

### Hub Pages to FILL (6)

These exist but have zero content. Each needs a strong landing page:

| Hub | Content needed |
|-----|---------------|
| `/technology/` | "Why ESA" narrative. Position ESA as the future of condition monitoring. Link to sub-pages. This is the ESA leadership page. |
| `/platform/` | SAM4 value prop summary with visual product overview. Link to sub-pages. |
| `/industries/` | Grid of industry cards with stats. "Trusted across X industries, Y countries." |
| `/resources/` | Filterable resource grid — blog, whitepapers, webinars, news. Email capture. |
| `/tools/` | Grid of interactive tools with descriptions. |
| `/proof/case-studies/` | Filterable archive of all 35 case studies. Filter by industry, asset type, KPI. |

---

## Navigation Structure

### Primary Nav

```
Problem    Technology ▾    Platform ▾    Industries ▾    Proof    Resources ▾    [Request a Demo]
```

### Mega Menu Content

**Technology**
- Why ESA (hub)
- Electrical Signature Analysis
- How It Works
- ESA vs Vibration

**Platform**
- SAM4 Platform
- What We Monitor
- How It Installs
- Integrations
- Security & Compliance

**Industries**
- Water & Wastewater
- Oil & Gas
- Metals & Mining
- Chemicals
- Pulp & Paper
- Airports

**Resources**
- Blog
- Whitepapers & Guides
- Webinars
- News & Press

### Footer

```
Column 1: Technology    Column 2: Platform     Column 3: Industries    Column 4: Company
- Why ESA              - SAM4 Platform        - Water                 - About
- How It Works         - What We Monitor      - Oil & Gas             - Partners
- ESA vs Vibration     - How It Installs      - Metals & Mining       - Contact
                       - Integrations         - Chemicals             - Careers (future)
                       - Security             - Pulp & Paper
                                              - Airports

Column 5: Resources    Column 6: Tools        Column 7: Legal
- Blog                 - Coverage Calculator   - Privacy Policy
- Whitepapers          - Asset Audit           - Cookie Policy
- Webinars             - ROI Calculator        - Terms of Use
- News
```

---

## Goal Mapping

### Goal 1 — ESA Leadership

| What sells this | Where it lives |
|----------------|----------------|
| "Why ESA" technology hub page | `/technology/` |
| ESA deep-dive (already strong) | `/technology/esa/` |
| ESA vs Vibration (already strong) | `/technology/esa-vs-vibration/` |
| Blog content on ESA topics (12 KB articles + blog posts) | `/resources/blog/` |
| Whitepapers on ESA methodology | `/resources/whitepapers/` |
| Webinars featuring ESA | `/resources/webinars/` |

Gap today: the Technology hub is empty. That's the page that should own the "Samotics = ESA" narrative. Write it.

### Goal 2 — Enterprise Credibility

| What sells this | Where it lives |
|----------------|----------------|
| Named customer stories (6 empty, 1 live) | `/proof/*` |
| 35 case studies showing breadth | `/proof/case-studies/` |
| Security & Compliance page | `/platform/security/` |
| Integrations (SCADA, historian, CMMS) | `/platform/integrations/` |
| Enterprise partner logos (ABB, Siemens, Schneider) | Trust bars + `/about/partners/` |
| News/press releases (36 posts) | `/resources/news/` |

Gap today: 6 of 7 customer story pages are empty. This is the single biggest credibility gap. Fill these first.

### Goal 3 — Lead Generation

| Conversion mechanism | Where it lives | Funnel stage |
|---------------------|----------------|--------------|
| Request a Demo CTA | `/contact/` + every page footer | Bottom |
| Asset Audit request | `/tools/asset-audit/` | Bottom |
| Coverage Calculator | `/tools/coverage-calculator/` | Mid-bottom |
| ROI Calculator (new) | `/tools/roi-calculator/` | Mid |
| Gated whitepapers (new) | `/resources/whitepapers/` | Mid |
| Webinar registration | `/resources/webinars/` | Top-mid |
| Blog (SEO traffic) | `/resources/blog/` | Top |
| Newsletter signup | Footer / resource hub | Top |

Gap today: no top-of-funnel or mid-funnel capture mechanisms exist. Blog is empty, no gated content, no ROI tool. All current conversion is bottom-funnel (demo request). That means you only capture buyers who already decided — you're missing everyone still researching.

---

## Execution Priority

| Priority | Action | Pages | Impact |
|----------|--------|-------|--------|
| **1** | Fix broken URL hierarchy | 12 pages need re-parenting | Blocks everything — broken URLs hurt SEO and credibility |
| **2** | Fill customer story pages | 6 pages (Southern Water, Vitens, Nyrstar, thyssenkrupp, Schiphol, + case study archive) | Highest credibility impact |
| **3** | Fill hub pages | Technology, Platform, Industries, Resources, Tools | Completes navigation, frames the story |
| **4** | Create Airports industry page | 1 page | Quick win, content ready |
| **5** | Import blog + news posts | ~72 posts | SEO foundation for top-of-funnel |
| **6** | Build whitepapers section + gate 2-3 pieces | 1 hub + 2-3 PDFs | First mid-funnel lead capture |
| **7** | Build ROI calculator | 1 interactive page | High-intent lead magnet |
| **8** | Fill legal pages | 3 pages | Compliance |

---

## Page Count Summary

| Category | Current (published) | Recommended | Delta |
|----------|-------------------|-------------|-------|
| Core pages | 28 with content | 28 | 0 |
| Hub pages | 6 empty | 6 filled | Fill existing |
| Industry pages | 5 live + 1 new | 6 | +1 |
| Proof pages | 1 live + 6 empty | 7 filled + archive | Fill existing + 1 new |
| Resource pages | 0 live | 4 (hub + 3 types) | +4 |
| Tool pages | 1 live | 3 | +2 |
| Legal | 0 live | 3 | Fill existing |
| Posts (imported) | 0 | ~132 | Import from old site |
| **Total pages** | **50** | **~53 pages + 132 posts** | |
