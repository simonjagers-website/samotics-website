# SAMOTICS — User Journey Map (Version 3.1)

**Persona and Buying Motion Flow Logic — Samotics Website & Content Strategy**

Owner: Marketing
Version: 3.1
Date: March 2026
Dependencies: Buyer Journey Framework v3.1, ICP & Buying Committee Map v3.1

---

## What Changed and Why

**Changes (v3.0 → v3.1):**

1. **Canonical Buying Motions enforced.** Removed all synonym drift. "Strategic Approval" → "Strategic & Financial Approval." "Validation (SAM4-X pilot)" → "Technical Validation." "Consensus Creation" → "Internal Alignment." All labels now match the Buying Motions Canon (Buyer Journey Framework, Section 0.0).

2. **Added three missing persona journeys.** Procurement Gatekeeper, Corporate Reliability, and Practitioner now have standalone journey maps. Even though these personas rarely self-serve on the website, they receive forwarded links and PDFs. Their content needs must be explicitly mapped.

3. **Added CTA → System Response mapping.** Each CTA now defines what happens after the click: form fields, automated response, internal routing, handoff SLA, and qualification gate. This turns the CTA framework from a sitemap into an operating system.

4. **Added Gating Doctrine.** Defined what content is ungated, gated, interactive, and shareable/printable. Removes ambiguity about what requires a form fill.

**Prior v3.0 changes (retained):**

- Non-linear buying motion model replacing linear funnel
- Champion enablement as dedicated content function
- Security and deployment confidence moved earlier
- Persona-aligned CTAs replacing generic "Request a Demo"
- Scenario entry mapping for all 8 buying scenarios
- Post-sale promise-to-delivery connection

---

## Canonical References

> **Buying Motions, SAM4-X positioning, Proof System, and Measurement Definitions are governed by the Buyer Journey Framework v3.1.** This document references but does not redefine them.

- **Buying Motions Canon:** See Buyer Journey Framework, Section 0.0
- **SAM4-X Canonical Positioning:** See Buyer Journey Framework, Section 0.1
- **Proof System:** See Buyer Journey Framework, Appendix A
- **Measurement Definitions:** See Buyer Journey Framework, Section 2.1

---

## 1.0 Buying Motion Model

The modern industrial buying process is not a funnel. It is a loop of independent research, internal deliberation, and external validation. Personas move between motions non-linearly. They revisit, skip, and run motions in parallel.

The journey map is organised around six canonical buying motions:

| Motion | Key Question | Content Function | Primary Content Assets |
|:---|:---|:---|:---|
| **1. Problem Recognition** | "Is this problem urgent and expensive enough to solve now?" | Cost-of-inaction validation | ROI calculator, industry downtime benchmarks, case studies with quantified impact |
| **2. Solution Exploration** | "What are the credible ways to solve this?" | Method validation | ESA technology explainer, Complementary Detection Matrix, ESA-vs-vibration comparison, expert guides |
| **3. Internal Alignment** | "How do I get my colleagues to agree this is the right approach?" | Internal selling | Champion Enablement Kit: 1-page ROI summary, short technical explainer, engineering FAQ, internal presentation deck |
| **4. Technical Validation** | "Will this actually work on our specific assets and in our workflow?" | Risk reduction | Detection matrix by asset class, diagnostic example pack, architecture diagram, install guide, security documentation |
| **5. Strategic & Financial Approval** | "Does this align with our strategy and is the business case solid?" | Strategic approval | Executive briefing, enterprise-grade proof, ABB partnership validation, TEI report, ISO 55000 alignment |
| **6. Deployment Confidence** | "How can we be sure this will not be a painful implementation?" | Deployment confidence | Implementation playbook, customer success stories, support SLAs, after-alert playbook, CMMS integration guide |

---

## 2.0 Persona Journey Maps

### 2.1 Champion (Reliability Manager)

**Role in deal:** Technical evaluator + internal champion. Builds the business case. Sells internally.

**Core question:** "Does this solve a problem I cannot solve now, and can I prove its value?"

