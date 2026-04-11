# ProjectOS Troubleshooting

## Problem
The repository already has a README and several overview docs.

### Why it blocks
Too many "start here" documents create context drift.

### What to do
- Pick one true entry point.
- Move detailed explanations into architecture or component pages.
- Leave the README for external introduction if needed, but keep the operating index separate.

## Problem
The team keeps writing long progress logs instead of durable docs.

### Why it blocks
Logs grow quickly and become expensive to reload.

### What to do
- Put current progress only in the session-status file.
- Move stable rules into architecture pages.
- Move module behavior into component pages.

## Problem
The structure feels heavy for a small repository.

### Why it blocks
Too many nodes too early create maintenance cost.

### What to do
- Start with the index, one architecture page, and one or two component pages.
- Add task and decision pages only when the repository actually needs them.
