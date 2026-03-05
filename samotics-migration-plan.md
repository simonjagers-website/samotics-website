# Samotics Website Migration Plan

**samotics.com → samoticstestpage.com**

---

## Current State Summary

**samotics.com (Elementor):** 46 published pages, 132 published posts (across 8 categories), 54 FAQs, 7 products, 6 testimonials, 4 use cases, 47 Elementor templates.

**samoticstestpage.com (Bricks):** ~30 active pages with Bricks content, 0 posts, 0 custom post types. Many pages are in `__trashed` parent slugs (industries, technology, proof, resources) — likely restructured at some point.

---

## 1. What Content to Transfer

### 1A. Pages — Direct Equivalents (already have shells on testpage)

These samotics.com pages map to existing samoticstestpage.com pages. Content needs to be adapted from Elementor to Bricks format, but the page structure exists.

| samotics.com | samoticstestpage.com | Status |
|---|---|---|
| Homepage | / | Has Bricks content |
| About | /about/ | Has Bricks content |
| Contact | /contact/ | Has Bricks content |
| Partners | /partners/ | Has Bricks content |
| ABB Partnership | /about/abb/ | Has Bricks content |
| Privacy & Cookie Policy | /privacy-policy/ + /cookie-policy/ | Empty — needs legal text |
| Terms of Usage | /terms-of-use/ | Empty — needs legal text |
| Product Overview → Platform | /platform/ | Empty parent page |
| SAM4 | /platform/sam4/ | Has Bricks content |
| Pricing | — | **No equivalent on testpage. Decision needed.** |

### 1B. Pages — New on testpage (no samotics.com equivalent)

These pages exist only on testpage and are net-new content for the redesign:

| Page | Status |
|---|---|
| /problem/ (The Problem) | Has Bricks content |
| /proximity-penalty/ | Has Bricks content |
| /platform/how-it-installs/ | Has Bricks content |
| /platform/security/ | Has Bricks content |
| /platform/integrations/ | Has Bricks content |
| /platform/what-we-monitor/ | Has Bricks content |
| /contact/asset-audit/ | Has Bricks content |
| /contact/partner-inquiry/ | Has Bricks content |
| /tools/coverage-calculator/ | Has Bricks content |
| /resources/esg-reporting/ | Has Bricks content |
| /industries/energy-efficiency/ | Has Bricks content |

### 1C. Content to Port — High Priority

These are published samotics.com pages with unique, valuable content that should move to testpage:

**Industry Pages (10 published)**
Currently on samotics.com at `/industries/*`. The testpage has 6 trashed industry pages with Bricks content. The samotics.com set is larger:

| samotics.com Industry | testpage equivalent | Action |
|---|---|---|
| Water (clean-water) | /industries__trashed/water/ (has Bricks) | Restore, merge content |
| Wastewater | /industries__trashed/water/ (combined) | Merge into Water page |
| Oil & Gas | /industries__trashed/oil-gas/ (has Bricks) | Restore, update content |
| Chemicals | /industries__trashed/chemicals/ (has Bricks) | Restore, update content |
| Mining | /industries__trashed/metals-mining/ (has Bricks) | Restore, update content |
| Steel | /industries__trashed/metals-mining/ (combined) | Merge into Metals & Mining |
| Pulp & Paper | /industries__trashed/pulp-paper/ (has Bricks) | Restore, update content |
| Cement | — | Merge into relevant industry or skip |
| Airports | — | New page or skip |
| Wind Energy | — | New page or skip |

**Recommendation:** Restore the 6 trashed industry pages. Merge Water + Wastewater into one. Merge Steel + Mining into Metals & Mining. Decide whether Cement, Airports, and Wind Energy warrant standalone pages or become subsections.

**Case Studies (28 published)**
This is the single largest content category. Every case study is a published post under `/case-studies/*`. No case study infrastructure exists on testpage. This is a high-priority gap — case studies are core proof content.

