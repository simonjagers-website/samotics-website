# Samotics.com Production Migration Plan

Static HTML → Astro + Storyblok + Vercel + HubSpot

**Date:** March 2026
**Status:** Draft
**Owner:** Simon Jagers

---

## Current State Audit

| Dimension | Status | Detail |
|---|---|---|
| **Pages** | 199 static HTML files | All inline CSS/JS, no shared stylesheet or component library |
| **Domain** | samoticstestpage.com | All 199 canonicals point here — must migrate to samotics.com |
| **Design system** | 1 of 199 pages updated | Only `/problem` has the orange header + new tokens. 198 pages still on old Space Cadet header |
| **GA4 / GTM** | Zero | No analytics on any page |
| **HubSpot** | 3 legacy references | No forms connected, no tracking code, no CRM integration |
| **Forms** | 11 pages have `<form>` elements | Contact, asset audit, security docs, resource gating — none connected to a backend |
| **Sitemap** | Missing | No sitemap.xml |
| **Robots.txt** | Missing | No robots.txt |
| **Structured data** | 38 pages | Partial coverage — needs audit for accuracy |
| **OG tags** | Partial | Some pages have them, homepage missing |
| **Cookie consent** | Missing | No consent manager |
| **SSL** | Unknown | Needs verification on production domain |
| **Shared CSS/JS** | None | Zero .css or .js files — everything is inline per page |
| **CMS** | None | All content hardcoded in HTML |
| **Deployment** | Manual | No CI/CD pipeline |

---

## Target Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Git Repo   │────▶│   Vercel     │◀────│  Storyblok  │
│  (Astro)    │     │  (Build +    │     │  (Content)  │
│             │     │   Deploy)    │     │             │
│ Components  │     │              │     │ Blog posts  │
│ Layouts     │     │ Auto-deploy  │     │ Case studies│
│ Design      │     │ on push or   │     │ News        │
│ tokens      │     │ webhook      │     │ Campaign    │
│ claude.md   │     │              │     │ pages       │
│ HubSpot     │     │              │     │             │
│ integration │     │              │     │ Visual      │
│ code        │     │              │     │ editor for  │
│             │     │              │     │ non-devs    │
└─────────────┘     └──────┬───────┘     └─────────────┘
                           │
                    ┌──────▼───────┐
                    │ samotics.com │
                    │              │
                    │ GA4 + GTM    │
                    │ HubSpot      │
                    │ Cookie       │
                    │ consent      │
                    └──────────────┘
