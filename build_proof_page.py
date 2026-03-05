#!/usr/bin/env python3
"""Build a unified Proof page combining case studies and detection stories with filters."""
import os, re, json

DIST = os.path.join(os.path.dirname(__file__), 'dist')
CS_PAGE = os.path.join(DIST, 'resources', 'case-studies', 'index.html')
PROOF_PAGE = os.path.join(DIST, 'proof', 'index.html')

# ── Read case studies page as template for header/footer chrome ──
with open(CS_PAGE) as f:
    cs_html = f.read()

# Extract header (everything up to and including </header>)
header_end = cs_html.index('</header>') + len('</header>')
header = cs_html[:header_end]

# Extract footer (from <!-- Pre-footer CTA --> or the prefooter section)
footer_marker = '<!-- Pre-footer CTA -->'
if footer_marker in cs_html:
    footer_start = cs_html.index(footer_marker)
else:
    footer_start = cs_html.index('<footer')
footer = cs_html[footer_start:]
# Remove the closing script tags and body/html that come with it
if '</body>' not in footer:
    footer += '\n</body>\n</html>'

# Fix title
header = header.replace('<title>Case Studies | Samotics</title>', '<title>Proof | Samotics</title>')
header = header.replace('Real-world results from SAM4 deployments across industries.', 'Detection stories and case studies from SAM4 deployments worldwide.')

# Remove the meta redirect if present
header = header.replace('<meta http-equiv="refresh" content="0;url=/resources/case-studies/">\n', '')

# ── Define all items ──
# Each item: { title, url, type, asset, fault, industry, excerpt }

