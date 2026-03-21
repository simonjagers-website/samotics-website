#!/usr/bin/env python3
"""
Build a complete static site from Samotics page fragments.
Generates full HTML documents from fragments, wrapping them with header/footer.

Usage:
    python build-site.py              # uses default paths (repo root)
    python build-site.py --source pages --dist dist
"""

import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Resolve paths relative to this script's location (repo root)
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SOURCE = SCRIPT_DIR / "pages"
DEFAULT_DIST = SCRIPT_DIR / "dist"

# Page mapping: (source_file, output_path, title)
PAGE_MAPPING = [
    # Main pages
    ("homepage", "", "Home"),
    ("about", "about/", "About"),
    ("contact", "contact/", "Contact"),
    ("asset-audit", "contact/asset-audit/", "Asset Audit"),
    ("partners", "partners/", "Partners"),
    ("problem", "problem/", "Problem"),
    ("proximity-penalty", "proximity-penalty/", "Proximity Penalty"),

    # Proof/Case Studies
    ("proof", "proof/", "Proof"),
    ("nyrstar", "proof/nyrstar/", "Nyrstar"),
    ("schiphol", "proof/schiphol/", "Schiphol"),
    ("southern-water", "proof/southern-water/", "Southern Water"),
    ("vitens", "proof/vitens/", "Vitens"),
    ("thyssenkrupp", "proof/thyssenkrupp/", "ThyssenKrupp"),
    ("case-studies-archive", "proof/case-studies/", "Case Studies"),

    # Technology
    ("technology-hub", "technology/", "Technology"),
    ("esa", "technology/esa/", "Electrical Signature Analysis"),
    ("esa-vs-vibration", "technology/esa-vs-vibration/", "ESA vs Vibration"),
    ("how-it-works", "technology/how-it-works/", "How It Works"),
    ("how-sam4-works", "technology/how-sam4-works/", "How SAM4 Works"),

    # Platform
    ("platform-hub", "platform/", "Platform"),
    ("sam4", "platform/sam4/", "SAM4"),
    ("how-it-installs", "platform/how-it-installs/", "How It Installs"),
    ("integrations", "platform/integrations/", "Integrations"),
    ("security", "platform/security/", "Security"),
    ("what-we-monitor", "platform/what-we-monitor/", "What We Monitor"),

    # Assets - individual pages
    ("mv-motors", "platform/what-we-monitor/mv-motors/", "MV Motors"),
    ("pumps", "platform/what-we-monitor/pumps/", "Pumps"),
    ("fans-blowers", "platform/what-we-monitor/fans-blowers/", "Fans & Blowers"),
    ("compressors", "platform/what-we-monitor/compressors/", "Compressors"),
    ("esps", "platform/what-we-monitor/esps/", "ESPs"),
    ("canned-motor-pumps", "platform/what-we-monitor/canned-motor-pumps/", "Canned Motor Pumps"),
    ("transmissions", "platform/what-we-monitor/transmissions/", "Transmissions"),
    ("conveyors", "platform/what-we-monitor/conveyors/", "Conveyors"),
    ("agitators-mixers", "platform/what-we-monitor/agitators-mixers/", "Agitators & Mixers"),
    ("archimedes-screws", "platform/what-we-monitor/archimedes-screws/", "Archimedes Screws"),
    ("lv-motors", "platform/what-we-monitor/lv-motors/", "LV Motors"),

    # Industries
    ("industries-hub", "industries/", "Industries"),
    ("water", "industries/water/", "Water", "industries/"),
    ("oil-gas", "industries/oil-gas/", "Oil & Gas", "industries/"),
    ("metals-mining", "industries/metals-mining/", "Metals & Mining", "industries/"),
    ("chemicals", "industries/chemicals/", "Chemicals", "industries/"),
    ("pulp-paper", "industries/pulp-paper/", "Pulp & Paper", "industries/"),
    ("airports", "industries/airports/", "Airports", "industries/"),
    ("energy-efficiency", "industries/energy-efficiency/", "Energy Efficiency"),

    # Resources
    ("resources-hub", "resources/", "Resources"),
    ("blog-archive", "resources/blog/", "Blog"),
    ("news-archive", "resources/news/", "News"),
    ("whitepapers-archive", "resources/whitepapers/", "Whitepapers"),
    ("roi-calculator", "resources/roi-calculator/", "ROI Calculator"),

    # Tools
    ("tools-hub", "tools/", "Tools"),
    ("coverage-calculator", "tools/coverage-calculator/", "Coverage Calculator"),

    # Partners
    ("abb", "partners/abb/", "ABB"),

    # 404
    ("404", "404.html", "Not Found"),
]

