#!/usr/bin/env python3
"""
Sync header and footer partials across all HTML files in dist/.

Usage:
  python scripts/sync-shared.py                 # Apply all changes
  python scripts/sync-shared.py --dry-run       # Show what would change
  python scripts/sync-shared.py --check         # Exit 1 if any file is out of sync
"""

import os
import re
import sys
from pathlib import Path

def load_partial(name):
    """Load a partial file from _partials/"""
    partial_path = Path(__file__).parent.parent / '_partials' / f'{name}.html'
    if not partial_path.exists():
        raise FileNotFoundError(f"Partial not found: {partial_path}")
    with open(partial_path, 'r', encoding='utf-8') as f:
        return f.read()

def sync_file(html_file, header, footer, dry_run=False, check=False):
    """
    Sync header and footer in a single HTML file.

    Returns: (changed, error_msg)
      - changed: True if file would be/was modified
      - error_msg: Error message if something went wrong, else None
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Failed to read: {e}"

    original_content = content

    # Replace header
    header_pattern = r'<header class="sam-header".*?</header>'
    if not re.search(header_pattern, content, re.DOTALL):
        return False, "No header found"
    content = re.sub(header_pattern, header, content, count=1, flags=re.DOTALL)

    # Replace footer
    footer_pattern = r'<footer class="sam-footer".*?</footer>'
    if not re.search(footer_pattern, content, re.DOTALL):
        return False, "No footer found"
    content = re.sub(footer_pattern, footer, content, count=1, flags=re.DOTALL)

    # Check if anything changed
    changed = content != original_content

    if changed and not dry_run and not check:
        try:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            return False, f"Failed to write: {e}"

    return changed, None

def main():
    dry_run = '--dry-run' in sys.argv
    check = '--check' in sys.argv

    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    dist_dir = repo_root / 'dist'

    if not dist_dir.exists():
        print(f"Error: dist/ directory not found at {dist_dir}")
        sys.exit(1)

    # Load partials
    try:
        header = load_partial('header')
        footer = load_partial('footer')
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Find all HTML files
    html_files = list(dist_dir.rglob('*.html'))
    if not html_files:
        print(f"Error: No HTML files found in {dist_dir}")
        sys.exit(1)

    # Process each file
    stats = {
        'total': len(html_files),
        'changed': 0,
        'unchanged': 0,
        'errors': []
    }

    for html_file in sorted(html_files):
        rel_path = html_file.relative_to(repo_root)
        changed, error_msg = sync_file(html_file, header, footer, dry_run=dry_run, check=check)

        if error_msg:
            stats['errors'].append((rel_path, error_msg))
            if not check:  # In check mode, we just track; in dry-run/apply, we report
                pass
        elif changed:
            stats['changed'] += 1
            mode = "would change" if dry_run or check else "changed"
            print(f"  {mode}: {rel_path}")
        else:
            stats['unchanged'] += 1

    # Report
    print()
    print(f"Total files processed:     {stats['total']}")
    print(f"Files changed:             {stats['changed']}")
    print(f"Files unchanged:           {stats['unchanged']}")
    print(f"Files with errors:         {len(stats['errors'])}")

    if stats['errors']:
        print("\nErrors:")
        for rel_path, error_msg in stats['errors']:
            print(f"  {rel_path}: {error_msg}")

    if dry_run:
        print("\n[DRY RUN] No files were modified.")
    elif check:
        if stats['changed'] > 0:
            print(f"\n[CHECK FAILED] {stats['changed']} file(s) out of sync")
            sys.exit(1)
        else:
            print("\n[CHECK PASSED] All files in sync")

if __name__ == '__main__':
    main()
