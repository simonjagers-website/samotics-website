# Samotics Canonical Lexicon

**Version 1.0 | February 2026**

This lexicon defines the controlled vocabulary for Samotics.com. It exists to prevent category drift, enforce consistency, and help every writer, internal or freelance, use the right word at the right moment.

**How to use it:** Start with the Quick Reference. If you need deeper guidance on a specific term, find it in the full entries below.

---

## Quick Reference

Scan this table before writing any page. Terms are grouped by function and ranked by priority.

### Tier 1: Category-Defining

Use these in headings, hero sections, CTAs, and nav. These terms define what Samotics is.

| Term | One-line guidance | Audience |
|---|---|---|
| **Inaccessible Asset Monitoring (IAM)** | Our category name. Always pair with a plain-English explanation. The market doesn't use this term yet. | All |
| **Reliability blind spot** | The problem we solve. Use to frame the pain. | Executive, Reliability |
| **Hard-to-reach assets** | The assets we serve. Submerged, remote, hazardous, sealed. | All |
| **Sensorless monitoring** | Our key differentiator. Monitoring without sensors on the asset. | All |
| **SAM4** | The product. All caps, no space. Never "Sam4" or "SAM-4." | All |
| **Electrical Signature Analysis (ESA)** | The method. Spell out on first use. Optionally clarify once: "ESA (incl. MCSA)." | Technical, Reliability |

### Tier 2: Supporting Vocabulary

Use in body copy, feature descriptions, and outcome sections.

| Term | One-line guidance | Audience |
|---|---|---|
| **Continuous monitoring** | Always-on, not route-based. Prefer over "real-time" (unless you state latency). | All |
| **Cabinet-based installation** | Where SAM4 lives. MCC or VFD cabinet. Emphasize: no shutdown required. | Technical, IT |
| **Uptime assurance** | Executive outcome framing. Don't say "guaranteed uptime." | Executive |
| **Condition visibility** | What operators get: clear insight into health and failure modes. | Reliability, Maintenance |
| **Anomaly detection** | First-stage detection: deviation from baseline. Not the same as diagnostics. | Technical |
| **Diagnostics** | Second stage: identifying the likely failure mode. Not "root cause" (too absolute). | Technical |
| **Early warning** | Detection with enough lead time to plan. Not "prevents all failures." | All |
| **Failure mode** | A specific degradation path (mechanical or electrical). Not generic "issue." | Technical |
| **Energy waste** | Excess energy from degradation or misoperation. Business case and sustainability. | Executive, Sustainability |
| **Unplanned downtime** | The cost we prevent. Anchor every business case here. | Executive |
| **Case study** | Documented customer result. Not "success story" (marketing-y). | All |

### Tier 3: Technical Depth

Use on technical pages, blogs, and validation content. Define or link to glossary.

| Term | One-line guidance | Audience |
|---|---|---|
| **High-frequency electrical data** | Waveform data at sufficient sampling rates. Only use when you can defend the claim. | Technical |
| **Analytics pipeline** | Signal → features → detection → diagnosis → recommendation. For system diagrams. | Technical |
| **Baseline** | Reference operating pattern for detecting deviations. Not "average." | Technical |
| **Operating regime** | Stable mode (speed, load, process state) with distinct signatures. | Technical |
| **Prognostics** | Time-to-failure estimation. Only use when you have defensible models. | Technical |
| **Ground truth** | Independent confirmation (inspection, teardown, work order). Not "the model said so." | Technical |
| **Detection lead time** | Time between detection and failure/intervention. Quantify per case. | Technical |
| **False positives / false negatives** | Be honest. Don't pretend they don't exist. | Technical |

### Standard Industry Terms

Use these as-is. No Samotics-specific definition needed. Just apply consistently.

| Term | Notes |
|---|---|
| MCC (Motor Control Center) | Spell out on first use. Not "control room." |
| VFD (Variable Frequency Drive) | Alternates: drive, inverter (if market expects it). Not "frequency controller." |
| CMMS / EAM | Maintenance/work management systems. Spell out on first use. |
| SCADA | Supervisory control. OT buyer language. |
| CBM (Condition-based maintenance) | Maintenance triggered by condition, not schedule. Not identical to PdM. |
| PdM (Predictive maintenance) | Broad market/SEO term. Use CBM when precision matters. |
| TCO (Total cost of ownership) | Lifecycle cost including energy, maintenance, downtime, replacement. |
| REST API | For integration pages. Pair with specifics: JSON, webhooks, bi-directional. |

---

## Banned and Restricted Terms

