# Content Workflows Under the New Architecture

Astro + Storyblok + Vercel + HubSpot

**Date:** March 2026
**Status:** Draft — refine during Phase 0 build

---

## How the Three Layers Work

Every change flows through one or more of these layers:

| Layer | What lives here | Who touches it | How it deploys |
|---|---|---|---|
| **Git repo** (Astro) | Components, layouts, design tokens, HubSpot integration code, `claude.md` rules | Developer or Claude Cowork | Push to `main` → Vercel auto-builds |
| **Storyblok** (CMS) | Blog posts, case studies, news, campaign pages, editable page sections | Marketing / content team | Save + publish → webhook fires → Vercel rebuilds |
| **Vercel** (Host) | Builds the site, serves it, handles redirects, edge functions | Automatic — triggered by Git push or Storyblok webhook | No manual action needed |

**Key principle:** Content people never touch Git. Developers never edit blog posts in Storyblok. Each layer has clear ownership.

---

## Process 1: Creating a Campaign Page

**Example:** "/campaigns/canned-motor-pumps" — a targeted landing page for a specific asset type, industry, or use case. Includes a hero, value props, social proof, and a gated CTA (HubSpot form).

### Prerequisites

- Campaign page template exists in Astro (built once during Phase 0)
- HubSpot form created for the campaign
- Storyblok content type "Campaign Page" defined with fields for: hero headline, hero subtext, value prop blocks, testimonial, CTA text, HubSpot form ID, SEO metadata

### Steps

| Step | Who | Where | What happens |
|---|---|---|---|
| **1. Brief** | Marketing | Anywhere (doc, Slack, Cowork) | Write the campaign brief: audience, goal, key message, CTA offer, target keywords. Define what the page needs to say and who it's for. |
| **2. Create HubSpot form** | Marketing | HubSpot | Build the lead capture form. Set up the workflow: confirmation email, CRM pipeline assignment, internal notification. Copy the form ID. |
| **3. Create page in Storyblok** | Marketing | Storyblok visual editor | Go to Storyblok → Content → Campaigns → "Add Entry." Select the "Campaign Page" content type. Fill in all fields: headline, subtext, value props, testimonial, CTA copy, form ID, meta title, meta description, OG image. |
| **4. Preview** | Marketing | Storyblok visual editor | Use the visual editor's live preview to check layout, copy, and mobile rendering. The preview connects to the Astro dev environment or Vercel preview deployment. |
| **5. Internal review** | Marketing + stakeholder | Storyblok preview URL | Share the preview link. Reviewer checks copy, CTA, form, and brand compliance. |
| **6. Publish** | Marketing | Storyblok | Click "Publish." Storyblok fires a webhook to Vercel. Vercel rebuilds the site. Page goes live within ~60 seconds. |
| **7. Verify** | Marketing | Live site | Check the live URL. Submit a test form entry. Confirm it lands in HubSpot. Verify GTM events fire (use Tag Assistant). |
| **8. Distribute** | Marketing | Email, ads, social | Share the live URL through campaign channels. |

### When a developer is needed

- **New section type** that doesn't exist in the template (e.g., an interactive calculator, video embed with custom player). Developer builds the component in Astro, pushes to Git, then it becomes available in Storyblok.
- **Custom tracking** beyond standard CTA events. Developer adds the GTM dataLayer push in the component code.

### When Claude Cowork helps

- Writing the campaign copy (load `samotics-content-writing` + `samotics-gtm-intelligence`)
- Building a new Astro component if needed
- Generating the HubSpot form embed code
- Creating the SEO metadata and OG image spec

---

## Process 2: Creating a Blog Post

**Example:** "/resources/blog/how-to-reduce-pump-energy-costs" — a long-form article with hero image, body content, inline images, author, publish date, related posts, and a CTA.

### Prerequisites

- Blog post template and layout exist in Astro
- Storyblok content type "Blog Post" defined with fields for: title, slug, author, publish date, category, hero image, body (rich text), excerpt, SEO metadata, related posts

### Steps

| Step | Who | Where | What happens |
|---|---|---|---|
| **1. Draft** | Author | Google Docs, Notion, or Cowork | Write the post. Include headline, subheadings, body text, image suggestions, and CTA. |
| **2. Upload images** | Author / Marketing | Storyblok asset manager | Upload hero image and any inline images to Storyblok's asset library. Storyblok handles image optimization (resize, format conversion, CDN delivery) automatically. |
| **3. Create entry in Storyblok** | Author / Marketing | Storyblok visual editor | Go to Content → Blog → "Add Entry." Fill in: title, slug, author, date, category, hero image (select from assets), paste body into the rich text editor, add inline images, write the excerpt, fill SEO fields. |
| **4. Format and preview** | Author | Storyblok visual editor | Use the rich text editor to format headings, lists, bold, links. Preview the rendered post in the visual editor. Check mobile layout. |
| **5. Editorial review** | Editor / Marketing | Storyblok preview URL | Share preview link. Reviewer checks for: factual accuracy, brand voice compliance, SEO optimization, image quality, CTA presence. |
| **6. Schedule or publish** | Marketing | Storyblok | Either set a future publish date (Storyblok handles scheduled publishing) or click "Publish" immediately. Webhook fires → Vercel rebuilds. |
| **7. Verify** | Marketing | Live site | Check the live URL. Confirm the post appears in the blog index page, category filters work, related posts display correctly, OG tags render on social preview tools. |
| **8. Distribute** | Marketing | Email, social, LinkedIn | Share via newsletter, social channels, paid promotion. |

