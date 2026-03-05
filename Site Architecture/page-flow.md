# Homepage Page Flow

Narrative arc, emotional progression, and section-by-section content logic

**Document:** Homepage — Page Flow
**Layer:** Content + Design
**Owner:** Marketing
**Status:** Draft
**Date:** February 2026
**Dependencies:** Page Brief, CTA Strategy, Messaging Framework, Writing Style Guide, Layout Rules, Aesthetic Direction
**Feeds Into:** Copywriting brief, Wireframe, CMS build

---

## How to Use This Document

This is the homepage blueprint. It defines not just what appears in each section, but why — and what the visitor should feel at each stage of the scroll. Copywriters use it to write content that builds a coherent argument from top to bottom. Designers use it to create a visual rhythm that reinforces the emotional arc. Developers use it to validate that section order and transitions match the intended experience.

The homepage is a router, not a brochure. But it's a router that tells a story. The visitor who scrolls to the bottom should arrive at the CTA with a fundamentally different belief about their monitoring coverage than when they started.

---

## Narrative Framework

The homepage follows StoryBrand's seven-part structure. The visitor is the hero. Samotics is the guide.

| StoryBrand Element | Homepage Section | What It Does |
|-------------------|-----------------|-------------|
| **Character** | Hero (§1) | The visitor — a reliability or operations leader responsible for assets they can't fully monitor. The page opens on their world, not ours. |
| **Problem** | Hero (§1) + Stakes (§2) | External: 30–40% of critical assets are unmonitored. Internal: "I know we have a gap but I can't quantify it or fix it with current tools." Philosophical: equipment this critical shouldn't be invisible. |
| **Guide** | Method (§3) | Samotics enters as the guide — not as a vendor, but as the company that solved the physics problem. Authority comes from the method (ESA), not from claims. Empathy comes from naming the problem correctly in §1–2. |
| **Plan** | Industry Routing (§4) | The plan is concrete: see how this works in your industry, with your assets, at your scale. The routing cards are the "three steps" — find your industry, see the proof, talk to us. |
| **Call to Action** | Terminal CTA (§7) | Direct: "Request a Demo." Transitional: "Start Your Asset Audit." Both earn their place because the argument has been built. |
| **Failure** | Stakes (§2) | The cost of inaction. £390K fines, €50K+ per avoided shutdown, 70,000 wasted inspection trips. This section answers: "What happens if I do nothing?" |
| **Success** | Social Proof (§5) + Platform Preview (§6) | The transformation: from reactive maintenance and blind spots to 10,000+ assets monitored, >90% detection rate, fleet-level visibility. The platform screenshot makes the success state tangible. |

### Cognitive Load Principle

StoryBrand's core insight for web design: every piece of content that doesn't help the visitor survive or thrive burns cognitive calories for nothing. The homepage budget is 50–80 seconds of scanning attention. Seven sections. Each section earns one belief shift. If a content block doesn't change what the visitor believes, it's noise — cut it.

This means:

- **No "About Samotics" section on the homepage.** The guide earns authority through evidence (proof, logos, platform), not through self-description. The About page exists for the CTO who specifically seeks it.
- **No feature lists.** Features burn calories. Outcomes don't. "Over 90% of developing faults detected" is an outcome. "20 kHz sampling frequency" is a feature. Features belong on `/technology/esa`.
- **No second reading path.** The homepage has one argument in one direction: top to bottom. No tabs, no toggles, no "choose your path" gimmicks above the industry routing section. Branching creates decision fatigue. The industry routing cards in §4 are the only branching point — and they come after the visitor already believes in the method.
- **One primary CTA per viewport.** Every additional button is a decision. Decisions cost calories. The hero gets one orange button. The terminal gets one orange button. Everything else is a text link.

---

## The Argument

The homepage makes one argument in seven moves:

1. You have a blind spot.
2. It's bigger than you think.
3. There's a way to close it.
4. It works in your industry.
5. Other companies like yours already trust it.
6. Here's what the platform looks like.
7. Here's how to start.

Every section serves exactly one of these moves. If a piece of content doesn't advance this argument, it doesn't belong on the homepage.

