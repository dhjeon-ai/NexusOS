# ProjectOS Risk Exceptions

## Purpose

Some changes need deeper reading even when the normal rule is selective loading.

## Read more deeply when the task involves

- security, authentication, or secrets
- destructive file operations
- path contracts or filesystem layout changes
- queue, retry, scheduling, or state-transition logic
- data loss risk
- explicit documentation verification

## Rule

Deep reading should still stay inside the relevant scope.

Do not treat a risk exception as permission to reread the entire repository.