**Likely entry points:**
- Google search for failure mode, monitoring gap, or competitor comparison
- Industry magazine article or conference
- Peer recommendation
- ABB referral

**Time on site:** 15–25 minutes across multiple visits.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Problem Recognition | Confirm the problem is worth solving. Seek external validation of the cost of inaction. | Industry benchmarks, ROI calculator, case studies with financial outcomes | /industries/[x]/, ROI calculator tool |
| Solution Exploration | Evaluate ESA as a credible approach. Compare to alternatives. Assess boundaries. | ESA technology explainer, Complementary Detection Matrix, ESA-vs-vibration comparison | /technology/esa/, /technology/esa-vs-vibration/ |
| Internal Alignment | Share findings with colleagues. Build initial internal case. | Champion Enablement Kit: 1-page summary, internal deck, ROI calculator output | Gated download (Champion Kit) |
| Technical Validation | **Delegates to Technical Validator.** Reviews their findings. Assesses diagnostic depth. | Detection matrix, case studies with timeline and diagnostic reasoning | /proof/[case]/, /technology/how-it-works/ |
| Strategic & Financial Approval | Presents business case to Economic Buyer (Enterprise). Addresses CFO and Procurement concerns. | Business case template, TEI report, vendor compliance docs | Gated Business Case Toolkit |
| Deployment Confidence | Confirms implementation will not disrupt operations. | Install guide, deployment timeline, customer success stories | /platform/how-it-installs/, /proof/ (deployment-focused) |

**Delegation moment:** Technical Validation is handed to the Technical Validator (Reliability Engineer, Maintenance Engineer). The Champion reviews results and decides whether to proceed to Strategic & Financial Approval.

**Primary CTA:** Calculate Your ROI (entry) → Build My Business Case (mid-journey) → Start Your Asset Audit (conversion)

---

### 2.2 Technical Validator — Reliability Engineer

**Role in deal:** Delegated technical gate. Evaluates detection capability, data quality, and diagnostic value. Their endorsement determines whether the solution advances.

**Core question:** "Show me detection logic, accuracy limits, and diagnostic depth for my asset types."

**Likely entry points:**
- Internal share from Champion (deep link to technology or case study page)
- Engineering article or technical blog post

**Time on site:** 15–30 minutes. Deep, focused sessions.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Technical Validation | Evaluate detection capability by asset class and failure mode. Assess accuracy and limits. | Detection matrix, diagnostic example pack (alert → reasoning → outcome), accuracy data, Measurement Definition Box | /technology/how-it-works/, /technology/esa/ |
| Solution Exploration | Understand where ESA applies and where it does not. Honest boundary conditions. | ESA-vs-vibration comparison, failure mode coverage by asset class, applicability constraints | /technology/esa-vs-vibration/ |
| Technical Validation | Review real detection examples with timeline and diagnostic reasoning. | Case studies with engineering detail (not marketing summaries) | /proof/[case]/ |
| Deployment Confidence | Assess workflow integration. How alerts appear, what to do, false positive handling. | Platform walkthrough, alert logic, analyst model, CMMS integration | /platform/sam4/, /platform/integrations/ |

**Required assets (high priority):**
- Engineering FAQ (addressing false positives, accuracy envelope, data requirements, VFD limitations)
- Detection matrix by failure mode and asset class (with constraints column)
- Diagnostic example pack (3–5 detailed alert-to-outcome stories)
- Architecture diagram (data flow, security, integration points)

**Primary CTA:** Get the Engineering Proof Pack → Schedule a Technical Deep-Dive

---

### 2.3 Technical Validator — Maintenance Engineer

**Role in deal:** Implementer + first-line responder. Validates that the system is practical to install and operate daily.

**Core question:** "How do we install this and what does my day look like with it?"

**Likely entry points:**
- Internal share from Champion or Reliability Engineer (direct link to install page)