### Content type variations

The same process applies to:

- **Case studies** (`/resources/case-studies/...`) — same flow, different Storyblok content type with fields for: customer name, industry, challenge, solution, results, quote
- **Knowledge base articles** (`/resources/knowledge-base/...`) — same flow, content type has: topic, difficulty level, related articles
- **News items** (`/resources/news/...`) — same flow, shorter content, often linking to external press

### When a developer is needed

- **New rich text component** — e.g., an embedded data visualization, interactive chart, or code block with syntax highlighting. Developer builds the Astro component and registers it as a Storyblok nested block.
- **Blog index changes** — modifying sort order, pagination logic, or filter categories requires Astro code changes.

### When Claude Cowork helps

- Writing or editing the post (load `samotics-content-writing`)
- SEO-optimizing the title, meta description, headings
- Generating the excerpt and social copy variants
- Suggesting related posts based on content overlap

---

## Process 3: Publishing a Press Release

**Example:** "/resources/news/abb-launches-drive-with-esa-from-samotics" — a news announcement with structured metadata, often distributed externally first, then published on the site.

### Prerequisites

- News/press release template exists in Astro
- Storyblok content type "Press Release" defined with fields for: headline, slug, publish date, body (rich text), hero image, source attribution, external link (if syndicated), SEO metadata

### Steps

| Step | Who | Where | What happens |
|---|---|---|---|
| **1. Draft and approve** | Comms / Marketing + Legal | Google Docs or internal review | Write the press release. Get legal and leadership sign-off on claims, quotes, and partner mentions. This step happens before any CMS work. |
| **2. External distribution** (if applicable) | Comms | Wire service, partner channels | If this is a joint release or major announcement, distribute via PR wire (e.g., Business Wire, PR Newswire) or partner co-publish. Coordinate embargo timing. |
| **3. Prepare assets** | Marketing | Storyblok asset manager | Upload hero image, any supporting visuals, partner logos. |
| **4. Create entry in Storyblok** | Marketing | Storyblok | Go to Content → News → "Add Entry." Paste the approved text. Add images. Fill metadata. If there's an external version (wire service, partner site), add the external link. |
| **5. Coordinate publish timing** | Marketing | Storyblok | If the release has an embargo, use Storyblok's scheduled publishing to align with the external distribution time. Otherwise, publish immediately. |
| **6. Publish** | Marketing | Storyblok | Click "Publish" or let the schedule trigger. Webhook → Vercel rebuild → live. |
| **7. Verify** | Marketing | Live site | Check URL, OG tags (critical for press — journalists will share this), structured data. |
| **8. Amplify** | Marketing | Social, email, sales team | Share internally and externally. Brief the sales team if the release is commercially relevant. Update the homepage "Latest News" section if featured. |

### Key difference from blog posts

Press releases have an external coordination dimension. The content is often finalized and approved before anyone touches Storyblok. The CMS step is mechanical — paste approved copy, attach assets, publish on schedule.

### When a developer is needed

- **Structured data for press releases** — adding `NewsArticle` schema markup to the template (one-time setup during Phase 0).
- **Homepage "Latest News" widget** — if the homepage dynamically pulls recent news, developer wires that up as an Astro component fetching from Storyblok.

### When Claude Cowork helps

- Drafting the press release (load `samotics-content-writing`)
- Writing social distribution copy (multiple variants for LinkedIn, Twitter, email)
- Generating the structured data JSON-LD
- Preparing the internal brief for sales team (load `internal-comms`)

---

## Process 4: Making Changes to an Existing Page

This is the most common workflow. It covers everything from fixing a typo to restructuring a page's layout.

### Decision tree: Where does the change live?

```
Is the change to CONTENT (text, images, metadata)?
  ├── YES → Make the change in Storyblok
  │         (no developer needed)
  │
  └── NO → Is it a STRUCTURAL or DESIGN change?
            ├── YES → Change the Astro component/layout in Git
            │         (developer or Claude Cowork)
            │
            └── Is it a TRACKING or INTEGRATION change?
                  └── YES → Change the HubSpot/GTM code in Git
                            (developer or Claude Cowork)
```

### Path A: Content change (Storyblok)

**Examples:** Fix a typo, update a customer quote, swap a hero image, change a CTA label, update pricing, edit meta description.

