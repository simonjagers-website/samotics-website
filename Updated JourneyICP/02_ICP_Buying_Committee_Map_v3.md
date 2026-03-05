# SAMOTICS — ICP & Buying Committee Map (Version 3.1)

**Who buys SAM4, why they buy, and how they buy — by industry**

Owner: Marketing + Sales
Version: 3.1
Date: March 2026
Dependencies: Buyer Journey Framework v3.1, User Journey Map v3.1

---

## What Changed and Why

**Changes (v3.0 → v3.1):**

1. **Canonical Buying Motions reference.** All stage labels now reference the Buying Motions Canon in the Buyer Journey Framework (Section 0.0). Removed all synonym drift ("Requirements Building," "Consensus Creation," "Validation," "Strategic Approval").

2. **SAM4-X canonical positioning.** Replaced mixed messaging about SAM4-X revenue role with canonical statement from Buyer Journey Framework (Section 0.1).

3. **Architecture-aware disqualifiers.** Replaced absolute disqualifiers ("No cloud adoption = disqualified") with gated language that accounts for hybrid, edge, and segmented architectures.

4. **Proof readiness status per industry.** Each playbook now shows whether flagship proof exists (Green), is partial (Yellow), or is missing (Red). This prevents marketing verticals where proof does not yet exist.

5. **ABB conditional positioning.** Replaced blanket "ABB is not a homepage hero" with persona-conditional guidance: lead with failure-mode logic for Champions/Validators; lead with ABB/viability for Enterprise Buyers and Procurement.

6. **Veto timing aligned to canonical motions.** Removed references to "Consensus Creation" and "Requirements Building" in timing descriptions.

**Prior v3.0 changes (retained):**

- Tiered ICP with firmographic, technographic, and behavioural dimensions
- 8-role buying committee
- Champion creation mechanics
- Land-and-expand formalisation
- Industry playbooks with entry persona, killer message, competitive positioning

---

## Canonical References

> **Buying Motions, SAM4-X positioning, and Proof System definitions are governed by the Buyer Journey Framework v3.1.** This document references but does not redefine them.

- **Buying Motions Canon:** See Buyer Journey Framework, Section 0.0
- **SAM4-X Canonical Positioning:** See Buyer Journey Framework, Section 0.1
- **Proof System:** See Buyer Journey Framework, Appendix A
- **Measurement Definitions:** See Buyer Journey Framework, Section 2.1

---

## 1.0 Scope

This document defines two complementary deployment motions and the ICP, buying committee, and industry playbooks that govern them.

**SAM4-X (Land Motion)**

> SAM4-X is a paid validation programme optimised to produce portable proof and an internal champion. Revenue is a byproduct; fleet expansion is the goal.

Monitoring of 1–10 critical assets selected via Asset Criticality Analysis. Project-managed with predefined success criteria, standardised ROI model, and deployment playbook. Short sales cycle. OpEx-funded. See Buyer Journey Framework Section 0.1 for the full definition.

**Fleet Programs (Expand Motion)**
Large-scale deployment across fleets with a structural monitoring gap. Enterprise-wide risk reduction and operational value. Longer sales cycle. CapEx or multi-site programme budget.

---

## 2.0 Ideal Customer Profile

The ICP defines organisations most likely to buy, renew, and expand. It uses a tiered, multi-dimensional model to prioritise GTM effort.

### 2.1 Account Tiers

| Tier | Definition | GTM Treatment | Approximate Size |
|:---|:---|:---|:---|
| **Tier 1 (Focus Accounts)** | Named accounts with highest strategic fit and propensity to buy. Multiple qualifying signals across firmographic, technographic, and behavioural dimensions. | Intensive ABM + dedicated AE. Goal: full committee coverage within 6 months. | 50–100 accounts |
| **Tier 2 (Priority Accounts)** | Strong firmographic and technographic fit. Fewer behavioural signals. | Targeted marketing + inbound/outbound qualification. | 200–500 accounts |
| **Tier 3 (Market)** | General fit on core criteria. | Inbound marketing. Qualify on engagement. | All others meeting minimum criteria |

**Calibration note:** All numeric thresholds below (revenue, employee count) are directional assumptions. Calibrate after 20 closed-won + 20 closed-lost deals by comparing conversion rates and ACV by tier.

### 2.2 ICP Dimensions

