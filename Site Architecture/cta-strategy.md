# CTA Strategy

Primary and secondary CTAs per page, button copy, form fields, and post-submission behaviour

**Document:** CTA Strategy — Base
**Layer:** Conversion
**Owner:** Marketing
**Status:** Draft
**Date:** February 2026
**Dependencies:** Site Architecture, Navigation Spec, #12 User Journey Map, #3 Buying Scenario Framework, Messaging Framework
**Feeds Into:** Page Briefs, Component Inventory, CMS Build, Marketing Automation

---

## How to Use This Document

This document specifies every CTA on samotics.com — what it says, where it appears, what form fields it triggers, and what happens after submission. Page brief authors use it to place the right CTAs on the right pages. Designers use it to build CTA components. Developers use it to wire form logic and post-submission flows.

The guiding rule: every CTA must match the persona's urgency and the scenario's stage. A Reliability Manager after a pump failure (S1) wants a demo in 48 hours. An Operations Director building a business case (S2) wants a downloadable PDF. A CTO evaluating strategic fit (S3) wants an executive conversation. One button cannot serve all three.

---

## CTA Inventory

Samotics.com uses five distinct CTAs in v1. Each maps to a specific persona, scenario, and conversion intent. Two more arrive in Phase 2/3.

| CTA | Primary Persona | Scenario | Urgency | Destination | Phase |
|-----|----------------|----------|---------|-------------|-------|
| **Request a Demo** | Reliability Manager | S1, S2 | High | `/contact` (demo intent) | v1 |
| **Start Your Asset Audit** | Operations Director | S2, S3 | Medium | `/contact/asset-audit` | v1 |
| **Talk to Us** | CTO / VP Engineering | S3 | Medium | `/contact` (executive intent) | v1 |
| **Request Security Docs** | Digital / Innovation Lead | S3 | Medium | Inline form on `/platform/security` | v1 |
| **Download Case Study** | Operations Director, all | S1–S3 | Varies | Inline form or direct download on `/proof/[case]` | v1 |
| **Discuss Partnership** | Channel Partner / OEM | S5 | Low | `/contact/partner-inquiry` | Phase 2 |
| **See Impact Data** | ESG / Sustainability Lead | S4 | Medium | `/contact` (energy intent) | Phase 3 |

---

## Global Nav CTA

The navigation bar carries one CTA across all pages. It does not change per page.

| Element | Specification |
|---------|--------------|
| **Button copy** | Request a Demo |
| **URL** | `/contact` |
| **Style** | Filled button, brand accent colour. Visually distinct from nav text links. |
| **Behaviour** | Links to `/contact` with `?intent=demo` parameter pre-selected (auto-selects "Demo" in the intent router). |
| **Rationale** | S1 (Critical Failure) is the highest-urgency, highest-traffic scenario. "Request a Demo" matches this urgency and is universally understood. Other CTAs appear contextually on individual pages. |
| **Mobile** | Visible in the nav bar at all times. Does not collapse into the hamburger menu. |

---

## CTA Definitions

### 1. Request a Demo

The primary conversion action for technical evaluators who have seen enough to want a live walkthrough.

**Button copy:** Request a Demo

**Where it appears (primary):**
- Nav bar (global, every page)
- Homepage hero
- `/technology/esa` — bottom of page
- `/technology/esa-vs-vibration` — bottom of page
- `/platform/sam4` — bottom of page
- `/platform/how-it-installs` — bottom of page
- `/industries/[x]` — bottom of page
- `/proof/[case-study]` — inline after case study content

**Where it appears (secondary):**
- `/technology/how-it-works` — bottom of page (secondary to "See the Platform")
- `/proof` hub — footer section

**Form destination:** `/contact` with `?intent=demo`

**Form fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First name | Text | Yes | |
| Last name | Text | Yes | |
| Work email | Email | Yes | Validated: must be company domain, not gmail/hotmail/etc. |
| Company | Text | Yes | |
| Job title | Text | Yes | Helps sales route to the right AE |
| Industry | Dropdown | Yes | Options: Water & Wastewater, Oil & Gas, Metals & Mining, Chemicals, Pulp & Paper, Pharma & Life Sciences, Other |
| Number of motors/assets | Dropdown | No | Options: <50, 50–200, 200–1,000, 1,000+. Qualifies fleet scale. |
| Anything else? | Textarea | No | Max 500 chars. Free-text for context. |