---

## Emotional Arc

The visitor's emotional state should shift through three phases as they scroll:

```
RECOGNITION          CREDIBILITY          CONFIDENCE
─────────────────    ─────────────────    ─────────────────
"They understand     "This is real        "I should talk
 my problem"          engineering"          to these people"

Sections 1–2         Sections 3–5         Sections 6–7
```

**Phase 1: Recognition.** The visitor sees their own problem reflected back at them. Not a product pitch — a mirror. The emotional register is empathy and precision. The visitor should feel understood, not sold to.

**Phase 2: Credibility.** The visitor sees evidence that the solution is real, validated, and operating at scale. The emotional register is authority and restraint. No hype. Numbers, names, and engineering logic.

**Phase 3: Confidence.** The visitor believes enough to take a step. The emotional register is calm assurance. The CTA feels like the obvious next move, not a pressure tactic.

---

## Section-by-Section Flow

---

### Section 1: Hero

**Argument move:** You have a blind spot.

**Emotional state:** Recognition. "These people understand my world."

| Property | Specification |
|----------|--------------|
| **Background** | `--bg-dark` (`#1F1F33`). Full-bleed. The page opens dark, serious, industrial. |
| **Layout** | Asymmetric. Headline spans columns 1–10. Visual element (SAM4 dashboard screenshot, spectral graph, or 3D render of MCC) in columns 12–16. Column 11 empty for tension. |
| **Height** | Full viewport on desktop (`100vh`). Content visible without scrolling. No scroll-triggered animations. |

**Headline:**

The headline names the problem, not the product. The visitor's first impression should be: "They understand what I'm dealing with."

Direction: State the blind spot in concrete, technical terms. Reference the monitoring gap, not the solution. The Reliability Manager arriving from an S1 failure and the Operations Director arriving from an S2 audit both need to see their reality named in the first line.

Example direction (not final copy):
> "30–40% of your critical rotating equipment has no condition monitoring. Every AC motor already tells you when something is wrong. Through its electrical signature."

The headline operates in the "Technically Rigorous" + "Direct and Purposeful" voice registers. No "revolutionary." No "welcome to the future of." Name the gap. Then name the signal.

**Sub-headline:**

One sentence that bridges problem to solution. Introduces ESA without explaining it. Links to `/technology/esa` for depth.

Example direction:
> "SAM4 uses AI-driven Electrical Signature Analysis to monitor every AC motor 24/7 — from the electrical cabinet, not the machine."

**Primary CTA:**

"Request a Demo" — `--bg-accent` (`#FF5429`) button. One orange CTA per viewport. This is the only orange element in the hero.

**Secondary CTA:**

"Watch how it works" or "See how ESA works" — ghost button (white border, white text on dark). Links to a short overview video or `/technology/how-it-works`. This serves the visitor who isn't ready to convert but wants to go deeper.

**Visual element:**

Not a stock photo. Not a generic "AI brain." Options (in priority order):

1. SAM4 dashboard screenshot — dark-mode, showing real asset health data, alert feed, spectral graph. This passes the "engineer recognition test" from the Aesthetic Direction: a Reliability Engineer should see a specific spectral signature and think "these people understand my motor."
2. 3D render of an MCC with data flowing outward — the "Inside-Out" visualization. Electricity flowing from the cabinet to distant assets as a stream of data.
3. Split visual — one side shows a submerged pump (dark, inaccessible, unmeasurable); the other shows the MCC (clean, safe, accessible, data-rich).

No stock photography of engineers pointing at tablets.

**What the visitor should feel at the end of this section:**

"These people understand the problem I'm trying to solve. This isn't a generic monitoring company."

---

### Section 2: The Stakes

**Argument move:** It's bigger than you think.

**Emotional state:** Urgency. The blind spot isn't an inconvenience — it's an active risk.

| Property | Specification |
|----------|--------------|
| **Background** | Transition from `--bg-dark` to `--bg-primary` (`#FFFFFF`) using `--gradient-dark-to-light`. Not a hard cut. The darkness of the hero fades into the clarity of the content sections. |
| **Layout** | Full container width. 3–4 stat callouts in a row, evenly spaced across the 16-column grid. |
| **Spacing** | `spacing-11` (128px) top padding from hero. `spacing-08` (48px) between heading and stats. |

