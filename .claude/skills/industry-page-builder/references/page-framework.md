# Industry Page Framework

The 9-section page structure for all industry vertical pages on samotics.com. This is the master document — read it before building, editing, or reviewing any industry page.

---

## Narrative arc

The industry page earns belief in sequence. Each section does one job. No section works without the one before it doing its job first.

```
Problem (Hero)
  -> Identity (Trust bar)
    -> Pain deepening (Challenges)
      -> Mechanism bridge (Why SAM4)
        -> Relevance (Assets monitored)
          -> Evidence (Proof / case studies)
            -> [Mid-page CTA for the convinced]
              -> Risk reduction (Installation)
                -> Objection handling (FAQ)
                  -> Action (Terminal CTA)
```

The arc maps to the proof stack framework used in high-trust B2B pages: Identity proof, Relevance proof, Capability proof, Outcome proof, and Risk proof — in that order. Rearranging the sections breaks the persuasion sequence.

---

## Section-by-section specification

### Section 1: Hero

**BEM class:** `sam-section sam-section--hero`
**Background:** Dark overlay on industry-specific image
**Belief shift:** "This is about my specific problem."

**Content beats:**
- Overline: Industry name (e.g., "Water & Wastewater")
- H1: Problem-led headline naming the blind spot. Not product-led. Example: "Your critical pumps sit where sensors cannot go."
- Subtitle: 1-2 sentences expanding the blind spot and introducing ESA as the bypass. Mention "from the motor control cabinet" or "from the MCC."
- Category line: Short positioning statement. Example: "Sensorless condition monitoring. From the electrical cabinet."
- Stats bar: 2-3 KPIs with `sam-stat` components. Use JetBrains Mono for values. Include measurement method box below.
- Measurement method box: Transparent background, 12px text, explains how the stats were measured. Non-negotiable — every hero stat needs attribution.
- CTA pair: Primary button ("Request a demo") + ghost button ("See results below" anchoring to #proof).

**Content rules:**
- The headline names the problem, not the product. If "SAM4" appears in the H1, you've failed.
- Stats must be industry-specific and verified. Source from `social-proof.md` in samotics-website-content or from per-industry-guide.md.
- Hero image must be industry-specific (not stock). 1920x1080 JPEG, 400KB max.

**Anti-patterns:**
- "SAM4 is the leading..." — product-first framing
- Unattributed stats without measurement method box
- Stock photography that could apply to any industry

---

### Section 2: Trust bar

**BEM class:** `sam-trust-bar`
**Background:** Inherits (does not count in alternation)
**Belief shift:** "Real companies in my sector use this."

**Content beats:**
- Label: "Trusted by leaders in [industry]"
- Logo strip: 4-5 customer logos, grayscale default, colour on hover
- Logos must be from verified customers in this specific vertical

**Content rules:**
- If fewer than 3 named customers exist for this vertical, omit the trust bar entirely. Never pad with logos from other industries.
- Logo height: 36-48px. Transparent PNG. Grayscale filter with 0.7 opacity default, full colour on hover (0.3s transition).

---

### Section 3: The problem (challenges)

**BEM class:** `sam-section sam-section--white` (or `--seashell` per alternation)
**Background:** White
**Belief shift:** "Yes, this is the pain I live with."

**Content beats:**
- Overline: "The problem"
- H2: Industry-specific headline naming the pain. Example: "Water assets fail silently. And expensively."
- Subtitle: 1 sentence framing the scale of the problem.
- Card grid: 4 challenge cards in a 2x2 grid. Each card has an icon, bold title, and 2-3 sentence description.

**Content rules:**
- This section does NOT mention SAM4 or ESA. Pure domain content. Earn credibility before introducing the product.
- Use industry-specific language from the `industry-lexicon` skill. "Sewage pump blockages," not "equipment failures."
- Anti-orphan rule: never use a 3+1 layout. Either find a fourth challenge or switch to a 3-column grid.
- Each challenge should name a specific failure mode, operational consequence, and cost driver.
- Load `failure-mode-explainer` skill for technical substance on failure mechanisms.

**Anti-patterns:**
- "SAM4 detects..." — product language in a problem section
- "Rotating equipment" — generic terminology
- Challenges that could apply to any industry

---

### Section 4: Why SAM4 (differentiators)

**BEM class:** `sam-section sam-section--seashell` (or `--white` per alternation)
**Background:** Seashell
**Belief shift:** "That's why sensors fail here — and this is a different approach."

**Content beats:**
- Overline: "Why SAM4"
- H2: "Why SAM4 works for [industry]"
- Card grid: 4 differentiator cards in a 2x2 grid. Each card: bold title + 2-3 sentences.
- Contrast line: 1 sentence at the bottom explaining why traditional monitoring fails for this industry. Centered, subtle styling.

**Content rules:**
- The four differentiators follow a standard structure adapted per industry:
  1. No sensors on the asset (the access argument)
  2. Works across your full fleet (the scale argument)
  3. Detects what vibration cannot (the capability argument)
  4. Deploys without downtime (the friction argument)
- The contrast line sharpens the gap between traditional monitoring and ESA. Example: "Traditional vibration sensors require physical access to the asset. For submerged, remote, or hazardous pump sets, that access does not exist."
- This section is the mechanism bridge. It must follow the challenges section — the visitor needs to feel the problem before hearing the solution.

---

### Section 5: What we monitor (assets)

**BEM class:** `sam-section sam-section--white` (or per alternation)
**Background:** White
**Belief shift:** "They monitor the exact equipment I run."

**Content beats:**
- Overline: "What we monitor"
- H2: "Critical assets in [industry]"
- Subtitle: 1 sentence confirming SAM4 monitors any AC motor-driven equipment from the MCC.
- Card grid: 3 asset cards in a 3-column grid. Each card is a clickable `<a>` linking to `/platform/what-we-monitor/[asset-type]`.

**Content rules:**
- Each card: asset type title, 2-sentence description naming specific faults ESA detects for that asset, and a link text ("Pump monitoring details ->").
- Name the specific equipment types for that industry. Water: submersible pumps, aeration blowers, agitators/mixers. Oil & Gas: ESPs, compressors, hazardous-area motors.
- Cards follow the Samotics card interaction pattern from `samotics-design-system`: whole card is an `<a>` tag, 1px border, 4px radius, shadow on hover only.

---

### Section 6: Proof (case studies)

**BEM class:** `sam-section sam-section--seashell` (or per alternation), `id="proof"`
**Background:** Seashell
**Belief shift:** "Here's quantified evidence from my peers."

**Content beats:**
- Overline: "Proof"
- H2: "[Industry] case studies"
- Featured case study: Full-width highlight card with overline, H3 title, descriptive paragraph, 3 KPI stats, and link to full case study.
- Supporting cards: 3 proof cards in a 3-column grid below. Each: KPI number headline, customer name, one-paragraph mechanism, link.
- **Mid-page CTA:** After the proof cards, add a secondary CTA. Text link or outline button: "Ready to see what SAM4 finds? Request a demo ->" This catches visitors who are convinced and shouldn't have to scroll further.

**Content rules:**
- No hedge language. Never "early results," "growing vertical," "strongest proof points."
- Stats must include measurement method boxes (via `technical-proof-architect` skill).
- If fewer than 3 case studies exist, use 2 + a summary card with aggregated stats.
- Featured case study should be the strongest evidence for this vertical.
- Load `plant-walkthrough-story-builder` for detection narrative content.

---

### Section 7: Installation

**BEM class:** `sam-section sam-section--white` (or per alternation)
**Background:** White
**Belief shift:** "This is easier to deploy than I expected."

**Content beats:**
- Overline: "Installation"
- H2: Industry-specific install headline reinforcing the constraint bypass. Example: "No sensors in the wet well."
- 2-column layout: 3-step install flow on the left, real SAM4 installation photo on the right.
- Steps: (1) Clip on at the MCC, (2) Connect to the network, (3) Monitor from anywhere.
- Optional customer quote below the install grid.

**Content rules:**
- The install headline should reinforce the industry-specific constraint: "No sensors in the wet well" (Water), "No entry to ATEX zones" (Oil & Gas), "No access to sealed housings" (Chemicals).
- Installation photo must be real (not stock). 800x600 JPEG, 80KB max.
- Steps should be concrete and specific. "Clip-on current transformers install in minutes. No asset shutdown, no confined-space entry."

---

### Section 8: FAQ

**BEM class:** `sam-section sam-section--seashell` (or per alternation)
**Background:** Seashell
**Belief shift:** "My remaining objections are addressed."

**Content beats:**
- Overline: "Common questions"
- H2: "[Industry] monitoring FAQ" or similar
- Accordion: 4-6 industry-specific questions with expandable answers.

**Content rules:**
- Source objections from sales calls for that vertical. Not generic questions.
- The primary objection for each industry should be the first question. Examples:
  - Water: "Our pumps are underground. Nothing monitors them."
  - Oil & Gas: "We already have vibration on critical assets. Why add ESA?"
  - Chemicals: "Can ESA work in ATEX Zone 1?"
  - Metals & Mining: "Our conveyors are kilometres long. How does monitoring from the MCC help?"
- Answers should be 2-4 sentences. Technical but accessible. Reference specific detection capabilities where relevant.
- Include at least one question about integration/data (e.g., "Does SAM4 integrate with our CMMS?") and one about deployment timeline (e.g., "How quickly can we deploy?").
- FAQ is positioned after installation and before the terminal CTA. It is the final objection-clearing layer before the conversion ask.

**Anti-patterns:**
- Generic questions that apply to any monitoring vendor
- Questions that are really just feature descriptions in disguise
- Answers longer than 5 sentences

---

### Section 9: Terminal CTA

**BEM class:** `sam-section sam-section--dark sam-terminal-cta`
**Background:** Dark (Space Cadet)
**Belief shift:** "I'm ready to act."

**Content beats:**
- Overline: "Get started"
- H2: Scale narrative naming the specific asset class. Example: "Monitor every pump. No sensors in the wet well."
- Subtitle: 1 sentence about the path from first site to fleet-wide.
- CTA pair: Primary button ("Start your asset audit") + ghost button ("Talk to a [industry] engineer" or "Request a demo").

**Content rules:**
- Name the asset class in the CTA, not "your equipment."
- The scale narrative should feel achievable: "Start with your highest-risk pumping stations. See results within weeks. Scale from there."

---

## Adaptation rules

The 9-section framework applies to all industry pages. Sections can be removed if content is genuinely unavailable, but follow these rules:

1. **Never remove sections 1, 3, 4, or 9.** Hero, challenges, differentiators, and terminal CTA are mandatory.
2. **Trust bar requires 3+ named customers.** If fewer, omit entirely.
3. **Proof section requires at least 1 named case study.** If none exist, replace with an aggregated stats card sourced from cross-industry data, and flag for content development.
4. **FAQ requires sourced objections.** If sales call data isn't available for a vertical, draft objections based on competitive intelligence and flag for validation.
5. **When removing any section, recolour adjacent sections** to maintain background alternation.
6. **If proof is weak, strengthen installation.** When a vertical has thin evidence, lean harder on the installation constraint story. The "how it deploys" argument is the next-strongest trust builder after proof.

---

## QA checklist

Before marking an industry page complete:

- [ ] All 9 sections present (or intentionally removed with alternation preserved)
- [ ] Hero headline is problem-led, not product-led
- [ ] Section 3 (challenges) contains zero mentions of SAM4 or ESA
- [ ] Section 4 (Why SAM4) comes AFTER section 3 (challenges), not before
- [ ] Hero image compressed and deployed to `dist/assets/images/heroes/`
- [ ] Customer logos processed (48px PNG, transparent) and deployed
- [ ] Install photo deployed
- [ ] No em-dashes anywhere in copy
- [ ] No hedge language around proof
- [ ] No two adjacent sections share the same background colour
- [ ] All case study links resolve to real pages
- [ ] All stats have measurement method boxes
- [ ] CTAs match CTA strategy (primary: Start Your Asset Audit; secondary: Request a Demo)
- [ ] Industry-specific terminology used throughout (verified against `industry-lexicon` skill)
- [ ] FAQ contains industry-specific objections, not generic questions
- [ ] Mid-page CTA present after proof section
- [ ] Source HTML committed to `pages/industries/{page}.html`
- [ ] Dist file rebuilt with correct inline CSS