These cause category drift, erode trust, or signal lazy thinking. Do not use on Samotics.com.

### Banned: Never Use

| Term | Why | Use Instead |
|---|---|---|
| Revolutionary / Game-changing | Looks fake. Breaks the restrained voice. | Let results speak. |
| Best-in-class / World-leading | Arrogant and unproven. | Be specific about what's good and why. |
| Cutting-edge / State-of-the-art | If it's good, the proof shows it. | Show evidence. |
| Utilize | Just say "use." | Use |
| Facilitate | Bureaucratic filler. | Help, ease, allow |
| Seamless | Nothing in industrial IT is seamless. | Integrated |
| End-to-end solution | Vague. What does it actually include? | Name the components. |
| Unique | Replace with proof and specifics. | Describe the differentiator. |

### Restricted: Only With Justification

| Term | Rule |
|---|---|
| IIoT platform / IoT platform / Industry 4.0 | Banned unless a page explicitly justifies context (e.g., analyst-facing content). |
| Digital transformation | Same as above. Too broad for Samotics positioning. |
| AI-powered insights | Say *what* insights: failure modes, load changes, energy waste, anomalies. |
| Real-time | Use "continuous monitoring" instead. Only say "real-time" if you state update rate and latency. |
| Platform | Use "SAM4," "SAM4 system," or "SAM4 monitoring." "Platform" is generic. |
| Optimization | Only with a specific variable + mechanism + result. Not as a standalone noun. |
| Solution | Vague. Is it hardware? Software? A service? Name the thing. |
| Non-invasive | Avoid. Sounds medical. Use "sensorless" or "cabinet-based." |
| Predicts / Prevents (as absolutes) | Never claim SAM4 "predicts failures" or "prevents downtime" without qualification. |

---

## Full Entries

Detailed guidance for terms where usage rules are non-obvious. Organized by function.

### Category and Problem Language

#### Inaccessible Asset Monitoring (IAM)

- **Definition:** Continuous condition and energy visibility for assets that cannot be instrumented or physically accessed during operation.
- **Use when:** Defining the category. Page titles, nav, hero sections.
- **Don't use when:** Talking about generic plant-wide monitoring or assets that are easily instrumented.
- **Alternates:** Monitoring hard-to-reach assets; monitoring inaccessible rotating equipment.
- **Avoid:** Asset management platform; IIoT platform; reliability software.
- **Category-creation note:** This is our term. The market does not use it yet. Always introduce it with a plain-English explanation. Never assume recognition. Use it as a heading term and explain it in the body.
- **Example (homepage):** "Inaccessible Asset Monitoring closes the reliability blind spot for equipment that sensors can't reach."
- **Example (technical page):** "IAM captures high-frequency electrical data from the MCC or VFD cabinet, providing continuous condition visibility without field-installed sensors."

#### Reliability blind spot

- **Definition:** The gap in condition and performance visibility created when assets can't be instrumented, accessed, or continuously monitored.
- **Use when:** Framing the problem. "Why now" sections. Executive pain-point language.
- **Don't use when:** The customer already has continuous, high-fidelity monitoring on that asset.
- **Alternates:** Visibility gap; condition visibility gap.
- **Avoid:** "Lack of insights" (too vague).
- **Example:** "Most critical pumps fail inside the reliability blind spot: no sensors, no access, no continuous signal."

#### Hard-to-reach assets

- **Definition:** Assets that are submerged, remote, hazardous, sealed, or otherwise impractical to instrument with physical sensors.
- **Use when:** Defining the ICP and asset class. Works across all audiences.
- **Don't use when:** The asset is easily instrumented and routinely inspected.
- **Alternates:** Inaccessible assets; difficult-to-access assets.
- **Avoid:** "Hidden assets" (non-technical).
- **Example:** "IAM is built for hard-to-reach assets: submerged pumps, sealed skids, and hazardous-zone motors."

#### Sensorless monitoring

- **Definition:** Monitoring without installing sensors on the asset itself. Data is captured from electrical cabinets.
- **Use when:** Differentiation vs. vibration. Core positioning language.
- **Don't use when:** A physical sensor is installed on the asset (e.g., a vibration sensor).
- **Alternates:** No sensors on the asset; cabinet-based monitoring.
- **Avoid:** "Non-invasive" (vague, medical connotation).
- **Example:** "SAM4 enables sensorless monitoring from the MCC or VFD. No cabling to the asset, no shutdown to install."

### Product and Architecture Language

#### SAM4

