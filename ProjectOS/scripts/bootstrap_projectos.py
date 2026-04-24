from __future__ import annotations

import argparse
from dataclasses import dataclass
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
  default_commands:{verification_commands}
  notes: "{verification_notes}"

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
{component_rows}

## Active Work

| File | Status |
|---|---|
| [[Active_Tasks/Task_Initial_Setup]] | Ready |
{adoption_task_row}
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


DISCOVERED_COMPONENT_TEMPLATE = """# {component_name}

- **Source Path**: `{source_path}`
- **Role**: Describe the responsibility of this detected project area.
- **Related Components**: `TBD`

## Key Contracts
- Input: `TBD`
- Output: `TBD`

## Policies & Constraints
- Replace with the main operating rules for this component.

## Known Issues / Risks
- Verify this generated draft against the actual code before treating it as source of truth.
"""


TASK_TEMPLATE = """# Task: Initial Setup

- **Status**: Ready
- **Created**: {created}
- **Components Touched**: `TBD`

## Goal

Stand up the first stable ProjectOS structure for this repository.
"""


ADOPTION_TASK_TEMPLATE = """# Task: NexusOS Adoption

- **Status**: Ready
- **Created**: {created}
- **Components Touched**: `Project structure`, `Agent rules`, `Documentation`

## Goal

Bring this existing repository under the NexusOS operating standard without overwriting existing project files.

## Detected Structure

- Docs root: `{docs_root}`
- Code root: `{code_root}`
- Agent rules file: `{agents_file}`
- Status file: `{status_file}`
- Verification commands: {verification_summary}

## Files Created

{created_files}

## Files Preserved

{preserved_files}

## Next Action

Review generated component drafts and fill in project-specific verification commands if needed.
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


@dataclass
class WriteResult:
    created: list[str]
    preserved: list[str]


def write_tracked(path: Path, content: str, root: Path, result: WriteResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rel_path = path.relative_to(root).as_posix()
    if path.exists():
        result.preserved.append(rel_path)
        return
    path.write_text(content, encoding="utf-8")
    result.created.append(rel_path)


def detect_docs_root(root: Path) -> str:
    for candidate in ["docs", "wiki", "Wiki", "documentation", "Documentation"]:
        if (root / candidate).is_dir():
            return candidate
    return "docs"


def detect_code_roots(root: Path) -> list[str]:
    candidates = ["src", "app", "apps", "lib", "server", "backend", "frontend", "client", "packages"]
    found = [candidate for candidate in candidates if (root / candidate).is_dir()]
    if found:
        return found

    marker_files = ["package.json", "pyproject.toml", "go.mod", "Cargo.toml"]
    if any((root / marker).exists() for marker in marker_files):
        return ["."]

    return ["src"]


def detect_verification_commands(root: Path) -> list[str]:
    commands: list[str] = []
    if (root / "package.json").exists():
        commands.append("npm test")
    if (
        (root / "pyproject.toml").exists()
        or (root / "pytest.ini").exists()
        or (root / "tests").is_dir()
    ):
        commands.append("pytest")
    if (root / "go.mod").exists():
        commands.append("go test ./...")
    if (root / "Cargo.toml").exists():
        commands.append("cargo test")
    return commands


def format_yaml_list(items: list[str]) -> str:
    if not items:
        return " []"
    return "\n" + "\n".join(f'    - "{item}"' for item in items)


def choose_agents_file(root: Path, requested: str, mode: str) -> str:
    requested_path = root / requested
    if mode == "adopt" and requested_path.exists():
        requested_obj = Path(requested)
        suffix = requested_obj.suffix or ".md"
        stem = requested_obj.stem or "AGENTS"
        parent = requested_obj.parent
        return (parent / f"{stem}.nexusos{suffix}").as_posix()
    return requested


def make_component_name(source_path: str) -> str:
    if source_path == ".":
        return "Repository_Root"
    normalized = source_path.replace("\\", "/").strip("/")
    parts = [part for part in normalized.replace("-", "_").split("/") if part]
    return "_".join(part[:1].upper() + part[1:] for part in parts) or "Main_Component"


def format_component_rows(component_names: list[str], source_paths: list[str]) -> str:
    rows = []
    for name, source_path in zip(component_names, source_paths):
        rows.append(f"| [[02_Components/{name}]] | `{source_path}` | Detected project area |")
    return "\n".join(rows)


def format_adoption_summary(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- `{item}`" for item in items)


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap a ProjectOS starter structure.")
    parser.add_argument("--root", required=True, help="Target repository root path")
    parser.add_argument("--project-name", required=True, help="Project display name")
    parser.add_argument(
        "--mode",
        choices=["init", "adopt"],
        default="init",
        help="init creates a starter structure; adopt safely adds NexusOS to an existing repository",
    )
    parser.add_argument("--docs-root", default=None, help="Docs root folder relative to the repository root")
    parser.add_argument("--code-root", default=None, help="Primary code root relative to the repository root")
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
    docs_root_name = args.docs_root or (detect_docs_root(root) if args.mode == "adopt" else "docs")
    detected_code_roots = detect_code_roots(root) if args.mode == "adopt" else [args.code_root or "src"]
    code_root_name = args.code_root or detected_code_roots[0]
    agents_file_name = choose_agents_file(root, args.agents_file, args.mode)
    verification_commands = detect_verification_commands(root) if args.mode == "adopt" else []
    verification_notes = (
        "Detected default commands from project files. Confirm they are correct."
        if verification_commands
        else "Add project-specific test, lint, build, or smoke-check commands here."
    )
    docs_root = root / docs_root_name
    created = "YYYY-MM-DD"
    result = WriteResult(created=[], preserved=[])
    if agents_file_name != args.agents_file and (root / args.agents_file).exists():
        result.preserved.append(args.agents_file)
    component_source_paths = detected_code_roots if args.mode == "adopt" else [code_root_name]
    component_names = [make_component_name(path) for path in component_source_paths]
    component_rows = (
        format_component_rows(component_names, component_source_paths)
        if args.mode == "adopt"
        else "| [[02_Components/Main_Component]] | `<fill-me>` | Primary module or service |"
    )
    adoption_task_row = "| [[Active_Tasks/Task_NexusOS_Adoption]] | Ready |" if args.mode == "adopt" else ""

    write_tracked(
        root / "nexusos.yaml",
        NEXUSOS_CONFIG_TEMPLATE.format(
            project_name=args.project_name,
            agents_file=agents_file_name,
            docs_root=docs_root_name,
            code_root=code_root_name,
            status_file=args.status_file,
            verification_commands=format_yaml_list(verification_commands),
            verification_notes=verification_notes,
        ),
        root,
        result,
    )
    write_tracked(
        root / agents_file_name,
        AGENTS_TEMPLATE.format(
            project_name=args.project_name,
            docs_root=docs_root_name,
            code_root=code_root_name,
            status_file=args.status_file,
        ),
        root,
        result,
    )
    write_tracked(
        docs_root / "00_Project_Index.md",
        INDEX_TEMPLATE.format(
            project_name=args.project_name,
            component_rows=component_rows,
            adoption_task_row=adoption_task_row,
        ),
        root,
        result,
    )
    write_tracked(
        docs_root / "01_Architecture" / "Directory_Structure.md",
        DIRECTORY_TEMPLATE.format(docs_root=docs_root_name, code_root=code_root_name),
        root,
        result,
    )
    write_tracked(
        docs_root / "01_Architecture" / "Data_Flows.md",
        DATA_FLOWS_TEMPLATE,
        root,
        result,
    )
    if args.mode == "adopt":
        for component_name, source_path in zip(component_names, component_source_paths):
            write_tracked(
                docs_root / "02_Components" / f"{component_name}.md",
                DISCOVERED_COMPONENT_TEMPLATE.format(
                    component_name=component_name,
                    source_path=source_path,
                ),
                root,
                result,
            )
    else:
        write_tracked(
            docs_root / "02_Components" / "Main_Component.md",
            COMPONENT_TEMPLATE.format(code_root=code_root_name),
            root,
            result,
        )
    write_tracked(
        docs_root / "Active_Tasks" / "Task_Initial_Setup.md",
        TASK_TEMPLATE.format(created=created),
        root,
        result,
    )
    write_tracked(
        docs_root / "Agent_Rules" / "task-sizing.md",
        TASK_SIZING_TEMPLATE,
        root,
        result,
    )
    write_tracked(
        docs_root / "Agent_Rules" / "verification-matrix.md",
        VERIFICATION_MATRIX_TEMPLATE,
        root,
        result,
    )
    write_tracked(
        docs_root / "Agent_Rules" / "decision-gates.md",
        DECISION_GATES_TEMPLATE,
        root,
        result,
    )
    write_tracked(
        docs_root / "Agent_Rules" / "handoff-packet.md",
        HANDOFF_PACKET_TEMPLATE,
        root,
        result,
    )
    write_tracked(
        root / args.status_file,
        STATUS_TEMPLATE.format(created=created),
        root,
        result,
    )
    if args.mode == "adopt":
        write_tracked(
            docs_root / "Active_Tasks" / "Task_NexusOS_Adoption.md",
            ADOPTION_TASK_TEMPLATE.format(
                created=created,
                docs_root=docs_root_name,
                code_root=code_root_name,
                agents_file=agents_file_name,
                status_file=args.status_file,
                verification_summary=", ".join(verification_commands) if verification_commands else "None detected",
                created_files=format_adoption_summary(result.created),
                preserved_files=format_adoption_summary(result.preserved),
            ),
            root,
            result,
        )

    for folder in [
        docs_root / "03_Decisions_ADR",
        docs_root / "04_Archive",
    ]:
        folder.mkdir(parents=True, exist_ok=True)

    print(f"ProjectOS {args.mode} completed at {root}")
    print(f"Created files: {len(result.created)}")
    print(f"Preserved existing files: {len(result.preserved)}")


if __name__ == "__main__":
    main()
