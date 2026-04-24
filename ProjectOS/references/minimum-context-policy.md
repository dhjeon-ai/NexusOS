# Minimum Context Policy

## Purpose

The minimum context policy keeps agents from rereading too much of a repository before each task.

## Default reading order

1. Read `nexusos.yaml`.
2. Read the agent rules file listed in `paths.agents_file`.
3. Read the index listed in `paths.index_file`.
4. Open only the directly relevant architecture, component, active task, or agent rule pages.
5. Search code with targeted commands before opening full files.

## Default limit

Before editing, open no more than the configured `context.default_limit` additional context pages unless the task clearly requires deeper reading.

The default limit is `3`.

## When to read more deeply

Read beyond the default limit when the task involves:

- security, authentication, or permissions
- data deletion, migration, or overwrite risk
- path contracts or package layout changes
- state transitions, queues, retries, schedulers, or workflow engines
- explicit documentation verification

Even in these cases, stay inside the relevant scope.

## Editing rule

Before editing, identify:

- the target file
- adjacent call sites or imports
- the minimum verification path

Do not treat broad repository reading as a substitute for focused verification.