**Time on site:** 10–20 minutes. Practical, action-oriented.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Deployment Confidence | Assess installation reality: tools, time, safety, production impact. | Install guide (<30 min install, MCC-based, zero downtime) | /platform/how-it-installs/ |
| Technical Validation | Evaluate daily workflow: what an alert looks like, what to do, escalation path. | Alert examples, after-alert playbook, roles and handoffs | /platform/sam4/ |
| Deployment Confidence | Confirm CMMS integration: how alerts flow into existing work orders. | CMMS integration documentation | /platform/integrations/ |
| Technical Validation | See real examples of alert → action → avoided failure. | Case studies focused on operational workflow, not financial outcomes | /proof/ |

**Required assets (high priority):**
- 1-page install sheet (tools, time, safety, zero-downtime proof)
- After-alert playbook (what happens when an alert fires)
- Roles and handoffs document (who does what)

**Primary CTA:** Schedule Install Guidance → Request a Technical Deep-Dive

---

### 2.4 Economic Buyer — Operations Director / Plant Manager

**Role in deal:** Budget holder for plant-level pilot. Approves based on risk, production impact, and ROI.

**Core question:** "What is the financial impact and how fast?"

**Likely entry points:**
- Internal share from Champion (typically a case study or ROI summary)
- Rarely self-educates via search

**Time on site:** 5–10 minutes. Scans for financial proof, then delegates.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Problem Recognition | Validate the financial magnitude of the problem. | Financial outcomes: avoided downtime cost, ROI figures, fleet-scale impact | /proof/, /industries/[x]/ |
| Strategic & Financial Approval | Assess vendor credibility and deployment speed. | Case study (fleet size + financial impact), company credibility (funding, ABB, customer scale) | /about/, /proof/[case]/ |
| Deployment Confidence | Confirm non-disruptive deployment. | Deployment timeline, installation summary | /platform/how-it-installs/ |
| Internal Alignment | Share ROI case internally (upward to Enterprise Economic Buyer). | ROI PDF, business case summary | Downloadable ROI summary |

**Primary CTA:** Start Your Asset Audit → Book an Executive Briefing (for enterprise discussions)

---

### 2.5 Economic Buyer (Enterprise) / Strategic Sponsor — CTO / VP Engineering

**Role in deal:** Strategic sponsor for enterprise-wide deployment. Approves scaling based on strategic fit and enterprise ROI.

**Core question:** "Is this scalable, enterprise-safe, and aligned with our corporate strategy?"

**Likely entry points:**
- Internal share from Champion or Operations Director
- ABB referral
- Executive peer network

**Time on site:** 5–10 minutes. High-level assessment only.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Strategic & Financial Approval | Validate vendor credibility and strategic vision. | Company story (funding, partnerships, customer scale), ABB relationship | /about/, /partners/abb/ |
| Strategic & Financial Approval | Assess platform strategy and enterprise readiness. | Platform overview, scalability proof, multi-site deployment model | /platform/sam4/ |
| Strategic & Financial Approval | Review enterprise proof: large-scale deployments with quantified outcomes. | Enterprise-scale case studies | /proof/ |
| Technical Validation (delegated) | Ensure security and compliance. | Security overview (delegates to IT/OT for detail) | /platform/security/ |

**Primary CTA:** Book an Executive Briefing

---

### 2.6 IT/OT Gatekeeper — CISO / Dir. of IT

**Role in deal:** Security and architecture gatekeeper. Can veto at any stage.

**Core question:** "Is it secure, does it integrate, and will it introduce risk?"

**Likely entry points:**
- Internal share from Champion (typically a direct link to security page)
- Forwarded security question from procurement process

**Time on site:** 10–15 minutes. Focused on security and architecture.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Technical Validation | Assess security posture: data handling, encryption, certifications. | Trust & Security Centre: certifications, data handling policies, penetration test summaries | /platform/security/ |
| Technical Validation | Evaluate integration: APIs, CMMS connectivity, data lake compatibility. | API documentation, integration guides, architecture diagrams | /platform/integrations/ |
| Technical Validation | Understand data flow and architecture. | End-to-end architecture diagram (from sensor to dashboard) | /technology/how-it-works/ |
| Strategic & Financial Approval | Validate enterprise readiness. | Enterprise deployment references, compliance documentation | /proof/ |

