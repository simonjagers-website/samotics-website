# Page Brief — Base

Purpose, target audience, primary action, traffic source, and key message for every page on samotics.com

**Document:** Page Brief — Base
**Layer:** Content
**Owner:** Marketing
**Status:** Draft
**Date:** February 2026
**Dependencies:** Site Architecture, Navigation Spec, CTA Strategy, #12 User Journey Map, #3 Buying Scenario Framework, Messaging Framework
**Feeds Into:** Copywriting briefs, Design wireframes, CMS build

---

## How to Use This Document

This is the content foundation for every page on the site. Each entry answers five questions: why does this page exist, who is it for, what should the visitor do next, how do they get here, and what is the one thing they must believe after reading it.

Copywriters use this to draft page content. Designers use it to prioritise content hierarchy. Developers use it to validate that every page has a defined purpose before building templates.

Every page traces back to at least one persona journey or buying scenario. There are no orphan pages.

---

## Page Briefs

---

### Homepage

| | |
|---|---|
| **URL** | `/` |
| **Phase** | v1 |
| **Purpose** | Route visitors to the right path based on their problem, industry, or role. Establish Samotics as the company that monitors what sensors can't reach. The homepage is a router, not a brochure. |
| **Target audience** | All personas. Weighted toward Reliability Manager (S1) and Operations Director (S2) — these drive the majority of inbound traffic. |
| **Primary action** | Request a Demo (hero). Secondary: Start Your Asset Audit (below problem statement). |
| **Traffic sources** | Brand search ("Samotics", "SAM4"), LinkedIn content clicks, direct navigation, ABB/partner referrals, internal links from email campaigns. |
| **Key message** | Every AC motor already tells you when something is wrong — through its electrical signature. Samotics listens. |

**Content priorities (in scroll order):**

1. Problem statement — name the blind spot within the first viewport. 30–40% of critical assets go unmonitored. Visitors from S1 and S2 need to see their problem reflected immediately.
2. Solution framing — ESA from the MCC. One sentence. Link to `/technology/esa`.
3. Industry routing — visual selector or grid linking to `/industries/[x]`. Organic search visitors self-select here.
4. Social proof — headline numbers: 10,000+ assets, 80+ customers, 5 continents, >90% detection rate. Links to `/proof`.
5. Platform preview — what SAM4 looks like. Screenshot or animation. Link to `/platform/sam4`.
6. Trust signals — ABB partnership, EIB financing, customer logos. Link to `/about`.
7. CTA block — Request a Demo (primary), Start Your Asset Audit (secondary).

**Design tension:** The homepage serves everyone, which means it risks serving no one well. The routing function matters more than the content depth. Every section should be scannable in under 5 seconds and link deeper for the visitor who wants more.

---

### Problem

| | |
|---|---|
| **URL** | `/problem` |
| **Phase** | v1 |
| **Purpose** | Name and quantify the monitoring blind spot. Validate the visitor's pain. Create urgency by showing that 30–40% of critical assets go unmonitored — and what that costs. |
| **Target audience** | Reliability Manager (S1, S2), Operations Director (S2). These visitors arrive with a known problem. The page must mirror their reality before offering a solution. |
| **Primary action** | Start Your Asset Audit. Secondary: Request a Demo. |
| **Traffic sources** | Homepage (problem statement block), Google organic (S1/S2 problem-aware searches: "pump failure prevention", "unmonitored critical assets"), industry page back-links. |
| **Key message** | The assets you can't monitor are the ones most likely to fail. And right now, 30–40% of your critical rotating equipment is invisible. |

**Content priorities:**

1. Open with the blind spot — 30–40% of critical rotating equipment has no condition monitoring. Use industry data, not Samotics marketing claims.
2. Cost of the gap — quantify: unplanned downtime cost, pollution risk, safety exposure, energy waste. Use real numbers where possible (Yorkshire Water: £390K potential fine from a single event).
3. Why this persists — link to `/problem/proximity-penalty` for the structural explanation. Most visitors don't need the full detail; they need to know there's a reason beyond negligence.
4. The shift — introduce ESA as the method that closes the gap. Don't sell the product here — sell the possibility that the gap can be closed. Link to `/technology/esa`.
5. CTA — Start Your Asset Audit (primary). This page attracts S2 visitors who are quantifying, not yet buying. The audit is the right-sized next step.

---

### The Proximity Penalty

| | |
|---|---|
| **URL** | `/problem/proximity-penalty` |
| **Phase** | v1 |
| **Purpose** | Explain why traditional monitoring can't reach 30–40% of critical assets. Physical, economic, and regulatory barriers. Reframe the gap as structural, not a failure of effort. |
| **Target audience** | Reliability Manager (S2) building an internal case. Operations Director who needs to explain the gap to leadership. |
| **Primary action** | Start Your Asset Audit. Secondary: See how ESA works → `/technology/esa`. |
| **Traffic sources** | `/problem` page (deeper dive link), Google organic ("why can't we monitor submerged pumps", "condition monitoring hard-to-reach assets"). |
| **Key message** | The reason 30–40% of your assets are unmonitored isn't negligence — it's physics. Sensors need proximity. These assets don't allow it. |

**Content priorities:**

1. Three barriers — physical (submerged, enclosed, hazardous), economic ($500 sensor becomes $5,000+ installed), regulatory (ATEX, confined space permits).
2. Examples per barrier — real assets, real industries. Submerged sewage pumps (Water), enclosed compressors (Chemicals), ATEX zone motors (Oil & Gas).
3. The structural reframe — this isn't something better maintenance practices can solve. It requires a fundamentally different monitoring approach.
4. Bridge to ESA — "What if you could monitor from the electrical cabinet instead of the asset?" Link to `/technology/esa`.

---

### ESA Technology

| | |
|---|---|
| **URL** | `/technology/esa` |
| **Phase** | v1 |
| **Purpose** | Establish ESA as credible, validated science. This is the core credibility page for technical evaluators. Physics, not marketing. |
| **Target audience** | Reliability Manager (S1, S2) — primary. Channel Partner (S5) evaluating differentiation. Operations Director scanning for legitimacy. |
| **Primary action** | Request a Demo. Secondary: See customer results → `/proof`. |
| **Traffic sources** | Homepage ("How it works" pathway), `/problem` (solution link), industry pages, Google organic ("electrical signature analysis", "motor current signature analysis"). |
| **Key message** | Every AC motor's electrical signature reveals the condition of the entire drivetrain — motor, transmission, coupling, and driven load. SAM4 reads that signature 24/7. |

**Content priorities:**