**Post-submission behaviour:**

| Step | Detail |
|------|--------|
| **Confirmation screen** | "Thanks, [First name]. We'll be in touch within 1 business day to schedule your demo." |
| **Confirmation email** | Immediate. Subject: "Your Samotics demo request." Body: confirms receipt, sets expectation (technical conversation, not a sales pitch), includes a link to a relevant case study based on industry selected. |
| **Internal routing** | Lead pushed to CRM (HubSpot). Auto-assigned to AE by industry and region. Slack notification to sales team. |
| **SLA** | Sales responds within 1 business day. Demo scheduled within 5 business days. |
| **Tracking** | `gtm_event: demo_request`, tagged with source page URL and industry. |

---

### 2. Start Your Asset Audit

A lower-commitment entry point for evaluators who aren't ready for a demo but want a concrete next step. Outputs a gap report — gives the Operations Director ammunition for an internal proposal.

**Button copy:** Start Your Asset Audit

**Where it appears (primary):**
- `/problem` — hero CTA and bottom of page
- `/problem/proximity-penalty` — bottom of page

**Where it appears (secondary):**
- Homepage — secondary CTA below fold (after the problem statement block)
- `/proof` hub — alternative CTA alongside "Request a Demo"
- `/proof/yorkshire-water` — inline (fleet-scale case, audit is natural next step)
- `/proof/southern-water` — inline

**Form destination:** `/contact/asset-audit`

**Form fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First name | Text | Yes | |
| Last name | Text | Yes | |
| Work email | Email | Yes | Company domain validation |
| Company | Text | Yes | |
| Job title | Text | Yes | |
| Industry | Dropdown | Yes | Same options as demo form |
| Number of sites | Dropdown | Yes | Options: 1, 2–5, 6–20, 20+ |
| Estimated number of rotating assets | Dropdown | Yes | Options: <100, 100–500, 500–2,000, 2,000+ |
| Current monitoring coverage | Dropdown | No | Options: <25%, 25–50%, 50–75%, >75%, Don't know |
| What prompted your interest? | Textarea | No | Max 500 chars |

**Post-submission behaviour:**

| Step | Detail |
|------|--------|
| **Confirmation screen** | "Thanks, [First name]. We'll prepare your asset audit scope and reach out within 2 business days." |
| **Confirmation email** | Immediate. Subject: "Your Samotics asset audit request." Body: explains what an asset audit delivers (coverage gap quantification, prioritised asset list, ROI estimate), sets timeline expectation, includes a link to the Yorkshire Water case study PDF. |
| **Internal routing** | Lead to CRM. Tagged as "Asset Audit" opportunity. Auto-assigned to AE. Higher qualification score due to fleet data provided. |
| **SLA** | Sales responds within 2 business days with proposed audit scope. |
| **Tracking** | `gtm_event: asset_audit_request`, tagged with source page, industry, fleet size. |

---

### 3. Talk to Us

Executive-level engagement. Not a product demo — a leadership conversation. Used by CTOs and VP Engineering evaluating SAM4 as a strategic initiative.

**Button copy:** Talk to Us

**Where it appears (primary):**
- `/about` — hero CTA
- `/about/abb` (or `/partners/abb`) — bottom of page

**Where it appears (secondary):**
- `/platform/sam4` — secondary CTA (for visitors coming from `/about`, signalling executive intent)
- `/platform/integrations` — bottom of page

**Form destination:** `/contact` with `?intent=executive`

**Form fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First name | Text | Yes | |
| Last name | Text | Yes | |
| Work email | Email | Yes | Company domain validation |
| Company | Text | Yes | |
| Job title | Text | Yes | |
| Industry | Dropdown | Yes | Same options as above |
| What would you like to discuss? | Dropdown | Yes | Options: Strategic evaluation, Enterprise rollout, ABB partnership, Other |
| Number of sites | Dropdown | No | Options: 1, 2–5, 6–20, 20+ |
| Additional context | Textarea | No | Max 500 chars |

**Post-submission behaviour:**