**Required assets (critical — IT veto is a primary deal-killer):**
- Trust & Security Centre (public page, not gated): certifications, SOC 2, data handling, architecture
- API documentation
- Integration guides for major CMMS platforms (SAP PM, Maximo, Infor EAM)

**Primary CTA:** Request a Security Review → Request Security Documentation

---

### 2.7 Procurement Gatekeeper

**Role in deal:** Commercial and vendor risk gatekeeper. Manages MSA negotiation, TCO analysis, and vendor compliance. Heavily involved in Fleet Programs; minimal in SAM4-X (often below tender threshold).

**Core question:** "Is this a responsible use of capital, and does this vendor meet our requirements?"

**Likely entry points:**
- Internal share from Champion or Economic Buyer (typically vendor compliance docs or pricing summary)
- Procurement process triggers (RFP, vendor onboarding)

**Time on site:** 5–10 minutes. Focused on compliance and commercial terms.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Strategic & Financial Approval | Evaluate vendor risk, financial stability, and compliance with procurement standards. | Vendor compliance pack, ABB partnership validation, financial stability indicators | /about/, /partners/abb/ |
| Strategic & Financial Approval | Compare TCO against alternatives. Review contract terms. | TCO comparison, standardised MSA, pricing structure summary | Direct from AE (not on public website) |
| Technical Validation | Confirm security and data handling meet corporate policies. | Trust & Security Centre (certifications, data handling, compliance) | /platform/security/ |

**Required assets:**
- Standardised MSA (pre-approved, fair terms)
- TCO comparison document
- Vendor compliance checklist (pre-filled)
- ABB partnership summary (for vendor risk assessment)

**Primary CTA:** None on website (Procurement typically receives materials from Champion or AE). Ensure all compliance materials are easily shareable as PDFs.

---

### 2.8 Corporate Reliability / Asset Management

**Role in deal:** Standards and governance gatekeeper. Sets cross-site deployment standards. Approves technologies for the corporate-approved vendor list. Critical for Fleet Programs.

**Core question:** "How does this fit our corporate asset management strategy and ISO 55000 framework?"

**Likely entry points:**
- Internal share from Champion or Economic Buyer (Enterprise)
- Conference or industry working group
- Peer network recommendation

**Time on site:** 5–15 minutes. Focused on standards alignment and multi-site proof.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Strategic & Financial Approval | Assess alignment with corporate asset management strategy and ISO 55000. | ISO 55000 alignment brief, standards compliance documentation | /about/, /technology/esa/ |
| Strategic & Financial Approval | Review multi-site deployment results for consistency and repeatability. | Multi-site results summary, deployment playbook | /proof/ |
| Solution Exploration | Understand where ESA fits in a layered detection strategy. | Complementary Detection Matrix, ESA-vs-vibration comparison | /technology/esa-vs-vibration/ |
| Deployment Confidence | Evaluate governance model for enterprise rollout. | Enterprise deployment playbook, corporate rollout model | /platform/sam4/ |

**Required assets:**
- ISO 55000 alignment brief (how SAM4 fits asset management frameworks)
- Multi-site results summary (aggregated proof across deployments)
- Enterprise deployment playbook (governance, phasing, standards)

**Primary CTA:** Book an Executive Briefing (typically initiated by Champion or Enterprise Economic Buyer on their behalf)

---

### 2.9 Practitioner (Maintenance Technician / Operator)

**Role in deal:** End user and adoption validator. Their resistance or endorsement during a pilot directly impacts expansion decisions. Rarely involved in the buying decision but critical for deployment success.

**Core question:** "Will this make my job easier or harder? Can I trust the alerts? Will this create extra work?"

**Likely entry points:**
- Internal communication from Champion or supervisor during pilot
- Rarely visits the website independently

**Time on site:** 5–10 minutes (if at all). Extremely practical focus.

**Buying motion flow:**

