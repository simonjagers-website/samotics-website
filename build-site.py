#!/usr/bin/env python3
"""
Build a complete static site from Samotics page fragments.
Generates full HTML documents from fragments, wrapping them with header/footer.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Configuration
SOURCE_DIR = Path("/sessions/stoic-sharp-darwin/mnt/Foundational Docs/pages")
DIST_DIR = Path("/sessions/stoic-sharp-darwin/dist")

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
        # Remove any HTML entities or extra formatting
        title = re.sub(r"<[^>]+>", "", title).strip()
        if title:
            return title
    return fallback_title


def clean_php(content):
    """Replace PHP snippets with static equivalents.

    Note: Some pages (blog-archive, news-archive) contain WordPress loop PHP code
    that should be replaced with static content or JavaScript-driven filtering.
    This function removes simple PHP echo statements but leaves complex logic intact
    for manual review.
    """
    # Remove simple PHP echo statements (home_url, get_template_directory_uri)
    content = re.sub(r"\{\{home_url\('\/'\)\}\}", "/", content)
    content = re.sub(r"\{\{home_url\('([^']+)'\)\}\}", r"\1", content)
    content = re.sub(r"<?php\s+echo\s+home_url\('\/'\);\s*\?>", "/", content)
    content = re.sub(r"<?php\s+echo\s+home_url\('([^']+)'\);\s*\?>", r"\1", content)
    content = re.sub(r"<?php\s+echo\s+get_template_directory_uri\(\);\s*\?>", "/assets", content)
    content = re.sub(r"<?php\s+echo\s+get_permalink\(\);\s*\?>", "#", content)

    # Note: Complex WordPress loops and WP_Query statements are intentionally left
    # for manual migration or JavaScript replacement
    return content


def strip_bricks_header(content):
    """Remove Bricks comment header from content."""
    # Remove the Bricks header comments
    content = re.sub(
        r"<!--\s*={3,}.*?BRICKS.*?={3,}\s*-->.*?<!--\s*PHP & HTML\s*-->",
        "",
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    # Also handle just the header comment without the second one
    content = re.sub(
        r"<!--\s*={3,}.*?Bricks\s+Code\s+Element.*?={3,}\s*-->",
        "",
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return content.strip()


def get_page_css(page_name):
    """Get CSS for a page, handling special cases like industries and assets."""
    css_parts = []

    # Check for page-specific CSS
    page_css_path = SOURCE_DIR / f"{page_name}.css"
    if page_css_path.exists():
        css_parts.append(read_file(page_css_path))

    # Industry pages: also include industry-template.css
    if page_name in ["water", "oil-gas", "metals-mining", "chemicals", "pulp-paper", "airports"]:
        template_css = SOURCE_DIR / "industry-template.css"
        if template_css.exists():
            css_parts.append(read_file(template_css))

    # Asset pages: include specific-asset.css and asset-type.css
    asset_names = [
        "mv-motors", "pumps", "fans-blowers", "compressors", "esps",
        "canned-motor-pumps", "transmissions", "conveyors", "agitators-mixers",
        "archimedes-screws", "lv-motors"
    ]
    if page_name in asset_names:
        for css_file in ["specific-asset.css", "asset-type.css"]:
            css_path = SOURCE_DIR / css_file
            if css_path.exists():
                css_parts.append(read_file(css_path))

    # Detection stories: include detection-story.css
    if page_name.startswith("detect-"):
        template_css = SOURCE_DIR / "detection-story.css"
        if template_css.exists():
            css_parts.append(read_file(template_css))

    return "\n".join(css_parts)


def build_html_page(page_name, output_path, title, source_subdir=""):
    """Build a complete HTML page from fragments."""
    # Determine source file location
    if source_subdir:
        page_html_path = SOURCE_DIR / source_subdir / f"{page_name}.html"
    else:
        page_html_path = SOURCE_DIR / f"{page_name}.html"

    if not page_html_path.exists():
        return False, f"Source file not found: {page_html_path}"

    # Read all components
    header_html = read_file(SOURCE_DIR / "header.html")
    header_css = read_file(SOURCE_DIR / "header.css")
    header_js = read_file(SOURCE_DIR / "header.js")

    footer_html = read_file(SOURCE_DIR / "footer.html")
    footer_css = read_file(SOURCE_DIR / "footer.css")
    footer_js = read_file(SOURCE_DIR / "footer.js")

    page_html = read_file(page_html_path)
    page_css = get_page_css(page_name)
    page_js = read_file(SOURCE_DIR / f"{page_name}.js")

    # Clean content
    header_html = strip_bricks_header(header_html)
    footer_html = strip_bricks_header(footer_html)
    page_html = strip_bricks_header(page_html)

    header_html = clean_php(header_html)
    footer_html = clean_php(footer_html)
    page_html = clean_php(page_html)
    header_js = clean_php(header_js)
    footer_js = clean_php(footer_js)
    page_js = clean_php(page_js)

    # Extract title from h1 if possible
    extracted_title = extract_title(page_html, title)
    page_title = f"{extracted_title} | Samotics"

    # Build HTML document
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

    # Create output directory and write file
    output_file = DIST_DIR / output_path
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
    """Main build function."""
    print("=" * 70)
    print("SAMOTICS STATIC SITE BUILDER")
    print("=" * 70)
    print(f"Source directory: {SOURCE_DIR}")
    print(f"Output directory: {DIST_DIR}")
    print()

    # Ensure source dir exists
    if not SOURCE_DIR.exists():
        print(f"ERROR: Source directory not found: {SOURCE_DIR}")
        return

    # Clear and create dist directory
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    stats = {"success": 0, "failed": 0, "skipped": 0}
    generated_pages = []
    failed_pages = []

    # Process main pages from PAGE_MAPPING
    print("Generating main pages...")
    print("-" * 70)

    for mapping in PAGE_MAPPING:
        page_name = mapping[0]
        output_path = mapping[1]
        title = mapping[2]
        source_subdir = mapping[3] if len(mapping) > 3 else ""

        success, result = build_html_page(page_name, output_path, title, source_subdir)

        if success:
            print(f"✓ {page_name:30} → {output_path}")
            generated_pages.append((output_path, page_name))
            stats["success"] += 1
        else:
            print(f"✗ {page_name:30} → ERROR: {result}")
            failed_pages.append(page_name)
            stats["failed"] += 1

    # Process detection stories
    print()
    print("Generating detection stories...")
    print("-" * 70)

    for story in DETECTION_STORIES:
        # Extract slug from story name
        slug = story.replace("detect-", "")
        output_path = f"proof/case-studies/{slug}/"

        success, result = build_html_page(story, output_path, slug.replace("-", " ").title())

        if success:
            print(f"✓ {story:30} → {output_path}")
            generated_pages.append((output_path, story))
            stats["success"] += 1
        else:
            print(f"✗ {story:30} → ERROR: {result}")
            failed_pages.append(story)
            stats["failed"] += 1

    # Print summary
    print()
    print("=" * 70)
    print("BUILD SUMMARY")
    print("=" * 70)
    print(f"Total pages generated:  {stats['success']}")
    print(f"Failed:                 {stats['failed']}")
    print()

    if failed_pages:
        print("Failed pages:")
        for page in failed_pages:
            print(f"  - {page}")
        print()

    print("Generated files:")
    output_paths = sorted(set(path for path, _ in generated_pages))
    for path in output_paths[:20]:  # Show first 20
        if str(path).endswith("index.html") or str(path).endswith(".html"):
            if not str(path).endswith("index.html"):
                print(f"  /{path}")
            else:
                print(f"  /{path}")
        else:
            print(f"  /{path}index.html")

    if len(output_paths) > 20:
        print(f"  ... and {len(output_paths) - 20} more")

    print()
    print("=" * 70)
    print("NOTES FOR STATIC DEPLOYMENT")
    print("=" * 70)
    print()
    print("Pages with WordPress PHP (require manual migration):")
    print("  • /resources/blog/ (blog-archive.html)")
    print("    - Contains WP_Query loops and category filtering")
    print("    - Recommend: Generate static posts OR use JavaScript-based filtering")
    print()
    print("  • /resources/news/ (news-archive.html)")
    print("    - Contains WP_Query loops for news posts")
    print("    - Recommend: Generate static posts OR use JavaScript-based filtering")
    print()
    print("Pages with dynamic content (may need updates):")
    print("  • /resources/webinars/ (if exists) - webinar archive")
    print("  • /resources/whitepapers/ (if exists) - whitepaper archive")
    print()
    print("All other pages are static and ready to deploy.")
    print()
    print(f"Output directory: {DIST_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
