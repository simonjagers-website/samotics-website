---
name: industry-page-builder
description: >
  Use this skill whenever building, editing, reviewing, or planning any industry page under
  /industries/ on samotics.com. This includes pages for Water & Wastewater, Oil & Gas,
  Chemicals & Process Industries, Metals & Mining, Pulp & Paper, Airports, and any future
  industry verticals. Trigger on any mention of "industry page", "vertical page", "water page",
  "oil and gas page", "chemicals page", "mining page", "pulp paper page", "airports page",
  or any request to write, edit, or review content for an industry-specific page. Also trigger
  when adding sections like "industry challenges", "industry proof", "why SAM4 works for [industry]",
  "industry FAQ", or "industry case studies" to any page. This skill supersedes samotics-website-content
  for industry pages — it has the industry-specific page framework, section order, narrative arc,
  persuasion logic, CSS conventions, and content rules that the general website skill does not.
  Always load this skill before touching an industry page.
---

# Industry Page Builder

## Job

Build and maintain the industry vertical pages under `/industries/`. This skill owns the page framework, section order, narrative arc, CSS conventions, and content rules specific to industry pages. It encodes the persuasion logic: each section earns one belief shift, in sequence, moving the visitor from "Is this relevant to my sector?" to "I'm ready to act."

Industry pages serve the **Problem Recognition** and **Solution Exploration** buying motions. The target audience is a Reliability Manager (primary) or Operations Director (secondary) who has landed on the page from organic search, the homepage industry routing section, or a proof page backlink. They are asking one question: "Does this company understand my world?"

---

## Strategic positioning

Three claims, in priority order. Every industry page makes all three:

1. **We understand this industry's operational reality.** Domain knowledge before product. The engineer decides in the first 10 seconds whether the page was written by someone who knows their world. Generic industrial language ("rotating equipment," "operational efficiency," "facilities") kills this instantly.

2. **We have quantified proof from their peers.** Named customers, named outcomes, named detection stories. Industry pages are proof pages — not brochures. If evidence is thin for a vertical, say so and show what exists honestly.

3. **ESA solves a constraint that traditional monitoring cannot.** Every industry has a specific reason sensors fail — wet wells, ATEX zones, underground access, distributed networks. The page must name that constraint and explain how ESA bypasses it from the MCC.

---

## Reference files

Three files in `references/`. Read them in order before building or editing any industry page.

| File | Read when | Contents |
|---|---|---|
| `page-framework.md` | Always — before any industry page work | The 9-section page structure with narrative arc, content rules per section, persuasion logic, per-industry adaptation table, and background alternation rules. This is the master document. |
| `css-conventions.md` | Building or editing HTML on any industry page | Dual token system, BEM class patterns, background alternation rules, responsive breakpoints, and component-level CSS specs for hero overlays, trust bars, challenge cards, proof highlights, install sections, FAQ accordions, and terminal CTAs. |
| `per-industry-guide.md` | Writing or editing content for a specific vertical | Industry-specific data: which customers to show, which challenges to name, which assets to feature, which case studies to link, which FAQ objections to address, which regulatory angles apply, and where evidence is thin. |

### Reading order

**Building a new industry page:**
1. `page-framework.md` — understand the 9-section structure and narrative arc
2. `css-conventions.md` — learn the established HTML/CSS patterns
3. `per-industry-guide.md` — get the industry-specific content inputs
4. Also load: `samotics-design-system` (colours, typography, spacing), `samotics-content-writing` (voice and tone), `industry-lexicon` (sector terminology — non-negotiable for credibility)

**Editing an existing section on an industry page:**
1. `page-framework.md` — check what that section should contain
2. `css-conventions.md` — match the established patterns
3. `per-industry-guide.md` if changing industry-specific content

**Reviewing or auditing an industry page:**
1. `page-framework.md` — run the narrative arc check and per-section requirements
2. `css-conventions.md` — check background alternation, token usage, responsive rules
3. `per-industry-guide.md` — verify industry-specific claims and evidence

---

## Page structure (9 sections)

Every industry page follows this structure. The framework is the same across all verticals; the content shifts per industry.

| # | Section | Background | Belief shift |
|---|---|---|---|
| 1 | Hero | Dark overlay on industry image | "This is about my specific problem." |
| 2 | Trust bar | Inherits | "Real companies in my sector use this." |
| 3 | The problem (challenges) | White | "Yes, this is the pain I live with." |
| 4 | Why SAM4 (differentiators) | Seashell | "That's why sensors fail — and this is different." |
| 5 | What we monitor (assets) | White | "They monitor the exact equipment I run." |
| 6 | Proof (case studies) | Seashell | "Here's quantified evidence from my peers." |
| 7 | Installation | White | "This is easier to deploy than I expected." |
| 8 | FAQ | Seashell | "My remaining objections are addressed." |
| 9 | Terminal CTA | Dark | "I'm ready to act." |