| Motion | What they do | Content they need | Website destination (directional) |
|:---|:---|:---|:---|
| Technical Validation | Evaluate alert quality during pilot: are alerts actionable? Are there too many false positives? | Alert examples (real screenshots), after-alert playbook (what to do step-by-step) | /platform/sam4/ |
| Deployment Confidence | Assess installation impact: will this disrupt their work? What changes in their daily routine? | 1-page install sheet, roles-and-handoffs document | /platform/how-it-installs/ |
| Deployment Confidence | Confirm CMMS integration: do alerts appear in their existing work order system? | CMMS integration screenshots, workflow examples | /platform/integrations/ |

**Required assets (high priority for adoption):**
- 1-page install sheet (tools, time, safety, zero-downtime proof)
- After-alert playbook (step-by-step: alert fires → what to do → who to escalate to)
- Roles-and-handoffs document (who does what — Samotics vs. customer)
- Real alert screenshots (not mockups — Practitioners spot fake UIs immediately)

**Primary CTA:** None on website (Practitioners are engaged during the pilot, not through marketing). Ensure all practitioner materials are easily printable and available as PDFs.

---

## 3.0 Scenario Entry Mapping

Each buying scenario from the Buyer Journey Framework v3.1 maps to specific entry channels and initial content needs.

| Scenario | Primary Entry Channel | Initial Content Need | First Page Destination |
|:---|:---|:---|:---|
| S1: Critical Asset Failure | Google search, peer referral, internal incident review | "What did our monitoring miss? What can detect this?" | /technology/esa/ or /industries/[x]/ |
| S2: Detection Completion | Internal RCM/FMEA review, conference, technical article | "Which failure modes are we blind to?" | /technology/esa-vs-vibration/, Detection Matrix |
| S3: Coverage Gap | Audit, conference, ABB referral, internal gap analysis | "How do we monitor assets we cannot reach?" | /technology/how-it-works/, /industries/[x]/ |
| S4: Energy & Efficiency Mandate | ESG programme review, energy audit | "How do we reduce motor fleet energy consumption?" | /industries/[x]/ (energy angle), ROI calculator |
| S5: Partner-Led | ABB referral, system integrator recommendation | "Our partner says this fills a gap. Validate." | /about/, /partners/abb/, /proof/ |
| S6: Regulatory & Insurance | Regulatory review, insurance mandate, compliance audit | "What monitoring meets this new requirement?" | /industries/[x]/ (compliance angle), /platform/security/ |
| S7: Technology Refresh | Maintenance strategy review, vendor end-of-life notice | "What replaces or complements our aging system?" | /technology/esa-vs-vibration/, /platform/integrations/ |
| S8: M&A Due Diligence | Acquisition team review, corporate reliability assessment | "What is the asset health risk in this facility?" | /proof/, /platform/how-it-installs/ |

---

## 4.0 Cross-Journey Content Architecture

### 4.1 Technical Resource Layer

A deep-content layer for engineers that does not pollute executive-facing pages:

- Jump-linked deep dives from summary pages
- Downloadable proof packs (detection matrix + diagnostic examples + architecture diagram)
- Install sheets and after-alert playbooks
- Engineering FAQ

**Design principle:** Every technical page has two layers. Layer 1 is the summary (for Champions and Economic Buyers). Layer 2 is the deep dive (for Technical Validators). Navigation between layers is seamless.

### 4.2 Internal Selling Layer

Content explicitly designed to be shared internally by the Champion:

- Champion Enablement Kit (gated): internal presentation deck, pre-built business case, ROI calculator, competitive positioning, security FAQ
- Business Case Toolkit (gated, late-stage): ROI template, executive summary, deployment timeline
- 1-page ROI summary (downloadable, shareable)
- Diagnostic example pack (shareable evidence for engineers)

**Design principle:** Every shareable asset must look professional when forwarded. No marketing fluff. Data-dense. Branded but not salesy.

### 4.3 Security-First Design

Security information is surfaced early, not hidden behind late-stage forms:

- Trust & Security Centre: public, ungated, prominent in navigation
- Security summary visible on technology and platform pages
- Architecture diagram accessible from multiple entry points
- Certifications and compliance badges on key landing pages

### 4.4 Gating Doctrine

What requires a form fill and what does not. Overgating kills trust; undergating loses lead data. This doctrine balances both.

