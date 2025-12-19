# Issue Templates Guide

## Purpose
Issue Forms standardize reporting and planning so that every issue is actionable, triageable, and traceable. Templates also apply consistent default labels and enforce required metadata such as **Type**, **Priority**, and **Acceptance criteria**.

## Available Issue Forms

| Template | Use when | Default labels |
|---|---|---|
| **Task** (`task.yml`) | Planned work item (non-urgent), typically feature, refactor, or chore | `task`, `type:feature`, `status:needs-review` :contentReference[oaicite:0]{index=0} |
| **Bug** (`bug.yml`) | Reproducible defect with clear steps and expected behavior | `bug`, `type:bug`, `status:needs-review` :contentReference[oaicite:1]{index=1} |
| **CI/CD** (`cicd.yml`) | Workflow/pipeline/deployment work, failures, or improvements | `ci/cd`, `type:feature`, `status:needs-review` :contentReference[oaicite:2]{index=2} |
| **Fix** (`fix.yml`) | Focused, small corrective adjustment (bug/refactor/chore) | `fix`, `status:needs-review` :contentReference[oaicite:3]{index=3} |
| **Style / Chore** (`chore_style.yml`) | Formatting, linting, cleanup, maintenance, minor refactor without functional change | `chore`, `style`, `type:chore`, `status:needs-review` :contentReference[oaicite:4]{index=4} |
| **Docs** (`docs.yml`) | Documentation-only changes | `docs`, `type:documentation`, `status:needs-review` :contentReference[oaicite:5]{index=5} |
| **Hotfix** (`hotfix.yml`) | Urgent production fix that must be applied to `main` ASAP | `hotfix`, `type:bug`, `status:needs-review` :contentReference[oaicite:6]{index=6} |
| **Blank Issue** (`config.yml`) | Only when no template fits | Enabled :contentReference[oaicite:7]{index=7} |

## How to choose the right template
- A user-facing defect with reproduction steps should use **Bug**. :contentReference[oaicite:8]{index=8}  
- A build, test, scan, or deployment workflow problem should use **CI/CD** and include the workflow/job path and the key error. :contentReference[oaicite:9]{index=9}  
- A small targeted correction that is not a full bug report should use **Fix**. :contentReference[oaicite:10]{index=10}  
- Any urgent incident that requires patching `main` should use **Hotfix** and must include branch instructions. :contentReference[oaicite:11]{index=11}  
- Non-functional maintenance or formatting should use **Style / Chore**. :contentReference[oaicite:12]{index=12}  
- Documentation-only work should use **Docs**. :contentReference[oaicite:13]{index=13}  
- Planned, structured work should use **Task**. :contentReference[oaicite:14]{index=14}  

## Shared fields and required inputs
Most templates include:
- **Type** (dropdown): required. The chosen value should match the actual nature of the work.   
- **Priority** (dropdown): required. Use `priority:backlog` when unsure, then update during triage.   
- **Acceptance criteria** (checkbox list): required in templates that include it. Write concrete, verifiable checkboxes.   
- **References**: optional where present, but recommended for logs, screenshots, related issues, and links.   

## Template-specific guidance

### Task
Use for planned work (not an urgent fix). Required fields:
- **Goal**: what is being achieved. :contentReference[oaicite:19]{index=19}  
- **Scope**: what is included and excluded. :contentReference[oaicite:20]{index=20}  
- **Checklist**: concrete steps, as checkboxes. :contentReference[oaicite:21]{index=21}  
- **Acceptance criteria**: completion definition, as checkboxes. :contentReference[oaicite:22]{index=22}  

### Bug
Use for reproducible bugs. Required fields:
- **Description**
- **Steps to reproduce**
- **Expected result** :contentReference[oaicite:23]{index=23}  

### CI/CD
Use for workflow and pipeline work. Required fields:
- **Context**: what fails or what is needed
- **Workflow / Job**: path and job name (example: `.github/workflows/pytests.yml -> test`)
- **Main error**: paste the key error (keep it minimal but sufficient)
- **Acceptance criteria**: must describe the passing condition :contentReference[oaicite:24]{index=24}  
Optional:
- **Run link**: GitHub Actions run URL :contentReference[oaicite:25]{index=25}  

### Fix
Use for focused, small adjustments. Required fields:
- **What will be fixed**
- **Acceptance criteria** :contentReference[oaicite:26]{index=26}  
Optional:
- **Impact / risk**
- **References** :contentReference[oaicite:27]{index=27}  

### Style / Chore
Use for non-functional changes (formatting, linting, cleanup, maintenance). Required fields:
- **Description**
- **Acceptance criteria** (includes “no functional behavior changed”) :contentReference[oaicite:28]{index=28}  
Optional:
- **Proposed changes** checklist
- **Tools involved**
- **References** :contentReference[oaicite:29]{index=29}  

### Docs
Use for documentation-only work. Required fields:
- **Summary**: what changes and why
- **Location**: where the change is made (files/paths)
- **Acceptance criteria**: correctness, links, spelling/formatting :contentReference[oaicite:30]{index=30}  

### Hotfix
Use for urgent fixes that must land in `main`. Required fields:
- **Impact** (real-world severity)
- **Problem description**
- **Fix plan**
- **Acceptance criteria**
- **Branch instructions** (must follow: `hotfix/<scope>-<short-slug>` from `main`) :contentReference[oaicite:31]{index=31}  
Optional:
- **Mitigation / workaround**
- **Steps to reproduce (if applicable)** :contentReference[oaicite:32]{index=32}  

## Acceptance Criteria and issue auto-close behavior
Some issues can be automatically closed when **all Acceptance criteria checkboxes are checked**. To avoid unintended closure:

- Reopening an issue never closes it automatically.
- Auto-close is evaluated only on real content changes (issue body edits) and only closes when all Acceptance criteria checkboxes are checked in the latest issue body.
- If new Acceptance Criteria items are added after closure, the safe flow is: reopen the issue, then edit the body and add at least one unchecked Acceptance Criteria item to keep it open until completion.

Operational recommendations:
- Avoid checking the last unchecked box until the issue is genuinely ready to be closed.
- When adding new work after closure, add the new unchecked Acceptance Criteria item before making other edits.

## Notes on labels applied by templates
Templates apply default labels at creation time. Type and priority values should be kept consistent with the issue content, and labels should reflect the chosen template’s intent.   

## Related Docs
- Labels guide: `docs/LABELS_GUIDE.md`
- Branching strategy: `docs/BRANCHING_STRATEGY.md`
- Commit convention: `docs/COMMIT_CONVENTION.md`
- CI/CD workflows: `docs/CI_CD_WORKFLOWS.md`
- Contributing flow: `CONTRIBUTING.md`
