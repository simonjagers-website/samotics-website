# Site Architecture

Full page hierarchy, linking logic, and URL structure for samotics.com

**Document:** Site Architecture — Base
**Layer:** Architecture
**Owner:** Marketing
**Status:** Draft
**Date:** February 2026
**Dependencies:** #3 Buying Scenario Framework, #12 User Journey Map, #11 Sitemap
**Feeds Into:** #15 Page Brief Template, Navigation Spec, CMS Build

---

## How to Use This Document

This document defines every page on samotics.com, organised by hierarchy. For each page it specifies the URL, parent–child relationships, what pages link to it (inbound), and what pages it links to (outbound). Use it to validate CMS structure, internal linking strategy, and URL conventions before build starts.

---

## URL Conventions

All URLs follow these rules:

| Rule | Convention | Example |
|------|-----------|---------|
| **Format** | Lowercase, hyphenated, no trailing slash | `/technology/how-it-works` |
| **Depth** | Maximum 3 levels deep | `/industries/water/yorkshire-water` |
| **Slugs** | Descriptive, keyword-relevant, no abbreviations | `/platform/security` not `/platform/sec` |
| **Parameters** | No query strings in navigation; reserved for UTM tracking | `?utm_source=linkedin` |
| **Canonicals** | Every page has a self-referencing canonical tag | `<link rel="canonical" href="https://samotics.com/technology/esa/">` |
| **Trailing slashes** | Consistent — pick one convention and enforce via redirect | Recommend: no trailing slash |
| **Phases** | Phase 2/3 pages noted but not built in v1; URLs reserved | `/partners/` reserved for Phase 2 |

---

## Complete Page Hierarchy

### Level 0: Root

| Page | URL | Purpose | Phase |
|------|-----|---------|-------|
| **Homepage** | `/` | Primary entry point. Routes visitors by problem, persona, or scenario. Serves S1 and S2 as highest-traffic scenarios. | v1 |

---

### Level 1: Primary Sections

These are the top-level sections accessible from the main navigation.

| Page | URL | Purpose | Phase |
|------|-----|---------|-------|
| **Problem** | `/problem` | Names the monitoring blind spot. Entry for S1 (Critical Failure) and S2 (Coverage Gap). | v1 |
| **Technology** | `/technology` | Section landing — routes to ESA, How It Works, ESA vs Vibration | v1 |
| **Platform** | `/platform` | Section landing — routes to SAM4, How It Installs, Security, Integrations | v1 |
| **Industries** | `/industries` | Section landing — routes to vertical pages | v1 |
| **Proof** | `/proof` | Proof hub — filterable grid of case studies, customer results, detection stories | v1 |
| **About** | `/about` | Company credibility: funding, team, ABB partnership, scale. Trust signal for CTO/VP (S3). | v1 |
| **Partners** | `/partners` | Partner programme overview, revenue model, enablement (S5) | Phase 2 |
| **Contact** | `/contact` | Conversion endpoint — intent-based routing (demo, audit, briefing, security docs, partnership) | v1 |
| **Blog / Resources** | `/resources` | Content hub — blog posts, webinars, whitepapers, downloads | v1 |

---

### Level 2: Problem Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **The Proximity Penalty** | `/problem/proximity-penalty` | `/problem` | Why traditional monitoring can't reach 30–40% of critical assets. Structural barriers. | v1 |

**Inbound links to `/problem`:**
- Homepage (hero or problem statement block)
- `/technology/esa` (back-link: "See the problem we solve")
- Industry pages (contextual link from problem framing)
- Google organic (S1, S2 search queries)

**Outbound links from `/problem`:**
- `/technology/esa` (the solution to the problem)
- `/problem/proximity-penalty` (deeper explanation)
- `/proof` (see results)
- `/contact/asset-audit` (CTA: Start Your Asset Audit)

---

