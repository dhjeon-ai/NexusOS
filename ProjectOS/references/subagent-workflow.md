# ProjectOS Subagent Workflow

## Purpose

Subagents are parallel helpers used for clearly bounded work. They should reduce waiting, not create confusion.

## Use subagents when

- the repository is large enough to split work safely
- two or more independent investigations can happen in parallel
- one worker can handle a bounded implementation slice while the main agent keeps the critical path moving

## Do not use subagents when

- the next local action depends on the answer immediately
- the task is too small to justify coordination
- the write scope is unclear or likely to collide

## Operating rules

- define file ownership before delegation
- keep delegated tasks concrete and self-contained
- do not ask multiple workers to edit the same file set without a strong reason
- the main agent should integrate, verify, and explain results

## Documentation rule

If the repository chooses Layer 2, document the subagent policy in architecture or operations pages so later sessions do not improvise different rules.
