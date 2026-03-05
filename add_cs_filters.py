#!/usr/bin/env python3
"""Add asset type / fault type / industry filter selectors to the Case Studies listing page."""
import os, re, json

DIST = os.path.join(os.path.dirname(__file__), 'dist')
PAGE = os.path.join(DIST, 'resources', 'case-studies', 'index.html')

# ── Tag mapping: slug → { asset, fault, industry } ──
TAGS = {
    "improving-baggage-handling-reliability-at-london-stansted": {
        "asset": "Conveyor", "fault": "Mechanical wear", "industry": "Aviation"
    },
    "improving-submersible-pump-efficiency-at-sabesp": {
        "asset": "Submersible pump", "fault": "Energy inefficiency", "industry": "Water"
    },
    "how-zinc-smelter-nyrstar-got-800-roi-in-11-months": {
        "asset": "Pump", "fault": "Multiple", "industry": "Mining & metals"
    },
    "identifying-and-fixing-a-broken-sine-wave-filter-in-electric-submersible-pumps": {
        "asset": "Submersible pump", "fault": "Electrical fault", "industry": "Oil & gas"
    },
    "southern-waters-success-story-preventing-3-failures-saving-748k-and-ensuring-resilience": {
        "asset": "Sewage pump", "fault": "Cavitation", "industry": "Water"
    },
    "common-faults-steel-manufacturing": {
        "asset": "Roller conveyor", "fault": "Multiple", "industry": "Steel"
    },
    "schiphol-success-story-2": {
        "asset": "Conveyor", "fault": "Mechanical wear", "industry": "Aviation"
    },
    "how-vitens-increased-operational-efficiency-by-7-through-real-time-asset-measurements": {
        "asset": "Booster pump", "fault": "Energy inefficiency", "industry": "Water"
    },
    "how-arcelormittal-prevented-31-hours-of-downtime-by-detecting-27-failures-ahead-of-time": {
        "asset": "Roller conveyor", "fault": "Multiple", "industry": "Steel"
    },
    "how-yorkshire-water-saved-390k-in-potential-fine-with-samotics": {
        "asset": "Sewage pump", "fault": "Clogging", "industry": "Water"
    },
    "preventing-downtime-on-borehole-pumps": {
        "asset": "Borehole pump", "fault": "Bearing damage", "industry": "Water"
    },
    "preventing-failure-in-wastewater-inlet-screws": {
        "asset": "Screw pump", "fault": "Belt degradation", "industry": "Water"
    },
    "yorkshire-water-external-clogging-detection-case": {
        "asset": "Sewage pump", "fault": "Clogging", "industry": "Water"
    },
    "yorkshire-water-case-study-preventing-pollution": {
        "asset": "Sewage pump", "fault": "Clogging", "industry": "Water"
    },
    "hot-strip-mill-degrading-rollers": {
        "asset": "Roller conveyor", "fault": "Bearing damage", "industry": "Steel"
    },
    "oxidation-ditch-rotor-fault-detection-case-study": {
        "asset": "Rotor", "fault": "Gearbox degradation", "industry": "Water"
    },
    "prevent-exhaust-fan-failure-in-wood-manufacturing-case-study": {
        "asset": "Fan", "fault": "Mechanical wear", "industry": "Manufacturing"
    },
    "two-pollution-events-prevented-and-eur-840k-saved-on-repairs-and-emergency-mitigation": {
        "asset": "Screw pump", "fault": "Belt degradation", "industry": "Water"
    },
    "heated-godet-roll-fault-detection-case-study": {
        "asset": "Godet roll", "fault": "Motor overload", "industry": "Manufacturing"
    },
    "alert-prevents-pollution-event-and-saves-eur-100k": {
        "asset": "Sewage pump", "fault": "Impeller damage", "industry": "Water"
    },
    "rightsizing-booster-pumps-to-save-wasted-energy": {
        "asset": "Booster pump", "fault": "Energy inefficiency", "industry": "Chemicals"
    },
    "aeration-blowers-energy-waste-reduction-case-study": {
        "asset": "Blower", "fault": "Energy inefficiency", "industry": "Water"
    },
    "reducing-wastewater-inlet-station-energy-costs": {
        "asset": "Screw pump", "fault": "Energy inefficiency", "industry": "Water"
    },
    "booster-pump-energy-optimization-case-study": {
        "asset": "Booster pump", "fault": "Energy inefficiency", "industry": "Water"
    },
    "preventing-downtime-on-belt-driven-equipment": {
        "asset": "Belt-driven equipment", "fault": "Belt degradation", "industry": "Chemicals"
    },
    "condition-monitoring-centrifugal-pump": {
        "asset": "Centrifugal pump", "fault": "Process issue", "industry": "Tank storage"
    },
    "condition-monitoring-wastewater-pump-detect-clogging": {
        "asset": "Sewage pump", "fault": "Clogging", "industry": "Water"
    },
    "loose-cardan-joint-caught-the-same-day-sam4-was-installed": {
        "asset": "Roller conveyor", "fault": "Coupling fault", "industry": "Steel"
    },
    "condition-monitoring-shot-blasting-machine": {
        "asset": "Shot blaster", "fault": "Mechanical wear", "industry": "Steel"
    },
    "case-study-steel-runout-table-cardan-shaft-coupling": {
        "asset": "Roller conveyor", "fault": "Coupling fault", "industry": "Steel"
    },
    "condition-monitoring-oil-transfer-pump": {
        "asset": "Transfer pump", "fault": "Coupling fault", "industry": "Tank storage"
    },
    "condition-monitoring-cooling-pump-misalignment-unbalance": {
        "asset": "Cooling pump", "fault": "Misalignment", "industry": "Food & beverage"
    },
    "case-study-steel-runout-table-roll-bearing": {
        "asset": "Roller conveyor", "fault": "Bearing damage", "industry": "Steel"
    },
    "condition-monitoring-circulator-pump-misalignment-gearbox": {
        "asset": "Circulator pump", "fault": "Misalignment", "industry": "Chemicals"
    },
    "condition-monitoring-for-anolyte-pumps-a-case-study": {
        "asset": "Anolyte pump", "fault": "Cavitation", "industry": "Chemicals"
    },
}

