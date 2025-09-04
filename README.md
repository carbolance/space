# Carbolance Space
[![Validate Products](https://img.shields.io/badge/validator-products-blue)](#validation)

## Purpose
The Carbolance Space (carbolance/space) is the single source of truth for brand copy, product descriptions, collections, and guidelines. It provides structure and context so that both humans and AI can retrieve and apply brand information consistently across platforms.

This repository is designed to:
- Store and organize product copy in Markdown format.
- Document brand guidelines, taglines, and key messaging.
- Support SEO optimization and product metadata.
- Enable easy collaboration and version control via Git.

## Repository Structure
```
products/
collections/
brand-guidelines/
meta/
scripts/
.githooks/
```

## Naming Conventions
- Files use **kebab-case** (e.g., `premium-t-shirt-midnight-black.md`).
- Product filenames match SKU or product name for clarity (e.g., `premium-long-sleeve-t-shirt-midnight-black.md`).
- Metadata and logs live in `meta/`.

## Getting Started
- Add new products in `products/` using Markdown.
- Keep copy concise and on-brand (see `brand-guidelines/voice-and-tone.md`).
- Update `meta/changelog.md` with each meaningful change.

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
