#!/usr/bin/env python3
"""Fix broken internal links across the site."""
import os, re, glob

DIST = os.path.join(os.path.dirname(__file__), 'dist')

# ── Link rewrites: old href → new href ──
REWRITES = {
    # Old /blogs/ paths → /resources/blog/
    '/blogs/condition-based-maintenance-pilot-to-implementation-at-scale-part-1-plan':
        '/resources/blog/condition-based-maintenance-pilot-to-implementation-at-scale-part-1-plan/',
    '/blogs/expert-interview-dirk-jan-wienen-condition-based-maintenance-water-industry':
        '/resources/blog/expert-interview-dirk-jan-wienen-condition-based-maintenance-water-industry/',

    # Shortened case study slugs → full slugs
    '/resources/case-studies/arcelormittal':
        '/resources/case-studies/how-arcelormittal-prevented-31-hours-of-downtime-by-detecting-27-failures-ahead-of-time/',
    '/resources/case-studies/yorkshire-water-case-study':
        '/resources/case-studies/yorkshire-water-case-study-preventing-pollution/',

    # KB slug mismatches
    '/resources/knowledge-base/the-esa-explainer':
        '/resources/knowledge-base/what-is-electrical-signature-analysis-esa/',
    '/resources/knowledge-base/the-esa-explainer-for-hot-strip-mills':
        '/resources/knowledge-base/what-is-electrical-signature-analysis-esa/',

    # Blog cross-links with wrong slugs (these posts don't exist under those slugs)
    '/resources/blog/business-case-predictive-maintenance':
        '/resources/blog/predictive-maintenance-quick-start-guide/',
    '/resources/blog/condition-monitoring-comparison':
        '/resources/blog/what-is-condition-monitoring/',
    '/resources/blog/drive-train-insights-using-electric-motor-as-vibration-sensor':
        '/resources/blog/remote-condition-monitoring-pumps/',

    # Old product/use-case paths
    '/products/sam4-energy': '/platform/sam4/',
    '/use-cases/reduce-energy-waste': '/industries/energy-efficiency/',

    # Site structure: missing /platform/ prefix
    '/security/': '/platform/security/',
    '/integrations/': '/platform/integrations/',
    '/how-it-installs/': '/platform/how-it-installs/',
    '/what-we-monitor/': '/platform/what-we-monitor/',

    # Industry path fixes
    '/industries/steel': '/industries/metals-mining/',
    '/industries/infrastructure/': '/industries/',

    # Tools path fix
    '/tools/roi-calculator/': '/resources/roi-calculator/',
    '/tools/asset-audit/': '/tools/',

    # Resource pages that don't exist → closest match
    '/resources/esg-reporting': '/resources/',
    '/resources/sample-report/': '/resources/',
    '/resources/technical-guide': '/resources/',
    '/resources/technical-guide/': '/resources/',
    '/demo': '/contact/',
    '/contact/partner-inquiry': '/contact/',

    # /proof/case-studies/ old paths → /resources/case-studies/
    '/proof/case-studies/condition-monitoring-anolyte-pump-detecting-cavitation/':
        '/resources/case-studies/condition-monitoring-for-anolyte-pumps-a-case-study/',
    '/proof/case-studies/condition-monitoring-centrifugal-pump/':
        '/resources/case-studies/condition-monitoring-centrifugal-pump/',
    '/proof/case-studies/condition-monitoring-oil-transfer-pump/':
        '/resources/case-studies/condition-monitoring-oil-transfer-pump/',
    '/proof/case-studies/heated-godet-roll-fault-detection-case-study/':
        '/resources/case-studies/heated-godet-roll-fault-detection-case-study/',
    '/proof/case-studies/hot-strip-mill-degrading-rollers/':
        '/resources/case-studies/hot-strip-mill-degrading-rollers/',
    '/proof/case-studies/how-arcelormittal-prevented-31-hours-of-downtime-by-detecting-27-failures-ahead-of-time/':
        '/resources/case-studies/how-arcelormittal-prevented-31-hours-of-downtime-by-detecting-27-failures-ahead-of-time/',
    '/proof/case-studies/how-schipol-airport-improved-reliability-of-its-current-baggage-handling-lines/':
        '/resources/case-studies/schiphol-success-story-2/',
    '/proof/case-studies/how-vitens-increased-operational-efficiency-by-7-through-real-time-asset-measurements/':
        '/resources/case-studies/how-vitens-increased-operational-efficiency-by-7-through-real-time-asset-measurements/',
    '/proof/case-studies/how-zinc-smelter-nyrstar-got-800-roi-in-11-months/':
        '/resources/case-studies/how-zinc-smelter-nyrstar-got-800-roi-in-11-months/',
    '/proof/case-studies/identifying-and-fixing-a-broken-sine-wave-filter-in-electric-submersible-pumps/':
        '/resources/case-studies/identifying-and-fixing-a-broken-sine-wave-filter-in-electric-submersible-pumps/',
    '/proof/case-studies/improving-baggage-handling-reliability-at-london-stansted/':
        '/resources/case-studies/improving-baggage-handling-reliability-at-london-stansted/',
    '/proof/case-studies/improving-submersible-pump-efficiency-at-sabesp/':
        '/resources/case-studies/improving-submersible-pump-efficiency-at-sabesp/',
    '/proof/case-studies/prevent-exhaust-fan-failure-in-wood-manufacturing-case-study/':
        '/resources/case-studies/prevent-exhaust-fan-failure-in-wood-manufacturing-case-study/',
    '/proof/case-studies/preventing-downtime-on-belt-driven-equipment/':
        '/resources/case-studies/preventing-downtime-on-belt-driven-equipment/',
    '/proof/case-studies/rightsizing-booster-pumps-to-save-wasted-energy/':
        '/resources/case-studies/rightsizing-booster-pumps-to-save-wasted-energy/',
    '/proof/case-studies/schiphol-airport/':
        '/resources/case-studies/schiphol-success-story-2/',
    '/proof/case-studies/southern-waters-success-story-preventing-3-failures-saving-748k-and-ensuring-resilience/':
        '/resources/case-studies/southern-waters-success-story-preventing-3-failures-saving-748k-and-ensuring-resilience/',
    '/proof/case-studies/yorkshire-water-avoid-potential-fines-with-samotics/':
        '/resources/case-studies/how-yorkshire-water-saved-390k-in-potential-fine-with-samotics/',

    # Proof filter links → case studies listing
    '/proof/case-studies/?cat=chemicals': '/resources/case-studies/',
    '/proof/case-studies/?cat=infrastructure': '/resources/case-studies/',
    '/proof/case-studies/?cat=metals-mining': '/resources/case-studies/',
    '/proof/case-studies/?cat=oil-gas': '/resources/case-studies/',
    '/proof/case-studies/?cat=water': '/resources/case-studies/',

    # Proof download links → case studies listing (downloads don't exist)
    '/proof/nyrstar/download': '/resources/case-studies/how-zinc-smelter-nyrstar-got-800-roi-in-11-months/',
    '/proof/schiphol/download': '/resources/case-studies/schiphol-success-story-2/',
    '/proof/southern-water/download': '/resources/case-studies/southern-waters-success-story-preventing-3-failures-saving-748k-and-ensuring-resilience/',
    '/proof/thyssenkrupp/download': '/resources/case-studies/',
    '/proof/vitens/download': '/resources/case-studies/how-vitens-increased-operational-efficiency-by-7-through-real-time-asset-measurements/',
    '/proof/yorkshire-water/download': '/resources/case-studies/how-yorkshire-water-saved-390k-in-potential-fine-with-samotics/',
    '/proof/yorkshire-water': '/resources/case-studies/how-yorkshire-water-saved-390k-in-potential-fine-with-samotics/',
    '/proof/yorkshire-water/': '/resources/case-studies/how-yorkshire-water-saved-390k-in-potential-fine-with-samotics/',

    # Problem sub-page
    '/problem/proximity-penalty': '/problem/',
}

# ── Scan and fix ──
html_files = glob.glob(os.path.join(DIST, '**', 'index.html'), recursive=True)
print(f'Scanning {len(html_files)} files...')

total_fixes = 0
files_changed = 0

for hf in html_files:
    with open(hf) as f:
        html = f.read()

    new_html = html
    file_fixes = 0

    for old, new in REWRITES.items():
        # Match href="OLD" exactly (with optional trailing quote)
        pattern = f'href="{old}"'
        replacement = f'href="{new}"'
        count = new_html.count(pattern)
        if count > 0:
            new_html = new_html.replace(pattern, replacement)
            file_fixes += count

    if file_fixes > 0:
        with open(hf, 'w') as f:
            f.write(new_html)
        rel = os.path.relpath(hf, DIST)
        print(f'  {rel}: {file_fixes} links fixed')
        total_fixes += file_fixes
        files_changed += 1

print(f'\nTotal: {total_fixes} links fixed across {files_changed} files')
