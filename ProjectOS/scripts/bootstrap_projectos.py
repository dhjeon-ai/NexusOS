from __future__ import annotations

import argparse
from pathlib import Path


NEXUSOS_CONFIG_TEMPLATE = """# NexusOS repository contract.
# Agents should read this file first when they need project paths, status files,
# verification commands, or context-loading limits.

project:
  name: "{project_name}"

paths:
  docs_root: "{docs_root}"
  code_root: "{code_root}"
  status_file: "{status_file}"
  index_file: "{docs_root}/00_Project_Index.md"

context:
  first_read:
    - "{docs_root}/00_Project_Index.md"
  default_limit: 3
  rule: "Read the index first, then open only the directly relevant architecture, component, or task pages."

verification:
  default_commands: []
  notes: "Add project-specific test, lint, build, or smoke-check commands here."

profiles:
  active:
    - core
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