Key case studies by industry:
- **Water:** Yorkshire Water (multiple), Southern Water, Vitens, wastewater pumps, booster pump energy, inlet station energy, aeration blowers, borehole pumps, blockage detection, oxidation ditch, Sabesp
- **Steel:** ArcelorMittal, thyssenkrupp, hot strip mill rollers, runout table (multiple), shot blasting
- **Chemicals/Manufacturing:** anolyte pump, circulator pump, cooling pump, heated godet roll, exhaust fans, oil transfer pump, Nyrstar
- **Airports:** Schiphol, London Stansted
- **Belt-driven:** belt-driven equipment

**Blog Posts (33 published)**
Long-form SEO and thought-leadership content at `/blog/*`. Ranges from 3,500 to 30,000 chars. Topics include condition monitoring guides, predictive maintenance, pump failure, CSO series (3 parts), CBM implementation series (4 parts), smart sewers series (2 parts).

**Knowledge Base Articles (11 published)**
Technical and educational content at `/kb/*`. Includes ESA explainer (31K chars), condition monitoring comparison (25K chars), pump fault detection, pump curve explainer, and several water-industry-focused pieces.

**News Articles (27 published)**
Company announcements at `/news/*`. Partnership announcements (ABB, Siemens, Schneider, Eviden, Seed Group), customer wins (Yorkshire Water, Thames Water, Anglian Water, South East Water, United Utilities, Northern Ireland Water, Southern Water, London Stansted, thyssenkrupp), funding/awards, product launches.

**Webinars (7 published)**
At `/webinars/*`. Mostly short registration/replay pages. Some multilingual (Spanish, Italian, Portuguese).

**Events (5 published)**
At `/events/*`. Recent/upcoming events (World Water-Tech 2026, Maintec 2026, Utility Week Live 2026, Global Water Summit 2026, SPE Europe).

**Success Stories (1 published)**
Yorkshire Water success story — the only published one.

**Use Cases (4 published)**
Custom post type: high-performance fibers, zinc production, auxiliary motors, canned motor pumps.

**Use Case Pages (3 published)**
Full pages at `/use-cases/*`: prevent pollution, reduce energy waste, stop unplanned downtime. These are large (100K-135K chars each in Elementor).

**Product Feature Pages (6 published)**
Custom post type at `/product/*`: pump blockage detection, predictive alerts, asset reliability service, asset map, Archimedes screw pump failure detection, reactor coolant pump monitoring.

**Other Pages**
- SAM4 Health, SAM4 Energy — product sub-pages
- Drive-integrated condition monitoring — ABB integration page
- AMP8 — UK water regulatory page (211K chars — very large)
- Sewage pump blockage detection — feature deep-dive (154K chars)
- Demo/Tour pages — lead gen
- Landing pages (5) — paid media destinations

### 1D. Content to Skip

- **Draft posts** (30) — incomplete, don't migrate
- **Elementor templates** (47) — Elementor-specific, replaced by Bricks templates
- **Elementor fonts** — already have Aeonik set up in Bricks
- **JetEngine/JetSmartFilters** — Elementor ecosystem plugins, won't work in Bricks
- **mt_pp (team members)** — 27 entries, likely handled differently on testpage
- **FAQ items** (54) — these are individual FAQ posts for the FAQ listing. Migrate the content, but the post type structure will change
- **Testimonials** (6 published) — structured data, migrate content but restructure
- **Landing pages** (5) — These are paid ad destinations. Port only if paid campaigns will redirect to testpage
- **Old/duplicate homepages** (drafts) — skip
- **Internal tools** (messaging house, benefits canvas, four levels canvas) — internal, skip

---

## 2. Sitemap Changes

