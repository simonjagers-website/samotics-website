#!/usr/bin/env python3
"""Replace SVG placeholders on listing pages with hero thumbnail images."""
import os, re, glob

DIST = os.path.join(os.path.dirname(__file__), 'dist')
IMG_DIR = os.path.join(DIST, 'assets', 'images', 'blog')

# Build lookup: slug → relative image path
hero_images = {}
for f in os.listdir(IMG_DIR):
    if f.endswith('-hero.jpg') or f.endswith('-hero.png') or f.endswith('-hero.jpeg') or f.endswith('-hero.webp'):
        slug = re.sub(r'-hero\.\w+$', '', f)
        hero_images[slug] = f'/assets/images/blog/{f}'

print(f"Found {len(hero_images)} hero images")

# Process each listing page
LISTING_PAGES = [
    os.path.join(DIST, 'resources', 'blog', 'index.html'),
    os.path.join(DIST, 'resources', 'case-studies', 'index.html'),
    os.path.join(DIST, 'resources', 'knowledge-base', 'index.html'),
    os.path.join(DIST, 'resources', 'news', 'index.html'),
]

# Pattern: extract slug from href, then replace the placeholder div
# href="/resources/blog/some-slug/" → slug = "some-slug"
card_pattern = re.compile(
    r'(<a\s+href="/resources/[^/]+/([^/]+)/"\s+class="sam-blog-card">)\s*'
    r'<div class="sam-blog-card__placeholder">\s*<svg[^<]*(?:<[^/][^<]*)*</svg>\s*</div>',
    re.DOTALL
)

total_replaced = 0
for page_path in LISTING_PAGES:
    if not os.path.exists(page_path):
        print(f"  SKIP (missing): {page_path}")
        continue

    with open(page_path, 'r') as f:
        html = f.read()

    count = 0
    new_html = html
    for m in list(card_pattern.finditer(html)):
        slug = m.group(2)
        if slug in hero_images:
            img_path = hero_images[slug]
            old_placeholder = m.group(0)
            # Build image thumbnail div
            new_thumb = (
                f'{m.group(1)}\n'
                f'        <div class="sam-blog-card__thumbnail">'
                f'<img src="{img_path}" alt="" loading="lazy" style="width:100%;height:200px;object-fit:cover;display:block;">'
                f'</div>'
            )
            new_html = new_html.replace(old_placeholder, new_thumb, 1)
            count += 1

    if count > 0:
        # Add CSS for thumbnail if not already present
        if 'sam-blog-card__thumbnail' not in html:
            css_insert = """\n.sam-blog-card__thumbnail {
  overflow: hidden;
  border-bottom: 1px solid var(--sam-border-light);
}
.sam-blog-card__thumbnail img {
  transition: transform 300ms ease-out;
}
.sam-blog-card:hover .sam-blog-card__thumbnail img {
  transform: scale(1.03);
}"""
            # Insert after the existing placeholder CSS
            new_html = new_html.replace(
                '.sam-blog-card__placeholder svg {\n  width: 48px; height: 48px;\n  color: var(--sam-comet); opacity: 0.3;\n}',
                '.sam-blog-card__placeholder svg {\n  width: 48px; height: 48px;\n  color: var(--sam-comet); opacity: 0.3;\n}' + css_insert
            )

        with open(page_path, 'w') as f:
            f.write(new_html)

        rel_path = os.path.relpath(page_path, DIST)
        print(f"  {rel_path}: {count} thumbnails added")
        total_replaced += count
    else:
        rel_path = os.path.relpath(page_path, DIST)
        print(f"  {rel_path}: 0 matched")

print(f"\nTotal: {total_replaced} thumbnails added across {len(LISTING_PAGES)} pages")