| Step | Detail |
|------|--------|
| **Confirmation screen** | "Thanks, [First name]. A member of our leadership team will reach out within 1 business day." |
| **Confirmation email** | Immediate. Subject: "Your Samotics inquiry." Body: confirms receipt. Tone: peer-level, not transactional. No case study push — this persona doesn't need selling. Mentions that a senior team member (not an SDR) will follow up. |
| **Internal routing** | Lead to CRM. Tagged as "Executive." Routed to senior AE or Sales Director based on company size and region. Slack notification to sales leadership. |
| **SLA** | Senior sales responds within 1 business day. |
| **Tracking** | `gtm_event: executive_inquiry`, tagged with source page, discussion topic. |

---

### 4. Request Security Docs

Gated download for the Digital/Innovation Lead who needs SOC 2 reports, architecture diagrams, and compliance documentation. This persona has veto power — if they can't get these docs, the deal stalls.

**Button copy:** Request Security Docs

**Where it appears (primary):**
- `/platform/security` — inline, positioned after the certifications and compliance content (not at the very top — they need to read the page first)

**Where it appears (secondary):**
- `/platform/integrations` — sidebar or bottom link ("Need security documentation?")

**This CTA does NOT appear in the nav or on unrelated pages.** It serves one persona (Digital Lead) in one scenario (S3). Putting it elsewhere dilutes the nav and confuses other personas.

**Form destination:** Inline form on `/platform/security` (no page redirect). Alternatively, a modal overlay.

**Form fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First name | Text | Yes | |
| Last name | Text | Yes | |
| Work email | Email | Yes | Company domain validation |
| Company | Text | Yes | |
| Job title | Text | Yes | |
| Which documents do you need? | Multi-select checkboxes | Yes | Options: SOC 2 Type II Report, ISO 27001 Certificate, Architecture Diagram, NIS2 Compliance Summary, All of the above |

**No industry field, no fleet size, no textarea.** This persona wants docs, not a conversation. Keep the form short. Every extra field is friction for someone with veto power.

**Post-submission behaviour:**

| Step | Detail |
|------|--------|
| **Confirmation screen** | "Downloading now. Check your inbox for the full security documentation package." |
| **Immediate action** | Selected documents delivered as immediate download (browser download) AND emailed as a ZIP or individual PDFs. No "we'll get back to you" delay — this persona needs the docs NOW to unblock their review. |
| **Confirmation email** | Immediate. Subject: "Samotics security documentation." Body: links to each requested document. Includes a single line: "Questions about our security architecture? Reply to this email." No marketing follow-up sequence. |
| **Internal routing** | Lead to CRM. Tagged as "Security Review." Flagged to AE working the account (if known) or auto-assigned. Indicates S3 deal in progress. |
| **SLA** | Docs delivered immediately. If the AE recognises the company from an active deal, they reach out within 1 business day to offer a security architecture walkthrough. |
| **Tracking** | `gtm_event: security_docs_download`, tagged with specific documents requested. |

---

### 5. Download Case Study

PDF downloads on case study pages. Critical for the Operations Director who sells internally with documents, not URLs. Also serves Reliability Managers who want to share proof with their boss.

**Button copy:** Download PDF *(on case study pages)*
**Alternative copy:** Download Case Study *(on proof hub, if used as a card-level action)*

**Where it appears:**
- Every `/proof/[case-study]` page — prominent button near the top of the page (above fold) AND repeated at the bottom
- `/proof` hub — download icon on each case study card (direct download, no form)

**Form fields:**

**Decision: Ungated.** Direct PDF download on click. No form. The Operations Director needs to share this internally — gating adds friction at the most critical journey step (S2, step 5). The visitor is already on the site and will convert through another CTA when ready.

**Post-download behaviour:**

| Step | Detail |
|------|--------|
| **Action** | PDF downloads immediately in browser. No confirmation page. |
| **Tracking** | `gtm_event: case_study_download`, tagged with case study name and source page. |
| **No email follow-up** | Ungated means no email capture. The proof is the nurture. |

---

### 6. Discuss Partnership (Phase 2)

Partnership inquiry for Channel Partners and OEMs. Distinct from product demo — different intent, different conversation, different sales owner.

**Button copy:** Discuss Partnership

**Where it appears (Phase 2):**
- `/partners` — hero CTA
- `/partners/abb` — secondary CTA
- `/about` — secondary link ("Interested in partnering?")

**v1 interim:** Until Phase 2 delivers `/partners` and `/contact/partner-inquiry`, partner inquiries route through the main `/contact` form using the intent selector ("Partnership discussion").

**Form destination:** `/contact/partner-inquiry` (Phase 2)

