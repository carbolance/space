#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validates product Markdown files for:
- kebab-case filenames
- required sections and ordering
- minimal field presence in Meta/SEO

Usage:
  python scripts/validate_products.py [--strict]

Exit code 0 = all good, 1 = warnings, 2 = errors.
"""
import sys, re, os, glob
from pathlib import Path

RE_KEBAB = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*\.md$')
REQUIRED_H1 = re.compile(r'^#\s+', re.M)
REQUIRED_SECTIONS = [
    "## Tagline",
    "## Description",
    "## Features",
    "## Materials & Care",
    "## Fit",
    "## Meta",
    "## SEO",
]

def check_filename(path):
    name = os.path.basename(path)
    return bool(RE_KEBAB.match(name))

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def has_h1(txt):
    return bool(REQUIRED_H1.search(txt))

def sections_in_order(txt):
    missing = []
    positions = []
    for s in REQUIRED_SECTIONS:
        i = txt.find(s)
        if i == -1:
            missing.append(s)
        positions.append(i)
    prior = -1
    out_of_order = False
    for i in positions:
        if i == -1:
            continue
        if i <= prior:
            out_of_order = True
        prior = i
    return (len(missing) == 0, missing, out_of_order)

def minimal_fields(txt):
    errs = []
    if "## Meta" in txt:
        if "SKU:" not in txt: errs.append("Meta: missing SKU")
        if "Category:" not in txt: errs.append("Meta: missing Category")
        if "Color:" not in txt: errs.append("Meta: missing Color")
    if "## SEO" in txt:
        if "Meta Title:" not in txt: errs.append("SEO: missing Meta Title")
        if "Meta Description:" not in txt: errs.append("SEO: missing Meta Description")
    return errs

def main(strict=False):
    repo_root = Path(__file__).resolve().parent.parent
    # Allow overriding products location; default to library/products, fallback to products (legacy)
    content_root = os.environ.get("CONTENT_ROOT", str(repo_root / "library"))
    candidates = [Path(content_root) / "products", repo_root / "products"]
    prod_dir = next((p for p in candidates if p.exists()), candidates[0])

    paths = sorted(glob.glob(str(prod_dir / "*.md")))
    # Ignore non-product docs in products folder
    paths = [p for p in paths if os.path.basename(p) != "README.md"]
    if not paths:
        print(f"No product files found in {prod_dir.relative_to(repo_root)}.")
        return 2

    errors, warnings = [], []
    for p in paths:
        rel = os.path.relpath(p, start=str(repo_root))
        if not check_filename(p):
            errors.append(f"[filename] {rel} is not kebab-case")
        txt = read(p)
        if not has_h1(txt):
            errors.append(f"[content] {rel} is missing H1 (# Product Title)")
        ok, missing, out_of_order = sections_in_order(txt)
        if missing:
            errors.append(f"[sections] {rel} missing: {', '.join(missing)}")
        if out_of_order:
            warnings.append(f"[sections] {rel} has sections out of preferred order")
        mf = minimal_fields(txt)
        errors.extend([f"[fields] {rel} {e}" for e in mf])

    if errors:
        print("ERRORS:")
        for e in errors: print(" -", e)
    if warnings:
        print("WARNINGS:")
        for w in warnings: print(" -", w)

    if errors:
        return 2
    if warnings and strict:
        return 2
    return 0

if __name__ == "__main__":
    strict = "--strict" in sys.argv
    sys.exit(main(strict))