ITEMS = [
    # ── Case Studies (35) ──
    {"title": "Improving baggage handling reliability at London Stansted", "url": "/resources/case-studies/improving-baggage-handling-reliability-at-london-stansted/", "type": "Case study", "asset": "Conveyor", "fault": "Mechanical wear", "industry": "Aviation", "excerpt": "How Stansted airport uses SAM4 to monitor baggage handling equipment continuously without interrupting operations."},
    {"title": "Improving submersible pump efficiency at Sabesp", "url": "/resources/case-studies/improving-submersible-pump-efficiency-at-sabesp/", "type": "Case study", "asset": "Submersible pump", "fault": "Energy inefficiency", "industry": "Water", "excerpt": "Sabesp unlocked real-time visibility into submersible pump performance, improving efficiency across thousands of assets."},
    {"title": "How zinc smelter Nyrstar got 800% ROI in 11 months", "url": "/resources/case-studies/how-zinc-smelter-nyrstar-got-800-roi-in-11-months/", "type": "Case study", "asset": "Pump", "fault": "Multiple", "industry": "Mining & metals", "excerpt": "Nyrstar moved from reactive firefighting to planned maintenance, achieving 800% ROI in under a year."},
    {"title": "Identifying a broken sine wave filter in ESPs", "url": "/resources/case-studies/identifying-and-fixing-a-broken-sine-wave-filter-in-electric-submersible-pumps/", "type": "Case study", "asset": "Submersible pump", "fault": "Electrical fault", "industry": "Oil & gas", "excerpt": "SAM4 detected irregular harmonic patterns and voltage imbalance on an ESP that other systems missed."},
    {"title": "Southern Water: preventing 3 failures, saving £748K", "url": "/resources/case-studies/southern-waters-success-story-preventing-3-failures-saving-748k-and-ensuring-resilience/", "type": "Case study", "asset": "Sewage pump", "fault": "Cavitation", "industry": "Water", "excerpt": "SAM4 detected three potential failures across 637 monitored pumps, preventing pollution incidents."},
    {"title": "9x common faults detected in steel manufacturing", "url": "/resources/case-studies/common-faults-steel-manufacturing/", "type": "Case study", "asset": "Roller conveyor", "fault": "Multiple", "industry": "Steel", "excerpt": "How SAM4 detects common faults in steel mills using actual anonymized results."},
    {"title": "How Schiphol Airport improved baggage handling reliability", "url": "/resources/case-studies/schiphol-success-story-2/", "type": "Case study", "asset": "Conveyor", "fault": "Mechanical wear", "industry": "Aviation", "excerpt": "Schiphol maximised the efficiency and reliability of its existing baggage handling lines with SAM4."},
    {"title": "How Vitens increased operational efficiency by 7%", "url": "/resources/case-studies/how-vitens-increased-operational-efficiency-by-7-through-real-time-asset-measurements/", "type": "Case study", "asset": "Booster pump", "fault": "Energy inefficiency", "industry": "Water", "excerpt": "Vitens used real-time measurements to improve pump efficiency and reduce energy consumption."},
    {"title": "How ArcelorMittal prevented 31 hours of downtime", "url": "/resources/case-studies/how-arcelormittal-prevented-31-hours-of-downtime-by-detecting-27-failures-ahead-of-time/", "type": "Case study", "asset": "Roller conveyor", "fault": "Multiple", "industry": "Steel", "excerpt": "SAM4 detected 27 failures ahead of time on hard-to-reach assets in a continuous steel production line."},
    {"title": "How Yorkshire Water saved £390k in potential fines", "url": "/resources/case-studies/how-yorkshire-water-saved-390k-in-potential-fine-with-samotics/", "type": "Case study", "asset": "Sewage pump", "fault": "Clogging", "industry": "Water", "excerpt": "Yorkshire Water transformed its maintenance operations with SAM4 clogging detection technology."},
    {"title": "Preventing downtime on borehole pumps", "url": "/resources/case-studies/preventing-downtime-on-borehole-pumps/", "type": "Case study", "asset": "Borehole pump", "fault": "Bearing damage", "industry": "Water", "excerpt": "How SAM4 monitors submerged borehole pumps to prevent unexpected failures in water distribution."},
    {"title": "Preventing failure in wastewater inlet screws", "url": "/resources/case-studies/preventing-failure-in-wastewater-inlet-screws/", "type": "Case study", "asset": "Screw pump", "fault": "Belt degradation", "industry": "Water", "excerpt": "SAM4 catches the top three screw pump failure modes remotely and in advance."},
    {"title": "Clogging detection identifies blockage outside the pump", "url": "/resources/case-studies/yorkshire-water-external-clogging-detection-case/", "type": "Case study", "asset": "Sewage pump", "fault": "Clogging", "industry": "Water", "excerpt": "SAM4 detected a developing blockage event on a sewage pump at Yorkshire Water."},
    {"title": "Early alerts prevent pollution event at Yorkshire Water", "url": "/resources/case-studies/yorkshire-water-case-study-preventing-pollution/", "type": "Case study", "asset": "Sewage pump", "fault": "Clogging", "industry": "Water", "excerpt": "SAM4 provided early warning of developing pump blockage, avoiding a pollution incident."},
    {"title": "16x early alerts to degrading rollers save €650k", "url": "/resources/case-studies/hot-strip-mill-degrading-rollers/", "type": "Case study", "asset": "Roller conveyor", "fault": "Bearing damage", "industry": "Steel", "excerpt": "Consistent early fault detection in roller conveyors keeps hot strip mill production on track."},
    {"title": "Early alerts on degrading oxidation ditch rotor", "url": "/resources/case-studies/oxidation-ditch-rotor-fault-detection-case-study/", "type": "Case study", "asset": "Rotor", "fault": "Gearbox degradation", "industry": "Water", "excerpt": "SAM4 provided early warning of gearbox degradation that the vibration system had missed."},
    {"title": "Six early alerts to degrading fans save €96k", "url": "/resources/case-studies/prevent-exhaust-fan-failure-in-wood-manufacturing-case-study/", "type": "Case study", "asset": "Fan", "fault": "Mechanical wear", "industry": "Manufacturing", "excerpt": "SAM4 detected 6 faults on exhaust fans, preventing 12 hours of unplanned downtime."},
    {"title": "Two pollution events prevented, €840k saved", "url": "/resources/case-studies/two-pollution-events-prevented-and-eur-840k-saved-on-repairs-and-emergency-mitigation/", "type": "Case study", "asset": "Screw pump", "fault": "Belt degradation", "industry": "Water", "excerpt": "SAM4 spotted belt issues in inlet screws early, saving close to a million in total."},
    {"title": "Early warning of failing heated godet roll", "url": "/resources/case-studies/heated-godet-roll-fault-detection-case-study/", "type": "Case study", "asset": "Godet roll", "fault": "Motor overload", "industry": "Manufacturing", "excerpt": "SAM4 detected motor overloading in a heated godet roll, saving $90k in production loss."},
    {"title": "Alert prevents pollution event, saves €100k", "url": "/resources/case-studies/alert-prevents-pollution-event-and-saves-eur-100k/", "type": "Case study", "asset": "Sewage pump", "fault": "Impeller damage", "industry": "Water", "excerpt": "SAM4 detected a broken impeller that vibration monitoring had missed."},
    {"title": "Rightsizing booster pumps to save €121k/year", "url": "/resources/case-studies/rightsizing-booster-pumps-to-save-wasted-energy/", "type": "Case study", "asset": "Booster pump", "fault": "Energy inefficiency", "industry": "Chemicals", "excerpt": "SAM4 identified a pump-system mismatch consuming 813 MWh more than needed annually."},
    {"title": "Aeration blowers: 5% energy saving overnight", "url": "/resources/case-studies/aeration-blowers-energy-waste-reduction-case-study/", "type": "Case study", "asset": "Blower", "fault": "Energy inefficiency", "industry": "Water", "excerpt": "SAM4 Energy identified a control strategy change that would save €120k/year with no capex."},
    {"title": "Wastewater inlet station energy cost reduced by €42k/year", "url": "/resources/case-studies/reducing-wastewater-inlet-station-energy-costs/", "type": "Case study", "asset": "Screw pump", "fault": "Energy inefficiency", "industry": "Water", "excerpt": "SAM4 determined that a single screw pump could handle all dry-weather flow."},
    {"title": "Rerating booster pumps to save €99k/year", "url": "/resources/case-studies/booster-pump-energy-optimization-case-study/", "type": "Case study", "asset": "Booster pump", "fault": "Energy inefficiency", "industry": "Water", "excerpt": "Hydraulic rerating of one booster pump pays for itself in less than 7 months."},
    {"title": "Preventing downtime on belt-driven equipment", "url": "/resources/case-studies/preventing-downtime-on-belt-driven-equipment/", "type": "Case study", "asset": "Belt-driven equipment", "fault": "Belt degradation", "industry": "Chemicals", "excerpt": "How SAM4 monitors belt-driven assets in ATEX zones and harsh environments."},
    {"title": "Condition monitoring for centrifugal pumps", "url": "/resources/case-studies/condition-monitoring-centrifugal-pump/", "type": "Case study", "asset": "Centrifugal pump", "fault": "Process issue", "industry": "Tank storage", "excerpt": "SAM4 alerted to suboptimal pump operation, enabling adjustments to avoid chronic damage."},
    {"title": "Condition monitoring for wastewater pumps", "url": "/resources/case-studies/condition-monitoring-wastewater-pump-detect-clogging/", "type": "Case study", "asset": "Sewage pump", "fault": "Clogging", "industry": "Water", "excerpt": "SAM4 detected debris clogging a wastewater collection pump's intake."},
    {"title": "Loose cardan joint caught same day SAM4 installed", "url": "/resources/case-studies/loose-cardan-joint-caught-the-same-day-sam4-was-installed/", "type": "Case study", "asset": "Roller conveyor", "fault": "Coupling fault", "industry": "Steel", "excerpt": "SAM4 caught a loose cardan shaft coupling within hours of installation."},
    {"title": "Condition monitoring for shot blasting machines", "url": "/resources/case-studies/condition-monitoring-shot-blasting-machine/", "type": "Case study", "asset": "Shot blaster", "fault": "Mechanical wear", "industry": "Steel", "excerpt": "SAM4 caught a loose blast wheel belt guard before it caused damage."},
    {"title": "Failing cardan shaft coupling in runout table", "url": "/resources/case-studies/case-study-steel-runout-table-cardan-shaft-coupling/", "type": "Case study", "asset": "Roller conveyor", "fault": "Coupling fault", "industry": "Steel", "excerpt": "SAM4 caught a failing cardan shaft coupling in a runout table roll."},
    {"title": "Condition monitoring for oil transfer pumps", "url": "/resources/case-studies/condition-monitoring-oil-transfer-pump/", "type": "Case study", "asset": "Transfer pump", "fault": "Coupling fault", "industry": "Tank storage", "excerpt": "SAM4 spotted coupling, vane and foundation issues before pump failure."},
    {"title": "Condition monitoring for cooling pumps", "url": "/resources/case-studies/condition-monitoring-cooling-pump-misalignment-unbalance/", "type": "Case study", "asset": "Cooling pump", "fault": "Misalignment", "industry": "Food & beverage", "excerpt": "SAM4 caught a missing foundation bolt in a cooling pump."},
    {"title": "Bearing failure avoided in runout table roll motor", "url": "/resources/case-studies/case-study-steel-runout-table-roll-bearing/", "type": "Case study", "asset": "Roller conveyor", "fault": "Bearing damage", "industry": "Steel", "excerpt": "SAM4 caught motor bearing failure 7 months in advance."},
    {"title": "Condition monitoring for circulator pumps", "url": "/resources/case-studies/condition-monitoring-circulator-pump-misalignment-gearbox/", "type": "Case study", "asset": "Circulator pump", "fault": "Misalignment", "industry": "Chemicals", "excerpt": "SAM4 caught gearbox-motor misalignment 7 months in advance."},
    {"title": "Condition monitoring for anolyte pumps", "url": "/resources/case-studies/condition-monitoring-for-anolyte-pumps-a-case-study/", "type": "Case study", "asset": "Anolyte pump", "fault": "Cavitation", "industry": "Chemicals", "excerpt": "SAM4 saved a chemical manufacturer €15k by detecting cavitation-induced damage."},

    # ── Detection Stories (17) ──
    {"title": "Bearing failure avoided in runout table roll", "url": "/proof/case-studies/bearing-failure-motor-roll/", "type": "Detection story", "asset": "Roller conveyor", "fault": "Bearing damage", "industry": "Steel", "excerpt": "SAM4 detected bearing degradation in a motor driving a critical runout table roll."},
    {"title": "Belt degradation in circulation pump", "url": "/proof/case-studies/belt-degradation-circulation-pump/", "type": "Detection story", "asset": "Circulator pump", "fault": "Belt degradation", "industry": "Chemicals", "excerpt": "Belt degradation detected in a critical circulation pump before rupture."},
    {"title": "Preventing downtime on belt-driven assets", "url": "/proof/case-studies/belt-driven-assets/", "type": "Detection story", "asset": "Belt-driven equipment", "fault": "Belt degradation", "industry": "Chemicals", "excerpt": "Monitoring belt-driven pumps, conveyors and fans in restricted-access zones."},
    {"title": "Preventing downtime on borehole pumps", "url": "/proof/case-studies/borehole-pump-detections/", "type": "Detection story", "asset": "Borehole pump", "fault": "Multiple", "industry": "Water", "excerpt": "How SAM4 monitors submerged borehole pumps to prevent failures in water distribution."},
    {"title": "Failing cardan shaft coupling in runout table", "url": "/proof/case-studies/cardan-shaft-coupling-roller/", "type": "Detection story", "asset": "Roller conveyor", "fault": "Coupling fault", "industry": "Steel", "excerpt": "SAM4 detected a failing cardan shaft coupling in a steel runout table roller."},
    {"title": "Anolyte pump saved from complete breakdown", "url": "/proof/case-studies/cavitation-anolyte-pump/", "type": "Detection story", "asset": "Anolyte pump", "fault": "Cavitation", "industry": "Chemicals", "excerpt": "SAM4 detected cavitation-induced damage and prevented total pump failure."},
    {"title": "Process insights prevent damage to centrifugal pump", "url": "/proof/case-studies/cavitation-centrifugal-pump/", "type": "Detection story", "asset": "Centrifugal pump", "fault": "Cavitation", "industry": "Tank storage", "excerpt": "SAM4 provided process insights to prevent long-term damage to a 200 kW centrifugal pump."},
    {"title": "Borehole pump clogging detected nearly one year early", "url": "/proof/case-studies/clogging-borehole-pump/", "type": "Detection story", "asset": "Borehole pump", "fault": "Clogging", "industry": "Water", "excerpt": "SAM4 detected developing clogging in a borehole pump nearly a year before failure."},
    {"title": "Debris clogging in wastewater collection pump", "url": "/proof/case-studies/clogging-wastewater-pump/", "type": "Detection story", "asset": "Sewage pump", "fault": "Clogging", "industry": "Water", "excerpt": "SAM4 alerted to debris clogging a wastewater pump's intake."},
    {"title": "Yorkshire Water prevents pollution with clogging detection", "url": "/proof/case-studies/clogging-yorkshire-water-sewage/", "type": "Detection story", "asset": "Sewage pump", "fault": "Clogging", "industry": "Water", "excerpt": "Automated clogging detection prevented a pollution event at Yorkshire Water."},
    {"title": "7 months warning on gearbox-motor misalignment", "url": "/proof/case-studies/gearbox-misalignment-circulator-pump/", "type": "Detection story", "asset": "Circulator pump", "fault": "Misalignment", "industry": "Chemicals", "excerpt": "SAM4 gave 7 months advance warning on gearbox-motor misalignment in a 160 kW pump."},
    {"title": "Preventing failure in wastewater inlet screws", "url": "/proof/case-studies/inlet-screw-monitoring/", "type": "Detection story", "asset": "Screw pump", "fault": "Belt degradation", "industry": "Water", "excerpt": "SAM4 catches the top three screw pump failure modes remotely and in advance."},
    {"title": "Loose belt guard caught in shot blasting machine", "url": "/proof/case-studies/loose-belt-guard-shot-blasting/", "type": "Detection story", "asset": "Shot blaster", "fault": "Mechanical wear", "industry": "Steel", "excerpt": "A loose belt guard was detected early before causing damage to the shot blasting machine."},
    {"title": "Loose cardan joint caught same day SAM4 installed", "url": "/proof/case-studies/loose-cardan-joint-roll/", "type": "Detection story", "asset": "Roller conveyor", "fault": "Coupling fault", "industry": "Steel", "excerpt": "SAM4 caught a loose cardan joint within hours of installation on a runout table roll."},
    {"title": "Missing bolt caught in 90 kW cooling pump", "url": "/proof/case-studies/missing-bolt-cooling-pump/", "type": "Detection story", "asset": "Cooling pump", "fault": "Misalignment", "industry": "Food & beverage", "excerpt": "SAM4 detected a missing foundation bolt causing misalignment in a cooling pump."},
    {"title": "Preventing failure in synthetic fiber production", "url": "/proof/case-studies/synthetic-fiber-production/", "type": "Detection story", "asset": "Godet roll", "fault": "Motor overload", "industry": "Manufacturing", "excerpt": "SAM4 detected developing issues in heated godet rolls used in synthetic fiber production."},
    {"title": "Three faults fixed in oil transfer pump", "url": "/proof/case-studies/three-faults-oil-transfer-pump/", "type": "Detection story", "asset": "Transfer pump", "fault": "Coupling fault", "industry": "Tank storage", "excerpt": "SAM4 spotted coupling, vane and foundation issues before complete pump failure."},
]

