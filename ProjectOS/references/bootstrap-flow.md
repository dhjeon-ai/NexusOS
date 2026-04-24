# ProjectOS Bootstrap Flow

## Goal

Stand up a repository structure that remains understandable after months of feature work.

## Scope gate before bootstrap

Before scaffolding, the agent should inspect the repository and decide which of these two modes fits:

- Layer 1 only
  - Use when the repository is small, early, or unlikely to need formal multi-session operations yet.
- Layer 1 plus Layer 2
  - Use when the repository will benefit from durable task rules, subagent coordination, reporting rules, risk exceptions, and sync checks.

The agent must not choose silently.

After the initial inspection, the agent should ask the user one direct confirmation:

`Do you want ProjectOS core structure only, or core structure plus operating rules?`

Only after that confirmation should the scaffold be applied.

## Mode selection

Use `--mode init` when the target repository is new or mostly empty.

Use `--mode adopt` when the target repository already has code, docs, README files, or agent rule files. Adopt mode must preserve existing files and add only missing NexusOS structure.

Use `--layer core` for the base operating standard.

Use `--layer full` when the user also wants task lifecycle, subagent workflow, reporting style, risk exception, and sync check pages.

## Phase 1. Pick the root contract

Create one root `nexusos.yaml` file and one root docs folder.

The repository contract stores the project-specific defaults that agents should not guess:

- project name
- agent rules file
- docs root
- code root
- status file
- index file
- agent rules root
- context-loading limit
- verification commands

In adopt mode, infer these defaults from the existing repository when explicit arguments are not provided.

Recommended default:

```text
nexusos.yaml
AGENTS.md
docs/
  00_Project_Index.md
  01_Architecture/
  02_Components/
  03_Decisions_ADR/
  04_Archive/
  Active_Tasks/
  Agent_Rules/
```

Create one root session-status file outside the docs folder:

```text
project_work_status.md
```

## Phase 2. Write the first-read index

The index should answer only four things:

- where to start
- what architecture pages exist
- what core components exist
- what active tasks exist

Do not turn the index into a long wiki.

The index should point agents back to `nexusos.yaml` for paths, context limits, verification commands, and agent rules.

## Phase 3. Lock selective loading rules

Add simple operating rules such as:

- read `nexusos.yaml` before assuming repository paths
- read `AGENTS.md` before starting implementation
- read one root page first
- open only directly relevant pages
- use the configured context limit before editing
- avoid broad rereads
- use active task pages only for medium or large work

## Phase 3b. Install the work harness

Create a small agent rule set:

- task sizing
- verification matrix
- decision gates
- handoff packet

These files define how agents decide work size, prove completion, stop for human decisions, and preserve continuity.

## Phase 3c. Adopt existing structure

When using adopt mode:

- detect existing docs roots such as `docs/`, `wiki/`, or `documentation/`
- detect code roots such as `src/`, `app/`, `backend/`, `frontend/`, or `packages/`
- detect basic verification commands from `package.json`, `pyproject.toml`, `pytest.ini`, `go.mod`, or `Cargo.toml`
- preserve existing files
- create `AGENTS.nexusos.md` when `AGENTS.md` already exists
- create `Task_NexusOS_Adoption.md` with created files, preserved files, and next actions
- guide the next agent through agent-rule reconciliation, documentation entrypoint reconciliation, verification command confirmation, component draft review, and layer follow-up

## Phase 4. Define component contracts

Create component pages for the modules that most work will touch.

Each page should describe:

- what it does
- where it lives
- what goes in and out
- which rules or risks matter

## Phase 5. Add task continuity

Use active task pages only when the work:

- spans three or more files
- introduces a new module
- changes a contract
- needs handoff continuity

## Phase 6. Add decision records

Create a decision page only when a future reader would ask:

"Why is the system built this way instead of another way?"

## Phase 7. Keep the system healthy

- update component pages when behavior changes
- archive completed task pages
- keep session status short and current
- resist adding duplicate overview files

## Layer 2 expansion

If the user chooses Layer 2, run with `--layer full` to add rule pages for:

- task lifecycle
- subagent workflow
- reporting style
- risk exceptions
- sync checks
