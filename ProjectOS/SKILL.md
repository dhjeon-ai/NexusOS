---
name: nexusos-bootstrap
description: Use when starting a new repository or adopting an existing repository into a durable agent work standard with a repository contract file, AGENTS.md rules, low-context entry documents, task sizing, verification gates, handoff packets, component maps, and task flow that stay cheap to load over time.
---

# ProjectOS

## Skill command

Use `/nexusos-bootstrap` when the runtime supports slash-command skills.

## When to use
- A new project needs a durable structure before feature work starts.
- An existing project needs to be safely organized under NexusOS rules without overwriting current files.
- The repository should stay easy for humans and agents to understand with low context cost.
- You want one clear entry point, selective loading rules, and stable documentation contracts.

## Core outcome
Create a project operating system with two expandable layers:

- Layer 1: repository contract, AGENTS.md, core structure, index, task rules, and low-context document contracts
- Layer 2: operating rules for task lifecycle, subagent usage, reporting style, risk exceptions, and sync checks

## Required inputs
- Repository root path
- Main code folders or likely code root
- Preferred docs root, if one already exists
- Preferred agent rules file name, if one already exists
- Preferred status file name, if one already exists
- Preferred project name

## Activation steps

1. Read `module.yaml` to confirm the output structure and capability map.
2. Read `references/node-model.md`, `references/bootstrap-flow.md`, `references/repository-contract.md`, `references/minimum-context-policy.md`, and `references/agent-work-harness.md`.
3. Read `resources/activation-checklist.md` and inspect the target repository before making changes.
4. Decide whether the repository needs only Layer 1 or both Layer 1 and Layer 2.
5. Ask the user to confirm exactly one choice:
   `Do you want ProjectOS core structure only, or core structure plus operating rules?`
6. Choose the script mode:
   - Use `--mode init` for a new or empty repository.
   - Use `--mode adopt` for an existing repository that already has source files, docs, or agent rules.
7. Run `scripts/bootstrap_projectos.py --root <PROJECT_ROOT> --project-name <NAME> --mode <init|adopt>` after the user confirms the scope. Add `--docs-root`, `--code-root`, `--agents-file`, or `--status-file` when the repository already has preferred names.
8. If the user chooses Layer 2, also read:
   - `references/task-lifecycle.md`
   - `references/subagent-workflow.md`
   - `references/reporting-style.md`
   - `references/risk-exceptions.md`
   - `references/sync-checks.md`
9. Customize the generated index, component pages, and rule pages for the target repository.
10. Verify the result with `resources/checklist.md`.

## Capability map

- Bootstrap docs and operating folders: `scripts/bootstrap_projectos.py`
- Adopt existing repositories safely: `scripts/bootstrap_projectos.py --mode adopt`
- Define project-specific paths and agent defaults: generated `nexusos.yaml`
- Install first-read agent rules: generated `AGENTS.md`
- Install work harness rules: generated `docs/Agent_Rules/`
- Define node roles and relationships: `references/node-model.md`
- Apply onboarding and selective-loading workflow: `references/bootstrap-flow.md`
- Apply minimum context loading: `references/minimum-context-policy.md`
- Apply task sizing, verification, decision, and handoff rules: `references/agent-work-harness.md`
- Expand to operating-rule layer: `resources/activation-checklist.md`
- Review target layout and naming examples: `resources/examples.md`

## Design rules

- Treat `nexusos.yaml` as the repository contract for paths, status file names, context limits, and verification commands.
- Treat `AGENTS.md` as the first operating guide for AI agents in the target repository.
- Keep the first-read index short and stable.
- Load one root context document first, then only the minimum relevant pages.
- Separate reusable operating rules from project-specific domain knowledge.
- Treat documents as nodes with clear roles: index, architecture, components, tasks, decisions, session status.
- Prefer durable contracts over long narrative notes.
- Do not apply Layer 2 rules automatically. Inspect first, then ask the user to choose whether Layer 2 is needed.
- In adopt mode, preserve existing files. If the requested `AGENTS.md` already exists, generate `AGENTS.nexusos.md` and point `nexusos.yaml` to it.

## How to execute

Use `resources/checklist.md` as the exit criteria.
Use `resources/activation-checklist.md` to decide whether to stop at Layer 1 or expand to Layer 2.
Use `resources/examples.md` for concrete target layouts.
Use `resources/troubleshooting.md` if an existing repository already has overlapping docs or naming conventions.
