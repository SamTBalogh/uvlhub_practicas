# Contributing

## Purpose
This repository follows a lightweight, operational workflow designed to keep `main` stable, integrate changes predictably, and ensure automation (CI/CD, security scans, and issue handling) remains reliable.

All contributors are expected to follow the rules and references in this document.

## Before you start
- Check existing issues and discussions to avoid duplicate work.
- Use the correct Issue Form when creating new work items.
- Make sure you understand the branching and commit rules used in this repository.

## Contribution Flow (No Pull Requests)

### 1) Create or pick an Issue
- Create an issue using the appropriate template (Task, Bug, CI/CD, Fix, Style/Chore, Docs, Hotfix).
- Ensure **Type**, **Priority**, and **Acceptance criteria** are filled correctly.
- If the issue is untriaged, keep `priority:backlog` until review.

Reference: `docs/ISSUES_TEMPLATES.md`

### 2) Create a short-lived branch
- Branch from `develop` for normal work.
- Branch from `main` only for urgent production hotfixes.

Reference: `docs/BRANCHING_STRATEGY.md`

### 3) Implement changes with Conventional Commits
- Follow the Conventional Commits format.
- Keep commits small and intention-focused.
- Use a meaningful scope (`api`, `frontend`, `docs`, etc.).

Reference: `docs/COMMIT_CONVENTION.md`

### 4) Run local checks (when applicable)
Before pushing, run the checks that match your changes:
- Format/lint checks for Python projects.
- Tests (especially if touching core logic).
- Any local build steps required by the component you changed.

CI details and expected checks:
- `docs/CI_CD_WORKFLOWS.md`

### 5) Push and verify CI
- Push your branch and confirm that relevant workflows are green in GitHub Actions.
- If a workflow fails, fix the root cause and push again.

Reference: `docs/CI_CD_WORKFLOWS.md`

### 6) Merge locally (no PRs)
Merges are done via local merge + push:
- Merge your work branch into `develop` with `--no-ff`.
- Delete the branch after merge.

Reference: `docs/BRANCHING_STRATEGY.md`

### 7) Keep issues accurate
- Keep the issue body aligned with the actual work and Acceptance Criteria.
- Be aware that issues may auto-close when all Acceptance Criteria checkboxes are checked.

References:
- Issue templates and Acceptance Criteria flow: `docs/ISSUES_TEMPLATES.md`
- Labels meaning: `docs/LABELS_GUIDE.md`

## Labels and triage
- Use exactly one `priority:*` label and one `type:*` label per issue.
- `status:needs-review` indicates the issue is pending triage.

Reference: `docs/LABELS_GUIDE.md`

## Documentation-first expectation
If a change affects usage, configuration, or expected behavior, update documentation as part of the same work.

Reference: `docs/` (see links below)

## Key References
- Branching strategy: `docs/BRANCHING_STRATEGY.md`
- Commit convention: `docs/COMMIT_CONVENTION.md`
- CI/CD workflows: `docs/CI_CD_WORKFLOWS.md`
- Issue templates: `docs/ISSUES_TEMPLATES.md`
- Labels guide: `docs/LABELS_GUIDE.md`