**Form fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First name | Text | Yes | |
| Last name | Text | Yes | |
| Work email | Email | Yes | Company domain validation |
| Company | Text | Yes | |
| Job title | Text | Yes | |
| Company type | Dropdown | Yes | Options: System Integrator, OEM, Service Provider, Distributor, Other |
| Industries you serve | Multi-select | Yes | Options: Water, Oil & Gas, Metals & Mining, Chemicals, Pulp & Paper, Other |
| What interests you about partnering? | Textarea | No | Max 500 chars |

**Post-submission behaviour:**

| Step | Detail |
|------|--------|
| **Confirmation screen** | "Thanks, [First name]. Our partnerships team will be in touch within 2 business days." |
| **Confirmation email** | Immediate. Subject: "Your Samotics partnership inquiry." Body: confirms receipt, links to the ABB partnership page as a reference model. |
| **Internal routing** | Lead to CRM. Tagged as "Partner." Routed to partnerships lead (not standard sales). |
| **SLA** | Partnerships team responds within 2 business days. |
| **Tracking** | `gtm_event: partner_inquiry`, tagged with company type and industries. |

---

### 7. See Impact Data (Phase 3)

Energy and ESG-focused conversion for the Sustainability Lead. Arrives when dedicated energy content is built.

**Button copy:** See Impact Data

**Where it appears (Phase 3):**
- `/industries/energy-efficiency` — hero CTA
- Industry pages (Water, Pulp & Paper) — secondary CTA in energy content sections

**v1 interim:** Energy-interested visitors route through the main `/contact` form. No dedicated energy CTA until Phase 3 content exists.

**Form destination:** `/contact` with `?intent=energy`

**Form fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First name | Text | Yes | |
| Last name | Text | Yes | |
| Work email | Email | Yes | |
| Company | Text | Yes | |
| Job title | Text | Yes | |
| Industry | Dropdown | Yes | Same options as above |
| Primary interest | Dropdown | Yes | Options: Energy cost reduction, ESG reporting, Pump efficiency, Motor rightsizing, General energy assessment |
| Number of motors/assets | Dropdown | No | Same options as demo form |

**Post-submission behaviour:**

| Step | Detail |
|------|--------|
| **Confirmation screen** | "Thanks, [First name]. We'll send you relevant impact data within 2 business days." |
| **Confirmation email** | Immediate. Subject: "Samotics energy impact data." Body: links to Vitens case study and Yorkshire Water energy data. Sets expectation for a follow-up with site-specific impact estimate. |
| **Internal routing** | Lead to CRM. Tagged as "Energy/ESG." Routed to AE with energy expertise. |
| **SLA** | Sales responds within 2 business days with relevant energy impact data. |
| **Tracking** | `gtm_event: energy_inquiry`, tagged with primary interest and industry. |

---

## Page-by-Page CTA Map

Every page, every CTA. Primary CTAs are the main conversion action. Secondary CTAs are supporting actions that serve a different persona or a lower-commitment step.

### Homepage

| Position | CTA | Copy | Type |
|----------|-----|------|------|
| Hero | Primary | Request a Demo | Button (accent) |
| Below problem statement | Secondary | Start Your Asset Audit | Button (outline) |
| Social proof section | Tertiary | See Customer Results | Text link → `/proof` |

### Problem Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/problem` | Hero | Primary | Start Your Asset Audit | Button (accent) |
| `/problem` | Bottom | Secondary | Request a Demo | Button (outline) |
| `/problem` | Inline | Tertiary | See how ESA works → | Text link → `/technology/esa` |
| `/problem/proximity-penalty` | Bottom | Primary | Start Your Asset Audit | Button (accent) |
| `/problem/proximity-penalty` | Bottom | Secondary | Request a Demo | Button (outline) |

### Technology Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/technology/esa` | Bottom | Primary | Request a Demo | Button (accent) |
| `/technology/esa` | Inline | Secondary | See customer results → | Text link → `/proof` |
| `/technology/how-it-works` | Bottom | Primary | See the SAM4 Platform | Button (accent) → `/platform/sam4` |
| `/technology/how-it-works` | Bottom | Secondary | Request a Demo | Button (outline) |
| `/technology/esa-vs-vibration` | Bottom | Primary | Request a Demo | Button (accent) |
| `/technology/esa-vs-vibration` | Inline | Secondary | See detection results → | Text link → `/proof` |

