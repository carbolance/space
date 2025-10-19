# Carbolance Space

[![Validate Products](https://img.shields.io/badge/validator-products-blue)](#validation)

## Purpose

The Carbolance Space (carbolance/space) is the **single source of truth** for brand copy, product descriptions, collections, and guidelines. It provides structure and context so that both humans and AI can retrieve and apply brand information consistently across platforms.

### This Carbolance library repository is designed to

* Store and organize product copy in Markdown format.
* Document brand guidelines, taglines, and key messaging (define brand voice).
* Support SEO optimization and product metadata.
* Enable simple edits, comments, and versioned collaboration.

### System Overview

#### Markdown Files (.md)

* Each product and collection has its own structured Markdown file.
* Lightweight, portable, and platform-agnostic.

#### Version Control with Git

* All Markdown files stored in a GitHub (or alternative) repository as the single source of truth.
* Enables version tracking, collaboration via pull requests, and a clean history of edits.

## Repository Structure (high-level)

```plaintext
/ (root)
├─ .githooks/          # local git hooks
├─ library/            # unified knowledge & content (products, brand, assets, seo, campaigns, etc.)
├─ scripts/            # automation & tooling
├─ CHANGELOG.md        # change history
└─ tree_structure.md   # generated detailed tree
```

## Naming Conventions

* Files and folders use **kebab-case** (e.g., `t-shirt-midnight-black.md`).
* Product filenames match SKU or product name for clarity (e.g., `long-sleeve-t-shirt-midnight-black.md`).
* Central knowledge (products, collections, brand, assets, seo, campaigns) lives under `library/`.

## Getting Started

* Add new products in `library/products/` using Markdown.
* Keep copy concise and on-brand (see `library/brand/voice-and-tone.md`).
* Update `CHANGELOG.md` with each meaningful change.

## Validation

Run the local validator before committing:

```bash
python3 scripts/validate_products.py --strict
```

Enable the local pre-commit hook once:

```bash
bash scripts/setup_git_hooks.sh
```

Exit codes: 0 = OK, 1 = warnings, 2 = errors. In `--strict` mode, warnings are treated as errors.