# Detection stories - special handling
DETECTION_STORIES = [
    "detect-bearing-failure-motor-roll",
    "detect-belt-degradation-circulation-pump",
    "detect-belt-driven-assets",
    "detect-borehole-pump-detections",
    "detect-cardan-shaft-coupling-roller",
    "detect-cavitation-anolyte-pump",
    "detect-cavitation-centrifugal-pump",
    "detect-clogging-borehole-pump",
    "detect-clogging-wastewater-pump",
    "detect-clogging-yorkshire-water-sewage",
    "detect-gearbox-misalignment-circulator-pump",
    "detect-inlet-screw-monitoring",
    "detect-loose-belt-guard-shot-blasting",
    "detect-loose-cardan-joint-roll",
    "detect-missing-bolt-cooling-pump",
    "detect-synthetic-fiber-production",
    "detect-three-faults-oil-transfer-pump",
]


def read_file(path):
    """Read file safely, return empty string if not found."""
    if not path.exists():
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"  Warning: Could not read {path}: {e}")
        return ""


def extract_title(html_content, fallback_title):
    """Extract title from first <h1> or use fallback."""
    h1_match = re.search(r"<h1[^>]*>([^<]+)</h1>", html_content)
    if h1_match:
        title = h1_match.group(1).strip()
        title = re.sub(r"<[^>]+>", "", title).strip()
        if title:
            return title
    return fallback_title


def clean_php(content):
    """Replace PHP snippets with static equivalents."""
    content = re.sub(r"\{\{home_url\('\/'\)\}\}", "/", content)
    content = re.sub(r"\{\{home_url\('([^']+)'\)\}\}", r"\1", content)
    content = re.sub(r"<?php\s+echo\s+home_url\('\/'\);\s*\?>", "/", content)
    content = re.sub(r"<?php\s+echo\s+home_url\('([^']+)'\);\s*\?>", r"\1", content)
    content = re.sub(r"<?php\s+echo\s+get_template_directory_uri\(\);\s*\?>", "/assets", content)
    content = re.sub(r"<?php\s+echo\s+get_permalink\(\);\s*\?>", "#", content)
    return content


