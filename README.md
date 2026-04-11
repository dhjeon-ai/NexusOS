# ProjectOS

ProjectOS is a reusable repository operating system for humans and AI agents.

It helps new projects start with a durable structure instead of growing into scattered notes, duplicate overviews, and expensive context reloads.

## What it does

ProjectOS installs a lightweight, node-based project structure built around:

- one clear entry document
- selective context loading
- stable architecture and component contracts
- task continuity for medium and large work
- optional operating-rule packs for long-lived projects

## Why use it

Most repositories begin with code first and structure later.

That usually leads to:

- too many "start here" documents
- weak handoff continuity
- unclear component boundaries
- AI agents re-reading too much context
- project rules living only in team memory

ProjectOS solves that by setting a small but durable operating model from the start.

## Two-layer design

### Layer 1: Core Structure

Use Layer 1 when you want a clean, low-cost project foundation.

It creates:

- a project index
- architecture pages
- component pages
- active task pages
- decision record folders
- a root session-status file

### Layer 2: Operating Rules

Use Layer 2 when the project needs stronger coordination and continuity.

It adds rules for:

- task lifecycle
- subagent usage
- reporting style
- risk exceptions
- sync checks

ProjectOS is designed so an agent inspects the repository first, then asks the user whether to apply Layer 1 only or Layer 1 plus Layer 2.

## Repository layout

```text
ProjectOS/
  SKILL.md
  module.yaml
  agents/
    openai.yaml
  references/
    bootstrap-flow.md
    node-model.md
    reporting-style.md
    risk-exceptions.md
    subagent-workflow.md
    sync-checks.md
    task-lifecycle.md
  resources/
    activation-checklist.md
    checklist.md
    examples.md
    troubleshooting.md
  scripts/
    bootstrap_projectos.py
```

## Quick start

Bootstrap a new repository:

```bash
python ProjectOS/scripts/bootstrap_projectos.py --root /path/to/my-new-repo --project-name "My New Repo"
```

This creates a starter operating structure such as:

```text
my-repo/
  docs/
    00_Project_Index.md
    01_Architecture/
    02_Components/
    03_Decisions_ADR/
    04_Archive/
    Active_Tasks/
  project_work_status.md
```

## How agents should use it

1. Read the minimum repository surface.
2. Review `resources/activation-checklist.md`.
3. Decide whether the repository likely needs only Layer 1 or both layers.
4. Ask the user to confirm one choice.
5. Apply only the confirmed scope.

## Design principles

- Keep the entry point small.
- Load only what is needed.
- Separate durable rules from temporary progress.
- Write component contracts, not long narrative summaries.
- Make future handoff cheap for both humans and AI agents.

## Status

ProjectOS is a reusable bootstrap package under active refinement.

The current version already supports:

- core repository scaffolding
- node-based documentation roles
- layered operating-rule design
- user-confirmed scope selection before expansion

## Next direction

- add layer-aware scaffold flags such as `--layer core` and `--layer full`
- add starter packs for different repository types
- publish install examples for both local and packaged distribution
