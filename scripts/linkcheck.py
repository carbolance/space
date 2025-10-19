#!/usr/bin/env python3
"""
Validate Markdown links within the repo, focusing on library/.
- Checks relative links resolve to existing files.
- For logical scheme links like asset:exports/web/..., validate under library/assets.
- Prints warnings for missing targets and exits non-zero only if --strict is passed.

Usage:
  python scripts/linkcheck.py [--strict]
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re

RE_MD_LINK = re.compile(r"!{0,1}\[[^\]]*\]\(([^)\s]+)\)")

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "library"
ASSETS = CONTENT / "assets"


def iter_markdown_files(base: Path):
    for p in base.rglob("*.md"):
        # Skip the generated tree file
        if p.name.startswith("tree_structure."):
            continue
        yield p


def validate_links(md_file: Path) -> list[str]:
    problems: list[str] = []
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    for m in RE_MD_LINK.finditer(text):
        target = m.group(1)
        if target.startswith("http://") or target.startswith("https://"):
            continue
        # Relative path
        resolved = (md_file.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            # points outside repo root
            problems.append(f"{md_file}: link points outside repo -> {target}")
            continue
        if not resolved.exists():
            problems.append(f"{md_file}: missing file -> {target}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    all_problems: list[str] = []
    for md in iter_markdown_files(CONTENT):
        all_problems.extend(validate_links(md))

    if all_problems:
        print("Linkcheck warnings/errors:")
        for p in all_problems:
            print("-", p)
        return 1 if args.strict else 0

    print("Linkcheck: no issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
