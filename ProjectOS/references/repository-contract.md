# Repository Contract

## Purpose

`nexusos.yaml` is the project-specific contract that tells agents where the important files live and which defaults to follow.

Use it to avoid hardcoded assumptions about:

- documentation root
- code root
- session status file
- first-read index
- context-loading limit
- project verification commands

## Generated default

The bootstrap script creates this file at the repository root:

```yaml
project:
  name: "Example Project"

paths:
  docs_root: "docs"
  code_root: "src"
  status_file: "project_work_status.md"
  index_file: "docs/00_Project_Index.md"

context:
  first_read:
    - "docs/00_Project_Index.md"
  default_limit: 3
  rule: "Read the index first, then open only the directly relevant architecture, component, or task pages."

verification:
  default_commands: []
  notes: "Add project-specific test, lint, build, or smoke-check commands here."

profiles:
  active:
    - core
```

## Agent behavior

1. Read `nexusos.yaml` before assuming repository paths.
2. Use `paths.index_file` as the first durable context document.
3. Use `context.default_limit` as the default number of additional context pages to open before editing.
4. Use `verification.default_commands` as the preferred verification surface when the project owner has filled it in.
5. Update this file only when the project contract changes, not for ordinary implementation work.

## Customization rule

Keep `nexusos.yaml` small. Store stable project defaults here, not long explanations or temporary task notes.