# ── Read page ──
with open(PAGE) as f:
    html = f.read()

# ── Collect unique values for each dimension ──
assets = sorted(set(t["asset"] for t in TAGS.values()))
faults = sorted(set(t["fault"] for t in TAGS.values()))
industries = sorted(set(t["industry"] for t in TAGS.values()))

print(f"Assets: {assets}")
print(f"Faults: {faults}")
print(f"Industries: {industries}")

# ── Step 1: Add data attributes to each card ──
# Pattern: <a href="/resources/case-studies/{slug}/" class="sam-blog-card">
card_re = re.compile(r'<a href="/resources/case-studies/([^/]+)/" class="sam-blog-card">')
updated = 0
for m in list(card_re.finditer(html)):
    slug = m.group(1)
    if slug in TAGS:
        t = TAGS[slug]
        old = m.group(0)
        new = f'<a href="/resources/case-studies/{slug}/" class="sam-blog-card" data-asset="{t["asset"]}" data-fault="{t["fault"]}" data-industry="{t["industry"]}">'
        html = html.replace(old, new, 1)
        updated += 1

print(f"Tagged {updated} cards")

# ── Step 2: Add filter bar HTML before the grid ──
def make_options(label, data_attr, values):
    opts = f'<option value="">All {label}</option>\n'
    for v in values:
        opts += f'              <option value="{v}">{v}</option>\n'
    return f"""          <select id="filter-{data_attr}" class="sam-cs-filter__select" data-filter="{data_attr}">
              {opts.strip()}
            </select>"""