| Dimension | Tier 1 Signal | Tier 2 Signal | Tier 3 Signal |
|:---|:---|:---|:---|
| **Firmographics** | | | |
| Industry | Water & Wastewater, Oil & Gas (upstream/midstream), Chemicals, Metals & Mining | Pulp & Paper, Pharmaceuticals, Airports | General manufacturing with motor-intensive operations |
| Revenue | >€1B *(calibrate)* | >€250M | >€50M |
| Employees | >5,000 *(calibrate)* | >1,000 | >500 |
| Operations | Multi-site (5+ production sites) or one very large complex site | Multi-site or one large site | At least one site with significant motor fleet |
| Geography | North America, Western Europe, Middle East (O&G) | Broader EMEA, APAC | Global |
| **Strategic Pressure** (at least one) | | | |
| Production risk | Documented recent critical failure or near-miss | Known production continuity concerns | General awareness of downtime cost |
| Regulatory / Compliance | Active regulatory pressure (e.g., AMP cycle, environmental compliance, safety audit) | Compliance programme in place | Basic regulatory requirements |
| ESG / Energy | Publicly stated ESG / Net-Zero goals; sustainability reporting requirements | Internal energy targets | General awareness |
| Digital initiative | Active digital transformation or Industry 4.0 programme mentioned in annual report or job postings | Digital roadmap in development | Openness to cloud-based tools |
| **Technographics** | | | |
| CMMS / EAM | SAP PM, IBM Maximo, or Infor EAM deployed | Any named CMMS/EAM in use | Basic maintenance tracking |
| Existing monitoring | Known use of vibration analysis (Emerson, Bently Nevada, SKF) — indicates CBM maturity and potential electrical monitoring gap | Some condition monitoring in place | Primarily reactive or calendar-based maintenance |
| Cloud posture | Cloud-first policy or known use of AWS/Azure for operational data | Cloud adoption in progress | Willing to adopt cloud analytics |
| **Behavioural / Intent** | | | |
| Intent signals | Actively researching "submerged pump monitoring," "ESA," "motor failure prediction," "electrical signature analysis" (via third-party intent data) | Some relevant search activity | None detected |
| Web engagement | Multiple stakeholders from same account visiting key pages (security, industry, case studies) | Single-stakeholder engagement | Basic website visit |
| People signals | Recent hiring of "Director of Reliability," "Head of Digital Operations," or "Asset Management Lead" | Reliability team growth | Stable team |

### 2.3 Disqualifiers

Disqualifiers use gated language rather than absolutes. Some conditions that seem disqualifying may be addressable with the right architecture or engagement approach.

| Condition | Disqualifier? | Gate |
|:---|:---|:---|
| Primary maintenance strategy is run-to-failure | **Yes** — if no intent or budget to change | If there is an active initiative to move toward CBM → not a disqualifier, but requires longer education cycle |
| No cloud adoption for operational technology | **Conditional** | Cloud refusal + no alternative architecture path (hybrid, edge, segmented) = disqualifier. If customer accepts hybrid/edge deployment → proceed, but flag integration complexity. Define approved architectures: (1) full cloud, (2) hybrid (edge compute + cloud analytics), (3) segmented network with data diode. |
| Recently signed fleet-wide, multi-year contract with direct competitor | **Yes** — for fleet motion | May still be open to SAM4-X on asset classes the competitor does not cover (e.g., electrical faults if competitor is vibration-only) |
| No identifiable critical assets or structural monitoring gap | **Yes** | N/A — no use case exists |
| No internal champion at site level AND no senior economic sponsor | **Yes** — for active pursuit | Park in nurture. Re-evaluate if a contact emerges. |
| No CMMS or structured maintenance workflow | **Conditional** | If customer is actively implementing CMMS → proceed with longer timeline. If no maintenance structure at all → disqualifier. |

---

## 3.0 The Enterprise Buying Committee

### 3.1 Role Map

