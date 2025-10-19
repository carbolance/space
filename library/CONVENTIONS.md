# Library Conventions

This document defines how we organize content and reference assets across the repo.

## Goals

- Keep copy/metadata close to what it describes.
- Reuse assets across website, social, ads, and print.
- Make references stable, readable, and easy to validate.

## Folder overview

- assets/ (source files, exports, templates)
  - brand/ (logos, icons, patterns)
  - exports/ (derivatives for channels, LFS)
  - source/ (master/originals, LFS)
  - templates/ (export presets, LUTs, profiles)
- brand/ (about, colors, identity, typography-and-fonts, voice-and-tone)
- campaigns/ (per-campaign briefs, documentation, planning, reporting, setup)
- collections/ (each references product slugs it includes)
- creatives/ (ad creatives, reels, stories, influencer, UGC)
  - ads/ (ad copy blocks, per-channel specs)
  - social/ (per-channel specs, templates, best practices)
- email/ (templates, snippets, campaigns)
- products/ (one file per product; flat, no extra nesting)
- seo/ (titles, metas, schema blocks)
- visuals/ (mockups, lifestyle, product-only)
- website/ (guidelines, templates, snippets)

## Linking assets and docs

Prefer standard Markdown relative links:

- Images: `![Alt text](../../assets/exports/web/brand/logos/mark--w512.webp)`
- Files: `[Download spec](../../assets/templates/ads/google/spec.pdf)`
- Docs: `[Brand colors](../../brand/colors.md)`

Relative paths are robust and portable in GitHub and static site tooling.

Keep it simple: prefer standard Markdown relative links. We’ll consider logical or external references as needed later.

## Image metadata sidecar

For images with unique generation or license details (AI-generated or otherwise), create a markdown sidecar next to the image using the same basename:

- `astronaut-01.png`
- `astronaut-01.md` (metadata)

Template

Use the single source of truth template at:

- `library/assets/IMAGE_METADATA_TEMPLATE.md`

Copy it next to your image and rename it to the same basename with `.md`.

## Referencing the image

- Relative: `![Astronaut](../exports/social/instagram/astronaut-01--1080x1350.webp)`

## Asset naming conventions

Use a pattern that captures subject, variant, and profile:

```text
<subject>--<variant>--<profile>.<ext>
```

Examples:

- `tee-midnight-black--hero-front--w1200.webp`
- `tee-midnight-black--reel-v1--1080x1920.mp4`

## Channel profiles

- web: w480, w768, w1200 (WebP/AVIF preferred)
- instagram: 1080x1350 (feed), 1080x1920 (story/reel)
- tiktok: 1080x1920
- youtube-shorts: 1080x1920
- ads/google, ads/meta, ads/x: per-network specs under `assets/templates/`

Brand assets

- Put reusable brand asset files (e.g., logos) under `library/assets/brand/`.

## Validation

We provide a simple link checker: `scripts/linkcheck.py`.

- Validates that relative links in Markdown point to existing files.

Integrate into pre-commit if desired.