### Platform Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/platform/sam4` | Bottom | Primary | Request a Demo | Button (accent) |
| `/platform/sam4` | Bottom | Secondary | Talk to Us | Button (outline) |
| `/platform/how-it-installs` | Bottom | Primary | Request a Demo | Button (accent) |
| `/platform/how-it-installs` | Inline | Secondary | See deployment results → | Text link → `/proof` |
| `/platform/security` | Inline | Primary | Request Security Docs | Button (accent) + inline form |
| `/platform/security` | Bottom | Secondary | Talk to Us | Button (outline) |
| `/platform/integrations` | Bottom | Primary | Talk to Us | Button (accent) |
| `/platform/integrations` | Sidebar | Secondary | Need security docs? | Text link → `/platform/security` form |

### Industry Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| All `/industries/[x]` | Hero | Primary | Request a Demo | Button (accent) |
| All `/industries/[x]` | Proof section | Secondary | See [Industry] Results → | Text link → `/proof` (filtered) |
| All `/industries/[x]` | Bottom | Tertiary | Start Your Asset Audit | Button (outline) |

### Proof Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/proof` hub | Footer | Primary | Request a Demo | Button (accent) |
| `/proof` hub | Footer | Secondary | Start Your Asset Audit | Button (outline) |
| `/proof/[case]` | Top + Bottom | Primary | Download PDF | Button (accent) |
| `/proof/[case]` | Bottom | Secondary | Request a Demo | Button (outline) |

### About Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/about` | Hero | Primary | Talk to Us | Button (accent) |
| `/about` | Bottom | Secondary | See Customer Results → | Text link → `/proof` |
| `/about/abb` | Bottom | Primary | Talk to Us | Button (accent) |
| `/about/abb` | Bottom | Secondary | Discuss Partnership | Text link → `/contact` (Phase 2: → `/contact/partner-inquiry`) |