# ── Collect unique filter values ──
assets = sorted(set(i["asset"] for i in ITEMS))
faults = sorted(set(i["fault"] for i in ITEMS))
industries = sorted(set(i["industry"] for i in ITEMS))
types = sorted(set(i["type"] for i in ITEMS))

print(f"Total items: {len(ITEMS)}")
print(f"  Case studies: {sum(1 for i in ITEMS if i['type'] == 'Case study')}")
print(f"  Detection stories: {sum(1 for i in ITEMS if i['type'] == 'Detection story')}")
print(f"Assets: {len(assets)}, Faults: {len(faults)}, Industries: {len(industries)}")

# ── Build page CSS ──
PAGE_CSS = """
/* ── Proof Listing Page ── */
.sam-proof-listing { max-width: 1200px; margin: 0 auto; padding: 0 24px; }

/* Hero */
.sam-proof-hero { background: var(--sam-seashell); padding: 64px 24px 48px; }
.sam-proof-hero__inner { max-width: 1200px; margin: 0 auto; }
.sam-proof-hero h1 { font-family: var(--sam-font); font-size: 2.8rem; font-weight: 700; color: var(--sam-space-cadet); margin: 0 0 16px; }
.sam-proof-hero .lead { font-family: var(--sam-font); font-size: 1.1rem; color: var(--sam-comet); line-height: 1.6; max-width: 70ch; margin: 0; }
.overline { font-family: var(--sam-font); font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin: 0 0 8px; }

/* Stats bar */
.sam-proof-stats { display: flex; gap: 48px; margin-top: 32px; }
.sam-proof-stats__item { display: flex; flex-direction: column; }
.sam-proof-stats__value { font-family: var(--sam-font); font-size: 2rem; font-weight: 700; color: var(--sam-space-cadet); }
.sam-proof-stats__label { font-family: var(--sam-font); font-size: 0.85rem; color: var(--sam-comet); margin-top: 4px; }

/* Filters */
.sam-proof-filter { padding: 32px 0; }
.sam-proof-filter__bar { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.sam-proof-filter__label { font-family: var(--sam-font); font-weight: 600; color: var(--sam-space-cadet); font-size: 0.95rem; white-space: nowrap; }
.sam-proof-filter__selects { display: flex; gap: 10px; flex-wrap: wrap; }
.sam-proof-filter__select {
  font-family: var(--sam-font); font-size: 0.9rem;
  padding: 8px 32px 8px 12px;
  border: 1px solid var(--sam-border-light); border-radius: 6px;
  background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' fill='none' stroke='%235A6A80' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat right 10px center;
  -webkit-appearance: none; appearance: none;
  color: var(--sam-space-cadet); cursor: pointer; min-width: 160px;
  transition: border-color 200ms;
}
.sam-proof-filter__select:hover, .sam-proof-filter__select:focus { border-color: var(--sam-orange); outline: none; }
.sam-proof-filter__clear { font-family: var(--sam-font); font-size: 0.85rem; font-weight: 600; color: var(--sam-orange); background: none; border: none; cursor: pointer; padding: 4px 0; white-space: nowrap; display: none; }
.sam-proof-filter__clear:hover { text-decoration: underline; }
.sam-proof-filter__count { font-family: var(--sam-font); font-size: 0.85rem; color: var(--sam-comet); margin-left: auto; white-space: nowrap; }

/* Grid */
.sam-proof-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; padding-bottom: 64px; }

/* Cards */
.sam-proof-card {
  display: flex; flex-direction: column;
  background: var(--sam-white); border: 1px solid var(--sam-border-light);
  border-radius: 12px; overflow: hidden; text-decoration: none;
  transition: box-shadow 200ms ease-out, transform 200ms ease-out;
  padding: 24px;
}
.sam-proof-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }
.sam-proof-card[data-hidden="true"] { display: none !important; }
.sam-proof-card__badges { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
.sam-proof-card__badge {
  font-family: var(--sam-font); font-size: 0.75rem; font-weight: 600;
  padding: 3px 8px; border-radius: 4px;
}
.sam-proof-card__badge--type { background: #E8F4FF; color: #005CBA; }
.sam-proof-card__badge--detection { background: #FFE8D6; color: #FF5429; }
.sam-proof-card__badge--industry { background: #D6F5F1; color: #0098AC; }
.sam-proof-card__title { font-family: var(--sam-font); font-size: 1.05rem; font-weight: 700; color: var(--sam-space-cadet); margin: 0 0 8px; line-height: 1.4; }
.sam-proof-card__excerpt { font-family: var(--sam-font); font-size: 0.9rem; color: var(--sam-comet); line-height: 1.6; margin: 0; flex: 1; }
.sam-proof-card__link { color: var(--sam-orange); font-weight: 600; font-size: 0.9rem; margin-top: 16px; display: inline-flex; align-items: center; gap: 6px; }

@media (max-width: 991px) {
  .sam-proof-hero h1 { font-size: 2.2rem; }
  .sam-proof-grid { grid-template-columns: repeat(2, 1fr); }
  .sam-proof-stats { gap: 32px; flex-wrap: wrap; }
}
@media (max-width: 600px) {
  .sam-proof-hero h1 { font-size: 1.75rem; }
  .sam-proof-grid { grid-template-columns: 1fr; }
  .sam-proof-filter__bar { flex-direction: column; align-items: stretch; }
  .sam-proof-filter__selects { flex-direction: column; }
  .sam-proof-filter__select { min-width: 100%; }
  .sam-proof-filter__count { margin-left: 0; }
  .sam-proof-stats { gap: 24px; }
}
"""