def strip_bricks_header(content):
    """Remove Bricks comment header from content."""
    content = re.sub(
        r"<!--\s*={3,}.*?BRICKS.*?={3,}\s*-->.*?<!--\s*PHP & HTML\s*-->",
        "",
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    content = re.sub(
        r"<!--\s*={3,}.*?Bricks\s+Code\s+Element.*?={3,}\s*-->",
        "",
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return content.strip()


def get_page_css(source_dir, page_name):
    """Get CSS for a page, handling special cases like industries and assets."""
    css_parts = []

    page_css_path = source_dir / f"{page_name}.css"
    if page_css_path.exists():
        css_parts.append(read_file(page_css_path))

    if page_name in ["water", "oil-gas", "metals-mining", "chemicals", "pulp-paper", "airports"]:
        template_css = source_dir / "industry-template.css"
        if template_css.exists():
            css_parts.append(read_file(template_css))

    asset_names = [
        "mv-motors", "pumps", "fans-blowers", "compressors", "esps",
        "canned-motor-pumps", "transmissions", "conveyors", "agitators-mixers",
        "archimedes-screws", "lv-motors"
    ]
    if page_name in asset_names:
        for css_file in ["specific-asset.css", "asset-type.css"]:
            css_path = source_dir / css_file
            if css_path.exists():
                css_parts.append(read_file(css_path))

    if page_name.startswith("detect-"):
        template_css = source_dir / "detection-story.css"
        if template_css.exists():
            css_parts.append(read_file(template_css))

    return "\n".join(css_parts)


def build_html_page(source_dir, dist_dir, page_name, output_path, title, source_subdir=""):
    """Build a complete HTML page from fragments."""
    if source_subdir:
        page_html_path = source_dir / source_subdir / f"{page_name}.html"
    else:
        page_html_path = source_dir / f"{page_name}.html"

    if not page_html_path.exists():
        return False, f"Source file not found: {page_html_path}"

    header_html = read_file(source_dir / "header.html")
    header_css = read_file(source_dir / "header.css")
    header_js = read_file(source_dir / "header.js")

    footer_html = read_file(source_dir / "footer.html")
    footer_css = read_file(source_dir / "footer.css")
    footer_js = read_file(source_dir / "footer.js")

    page_html = read_file(page_html_path)
    page_css = get_page_css(source_dir, page_name)
    page_js = read_file(source_dir / f"{page_name}.js")

    header_html = strip_bricks_header(header_html)
    footer_html = strip_bricks_header(footer_html)
    page_html = strip_bricks_header(page_html)

    header_html = clean_php(header_html)
    footer_html = clean_php(footer_html)
    page_html = clean_php(page_html)
    header_js = clean_php(header_js)
    footer_js = clean_php(footer_js)
    page_js = clean_php(page_js)

    extracted_title = extract_title(page_html, title)
    page_title = f"{extracted_title} | Samotics"

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page_title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    /* Header CSS */
    {header_css}
    /* Footer CSS */
    {footer_css}
    /* Page CSS */
    {page_css}
  </style>
</head>
<body>
  {header_html}
  {page_html}
  {footer_html}
  <script>
    {header_js}
  </script>
  <script>
    {footer_js}
  </script>
  <script>
    {page_js}
  </script>
</body>
</html>
"""

    output_file = dist_dir / output_path
    if str(output_file).endswith(".html"):
        output_file.parent.mkdir(parents=True, exist_ok=True)
    else:
        output_file.mkdir(parents=True, exist_ok=True)
        output_file = output_file / "index.html"

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_doc)
        return True, str(output_file)
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description="Build Samotics static site")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                        help="Source pages directory (default: ./pages)")
    parser.add_argument("--dist", type=Path, default=DEFAULT_DIST,
                        help="Output directory (default: ./dist)")
    args = parser.parse_args()

    source_dir = args.source.resolve()
    dist_dir = args.dist.resolve()

    print("=" * 70)
    print("SAMOTICS STATIC SITE BUILDER")
    print("=" * 70)
    print(f"Source directory: {source_dir}")
    print(f"Output directory: {dist_dir}")
    print()

    if not source_dir.exists():
        print(f"ERROR: Source directory not found: {source_dir}")
        return 1

    dist_dir.mkdir(parents=True, exist_ok=True)

    stats = {"success": 0, "failed": 0}
    generated_pages = []
    failed_pages = []

    print("Generating main pages...")
    print("-" * 70)

    for mapping in PAGE_MAPPING:
        page_name = mapping[0]
        output_path = mapping[1]
        title = mapping[2]
        source_subdir = mapping[3] if len(mapping) > 3 else ""

        success, result = build_html_page(source_dir, dist_dir, page_name, output_path, title, source_subdir)

        if success:
            print(f"  OK  {page_name:30} -> {output_path}")
            generated_pages.append((output_path, page_name))
            stats["success"] += 1
        else:
            print(f"  FAIL {page_name:30} -> {result}")
            failed_pages.append(page_name)
            stats["failed"] += 1

    print()
    print("Generating detection stories...")
    print("-" * 70)

    for story in DETECTION_STORIES:
        slug = story.replace("detect-", "")
        output_path = f"proof/case-studies/{slug}/"

        success, result = build_html_page(source_dir, dist_dir, story, output_path, slug.replace("-", " ").title())

        if success:
            print(f"  OK  {story:30} -> {output_path}")
            generated_pages.append((output_path, story))
            stats["success"] += 1
        else:
            print(f"  FAIL {story:30} -> {result}")
            failed_pages.append(story)
            stats["failed"] += 1

    print()
    print("=" * 70)
    print(f"BUILD COMPLETE: {stats['success']} pages generated, {stats['failed']} failed")
    print("=" * 70)

    if failed_pages:
        print("\nFailed pages:")
        for page in failed_pages:
            print(f"  - {page}")

    return 1 if stats["failed"] > 0 and stats["success"] == 0 else 0


if __name__ == "__main__":
    exit(main())