| Role | Typical Title(s) | Core Question | Core Need | Key Enablement Asset |
|:---|:---|:---|:---|:---|
| **Champion** | Reliability Manager, Maintenance Superintendent | "Will this solve my problem and make me look credible?" | Internal proof, access to power, tools to sell internally | Champion Enablement Kit (internal deck, business case template, ROI calculator, security FAQ) |
| **Technical Validator** | Maintenance / Reliability Engineer, CBM Analyst | "Show me detection logic, limits, and diagnostic value." | Detection examples, asset-type validation, workflow integration proof, diagnostic depth | Detection matrix, engineering FAQ, diagnostic example pack, architecture diagram |
| **Economic Buyer (Plant)** | Plant Director, Operations Manager, Mill Manager | "What is the financial impact and how fast?" | Credible ROI, deployment speed, production impact | Validated ROI model (from pilot data), deployment timeline |
| **Economic Buyer (Enterprise)** | VP Operations, VP Reliability, CTO | "Is this scalable, strategic, and enterprise-safe?" | Confidence in long-term vision, vendor viability, strategic alignment | Executive briefing, multi-site deployment playbook, enterprise business case |
| **IT/OT Gatekeeper** | CISO, Dir. of IT, Head of OT Security | "Will this introduce risk to my environment?" | Proof of security, data integrity, seamless integration | Trust & Security Centre (certifications, architecture, data handling policies), API documentation |
| **Procurement Gatekeeper** | Procurement / Sourcing Manager, Contract Manager | "Is this a responsible use of capital? Does it meet our vendor requirements?" | Financial rigour, competitive pricing, contract compliance, TCO | Standardised MSA, TCO comparison, vendor compliance documentation |
| **Corporate Reliability / Asset Management** | VP Asset Management, Global Reliability Director | "How does this fit our corporate asset management strategy?" | Cross-site consistency, standards alignment, strategic fit | Multi-site results summary, ISO 55000 alignment brief, deployment playbook |
| **Practitioner** | Maintenance Technician, Operator | "Will this make my job easier or harder?" | Usability, trustworthy alerts, minimal noise | Live product demo (day-in-the-life workflow), install sheet, after-alert playbook |

### 3.2 Committee Composition by Motion

| Role | SAM4-X (Land) | Fleet Program (Expand) |
|:---|:---|:---|
| Champion | **Active** — owns the pilot | **Active** — builds the enterprise case |
| Technical Validator | **Active** — validates detection on target assets | **Active** — validates scalability |
| Economic Buyer (Plant) | **Active** — approves pilot budget | Consulted — provides site-level input |
| Economic Buyer (Enterprise) | Informed | **Active** — approves enterprise budget |
| IT/OT Gatekeeper | Consulted (may be bypassed for small pilots) — but always send Trust & Security Centre proactively | **Active** — full security review required |
| Procurement Gatekeeper | Minimal (often below tender threshold) | **Active** — manages vendor selection and terms |
| Corporate Reliability | Informed | **Active** — sets standards for enterprise deployment |
| Practitioner | **Active** — validates usability during pilot | Consulted — provides adoption feedback |

### 3.3 Champion Creation Mechanics

1. **Identify.** Find individuals with high personal pain (recurring failures, missed KPIs, career risk from downtime) and organisational influence (trusted by directors, cross-departmental visibility).
2. **Test.** Assign a small but meaningful task: "Can you get us the failure data for the last 12 months on Asset X?" or "Can you schedule 15 minutes with your IT lead?" Willingness and ability proves commitment.
3. **Equip.** Grant access to the Champion Enablement Kit: a secure portal with a pre-built business case, ROI calculator, internal presentation deck, competitive positioning document, and security FAQ.

**Key metric:** "Champion Created" should be a leading indicator KPI for all AEs on Tier 1 accounts.

### 3.4 Veto Dynamics & Risk Mitigation

| Veto Source | Primary Blocker | Default Timing | Mitigation |
|:---|:---|:---|:---|
| IT/OT Security (CISO) | Data sovereignty, network risk, cloud resistance | **Any stage — can kill at any time** | Engage in first follow-up. Proactively share Trust & Security Centre link. Never wait for them to surface. |
| Finance / Procurement | TCO concerns, vendor risk, unfavourable contract terms | Strategic & Financial Approval (but can surface earlier in mature procurement orgs) | Treat Procurement as a partner from Internal Alignment onward. Provide compliance documents and TEI report upfront. Use standardised MSA. |
| Corporate Reliability | "Not in our standards" / "Not our approved vendor" | Strategic & Financial Approval | Align all messaging with ISO 55000 and the organisation's existing asset management strategy. Engage Corporate Reliability before the enterprise pitch. |
| Incumbent Sceptic | "We tried this before" / "I trust my experience over your AI" | Solution Exploration | Non-confrontational framing: "AND not OR." Reference the Complementary Detection Matrix. Position SAM4 as strengthening their strategy. |

