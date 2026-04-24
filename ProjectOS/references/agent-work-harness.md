# Agent Work Harness

## Purpose

The work harness gives agents one repeatable way to size work, verify changes, stop for user decisions, and hand off unfinished tasks.

The bootstrap script installs these files under `docs/Agent_Rules/` by default:

- `task-sizing.md`
- `verification-matrix.md`
- `decision-gates.md`
- `handoff-packet.md`

It also installs `AGENTS.md` at the repository root.

## Installed roles

| File | Role |
|---|---|
| `AGENTS.md` | First operating guide for AI agents |
| `docs/Agent_Rules/task-sizing.md` | Classifies tiny, small, medium, and large work |
| `docs/Agent_Rules/verification-matrix.md` | Maps change types to minimum verification |
| `docs/Agent_Rules/decision-gates.md` | Lists high-risk changes that need user confirmation |
| `docs/Agent_Rules/handoff-packet.md` | Defines the continuity summary for task handoff |

## Agent behavior

1. Read `AGENTS.md` after `nexusos.yaml`.
2. Use task sizing before deciding whether to create an active task page.
3. Use the verification matrix before reporting work as done.
4. Stop at decision gates instead of silently applying high-risk changes.
5. Use the handoff packet for medium or large work, blocked work, or session-close summaries.

## Design rule

Keep root `AGENTS.md` short. Put detailed project-specific rules in `docs/Agent_Rules/` or another rules root configured in `nexusos.yaml`.