1. What ESA is — physics-first explanation. Current and voltage signatures captured at the MCC. AI models trained on thousands of assets.
2. What it detects — fault types: bearing degradation, misalignment, imbalance, cavitation, clogging, electrical faults, process deviations. Detection matrix by equipment type.
3. How it's different from MCSA — legacy ESA was an oscilloscope for specialists. SAM4 is a dashboard for operations. Same physics, different experience.
4. Validation — ISO 20958, 40+ years of ESA science, 10,000+ assets monitored.
5. Layered content — headline → explainer → deep dive. Jump links for visitors who want to go deep. The Reliability Manager reads every section. The Ops Director reads the headline and leaves.

**Design pattern:** Layered content with jump links. Must serve both the 3-minute scan and the 15-minute deep read.

---

### How It Works

| | |
|---|---|
| **URL** | `/technology/how-it-works` |
| **Phase** | v1 |
| **Purpose** | Show the end-to-end data flow from sensor to insight. Architecture page for the Digital/Innovation Lead evaluating how data moves. |
| **Target audience** | Digital / Innovation Lead (S3) — primary. Reliability Manager wanting the full picture. |
| **Primary action** | See the SAM4 Platform → `/platform/sam4`. Secondary: Request a Demo. |
| **Traffic sources** | `/technology/esa` (deeper dive), `/platform/sam4` (architecture reference), Digital Lead journey (S3). |
| **Key message** | From the MCC to your dashboard: current/voltage data captured → edge processing → cellular transmission → cloud analytics → SAM4 alerts. No corporate network required. |

**Content priorities:**

1. Visual data flow — diagram showing: CT/VT clamp at MCC → Samotics gateway → cellular connection → cloud → SAM4 dashboard → CMMS integration. This is the page's anchor.
2. Key architecture points — cellular (not corporate WiFi), edge processing, cloud analytics, API connectivity.
3. What the Digital Lead needs — data residency, processing pipeline, network isolation, no corporate IT dependency.
4. Link to security and integrations — natural next step for the Digital Lead evaluating architecture.

---

### ESA vs Vibration

| | |
|---|---|
| **URL** | `/technology/esa-vs-vibration` |
| **Phase** | v1 |
| **Purpose** | Handle the #1 objection head-on. Position ESA as complementary to vibration, not a replacement. Honest comparison builds credibility. |
| **Target audience** | Reliability Manager (S1, S2) — this persona almost certainly has an existing vibration programme and needs to understand where ESA fits. |
| **Primary action** | Request a Demo. Secondary: See detection results → `/proof`. |
| **Traffic sources** | `/technology/esa` (comparison link), Google organic ("ESA vs vibration monitoring", "electrical signature vs vibration analysis"), Reliability Manager journey (S1, step 3). |
| **Key message** | For accessible assets, vibration is excellent. But 30–40% of your fleet can't be reached by sensors on the machine. ESA monitors from the MCC — covering what vibration can't. 90% from ESA beats 0% from nothing. |

**Content priorities:**

1. Comparison table — sensor location, access requirements, installation time, monitoring mode, fault coverage, cost per point. Factual. No spin.
2. Where ESA wins — submerged, enclosed, hazardous, remote assets. Continuous monitoring between vibration rounds. Electrical fault detection.
3. Where vibration wins — specific mechanical faults on accessible assets may have higher resolution with vibration. Acknowledge this.
4. The complementary argument — many customers run both. ESA extends coverage; vibration provides depth on accessible assets. Combined = most complete monitoring programme.
5. Proof — Schiphol detected bearing damage that vibration monitoring missed.

**Critical note:** This page determines whether the Reliability Manager accepts ESA as valid (S1, step 3). If the comparison feels dishonest or evasive, they leave. Candour is the conversion mechanism.

---

### SAM4 Platform

| | |
|---|---|
| **URL** | `/platform/sam4` |
| **Phase** | v1 |
| **Purpose** | Show what the visitor will actually use day-to-day. Dashboard, alert logic, diagnostics, service model. The most-visited page across all personas. |
| **Target audience** | All personas. Reliability Manager evaluates usability. Operations Director evaluates ROI. CTO evaluates enterprise fit. Digital Lead evaluates architecture. Partner evaluates differentiation. |
| **Primary action** | Request a Demo. Secondary: Talk to Us (for executive visitors). |
| **Traffic sources** | Homepage (platform pathway), `/technology/esa` and `/technology/how-it-works` (method → platform flow), all industry pages, CTO journey (S3, step 2). |
| **Key message** | SAM4 is the platform that turns every connected AC motor into a continuous health sensor. Dashboard, diagnostics, alerts, and expert analysis — one view across your entire fleet. |

**Content priorities:**

1. Dashboard showcase — screenshots or interactive preview. Asset health overview, alert feed, diagnostic detail, fleet-level analytics.
2. Alert logic — how alerts work, severity levels, notification channels. The Reliability Manager wants to know: will this generate false positives that train my team to ignore it?
3. Diagnostic depth — what the diagnostician sees. Fault type, severity, recommended action, timeline.
4. Service model — SAM4 isn't just software. Dedicated CSM, diagnostic support, quarterly reviews. This is a partnership, not a login.
5. Enterprise features — multi-site management, role-based access, API, reporting dashboards. For the CTO and Digital Lead.
6. Links to deployment (How It Installs), security, integrations.

**Design pattern:** Progressive disclosure. Overview layer for the 5-minute scan. Expandable sections for technical depth. The CTO reads the overview. The Digital Lead expands everything.

---

### How It Installs

| | |
|---|---|
| **URL** | `/platform/how-it-installs` |
| **Phase** | v1 |
| **Purpose** | Remove the deployment objection. Show that installation is fast, non-invasive, and practical for any maintenance team. |
| **Target audience** | Reliability Manager (S1, step 6), Operations Director (S1/S2, step 4). Both need to believe their team can deploy this without disruption. |
| **Primary action** | Request a Demo. Secondary: See deployment results → `/proof`. |
| **Traffic sources** | `/platform/sam4` (deployment details link), buying scenario flows (S1 step 4, S2 step 4). |
| **Key message** | Less than 30 minutes per machine. At the MCC, not on the asset. No production downtime. No scaffolding, no permits, no ATEX certification. Your team can do this. |

**Content priorities:**

1. Installation steps — visual, numbered. CT/VT clamp installation at the MCC. Gateway setup. Cellular connectivity. First data within hours.
2. Time and effort — <30 minutes per machine. No shutdown. No specialist contractor required.
3. What's NOT needed — no sensors on the machine, no corporate network changes, no production impact.
4. Scale — pilot (5–20 assets) → site (50–200) → fleet (1,000+). Same process at every scale.
5. Customer quote on deployment ease — Pfleiderer: "very low installation effort."