### Level 2: Technology Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **ESA Technology** | `/technology/esa` | `/technology` | Core credibility page. ESA explained with physics, not marketing. Fault types, signal path, data quality. | v1 |
| **How It Works** | `/technology/how-it-works` | `/technology` | End-to-end data flow: sensor → MCC → cloud → SAM4 dashboard. Architecture for Digital Lead. | v1 |
| **ESA vs Vibration** | `/technology/esa-vs-vibration` | `/technology` | Honest comparison. ESA complements vibration — doesn't replace it. Key page for Reliability Manager (S1). | v1 |

**Inbound links to `/technology/esa`:**
- Homepage (primary "How it works" pathway)
- `/problem` (solution to the blind spot)
- Industry pages (technology reference)
- `/proof` case studies (back-link to method)
- Partner pages (technology evaluation)

**Outbound links from `/technology/esa`:**
- `/technology/how-it-works` (go deeper)
- `/technology/esa-vs-vibration` (comparison)
- `/platform/sam4` (see the platform)
- `/proof` (see results)
- `/contact` (Request a Demo)

**Inbound links to `/technology/how-it-works`:**
- `/technology/esa` (deeper dive)
- `/platform/sam4` (architecture reference)
- Digital Lead journey (S3, step 3)

**Outbound links from `/technology/how-it-works`:**
- `/platform/sam4` (the platform that delivers it)
- `/platform/security` (security architecture)
- `/platform/integrations` (how it connects)
- `/proof` (validation)

**Inbound links to `/technology/esa-vs-vibration`:**
- `/technology/esa` (comparison link)
- Reliability Manager journey (S1, step 3)
- Google organic (comparison searches)

**Outbound links from `/technology/esa-vs-vibration`:**
- `/proof` (proof that ESA works)
- `/technology/how-it-works` (how ESA works in practice)
- `/contact` (Request a Demo)

---

### Level 2: Platform Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **SAM4 Platform** | `/platform/sam4` | `/platform` | Dashboard, alert logic, diagnostics, service model. Core convergence page — all personas visit. | v1 |
| **What We Monitor** | `/platform/what-we-monitor` | `/platform` | Asset-type qualification page. Shows every equipment category SAM4 monitors, detectable faults per type, capabilities (health, energy, alerts), and fleet experience. Cross-industry. | v1+ |
| **How It Installs** | `/platform/how-it-installs` | `/platform` | <30 min install, non-invasive, cellular connectivity. Removes deployment objection. | v1 |
| **Security & Compliance** | `/platform/security` | `/platform` | SOC 2 Type II, ISO 27001, ISO 9001, NIS2, cellular architecture. Gatekeeper page for Digital Lead (S3). | v1 |
| **Integrations** | `/platform/integrations` | `/platform` | CMMS integration (SAP PM, IBM Maximo), SCADA, API. Digital Lead evaluation (S3). | v1 |

**Inbound links to `/platform/sam4`:**
- Homepage (primary platform pathway)
- `/technology/esa` and `/technology/how-it-works` (method → platform)
- All industry pages (platform reference)
- Partner pages (technology evaluation)
- CTO journey (S3, step 2)

**Outbound links from `/platform/sam4`:**
- `/platform/how-it-installs` (deployment)
- `/platform/security` (compliance)
- `/platform/integrations` (connectivity)
- `/proof` (customer results)
- `/contact` (Request a Demo)

**Inbound links to `/platform/security`:**
- `/platform/sam4` (security details)
- Digital Lead journey (S3, step 4) — critical gatekeeper page
- CTO journey (S3, step 4)

**Outbound links from `/platform/security`:**
- Security docs download (gated form — v1 mitigation for Digital Lead)
- `/platform/integrations` (related technical content)
- `/contact` (Request Security Docs CTA)

**Inbound links to `/platform/how-it-installs`:**
- `/platform/sam4` (deployment details)
- Reliability Manager journey (S1, step 6)
- Operations Director journey (S1/S2, step 4)

**Outbound links from `/platform/how-it-installs`:**
- `/proof` (see deployment results)
- `/contact` (Request a Demo)

**Inbound links to `/platform/integrations`:**
- `/platform/sam4` (integration details)
- `/platform/security` (related technical)
- Digital Lead journey (S3, step 2)

