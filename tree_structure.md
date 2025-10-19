# Tree Structure

```plaintext
/ (root)
├─ .githooks/ — local git hook scripts
│  └─ pre-commit — pre-commit hook (local)
├─ library/ — brand knowledge library
│  ├─ assets/ — asset sources, exports & templates
│  │  ├─ brand/
│  │  │  └─ README.md
│  │  ├─ exports/
│  │  ├─ photography/
│  │  │  └─ photography-tips.md
│  │  ├─ source/
│  │  ├─ templates/
│  │  └─ IMAGE_METADATA_TEMPLATE.md — image metadata template
│  ├─ brand/ — brand rules and assets
│  │  ├─ about.md
│  │  ├─ basics.md
│  │  ├─ colors.md — brand color definitions
│  │  ├─ community-and-niche.md
│  │  ├─ culture.md
│  │  ├─ ethos.md
│  │  ├─ identity.md
│  │  ├─ massive-value.md
│  │  ├─ perspective.md
│  │  ├─ story-and-community.md
│  │  ├─ strategy.md
│  │  ├─ typography-and-fonts.md — type scale and usage
│  │  └─ voice-and-tone.md — messaging guidelines
│  ├─ campaigns/
│  │  ├─ apparel-marketing.md
│  │  ├─ overall-marketing.md
│  │  └─ promotional-offers.md
│  ├─ collections/ — curated product collections
│  │  ├─ collection-page-copy.md
│  │  ├─ essentials.md
│  │  └─ README.md
│  ├─ copywriting/
│  │  ├─ post-delivery-survey-email.md
│  │  ├─ thank-you.md
│  │  └─ welcome-series-email.md
│  ├─ creatives/
│  │  ├─ ads/
│  │  ├─ social/
│  │  ├─ graphics-ideas.md
│  │  └─ video-editing.md
│  ├─ products/ — product pages and metadata
│  │  ├─ long-sleeve-t-shirt-midnight-black.md — long sleeve product
│  │  ├─ README.md
│  │  └─ t-shirt-midnight-black.md — short sleeve product
│  ├─ seo/ — SEO related snippets and tags
│  │  ├─ README.md
│  │  └─ seo-tags.md — recommended SEO tags
│  ├─ website/
│  │  ├─ about-page-copy.md
│  │  ├─ landing-page-copy.md
│  │  ├─ product-page-guidelines.md
│  │  ├─ t-shirt-product-page-copy.md
│  │  └─ website-to-do-list.md
│  ├─ CONVENTIONS.md
│  └─ plans.md
├─ scripts/ — utility scripts and automation
│  ├─ export_metafields.py — export product metafields
│  ├─ generate_tree.py — generate this ASCII tree
│  ├─ import_metafields.py — import metafields into platform
│  ├─ linkcheck.py
│  ├─ mapping.md — field mapping notes
│  ├─ setup_git_hooks.sh — installs local githooks
│  └─ validate_products.py — product validation tool
├─ .editorconfig — editor configuration rules
├─ .env.example — example environment variables
├─ .gitattributes — repository attributes for Git
├─ .gitignore — files and folders excluded from Git
├─ AGENTS.md
├─ APP_VISION.md — product vision and goals
├─ CHANGELOG.md — release notes and changes
├─ CONTRIBUTING.md — contribution guidelines
├─ README.md — project overview and quick start
└─ tree_structure.md — this ASCII tree (generated)
```