---

## 4.0 Deal Motion: Land-and-Expand

### 4.1 The Land Motion (SAM4-X)

> SAM4-X is a paid validation programme optimised to produce portable proof and an internal champion. Revenue is a byproduct; fleet expansion is the goal.

**Typical deal:**

- 1–10 critical assets selected via Asset Criticality Analysis
- Installed in 1–2 days
- OpEx funded (often below tender threshold)
- 3–6 month engagement
- Dedicated customer success support
- Project-managed with executive check-ins

**Success criteria (defined upfront with customer):**

- **Technical:** Detect specified failure modes on target assets.
- **Operational:** Integrate alerts into existing CMMS workflow. Positive practitioner feedback.
- **Financial:** Develop ROI model based on actual catches and agreed downtime costs.
- **Scalability:** Document deployment playbook for replication at another site.

### 4.2 Expansion Triggers

If pilot success criteria are met, the following triggers activate the fleet conversation:

| Trigger Type | Example | Action |
|:---|:---|:---|
| Financial | Prevent one critical failure with documented ROI >10× pilot cost | Champion presents ROI case to Economic Buyer (Enterprise) |
| Operational | Achieve detection of specified faults with actionable lead time over 90 days | Technical Validator endorses fleet deployment |
| Strategic | Identify energy savings on a cohort of assets aligned with ESG targets | ESG / Energy Lead co-sponsors budget request |
| Contractual | Pilot contract includes a formal expansion review at defined milestone | Samotics AE facilitates review meeting with full committee |

### 4.3 The Expand Motion (Fleet Programs)

**Purpose:** Enterprise-wide deployment for long-term risk reduction and operational value.

**Typical deal:**

- 50–500+ assets deployed across multiple sites
- Phased rollout over 6–18 months
- CapEx or multi-site programme budget
- Full buying committee engaged
- Governed by Corporate Reliability standards

**Key differences from SAM4-X:**

- Procurement Gatekeeper heavily involved (vendor selection, MSA negotiation)
- IT/OT Gatekeeper conducts full security review
- Corporate Reliability sets deployment standards
- Enterprise Economic Buyer approves budget (not Plant Director)
- ROI model must be portable across sites

---

## 5.0 Universal Objections

| Objection | Likely Source(s) | Response |
|:---|:---|:---|
| "We already have condition monitoring" | Champion, Corporate Reliability | "SAM4 covers the failure modes and assets your existing programme cannot reach. This is completion, not replacement. See the Complementary Detection Matrix." |
| "ESA is not as accurate as vibration" | Technical Validator | "For mechanical faults, vibration is more applicable. For electrical faults and process loads, ESA is more sensitive. See the Measurement Definition Box (Buyer Journey Framework, Section 2.1) for how we define and validate accuracy." |
| "We tried ESA / MCSA before" | Technical Validator, Practitioner | "Legacy MCSA required a specialist per measurement. SAM4 applies AI across continuously monitored fleets, detecting cross-asset patterns at scale. Same physics — different operational model." |
| "What about false positives?" | Technical Validator, Practitioner | "Only validated findings are delivered. Every alert is reviewed by a Samotics diagnostics engineer. We track and report TP/FP rates as part of every engagement." |
| "Why trust a relatively small company?" | Economic Buyer, Procurement | "Enterprise readiness validated by the ABB strategic partnership. Proven at global scale. Reference customers available. Third-party ROI validation in progress." |
| "Another pilot that will not scale" | Economic Buyer (Enterprise), Corporate Reliability | "SAM4-X is not a generic pilot. Predefined success criteria, standardised ROI model, documented deployment playbook. Its primary deliverable is a repeatable template for enterprise rollout." |

---

## 6.0 Industry Buying Playbooks

Each playbook now includes a **Proof Readiness** indicator. This determines whether the vertical is ready for active marketing.

- **Green:** Flagship proof exists and is customer-approved for external use.
- **Yellow:** Partial proof exists (internal data, unnamed customer, or limited scope).
- **Red:** No proof. Do not lead marketing campaigns with this vertical until proof is created. Creating credibility debt is worse than a delayed launch.

### 6.1 Water & Wastewater — Proof Readiness: 🟢 GREEN