filter_html = f"""
    <div class="sam-cs-filter">
      <div class="sam-cs-filter__bar">
        <span class="sam-cs-filter__label">Filter by:</span>
        <div class="sam-cs-filter__selects">
{make_options("asset types", "asset", assets)}
{make_options("fault types", "fault", faults)}
{make_options("industries", "industry", industries)}
        </div>
        <button class="sam-cs-filter__clear" id="filter-clear" style="display:none;">Clear filters</button>
        <span class="sam-cs-filter__count" id="filter-count"></span>
      </div>
    </div>
"""

# Insert before the grid
html = html.replace(
    '<div class="sam-listing__grid-wrap">',
    filter_html + '\n    <div class="sam-listing__grid-wrap">'
)

# ── Step 3: Add CSS ──
filter_css = """
/* ── Case Study Filters ── */
.sam-cs-filter {
  margin-bottom: var(--sp-08);
}
.sam-cs-filter__bar {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
.sam-cs-filter__label {
  font-family: var(--sam-font);
  font-weight: 600;
  color: var(--sam-space-cadet);
  font-size: 0.95rem;
  white-space: nowrap;
}
.sam-cs-filter__selects {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.sam-cs-filter__select {
  font-family: var(--sam-font);
  font-size: 0.9rem;
  padding: 8px 32px 8px 12px;
  border: 1px solid var(--sam-border-light);
  border-radius: 6px;
  background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' fill='none' stroke='%235A6A80' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat right 10px center;
  -webkit-appearance: none;
  appearance: none;
  color: var(--sam-space-cadet);
  cursor: pointer;
  min-width: 160px;
  transition: border-color 200ms;
}
.sam-cs-filter__select:hover,
.sam-cs-filter__select:focus {
  border-color: var(--sam-orange);
  outline: none;
}
.sam-cs-filter__select:not([value=""]):not(:first-child) {
  border-color: var(--sam-orange);
}
.sam-cs-filter__clear {
  font-family: var(--sam-font);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--sam-orange);
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 0;
  white-space: nowrap;
}
.sam-cs-filter__clear:hover {
  text-decoration: underline;
}
.sam-cs-filter__count {
  font-family: var(--sam-font);
  font-size: 0.85rem;
  color: var(--sam-comet);
  margin-left: auto;
  white-space: nowrap;
}
.sam-blog-card[data-hidden="true"] {
  display: none !important;
}
@media (max-width: 600px) {
  .sam-cs-filter__bar {
    flex-direction: column;
    align-items: stretch;
  }
  .sam-cs-filter__selects {
    flex-direction: column;
  }
  .sam-cs-filter__select {
    min-width: 100%;
  }
  .sam-cs-filter__count {
    margin-left: 0;
  }
}"""

# Insert CSS before closing </style>
# Find last </style> in the head
style_close_pos = html.rfind('</style>')
if style_close_pos == -1:
    # Fallback: insert before </head>
    html = html.replace('</head>', f'<style>{filter_css}</style>\n</head>')
else:
    html = html[:style_close_pos] + filter_css + '\n' + html[style_close_pos:]

# ── Step 4: Add JS ──
filter_js = """
<script>
(function() {
  const selects = document.querySelectorAll('.sam-cs-filter__select');
  const clearBtn = document.getElementById('filter-clear');
  const countEl = document.getElementById('filter-count');
  const cards = document.querySelectorAll('.sam-blog-card[data-asset]');
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
    countEl.textContent = anyActive ? visible + ' of ' + total + ' shown' : total + ' detection stories';

    // Highlight active selects
    selects.forEach(s => {
      s.style.borderColor = s.value ? '#FF5429' : '';
    });
  }

  selects.forEach(s => s.addEventListener('change', applyFilters));
  clearBtn.addEventListener('click', () => {
    selects.forEach(s => { s.value = ''; });
    applyFilters();
  });

  // Init
  applyFilters();
})();
</script>"""

# Insert before </body>
html = html.replace('</body>', filter_js + '\n</body>')

# ── Write ──
with open(PAGE, 'w') as f:
    f.write(html)

print("Done! Filter bar added to case studies listing page.")