| Step | Who | Where | What happens |
|---|---|---|---|
| **1. Find the page** | Marketing | Storyblok | Navigate to the page in the content tree. Or use Storyblok's search. |
| **2. Edit** | Marketing | Storyblok visual editor | Make the change directly in the visual editor. See the update in real-time preview. |
| **3. Review** | Marketing | Storyblok preview | Check the change looks correct on desktop and mobile. |
| **4. Publish** | Marketing | Storyblok | Click "Publish." Webhook → Vercel rebuild → live in ~60 seconds. |

**Time from edit to live: ~2 minutes.**

### Path B: Structural or design change (Git)

**Examples:** Add a new section type to a page template, change the header layout, update design tokens (colors, spacing), add a new component (testimonial carousel, pricing table), modify the navigation structure.

| Step | Who | Where | What happens |
|---|---|---|---|
| **1. Scope the change** | Developer / Claude Cowork | Codebase | Identify which component(s) or layout(s) need modification. Check the design system specs. |
| **2. Branch** | Developer / Claude Cowork | Git | Create a feature branch from `main`. |
| **3. Build** | Developer / Claude Cowork | Local dev / Cowork session | Make the code changes. Test locally with `astro dev`. |
| **4. Preview deploy** | Automatic | Vercel | Push the branch. Vercel creates a preview deployment with a unique URL. |
| **5. Review** | Marketing + Developer | Vercel preview URL | Check the changes on the preview deployment. Verify nothing broke on other pages using the same component. |
| **6. Merge** | Developer | Git (GitHub PR) | Merge the feature branch into `main`. Vercel auto-deploys to production. |
| **7. Verify** | Developer | Live site | Spot-check affected pages on production. |

**Time from code to live: ~30 minutes to a few hours, depending on review cycle.**

### Path C: Tracking or integration change (Git + external platform)

**Examples:** Add a new GTM event, connect a HubSpot form to a new workflow, add a consent category, change tracking parameters.

| Step | Who | Where | What happens |
|---|---|---|---|
| **1. Define the requirement** | Marketing | Brief / Slack | Specify what needs to be tracked, which events, what data. |
| **2. Update GTM container** (if needed) | Developer / Marketing | GTM web interface | Add or modify tags, triggers, variables in GTM. |
| **3. Update code** (if needed) | Developer / Claude Cowork | Git | Add `dataLayer.push()` calls, HubSpot embed code, or consent logic in Astro components. |
| **4. Test** | Developer | Preview deployment + GTM debug mode | Use GTM's preview mode to verify events fire correctly. Check HubSpot for test form submissions. |
| **5. Publish GTM** | Marketing / Developer | GTM | Publish the GTM container version. |
| **6. Merge code** | Developer | Git | Merge and deploy code changes. |
| **7. Validate** | Marketing | GA4 real-time reports | Confirm events appear in GA4 with correct parameters. |

---

## Quick Reference: Who Does What

| Role | Tools they use | What they own |
|---|---|---|
| **Marketing / Content** | Storyblok visual editor, HubSpot, GTM (tags) | All content: blog posts, case studies, news, campaign pages, page edits, forms, email workflows |
| **Developer / Claude Cowork** | Git (VS Code / Cowork), Astro CLI, Vercel dashboard | All code: components, layouts, design tokens, integrations, build config, redirects |
| **Both** | Vercel preview URLs, GTM debug mode | QA and verification |

---

## What Storyblok Can and Cannot Do

### Can do (no developer needed)

- Create, edit, and publish any page that uses an existing template
- Upload and manage images (with automatic optimization)
- Schedule future publishes
- Revert to previous versions of any content entry
- Duplicate an existing page as a starting point
- Reorder pages and manage the content tree
- Edit SEO metadata (title, description, OG image)
- A/B test content variants (with Storyblok's experimentation feature)

### Cannot do (needs a developer)

- Add a new page type or template that doesn't exist yet
- Create a new interactive component (calculator, configurator, map)
- Change the site navigation structure (header/footer links)
- Modify design tokens (colors, fonts, spacing)
- Add or change tracking events
- Set up redirects
- Change build or deployment configuration

---

## Naming Conventions

| Content type | URL pattern | Storyblok folder |
|---|---|---|
| Blog post | `/resources/blog/{slug}` | Content → Resources → Blog |
| Case study | `/resources/case-studies/{slug}` | Content → Resources → Case Studies |
| Knowledge base | `/resources/knowledge-base/{slug}` | Content → Resources → Knowledge Base |
| News / Press release | `/resources/news/{slug}` | Content → Resources → News |
| Campaign page | `/campaigns/{slug}` | Content → Campaigns |
| Industry page | `/industries/{slug}` | Content → Industries |
| Platform page | `/platform/{slug}` | Content → Platform |
| Technology page | `/technology/{slug}` | Content → Technology |