| Component | Detail |
|:---|:---|
| **Deal speed** | 6–18 months (AMP cycle dependent) |
| **Core trigger** | Unmonitored submerged pumps = unaddressed risk for pollution events and service interruptions |
| **Entry persona** | Asset Manager / Network Manager |
| **Killer message** | "The only proven monitoring for your most critical and inaccessible assets — your submerged pumps — to prevent pollution events and ensure regulatory compliance." |
| **Flagship proof** | Southern Water: prevented 3 critical failures, avoided major pollution event, saved £748,000. (Leads all campaigns.) **[Samotics-truth]** |
| **ROI model** | Cost of pollution fine + emergency crew dispatch + energy savings from pump optimisation |
| **Competitive position** | SAM4 vs. manual inspection / run-to-failure. Focus on cost/risk gap between proactive monitoring and reactive repairs. Safety benefits of remote monitoring. |
| **Buying dynamic** | AMP cycle driven. Procurement-heavy. Pilots often below tender threshold. |
| **Committee nuance** | Head of Compliance has significant influence due to regulatory pressure. Engage early with pollution prevention proof. |

### 6.2 Oil & Gas — Proof Readiness: 🔴 RED

| Component | Detail |
|:---|:---|
| **Deal speed** | 6–12 months |
| **Core trigger** | Safe-zone installation removes ATEX certification barriers. Critical asset risk (ESPs, compressors) where failure = production shutdown. |
| **Entry persona** | Reliability Lead |
| **Killer message** | "Monitor your most critical rotating equipment from the safe zone — no ATEX certification, no sensor exposure, no production disruption." |
| **Flagship proof** | **[MISSING — Highest-priority case study gap. Do not lead O&G campaigns until flagship proof exists.]** |
| **ROI model** | Production deferment cost/day × days of avoided downtime + reduced inspection frequency |
| **Competitive position** | SAM4 vs. traditional vibration with ATEX-certified sensors. Focus on installation barrier elimination and offshore hardware survival. |
| **Buying dynamic** | Reliability-led evaluation. Safety culture accelerates approval for non-intrusive solutions. |
| **Committee nuance** | HSE has significant influence. Safe-zone installation is a buying requirement, not a feature. |

### 6.3 Chemicals & Pharmaceuticals — Proof Readiness: 🔴 RED

| Component | Detail |
|:---|:---|
| **Deal speed** | 6–12 months |
| **Core trigger** | Batch integrity and clean-room uptime. MCC monitoring avoids sensor certification and decontamination downtime. |
| **Entry persona** | Plant Manager |
| **Killer message** | "Protect batch integrity and clean-room uptime with monitoring that never enters your process environment." |
| **Flagship proof** | **[MISSING — Need case study demonstrating batch protection or decontamination avoidance.]** |
| **ROI model** | Cost of batch loss + decontamination downtime + sensor certification costs avoided |
| **Competitive position** | SAM4 vs. sensor-based monitoring requiring process-area installation. Focus on contamination risk elimination. |
| **Committee nuance** | Quality Assurance (QA) may have significant veto power. Engage with contamination-free monitoring proof. |

### 6.4 Metals & Mining — Proof Readiness: 🔴 RED

| Component | Detail |
|:---|:---|
| **Deal speed** | 3–9 months |
| **Core trigger** | Extreme environments destroy conventional sensors. Ventilation = safety-critical. Production urgency in continuous operations. |
| **Entry persona** | Maintenance Superintendent |
| **Killer message** | "Monitor critical equipment in environments that destroy conventional sensors — from the safety of the MCC." |
| **Flagship proof** | **[MISSING — Need case study with harsh environment focus.]** |
| **ROI model** | Production loss/hour × avoided downtime + sensor replacement costs avoided |
| **Competitive position** | SAM4 vs. vibration sensors in extreme environments. Focus on sensor survival and maintenance access challenges. |
| **Committee nuance** | Production urgency can accelerate deals. Safety-critical ventilation systems may provide fastest entry point. |

### 6.5 Pulp & Paper — Proof Readiness: 🟡 YELLOW