**Heading:**

Short, declarative. Names the cost of the blind spot.

Example direction:
> "The cost of what you can't see"

**Stats strip:**

Three to four headline numbers that quantify the risk. Each stat has a large number, a one-line label, and a source attribution (small text). These are not Samotics marketing claims — they're industry facts or customer outcomes.

Candidate stats (select 3–4):

| Stat | Label | Source |
|------|-------|--------|
| 30–40% | of critical assets go unmonitored | Industry data |
| £390K | potential fine avoided from a single detection | Yorkshire Water |
| €50K+ | saved per avoided unplanned shutdown | ArcelorMittal |
| 70,000 | manual inspection trips replaced per year | Yorkshire Water |
| $5,000+ | installed cost per sensor on a submerged pump | Proximity Penalty economics |

**Body text (optional):**

One short paragraph (2–3 sentences) that connects the stats. Not required if the stats speak for themselves. If included, operate in the "Commercially Clear" voice register.

Example direction:
> "Traditional condition monitoring forces a trade-off: expensive sensor installations or no monitoring at all. For submerged pumps, enclosed drives, and hazardous-zone motors, most teams choose nothing. The result: failures you didn't see coming."

**Link:**

"Understand the blind spot →" — text link to `/problem`. For the visitor who wants the full argument before seeing the solution.

**What the visitor should feel at the end of this section:**

"The gap is bigger and more expensive than I thought. This isn't something I can keep ignoring."

---

### Section 3: The Method

**Argument move:** There's a way to close it.

**Emotional state:** Shift from urgency to possibility. The problem has a solution — and it's grounded in real engineering.

| Property | Specification |
|----------|--------------|
| **Background** | `--bg-primary` (`#FFFFFF`). Clean, light. The solution section should feel clear and confident after the weight of the problem. |
| **Layout** | Asymmetric split. Left side (columns 1–8): text content. Right side (columns 9–16): visual (data flow diagram, MCC-to-asset animation, or product screenshot). |
| **Spacing** | `spacing-11` (128px) from previous section. |

**Heading:**

Name the method. Not the product — the approach.

Example direction:
> "Monitor from the electrical cabinet. Not the machine."

**Body text:**