**Outbound links from `/platform/integrations`:**
- `/platform/security` (security review)
- `/proof` (integration case studies)
- `/contact` (Talk to Us)

---

### Level 2: Industries Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **Water & Wastewater** | `/industries/water` | `/industries` | Strongest proof industry. Dual framing: reactive (failure) + proactive (coverage). | v1 |
| **Oil & Gas** | `/industries/oil-gas` | `/industries` | ATEX/hazardous zone focus. Safe-zone monitoring from MCC. | v1 |
| **Metals & Mining** | `/industries/metals-mining` | `/industries` | Extreme environment assets. Bearing faults, crusher monitoring. | v1 |
| **Chemicals** | `/industries/chemicals` | `/industries` | ATEX compliance, process-critical pumps and compressors. | v1 |
| **Pulp & Paper** | `/industries/pulp-paper` | `/industries` | Energy efficiency + reliability dual value. Growing S4 scenario. | v1 |
| **Energy Efficiency** | `/industries/energy-efficiency` | `/industries` | Dedicated energy/ESG entry point. BEP deviation, oversized motors. | Phase 3 |

**Inbound links to industry pages (general pattern):**
- Homepage (industry routing block)
- `/industries` section landing (grid/list)
- Google organic (industry + problem searches)
- `/proof` case studies (back-link to industry context)

**Outbound links from industry pages (general pattern):**
- `/proof/[industry-case-study]` (matching proof)
- `/technology/esa` (how it works for this industry)
- `/platform/sam4` (the platform)
- `/contact` (scenario-appropriate CTA)

---

### Level 2: Proof Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **Yorkshire Water** | `/proof/yorkshire-water` | `/proof` | Fleet-scale case study. £9.8M benefits, 1,300 assets, 70K inspections eliminated. | v1 |
| **Southern Water** | `/proof/southern-water` | `/proof` | 63 failures caught, £748K annual savings. | v1 |
| **Schiphol** | `/proof/schiphol` | `/proof` | 9/9 faults detected (100% detection rate). | v1 |
| **thyssenkrupp** | `/proof/thyssenkrupp` | `/proof` | Bearing fault in extreme environment. | v1 |
| **Nyrstar** | `/proof/nyrstar` | `/proof` | 800% ROI in 11 months. | v1 |
| **Vitens** | `/proof/vitens` | `/proof` | 7.1% energy efficiency improvement. Energy scenario proof. | v1 |
| *Additional case studies* | `/proof/[client-slug]` | `/proof` | Pattern for future case studies (BASF, etc.) | Ongoing |

#### Detection Stories (Level 2 under Proof)

Individual fault detection pages — lighter than full case studies, documenting specific SAM4 detections with situation/detection/outcome narrative. All use `detection-story.css` and `detection-story.js`.

