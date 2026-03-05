# Samotics Website Audit — 2 March 2026

Audited against: Brand Voice System, Brand Voice GTM Extension, Buyer Journey Framework v3.1, ICP & Buying Committee Map v3.1, User Journey Map v3.1.

191 HTML pages crawled. Navigation, content, structure, SEO, and CTAs reviewed.

---

## Overall scores

| Area | Score | Status |
|------|-------|--------|
| Navigation consistency | 10/10 | All 191 pages share identical nav |
| Footer consistency | 10/10 | Identical structure everywhere |
| Brand voice compliance | 8.5/10 | No banned terms found; proof-first, engineer-led |
| Hero messaging | 9/10 | Problem-first, specific, quantified |
| CTA strategy | 4/10 | "Request a Demo" dominates; not aligned to buyer journey |
| SEO / meta | 6/10 | 62% of titles too long; 5 duplicates; 5 missing descriptions |
| Structural completeness | 7/10 | Key GTM pages exist but gaps remain |

---

## Critical fixes (do this week)

### 1. Utility page titles show "Page not found"

5 pages have `<title>Page not found | Samotics</title>` instead of proper titles:

- `/careers/` → should be "Careers | Samotics"
- `/privacy/` → "Privacy Policy | Samotics"
- `/terms/` → "Terms of Use | Samotics"
- `/cookies/` → "Cookie Policy | Samotics"
- `/404.html` → keep as is (it's the actual 404)

These pages also lack `<meta name="description">`. Fix: add unique titles and descriptions.

**Effort:** 15 minutes.

### 2. Duplicate page titles (SEO cannibalisation)

5 detection stories share exact titles with their case study counterparts in `/resources/case-studies/`:

| Title | Page 1 | Page 2 |
|-------|--------|--------|
| "Bearing failure avoided in motor driving critical runout table roll" | /proof/case-studies/bearing-failure-motor-roll/ | /resources/case-studies/case-study-steel-runout-table-roll-bearing/ |
| "Loose cardan joint caught the same day SAM4 was installed" | /proof/case-studies/loose-cardan-joint-roll/ | /resources/case-studies/loose-cardan-joint-caught-the-same-day-sam4-was-installed/ |
| "Preventing downtime on borehole pumps" | /proof/case-studies/borehole-pump-detections/ | /resources/case-studies/preventing-downtime-on-borehole-pumps/ |
| "Preventing failure in wastewater inlet screws" | /proof/case-studies/inlet-screw-monitoring/ | /resources/case-studies/preventing-failure-in-wastewater-inlet-screws/ |
| "Three faults detected on oil transfer pump" | (check) | (check) |

Fix: Prefix detection story titles with "Detection Story:" or differentiate them. Consider whether both pages need to exist — the proof pages and case study pages likely cover the same content.

**Effort:** 20 minutes.

### 3. "Request a Demo" appears on every page — doesn't match brand voice

The header CTA on all 191 pages is "Request a Demo." The brand voice system says:

> CTA language is: Low pressure. Engineer-led. Specific.
> Example: "See real spectral data" / "Talk to an engineer" / "Review your asset class"
> Not: "Book a sales call."

"Request a Demo" is closer to generic SaaS than engineering authority.

**Recommended replacement for header CTA:** "Talk to an engineer"

This matches the GTM Extension and is used by 0 pages currently. It signals expertise, not sales pressure.

**Effort:** 30 minutes (global find-replace across nav).

---

## High-priority improvements (next 2 weeks)

### 4. CTA strategy doesn't match the User Journey Map

The User Journey Map defines 7 persona-aligned CTAs. Current usage across the site:

| GTM-defined CTA | Current usage | Should appear on |
|-----------------|---------------|-----------------|
| Calculate Your ROI | ✓ ROI calculator exists | Homepage, industry pages, /problem/ |
| Get the Engineering Proof Pack | ✗ Not used anywhere | Technology pages, ESA page |
| Schedule a Technical Deep-Dive | ✗ Not used anywhere | Platform pages, how-it-works |
| Request a Security Review | ✗ Not used anywhere | Security page, contact page |
| Book an Executive Briefing | ✗ Not used anywhere | About page, proof page |
| Start Your Asset Audit | ✓ /contact/asset-audit/ exists | Industry pages, homepage |
| Build My Business Case | ✗ Not used anywhere | Case study pages |

The contact page does offer intent-based routing (good), but individual pages don't surface the right CTA for their audience.

**Effort:** 2–3 hours to add contextual CTAs to key landing pages.

### 5. Page titles exceed 60 characters (62% of pages)

119 of 191 pages have titles that get truncated in search results. Examples:

- "Start with clarity. Know exactly where your monitoring gaps are. | Samotics" (75 chars)
- "Tell us what you need. We'll match you with the right conversation. | Samotics" (78 chars)

Fix: Shorten to pattern `[Topic] | Samotics` staying under 55 chars. For blog/case study posts, front-load the keyword.

**Effort:** 2 hours (batch script).

### 6. Platform overview page is feature-first, not outcome-first

Current hero: "SAM4: from signal to insight in minutes."

This sounds like a software pitch. Every other section of the site leads with the problem or outcome. The platform page should too.

**Better:** "Managed condition monitoring. Not another dashboard." — then list features as supporting evidence.

The GTM docs explicitly say: "We never sound like: A software vendor describing a dashboard."

**Effort:** 30 minutes.

### 7. Airports page lacks quantified proof

Every other industry page includes specific financial outcomes. Airports shows "2 major airports" but no metrics. The proof readiness is Yellow — partial data exists (Schiphol: 9 of 9 faults detected).

Fix: Pull the Schiphol/Stansted data into the hero callout, matching the water page pattern (£9.8M stat bar).

**Effort:** 30 minutes.

---

## Structural gaps vs. User Journey Map

The User Journey Map defines specific page destinations for each persona and buying motion. Current gap analysis:

### Pages that exist and work well
- ✅ `/technology/esa/` — ESA explainer
- ✅ `/technology/esa-vs-vibration/` — Complementary positioning (excellent "AND not OR")
- ✅ `/technology/how-it-works/` — 5-step pipeline
- ✅ `/platform/sam4/` — Platform detail with managed service emphasis
- ✅ `/platform/security/` — Functions as Trust & Security Centre
- ✅ `/platform/how-it-installs/` — Practical, time-specific (<30 min)
- ✅ `/platform/integrations/` — CMMS integration detail
- ✅ `/resources/roi-calculator/` — Interactive ROI tool
- ✅ `/contact/` — Intent-based routing (5 paths)
- ✅ `/contact/asset-audit/` — SAM4-X entry point
- ✅ `/about/` — ABB partnership, enterprise credibility
- ✅ `/partners/abb/` — Dedicated ABB page
- ✅ All 6 industry pages with market-specific messaging

### Pages that are missing or weak

| GTM requirement | Current state | Gap |
|-----------------|--------------|-----|
| **Champion Enablement Kit** (gated download) | Does not exist | Critical — "highest content priority" per User Journey Map |
| **Engineering Proof Pack** (detection matrix + diagnostic examples) | Does not exist as downloadable bundle | High — Technical Validators need this |
| **Business Case Toolkit** (ROI template + exec summary) | Does not exist | High — Champions need this for CFO conversations |
| **Executive Proof Pack** | Does not exist | Medium — Enterprise buyers need fleet-scale evidence |
| **Security Proof Pack** (beyond public Trust Centre) | Does not exist | Medium — detailed pack for IT/OT review |
| **ISO 55000 alignment brief** | Does not exist | Medium — Corporate Reliability persona has no content |
| **Deployment playbook** (public version) | Partially covered by how-it-installs | Medium — needs expansion |
| **After-alert playbook** | Does not exist | Medium — Practitioners need this |
| **1-page install sheet** (printable) | Does not exist as standalone PDF | Medium |
| **Engineering FAQ** | Does not exist as standalone page | Medium — VFD limitations, accuracy, data requirements |
| **/customers/** page | Link exists in footer but page doesn't exist | Low — could redirect to /proof/ |

### Content the GTM docs say we should NOT have

| Red-readiness verticals | Current state | GTM guidance |
|------------------------|---------------|-------------|
| Oil & Gas | Full industry page exists | "Do not lead O&G campaigns until flagship proof exists" |
| Chemicals | Full industry page exists | "Do not lead campaigns until proof exists" |
| Metals & Mining | Full industry page exists | "Do not lead campaigns until proof exists" |

These pages exist and are well-written with honest proof framing ("early deployments", transparent about metrics). The GTM docs say Red verticals should get "a placeholder page, not a campaign." Current pages are somewhere in between — they're honest about proof status but fully built out. This is a judgment call. The content is honest enough to keep, but paid campaigns should not point to Red verticals.

---

## Brand voice compliance detail

### Banned terms — none found ✅

Searched all 191 pages for: revolutionary, game-changing, best-in-class, world-leading, seamless, cutting-edge, next-generation, delve, navigate, landscape, harness, embark, journey, digital transformation, smart water, comprehensive solution, deploy anywhere.

Zero matches. Excellent discipline.

### Narrative arc — strong ✅

Homepage follows the full 7-step arc: blind spot → risk → why traditional fails → ESA → detection → outcome → fleet.

Industry pages follow the GTM voice mapping accurately:
- Water leads with pollution prevention + operational confidence ✅
- Chemicals leads with reach + safety ✅
- Metals leads with downtime economics ✅
- O&G leads with ATEX/safe-zone installation ✅

### "System + expert colleague" positioning — strong ✅

Multiple pages signal the managed service model:
- "Fully managed. Not self-serve."
- "Every AI-flagged anomaly is reviewed by a Samotics reliability engineer"
- "Dedicated diagnostics team. Named customer success manager."
- "Only validated findings are delivered."

### ESA vs vibration — correctly positioned as AND not OR ✅

The ESA-vs-vibration page is exceptional: "ESA & Vibration Monitoring: Not a replacement. An extension." It includes "Vibration's strengths: We're not going to pretend otherwise." And transparently reports: "58 out of 1,135 confirmed fault events did not have a prior SAM4 alert."

### Honest boundaries — strong ✅

ESA page explicitly states what ESA doesn't do well:
- VFD limitations
- Load-dependent detection
- MCC access requirement
- New asset types need learning time

This matches the brand voice non-negotiable: "state limitations."

### Proof hierarchy — correctly applied ✅

Best proof leads: Southern Water (£748k, named), Yorkshire Water (£390k, named), ArcelorMittal (27 failures, named), Nyrstar (800% ROI, named). Unnamed outcomes used as secondary. Technical capability never leads without a number.

---

## Recommended action priority

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Fix utility page titles + meta | SEO | 15 min |
| 2 | Differentiate duplicate page titles | SEO | 20 min |
| 3 | Replace "Request a Demo" header CTA with "Talk to an engineer" | Brand voice | 30 min |
| 4 | Add persona-aligned CTAs to key landing pages | Conversion | 2-3 hrs |
| 5 | Batch-shorten page titles to <55 chars | SEO | 2 hrs |
| 6 | Rewrite platform overview hero to outcome-first | Brand voice | 30 min |
| 7 | Add quantified proof to airports page | Credibility | 30 min |
| 8 | Build Champion Enablement Kit page/download | GTM critical | 4-6 hrs |
| 9 | Build Engineering Proof Pack download | GTM high | 3-4 hrs |
| 10 | Build Business Case Toolkit download | GTM high | 3-4 hrs |
| 11 | Create Engineering FAQ page | Technical trust | 2-3 hrs |
| 12 | Resolve proof/case-studies duplication (17 detection stories exist in both /proof/ and /resources/) | Site hygiene | 1-2 hrs |

---

*Generated by automated crawl + manual review. 191 pages audited.*