- **Definition:** Samotics' sensorless condition and energy monitoring system. Analyzes high-frequency electrical signatures from MCC/VFD cabinets to detect condition, performance, and energy changes.
- **Use when:** Product reference. "How it works" pages. Comparisons. Always capitalize: SAM4.
- **Don't use when:** Referring to Samotics the company.
- **Alternates:** None. Keep styling consistent. Use "SAM4 Health" or "SAM4 Energy" when being specific.
- **Avoid:** "The platform" (generic). "The Samotics solution" (vague).
- **Example:** "SAM4 is installed in the cabinet and monitors assets continuously. No field sensors required."

#### Electrical Signature Analysis (ESA)

- **Definition:** Analysis of electrical current and voltage signatures to infer mechanical and electrical condition and performance.
- **Use when:** Naming the method. Technical credibility. "How it works" pages.
- **Don't use when:** The audience only needs outcomes, use plain language and mention ESA parenthetically.
- **Alternates:** "ESA (incl. MCSA)" as a one-time clarifier where the audience expects MCSA.
- **Avoid:** Switching between ESA and MCSA randomly. Pick ESA and stick with it.
- **Example (technical):** "ESA detects subtle changes in electrical signatures that correlate with mechanical and electrical degradation."
- **Example (executive):** "Using Electrical Signature Analysis (ESA), SAM4 reads the health of your assets from the power signal alone."

#### Cabinet-based installation

- **Definition:** Deployment inside or adjacent to electrical cabinets (MCC/VFD), not on the asset.
- **Use when:** Explaining the install model and its safety/access advantages. IT reassurance.
- **Alternates:** Installed in the MCC/VFD cabinet; panel-based deployment.
- **Avoid:** "Quick install" (unless quantified with hours/minutes).
- **Example:** "Cabinet-based installation means no shutdowns, no confined-space entry, and no work near rotating equipment."

### Diagnostics and Outputs

#### Anomaly detection vs. Diagnostics

These two terms are often confused. They describe different stages of the analytics pipeline.

| Stage | Term | Meaning | Example |
|---|---|---|---|
| Stage 1 | **Anomaly detection** | Identifies behavior that deviates from baseline. Does not name the cause. | "SAM4 flagged a deviation in the current spectrum." |
| Stage 2 | **Diagnostics** | Determines the most likely cause (failure mode). | "Diagnostics identified stage-one bearing wear." |

