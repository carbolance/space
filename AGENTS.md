# Agents

The Carbolance Space is intentionally agent-first. This document outlines how autonomous and assistive agents should discover, enrich, and contribute to the library while staying aligned with brand standards.

## Purpose

- Provide a stable knowledge core so agents can answer questions and synthesize assets confidently.
- Encode expectations for how agents reference copy, media, and metadata across the `library/` namespace.
- Establish shared language for orchestration with external systems (asset stores, CMS, ad platforms) as integrations come online.

## Agent Principles

- **Single source of truth** — Agents must treat Space Markdown as canonical unless a human explicitly overrides it.
- **Context stitching** — Compose outputs by linking to existing library nodes (products, campaigns, brand voice) before generating new material.
- **Traceable moves** — Record each material action (drafting, tagging, exporting) so humans can audit decisions and lineage.
- **Least surprise** — Prefer deterministic, reproducible flows; surface uncertainties or missing data instead of guessing.

## Intended Agent Archetypes

| Archetype | Focus | Primary Inputs | Primary Outputs |
|-----------|-------|----------------|-----------------|
| Context Scout | Navigate the library, collect relevant references, and expose gaps. | `library/*`, `tree_structure.md` | Curated context packets, gap reports |
| Copy Crafter | Generate or refine copy blocks consistent with `library/brand/voice-and-tone.md`. | Brand voice, product docs, campaign briefs | Draft copy, revision notes |
| Asset Librarian | Map media assets and metadata, ensure export coverage per channel specs. | `library/assets/**`, metadata sidecars | Asset manifests, export requests |
| Activation Pilot | Prepare deployment payloads for external systems (CMS, ads, email). | Canonical copy, CTA taxonomy, integration configs | Channel-ready payloads, change logs |

## Coordination Surface

- **Canonical directories** — Agents default to the directory conventions in `library/CONVENTIONS.md` when reading or writing.
- **Link integrity** — Run `scripts/linkcheck.py` or equivalent before proposing changes that add references.
- **Change tracking** — Update `CHANGELOG.md` or agent-specific logs with concise, human-readable notes.
- **Sandboxing** — Respect environment policies (no network, write scopes) and request elevation through orchestration rules if needed.

## Expansion Roadmap

1. **External asset graph** — Mirror asset IDs across cloud storage for traceable fetch operations.
2. **Integration adapters** — Define payload schemas for primary channels (web, ads, email) so agents can publish without manual formatting.
3. **Feedback loops** — Capture performance signals (CTR, conversion, qualitative notes) to inform future agent prompts.
4. **Agent marketplace** — Register third-party or specialized agents with declared capabilities, trust levels, and escalation paths.

## Getting Started

- Sync your agent runtime with the latest `main` branch to avoid stale context.
- Begin in read-only mode: crawl the library, map dependencies, and confirm required directories exist.
- Prepare a capability manifest (inputs, outputs, and validation steps) before committing changes.
- Coordinate with humans via issues or pull requests for major workflow introductions.

As new agents join the Space, extend this document with playbooks, escalation policies, and integration contracts. Keep the emphasis on agent-first collaboration while preserving human oversight and brand fidelity.
