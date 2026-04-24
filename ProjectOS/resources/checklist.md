# ProjectOS Exit Checklist

- The repository was inspected before scaffolding.
- The user confirmed whether to apply Layer 1 only or Layer 1 plus Layer 2.
- `nexusos.yaml` exists at the repository root.
- `nexusos.yaml` records the agent rules file, docs root, code root, status file, index file, agent rules root, and context-loading limit.
- `AGENTS.md` exists at the repository root or at the configured agent rules path.
- The repository has one clear index page.
- The index page tells a new reader what to open first.
- The index page points agents to `nexusos.yaml` before broader context loading.
- `Agent_Rules/` contains task sizing, verification matrix, decision gates, and handoff packet rules.
- In adopt mode, existing files were preserved and conflicts were handled with NexusOS-specific candidate files.
- In adopt mode, an adoption task report lists created files, preserved files, detected structure, and next action.
- Architecture, component, task, and decision folders exist.
- The session-status file exists at the repository root.
- Selective-loading rules are written down.
- At least the main components have contract pages.
- Active task pages are used only for work large enough to need continuity.
- If Layer 2 was chosen, operating-rule pages exist for task lifecycle, subagent workflow, reporting style, risk exceptions, and sync checks.
- The structure can be explained without repository-specific tribal knowledge.