### Current samoticstestpage.com Structure
```
/                              ← Homepage
/problem/                      ← The Problem
/proximity-penalty/            ← The Proximity Penalty
/technology/                   ← Parent (empty)
  /technology/esa/             ← (trashed)
  /technology/how-it-works/    ← (trashed)
  /technology/esa-vs-vibration/ ← (trashed)
/platform/                     ← Parent (empty)
  /platform/sam4/
  /platform/how-it-installs/
  /platform/security/
  /platform/integrations/
  /platform/what-we-monitor/
/industries/                   ← Parent (empty)
  /industries/energy-efficiency/
  /industries/water/           ← (trashed)
  /industries/oil-gas/         ← (trashed)
  /industries/metals-mining/   ← (trashed)
  /industries/chemicals/       ← (trashed)
  /industries/pulp-paper/      ← (trashed)
/proof/                        ← Proof hub
  /proof/yorkshire-water/      ← (trashed, + case study variant)
  /proof/southern-water/       ← (trashed)
  /proof/schiphol/             ← (trashed)
  /proof/thyssenkrupp/         ← (trashed)
  /proof/nyrstar/              ← (trashed)
  /proof/vitens/               ← (trashed)
/resources/                    ← Parent (empty)
  /resources/esg-reporting/
  /resources/blog/             ← (trashed)
  /resources/webinars/         ← (trashed)
  /resources/downloads/        ← (trashed)
/about/
  /about/abb/
/contact/
  /contact/asset-audit/
  /contact/partner-inquiry/
/partners/
/tools/
  /tools/coverage-calculator/
/privacy-policy/
/terms-of-use/
/cookie-policy/
```

### Recommended Sitemap for Launch
```
/                                  ← Homepage
/problem/                          ← The Problem
/proximity-penalty/                ← The Proximity Penalty (or move under /problem/)

/technology/                       ← Restore as parent page
  /technology/esa/                 ← Untrash
  /technology/how-it-works/        ← Untrash
  /technology/esa-vs-vibration/    ← Untrash

/platform/                         ← Add content to parent page
  /platform/sam4/
  /platform/how-it-installs/
  /platform/security/
  /platform/integrations/
  /platform/what-we-monitor/
    /platform/what-we-monitor/pumps/          ← NEW (from our templates)
    /platform/what-we-monitor/compressors/    ← NEW
    /platform/what-we-monitor/fans-blowers/   ← NEW
    /platform/what-we-monitor/conveyors/      ← NEW
    /platform/what-we-monitor/crushers-mills/ ← NEW
    /platform/what-we-monitor/agitators-mixers/ ← NEW
    /platform/what-we-monitor/esps/           ← NEW

/industries/                       ← Add content to parent page
  /industries/water/               ← Untrash, populate from samotics.com
  /industries/oil-gas/             ← Untrash, populate
  /industries/metals-mining/       ← Untrash, populate
  /industries/chemicals/           ← Untrash, populate
  /industries/pulp-paper/          ← Untrash, populate
  /industries/energy-efficiency/

/proof/                            ← Proof hub (case studies, success stories)
  /proof/yorkshire-water/          ← Untrash
  /proof/southern-water/           ← Untrash
  /proof/schiphol/                 ← Untrash
  /proof/thyssenkrupp/             ← Untrash
  /proof/nyrstar/                  ← Untrash
  /proof/vitens/                   ← Untrash
  /proof/arcelormittal/            ← NEW
  /proof/stansted/                 ← NEW

/resources/                        ← Resources hub page
  /resources/blog/                 ← Untrash (archive page)
  /resources/webinars/             ← Untrash
  /resources/downloads/            ← Untrash
  /resources/esg-reporting/
  /resources/case-studies/         ← NEW (or keep under /proof/)

/about/
  /about/abb/
/contact/
  /contact/asset-audit/
  /contact/partner-inquiry/
/partners/
/tools/
  /tools/coverage-calculator/
/news/                             ← NEW (post archive)
/events/                           ← NEW (or under /resources/)
/demo/                             ← NEW (lead gen)
/privacy-policy/
/terms-of-use/
/cookie-policy/
```

### Key Sitemap Decisions Needed

