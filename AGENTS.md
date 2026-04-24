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
python ProjectOS/scripts/bootstrap_projectos.py --root /path/to/existing-repo --project-name "Project Name" --mode adopt
```

## Agent Behavior

1. Read `ProjectOS/SKILL.md` before applying NexusOS.
2. Use `--mode adopt` when the target repository already has code, docs, README files, or agent rules.
3. Preserve existing files. Do not overwrite project-specific rules.
4. After applying NexusOS, report created files, preserved files, detected structure, and remaining user decisions.