**Ungated (no form required):**
- Trust & Security Centre (full contents)
- Complementary Detection Matrix (summary version)
- 1 flagship case study per vertical (at Green proof readiness)
- Install summary (1-page overview)
- ESA technology explainer
- ESA-vs-vibration comparison
- ROI calculator (interactive, self-service — captures email only if user wants to save results)

**Gated (form required — name, email, company, role):**
- Champion Enablement Kit
- Business Case Toolkit
- Technical Proof Pack (full detection matrix + diagnostic examples + architecture)
- Executive Proof Pack
- Security Proof Pack (detailed — beyond what's on the public Trust & Security Centre)

**Printable / Shareable (designed for internal forwarding):**
- All gated content must be downloadable as PDF
- 1-page ROI summary (designed for email forwarding)
- Diagnostic example pack (designed for engineer-to-engineer sharing)
- Install sheet and after-alert playbook (designed for practitioner distribution)

---

## 5.0 CTA Intent Routing

Replace the single "Request a Demo" with persona-aligned, value-first offers mapped to canonical buying motions.

### 5.1 CTA Definitions

| CTA | Target Persona | Buying Motion | Friction Level |
|:---|:---|:---|:---|
| **Calculate Your ROI** | Champion, Economic Buyer (Plant) | Problem Recognition | Low (self-service, instant value) |
| **Get the Engineering Proof Pack** | Technical Validator (Reliability Engineer) | Technical Validation | Low (gated download) |
| **Schedule a Technical Deep-Dive** | Technical Validator (both) | Technical Validation | Medium (requires scheduling) |
| **Request a Security Review** | IT/OT Gatekeeper | Technical Validation | Medium (initiates security conversation) |
| **Book an Executive Briefing** | Economic Buyer (Enterprise), CTO | Strategic & Financial Approval | Medium (requires executive commitment) |
| **Start Your Asset Audit** | Champion, Economic Buyer (Plant) | Technical Validation | High (conversion to SAM4-X) |
| **Build My Business Case** | Champion | Internal Alignment | Medium (gated toolkit) |

**Routing logic:** CTAs are placed contextually on pages aligned to their buying motion. The /contact/ page offers all options with clear descriptions of what each delivers.

### 5.2 CTA → System Response Mapping

What happens after a CTA click. This defines the handoff from marketing to sales.

| CTA | Form Fields (minimum) | Automated Response | Internal Routing | Handoff SLA | Qualification Gate |
|:---|:---|:---|:---|:---|:---|
| **Calculate Your ROI** | Email (optional — only to save results) | Instant results on screen. If email provided: PDF summary + "Want to discuss your results?" email at +24hrs | If email captured from Tier 1/2 account → AE notification | 24hrs (if Tier 1/2) | Account matches ICP Tier 1 or 2 |
| **Get the Engineering Proof Pack** | Name, email, company, role | Instant download link + confirmation email with related technical content links | Lead routed to SDR for qualification. If Tier 1 account → AE notification | 4hrs (business hours) | Role matches Technical Validator; company matches ICP |
| **Schedule a Technical Deep-Dive** | Name, email, company, role, preferred time | Calendar booking link (Solutions Engineer) + confirmation with prep materials | SE assigned. AE notified. If no existing opp → SDR qualifies first | 24hrs to confirm session | Qualified lead (existing opp or SDR-confirmed) |
| **Request a Security Review** | Name, email, company, role | Acknowledgment email + Trust & Security Centre link | Routed to SE (security track). AE notified. | 24hrs to first response | Company matches ICP; role is IT/OT |
| **Book an Executive Briefing** | Name, email, company, title | Acknowledgment email + briefing prep form | Routed to AE (or Sales Director for Tier 1). SE prepares briefing. | 48hrs to confirm session | Exec-level title; company matches ICP Tier 1 or 2 |
| **Start Your Asset Audit** | Name, email, company, role, asset type, number of assets | Acknowledgment email + "What to expect" PDF | Routed to AE as high-intent lead. CS looped in for scoping. | 4hrs (business hours) | High intent. AE qualifies: budget, timeline, champion identified |
| **Build My Business Case** | Name, email, company, role | Instant access to Business Case Toolkit + confirmation email | Lead routed to AE. If existing opp → AE follows up. If new → SDR qualifies. | 24hrs | Existing qualified opportunity or Tier 1/2 account |

---

## 6.0 Journey Gaps & Content Priorities

| Gap | Risk | Priority | Action |
|:---|:---|:---|:---|
| No Champion Enablement Kit | Deals stall at Internal Alignment. Champion cannot sell internally. | **Critical** | Build Kit: internal deck, business case template, ROI calculator, security FAQ, competitive positioning. |
| No Trust & Security Centre | IT veto kills deal before Champion even knows. | **Critical** | Build public page: certifications, architecture, data handling, compliance. |
| No engineering-grade technical depth (with honest boundaries) | Technical Validators cannot validate. Champion loses credibility. | **Critical** | Build: detection matrix with constraints column, diagnostic example packs, engineering FAQ (including VFD limitations), architecture diagram. |
| No install playbook | Adoption friction. Practitioners resist unfamiliar tools. | **High** | Build: 1-page install sheet, after-alert playbook, roles-and-handoffs document. |
| No downloadable proof packs | Internal deal stalls. Committee members cannot evaluate offline. | **High** | Create downloadable bundles by persona: Technical Pack, Executive Pack, Security Pack. (See Proof System, Appendix A in Buyer Journey Framework.) |
| No ROI calculator | Champions build ad hoc cases. Inconsistent, less credible. | **High** | Build interactive calculator: inputs = downtime cost, asset count, failure frequency. |
| No flagship case studies for O&G, Chemicals, Mining | Industry pages lack proof. Credibility gap in key verticals. | **High** | Prioritise case study development for Red proof-readiness industries (see ICP doc, Section 6). |
| No third-party ROI validation | Financial Approvers and Procurement lack external credibility. | **Medium** | Commission Forrester TEI or equivalent independent study. |
| No deployment-focused customer stories | Deployment confidence gap vs. competitors (Augury, Siemens). | **Medium** | Produce customer interviews focused on implementation experience, team adoption, and long-term success. |
| No PdM Champion content series | No thought leadership positioning for primary buyer persona. | **Medium** | Develop content series (blog, webinar) for reliability leaders navigating PdM adoption and scaling. |
| No Procurement / Corporate Reliability content | These personas receive forwarded links but find nothing designed for them. | **Medium** | Build: vendor compliance checklist, ISO 55000 alignment brief, TCO comparison template. |

---

## 7.0 Connection to Post-Sale User Journey

The User Journey Map does not end at conversion. The promises made during the buying journey must connect to the operational reality after the deal closes.

| Buying Journey Promise | Post-Sale Delivery | Owner |
|:---|:---|:---|
| "First insights within 30 days" (Phase 1: Operational Baseline) | Installation validation, load profiling, energy baseline delivered in SAM4 dashboard | Customer Success |
| "Actionable anomaly detection in 30–90 days" (Phase 2) | Validated alerts delivered to CMMS. Regular review cadence with customer. | Diagnostics Engineering + Customer Success |
| "Quantifiable ROI in 90+ days" (Phase 3) | Tracked catches with documented financial impact. Formal ROI review at 90-day mark. | Customer Success + Champion |
| "Only validated findings — no false positive noise" | All alerts reviewed by Samotics diagnostics engineers before delivery. TP/FP rates tracked per engagement. | Diagnostics Engineering |
| "Sub-30-minute MCC installation, zero production impact" | Dedicated installation support. Installation validation confirmation. | Field Engineering |
| "Seamless CMMS integration" | Functional work order integration within first 30 days | IT/OT Integration Team |
| "Repeatable deployment playbook for scale" | Documented playbook delivered at pilot completion. Multi-site review meeting. | Customer Success + Champion |

**Design principle:** Every claim made on the website or in sales materials must have a corresponding delivery mechanism post-sale. Broken promises during the buying journey become churn drivers in the user journey.

---

*End of document.*