| Page | URL | Parent | Industry | Fault Type | Phase |
|------|-----|--------|----------|-----------|-------|
| **Inlet screw monitoring** | `/proof/inlet-screw-monitoring` | `/proof` | Water | Belt, gearbox, bearing | v1+ |
| **Belt degradation — circulation pump** | `/proof/belt-degradation-circulation-pump` | `/proof` | Chemicals | Belt degradation | v1+ |
| **Cavitation — anolyte pump** | `/proof/cavitation-anolyte-pump` | `/proof` | Chemicals | Cavitation, seal damage | v1+ |
| **Clogging — wastewater pump** | `/proof/clogging-wastewater-pump` | `/proof` | Water | Clogging | v1+ |
| **Missing bolt — cooling pump** | `/proof/missing-bolt-cooling-pump` | `/proof` | Manufacturing | Missing coupling bolt | v1+ |
| **Cardan shaft coupling — roller** | `/proof/cardan-shaft-coupling-roller` | `/proof` | Steel | Failing cardan coupling | v1+ |
| **Synthetic fibre production** | `/proof/synthetic-fiber-production` | `/proof` | Manufacturing | Motor overloading | v1+ |
| **Loose cardan joint — roll** | `/proof/loose-cardan-joint-roll` | `/proof` | Steel | Loose coupling | v1+ |
| **Three faults — oil transfer pump** | `/proof/three-faults-oil-transfer-pump` | `/proof` | Manufacturing | Multiple mechanical | v1+ |
| **Clogging — borehole pump** | `/proof/clogging-borehole-pump` | `/proof` | Water | Iron buildup clogging | v1+ |
| **Gearbox misalignment — circulator pump** | `/proof/gearbox-misalignment-circulator-pump` | `/proof` | Manufacturing | Misalignment | v1+ |
| **Borehole pump detections** | `/proof/borehole-pump-detections` | `/proof` | Water | Clogging, VFD, mechanical | v1+ |
| **Loose belt guard — shot blasting** | `/proof/loose-belt-guard-shot-blasting` | `/proof` | Manufacturing | Loose belt guard | v1+ |
| **Bearing failure — motor roll** | `/proof/bearing-failure-motor-roll` | `/proof` | Steel | Bearing degradation | v1+ |
| **Clogging — Yorkshire Water sewage** | `/proof/clogging-yorkshire-water-sewage` | `/proof` | Water | Complete blockage | v1+ |
| **Belt-driven assets detection** | `/proof/belt-driven-assets-detection` | `/proof` | Chemicals | Belt, bearing, pulley | v1+ |
| **Cavitation — centrifugal pump** | `/proof/cavitation-centrifugal-pump` | `/proof` | Chemicals | Cavitation | v1+ |

**Inbound links to `/proof` (hub):**
- Homepage (social proof block)
- Every technology page (validation)
- Every industry page (matching proof)
- Every platform page (results)
- Operations Director journey (S1/S2, step 2)

**Outbound links from `/proof` (hub):**
- Individual case studies (filterable by industry, asset type, outcome)
- `/contact` (CTA contextual to case study)
- PDF download per case study (critical for Operations Director — v1 priority)

**Outbound links from individual case studies:**
- `/technology/esa` (back to method)
- `/industries/[x]` (back to industry context)
- `/platform/sam4` (platform that delivered results)
- `/contact` (CTA)
- PDF download (shareable proof asset)

---

### Level 2: About Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **ABB Partnership** | `/about/abb` or `/partners/abb` | `/about` (v1) / `/partners` (Phase 2) | ABB equity partnership, ACS880 integration, co-sell model. Critical for S3 and S5. | v1 |

**Inbound links to `/about`:**
- Homepage (company credibility link)
- CTO journey (S3, step 1)
- Operations Director journey (step 3 — 30-second credibility check)
- Footer (persistent)

**Outbound links from `/about`:**
- `/partners/abb` (ABB partnership detail)
- `/proof` (customer scale)
- `/contact` (Talk to Us)

---

### Level 2: Contact Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **Asset Audit** | `/contact/asset-audit` | `/contact` | Low-commitment first step for Operations Director (S2). Outputs a gap report. | v1 |
| **Partner Inquiry** | `/contact/partner-inquiry` | `/contact` | Partnership conversation — distinct from product demo. | Phase 2 |

**Inbound links to `/contact` (all paths converge here):**
- Every page on the site (via nav CTA or in-page CTA)
- Persona-specific: Reliability Manager → Request a Demo; Ops Director → Asset Audit; CTO → Talk to Us; Digital Lead → Request Security Docs; Partner → Discuss Partnership

**v1 Contact routing:** Intent selector on the main contact form: "I want a demo / audit / executive briefing / security docs / partnership discussion." Phase 2 breaks these into separate landing pages.

---

### Level 2: Resources Section

| Page | URL | Parent | Purpose | Phase |
|------|-----|--------|---------|-------|
| **Blog** | `/resources/blog` | `/resources` | Thought leadership, detection stories, industry insights | v1 |
| **Webinars** | `/resources/webinars` | `/resources` | On-demand and upcoming webinars | v1 |
| **Downloads** | `/resources/downloads` | `/resources` | Whitepapers, one-pagers, technical briefs | v1 |