---

### Security & Compliance

| | |
|---|---|
| **URL** | `/platform/security` |
| **Phase** | v1 |
| **Purpose** | Pass the Digital Lead's security review. This page exists to prevent a deal-killing veto at S3, step 4. It must be substantial, not a bullet list of certification logos. |
| **Target audience** | Digital / Innovation Lead (S3) — primary. CTO (S3) — secondary scan. |
| **Primary action** | Request Security Docs (inline gated form). Secondary: Talk to Us. |
| **Traffic sources** | `/platform/sam4` (security details link), Digital Lead journey (S3, step 4), CTO journey (S3, step 4). |
| **Key message** | SOC 2 Type II certified. ISO 27001 and ISO 9001 compliant. Cellular architecture — no corporate network dependency. Your IT/OT review starts here. |

**Content priorities:**

1. Certifications — SOC 2 Type II, ISO 27001, ISO 9001, NIS2 compliance. Each with scope description, not just a logo.
2. Cellular architecture — data flows over cellular, not corporate WiFi/LAN. No network changes. No firewall rules. This is the single most important architectural point for the Digital Lead.
3. Data security — encryption in transit and at rest, data residency, access controls, audit logging.
4. Compliance frameworks — NIS2, OFWAT, industry-specific regulatory alignment.
5. Downloadable security docs — gated form (see CTA Strategy §4). SOC 2 report, architecture diagram, NIS2 compliance summary. Immediate download after form submission. No delay.

**Critical note:** If this page is thin, the Digital Lead vetoes the deal regardless of champion enthusiasm. This page must feel like it was written for a security reviewer, not a marketing audience.

---

### Integrations

| | |
|---|---|
| **URL** | `/platform/integrations` |
| **Phase** | v1 |
| **Purpose** | Show how SAM4 connects to existing systems. CMMS integration is a top concern for the Digital Lead and a workflow requirement for the Reliability Manager. |
| **Target audience** | Digital / Innovation Lead (S3) — evaluating stack compatibility. Reliability Manager — checking whether SAM4 fits existing CMMS workflows. |
| **Primary action** | Talk to Us. Secondary: Need security docs? → `/platform/security`. |
| **Traffic sources** | `/platform/sam4` (integration details), `/platform/security` (related technical), Digital Lead journey. |
| **Key message** | SAM4 integrates with your CMMS, SCADA, and existing workflows. SAP PM, IBM Maximo, and API connectivity — so alerts reach the people who act on them. |

**Content priorities:**

1. CMMS integration — SAP PM, IBM Maximo. How alerts flow into work orders.
2. SCADA connectivity — where relevant (Water, Oil & Gas).
3. API — REST API for custom integrations. Technical documentation link (or mention of availability on request).
4. What integration looks like — not just a list of logos. Show the data flow: SAM4 alert → CMMS work order → maintenance action.

---

### Water & Wastewater

| | |
|---|---|
| **URL** | `/industries/water` |
| **Phase** | v1 |
| **Purpose** | Samotics' strongest vertical. Entry point for water utility visitors arriving from S1 (pump failure) or S2 (coverage gap). Must serve both the reactive and the proactive mindset. |
| **Target audience** | Reliability Manager (S1, S2) at a water utility. Operations Director evaluating fleet-scale monitoring. |
| **Primary action** | Request a Demo. Tertiary: Start Your Asset Audit. |
| **Traffic sources** | Google organic ("submerged pump monitoring", "sewage pump failure detection", "condition monitoring water utility"), homepage industry routing, `/proof` back-links. |
| **Key message** | Continuous pump health monitoring — without a site visit. SAM4 monitors every connected pump 24/7 from the MCC, detecting blockages, bearing degradation, and efficiency losses before they cause failures, fines, or pollution. |

**Content priorities:**

1. Name the trigger — lead with the problem, not the product. Pump failures at remote unmanned sites. OFWAT fines. Pollution events. AMP performance commitments.
2. Asset types monitored — submersible pumps, booster pumps, boreholes, circulation pumps, blowers.
3. Proof — Yorkshire Water (£10M contract, 1,000+ stations), Southern Water (63 failures caught), Vitens (7.1% efficiency). Link to each case study.
4. Dual framing — reactive (S1: "Your pump just failed. Here's how to prevent it from happening again.") + proactive (S2: "You know 30% of your pumps are unmonitored. Here's how to close the gap.").
5. OFWAT/regulatory alignment — monitoring coverage as regulatory evidence. Pollution prevention data.
6. Energy angle — pump efficiency monitoring. 28% electricity reduction targets (Yorkshire Water). This serves S4 visitors who land here.

**Design pattern:** Dual framing. The page needs to serve both the "something just broke" visitor and the "we're planning a rollout" visitor. Consider tab or section structure that addresses both mindsets.

---

### Oil & Gas

| | |
|---|---|
| **URL** | `/industries/oil-gas` |
| **Phase** | v1 |
| **Purpose** | Position SAM4 as the solution for hazardous and ATEX zone monitoring. Safe-zone installation from the MCC eliminates the access barrier. |
| **Target audience** | Reliability Manager (S1), HSE Officer (gatekeeper in hazardous zones). |
| **Primary action** | Request a Demo. |
| **Traffic sources** | Google organic ("ATEX zone motor monitoring", "hazardous area condition monitoring"), homepage industry routing. |
| **Key message** | Monitor motors in ATEX zones, offshore platforms, and hazardous areas — from the safety of the MCC. No sensors in the hazardous zone. No permits. No risk. |

**Content priorities:**

1. ATEX/hazardous zone focus — the defining value prop for Oil & Gas. Installation at the MCC means no ATEX certification, no confined space entry, no hot work permits.
2. Asset types — compressors, pumps, fans, generators in upstream, midstream, and downstream operations.
3. Safety framing — HSE officers care about reducing exposure to hazardous zones. SAM4 eliminates the need for personnel to access these areas for monitoring.
4. Proof — available case studies and customer logos relevant to Oil & Gas.
5. Link to ESA technology and installation pages.

---

### Metals & Mining

| | |
|---|---|
| **URL** | `/industries/metals-mining` |
| **Phase** | v1 |
| **Purpose** | Catch what periodic maintenance rounds miss. Continuous monitoring in extreme environments where vibration walk-arounds are infrequent or impractical. |
| **Target audience** | Reliability Manager (S1), Operations Director. |
| **Primary action** | Request a Demo. |
| **Traffic sources** | Google organic ("motor monitoring steel plant", "bearing failure detection manufacturing"), homepage industry routing. |
| **Key message** | Catch what your maintenance schedule misses. SAM4 monitors motor signatures continuously, surfacing anomalies between rounds — in high-temperature, high-vibration environments where sensors struggle. |