# ── Build cards HTML ──
cards_html = ""
for item in ITEMS:
    badge_class = "sam-proof-card__badge--type" if item["type"] == "Case study" else "sam-proof-card__badge--detection"
    cards_html += f"""
      <a href="{item['url']}" class="sam-proof-card" data-type="{item['type']}" data-asset="{item['asset']}" data-fault="{item['fault']}" data-industry="{item['industry']}">
        <div class="sam-proof-card__badges">
          <span class="sam-proof-card__badge {badge_class}">{item['type']}</span>
          <span class="sam-proof-card__badge sam-proof-card__badge--industry">{item['industry']}</span>
        </div>
        <h3 class="sam-proof-card__title">{item['title']}</h3>
        <p class="sam-proof-card__excerpt">{item['excerpt']}</p>
        <span class="sam-proof-card__link">Read more <span style="font-size: 1.2em;">→</span></span>
      </a>"""

# ── Build filter options ──
def options_html(label, attr, values):
    opts = f'<option value="">All {label}</option>'
    for v in values:
        opts += f'<option value="{v}">{v}</option>'
    return f'<select class="sam-proof-filter__select" data-filter="{attr}">{opts}</select>'

# ── Build JS ──
JS = """
<script>
(function() {
  const selects = document.querySelectorAll('.sam-proof-filter__select');
  const clearBtn = document.getElementById('proof-filter-clear');
  const countEl = document.getElementById('proof-filter-count');
  const cards = document.querySelectorAll('.sam-proof-card');
  const total = cards.length;

  function applyFilters() {
    const filters = {};
    let anyActive = false;
    selects.forEach(s => {
      const attr = s.dataset.filter;
      const val = s.value;
      if (val) { filters[attr] = val; anyActive = true; }
    });

    let visible = 0;
    cards.forEach(card => {
      let show = true;
      for (const [attr, val] of Object.entries(filters)) {
        if (card.dataset[attr] !== val) { show = false; break; }
      }
      card.setAttribute('data-hidden', !show);
      if (show) visible++;
    });

    clearBtn.style.display = anyActive ? '' : 'none';
    countEl.textContent = anyActive ? visible + ' of ' + total + ' shown' : total + ' results';
    selects.forEach(s => { s.style.borderColor = s.value ? '#FF5429' : ''; });
  }

  selects.forEach(s => s.addEventListener('change', applyFilters));
  clearBtn.addEventListener('click', () => {
    selects.forEach(s => { s.value = ''; });
    applyFilters();
  });
  applyFilters();
})();
</script>
"""

