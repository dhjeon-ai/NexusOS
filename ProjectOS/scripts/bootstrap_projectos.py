from __future__ import annotations

import argparse
from pathlib import Path


NEXUSOS_CONFIG_TEMPLATE = """# NexusOS repository contract.
# Agents should read this file first when they need project paths, status files,
# verification commands, or context-loading limits.

project:
  name: "{project_name}"

paths:
  agents_file: "{agents_file}"
  docs_root: "{docs_root}"
  code_root: "{code_root}"
  status_file: "{status_file}"
  index_file: "{docs_root}/00_Project_Index.md"
  agent_rules_root: "{docs_root}/Agent_Rules"

context:
  first_read:
    - "{agents_file}"
    - "{docs_root}/00_Project_Index.md"
  default_limit: 3
  rule: "Read nexusos.yaml, the agent rules file, and the index first; then open only directly relevant architecture, component, task, or agent rule pages."

verification:
  default_commands: []
  notes: "Add project-specific test, lint, build, or smoke-check commands here."

profiles:
  active:
    - core
"""


AGENTS_TEMPLATE = """# {project_name} Agent Rules

This file is the first operating guide for AI agents working in this repository.

Repository contract: `nexusos.yaml`
Docs root: `{docs_root}`
Code root: `{code_root}`
Status file: `{status_file}`

---

## 1. Start Every Task the Same Way

1. Read `nexusos.yaml`.
2. Read `{docs_root}/00_Project_Index.md`.
3. Open only the directly relevant architecture, component, active task, or agent rule pages.
4. Before editing, identify the target file, adjacent call sites, and minimum verification path.

Default context limit: open no more than 3 additional context pages before editing unless the task has security, data-loss, path-contract, or state-transition risk.

---

## 2. Size the Task

Use `{docs_root}/Agent_Rules/task-sizing.md`.

- Tiny: trivial wording, formatting, or single-line cleanup.
- Small: one focused file or a narrow local fix.
- Medium: 2 to 4 files, behavior change, or documentation update required.
- Large: new module, architecture change, cross-surface feature, migration, or handoff risk.

Medium and large work should use an active task page.

---

## 3. Verify Before Done

Use `{docs_root}/Agent_Rules/verification-matrix.md`.

Run the smallest verification that proves the changed behavior works. If verification is skipped, explain why and state the remaining risk.

---

## 4. Stop at Decision Gates

Use `{docs_root}/Agent_Rules/decision-gates.md`.

Ask the user before irreversible or high-risk changes such as data deletion, credential changes, public API breaks, large rewrites, or production deployment.

---

## 5. Record Work for Continuity

Use `{docs_root}/Agent_Rules/handoff-packet.md`.

Keep `{status_file}` short and current during meaningful work. For medium or large tasks, record scope, changed files, verification, and remaining risks in the active task page.

---

## 6. Keep Changes Minimal

Prefer the smallest change that solves the task. Do not rewrite unrelated files. Do not add new rules or documents unless the task needs them.
"""


INDEX_TEMPLATE = """# {project_name} - Project Index

> Purpose: single entry point for project context loading.
> Read this file first, then open only the pages directly related to the task.

---

## How to Use This Index

1. Read `../nexusos.yaml` for repository paths and context limits.
2. Start here.
3. Open only the relevant architecture, component, or active task pages.
4. Create an active task page only for work large enough to need continuity.

## Minimum Context Policy

- Open this index before any broader repository reading.
- By default, open no more than 3 additional context pages before editing.
- Prefer targeted search and small file ranges over full repository scans.
- Read deeper only for security, data-loss risk, path contracts, or state-transition logic.

---

## Architecture

| File | Description |
|---|---|
| [[01_Architecture/Directory_Structure]] | Physical layout and placement rules |
| [[01_Architecture/Data_Flows]] | Main flows and cross-component orchestration |

## Agent Rules

| File | Description |
|---|---|
| [[Agent_Rules/task-sizing]] | Task size classes and required workflow |
| [[Agent_Rules/verification-matrix]] | Minimum verification by change type |
| [[Agent_Rules/decision-gates]] | User confirmation gates for high-risk work |
| [[Agent_Rules/handoff-packet]] | Session and task handoff format |

## Core Components

| File | Module Path | Role |
|---|---|---|
| [[02_Components/Main_Component]] | `<fill-me>` | Primary module or service |

## Active Work

| File | Status |
|---|---|
| [[Active_Tasks/Task_Initial_Setup]] | Ready |
"""


DIRECTORY_TEMPLATE = """# Directory Structure

- **Docs Root**: `{docs_root}`
- **Code Root**: `{code_root}`

## Placement Rules

- Put runtime code in the main code root.
- Put durable operating documents under the docs root.
- Keep current-session progress in the repository root status file.
"""


DATA_FLOWS_TEMPLATE = """# Data Flows

## Primary Flow

- Entry
- Processing
- Storage
- Output
"""


COMPONENT_TEMPLATE = """# Main Component

- **Source Path**: `{code_root}`
- **Role**: Replace with the main responsibility of this module.
- **Related Components**: `TBD`

## Key Contracts
- Input: `TBD`
- Output: `TBD`

## Policies & Constraints
- Replace with the main operating rules.

## Known Issues / Risks
- Replace with current known risks.
"""


TASK_TEMPLATE = """# Task: Initial Setup

- **Status**: Ready
- **Created**: {created}
- **Components Touched**: `TBD`

## Goal

Stand up the first stable ProjectOS structure for this repository.
"""


