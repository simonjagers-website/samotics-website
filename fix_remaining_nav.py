#!/usr/bin/env python3
"""
Fix Assets navigation on 11 remaining blog/case-study pages.
Run from the root of the samotics-website repo:
    python3 fix_remaining_nav.py
"""
import os

FILES = [
    "dist/resources/blog/proven-maintenance-strategies-for-industrial-equipment/index.html",
    "dist/resources/blog/reduce-maintenance-costs-for-your-wind-farm/index.html",
    "dist/resources/blog/remote-condition-monitoring-pumps/index.html",
    "dist/resources/blog/sam4s-hardware-architect-talks-about-medium-voltage-monitoring/index.html",
    "dist/resources/blog/secure-water-supply-drought-season-condition-monitoring-borehole-pumps/index.html",
    "dist/resources/blog/should-you-use-vibration-analysis-condition-monitoring/index.html",
    "dist/resources/blog/smart-sewers-detect-pumping-station-blockages/index.html",
    "dist/resources/blog/smart-sewers-proactive-maintenance/index.html",
    "dist/resources/case-studies/case-study-steel-runout-table-cardan-shaft-coupling/index.html",
    "dist/resources/case-studies/case-study-steel-runout-table-roll-bearing/index.html",
    "dist/resources/case-studies/common-faults-steel-manufacturing/index.html",
]

# DESKTOP: Old Platform dropdown (with What We Monitor)
OLD_DESKTOP = """      <div class="sam-nav__item sam-nav__item--has-dropdown">
        <button class="sam-nav__link" aria-expanded="false" aria-haspopup="true">
          Platform
          <svg class="sam-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">
            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="sam-dropdown" role="menu">
          <a href="/platform/sam4" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">SAM4 Platform</span>
            <span class="sam-dropdown__desc">Dashboard, diagnostics, and service model</span>
          </a>
          <a href="/platform/how-it-installs" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">How It Installs</span>
            <span class="sam-dropdown__desc">&lt;60 minutes, back online same shift</span>
          </a>
          <a href="/platform/security" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Security &amp; Compliance</span>
            <span class="sam-dropdown__desc">ISO 27001, ISO 9001, NIS2 aligned, cellular architecture</span>
          </a>
          <a href="/platform/what-we-monitor" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">What We Monitor</span>
            <span class="sam-dropdown__desc">Detection matrix by asset type and fault mode</span>
          </a>
        </div>
      </div>"""

# DESKTOP: New Assets + Platform (without What We Monitor)
NEW_DESKTOP = """      <div class="sam-nav__item sam-nav__item--has-dropdown">
        <button class="sam-nav__link" aria-expanded="false" aria-haspopup="true">
          Assets
          <svg class="sam-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">
            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="sam-dropdown" role="menu">
          <a href="/platform/what-we-monitor/pumps" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Pumps</span>
            <span class="sam-dropdown__desc">Centrifugal, submersible, borehole, and canned motor</span>
          </a>
          <a href="/platform/what-we-monitor/compressors" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Compressors</span>
            <span class="sam-dropdown__desc">Reciprocating, screw, and centrifugal</span>
          </a>
          <a href="/platform/what-we-monitor/fans-blowers" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Fans &amp; Blowers</span>
            <span class="sam-dropdown__desc">Axial, centrifugal, and process air</span>
          </a>
          <a href="/platform/what-we-monitor/conveyors" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Conveyors</span>
            <span class="sam-dropdown__desc">Belt, screw, and chain conveyors</span>
          </a>
          <a href="/platform/what-we-monitor/transmissions" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Transmissions</span>
            <span class="sam-dropdown__desc">Gearboxes, couplings, and belt drives</span>
          </a>
          <a href="/platform/what-we-monitor" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">All Assets &amp; Motors</span>
            <span class="sam-dropdown__desc">Full detection matrix by asset type and fault mode</span>
          </a>
        </div>
      </div>

      <div class="sam-nav__item sam-nav__item--has-dropdown">
        <button class="sam-nav__link" aria-expanded="false" aria-haspopup="true">
          Platform
          <svg class="sam-nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">
            <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="sam-dropdown" role="menu">
          <a href="/platform/sam4" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">SAM4 Platform</span>
            <span class="sam-dropdown__desc">Dashboard, diagnostics, and service model</span>
          </a>
          <a href="/platform/how-it-installs" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">How It Installs</span>
            <span class="sam-dropdown__desc">&lt;60 minutes, back online same shift</span>
          </a>
          <a href="/platform/security" class="sam-dropdown__item" role="menuitem">
            <span class="sam-dropdown__label">Security &amp; Compliance</span>
            <span class="sam-dropdown__desc">ISO 27001, ISO 9001, NIS2 aligned, cellular architecture</span>
          </a>
        </div>
      </div>"""

# MOBILE: Old Platform group (with What We Monitor)
OLD_MOBILE = """      <div class="sam-mobile-nav__group">
        <button class="sam-mobile-nav__toggle" aria-expanded="false">
          Platform
          <svg class="sam-mobile-nav__arrow" width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">
            <path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="sam-mobile-nav__sub">
          <a href="/platform/sam4">SAM4 Platform</a>
          <a href="/platform/how-it-installs">How It Installs</a>
          <a href="/platform/security">Security &amp; Compliance</a>
          <a href="/platform/what-we-monitor">What We Monitor</a>
        </div>
      </div>"""

# MOBILE: New Assets + Platform groups
NEW_MOBILE = """      <div class="sam-mobile-nav__group">
        <button class="sam-mobile-nav__toggle" aria-expanded="false">
          Assets
          <svg class="sam-mobile-nav__arrow" width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">
            <path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="sam-mobile-nav__sub">
          <a href="/platform/what-we-monitor/pumps">Pumps</a>
          <a href="/platform/what-we-monitor/compressors">Compressors</a>
          <a href="/platform/what-we-monitor/fans-blowers">Fans &amp; Blowers</a>
          <a href="/platform/what-we-monitor/conveyors">Conveyors</a>
          <a href="/platform/what-we-monitor/transmissions">Transmissions</a>
          <a href="/platform/what-we-monitor">All Assets &amp; Motors</a>
        </div>
      </div>

      <div class="sam-mobile-nav__group">
        <button class="sam-mobile-nav__toggle" aria-expanded="false">
          Platform
          <svg class="sam-mobile-nav__arrow" width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">
            <path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <div class="sam-mobile-nav__sub">
          <a href="/platform/sam4">SAM4 Platform</a>
          <a href="/platform/how-it-installs">How It Installs</a>
          <a href="/platform/security">Security &amp; Compliance</a>
        </div>
      </div>"""

updated = 0
skipped = []

for f in FILES:
    if not os.path.exists(f):
        skipped.append(f"{f} (NOT FOUND)")
        continue
    content = open(f, 'r').read()
    original = content
    if OLD_DESKTOP in content:
        content = content.replace(OLD_DESKTOP, NEW_DESKTOP, 1)
    if OLD_MOBILE in content:
        content = content.replace(OLD_MOBILE, NEW_MOBILE, 1)
    if content != original:
        open(f, 'w').write(content)
        updated += 1
        print(f"  Updated: {f}")
    else:
        skipped.append(f"{f} (no match)")

print(f"\n{updated} files updated, {len(skipped)} skipped")
if skipped:
    for s in skipped:
        print(f"  SKIP: {s}")
