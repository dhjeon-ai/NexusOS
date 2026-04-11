# ProjectOS Node Model

## Purpose

ProjectOS treats repository understanding as a small graph of durable document nodes.

Each node has one job so humans and agents do not need to reload the whole repository every time.

## Core node types

### 1. Index node
- Role: Single starting point.
- Typical file: `docs/00_Project_Index.md`
- Contains:
  - how to load context
  - the main architecture pages
  - active tasks
  - core components
  - major decisions

### 2. Architecture node
- Role: System-wide rules and flow descriptions.
- Typical folder: `docs/01_Architecture/`
- Contains:
  - directory structure contract
  - data flow or workflow map
  - operating rules that apply across components

### 3. Component node
- Role: Current contract for one module or service area.
- Typical folder: `docs/02_Components/`
- Contains:
  - source path
  - role
  - inputs and outputs
  - constraints
  - risks

### 4. Task node
- Role: Active continuity for work large enough to span sessions or many files.
- Typical folder: `docs/Active_Tasks/`
- Contains:
  - status
  - created date
  - touched components
  - scope
  - acceptance criteria

### 5. Decision node
- Role: Record a major design choice and why it exists.
- Typical folder: `docs/03_Decisions_ADR/`
- Contains:
  - decision
  - rationale
  - alternatives
  - consequences

### 6. Session-status node
- Role: Keep only current-session progress.
- Typical file: `project_work_status.md`
- Contains:
  - latest milestones
  - current phase
  - blockers

## Relationship rules

- The index node points to architecture, component, task, and decision nodes.
- Architecture nodes explain cross-cutting rules that component nodes should not duplicate.
- Component nodes describe present behavior, not implementation history.
- Task nodes point to the components they touch.
- Decision nodes explain why a system rule exists when the reason is not obvious from code alone.
- Session status is temporary and should never replace durable architecture or component documents.

## Token-saving rule

The graph should allow a normal task to start with:

1. one index node
2. one or two scoped pages
3. the target code files

If more documents are routinely required, the structure is too noisy and should be simplified.