**Content priorities:**

1. Between-rounds detection — unplanned downtime costs tens of thousands per hour. SAM4 fills the gap between periodic vibration checks.
2. Proof — ArcelorMittal (bearing fault detected 5 months early, €50K+ saved), Nyrstar (ROI within months), Nucor (detecting issues outside maintenance schedule).
3. Extreme environments — high temperature, dust, heavy vibration. Sensors at the MCC avoid these conditions entirely.
4. Asset types — crushers, conveyors, fans, compressors, cooling water pumps.

---

### Chemicals

| | |
|---|---|
| **URL** | `/industries/chemicals` |
| **Phase** | v1 |
| **Purpose** | Extend monitoring coverage to process-critical pumps and compressors in ATEX zones. Low installation effort in environments where shutdowns are expensive and access is restricted. |
| **Target audience** | Reliability Manager (S1), Digital / Innovation Lead evaluating technology fit. |
| **Primary action** | Request a Demo. |
| **Traffic sources** | Google organic ("chemical plant motor monitoring", "ATEX condition monitoring"), homepage industry routing. |
| **Key message** | Monitor every critical motor from the MCC — in hours, not months. No shutdown. No sensor mounting on rotating equipment. Full ATEX compatibility. |

**Content priorities:**

1. ATEX compatibility and access restrictions — similar to Oil & Gas but process-chemical focus.
2. Proof — DuPont (40% downtime reduction, 3 European sites), DSM-Firmenich, Nobian, OCI, Evonik, Lenzing.
3. Low installation effort — Pfleiderer: "very low installation effort." No production disruption.
4. Integration with existing reliability workflows.

---

### Pulp & Paper

| | |
|---|---|
| **URL** | `/industries/pulp-paper` |
| **Phase** | v1 |
| **Purpose** | Dual value: reliability AND energy efficiency. This industry is a growing entry point for S4 (Energy & Efficiency Mandate) alongside S1/S2. |
| **Target audience** | Reliability Manager (S1, S2), Mill/Plant Manager (S4 — energy costs), ESG/Sustainability Lead (S4 — reportable savings). |
| **Primary action** | Request a Demo. |
| **Traffic sources** | Google organic ("pulp paper motor monitoring", "mill energy efficiency"), homepage industry routing. |
| **Key message** | Reliability and energy efficiency are the same problem from different angles. SAM4 monitors motor health AND energy performance — catching faults before they stop production and identifying waste before it hits your bill. |

**Content priorities:**

1. Dual framing — reliability (failure prevention) + energy (efficiency monitoring, motor rightsizing). This page bridges S1/S2 and S4.
2. Asset types — refiners, pumps, fans, compressors in pulp and paper mills.
3. Energy data — BEP deviation, oversized motor detection, kWh savings.
4. Proof — Pfleiderer case studies, relevant detection stories.
5. ESG alignment — reportable energy outcomes for sustainability teams.

---

### Proof Hub

| | |
|---|---|
| **URL** | `/proof` |
| **Phase** | v1 |
| **Purpose** | Filterable grid of customer results. Every persona visits this page. It must serve the Reliability Manager wanting fault detail, the Operations Director wanting ROI, and the CTO wanting enterprise scale — in one view. |
| **Target audience** | All personas, all scenarios. The most-visited page after the homepage. |
| **Primary action** | Request a Demo (footer). Secondary: Start Your Asset Audit. Per-card: Download PDF (ungated). |
| **Traffic sources** | Homepage (social proof block), every technology page (validation), every industry page (matching proof), every platform page (results). |
| **Key message** | Real results from real customers. Filter by industry, asset type, or outcome to find proof that matters to your operation. |

**Content priorities:**

1. Filterable grid — filter by: industry (Water, Metals, Chemicals, etc.), outcome type (ROI, detection, energy, scale), asset type (pumps, compressors, fans, etc.).
2. Card design — each card shows: customer name/logo, industry, headline outcome (e.g., "£9.8M in benefits"), one-line summary. Click through to full case study.
3. Download icon per card — direct PDF download (ungated). The Operations Director scans, downloads, and leaves. Don't make them click through to download.
4. Aggregate stats banner — top of page: 10,000+ assets, 80+ customers, 5 continents, >90% detection rate.

---

### Individual Case Studies (Template)

| | |
|---|---|
| **URL** | `/proof/[client-slug]` (e.g., `/proof/yorkshire-water`) |
| **Phase** | v1 |
| **Purpose** | Deep-dive customer story. Specific fault detected, specific financial outcome, specific timeline. This is where the Reliability Manager confirms "they caught a fault I'd recognise" and the Operations Director gets the number for the business case. |
| **Target audience** | Reliability Manager (S1 step 4, S2 step 4) — wants fault detail. Operations Director (S2 step 2, step 5) — wants financial outcomes. CTO (S3 step 3) — wants enterprise scale. |
| **Primary action** | Download PDF (ungated, above fold + bottom). Secondary: Request a Demo. |
| **Traffic sources** | `/proof` hub (card click), industry pages (matching proof link), Google organic (customer name + Samotics), LinkedIn shares. |
| **Key message** | Varies by case study. Always follows the pattern: "[Customer] faced [problem]. SAM4 detected [specific fault/outcome]. Result: [quantified impact]." |

**Content structure (template for all case studies):**

1. Headline outcome — the number that stops the scroll. "£9.8M in benefits" or "9/9 faults detected" or "800% ROI in 11 months."
2. Customer context — who they are, what they operate, why they needed monitoring.
3. The challenge — specific problem or gap. Name the asset type and the risk.
4. The solution — how SAM4 was deployed. Fleet size, timeline, installation.
5. Results — quantified outcomes: financial savings, faults detected, downtime avoided, pollution prevented, energy savings. Use tables or callout boxes for scannability.
6. Customer quote — attributed, named, role-specific.
7. PDF download — prominent, above fold. Ungated.
8. Related case studies — 2–3 links to case studies in the same industry or with similar outcomes.

**Case studies in v1:**

