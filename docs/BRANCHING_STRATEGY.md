# Branching Strategy (No Pull Requests)

## Purpose
A simple, verifiable, and repeatable branching model is adopted to keep `main` stable, integrate day-to-day work in `develop`, and implement tasks in short-lived branches, minimizing conflicts and enabling easy rollbacks.

Integration is done via **local merges + direct `git push`**. **Pull Requests are not used**.

## Operating Principles
- `main` is the deployable/production state.
- `develop` is the team’s continuous integration branch.
- Every change is implemented in a short-lived branch created from `develop` (except `hotfix/*`).
- Avoid rewriting shared history (no `push --force`).
- Integrations are recorded with an explicit **merge commit** (`--no-ff`) for traceability.

## Long-lived Branches

### `main`
- Stable and deployable.
- Direct work on `main` is avoided.
- Changes reach `main` from:
  - `develop` (normal release), or
  - `hotfix/*` (urgent fixes).

### `develop`
- Daily integration branch.
- Work branches are created from `develop` and merged back into `develop`.

## Short-lived Branches
Every task or fix is implemented in a short-lived branch.

Expected criteria:
- Target duration: **1 to 3 days** (avoid exceeding **5 business days**).
- Narrow scope: **one intent per branch**.
- Sync often: keep the branch updated with its base to reduce conflicts.
- Clean up: delete the branch after merging.

## Branch Types and Naming Convention

### Format
`<type>/<scope>-<short-slug>`

- `<type>`: branch type (listed below).
- `<scope>`: module/area (api, frontend, infra, docs, auth, db, etc.).
- `<short-slug>`: short description in `kebab-case`.

Optional (recommended for traceability):
- Prefix the slug with the Issue number:  
  `<type>/<scope>-<issueNumber>-<short-slug>`  
  Example: `feature/frontend-123-card-details`

### Examples
- `feature/frontend-card-details`
- `bugfix/api-null-pointer-login`
- `cicd/infra-dependency-check-cache`
- `fix/frontend-navbar-typo`
- `chore/repo-bump-deps`
- `style/frontend-prettier-run`
- `docs/repo-branching-strategy`
- `hotfix/api-auth-500-main`

### Allowed Types and Rules
- `feature/*`: new functionality. Base `develop`, target `develop`.
- `bugfix/*`: functional/user-facing defect fix. Base `develop`, target `develop`.
- `fix/*`: small, tightly scoped fixes. Base `develop`, target `develop`.
- `cicd/*`: pipelines, workflows, deployment, infrastructure. Base `develop`, target `develop`.
- `chore/*`: maintenance, dependencies, tooling, refactor without functional change. Base `develop`, target `develop`.
- `style/*`: formatting, linting, purely stylistic changes. Base `develop`, target `develop`.
- `docs/*`: documentation. Base `develop`, target `develop`.
- `hotfix/*`: urgent fixes when `main` is affected. Base `main`, target `main`, then sync to `develop`.

## Workflow Without Pull Requests

### 1) Create a work branch from `develop`
```bash
git checkout develop
git pull
git checkout -b feature/frontend-card-details
```

### 2) Keep the branch up to date (without rewriting history)

Merging from `develop` is recommended (avoids rebase and avoids rewriting remote history):

```bash
git checkout feature/frontend-card-details
git fetch origin
git merge origin/develop
```

### 3) Merge a work branch into `develop` (explicit merge commit)

Use `--no-ff` to preserve a clear integration commit:

```bash
git checkout develop
git pull
git merge --no-ff feature/frontend-card-details
git push
```

## 4) Delete the branch after merging

```bash
git branch -d feature/frontend-card-details
git push origin --delete feature/frontend-card-details
```

## Integration and Minimum Quality Gate (Before Merging)

Before merging into `develop` or `main`, ensure:

- The branch builds and passes relevant tests locally when applicable.
- GitHub Actions workflows related to the change are green after pushing (see `docs/CI_CD_WORKFLOWS.md`).
- Documentation is updated when the change affects usage, configuration, or behavior.

## Production Hotfix (`hotfix/*`)

### When to Use
Use when a defect in `main` requires an urgent correction (production impacted).

### Procedure

#### 1) Create the hotfix from `main`

```bash
git checkout main
git pull
git checkout -b hotfix/api-auth-500-main
```

#### 2) Implement and push the fix
Push commits to the `hotfix/*` branch as usual.

#### 3) Merge into `main` (explicit merge commit)

```bash
git checkout main
git pull
git merge --no-ff hotfix/api-auth-500-main
git push
```

#### 4) Sync the hotfix into `develop`

```bash
git checkout develop
git pull
git merge --no-ff hotfix/api-auth-500-main
git push
```

#### 5) Delete the hotfix branch

```bash
git branch -d hotfix/api-auth-500-main
git push origin --delete hotfix/api-auth-500-main
```

## Releases: Promoting `develop` to `main`

When publishing a release:

```bash
git checkout main
git pull
git merge --no-ff develop
git push
```

Optional (recommended): tag the release if a versioning convention exists in the repository.

## Prohibited Practices
- No direct work on `main`.
- No Pull Requests as an integration mechanism.
- No rewriting shared history (`push --force`) except in exceptional, coordinated incidents.
- No long-running branches: if scope grows, split the work into smaller branches.

## Repository References
- Commit convention: `docs/COMMIT_CONVENTION.md`
- CI/CD workflows and guarantees: `docs/CI_CD_WORKFLOWS.md`
- Issue templates and Acceptance Criteria flow: `docs/ISSUES_TEMPLATES.md`
- Labels and automations: `docs/LABELS_GUIDE.md`
- Contribution flow: `CONTRIBUTING.md`