STATUS_TEMPLATE = """# Project Work Status

- Date: {created}
- Task: Initial ProjectOS setup
- Status: ready
- Summary: Bootstrap structure created. Customize architecture, components, and active task pages next.
- Current phase: initial customization
"""


TASK_SIZING_TEMPLATE = """# Task Sizing

Use this guide to choose the right amount of planning, documentation, and verification.

| Size | Typical Scope | Required Handling |
|---|---|---|
| Tiny | Typo, comment, formatting, or one obvious line | Edit directly and verify if practical |
| Small | One focused file or narrow local behavior fix | Inspect adjacent code and run focused verification |
| Medium | 2 to 4 files, user-visible behavior, or documentation update | Create or update an active task page |
| Large | New module, architecture change, migration, cross-surface feature, or handoff risk | Use an active task page with scope, acceptance criteria, and verification plan |

Escalate the size when a task touches security, data loss, path contracts, state transitions, or public interfaces.
"""


VERIFICATION_MATRIX_TEMPLATE = """# Verification Matrix

Use the smallest check that proves the changed behavior works.

| Change Type | Minimum Verification |
|---|---|
| Docs only | Read the changed page and check links or referenced paths |
| Single code file | Run the closest unit test, script, or direct smoke check |
| Multiple code files | Run the relevant test group or integration smoke check |
| UI change | Inspect the screen or run the UI smoke path |
| Configuration change | Start or dry-run the affected tool and inspect logs |
| Public contract change | Verify callers, examples, and related documentation |
| Security or permission change | Run focused checks and request review before completion |
| Data migration or deletion | Use dry-run or backup first; require user confirmation |

If no verification command exists yet, add a note to `nexusos.yaml` under `verification.notes` or propose a project-specific command.
"""


DECISION_GATES_TEMPLATE = """# Decision Gates

Stop and ask the user before changes that are hard to undo or affect external users.

Ask for confirmation before:

- deleting, overwriting, or migrating data
- changing credentials, secrets, authentication, or permissions
- changing public APIs, file formats, or path contracts
- replacing a working architecture with a large rewrite
- deploying to production or publishing a package
- applying a change whose impact cannot be verified locally

When asking, present one decision at a time and describe the fastest, safest, or most scalable path.
"""


HANDOFF_PACKET_TEMPLATE = """# Handoff Packet

Use this format when a task is medium or large, a session is ending, or another agent needs to continue.

## Current State

- Status: In Progress | Blocked | Done
- Goal:
- Current phase:

## Work Completed

- Files changed:
- Behavior changed:
- Documentation updated:

## Verification

- Working:
- Not yet verified:
- Has risks:

## Remaining Work

- Next action:
- Open risks:
- User decision needed:
"""


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap a ProjectOS starter structure.")
    parser.add_argument("--root", required=True, help="Target repository root path")
    parser.add_argument("--project-name", required=True, help="Project display name")
    parser.add_argument("--docs-root", default="docs", help="Docs root folder relative to the repository root")
    parser.add_argument("--code-root", default="src", help="Primary code root relative to the repository root")
    parser.add_argument(
        "--agents-file",
        default="AGENTS.md",
        help="Agent rules file relative to the repository root",
    )
    parser.add_argument(
        "--status-file",
        default="project_work_status.md",
        help="Session status file relative to the repository root",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    docs_root = root / args.docs_root
    created = "YYYY-MM-DD"

    write_if_missing(
        root / "nexusos.yaml",
        NEXUSOS_CONFIG_TEMPLATE.format(
            project_name=args.project_name,
            agents_file=args.agents_file,
            docs_root=args.docs_root,
            code_root=args.code_root,
            status_file=args.status_file,
        ),
    )
    write_if_missing(
        root / args.agents_file,
        AGENTS_TEMPLATE.format(
            project_name=args.project_name,
            docs_root=args.docs_root,
            code_root=args.code_root,
            status_file=args.status_file,
        ),
    )
    write_if_missing(
        docs_root / "00_Project_Index.md",
        INDEX_TEMPLATE.format(project_name=args.project_name),
    )
    write_if_missing(
        docs_root / "01_Architecture" / "Directory_Structure.md",
        DIRECTORY_TEMPLATE.format(docs_root=args.docs_root, code_root=args.code_root),
    )
    write_if_missing(
        docs_root / "01_Architecture" / "Data_Flows.md",
        DATA_FLOWS_TEMPLATE,
    )
    write_if_missing(
        docs_root / "02_Components" / "Main_Component.md",
        COMPONENT_TEMPLATE.format(code_root=args.code_root),
    )
    write_if_missing(
        docs_root / "Active_Tasks" / "Task_Initial_Setup.md",
        TASK_TEMPLATE.format(created=created),
    )
    write_if_missing(
        docs_root / "Agent_Rules" / "task-sizing.md",
        TASK_SIZING_TEMPLATE,
    )
    write_if_missing(
        docs_root / "Agent_Rules" / "verification-matrix.md",
        VERIFICATION_MATRIX_TEMPLATE,
    )
    write_if_missing(
        docs_root / "Agent_Rules" / "decision-gates.md",
        DECISION_GATES_TEMPLATE,
    )
    write_if_missing(
        docs_root / "Agent_Rules" / "handoff-packet.md",
        HANDOFF_PACKET_TEMPLATE,
    )
    write_if_missing(
        root / args.status_file,
        STATUS_TEMPLATE.format(created=created),
    )

    for folder in [
        docs_root / "03_Decisions_ADR",
        docs_root / "04_Archive",
    ]:
        folder.mkdir(parents=True, exist_ok=True)

    print(f"ProjectOS scaffold created at {root}")


if __name__ == "__main__":
    main()