| Case Study | URL | Headline Outcome | Primary Scenario |
|-----------|-----|-----------------|-----------------|
| Yorkshire Water | `/proof/yorkshire-water` | £9.8M benefits, 1,300 assets, 70K inspections replaced | S2 (fleet-scale coverage) |
| Southern Water | `/proof/southern-water` | 63 failures caught, £748K annual savings | S1/S2 (detection volume) |
| Schiphol | `/proof/schiphol` | 9/9 faults detected — 100% detection rate | S1 (detection accuracy) |
| thyssenkrupp | `/proof/thyssenkrupp` | Bearing fault in extreme environment | S1 (harsh environment) |
| Nyrstar | `/proof/nyrstar` | 800% ROI in 11 months | S1/S2 (fast ROI) |
| Vitens | `/proof/vitens` | 7.1% energy efficiency improvement | S4 (energy) |

---

### About

| | |
|---|---|
| **URL** | `/about` |
| **Phase** | v1 |
| **Purpose** | Company credibility page. Exists to pass the CTO's 30-second trust check at S3, step 1. Not a mission statement — a trust signal. |
| **Target audience** | CTO / VP Engineering (S3) — primary. Operations Director (30-second credibility check). |
| **Primary action** | Talk to Us. Secondary: See Customer Results → `/proof`. |
| **Traffic sources** | Homepage (company link), CTO journey (S3, step 1), Operations Director journey (step 3), footer (persistent). |
| **Key message** | Samotics is an enterprise-grade technology company backed by ABB, Siemens, and the European Investment Bank. 10,000+ assets monitored across 5 continents. This is a credible partner for a strategic initiative. |

**Content priorities (stats-first layout):**

1. Numbers above the fold — assets monitored (10,000+), customers (80+), continents (5), team (~103), total funding ($44.1M). The CTO scans these in 5 seconds and decides whether to go deeper.
2. Strategic partnerships — ABB (10% equity, ACS880 integration), Siemens (NXpower Monitor), EIB financing (€20M). These are credibility multipliers.
3. Team — leadership team with photos, titles, backgrounds. Optional: key technical leadership.
4. Founded — 2015, Leiden, Netherlands. Brief company origin. No "our vision" fluff.
5. Link to ABB partnership page for deeper detail.

**Design pattern:** Stats-first. Numbers before narrative. The CTO doesn't read paragraphs on an About page — they scan for scale indicators.

---

### ABB Partnership

| | |
|---|---|
| **URL** | `/about/abb` (v1) → `/partners/abb` (Phase 2) |
| **Phase** | v1 |
| **Purpose** | ABB partnership detail. Equity stake, ACS880 integration, co-sell model. Critical for S3 (CTO) and S5 (Channel Partner). |
| **Target audience** | CTO / VP Engineering (S3) — ABB validation. Channel Partner (S5) — reference partner model. |
| **Primary action** | Talk to Us. Secondary: Discuss Partnership (text link, routes to `/contact` with partner intent in v1). |
| **Traffic sources** | `/about` (partnership link), ABB referrals (direct link shared by ABB account teams), CTO journey (S3, step 1), Partner journey (S5, steps 1 and 4). |
| **Key message** | ABB evaluated every option in the market and chose Samotics. 10% equity stake. SAM4 ESA integrated into ABB's flagship ACS880 variable frequency drives. |

**Content priorities:**

1. The fact that ABB invested — 10% equity. This matters more than any co-marketing arrangement. They had the resources to build this internally. They chose partnership.
2. ACS880 integration — SAM4 ESA embedded in ABB's flagship drives. Technical integration, not just a logo swap.
3. Co-sell model — how ABB account teams introduce Samotics. Relevant for S5 partners evaluating the channel model.
4. Quote or endorsement from ABB if available.

---

### Contact

| | |
|---|---|
| **URL** | `/contact` |
| **Phase** | v1 |
| **Purpose** | Conversion endpoint for every journey. Must route by intent: demo (Reliability), audit (Ops), executive briefing (CTO), security docs (Digital), partnership (Partner). |
| **Target audience** | All personas, all scenarios. |
| **Primary action** | Intent-based form submission (see CTA Strategy for full form specs). |
| **Traffic sources** | Every page on the site (via nav CTA or in-page CTA). UTM-tagged campaign links. |
| **Key message** | Tell us what you need. We'll match you with the right conversation. |

**Content priorities:**

1. Intent selector — displayed first. Five options: demo, audit, executive briefing, security docs, partnership. Form fields appear after selection (progressive disclosure).
2. No wall of fields — the intent selector IS the first interaction. This prevents the generic "fill in 12 fields" experience that kills conversion.
3. Expectation setting — after intent selection, show a one-line description of what happens next ("We'll schedule a technical demo within 5 business days").
4. Social proof — customer logos or a single stat below the form. Light touch — don't distract from the form.

---

### Asset Audit

| | |
|---|---|
| **URL** | `/contact/asset-audit` |
| **Phase** | v1 |
| **Purpose** | Dedicated landing page for the asset audit CTA. Lower-commitment than a demo. Outputs a gap report that the Operations Director can use for an internal proposal. |
| **Target audience** | Operations Director (S2, S3). Reliability Manager (S2) building a case. |
| **Primary action** | Submit asset audit form (see CTA Strategy §2 for fields). |
| **Traffic sources** | `/problem` (primary CTA), homepage (secondary CTA), `/proof` (alternative CTA on fleet-scale case studies). |
| **Key message** | Start with clarity. An asset audit quantifies your coverage gap, prioritises your assets, and gives you the data for an internal business case. No commitment beyond the conversation. |

**Content priorities:**

1. What an asset audit delivers — coverage gap quantification, prioritised asset list, ROI estimate, deployment recommendation. Be specific about the output.
2. What it requires — a conversation about your fleet, your sites, and your monitoring coverage. 30–60 minutes.
3. Form — shorter context than the main contact form. Focus on fleet data (sites, asset count, current coverage).
4. Expectation — "We'll prepare your audit scope and reach out within 2 business days."

---

### Blog / Resources

| | |
|---|---|
| **URL** | `/resources` (hub), `/resources/blog`, `/resources/webinars`, `/resources/downloads` |
| **Phase** | v1 |
| **Purpose** | Content hub for thought leadership, detection stories, industry insights, and downloadable assets. Supports SEO, nurture, and top-of-funnel awareness. |
| **Target audience** | Broad. Blog serves awareness visitors. Downloads serve mid-funnel evaluators. Webinars serve engaged prospects. |
| **Primary action** | Varies by content type. Blog: Request a Demo (bottom). Downloads: Download (per asset). Webinars: Watch Now / Register. |
| **Traffic sources** | Google organic (long-tail content searches), LinkedIn content clicks, email nurture campaigns, social shares. |
| **Key message** | Varies by content piece. The hub itself: "Insights on condition monitoring, predictive maintenance, and industrial reliability." |

---

### Utility Pages