Background alternation rule: no two consecutive sections may share the same background colour. If a section is removed, recolour adjacent sections to maintain alternation. The trust bar inherits and does not count in the alternation sequence.

The section order reflects the **proof stack** persuasion logic: Problem → Identity → Pain → Mechanism → Relevance → Evidence → Risk Reduction → Objection Handling → Action. Each section earns the right for the next section to exist.

Full section-by-section content specs, narrative arc, and per-industry adaptation table are in `references/page-framework.md`.

---

## Key content rules

1. **Hero frames the problem, not the product.** The headline names the blind spot. SAM4 enters later. A hero that leads with "SAM4 monitors..." has failed.
2. **Challenges come before differentiators.** The visitor must feel the problem before hearing the solution. Placing "Why SAM4" before "The problem" violates the persuasion sequence.
3. **Section 3 does NOT mention SAM4 or ESA.** Pure domain content. Name the operational risks in the customer's language. Earn credibility before introducing the product.
4. **Section 4 bridges the gap.** After the visitor recognises the problem, section 4 explains why traditional approaches fail and how ESA bypasses the constraint. This is the mechanism bridge between problem and proof.
5. **No hedge language around proof.** Never qualify with "early results," "growing vertical," "strongest proof points." The numbers do the work. If scope is limited, state it factually ("across two sites") without editorialising.
6. **FAQ addresses real sales objections.** Source objections from sales calls for that vertical. Not generic questions. The primary objection for each industry should be addressed head-on.
7. **Mid-page CTA after proof.** Visitors convinced by the proof section should not have to scroll past installation and FAQ to act. Add a secondary CTA (text link or outline button) after the proof section.
8. **Industry-lexicon is non-negotiable.** Load the `industry-lexicon` skill before writing any industry page content. Generic language destroys credibility with engineers.
9. **All stats require measurement method boxes.** Every quantified claim must include methodology attribution. This is a differentiation choice — competitors don't do it.

---

## Per-industry emphasis

Not all sections carry equal weight on every page. The framework is the same but emphasis shifts:

| Industry | Primary constraint | Strongest proof | Key challenge framing |
|---|---|---|---|
| Water & Wastewater | Pumps underground / in wet wells | Yorkshire Water (5,000+ pumps, £20M+) | Pollution events, regulatory fines, inspection cost |
| Oil & Gas | ATEX zones, hazardous areas | ADNOC, Shell | Safety cases, explosion risk, access restrictions |
| Chemicals | ATEX + process safety | Currenta, AstraZeneca | SEVESO compliance, continuous process, sensor access |
| Metals & Mining | Harsh environment, distributed | Site-specific | Conveyor downtime, mill availability, remote access |
| Pulp & Paper | Energy cost, distributed mills | Site-specific | Energy waste, drying section reliability, remote sites |
| Airports | Baggage handling continuity | Site-specific | Conveyor uptime, passenger impact, distributed assets |

Full per-industry content inputs are in `references/per-industry-guide.md`.

---

## Cross-skill loading

When building or editing an industry page, also load these skills:

| Skill | Why |
|---|---|
| `samotics-design-system` | Colours, typography, spacing, card patterns, responsive rules |
| `samotics-content-writing` | Brand voice, tone, writing rules, banned words |
| `industry-lexicon` | Sector-specific terminology — the difference between credible and generic |
| `technical-proof-architect` | Evidence validation for proof section stats and measurement method boxes |
| `samotics-gtm-intelligence` | Buyer personas and buying motions for CTA and FAQ targeting |
| `failure-mode-explainer` | Technical substance for challenges section (failure physics per industry) |
| `plant-walkthrough-story-builder` | Detection narratives for proof section case study cards |

---

## What this skill does NOT do

| Out of scope | Who does it |
|---|---|
| General website structure, nav, site architecture | samotics-website-content |
| Asset monitoring pages under /platform/what-we-monitor/ | asset-page-builder |
| Visual design tokens, colour system, typography scale | samotics-design-system |
| Writing voice and tone rules | samotics-content-writing |
| GTM strategy, buyer personas, buying stages | samotics-gtm-intelligence |
| Competitive positioning and battlecards | competitive-intelligence |
| Technology/ESA explainer pages | samotics-website-content |