- Use "anomaly detection" when being conservative or when the system hasn't classified the fault.
- Use "diagnostics" when the system names a specific failure mode.
- **Avoid:** "Root cause" (implies certainty we can't always deliver). Use "likely cause" or "indicated failure mode."

#### Prognostics

- **Definition:** Estimating remaining time-to-failure or failure probability over time.
- **Use when:** You have defensible models and confidence bands. Validation pages.
- **Don't use when:** You cannot estimate timelines reliably. Don't imply prognostics if you only provide diagnostics.
- **Alternates:** Risk forecasting; remaining useful life (only if truly provided).
- **Avoid:** "Predicts the exact failure date." Never.
- **Example:** "Where applicable, prognostics estimates risk windows, not exact dates."

#### Early warning

- **Definition:** Detection with enough lead time to plan maintenance before an unplanned event.
- **Use when:** Value framing. Case studies. The bridge between technical detection and business outcome.
- **Don't use when:** The warning came too late to act. That's not early warning, that's late detection.
- **Alternates:** Lead time; advance notice.
- **Avoid:** "Prevents all failures."
- **Example:** "Early warning turns reactive repair into planned intervention, typically months before predicted failure."

### Value and Business Language

#### Unplanned downtime

- **Definition:** Unexpected asset stoppage that disrupts production or service.
- **Use when:** Business case, ROI, executive copy. This is the anchor metric for every value conversation.
- **Alternates:** Unplanned outage.
- **Avoid:** "Stops" (casual).
- **Example:** "Reducing unplanned downtime is the fastest ROI lever for most industrial sites."

#### Energy waste

- **Definition:** Excess energy consumption caused by degradation, misoperation, or process issues.
- **Use when:** Business case and sustainability. Pairs with condition monitoring to show dual value.
- **Don't use when:** You don't have comparative data to substantiate the claim.
- **Alternates:** Avoidable energy loss; inefficiency.
- **Avoid:** "Green savings" (marketing tone). "Energy optimization" without specifying actions and results.
- **Example:** "Energy waste often rises before a mechanical failure becomes visible. SAM4 catches both."

#### Uptime assurance

- **Definition:** Reducing unplanned downtime by detecting degradation early enough to plan maintenance.
- **Use when:** Executive outcome framing. High-level positioning.
- **Don't use when:** You can't link to specific detection and intervention pathways.
- **Alternates:** Availability improvement; reliability improvement.
- **Avoid:** "Guaranteed uptime" (absolute claim. Never make it).
- **Example:** "IAM provides uptime assurance where sensors aren't feasible."

### Proof and Credibility

#### Case study

- **Definition:** Documented customer result with context, method, and measured outcomes.
- **Use when:** Evidence pages. Sales enablement. Anywhere you need proof.
- **Alternates:** Customer story (lighter tone, social media).
- **Avoid:** "Success story" (marketing-y).
- **Example:** "Each case study includes asset context, signals, diagnosis, action, and quantified results."

#### Ground truth

- **Definition:** Independent confirmation of a detected issue through inspection, teardown, measurement, or work order.
- **Use when:** Explaining validation methods. Accuracy claims. Evidence pages.
- **Don't use when:** You mean "the model said so." Ground truth is external to the model.
- **Alternates:** Field confirmation; maintenance confirmation.
- **Example:** "Ground truth comes from maintenance confirmation and post-event analysis, not from the model itself."

#### False positives / false negatives

- **Definition:** Incorrect alerts (false positive) vs. missed faults (false negative). Both are key to adoption and trust.
- **Use when:** Technical validation pages. Engineering trust conversations. Q&A.
- **Don't avoid them.** Pretending they don't exist destroys credibility with engineers.
- **Example:** "We report false positive and false negative rates to set realistic expectations. Our false alarm rate is below 1%."

#### Coverage and limitations

- **Definition:** Explicit statement of what SAM4 can and cannot detect per asset type and configuration.
- **Use when:** How-it-works pages. FAQ. Technical validation.
- **Avoid:** "Covers everything."
- **Example:** "Coverage and limitations are documented per drive type and operating regime. Assets must operate at a minimum of 450 RPM at 50 Hz for reliable detection."

### Integration and Security

These terms are standard industry vocabulary. The lexicon guidance here is about *how* to use them, not *what* they mean.

| Term | Samotics usage rule |
|---|---|
| **Integration** | Always name what integrates with what. "SAM4 integrates with IBM Maximo," not "we offer integration." |
| **CMMS / EAM** | Spell out on first use. Name specific platforms (SAP, IBM Maximo) when possible. |
| **SCADA / Historian** | OT buyer language. Use on integration and IT pages. |
| **Deployment model** | Always specify: cloud, on-prem, hybrid. Never "flexible deployment" without detail. |
| **Data ownership** | "Data ownership remains with the customer." State this clearly on security pages. |
| **Cybersecurity** | Wired cabinet communication. Encryption in transit and at rest. SOC2/ISO. Never "bank-level security." |

### Commercial Language

| Term | Use when | Avoid |
|---|---|---|
| **Pilot** | Pre-rollout. Time-bound evaluation with defined success criteria. | "Proof of concept" if it implies toy scope. |
| **Rollout** | Scaling from pilot to fleet/site/region. | |
| **Time-to-value** | Countering "long implementation" objections. Measure as time to first actionable detection. | "Instant value" unless true and defined. |
| **Payback period** | ROI pages and proposals. Always quantify. | "Fast ROI" without numbers. |

---

## Partner Vocabulary

When referencing strategic partners, use these conventions.

| Partner | Allowed references | Avoid |
|---|---|---|
| **ABB** | "ABB," "ABB Motion Services," "embedded ESA in ABB drives" | "ABB's SAM4" (it's our product, not theirs) |
| **SLB** | "SLB" (not "Schlumberger" unless quoting historical context) | Implying SLB endorses claims they haven't validated |

When co-branding, name both parties clearly: "Samotics and ABB have partnered to..." Always position SAM4 as the Samotics product within a joint offering.

---

## Naming Rules

| Element | Rule |
|---|---|
| **SAM4** | All caps, no space, no hyphen. Never "Sam4" or "SAM-4." |
| **IAM** | Spell out as "Inaccessible Asset Monitoring (IAM)" on first use per page, then IAM. |
| **ESA** | Spell out as "Electrical Signature Analysis (ESA)" on first use per page. |
| **Samotics** | Never "Samotics B.V." or "The Samotics Team" in body copy. |
| **SAM4 Health / SAM4 Energy** | Use when being specific about the product module. |
| **Possessives** | "Samotics' insights" or "insights from Samotics." Avoid "Samotics's." |
| **Hardware** | "DAQ device," "Connectivity Kit," "Motor Kit." Capitalize consistently. |

---

*This lexicon is a living document. Propose additions or changes via the content lead. Last updated: February 2026.*