---

### Utility Pages

| Page | URL | Purpose | Phase |
|------|-----|---------|-------|
| **Privacy Policy** | `/privacy` | GDPR compliance | v1 |
| **Terms of Use** | `/terms` | Legal | v1 |
| **Cookie Policy** | `/cookies` | Cookie consent reference | v1 |
| **404 Page** | `/404` | Custom error page with navigation back to key sections | v1 |
| **Sitemap (XML)** | `/sitemap.xml` | SEO crawl directive | v1 |

---

## Cross-Page Linking Map

This table summarises the highest-priority internal links. Every link exists because a persona journey or buying scenario requires it.

| From | To | Reason |
|------|----|--------|
| Homepage | `/problem` | S1/S2 visitors need problem validation immediately |
| Homepage | `/technology/esa` | Reliability Manager pathway — one click to technology |
| Homepage | `/industries/[x]` | Industry routing for organic search visitors |
| Homepage | `/proof` | Social proof block — headline numbers |
| `/problem` | `/technology/esa` | Problem → solution flow |
| `/problem` | `/proof` | Problem → proof flow |
| `/technology/esa` | `/technology/esa-vs-vibration` | Reliability Manager comparison need |
| `/technology/esa` | `/platform/sam4` | Method → platform flow |
| `/platform/sam4` | `/platform/security` | CTO/Digital Lead security check |
| `/platform/sam4` | `/platform/how-it-installs` | Deployment practicality |
| `/platform/security` | Security docs download | Digital Lead gated download (v1 gap mitigation) |
| `/industries/[x]` | `/proof/[matching-case]` | Industry → proof link (critical: S1 stalls without it) |
| `/proof/[case]` | PDF download | Operations Director needs shareable assets |
| `/about` | `/partners/abb` | CTO journey — ABB validation |
| Every page | `/contact` | Via nav CTA and in-page contextual CTAs |

---

## Convergence Points

Pages that serve multiple personas and scenarios simultaneously. These require careful design to serve all audiences without diluting any single message.

| Page | Personas Served | Scenarios | Design Pattern |
|------|----------------|-----------|----------------|
| `/proof` | All 6 personas | S1–S5 | Filterable grid: industry, asset type, outcome type (ROI, detection, energy) |
| `/platform/sam4` | Reliability, Ops, CTO, Digital, Partner | S1–S5 | Progressive disclosure: overview → expand for technical detail |
| `/about` | CTO, Ops Director | S3 | Stats-first layout: numbers (funding, assets, customers) before narrative |
| `/contact` | All personas | S1–S5 | Intent-based routing: demo / audit / briefing / security docs / partnership |
| `/technology/esa` | Reliability, Ops, Partner | S1, S2, S5 | Layered content: headline → explainer → deep dive with jump links |
| `/industries/water` | Reliability, Ops | S1, S2, S4 | Dual framing: reactive (failure) + proactive (coverage) |

---

## Phase Roadmap

| Phase | Pages Added | URL Reserved |
|-------|------------|--------------|
| **v1** | All Level 0–2 pages except where noted. 25–30 pages total. | — |
| **Phase 2** | `/partners`, `/contact/partner-inquiry`, energy case studies, additional industry case studies (BASF, chemicals) | `/partners`, `/partners/programme`, `/contact/partner-inquiry` |
| **Phase 3** | `/industries/energy-efficiency`, ESG content, coverage calculator tool | `/industries/energy-efficiency`, `/tools/coverage-calculator` |

---

## Technical Notes

- **CMS:** URL slugs must match this spec exactly. No auto-generated slugs.
- **Redirects:** If any URL changes post-launch, implement 301 redirects. No 302s.
- **Canonical tags:** Every page self-canonicalises. No duplicate content across industry/proof pages.
- **Indexing:** All v1 pages indexed. Phase 2/3 placeholder pages should not exist in CMS until content is ready (no thin pages).
- **Schema markup:** Case study pages should use `Article` or `CaseStudy` structured data. Product pages should use `Product` or `SoftwareApplication`.