**Privacy Policy** (`/privacy`): GDPR compliance. Legal requirement. No CTA.

**Terms of Use** (`/terms`): Legal. No CTA.

**Cookie Policy** (`/cookies`): Cookie consent reference. No CTA.

**404 Page** (`/404`): Custom error page. Purpose: recover lost visitors. Include links to homepage, `/proof`, `/technology/esa`, and `/contact`. Tone: helpful, not cute. Message: "This page doesn't exist. Here's where you probably meant to go."

---

## Phase 2 Pages

---

### Partners Hub

| | |
|---|---|
| **URL** | `/partners` |
| **Phase** | Phase 2 |
| **Purpose** | Partner programme overview. Exists to convert Channel Partners (S5) and OEMs who want to resell or integrate SAM4 into their service offering. This is not a customer page — it speaks to businesses evaluating a commercial relationship with Samotics. |
| **Target audience** | Channel Partner / System Integrator / OEM (S5) — primary. ABB account teams sending prospects to learn about the programme. |
| **Primary action** | Discuss Partnership (accent button → `/contact/partner-inquiry`). Secondary: Talk to Us (outline → `/contact?intent=executive`). |
| **Traffic sources** | `/about` (secondary link: "Interested in partnering?"), `/about/abb` → `/partners/abb` (natural next step), ABB referrals (direct link), Google organic ("Samotics partner programme"), LinkedIn outreach. |
| **Key message** | Partner with the company ABB chose. Bring continuous condition monitoring to your customers without building the technology yourself. SAM4 integrates into your existing service model — from VFD suppliers to maintenance contractors. |

**Content priorities:**

1. ABB as proof of model — ABB evaluated the market, took a 10% equity stake, and co-sells SAM4 through their account teams. If the world's largest drives manufacturer chose partnership over build, the model works. Link to `/partners/abb` for detail.
2. Partner types served — System Integrators, OEMs (drives, motors), Service Providers (maintenance, reliability consulting), Distributors. Each type sees SAM4 differently: the SI integrates it into monitoring projects; the OEM embeds it in hardware; the service provider offers it as a managed service.
3. What Samotics provides — technical enablement, co-marketing support, dedicated partner manager, deal registration, lead sharing. Be specific. Partners evaluate programmes on economics and support, not technology alone.
4. Commercial model — outline without exact numbers (those come in the conversation). Revenue share, tiered programme, protected territories. Enough to qualify interest without giving away the negotiation.
5. Existing partner logos/names — social proof specific to the partner audience. If available, show the breadth of the current partner ecosystem.

**Design pattern:** Problem-solution-proof structure, but framed for the partner persona. Lead with the ABB validation, then programme details, then CTA. Stats strip: number of partners, countries, joint deployments.

**Structural changes triggered by this page:**
- Navigation: "About" becomes a dropdown — Company, Partners, ABB Partnership. (See navigation spec §Phase 2.)
- ABB Partnership page moves from `/about/abb` to `/partners/abb`. Implement 301 redirect.
- Footer: add "Partners" link in the Company column.
- `/about` page: add secondary link — "Interested in partnering? See our partner programme →" linking to `/partners`.

---

### Partner Inquiry

| | |
|---|---|
| **URL** | `/contact/partner-inquiry` |
| **Phase** | Phase 2 |
| **Purpose** | Dedicated partnership inquiry form. Replaces the v1 interim routing through the `/contact` intent selector. Partners need a distinct conversation — different sales owner, different qualification criteria, different SLA. |
| **Target audience** | Channel Partner / System Integrator / OEM (S5). |
| **Primary action** | Submit partnership inquiry form. |
| **Traffic sources** | `/partners` (primary CTA), `/partners/abb` (secondary CTA: "Discuss Partnership"), `/about` (secondary link), `/contact` intent selector (redirect from "I'm interested in a partnership" in v1). |
| **Key message** | Tell us about your business. Our partnerships team — not sales — will reach out within 2 business days to explore fit. |

**Content priorities:**

1. Form — full partner form fields per CTA Strategy §6: first name, last name, work email, company, job title, company type (dropdown: SI, OEM, Service Provider, Distributor, Other), industries you serve (multi-select: Water, Oil & Gas, Metals & Mining, Chemicals, Pulp & Paper, Other), what interests you about partnering (textarea, optional, 500 char max).
2. Expectation setting — "Our partnerships team will reach out within 2 business days." Not sales. Not an SDR. The partner persona is evaluating a commercial relationship and expects peer-level engagement.
3. Light context above the form — 2–3 sentences explaining what the partnership conversation covers: commercial model, technical enablement, territory, and go-to-market support. Keep it short — they arrived from `/partners` where they already read the programme detail.
4. Social proof — ABB partnership reference. "ABB is our flagship partner. See how the model works →" linking to `/partners/abb`.

**Design pattern:** Matches `/contact/asset-audit` structure — hero, light value prop, form, social proof. No intent router (single purpose). Form is the page.

**Post-submission behaviour:** Per CTA Strategy §6 — personalised confirmation ("Thanks, [First name]. Our partnerships team will be in touch within 2 business days."), confirmation email linking to ABB partnership page, CRM lead tagged as "Partner" and routed to partnerships lead (not standard sales), GTM event `partner_inquiry`.

**v1 → Phase 2 migration:**
- The `/contact` intent selector option "I'm interested in a partnership" should redirect to `/contact/partner-inquiry` instead of revealing the inline partner form.
- Keep the v1 inline partner form as a fallback for 30 days, then remove.
- Update the ABB page (`/partners/abb`) "Discuss Partnership" link from `/contact?intent=partner` to `/contact/partner-inquiry`.

---

### ABB Partnership — URL Migration

| | |
|---|---|
| **Current URL (v1)** | `/about/abb` |
| **New URL (Phase 2)** | `/partners/abb` |
| **Action** | Move page, implement 301 redirect from `/about/abb` to `/partners/abb`. |

**Changes required:**

1. 301 redirect: `/about/abb` → `/partners/abb`. Permanent. Do not remove — ABB account teams have shared the v1 URL directly with prospects.
2. Content update: Add "Discuss Partnership" as accent button at bottom (currently a text link). Route to `/contact/partner-inquiry` instead of `/contact?intent=partner`.
3. Breadcrumb update: About → ABB Partnership becomes Partners → ABB Partnership.
4. Internal links update: `/about` page link to ABB partnership must point to `/partners/abb`. All industry pages, proof pages, and any cross-references must be updated.
5. Navigation update: ABB Partnership moves under the "Partners" dropdown (or "About" dropdown if Partners is a sub-item of About).
6. No content rewrite needed — the page content is correct for both CTO (S3) and Partner (S5) audiences. The move is structural, not editorial.