### Contact Pages

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/contact` | Hero | Primary | Submit form (dynamic based on intent) | Form submit button |
| `/contact/asset-audit` | Hero | Primary | Request Your Asset Audit | Form submit button |

### Section Hub Pages

Hub pages route visitors to children. In v1, most of these are not standalone pages (nav dropdowns link to children directly). If built as landing pages, apply these CTAs.

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| `/technology` (if built) | Bottom | Primary | Request a Demo | Button (accent) |
| `/platform` (if built) | Bottom | Primary | Request a Demo | Button (accent) |
| `/industries` (if built) | Bottom | Primary | Request a Demo | Button (accent) |
| `/resources` | Bottom | Primary | Request a Demo | Button (accent) |
| `/partners` (Phase 2) | Hero | Primary | Discuss Partnership | Button (accent) |
| `/partners` (Phase 2) | Bottom | Secondary | Talk to Us | Button (outline) |

### Resources

| Page | Position | CTA | Copy | Type |
|------|----------|-----|------|------|
| Blog posts | Bottom | Primary | Request a Demo | Button (accent) |
| Blog posts | Sidebar | Secondary | Download related content | Contextual |
| Webinar pages | Hero | Primary | Watch Now / Register | Button (accent) |
| Download pages | Inline | Primary | Download | Button per asset |

---

## Contact Page: Intent Router

The main `/contact` page uses an intent selector to route visitors to the right form. In v1, this is a single page with conditional form fields. Phase 2 breaks these into separate landing pages.

### Intent Selector

Displayed prominently at the top of the `/contact` page. Visitor selects their intent, and the form fields adjust.

| Intent Option | Maps to CTA | Form Fields Shown |
|--------------|-------------|-------------------|
| I'd like a demo | Request a Demo | Demo form fields (see §1 above) |
| I want an asset audit | Start Your Asset Audit | Asset audit form fields (see §2 above) |
| I'd like to speak with your team | Talk to Us | Executive form fields (see §3 above) |
| I need security documentation | Request Security Docs | Redirects to `/platform/security` inline form |
| I'm interested in a partnership | Discuss Partnership | v1: simplified partner fields (name, email, company, company type, message). Phase 2: redirects to `/contact/partner-inquiry`. |

### Fallback

If a visitor arrives at `/contact` without a `?intent=` parameter, the intent selector is shown by default. No form fields are visible until an intent is selected. This prevents the "wall of fields" problem and forces self-qualification.

---

## CTA Design Rules

| Rule | Specification |
|------|--------------|
| **One primary CTA per viewport** | Never show two accent-coloured buttons in the same visible area. One primary (filled), one secondary (outline or text link). |
| **Button hierarchy** | Primary: filled accent button. Secondary: outline button. Tertiary: text link with arrow (→). |
| **Copy length** | Maximum 4 words on a button. "Request a Demo" (3). "Start Your Asset Audit" (4). |
| **No generic CTAs** | Never use "Learn More", "Get Started", "Submit", or "Click Here" as standalone buttons. Every CTA must state what happens next. |
| **Verb-first** | Every button starts with a verb: Request, Start, Download, Talk, Discuss, See. |
| **Consistent placement** | Primary CTA appears in hero AND bottom of every page. Visitors who scroll to the bottom have earned a CTA — don't make them scroll back up. |
| **Mobile sizing** | Buttons are full-width on mobile (< 768px). Minimum height: 48px. Minimum font size: 16px. |
| **Loading state** | On form submission, button shows a spinner and becomes disabled. Copy changes to "Sending..." to prevent double-submission. |
| **Error state** | If form submission fails, show an inline error message above the submit button. Do not clear form fields on error. |

---

## Form Validation Rules

| Rule | Specification |
|------|--------------|
| **Email validation** | Must contain @ and a valid domain. Soft warning on free email providers (gmail.com, hotmail.com, yahoo.com, outlook.com) — show "Company email preferred" but allow submission. Exception: no warning on security docs form. |
| **Required fields** | Marked with asterisk (*). Inline validation on blur — don't wait for submission to show errors. |
| **Error messages** | Specific, not generic. "Please enter your work email" not "Invalid input." |
| **Field order** | Name → Email → Company → Job title → Intent-specific fields → Free text (always last). |
| **Autofill** | Support browser autofill on all standard fields (name, email, company). Use correct `autocomplete` attributes. |
| **Progressive disclosure** | On the contact page, show only the intent selector first. Reveal form fields after intent selection. Reduces perceived form length. |
| **GDPR consent** | Checkbox below submit button: "I agree to receive communications from Samotics. View our [Privacy Policy](/privacy)." Required for submission. Not pre-checked. |
| **Spam prevention** | Honeypot field (hidden). No visible CAPTCHA unless bot traffic exceeds threshold. |

---

## Tracking and Attribution

Every form submission fires a GTM event with the following data layer:

| Variable | Value |
|----------|-------|
| `event` | `form_submission` |
| `form_type` | `demo_request` / `asset_audit` / `executive_inquiry` / `security_docs` / `case_study_download` / `partner_inquiry` / `energy_inquiry` |
| `source_page` | URL of the page where the CTA was clicked |
| `intent` | Intent value from the contact router (if applicable) |
| `industry` | Selected industry (if captured) |
| `fleet_size` | Selected asset count (if captured) |
| `utm_source` | From URL parameter |
| `utm_medium` | From URL parameter |
| `utm_campaign` | From URL parameter |

Additionally, every CTA button click (not just form submissions) fires a `cta_click` event with button copy and source page. This captures intent even when visitors don't complete the form.

---

## Phase Roadmap

| Phase | Changes |
|-------|---------|
| **v1** | Five CTAs live. Contact page uses intent router (single page). Case study PDFs ungated. Security docs gated. |
| **Phase 2** | Add "Discuss Partnership" as standalone form at `/contact/partner-inquiry`. Consider light gate on case study PDFs (email only). Break contact page intent router into separate landing pages if conversion data supports it. |
| **Phase 3** | Add "See Impact Data" CTA on energy content pages. Add coverage calculator tool with its own CTA ("Calculate Your Coverage Gap"). Evaluate A/B tests on form length and gating strategy. |

---

## Open Questions for Review

1. ~~**Case study gating.**~~ **Decided: Ungated.** Direct PDF download, no form. Revisit in Phase 2 if lead capture data demands it.
2. ~~**Free email blocking.**~~ **Decided: Soft warning.** Show "Company email preferred" but allow submission. No hard block.
3. **Post-submission nurture sequences.** This document covers immediate post-submission behaviour. The full nurture cadence (follow-up emails at day 3, 7, 14) needs a separate marketing automation spec.
4. **Chatbot/live chat.** Not specified here. If a chatbot is planned, it needs its own CTA logic and should not compete with form-based CTAs on the same page.