```

---

## Migration Phases

### Phase 0: Foundation (Week 1–2)

Everything that needs to exist before any page goes live.

**0.1 — Astro project scaffold**

- [ ] Initialise Astro project with TypeScript
- [ ] Configure Vercel adapter (`@astrojs/vercel`)
- [ ] Set up project structure:
  ```
  src/
    components/    # Header, Footer, CTA, Cards, etc.
    layouts/       # BaseLayout, PageLayout, BlogLayout
    pages/         # Static routes
    styles/        # Global design tokens, shared CSS
    content/       # Local content (non-CMS pages)
    lib/           # HubSpot, Storyblok, GTM utilities
  public/
    assets/        # Images, fonts, favicons
  ```
- [ ] Create `claude.md` project instructions file (brand voice, content schemas, writing rules, five-agent pipeline)

**0.2 — Design system as shared CSS**

- [ ] Extract the design token `:root` block from the updated problem page into `src/styles/tokens.css`
- [ ] Create `src/styles/typography.css` from the typography system spec
- [ ] Create `src/styles/reset.css` (minimal reset)
- [ ] Create `src/styles/global.css` that imports all three
- [ ] Every page imports one shared stylesheet instead of inline CSS

**0.3 — Component library**

Build these Astro components from the existing inline HTML/CSS:

| Component | Source | Notes |
|---|---|---|
| `Header.astro` | Current header CSS/HTML | Orange header, Space Cadet CTA, mobile menu |
| `Footer.astro` | Current footer CSS/HTML | Pre-footer CTA, footer grid, accordion mobile |
| `HeroSection.astro` | Hero pattern from problem page | Props: title, subtitle, lead, bgImage, ctas |
| `SectionHeading.astro` | Overline + H2 + lead pattern | Props: overline, title, lead, overlineColor |
| `StatCard.astro` | Scale section stat cards | Props: value, label, source |
| `ContentCard.astro` | Cost/barrier card patterns | Props: icon, title, desc, tags |
| `CTABlock.astro` | CTA block pattern | Props: heading, sub, primaryCTA, secondaryCTA |
| `Button.astro` | .sam-btn variants | Props: variant (primary/ghost/secondary), href, label |
| `BaseLayout.astro` | HTML shell | Head tags, fonts, GTM, cookie consent, header, footer |

**0.4 — Domain and hosting**

- [ ] Configure samotics.com DNS to point to Vercel
- [ ] Set up SSL certificate (Vercel handles this automatically)
- [ ] Create Vercel project, connect to git repo
- [ ] Configure preview deployments for branches
- [ ] Set up production deployment on `main` branch merge

**0.5 — Storyblok setup**

- [ ] Create Storyblok space for samotics.com
- [ ] Define content types:
  - `blog_post` — title, author, date, category, body (rich text), featured image, SEO fields
  - `case_study` — title, customer, industry, asset type, kpi_results, body, images
  - `news_item` — title, date, body, source link
  - `campaign_page` — flexible layout with content blocks
- [ ] Install Storyblok Astro integration (`@storyblok/astro`)
- [ ] Configure preview mode for visual editor
- [ ] Set up webhook to Vercel for content publish → rebuild

---

### Phase 1: Core Pages Migration (Week 2–4)

Convert the highest-traffic static pages to Astro components. These pages stay in git (not CMS) because they change rarely and need tight design control.

**1.1 — Migrate core pages (in order of priority)**

| Priority | Page | URL | Notes |
|---|---|---|---|
| P0 | Homepage | `/` | Most traffic. Uses all components. Migration template for everything else. |
| P0 | Problem | `/problem` | Already has updated design system. Convert to components. |
| P0 | Contact | `/contact` | Must have working HubSpot form before launch |
| P0 | Contact/Asset Audit | `/contact/asset-audit` | Second conversion form |
| P1 | Technology landing | `/technology` | Section router |
| P1 | Technology/ESA | `/technology/esa` | Core credibility page |
| P1 | Technology/How It Works | `/technology/how-it-works` | |
| P1 | Platform landing | `/platform` | Section router |
| P1 | Platform/SAM4 | `/platform/sam4` | Product page |
| P1 | About | `/about` | Trust/credibility |
| P2 | All industry pages (7) | `/industries/*` | Can use a shared template |
| P2 | Remaining technology pages | `/technology/*` | |
| P2 | Remaining platform pages | `/platform/*` | |
| P3 | Proof hub + case studies | `/proof/*` | Move to Storyblok as CMS content |
| P3 | Blog posts | `/resources/blog/*` | Move to Storyblok |
| P3 | News | `/resources/news/*` | Move to Storyblok |

**1.2 — Apply design system to all migrated pages**

Every page gets the updated design system as part of migration:
- Orange header (not Space Cadet)
- Updated CSS tokens
- Typography per spec (Major Third desktop, Minor Third mobile)
- Proper shadows (Space Cadet base, not black)
- Zero border-radius on cards
- Section backgrounds: white/seashell alternating, dark only for hero+footer

---

### Phase 2: Tracking and Analytics (Week 3–4)

**2.1 — Google Tag Manager**

- [ ] Create GTM container for samotics.com
- [ ] Add GTM snippet to `BaseLayout.astro` (head + body)
- [ ] Configure data layer variables:
  - `page_type` (homepage, problem, technology, platform, industry, proof, blog, contact)
  - `page_section` (which section of the site)
  - `user_intent` (demo, audit, security-docs, case-study — from URL params)

**2.2 — GA4**

- [ ] Create GA4 property for samotics.com
- [ ] Connect GA4 to GTM (GA4 Configuration tag)
- [ ] Set up events:
  - `page_view` (automatic)
  - `scroll_depth` (25%, 50%, 75%, 100%)
  - `cta_click` (label, destination, page)
  - `form_start` (which form)
  - `form_submit` (which form, success/failure)
  - `outbound_link` (destination)
  - `file_download` (filename, type)
- [ ] Set up conversions:
  - `demo_request` — form submission on /contact with intent=demo
  - `asset_audit_request` — form submission on /contact/asset-audit
  - `security_docs_request` — form submission on /platform/security
  - `case_study_download` — gated PDF download
- [ ] Configure custom dimensions:
  - `industry` (from form selection or URL)
  - `content_type` (blog, case study, knowledge base, news)

**2.3 — HubSpot integration**

- [ ] Install HubSpot tracking code in `BaseLayout.astro`
- [ ] Create HubSpot forms:
  - Demo request form (fields per CTA strategy spec)
  - Asset audit form (fields per CTA strategy spec)
  - Security docs request form
  - Case study download form
  - Newsletter/blog subscription form
  - General contact form
- [ ] Configure form-to-CRM pipeline:
  - Lead creation on form submit
  - Auto-assign to AE by industry + region
  - Slack notification to sales channel
  - Confirmation email (per CTA strategy post-submission spec)
- [ ] Set up HubSpot ↔ GTM event forwarding:
  - `gtm_event: demo_request` on demo form submit
  - `gtm_event: audit_request` on audit form submit
- [ ] Configure lead scoring rules in HubSpot:
  - Form type weight
  - Industry weight
  - Fleet size weight
  - Page visit history weight

**2.4 — Cookie consent**

- [ ] Implement cookie consent banner (Cookiebot, OneTrust, or custom)
- [ ] Consent categories: Necessary, Analytics, Marketing
- [ ] GTM configured to respect consent state:
  - GA4 fires only after Analytics consent
  - HubSpot tracking fires only after Marketing consent
  - HubSpot forms fire always (Necessary — they're functional)
- [ ] Cookie policy page (`/cookies`) — already exists in static, migrate to Astro

---

### Phase 3: SEO Infrastructure (Week 4–5)

**3.1 — Technical SEO**

- [ ] Generate `sitemap.xml` automatically via `@astrojs/sitemap`
- [ ] Create `robots.txt`:
  ```
  User-agent: *
  Allow: /
  Disallow: /tools/
  Disallow: /campaigns/
  Sitemap: https://samotics.com/sitemap-index.xml
  ```
- [ ] Update ALL canonical URLs from `samoticstestpage.com` → `samotics.com`
- [ ] Enforce consistent URL format (trailing slash or not — pick one, redirect the other)
- [ ] Set up 301 redirects for any URL changes from old site
- [ ] Add `hreflang` tags if multilingual is planned (DE, NL, FR)

**3.2 — On-page SEO**

- [ ] Audit and update `<title>` tags — format: `{Page Title} | Samotics`
- [ ] Audit and update `<meta name="description">` — unique per page, 150-160 chars
- [ ] Complete OG tags on all pages:
  - `og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `og:site_name`
- [ ] Add Twitter Card meta tags
- [ ] Ensure H1 hierarchy is correct on every page (one H1, proper H2-H6 nesting)

**3.3 — Structured data**

- [ ] Audit existing 38 pages with structured data for accuracy
- [ ] Add `Organization` schema to homepage
- [ ] Add `WebSite` schema with search action
- [ ] Add `BreadcrumbList` schema to all pages
- [ ] Add `Article` schema to blog posts
- [ ] Add `FAQPage` schema where applicable
- [ ] Add `Product` schema to SAM4 platform page
- [ ] Validate all structured data via Google Rich Results Test

**3.4 — Performance**

- [ ] Image optimisation: convert all images to WebP/AVIF via Astro's `<Image>` component
- [ ] Lazy load below-fold images
- [ ] Preload critical fonts (already using `font-display: swap`)
- [ ] Target Core Web Vitals:
  - LCP < 2.5s
  - FID < 100ms
  - CLS < 0.1
- [ ] Set up performance monitoring in GA4

---

### Phase 4: Content Migration to Storyblok (Week 5–7)

These pages change frequently and benefit from CMS management.

**4.1 — Blog posts**

- [ ] Migrate all blog post content to Storyblok `blog_post` content type
- [ ] Create blog listing page (`/resources/blog`) that pulls from Storyblok
- [ ] Create blog post template that renders Storyblok rich text
- [ ] Set up category/tag taxonomy
- [ ] Configure RSS feed

**4.2 — Case studies**

- [ ] Migrate case studies to Storyblok `case_study` content type
- [ ] Create case study listing page (`/proof/case-studies`) with industry filtering
- [ ] Create case study template
- [ ] Link case studies to industry pages (dynamic)

**4.3 — News/press**

- [ ] Migrate news items to Storyblok `news_item` content type
- [ ] Create news listing page
- [ ] Create news item template

**4.4 — Resource gating**

- [ ] Whitepapers, engineering proof pack, business case toolkit — gate with HubSpot forms
- [ ] Create resource download template with form + immediate PDF delivery
- [ ] Track downloads as GA4 conversions

---

### Phase 5: Launch Checklist (Week 7–8)

**Pre-launch (before DNS switch)**

- [ ] All P0 and P1 pages migrated and design-system compliant
- [ ] All forms tested end-to-end (submit → HubSpot CRM → Slack notification → confirmation email)
- [ ] GA4 + GTM firing correctly (verify in GTM Preview mode)
- [ ] Cookie consent working and blocking tags before consent
- [ ] HubSpot tracking active
- [ ] Sitemap.xml generated and valid
- [ ] Robots.txt in place
- [ ] All canonicals pointing to samotics.com
- [ ] 301 redirects configured for any changed URLs
- [ ] OG tags and structured data validated
- [ ] Core Web Vitals passing
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsive tested (iOS Safari, Android Chrome)
- [ ] Accessibility: keyboard navigation, screen reader, WCAG 2.1 AA contrast
- [ ] Favicon and Apple touch icons
- [ ] 404 page styled and functional
- [ ] Legal pages live: Privacy, Terms, Cookies

**Launch (DNS cutover)**

- [ ] Point samotics.com DNS to Vercel
- [ ] SSL certificate provisioned
- [ ] Verify all pages resolve on production domain
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Verify GA4 receiving real traffic
- [ ] Verify HubSpot tracking active on production
- [ ] Test all forms on production domain
- [ ] Monitor Core Web Vitals for 48 hours

**Post-launch (Week 1–2 after)**

- [ ] Monitor Search Console for crawl errors
- [ ] Monitor 404 logs — add redirects for any broken inbound links
- [ ] Verify HubSpot lead flow is working (real submissions → CRM → sales notification)
- [ ] Set up GA4 dashboards: traffic, conversions, top pages, bounce rate by section
- [ ] Set up weekly automated report (GA4 → email)
- [ ] Index coverage check in Search Console after 1 week
- [ ] Performance regression check after 2 weeks

---

## Scope Decision: What Stays in Git vs Storyblok

| Content type | Location | Reason |
|---|---|---|
| Homepage | Git | Tight design control, rarely changes |
| Problem pages | Git | Core narrative, stable |
| Technology pages | Git | Technical accuracy, developer-maintained |
| Platform pages | Git | Product pages, design-heavy |
| Industry pages | Git | Template-driven but stable |
| About | Git | Stable |
| Contact/forms | Git | Functional, form logic |
| Legal pages | Git | Stable |
| Blog posts | Storyblok | Frequent updates, multiple authors |
| Case studies | Storyblok | Regular additions, filterable |
| News/press | Storyblok | Regular additions |
| Campaign pages | Storyblok | Marketing-driven, fast iteration |
| Resource downloads | Storyblok | Gated content, marketing-managed |

---

## Open Questions

1. **Current samotics.com** — Is there an existing live site that needs redirect mapping? Or is samotics.com currently parked/redirecting?
2. **HubSpot tier** — Which HubSpot plan? Free CRM, Starter, Professional? Affects form features and automation.
3. **Storyblok tier** — Community (free) or Business? Affects API limits and visual editor features.
4. **Existing Google Search Console** — Is there an existing GSC property for samotics.com with historical data?
5. **Image assets** — The current site references placeholder/stock images in many places. Are production images ready?
6. **Multilingual** — Any plans for DE/NL/FR pages? Affects URL structure decisions now.
7. **Team** — Who else will work on this besides you? Affects Storyblok role setup and claude.md documentation depth.
8. **Timeline** — Is the 8-week estimate realistic for your availability? The critical path is Phase 0 (Astro scaffold) → Phase 1 P0 pages → Phase 2 forms/tracking → launch.

---

## Estimated Effort

| Phase | Effort | Dependency |
|---|---|---|
| Phase 0: Foundation | 2 weeks | None — start here |
| Phase 1: Core pages | 2 weeks | Phase 0 complete |
| Phase 2: Tracking | 1 week (parallel with Phase 1) | GTM/GA4 accounts created |
| Phase 3: SEO | 1 week (parallel with Phase 1) | Astro sitemap plugin |
| Phase 4: CMS content | 2 weeks | Storyblok space + templates |
| Phase 5: Launch | 1 week | All P0/P1 complete |
| **Total** | **~6–8 weeks** | Critical path: Phase 0 → 1 → 5 |

Phase 4 (CMS migration of blog/case studies) can happen after launch. The site can go live with those pages still as static HTML, then migrate to Storyblok incrementally.
