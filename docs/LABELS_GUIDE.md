# Labels Guide

## Purpose
Labels are used to keep issues searchable, consistently triaged, and operationally clear. This guide defines the meaning of each label category and the minimal rules for applying them.

## Priority Labels
Exactly **one** priority label should be present on every issue.

- `priority:critical`  
  Apply when there is an immediate and severe impact, such as production outage, critical security exposure, major data loss risk, or a blocker that cannot wait for normal planning.

- `priority:high`  
  Apply when impact is significant (many users affected, core flows broken, release-blocking), but the situation is not at the emergency level of `critical`.

- `priority:medium`  
  Apply for normal planned work with moderate impact. This is the default for most scheduled items once triaged.

- `priority:low`  
  Apply for minor issues and improvements with limited impact, safe to defer.

- `priority:backlog`  
  Apply when the issue is **not yet triaged** or priority is unknown. This is the expected default until review assigns a real priority.

## Status Labels

### Default status label
- `status:needs-review`  
  Means the issue is **pending triage**. Operationally, it indicates that the issue still requires review to confirm scope, validate information (especially for bugs/CI failures), and assign a non-backlog priority.

Practical interpretation:
- With `status:needs-review`, the issue is not considered “ready for scheduling”.
- Removing it implies the issue has been reviewed and has enough clarity to be worked on.

## Type Labels (used by templates)
Type labels describe the nature of the work. Apply **one** type label that matches the issue’s intent.

- `type:bug`  
  A defect: incorrect behavior, crash, regression, or anything that violates expected functionality.

- `type:feature`  
  A new capability or enhancement that adds user-facing value.

- `type:chore`  
  Maintenance and housekeeping: dependency bumps, tooling updates, cleanup tasks, routine refactors without user-visible change.

- `type:documentation`  
  Documentation work: README/docs updates, repository guidelines, template documentation, clarifications, formatting of documentation.

Operational rule:
- If multiple categories apply, choose the dominant one. Split into multiple issues when the work is genuinely different in nature.

## Automation That Applies Labels
Label application is partially automated to reduce drift and enforce consistency:

- An automation applies/maintains:
  - A **single-choice priority label** based on the Issue Form’s Priority field (with a fallback to `priority:backlog` when missing/invalid).
  - The default status label `status:needs-review` while an issue remains `priority:backlog`.
  - A **single-choice type label** from the Issue Form’s Type field when present and valid.

Operational implications:
- Editing an issue body can cause priority/type/status labels to be updated to match the Issue Form fields.
- To change priority/type reliably, update the Issue Form fields in the issue body (the `### Priority` / `### Type` sections) so automation and labels remain aligned.

## Automation That Closes Issues (Acceptance Criteria Auto-close)
Some issues may be automatically closed when their **Acceptance Criteria** are fully completed.

Intended behavior:
- Auto-close evaluates the **latest issue body** and closes only when **all Acceptance Criteria checkboxes are checked**.
- Reopening an issue does **not** immediately re-close it by itself.
- Auto-close is evaluated on **real content changes** (issue body edits), not on reopening alone.

Operational guidance:
- Avoid checking the last remaining Acceptance Criteria box until the issue is truly complete.
- If new Acceptance Criteria items are added after an issue was closed, the safe flow is:
  - Reopen the issue, then
  - Edit the body and add at least one **unchecked** Acceptance Criteria item so it remains open until completion.

## Minimal Labeling Rules
- One priority label only.
- One type label only.
- Use `status:needs-review` to mark issues that still require triage, and remove it once priority and scope are confirmed.

## Related Docs
- Issue templates and Acceptance Criteria flow: `docs/ISSUES_TEMPLATES.md`
- CI/CD workflows (automation details): `docs/CI_CD_WORKFLOWS.md`
- Branching strategy: `docs/BRANCHING_STRATEGY.md`
- Commit convention: `docs/COMMIT_CONVENTION.md`
- Contributing flow: `CONTRIBUTING.md`
