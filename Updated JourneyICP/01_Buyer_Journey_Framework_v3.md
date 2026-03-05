# SAMOTICS — Buyer Journey Framework (Version 3.1)

**Layered Detection & Reliability-Driven Buying Model**

Owner: Marketing + Sales
Version: 3.1
Date: March 2026
Dependencies: ICP & Buying Committee Map v3.1, User Journey Map v3.1

---

## What Changed and Why

**Structural changes (v3.0 → v3.1):**

1. **Locked a canonical Buying Motions list.** All three documents now reference a single "Buying Motions Canon" box with exact labels and a synonym blacklist. Eliminates prior drift where "Requirements Building," "Supplier Selection," "Consensus Creation," and "Validation" were used interchangeably with the canonical names.

2. **Added constraints and boundary conditions to the Detection Matrix.** The v3.0 matrix read like a brochure. Engineers will ask where ESA fails. Added a fourth column showing applicability constraints — VFDs, low load, MCC access, SNR — to increase trust by showing honest limits.

3. **Added Measurement Definition Box.** The "+90% detection accuracy" claim was a credibility risk without defining what is being measured, against what denominator, and how validation works. Defined TP/FP/FN, scope, audit method, and reporting cadence.

4. **Added exit criteria per buying motion.** The motions table previously mixed content strategy with sales process. Sales needs "this motion is complete when ___." Added an exit criterion per motion to make the framework AE-operational.

5. **Added qualification tests and "fast no" triggers per scenario.** Each scenario was well-described but gave sales no permission to walk away early. Added 3–4 qualifying questions and disqualifiers per scenario.

6. **Added role timing doctrine.** Role maps aligned across docs, but behaviour descriptions were inconsistent (e.g., Procurement as "late stage" vs. "engage early"). Added default first-touch timing, earliest veto stage, and early-involvement triggers per role.

7. **Added Proof System appendix.** The single biggest gap: repeated references to accuracy, TEI, case studies, validated findings, and diagnostics review without defining what counts as proof, who signs it off, or how it's packaged. Defined proof types, evidence hierarchy, measurement definitions, standard formats, and review owners.

8. **Fixed "68% of pilots fail" stat.** Replaced with Samotics-specific framing: "Scaling is the default failure mode in industrial AI. Our observed barriers are..." — more credible than an unsourced stat.

9. **Separated three types of truth.** All claims are now explicitly marked as: world-truth (industry-wide), Samotics-truth (proven in practice), or design-intent (what we're building toward but haven't yet validated).

**Prior v3.0 changes (retained):**

- RCM-first framing (failure-mode-driven, not technology-first)
- Non-linear buying motions replacing linear funnel
- Expanded buying committee (8 roles)
- 8 buying scenarios
- Phased time-to-value model (30 / 30–90 / 90+ days)
- Pilot-to-enterprise deployment model

---

## 0.0 Buying Motions Canon

> **These six labels are canonical.** Use them verbatim across all Samotics GTM documents, CRM stages, content tags, and sales playbooks. Do not use synonyms.

| # | Canonical Name | Key Question |
|:---|:---|:---|
| 1 | **Problem Recognition** | "Is this problem urgent and expensive enough to solve now?" |
| 2 | **Solution Exploration** | "What are the credible ways to solve this?" |
| 3 | **Internal Alignment** | "How do I get my colleagues to agree this is the right approach?" |
| 4 | **Technical Validation** | "Will this actually work on our specific assets and in our workflow?" |
| 5 | **Strategic & Financial Approval** | "Does this align with our strategy and is the business case solid?" |
| 6 | **Deployment Confidence** | "How can we be sure this will not be a painful implementation?" |

**Synonym blacklist — do not use these terms as stage names:**

- ~~Requirements Building~~ → use Internal Alignment or Technical Validation
- ~~Supplier Selection~~ → use Technical Validation
- ~~Validation~~ (standalone) → use Technical Validation
- ~~Consensus Creation~~ → use Internal Alignment (early) or Strategic & Financial Approval (late)
- ~~Strategic Approval~~ (without "& Financial") → use Strategic & Financial Approval

---

## 0.1 SAM4-X Canonical Positioning

> **SAM4-X is a paid validation programme optimised to produce portable proof and an internal champion. Revenue is a byproduct; fleet expansion is the goal.**

SAM4-X is not "a pilot." It differs from a generic pilot in four ways:

| Dimension | Generic Pilot | SAM4-X |
|:---|:---|:---|
| **Primary goal** | Prove tech works | Produce proof + champion + expansion-ready playbook |
| **Scope** | Flexible | 1–10 critical assets selected via Asset Criticality Analysis |
| **Deliverables** | Report | Standardised ROI model, deployment playbook, champion materials |
| **Exit** | "Was it successful?" | Predefined success criteria that trigger a formal expansion review |
| **Governance** | Ad hoc | Project-managed with executive check-ins and CS support |

---

## 0.2 Three Types of Truth

All claims in this framework are marked by evidence tier:

| Marker | Meaning | Example |
|:---|:---|:---|
| **[World-truth]** | Industry-wide fact, independently verifiable | "Enterprise buying committees typically involve 8–13 stakeholders" |
| **[Samotics-truth]** | Proven in Samotics operations, verifiable by reference customers | "Southern Water: prevented 3 critical failures, saved £748,000" |
| **[Design-intent]** | What we're building toward but have not yet independently validated | "+90% detection accuracy across all fault classes" (see Measurement Box) |

Where a claim appears without a marker, assume [Samotics-truth] — it reflects current operational reality but has not been independently audited.

---

## 1.0 Governing Principle: Failure-Mode-Driven Technology Selection

The only defensible reason to adopt a new monitoring technology is that it is the most effective and applicable method for detecting a high-consequence failure mode that current strategies cannot adequately address.

All technology decisions in this framework follow Reliability-Centered Maintenance (RCM) logic: **[World-truth]**

> **Function → Functional Failure → Failure Mode → Failure Effect → Consequence → Select Detection Method**

SAM4 (Electrical Signature Analysis) is not a replacement for vibration analysis. It is a different technology, sensitive to different physical phenomena. Its value is realised when applied to failure modes for which it is the most effective detection method.

This framework does not start with SAM4. It starts with the failure modes your current programme cannot detect.

---

## 2.0 Complementary Detection Matrix

A world-class reliability programme layers technologies to cover the full range of high-consequence failure modes. ESA and Vibration Analysis are complementary, not competitive. **[World-truth]**

| Failure Mode | Primary Detection Method | Rationale | Applicability Constraints / Boundary Conditions |
|:---|:---|:---|:---|
| Mechanical imbalance, misalignment, looseness | **Vibration Analysis** | Classic mechanical faults with clear low-frequency vibration signatures. Vibration is the most direct detection method. | Vibration: requires sensor access to asset. ESA has limited sensitivity to these mechanical faults — do not position ESA here. |
| Bearing wear (late stage) | **Vibration Analysis** | Degraded bearings generate distinct high-frequency vibration signals. Industry standard. | Vibration: requires physical sensor; compromised in submersed/inaccessible assets. ESA detects only late-stage bearing degradation through load changes. |
| Broken rotor bars, end ring faults | **Electrical Signature Analysis** | Electrical faults create torque pulsations and magnetic field changes directly detectable in current/voltage signatures. Vibration detects these only in very late stages, if at all. | ESA: requires access to MCC. Detection sensitivity reduced with VFDs (variable frequency drives) due to spectral contamination. Low-load conditions (<30% rated) reduce signal-to-noise ratio. |
| Stator winding faults (insulation breakdown) | **Electrical Signature Analysis** | ESA detects subtle signature changes from turn-to-turn shorts or insulation degradation long before ground fault or catastrophic failure. | ESA: VFDs with active front ends can mask stator fault signatures. Very early-stage inter-turn faults may be below detection threshold in high-noise environments. |
| Static / dynamic eccentricity | **Electrical Signature Analysis** | Uneven air gap directly impacts the magnetic field, creating clear and early electrical signatures. | ESA: requires motor nameplate data for accurate diagnosis. Sensitivity reduced in slip-ring motors and some wound-rotor designs. |
| Process-driven faults (cavitation, blockage) | **Both (complementary)** | ESA detects load and torque changes. Vibration detects high-frequency cavitation energy. Together they provide confirmation and a fuller picture. | ESA: detects process anomalies via load change — but cannot distinguish between cavitation and other load-change causes without vibration or process data for confirmation. |
| Early-stage bearing wear | **Both (complementary)** | ESA can detect increased load and friction before clear vibration signatures develop. Vibration excels at diagnosing the specific bearing fault as it progresses. | ESA: bearing detection via load signature is probabilistic in early stages, not deterministic. False negatives are possible for bearings under variable process loads. Vibration remains the gold standard for bearing fault classification. |

**What ESA does not do well (honest boundaries):**

- ESA is not a replacement for vibration on mechanical faults where vibration has a direct physical measurement path.
- VFDs significantly reduce ESA's diagnostic accuracy for certain fault types. Samotics has developed VFD-specific algorithms, but detection envelopes are narrower than for direct-on-line motors. **[Design-intent: VFD algorithm maturity is advancing but not yet at parity with DOL detection.]**
- MCC access is mandatory. If the motor control cabinet is not physically accessible or not wired for current/voltage measurement, ESA cannot be deployed.

---

### 2.1 Measurement Definition Box

> **How Samotics defines and validates detection performance** **[Samotics-truth — subject to independent audit]**