3–4 short paragraphs (1–3 sentences each) that explain ESA in plain, technical terms. Follow the "Technically Rigorous" register but keep it scannable. This is not the deep-dive (that's `/technology/esa`) — it's the elevator pitch for the method.

Content beats:

1. How it works: Current and voltage signatures captured at the MCC reveal the condition of the entire drivetrain — motor, transmission, coupling, and driven load.
2. What it catches: Over 90% of developing faults detected weeks to months before failure.
3. Why it's different: No sensors on the machine. No production downtime to install. Less than 30 minutes per asset.

**Three value cards (optional):**

Compact cards highlighting the three core differentiators. Each card: icon (functional, not decorative), one-line headline, one-line description. Cards use `--border-light` (`#E8E4E0`) borders, zero border-radius.

| Card | Headline | Description |
|------|----------|-------------|
| 1 | No sensors on the machine | Monitors from the MCC. Submerged, enclosed, hazardous — all reachable. |
| 2 | Install in under 30 minutes | No shutdown, no scaffolding, no ATEX permits. |
| 3 | >90% fault detection | Weeks to months of lead time before failure. |

**Link:**

"How ESA works →" — text link to `/technology/esa`.

**What the visitor should feel at the end of this section:**

"This is real engineering, not a gimmick. The method makes physical sense. I want to see if it works in my industry."

---

### Section 4: Industry Routing

**Argument move:** It works in your industry.

**Emotional state:** Relevance. The visitor sees themselves — their industry, their assets, their problems.

| Property | Specification |
|----------|--------------|
| **Background** | `--bg-secondary` (`#F8F5F2`). Transition from white via `--gradient-section-fade`. The warm Seashell background subtly differentiates this section from the technology content above. |
| **Layout** | Full container width. Grid of industry cards, 3 across on desktop (columns spanning ~5 each with gutters), stacked on mobile. |
| **Spacing** | `spacing-11` (128px) from previous section. |

**Heading:**

Example direction:
> "Monitoring the assets your industry can't reach"

**Industry cards:**

One card per industry. Each card is a routing element — it links to the corresponding `/industries/[x]` page. The card IS the interaction.

| Industry | Visual | Headline | One-line proof |
|----------|--------|----------|----------------|
| Water & Wastewater | Submersible pump or pumping station | Continuous pump health — without a site visit | 1,000+ pumping stations monitored |
| Oil & Gas | MCC in an industrial facility | Safe-zone monitoring for hazardous areas | ATEX-compatible from the MCC |
| Metals & Mining | Heavy industrial motors | Catch what your maintenance schedule misses | Bearing faults detected 5 months early |
| Chemicals | Process plant | Full fleet coverage in hours, not months | 40% reduction in equipment downtime |
| Pulp & Paper | Mill equipment | Reliability and energy efficiency in one platform | 7.1% pump efficiency improvement |

**Card design:**

Zero border-radius. `--border-light` border. On hover: subtle lift (`--shadow-md`) and `--border-accent` (2px left border, Samotics Orange). Each card shows the industry name, a single-line proof point, and links to the full industry page.

No "Learn More" buttons. The card itself is the link. Cursor changes to pointer on hover. The proof point on each card is the hook that earns the click.

**What the visitor should feel at the end of this section:**

"They work in my industry. They've already solved this for companies like mine. Let me see the proof."

---

### Section 5: Social Proof

**Argument move:** Other companies like yours already trust it.

**Emotional state:** Validation. The visitor is no longer evaluating a claim — they're seeing evidence that others have already made this decision.

| Property | Specification |
|----------|--------------|
| **Background** | `--bg-primary` (`#FFFFFF`). Back to white. Clean canvas for the numbers and logos to stand out. |
| **Layout** | Two sub-sections: (a) aggregate stats bar, (b) customer logo strip + featured quote. |
| **Spacing** | `spacing-11` (128px) from previous section. |

**Sub-section A: Aggregate Stats Bar**

A single row of 4–5 headline numbers. Large typography. `--color-primary` (`#1F1F33`). No background boxes — the numbers float on white.

| Stat | Label |
|------|-------|
| 10,000+ | assets monitored |
| 80+ | customers |
| 5 | continents |
| >90% | fault detection rate |
| 8 months | average payback |

These numbers do the heavy lifting. No paragraphs of explanation needed. The stats bar is the most scannable element on the page.

**Sub-section B: Customer Logos + Featured Quote**

Customer logos in a horizontal strip. Greyscale by default, colour on hover. Logos visible: Yorkshire Water, ArcelorMittal, DuPont, Schiphol, Nyrstar, Vitens, Nucor, ABB. No more than 8–10 to avoid visual noise.

Below the logos, one featured customer quote. Rotate quotes periodically or select one that speaks to the widest audience.

Candidate quote:
> "SAM4 detected possible bearing damage which we had not picked up through our vibration monitoring." — Schiphol Airport

This quote works because it directly addresses the #1 objection (vibration vs ESA) and names a recognisable brand.

**Link:**

"See all customer results →" — text link to `/proof`.

**What the visitor should feel at the end of this section:**

"This isn't theoretical. Real companies I've heard of are using this at scale. The numbers are credible."

---

### Section 6: Platform Preview

**Argument move:** Here's what the platform looks like.

**Emotional state:** Concreteness. The solution stops being abstract and becomes tangible. The visitor can picture themselves using this.

| Property | Specification |
|----------|--------------|
| **Background** | `--bg-dark` (`#1F1F33`). Full-bleed. Returns to the dark palette from the hero. The SAM4 dashboard screenshot glows against Space Cadet — the "flight deck" aesthetic from the Aesthetic Direction. |
| **Layout** | Asymmetric. Heading and 3–4 capability callouts in columns 1–6. Large dashboard screenshot or interactive preview in columns 7–16. The visual dominates. |
| **Spacing** | `spacing-12` (160px) from previous section. The extra spacing before the dark section creates a clear break and signals "we're showing you something important." |

**Heading:**

Example direction:
> "One platform. Every motor. 24/7."

**Capability callouts (left column):**

3–4 short callouts, each a single line with a small icon. These name what the visitor would see in the platform. Functional descriptions, not marketing adjectives.

| Callout |
|---------|
| Fleet-level asset health dashboard |
| AI-driven anomaly detection and alerting |
| Diagnostic reports with recommended actions |
| CMMS integration (SAP PM, IBM Maximo) |

**Visual (right column, dominant):**

SAM4 dashboard screenshot. Dark-mode. Showing real (or realistic) data: asset health grid, alert severity indicators, a spectral analysis graph with a highlighted anomaly. This is the hero image of the section — it must feel like a real product, not a mockup.

The screenshot should pass the engineer recognition test: specific enough that a Reliability Manager sees a tool they'd use, not a brochure image.

**Link:**

"Explore the SAM4 platform →" — text link to `/platform/sam4`.

**No CTA button in this section.** The platform preview is not the conversion point — it's a credibility builder. The CTA comes in the next (and final) section. Placing a button here would compete with the terminal CTA and violate the one-primary-CTA-per-viewport rule.

**What the visitor should feel at the end of this section:**

"I can see myself using this. It looks like a real tool, not a marketing demo. I want to see it with my own data."

---

### Section 7: Terminal CTA

**Argument move:** Here's how to start.

**Emotional state:** Confidence and readiness. The visitor has been given problem, method, proof, and product. The CTA should feel like the natural conclusion, not a hard sell.

| Property | Specification |
|----------|--------------|
| **Background** | Continues `--bg-dark` (`#1F1F33`) from the platform preview section. No break between sections 6 and 7 — the dark surface runs continuously. The CTA block lives in the pre-footer "Terminal" block defined in the Layout Rules. |
| **Layout** | Strict split. Columns 1–8: headline and sub-line. Column 9: empty (visual gap). Columns 10–16: CTA buttons or minimal form. |
| **Spacing** | `spacing-10` (96px) from platform preview content. Visually, this section is the bottom of the dark zone before the footer. |

**Headline:**

Big. White. Declarative. The headline restates the value proposition in outcome terms — not what the product does, but what changes for the visitor.

Example direction:
> "Stop reacting to failures you could have seen coming"

Or, more solution-oriented:
> "Monitor every motor. From the cabinet. Starting now."

The tone here is "Restrained and Authoritative" — confidence without pressure.

**Sub-line:**

One sentence that sets the expectation for what happens after clicking. This matters: the Reliability Manager wants a technical conversation, not a sales pitch. Name it.

Example direction:
> "Request a demo and speak with one of our reliability engineers within 48 hours."

**Primary CTA:**

"Request a Demo" — `--bg-accent` (`#FF5429`) button. Same button as the nav, but here it's earned. The visitor has scrolled through the full argument. This is the payoff.

**Secondary CTA:**

"Start Your Asset Audit" — ghost button (white border, white text). For the visitor who isn't ready for a demo but wants a lower-commitment next step. This serves the S2 Operations Director who needs an audit to build an internal case.

**What the visitor should feel at the end of this section:**

"I've seen enough. These people understand my problem, the technology is credible, and other companies trust it. A demo is worth my time."

---

## Full Scroll Summary

| # | Section | Background | Argument Move | StoryBrand Role | Emotional State | Time to Read |
|---|---------|-----------|---------------|----------------|-----------------|-------------|
| 1 | Hero | Dark (`#1F1F33`) | You have a blind spot | Character + Problem | Recognition | 5–8 sec |
| 2 | Stakes | White (`#FFFFFF`) | It's bigger than you think | Failure (stakes) | Urgency | 8–12 sec |
| 3 | Method | White (`#FFFFFF`) | There's a way to close it | Guide (authority) | Possibility | 15–20 sec |
| 4 | Industry Routing | Seashell (`#F8F5F2`) | It works in your industry | Plan | Relevance | 5–10 sec |
| 5 | Social Proof | White (`#FFFFFF`) | Others already trust it | Success (evidence) | Validation | 5–8 sec |
| 6 | Platform Preview | Dark (`#1F1F33`) | Here's what it looks like | Success (tangible) | Concreteness | 10–15 sec |
| 7 | Terminal CTA | Dark (`#1F1F33`) | Here's how to start | Call to Action | Confidence | 3–5 sec |

**Total estimated scroll time:** 50–80 seconds for a scanning visitor. Longer for someone who reads body text. The page is designed for the scan — every section's heading and visual must communicate the argument move without reading the body copy.

---

## Colour Rhythm

The page alternates between dark and light surfaces in a deliberate pattern:

```
DARK    ████████████████  Hero
LIGHT   ░░░░░░░░░░░░░░░░  Stakes (white)
LIGHT   ░░░░░░░░░░░░░░░░  Method (white)
WARM    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  Industry Routing (seashell)
LIGHT   ░░░░░░░░░░░░░░░░  Social Proof (white)
DARK    ████████████████  Platform Preview
DARK    ████████████████  Terminal CTA
DARK    ████████████████  Footer
```

The pattern creates two dark bookends (hero + platform/CTA/footer) with a light middle section. The seashell section in the middle provides a subtle break within the light zone. Transitions between surfaces use the gradient tokens from the Layout Rules — no hard colour cuts.

This rhythm reinforces the emotional arc: the page opens in the gravity of the problem (dark), moves into clarity and evidence (light), then returns to dark for the product and the close. The visitor subconsciously associates the dark sections with Samotics (authority, the platform) and the light sections with their own evaluation process (evidence, proof, routing).

---

## Persona-Specific Scan Paths

Different personas read the homepage differently. The flow must work for all of them, but each has a natural exit point.

**Reliability Manager (S1 — failure just happened):**
Hero (recognised the problem) → Method (understood ESA) → exits to `/technology/esa` or `/industries/[x]`. May never reach Section 5. The hero and method sections must be strong enough to convert or route this persona within 20 seconds.

**Operations Director (S2 — building a case):**
Hero → Stakes (the numbers catch their eye) → Social Proof (validation) → exits to `/proof` or clicks "Start Your Asset Audit." This persona scans for numbers and logos. The stats bar in Section 5 is their anchor.

**CTO / VP Engineering (S3 — strategic evaluation):**
Hero (brief scan) → Social Proof (logos, scale) → Platform Preview (enterprise fit) → exits to `/about` or `/platform/sam4`. This persona is often pre-qualified by an internal champion. They spend 30 seconds on the homepage, scanning for enterprise credibility signals. The aggregate stats bar and the ABB logo in the logo strip are their decision points.

**Channel Partner (S5 — evaluating the technology):**
Hero → Method (is this differentiated?) → Industry Routing (where does this sell?) → Social Proof (ABB logo) → exits to `/about/abb` or `/platform/sam4`. The partner evaluates market opportunity, not personal pain.

---

## Content Dependencies

| Section | Requires Before Copywriting |
|---------|---------------------------|
| Hero | Final headline direction approved. SAM4 dashboard screenshot or 3D render produced. |
| Stakes | Stats verified with customer success team. Source attributions confirmed. |
| Method | ESA elevator pitch finalised (aligns with `/technology/esa` page copy). |
| Industry Routing | Industry page URLs and one-line proof points confirmed per industry. |
| Social Proof | Customer logo usage approvals. Featured quote approved by customer. |
| Platform Preview | Production-quality SAM4 dashboard screenshot with realistic data. |
| Terminal CTA | CTA copy finalised per CTA Strategy. Post-submission flow implemented. |

---

## What This Document Does Not Cover

This is the narrative and emotional flow. It does not replace:

- **Page Brief** — for the strategic purpose, target audience, and traffic sources. Already documented.
- **CTA Strategy** — for form fields, post-submission behaviour, and tracking. Already documented.
- **Wireframe** — for pixel-level layout, responsive breakpoints, and component specs. Next step.
- **Final copy** — headline and body text directions in this document are illustrative, not final. The copywriter owns the final language, guided by the Writing Style Guide.