---

## Phase 3 Pages

---

### Energy Efficiency

| | |
|---|---|
| **URL** | `/industries/energy-efficiency` |
| **Phase** | Phase 3 |
| **Purpose** | Dedicated entry point for the S4 persona (Energy & Efficiency Mandate). Unlike the Pulp & Paper page which bridges reliability + energy, this page is energy-first. It speaks to the Sustainability Lead, Energy Manager, or Plant Manager whose mandate is cost reduction and ESG reporting — not fault detection. |
| **Target audience** | ESG / Sustainability Lead (S4 primary), Plant Manager with energy KPIs (S4 secondary), Reliability Manager discovering the energy angle (S1/S2 cross-sell). |
| **Primary action** | See Impact Data (accent button → `/contact?intent=energy`). Secondary: Request a Demo (outline → `/contact?intent=demo`). |
| **Traffic sources** | Google organic ("motor energy efficiency monitoring", "pump BEP monitoring", "ESG energy savings industrial"), `/industries/pulp-paper` cross-link, homepage industry routing (Phase 3 nav update), `/resources/esg-reporting` back-link. |
| **Key message** | Every motor in your plant is a line item on your energy bill. SAM4 measures exactly how much each one wastes — BEP deviation, oversized motors, degraded efficiency — and turns it into reportable savings your sustainability team can use. |

**Content priorities:**

1. Lead with energy waste, not faults — this page serves the S4 visitor. Frame SAM4 as an energy intelligence tool that also catches faults, not a condition monitoring tool that also saves energy.
2. Quantified savings — BEP deviation percentages, kWh attribution per asset, oversized motor detection. The S4 persona needs numbers for business cases and ESG reports.
3. Cross-industry relevance — energy waste exists in every vertical: water (pumping = 80% of electricity), chemicals (compressors), metals (fans), pulp & paper (refiners). Position this page as industry-agnostic.
4. ESG reporting — SAM4 data is auditable, exportable, and attributable to specific assets and actions. Sustainability teams get measured outcomes, not modelled estimates.
5. Proof — Vitens (7.1% energy efficiency improvement), Yorkshire Water (28% electricity reduction target using SAM4 data). Cross-link to full case studies.

**Design pattern:** Industry page structure (Hero → Problem → Capabilities → Proof → CTA) but energy-framed. Lead with the cost problem, not the failure problem. Use teal/green-adjacent accents for energy sections to visually distinguish from reliability-focused industry pages.

**Structural changes triggered by this page:**
- Navigation: Add "Energy Efficiency" as 6th item in Industries dropdown with subtle "New" badge. (Per navigation spec: 6 items is the limit.)
- Homepage: Consider adding energy routing in the industry block (optional — evaluate after launch).
- Pulp & Paper page: Add cross-link — "Looking for energy efficiency across all industries? See our energy monitoring page →"

---

### Coverage Calculator

| | |
|---|---|
| **URL** | `/tools/coverage-calculator` |
| **Phase** | Phase 3 |
| **Purpose** | Interactive self-service tool that quantifies a visitor's monitoring coverage gap. Converts the abstract problem ("some of our assets aren't monitored") into a specific number ("you have a 68% coverage gap exposing £2.1M in annual risk"). Generates urgency without a sales call. Captures lead data as a soft conversion. |
| **Target audience** | Reliability Manager (S2 — "I know I have a gap but can't quantify it"), Operations Director building a business case (S3), Plant Manager preparing a board presentation. |
| **Primary action** | Calculate Your Coverage Gap (tool interaction). Secondary: Start Your Asset Audit (accent button → `/contact?intent=audit`). |
| **Traffic sources** | `/problem` (cross-link: "Quantify your own coverage gap →"), `/problem/proximity-penalty` (cross-link), Google organic ("condition monitoring coverage calculator", "rotating asset monitoring gap"), email campaigns, LinkedIn ads. |
| **Key message** | You know some of your assets aren't monitored. This tool tells you exactly how many, what it's costing you, and where to start. |

**Content priorities:**

1. Calculator inputs — keep it simple. 4 fields max: total rotating assets, currently monitored assets, average cost of unplanned downtime per event, estimated failure events per year on unmonitored assets. All fields have sensible defaults/placeholders so the user can run it immediately.
2. Calculator outputs — coverage gap %, estimated annual risk exposure (£/€/$), comparison benchmark ("Industry average: 60–70% coverage. You: 32%"), and a personalised recommendation tier (Low gap / Moderate gap / Critical gap).
3. Soft lead capture — after showing results, offer "Get a detailed analysis" form (first name, email, company). Ungated results + gated detail = low friction, high intent.
4. Social proof strip — show 1–2 relevant stats (10,000+ assets monitored, 80+ customers) to reinforce credibility at the decision moment.
5. Asset Audit bridge — the calculator quantifies the gap; the asset audit is the next step. Connect them explicitly: "Your gap is X%. An asset audit identifies exactly which assets to prioritise."

**Design pattern:** Tool page — distinct from content pages. Hero (short, no photo) → Calculator (interactive section, white bg) → Results (dynamic, shown after calculation) → Lead Capture (seashell bg) → CTA Block. Minimal chrome, maximum focus on the tool.

**Calculator logic:**
- Coverage gap = ((total - monitored) / total) × 100
- Annual risk = (total - monitored) × (avg downtime cost) × (failure rate / total unmonitored) — simplified as (total - monitored) × avg downtime cost × failure probability
- Benchmark: <40% = Critical, 40–65% = Moderate, >65% = Low gap
- Currency: detect from browser locale or default to € with toggle

**Post-calculation behaviour:**

| Step | Detail |
|------|--------|
| **Results display** | Animated number reveal. Coverage gap %, annual risk estimate, benchmark comparison, recommendation tier with colour coding (red/amber/green). |
| **Detail form** | Optional. First name, work email, company. Submit: "Get Your Detailed Analysis". |
| **GTM tracking** | `coverage_calculator_completed` event with gap_percentage and risk_tier (no PII). If form submitted: `coverage_calculator_lead` with form data. |
| **Internal routing** | Lead to CRM. Tagged as "Calculator — [tier]." Routed to AE based on tier (Critical = fast-track). |

---

### ESG Reporting