1. **Case studies:** Live under `/proof/*` (current testpage pattern) or `/case-studies/*` (current samotics.com pattern)?
2. **Blog posts:** Stay at `/resources/blog/*` or move to `/blog/*` for SEO continuity?
3. **News vs Blog:** Keep separate (as on samotics.com) or merge into one content hub?
4. **Trashed technology pages:** Restore or permanently remove? They have Bricks content.
5. **AMP8 page:** Port to testpage? It's a very large, specific regulatory page.
6. **Pricing page:** Include on new site?
7. **Demo/Tour pages:** Which lead-gen pattern to use?
8. **Use case pages (/use-cases/):** Port the 3 large use case pages or restructure into the new site?

---

## 3. New Templates Needed

### 3A. Post Type Templates (Bricks)

Currently testpage has **zero post types** beyond pages. You need Bricks templates for:

1. **Blog Post Template** — Single post layout for `/resources/blog/*` (33 posts to migrate)
2. **Blog Archive Template** — Filterable grid for the blog listing page
3. **Case Study Template** — Single post layout for case studies (28 posts). Should include: headline, KPI summary, customer/industry tags, body content, CTA
4. **Case Study Archive Template** — Filterable grid with industry/application filters
5. **News Post Template** — Single post layout for news articles (27 posts)
6. **News Archive Template** — Chronological listing
7. **Webinar Post Template** — Registration/replay page (7 posts)
8. **Event Post Template** — Event detail with date, location, CTA (5 posts)
9. **FAQ Template** — Either a single FAQ page with accordion sections, or individual FAQ posts with a listing template (54 items)

### 3B. Page Templates (Bricks Code Elements)

We've already built templates for:
- Homepage
- What We Monitor (hub)
- Asset-specific pages (7 pages built)

Still needed:
10. **Industry Page Template** — For the 5-6 industry vertical pages. Sections: hero, key stats, typical assets monitored, relevant case studies, relevant FAQs, CTA
11. **Proof/Customer Story Page Template** — For the ~8 customer story pages under /proof/. Sections: hero, customer overview, challenge, solution, results with KPIs, quote, CTA
12. **Resource Hub Template** — For /resources/ parent page. Grid of content types (blog, webinars, downloads, case studies)

### 3C. Global Templates

13. **404 Page** — samotics.com has one; testpage needs one
14. **Search Results Template** — If site search is planned

---

## 4. How to Move Content Effectively

### Step 1: Fix the URL Structure (1 day)

In WordPress admin on samoticstestpage.com:
- Untrash the 6 industry pages, 6+ proof pages, 3 technology pages, and 3 resource pages
- Fix their parent slugs so URLs resolve correctly (remove `__trashed` suffixes)
- Set `/platform/` and `/technology/` parent pages to have proper landing content (even if minimal)
- Register the required custom post types: `case-study`, `event` (or use categories on regular posts)

### Step 2: Create Post Templates in Bricks (2-3 days)

Build the 9 post-type templates listed in Section 3A using Bricks' template system. Each needs:
- A single-post template (the layout for individual posts)
- An archive template (the listing page)
- Proper category/taxonomy registration

### Step 3: Bulk Import Posts via WordPress Importer (1 day)

Use WordPress' built-in WXR importer or WP All Import:
1. Filter the samotics.com XML export to extract only the post categories you want (case studies, blog, news, webinars, events)
2. Import into testpage
3. Reassign authors if needed
4. The Elementor content won't render, but the post body text/HTML will be there as raw content
5. For each post, strip Elementor shortcodes and keep the raw text + images

**Alternative for cleaner migration:** Write a script that extracts plain text + images from each post in the XML, then creates new posts on testpage via WP REST API or direct import.

### Step 4: Migrate Page Content Manually (3-5 days)

For the ~15 pages that need content ported from samotics.com:
- Open the samotics.com page and the testpage equivalent side by side
- Copy text content, update to match the new Bricks template structure
- Re-upload images to testpage media library
- Industry pages, proof pages, and product pages are the priority

### Step 5: Populate Empty Pages (2-3 days)

Fill in the pages that currently have no content (see Section 5 below).

### Step 6: Set Up Redirects (1 day)