| Term | Definition |
|:---|:---|
| **True Positive (TP)** | An alert issued by SAM4 that is confirmed by the customer (via inspection, repair, or post-mortem) as a real fault or developing fault. |
| **False Positive (FP)** | An alert issued by SAM4 that, upon investigation, does not correspond to a real fault. |
| **False Negative (FN)** | A fault that occurred on a monitored asset but was not flagged by SAM4 before failure. |
| **Detection Accuracy** | TP / (TP + FP) for delivered alerts. Note: this measures precision of delivered findings, not recall across all possible faults. |
| **Lead Time** | Time between the first SAM4 alert and the point at which the fault would have caused unplanned downtime (as estimated by the customer's maintenance team). |

**Scope of "+90% detection accuracy" claim:**

- Measured across validated findings delivered to customers (i.e., after Samotics diagnostics engineer review, not raw algorithmic output).
- Denominator: all findings delivered to customers in the measurement period.
- Fault classes included: electrical faults (rotor, stator, eccentricity), process faults (cavitation, blockage), and load anomalies. Mechanical-only faults (pure imbalance, misalignment) are not included — these are vibration's domain.
- This figure is a Samotics internal measurement. **[Design-intent: commission an independent audit or Forrester TEI to convert this to third-party validated.]**

**Validation method:**

- Every finding is reviewed by a Samotics diagnostics engineer before delivery.
- Customer confirmation is tracked for all delivered findings.
- TP/FP rates are reported as part of pilot success criteria.
- FN tracking depends on customer reporting of undetected failures.

---

## 3.0 The Enterprise Buying Committee

Enterprise decisions are made by committees, not individuals. A typical deal involves 8–13 stakeholders. **[World-truth]** The framework below maps the roles Samotics must engage to close and scale.

### 3.1 Role Map with Timing Doctrine

| Role | Typical Title(s) | Primary Concern | Core Question | Enablement Asset | Default First Touch | Earliest Veto Stage | Trigger for Early Involvement |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **Champion** | Reliability Manager, Maintenance Superintendent | Solving recurring failures, building career credibility | "Does this solve a problem I cannot solve now, and can I prove its value internally?" | Champion Enablement Kit | Problem Recognition | N/A (advocate, not veto) | Always engaged first |
| **Technical Validator** | Maintenance / Reliability Engineer, CBM Analyst | Data quality, workflow fit, diagnostic depth | "Show me the raw data. How does this compare to our existing systems?" | Detection matrix, engineering FAQ, diagnostic example pack, architecture diagram | Solution Exploration | Internal Alignment | Champion delegates technical evaluation |
| **Economic Buyer (Plant)** | Plant Director, Operations Manager | Production targets, plant-level budget, risk profile | "Will this pilot be safe, non-disruptive, and deliver a clear return for my plant?" | Validated ROI model, deployment timeline, production impact analysis | Internal Alignment | Technical Validation | Champion needs budget approval for pilot |
| **Economic Buyer (Enterprise)** | VP Operations, VP Reliability, CTO | Enterprise-wide value, scalability, strategic alignment | "Can you show me a repeatable model for deployment and ROI across all our sites?" | Enterprise business case, multi-site deployment playbook, executive briefing | Strategic & Financial Approval | Strategic & Financial Approval | Fleet expansion discussion begins |
| **IT/OT Gatekeeper** | CISO, Dir. of IT, Head of OT Security | Cybersecurity, data governance, network architecture | "What data do you collect, where is it stored, and how does it integrate with our infrastructure?" | Trust & Security Centre, integration documentation | **Proactive: first follow-up** | **Any stage — can kill at any time** | Always. Do not wait for them to surface. Send Trust & Security Centre link in first follow-up email. |
| **Procurement Gatekeeper** | Procurement / Sourcing Manager | Commercial terms, TCO, vendor compliance | "How does pricing compare? What are total lifetime costs? Do you comply with our MSA?" | Standardised MSA, TCO comparison, vendor compliance documentation | Internal Alignment (for Fleet); may be bypassed for SAM4-X below tender threshold | Strategic & Financial Approval | Deal value exceeds tender threshold; multi-year term; enterprise MSA required |
| **Corporate Reliability / Asset Management** | VP Asset Management, Global Reliability Director | Standards, cross-site consistency, strategic fit | "How does this fit our corporate asset management strategy and ISO 55000 framework?" | Multi-site results summary, standards alignment brief, deployment playbook | Strategic & Financial Approval | Strategic & Financial Approval | Fleet expansion or enterprise standardisation discussion |
| **Practitioner** | Maintenance Technician, Operator | Day-to-day usability, alert reliability | "Will this make my job easier or harder? Can I trust the alerts?" | Live product demo, install sheet, after-alert playbook | Technical Validation (pilot phase) | Deployment Confidence | Pilot installation begins |

### 3.2 Champion Creation Mechanics

Champions are not found — they are made.

1. **Identify.** Look for individuals with high personal pain (recurring failures, missed KPIs) and organisational influence (trusted by directors, cross-departmental relationships).
2. **Test.** Assign a small but meaningful task: "Can you get us the failure data for the last 12 months on Asset X?" Willingness and ability to complete it proves commitment.
3. **Equip.** Grant access to the Champion Enablement Kit. Make it easy for them to sell internally: pre-built business case, ROI calculator, internal presentation deck, competitive positioning, security FAQ.

### 3.3 Veto Dynamics

| Veto Source | Primary Blocker | Default Timing | Mitigation |
|:---|:---|:---|:---|
| IT/OT Security | Data sovereignty, network risk, cloud resistance | **Any stage** | Engage in first follow-up. Proactively provide Trust & Security Centre. Never wait for them to ask. |
| Finance / Procurement | TCO concerns, vendor risk, contract terms | Strategic & Financial Approval (but can surface earlier in mature procurement orgs) | Treat Procurement as a partner from Internal Alignment onward. Provide all compliance documents and TEI report upfront. Use standardised MSA. |
| Corporate Reliability | "Not in our standards" | Strategic & Financial Approval | Align messaging with ISO 55000 and the organisation's existing asset management strategy. Engage before the enterprise pitch. |
| Incumbent Sceptic | "We tried this before" / "I trust my experience" | Solution Exploration | Non-confrontational: "AND not OR." ESA completes their strategy, it does not replace it. Reference the Detection Matrix. |

---

## 4.0 The Buying Journey: Six Buying Motions

The buying process is not a linear funnel. It is a series of six parallel motions that the committee completes in loops. Deals stall when a motion is unsupported.

These motions are adapted from Gartner's buying jobs framework. Labels are canonical — see Section 0.0.

| Buying Motion | Key Question | Samotics Play | Primary Stakeholders | Exit Criterion |
|:---|:---|:---|:---|:---|
| **1. Problem Recognition** | "Is this problem urgent and expensive enough to solve now?" | Lead with cost-of-inaction data. Industry benchmarks on downtime cost, energy waste, and failure frequency. ROI calculator as first-touch asset. | Champion, Economic Buyer (Plant) | Champion confirms: "We have a quantified problem worth solving, and I have internal support to explore solutions." |
| **2. Solution Exploration** | "What are the credible ways to solve this?" | Define the category. Explain ESA vs. vibration vs. thermal. Position layered detection as the standard. Use "SAM4 + Vibration" framing, never "SAM4 vs. Vibration." | Champion, Technical Validator | Champion and Technical Validator agree: "ESA is a credible approach for the failure modes we care about. We want to evaluate Samotics specifically." |
| **3. Internal Alignment** | "How do I get my colleagues to agree this is the right approach?" | Equip the Champion with the Champion Enablement Kit. Co-author requirements with the Champion. Ensure SAM4's unique strengths (safe-zone installation, electrical fault detection, fleet scalability) appear as criteria. Provide spec sheets, integration guides, architecture diagrams. | Champion, Technical Validator, IT/OT Gatekeeper | Champion confirms: "I have buy-in from my direct manager and IT/OT has no blocking objections. We can proceed to a formal evaluation or pilot." |
| **4. Technical Validation** | "Will this actually work on our specific assets and in our workflow?" | Industry-specific case studies. Detection matrix. Proactive security documentation. Execute SAM4-X programme: formal, project-managed engagement with predefined success criteria. | Technical Validator, Economic Buyer (Plant), Practitioner, IT/OT Gatekeeper, Procurement | Technical Validator confirms: "SAM4 detected [specific faults] on our assets with [lead time]. It integrates with our workflow. I endorse expansion." |
| **5. Strategic & Financial Approval** | "Does this align with our strategy and is the business case solid?" | Executive briefing. Enterprise-grade proof. Help the Champion prepare for CFO and Procurement review. Provide Business Case Toolkit and TEI report. | Economic Buyer (Enterprise), Corporate Reliability, Procurement, IT/OT Gatekeeper | Economic Buyer (Enterprise) confirms: "The business case meets our ROI threshold, and Procurement has no blocking concerns. We approve the budget." |
| **6. Deployment Confidence** | "How can we be sure this will not be a painful implementation?" | Shift from selling to consulting. Provide implementation playbook, customer success stories, support SLAs. Help the Champion navigate remaining internal politics. Address all remaining stakeholder concerns. | All roles — Champion leads internally | All stakeholders confirm: "We understand the deployment plan, timeline, and support model. We are ready to sign." |

### 4.1 Objection Handling by Buying Motion

| Objection | Likely Source | Buying Motion | Response |
|:---|:---|:---|:---|
| "We already have condition monitoring" | Champion, Corporate Reliability | Solution Exploration | "Exactly. SAM4 covers the failure modes and assets your existing programme cannot reach. See the Detection Matrix — this is completion, not replacement." |
| "ESA is not as accurate as vibration" | Technical Validator | Internal Alignment | "For mechanical faults, vibration is more applicable. For electrical faults and process-driven loads, ESA is more sensitive. See the Measurement Definition Box for how we define and validate accuracy." |
| "We tried ESA / MCSA before" | Technical Validator, Incumbent Sceptic | Solution Exploration | "Legacy MCSA required a specialist to interpret individual measurements. SAM4 applies AI across continuously monitored fleets, detecting cross-asset patterns no human can recognise at scale. Same physics — completely different operational model." |
| "Why trust a relatively small company?" | Economic Buyer, Procurement | Strategic & Financial Approval | "Enterprise readiness validated by the ABB strategic partnership. Proven at global scale with leading utilities. Reference customers available. Request a third-party validated ROI study or speak directly to customers." |
| "Another pilot that will not scale" | Economic Buyer (Enterprise), Corporate Reliability | Deployment Confidence | "SAM4-X is not a generic pilot. It has predefined success criteria, a standardised ROI model, and a documented deployment playbook. Its primary deliverable is a repeatable template for enterprise rollout." |
| "What about false positives?" | Technical Validator, Practitioner | Technical Validation | "Only validated findings are delivered. Every alert is reviewed by a Samotics diagnostics engineer. We track and report TP/FP rates as part of every engagement. See the Measurement Definition Box." |

---

## 5.0 Strategic Buying Scenarios

Eight entry scenarios that drive SAM4 demand. Each maps to the buying committee and buying motions above.

Each scenario now includes qualification tests — questions that confirm the scenario is real and actionable — and "fast no" triggers that signal Samotics should deprioritise.

### Scenario 1: Critical Asset Failure (Reactive)

**Trigger:** A recent, costly, unexpected failure of a critical asset — often one already monitored by vibration.

**Mindset:** "Our existing system missed this. What else are we blind to?"

**Strategic logic:** The cost of the failure provides immediate, undeniable justification for a complementary detection layer.

**Active committee:** Champion (defines failure history), Technical Validator (validates detection gap), Economic Buyer — Plant (approves based on downtime cost).

**Deal dynamic:** Fast approval cycle. Emotional urgency. Risk: urgency fades if not captured within 60 days.

**Proof required:** Detection matrix showing fault types missed by current system. Case study with comparable asset and failure mode. Quantified avoided downtime.

**Qualification tests:**

- Was the failure on a motor-driven asset where ESA would have had a detection path?
- Can the customer quantify the cost of the failure (downtime, repair, consequential damage)?
- Is there an identifiable champion who owns the failure analysis or corrective action?
- Is there budget or willingness to fund a pilot within the current quarter?

**Fast no triggers:**

- Failure was on a non-motor asset (e.g., piping, structural) — ESA has no detection path.
- Organisation has already committed to a different corrective action (e.g., redundancy, redesign).
- No identifiable champion — incident is being managed by committee with no single owner.

---

### Scenario 2: Detection Completion (Strategic)

**Trigger:** A formal FMEA or RCM analysis reveals that high-consequence electrical failure modes are not being detected by the current CBM programme.

**Mindset:** "We are data-driven. Our analysis shows a gap in our detection strategy for critical assets."

**Strategic logic:** Proactive, risk-based decision by a mature reliability organisation. Investment justified by formal risk assessment and ISO 55000 alignment.

**Active committee:** Champion (owns the analysis), Technical Validator (validates complementary value), Corporate Reliability (approves strategic fit), Economic Buyer — Enterprise (funds from reliability budget).

**Deal dynamic:** Slower but higher-value. Committee-driven. Requires alignment with corporate standards.

**Proof required:** Complementary Detection Matrix. Parallel deployment case studies. Alignment with ISO 55000 and existing asset management strategy.

**Qualification tests:**

- Has the organisation completed a formal FMEA or RCM analysis that identified electrical fault gaps?
- Is there a corporate reliability function that sets standards for monitoring technologies?
- Does the organisation have experience with condition-based maintenance (not starting from zero)?
- Is there budget allocated for reliability programme expansion (not competing with a different initiative)?

**Fast no triggers:**

- Organisation has no formal maintenance strategy — run-to-failure dominant.
- FMEA identified gaps, but the corrective action was "accept risk" — no appetite for investment.
- Corporate Reliability has already standardised on a competitor for the electrical layer.

---

### Scenario 3: Coverage Gap — Unreachable Assets (Strategic)

**Trigger:** 30–40% of assets are unmonitored because they are physically inaccessible, in hazardous zones, or too numerous for cost-effective sensor deployment.

**Mindset:** "We have a massive blind spot. How do we get visibility without a huge capital investment?"

**Strategic logic:** ESA's ability to monitor from the motor control cabinet (MCC) provides a cost-effective way to close this gap.

**Active committee:** Champion (quantifies the gap), Technical Validator (validates MCC-based approach), Economic Buyer — Plant (approves based on risk reduction).

**Deal dynamic:** Strong initial momentum. Scales naturally as coverage gap is quantified across sites.

**Proof required:** Fleet deployment case studies. Installation demonstration (sub-30-minute, MCC-based). Energy and operational baselines from first 30 days.

**Qualification tests:**

- Can the customer quantify the number and criticality of unmonitored assets?
- Are the unmonitored assets motor-driven (not, e.g., passive heat exchangers or piping)?
- Is MCC access available for those assets?
- Is there a risk or compliance driver for monitoring these assets (not just "nice to have")?

**Fast no triggers:**

- Unmonitored assets are not motor-driven — ESA does not apply.
- MCC access is unavailable or would require significant infrastructure modification.
- Customer is looking for a comprehensive IIoT platform, not a focused monitoring solution — scope mismatch.

---

### Scenario 4: Energy & Efficiency Mandate

**Trigger:** Corporate ESG targets, energy cost pressure, or sustainability reporting requirements create a mandate to optimise motor-driven systems.

**Mindset:** "We need to reduce energy consumption and prove it in our ESG framework."

**Strategic logic:** SAM4 provides continuous energy monitoring and BEP analysis across motor fleets. Budget unlocked via ESG or energy programmes.

**Active committee:** ESG / Energy Lead (budget co-owner), Champion (programme owner), Economic Buyer — Enterprise (approves based on ESG targets).

**Deal dynamic:** Budget often ring-fenced and easier to access. Requires energy data integration with ESG reporting.

**Proof required:** Energy baseline and optimisation data. Reportable emissions reduction. Case studies with quantified energy savings.

**Qualification tests:**

- Does the organisation have a quantified energy reduction target for motor-driven systems?
- Is there a dedicated ESG or energy budget (separate from maintenance)?
- Does the customer have energy metering infrastructure, or will SAM4 be the primary energy data source?
- Is there a reporting requirement (e.g., CSRD, SECR) that this data would feed?

**Fast no triggers:**

- Energy is a "nice to have" with no budget or reporting mandate behind it.
- Organisation is looking for a full energy management platform (BMS-level), not asset-level monitoring.
- Motor fleet is too small (<50 assets) to generate meaningful aggregate energy insights.

---

### Scenario 5: Partner-Led

**Trigger:** ABB, a system integrator, or an existing technology partner recommends SAM4 as a complementary monitoring layer.

**Mindset:** "Our trusted partner says this fills a gap. Show us."

**Strategic logic:** Partner credibility accelerates trust-building. Shortens early buying motions (Problem Recognition and Solution Exploration already completed by partner).

**Active committee:** Champion (introduced by partner), Technical Validator, IT/OT Gatekeeper (integration with partner's systems).

**Deal dynamic:** Accelerated. Entry point is mid-journey. Risk: dependency on partner's sales cycle.

**Proof required:** Joint case studies with partner. Integration architecture. Partner endorsement materials.

**Qualification tests:**

- Is the partner actively engaged in the account (not just a name-drop)?
- Has the partner identified a specific use case or asset class?
- Does the customer have a pre-existing relationship with Samotics' partner ecosystem?

**Fast no triggers:**

- Partner relationship is nominal — no active engagement or joint selling.
- Customer is evaluating the partner's own monitoring solution as a direct competitor to SAM4.

---

### Scenario 6: Regulatory & Insurance Mandate (Compliance-Driven)

**Trigger:** A new regulation or industrial insurer requires proof of asset integrity for a specific equipment class.

**Mindset:** "We must comply. What is the most efficient way to meet this requirement and document it?"

**Strategic logic:** Cost of non-compliance makes the investment non-negotiable. Focus is on auditable monitoring.

**Active committee:** Champion (identifies compliance gap), Corporate Reliability (defines standards), Procurement (manages vendor compliance), Economic Buyer — Enterprise (approves based on compliance risk).

**Deal dynamic:** Non-discretionary spend. Fast once the regulatory driver is confirmed. Procurement-heavy.

**Proof required:** Compliance alignment documentation. Audit trail capabilities. Regulatory case studies.

**Qualification tests:**

- Is there a specific, documented regulatory or insurance requirement?
- Does the requirement apply to motor-driven assets specifically?
- Is there a compliance deadline creating urgency?
- Has the organisation budgeted for compliance remediation?

**Fast no triggers:**

- Regulatory requirement is vague or aspirational — no enforcement timeline.
- Requirement can be met by existing monitoring infrastructure — no gap for ESA.
- Organisation is contesting the regulation rather than complying.

---

### Scenario 7: Technology Refresh / Obsolescence

**Trigger:** An existing condition monitoring system is aging, unsupported, or too costly to maintain.

**Mindset:** "Our current system is end-of-life. We need to modernise without losing detection capability."

**Strategic logic:** The refresh cycle creates a natural buying window. SAM4 can be positioned as the electrical layer in a modernised detection stack.

**Active committee:** Champion (defines replacement requirements), Technical Validator (validates against current system), IT/OT Gatekeeper (integration with new architecture), Procurement (manages vendor selection).

**Deal dynamic:** Competitive evaluation. Requires clear differentiation on detection capability.

**Proof required:** Head-to-head detection comparison. Integration with modern platforms. Migration plan from legacy system.

**Qualification tests:**

- Is the existing system genuinely end-of-life (not just underperforming)?
- Is the customer evaluating ESA specifically, or a broad replacement platform?
- Is there a defined refresh timeline and budget?
- Does the customer accept a layered approach (ESA + vibration), or are they looking for a single-vendor replacement?

**Fast no triggers:**

- Customer wants a single-vendor, all-in-one replacement — SAM4 is a layer, not a platform.
- Refresh budget has already been allocated to a competitor.
- Existing system is a direct ESA competitor (rare, but possible).

---

### Scenario 8: M&A Due Diligence / Integration

**Trigger:** Company acquires a new facility and needs to rapidly assess asset health and hidden liabilities.

**Mindset:** "What are we buying? What is the hidden risk in this facility's assets?"

**Strategic logic:** Rapid, non-intrusive monitoring deployment provides data for financial valuation and post-merger integration.

**Active committee:** Corporate Reliability (defines assessment standards), Economic Buyer — Enterprise (justifies based on acquisition risk), Technical Validator (executes rapid assessment).

**Deal dynamic:** Time-pressured. Budget justified by acquisition value. Short engagement, can seed fleet deployment.

**Proof required:** Rapid deployment case studies. Asset health assessment reports. Integration with corporate standards.

**Qualification tests:**

- Is the acquisition confirmed or highly probable (not exploratory)?
- Are the acquired assets motor-driven and significant in number?
- Is there a defined due diligence timeline?
- Will the acquiring company have MCC access during due diligence?

**Fast no triggers:**

- Acquisition is speculative — no committed timeline.
- Acquired facility has minimal motor fleet.
- Due diligence is focused on non-asset factors (financial, legal, HR).

---

## 6.0 Phased Time-to-Value Model

Value delivery follows three distinct phases. Each phase serves a different audience and builds toward quantifiable ROI. **[Samotics-truth]**

### Phase 1: Operational Baseline (First 30 Days)

**Value delivered:** Installation validation. Asset load profiling. Energy consumption baseline. Identification of gross operational issues (severe voltage imbalance, phase issues).

**Audience:** Technical Validator, Practitioner.

**What this is:** Proof the system works and immediate operational visibility.

**What this is not:** Predictive maintenance. Do not claim ROI at this stage.

### Phase 2: Anomaly Detection & Performance Insights (30–90 Days)

**Value delivered:** Detection of anomalous behaviour. Performance deviations from baseline. Developing faults flagged with actionable recommendations.

**Audience:** Champion, Practitioner, Economic Buyer (Plant).

**What this is:** Early detection signals and maintenance planning inputs.

**What this is not:** Full predictive ROI. Lead times on specific failure modes are still building.

### Phase 3: Predictive ROI & Risk Reduction (90+ Days)

**Value delivered:** Early detection of specific, high-consequence failure modes with sufficient lead time to plan corrective action and avoid failure. Quantifiable avoided downtime and cost savings.

**Audience:** Economic Buyer (Plant), Economic Buyer (Enterprise), Corporate Reliability, Finance.

**What this is:** The defensible business case for enterprise scale.

### ROI Calculation Framework

The business case is built on a simple, agreed-upon formula:

**ROI = (Quantified Value of Avoided Failures + Energy Savings) − Total Cost of Ownership**

Where:

- **Avoided Failures** = Σ [(Cost of Downtime/hr) × (Production Hours Saved) + (Cost of Reactive Repair) − (Cost of Planned Repair)] for each validated catch
- **Energy Savings** = Measured improvement in operational efficiency × energy cost per kWh × hours
- **Total Cost of Ownership** = Subscription fees + installation costs + training + internal labour

---

## 7.0 From Pilot to Enterprise Standard

Scaling is the default failure mode in industrial AI. The most common barriers Samotics has observed in customer deployments are: non-portable data pipelines, lack of a standardised ROI baseline, no clear ownership of the outcome, and pilot scope that was too narrow to generate compelling proof. **[Samotics-truth]**

This deployment model is designed to prevent pilot purgatory.

### Phase 1: Strategic Pilot (SAM4-X) (3–6 Months)

**Goal:** Prove technical viability AND create a repeatable deployment playbook.

**Asset selection:** 1–10 assets chosen via formal Asset Criticality Analysis. Mix of asset types and known failure modes.

**Success criteria (defined upfront — see SAM4-X Canonical Positioning, Section 0.1):**

- **Technical:** Detect X specified failure modes with Y lead time vs. existing methods.
- **Operational:** Integrate alerts into existing CMMS workflow. Positive practitioner feedback.
- **Financial:** Develop standardised ROI model based on actual catches and agreed downtime costs.
- **Scalability:** Document a playbook for data integration, installation, and training that another plant can execute.

**Team:** Cross-functional — Reliability, Maintenance, IT/OT, Operations.

### Phase 2: Multi-Site Validation (6–12 Months)

**Goal:** Prove the playbook is repeatable and the ROI model holds across sites.

**Action:** Replicate the pilot at 2–3 additional, diverse plants using the Phase 1 playbook.

**Refine:** Update playbook and ROI model with lessons learned.

**Build the enterprise case:** Consolidate results into a single business case for enterprise decision-makers.

### Phase 3: Enterprise Rollout (Ongoing)

**Goal:** Establish the technology as a corporate standard.

**Action:** Phased rollout across all high-criticality assets, governed by Corporate Reliability.

**Ownership:** Corporate Reliability owns the global standard. Plant Managers own site deployment.

**Measure:** Enterprise-wide metrics on uptime, maintenance cost reduction, energy savings, and safety improvement.

---

## 8.0 Strategic Positioning

Best-in-class reliability programmes do not choose one detection method. They build layered detection strategies driven by risk and rooted in RCM. **[World-truth]**

SAM4 adds the electrical intelligence layer that existing mechanical monitoring systems cannot provide. **[Samotics-truth]**

For your most critical assets, a single detection method is a single point of failure.

This framework is designed to move those assets from monitored to fully protected.

---

## 9.0 Content & Proof Requirements Summary

| Asset | Purpose | Buying Motion Served | Priority |
|:---|:---|:---|:---|
| Complementary Detection Matrix | Technical credibility with Validators | Solution Exploration, Technical Validation | Critical — must exist at launch |
| Champion Enablement Kit | Internal selling by Champions | Internal Alignment | Critical — highest content priority |
| Trust & Security Centre | De-risk IT/OT veto | Technical Validation, Strategic & Financial Approval | Critical — engage in first follow-up |
| Industry-specific case studies (per vertical) | Technical Validation proof | Technical Validation | High — start with strongest vertical |
| ROI calculator | Self-service business case input | Problem Recognition, Internal Alignment | High — interactive, self-service |
| Third-party validated ROI study (e.g., Forrester TEI) | Financial Approver credibility | Strategic & Financial Approval | High — commission if not available |
| Standardised MSA | Reduce Procurement friction | Strategic & Financial Approval | Medium — accelerates contracting |
| Deployment playbook (public version) | Deployment confidence | Deployment Confidence | Medium — differentiator vs. competitors |
| "Why best-in-class plants still add SAM4" narrative | Overcome incumbent resistance | Solution Exploration | Medium — supports Detection Completion scenario |
| Multi-site results summary | Enterprise scale proof | Strategic & Financial Approval | Medium — builds over time from deployments |

---

## Appendix A: Samotics Proof System

> **Shared reference for all GTM documents. Defines what counts as proof, how it's validated, and how it's packaged.**

### A.1 Proof Types

| Proof Type | What It Proves | Example |
|:---|:---|:---|
| **Technical** | Detection capability, accuracy, diagnostic depth | Detection matrix, diagnostic example pack, measurement definitions |
| **Financial** | ROI, cost avoidance, energy savings | ROI calculator output, validated catch reports, TEI report |
| **Operational** | Workflow fit, usability, adoption | Practitioner feedback, CMMS integration confirmation, after-alert playbook |
| **Security** | Data protection, compliance, architecture safety | Trust & Security Centre, SOC 2 report, penetration test summary |

### A.2 Evidence Hierarchy

Listed from weakest to strongest. Higher tiers are more persuasive and should be prioritised for high-value deals.

| Tier | Evidence Type | Credibility | Example |
|:---|:---|:---|:---|
| 1 | **Anecdote** | Low — self-asserted, unverifiable | "A customer told us they saved money." |
| 2 | **Internal case study** | Medium — Samotics-authored, customer-approved | "Southern Water: prevented 3 critical failures, saved £748,000." |
| 3 | **Customer-attributed quote** | Medium-High — customer speaks in their own voice | Named customer testimonial on website or in reference call. |
| 4 | **Audited case study** | High — independently verified data | Case study with independently audited financial outcomes. |
| 5 | **Third-party validated study** | Highest — independent methodology | Forrester TEI, independent research study, peer-reviewed publication. |

**Current state [Samotics-truth]:** Most Samotics proof is at Tier 2 (internal case studies). Tier 5 (third-party validation) is a **[Design-intent]** priority.

### A.3 Standard Proof Formats

| Format | Audience | Contents | Length |
|:---|:---|:---|:---|
| **1-Page Catch Summary** | Champion (for internal sharing) | Asset, fault detected, lead time, action taken, cost avoided | 1 page |
| **Technical Proof Pack** | Technical Validator | Detection matrix, 3–5 diagnostic examples, engineering FAQ, architecture diagram | 5–10 pages |
| **Executive Proof Pack** | Economic Buyer (Enterprise), CTO | ROI model, fleet-scale results, deployment playbook summary, ABB partnership | 3–5 pages |
| **Security Proof Pack** | IT/OT Gatekeeper | Trust & Security Centre summary, certifications, architecture, data handling, pen test summary | 3–5 pages |
| **Business Case Toolkit** | Champion (for CFO/Procurement) | ROI calculator, business case template, TEI report (if available), internal presentation deck | Bundle |

### A.4 Review & Approval Owners

| Proof Asset | Author | Reviewer | Approver |
|:---|:---|:---|:---|
| Catch summary / diagnostic example | Diagnostics Engineering | Solutions Engineering | Customer (confirmation) |
| ROI model / financial case | Customer Success + Champion | Finance (Samotics) | Customer (agreement on methodology) |
| Security documentation | Engineering (InfoSec) | CISO (Samotics) | External auditor (for certifications) |
| Case study (published) | Marketing | Customer Success | Customer (final sign-off) |
| TEI / third-party study | External firm | Marketing + Finance | Independent (firm's methodology) |

---

*End of document.*