| Component | Detail |
|:---|:---|
| **Deal speed** | 3–6 months |
| **Core trigger** | Energy optimisation and BEP correction across large motor fleets. Continuous operations with thin margins. |
| **Entry persona** | Mill Manager |
| **Killer message** | "Optimise energy consumption and protect production continuity across your entire motor fleet." |
| **Flagship proof** | **[PARTIAL — Energy data exists but no named, customer-approved case study for external use.]** |
| **ROI model** | Energy cost savings (kWh × tariff × hours) + avoided production downtime |
| **Competitive position** | Focus on energy value proposition alongside reliability. Energy angle often unlocks sustainability budget. |
| **Committee nuance** | ROI-driven, fast decisions. Mill Manager often has authority to approve pilot without extensive committee. |

### 6.6 Airports — Proof Readiness: 🟡 YELLOW

| Component | Detail |
|:---|:---|
| **Deal speed** | 6–12 months |
| **Core trigger** | Baggage system uptime. Fire-fighting and drainage pump reliability. Distributed motor fleets. |
| **Entry persona** | Asset / Baggage Systems Manager |
| **Killer message** | "Protect passenger experience and safety-critical systems with fleet-wide monitoring of your distributed motor assets." |
| **Flagship proof** | **[PARTIAL — Deployment data exists but no named case study for external use.]** |
| **ROI model** | Passenger disruption cost + SLA penalties + emergency repair costs |
| **Competitive position** | Focus on fleet coverage for distributed, hard-to-access assets. |
| **Committee nuance** | SLA-driven environment. Compliance with safety regulations (fire systems, drainage) can accelerate approval. |

---

## 7.0 Website & GTM Implications

### 7.1 Technical Credibility

Technical credibility within 30 seconds. Homepage and landing pages must immediately signal domain expertise, not generic SaaS messaging.

### 7.2 Champion Enablement

Every page must provide shareable proof assets. The Champion Enablement Kit (gated, for qualified leads) is the highest-priority content asset.

### 7.3 Security Visibility

Dedicated Trust & Security Centre. Public-facing. Certifications, architecture, data handling policies. Not hidden behind a form.

### 7.4 Industry Relevance

Industry pages lead with primary trigger and flagship proof. Only launch industry pages for verticals at Green or Yellow proof readiness. Red verticals get a placeholder page, not a campaign.

### 7.5 Motion-Based CTAs

Aligned to canonical buying motions (see Buyer Journey Framework, Section 0.0):

| CTA | Target | Buying Motion |
|:---|:---|:---|
| Calculate Your ROI | Champion, Economic Buyer | Problem Recognition |
| Get the Engineering Proof Pack | Technical Validator | Technical Validation |
| Schedule a Technical Deep-Dive | Technical Validator | Technical Validation |
| Request a Security Review | IT/OT Gatekeeper | Technical Validation |
| Book an Executive Briefing | Economic Buyer (Enterprise), CTO | Strategic & Financial Approval |
| Start Your Asset Audit | Champion, Economic Buyer (Plant) | Technical Validation |
| Build My Business Case | Champion | Internal Alignment |

### 7.6 ABB Partnership Positioning (Conditional)

ABB partnership positioning depends on the audience:

| Audience | ABB Positioning | Rationale |
|:---|:---|:---|
| Champion, Technical Validator | Secondary — lead with failure-mode logic and detection proof | These buyers care about technical capability, not vendor pedigree |
| Economic Buyer (Enterprise), CTO | Primary — lead with ABB partnership and enterprise credibility | These buyers need vendor viability signals early |
| Procurement Gatekeeper | Primary — include in vendor compliance pack | Procurement evaluates vendor risk; ABB signals stability |
| IT/OT Gatekeeper | Secondary — they care about security, not partnerships | Trust & Security Centre is their primary asset |

**Website implication:** ABB partnership appears on /about/ and /partners/ pages (accessible to all), and is prominently featured in executive-facing content and the Business Case Toolkit. It is not the homepage hero — the homepage leads with the problem and the detection capability.

### 7.7 Core Differentiator

Detection of both mechanical AND electrical faults must be prominent. The Complementary Detection Matrix should be accessible from every technology page.

---

## 8.0 Strategic Outcome

SAM4-X produces portable proof and internal champions that drive fleet expansion. Revenue is a byproduct of the land motion; enterprise scale is the goal.

Fleet Programs create the category and long-term enterprise scale.

The ICP ensures GTM resources are concentrated on accounts with the highest propensity to buy, renew, and expand.

The Buying Committee Map ensures every deal is multi-threaded across the full decision-making group, reducing the risk of single-point-of-failure champion dependency.

---

*End of document.*