Create a redirect map from old samotics.com URLs to new testpage URLs. Critical for SEO. Use a plugin like Redirection or handle at the server level.

### Step 7: QA Pass (2-3 days)

- Check every page renders correctly
- Verify all internal links work
- Test responsive layouts
- Check meta titles/descriptions
- Validate forms work
- Test navigation (header/footer links)

---

## 5. Empty Pages on samoticstestpage.com That Need Content

### Pages With No Bricks Content At All

| Page | What It Needs |
|---|---|
| /technology/ | Parent landing page — overview of ESA technology, links to sub-pages |
| /platform/ | Parent landing page — overview of SAM4 platform, links to sub-pages |
| /industries/ | Parent landing page — industry grid, links to sub-pages |
| /resources/ | Resource hub — grid linking to blog, webinars, downloads, case studies |
| /privacy-policy/ | Legal text (copy from samotics.com) |
| /terms-of-use/ | Legal text (copy from samotics.com) |
| /cookie-policy/ | Legal text (copy from samotics.com) |
| /tools/ | Parent landing page for tools (or redirect to /tools/coverage-calculator/) |

### Pages With Bricks Content But Likely Needing Real Copy

| Page | Status |
|---|---|
| /proof/ | Has Bricks layout — check if customer stories are populated or placeholder |
| /about/ | Has Bricks layout — check if team, mission, and history text is final |
| /contact/ | Has Bricks layout — check if form is functional |
| /partners/ | Has Bricks layout — check if partner list is current |

### Trashed Pages That Need Restoration + Content

| Page | Source Content |
|---|---|
| /industries/water/ | samotics.com /industries/clean-water + /industries/wastewater (85K + 151K chars) |
| /industries/oil-gas/ | samotics.com /industries/oil-gas (24K chars) |
| /industries/metals-mining/ | samotics.com /industries/mining + /industries/steel (46K + 93K chars) |
| /industries/chemicals/ | samotics.com /industries/chemicals (69K chars) |
| /industries/pulp-paper/ | samotics.com /industries/pulp-paper (20K chars) |
| /proof/yorkshire-water/ | samotics.com case studies + success story |
| /proof/southern-water/ | samotics.com case study (4.6K chars) |
| /proof/schiphol/ | samotics.com case study (3.9K chars) |
| /proof/thyssenkrupp/ | samotics.com case study (4.5K chars) + news |
| /proof/nyrstar/ | samotics.com case study (2.8K chars) |
| /proof/vitens/ | samotics.com case study (14.8K chars) |
| /technology/esa/ | samotics.com KB article on ESA (31K chars) |
| /technology/how-it-works/ | samotics.com product overview content |
| /technology/esa-vs-vibration/ | samotics.com KB condition monitoring comparison (25K chars) |
| /resources/blog/ | Archive page — needs blog posts imported first |
| /resources/webinars/ | Archive page — needs webinar posts imported first |
| /resources/downloads/ | Archive page — needs downloadable assets |

---

## Priority Order for Launch

**Phase 1 — Structure & Templates (Week 1)**
1. Fix URL structure (untrash pages, set parents)
2. Build post-type templates (blog, case study, news)
3. Register custom post types/taxonomies

**Phase 2 — Content Migration (Week 2-3)**
4. Import blog posts (33 articles)
5. Import case studies (28 articles)
6. Import news articles (27 articles)
7. Port industry page content (5-6 pages)
8. Port proof/customer story content (6-8 pages)
9. Port technology page content (3 pages)
10. Fill legal pages (privacy, terms, cookies)

**Phase 3 — Polish (Week 3-4)**
11. Fill parent/hub pages (platform, industries, resources, technology, tools)
12. Set up redirects from old URLs
13. Import FAQs (decide on format)
14. Port webinar and event content
15. QA every page

**Phase 4 — Nice to Have (Post-Launch)**
16. Port use-case pages (3 large pages)
17. Port AMP8 page if still relevant
18. Port landing pages if paid campaigns need them
19. Import testimonials
20. Build search functionality