| | |
|---|---|
| **URL** | `/resources/esg-reporting` |
| **Phase** | Phase 3 |
| **Purpose** | Content page for the Sustainability Lead (S4) who needs to understand how SAM4 data maps to ESG reporting frameworks. Bridges the gap between "energy monitoring tool" and "reportable ESG outcome." Supports the Energy Efficiency page with deeper ESG-specific content. |
| **Target audience** | ESG / Sustainability Lead (S4 primary), CFO or board-level stakeholder evaluating ESG programme ROI (S4 secondary). |
| **Primary action** | See Impact Data (accent button → `/contact?intent=energy`). Secondary: Download ESG Data Sheet (outline, ungated PDF). |
| **Traffic sources** | `/industries/energy-efficiency` (cross-link), Google organic ("industrial ESG energy reporting", "motor efficiency ESG data", "condition monitoring sustainability reporting"), LinkedIn thought leadership campaigns. |
| **Key message** | SAM4 doesn't just save energy — it proves it. Every kilowatt-hour saved is measured, attributed, and exportable in a format your sustainability team can use for ESG reports, regulatory filings, and board presentations. |

**Content priorities:**

1. Framework alignment — explain how SAM4 energy data maps to common ESG frameworks: GHG Protocol Scope 2, CSRD (EU Corporate Sustainability Reporting Directive), TCFD, CDP. Don't overdo it — the S4 persona knows these acronyms. Show the mapping, not the tutorial.
2. Measured vs modelled — SAM4's differentiator for ESG is that savings are measured from continuous electrical signature data, not modelled from assumptions. Auditors prefer measured outcomes. Make this the centrepiece.
3. Data outputs — what SAM4 exports: kWh savings per asset, baseline vs current consumption, CO₂ equivalent calculations, time-series efficiency data. Exportable as CSV or API.
4. Proof — Vitens (7.1% efficiency gain = quantified kWh), Yorkshire Water (28% electricity reduction target). Frame as "here's what reportable ESG outcomes look like in practice."
5. Download asset — ESG Data Sheet (PDF, ungated). A 2-page summary of SAM4's ESG data capabilities, framework alignment, and example outputs. Serves as a leave-behind for the Sustainability Lead to share internally.

**Design pattern:** Content page — similar to technology pages. Hero → Key Differentiator (measured vs modelled) → Framework Mapping (4 cards) → Data Outputs → Proof → CTA Block. Clean, authoritative, data-heavy. No dual-framing — single audience, single message.

**Structural changes triggered by this page:**
- Resources section: Add "ESG Reporting" to the resources listing if one exists.
- Energy Efficiency page: Add cross-link — "Need ESG-ready data? See how SAM4 maps to reporting frameworks →"
- Pulp & Paper page: Consider adding ESG cross-link in the energy data section.

---

## Quick Reference Matrix

Every v1 page at a glance. The "Story Role" column maps each page to its function in the buyer's StoryBrand narrative. This helps content writers maintain the narrative thread across pages: a "Problem" page should deepen the pain, not introduce the guide. A "Guide" page should demonstrate authority and empathy, not restate the problem. A "Success" page should show the transformation, not the method.

| Page | Primary Persona | Scenario | Primary CTA | Story Role | Key Metric |
|------|----------------|----------|-------------|-----------|------------|
| Homepage | All (S1/S2 weighted) | S1, S2 | Request a Demo | Full arc (compressed) | 10,000+ assets |
| Problem | Reliability, Ops | S1, S2 | Start Your Asset Audit | Problem (external + internal) | 30–40% unmonitored |
| Proximity Penalty | Reliability, Ops | S2 | Start Your Asset Audit | Problem (philosophical) | $500 → $5,000+ installed |
| ESA Technology | Reliability, Partner | S1, S2, S5 | Request a Demo | Guide (authority) | >90% detection rate |
| How It Works | Digital Lead | S3 | See the SAM4 Platform | Guide (authority, technical) | Cellular — no network changes |
| ESA vs Vibration | Reliability | S1, S2 | Request a Demo | Guide (empathy + honesty) | 90% beats 0% |
| SAM4 Platform | All | S1–S5 | Request a Demo | Plan (the tool) | Fleet-level dashboard |
| How It Installs | Reliability, Ops | S1, S2 | Request a Demo | Plan (ease of execution) | <30 minutes per machine |
| Security | Digital Lead, CTO | S3 | Request Security Docs | Plan (risk removal) | SOC 2 Type II |
| Integrations | Digital Lead | S3 | Talk to Us | Plan (fits your world) | SAP PM, IBM Maximo |
| Water | Reliability, Ops | S1, S2, S4 | Request a Demo | Problem + Success (industry) | 1,000+ pumping stations |
| Oil & Gas | Reliability, HSE | S1 | Request a Demo | Problem + Success (industry) | ATEX safe-zone install |
| Metals & Mining | Reliability, Ops | S1 | Request a Demo | Problem + Success (industry) | 5 months early detection |
| Chemicals | Reliability, Digital | S1 | Request a Demo | Problem + Success (industry) | 40% downtime reduction |
| Pulp & Paper | Reliability, Plant Mgr | S1, S2, S4 | Request a Demo | Problem + Success (industry) | 7.1% efficiency gain |
| Proof Hub | All | S1–S5 | Request a Demo + PDF | Success (transformation) | 80+ customers |
| Case Studies | Reliability, Ops, CTO | S1–S3 | Download PDF | Success (specific proof) | Varies per case |
| About | CTO, Ops | S3 | Talk to Us | Guide (identity + authority) | $44.1M funded |
| ABB Partnership | CTO, Partner | S3, S5 | Talk to Us | Guide (endorsed authority) | 10% ABB equity stake |
| Contact | All | S1–S5 | Intent-based form | Call to Action | — |
| Asset Audit | Ops, Reliability | S2, S3 | Submit audit form | Call to Action (transitional) | — |
| Resources | Broad | Awareness | Varies | Guide (thought leadership) | — |
| **Phase 2** | | | | | |
| Partners Hub | Partner, SI, OEM | S5 | Discuss Partnership | Guide (programme) | ABB reference model |
| Partner Inquiry | Partner, SI, OEM | S5 | Submit partner form | Call to Action | — |
| ABB Partnership* | CTO, Partner | S3, S5 | Talk to Us + Discuss Partnership | Guide (endorsed authority) | 10% ABB equity stake |
| **Phase 3** | | | | | |
| Energy Efficiency | Sustainability, Plant Mgr | S4 | See Impact Data | Problem + Success (energy) | 7.1% efficiency gain |
| Coverage Calculator | Reliability, Ops | S2, S3 | Calculate Your Coverage Gap | Plan (self-service tool) | Coverage gap % |
| ESG Reporting | Sustainability, CFO | S4 | See Impact Data + PDF | Guide (ESG authority) | Measured vs modelled |
