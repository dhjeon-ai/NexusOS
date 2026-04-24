# NexusOS Agent Entry

This repository packages NexusOS as a reusable agent work standard.

## Available Skill Command

Use this skill command when the runtime supports slash-command skills:

```text
/nexusos-bootstrap
```

Use it for either goal:

- Set up NexusOS in a new repository.
- Adopt an existing repository into NexusOS without overwriting current files.

## Direct Script Fallback

If slash-command skills are not available, run the bootstrap script directly.

New repository:

```bash
python ProjectOS/scripts/bootstrap_projectos.py --root /path/to/new-repo --project-name "Project Name" --mode init
```

Existing repository:

```bash
python ProjectOS/scripts/bootstrap_projectos.py --root /path/to/existing-repo --project-name "Project Name" --mode adopt --layer core --runtime local
```

Use `--layer full` when the user also wants task lifecycle, subagent workflow, reporting style, risk exception, and sync check pages.
Use `--runtime local` when the user wants Hermes-like lessons, reflection prompts, NexusOS checks, and a git hook template.

## Agent Behavior

1. Read `ProjectOS/SKILL.md` before applying NexusOS.
2. Use `--mode adopt` when the target repository already has code, docs, README files, or agent rules.
3. Preserve existing files. Do not overwrite project-specific rules.
4. After applying NexusOS, report created files, preserved files, detected structure, and remaining user decisions.
5. In adopt mode, guide the user through agent-rule reconciliation, documentation entrypoint reconciliation, verification command confirmation, and component draft review.
6. When the user corrects the agent, record the lesson in the generated `lessons.md`. If a repeatable workflow emerges, record it in `skill-candidates.md`.