# ── Assemble page ──
BODY = f"""
<main>
  <section class="sam-proof-hero">
    <div class="sam-proof-hero__inner">
      <p class="overline" style="color: var(--sam-orange);">Proof</p>
      <h1>Detection stories and case studies</h1>
      <p class="lead">Real results from SAM4 deployments across water, steel, chemicals, mining, and more. Every story backed by validated data.</p>
      <div class="sam-proof-stats">
        <div class="sam-proof-stats__item">
          <span class="sam-proof-stats__value">52</span>
          <span class="sam-proof-stats__label">Stories</span>
        </div>
        <div class="sam-proof-stats__item">
          <span class="sam-proof-stats__value">9</span>
          <span class="sam-proof-stats__label">Industries</span>
        </div>
        <div class="sam-proof-stats__item">
          <span class="sam-proof-stats__value">19</span>
          <span class="sam-proof-stats__label">Asset types</span>
        </div>
        <div class="sam-proof-stats__item">
          <span class="sam-proof-stats__value">14</span>
          <span class="sam-proof-stats__label">Fault types</span>
        </div>
      </div>
    </div>
  </section>

  <div class="sam-proof-listing">
    <div class="sam-proof-filter">
      <div class="sam-proof-filter__bar">
        <span class="sam-proof-filter__label">Filter by:</span>
        <div class="sam-proof-filter__selects">
          {options_html("resource types", "type", types)}
          {options_html("asset types", "asset", assets)}
          {options_html("fault types", "fault", faults)}
          {options_html("industries", "industry", industries)}
        </div>
        <button class="sam-proof-filter__clear" id="proof-filter-clear">Clear filters</button>
        <span class="sam-proof-filter__count" id="proof-filter-count"></span>
      </div>
    </div>

    <div class="sam-proof-grid">
{cards_html}
    </div>
  </div>
</main>
"""

# Insert CSS into header (before </style>)
style_close = header.rfind('</style>')
if style_close != -1:
    header = header[:style_close] + PAGE_CSS + '\n</style>' + header[style_close + len('</style>'):]

# Assemble
full_page = header + '\n' + BODY + '\n' + footer
# Insert JS before </body>
full_page = full_page.replace('</body>', JS + '\n</body>')

# Write
with open(PROOF_PAGE, 'w') as f:
    f.write(full_page)

print(f"\nWrote proof page: {PROOF_PAGE}")
print(f"  {len(ITEMS)} cards, 4 filter dimensions")
