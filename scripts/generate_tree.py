#!/usr/bin/env python3
"""
Generate an ASCII tree of the repository (folders first, alphabetical) with optional one-line descriptions
and write it to tree_structure.md at the repo root.

Usage:
  python scripts/generate_tree.py

This script intentionally skips some common noise directories (e.g., .git, __pycache__) to keep the tree clean.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, List, Tuple

# Root is the repo root (script is in scripts/)
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = ROOT / "tree_structure.md"

# Directories to always skip
SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
    "ENV",
    "env",
    ".idea",
    ".vscode",
    "node_modules",
}

# Files to skip by exact name
SKIP_FILES = {
    # none for now
}

# File suffixes to skip
SKIP_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".DS_Store",
}

# Optional one-line descriptions keyed by posix-style relative paths
DESCRIPTIONS = {
    ".githooks/": "local git hook scripts",
    ".githooks/pre-commit": "pre-commit hook (local)",
    "library/": "brand knowledge library",
    "library/brand/": "brand rules and assets",
    "library/brand/colors.md": "brand color definitions",
    "library/brand/typography-and-fonts.md": "type scale and usage",
    "library/brand/voice-and-tone.md": "messaging guidelines",
    "library/collections/": "curated product collections",
    "library/products/": "product pages and metadata",
    "library/products/long-sleeve-t-shirt-midnight-black.md": "long sleeve product",
    "library/products/t-shirt-midnight-black.md": "short sleeve product",
    "library/seo/": "SEO related snippets and tags",
    "library/seo/seo-tags.md": "recommended SEO tags",
    "library/assets/": "asset sources, exports & templates",
    "library/assets/IMAGE_METADATA_TEMPLATE.md": "image metadata template",
    "scripts/": "utility scripts and automation",
    "scripts/export_metafields.py": "export product metafields",
    "scripts/import_metafields.py": "import metafields into platform",
    "scripts/mapping.md": "field mapping notes",
    "scripts/setup_git_hooks.sh": "installs local githooks",
    "scripts/validate_products.py": "product validation tool",
    "scripts/generate_tree.py": "generate this ASCII tree",
    ".editorconfig": "editor configuration rules",
    ".env.example": "example environment variables",
    ".gitattributes": "repository attributes for Git",
    ".gitignore": "files and folders excluded from Git",
    "APP_VISION.md": "product vision and goals",
    "CHANGELOG.md": "release notes and changes",
    "CONTRIBUTING.md": "contribution guidelines",
    "README.md": "project overview and quick start",
    "tree_structure.md": "this ASCII tree (generated)",
}


def list_dir_sorted(path: Path) -> Tuple[List[Path], List[Path]]:
    """Return (dirs, files) under path, each sorted alphabetically (case-insensitive)."""
    try:
        entries = list(path.iterdir())
    except PermissionError:
        return [], []
    dirs = [p for p in entries if p.is_dir() and p.name not in SKIP_DIRS]
    files = [p for p in entries if p.is_file() and p.name not in SKIP_FILES and p.suffix not in SKIP_SUFFIXES]
    key = lambda p: p.name.lower()
    return sorted(dirs, key=key), sorted(files, key=key)


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def describe(rel_path: str, is_dir: bool) -> str:
    key = rel_path + ("/" if is_dir and not rel_path.endswith("/") else "") if is_dir else rel_path
    return DESCRIPTIONS.get(key, "").strip()


def render_tree(path: Path, prefix: str = "") -> List[str]:
    lines: List[str] = []
    dirs, files = list_dir_sorted(path)

    # Folders first, then files
    items: List[Tuple[Path, bool]] = [(d, True) for d in dirs] + [(f, False) for f in files]

    total = len(items)
    for idx, (p, is_dir) in enumerate(items):
        connector = "└─" if idx == total - 1 else "├─"
        name = p.name + ("/" if is_dir else "")
        d = describe(rel(p), is_dir)
        desc = f" — {d}" if d else ""
        lines.append(f"{prefix}{connector} {name}{desc}")
        if is_dir:
            extension = "   " if idx == total - 1 else "│  "
            lines.extend(render_tree(p, prefix + extension))
    return lines


def generate() -> str:
    header = "/ (root)"
    body = render_tree(ROOT)
    tree_text = "\n".join([header] + body) + "\n"
    # Wrap in Markdown code fences for readability
    return "# Tree Structure\n\n" + "```plaintext\n" + tree_text + "```\n"


def main() -> None:
    output = generate()
    OUTPUT_FILE.write_text(output, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
