# CI/CD Workflows Guide

## Purpose
This repository uses GitHub Actions workflows to enforce commit hygiene, code style, test reliability, and security scanning. This guide documents which workflows exist, what they guarantee, when they run, where to find their reports, and what to do when a workflow fails.

## Where to find results
- **Workflow runs and logs**: GitHub → **Actions** tab → select the workflow → open the run to inspect step logs.
- **Artifacts**: Inside a workflow run page → **Artifacts** section (downloadable reports).
- **Code Scanning (SARIF)**: GitHub → **Security** tab → **Code scanning alerts** (for SARIF uploads).

## Workflows

### 1) Commits Syntax Checker
**Goal / guarantee**
- Validates commit messages against **Conventional Commits** to keep history consistent and automation-friendly. :contentReference[oaicite:0]{index=0}

**Triggers**
- Runs on every `push` and on `pull_request`. :contentReference[oaicite:1]{index=1}

**What to do when it fails**
- A commit message in the pushed range does not match the required format.
- Preferred fixes:
  - If not pushed yet: rewrite locally (`git commit --amend`) before pushing.
  - If already pushed and force-push is not allowed: create a clean branch from the target base and **cherry-pick** the commits, then delete the bad branch.
- Reference the expected format in `docs/COMMIT_CONVENTION.md`.

---

### 2) Python Lint
**Goal / guarantee**
- Enforces Python style and quality gates:
  - `flake8` linting
  - `black --check` formatting
  - `isort --check-only` import ordering :contentReference[oaicite:2]{index=2}

**Triggers**
- Runs on every `push` and on `pull_request`. :contentReference[oaicite:3]{index=3}

**Where to find reports**
- Action run logs (no separate artifact). :contentReference[oaicite:4]{index=4}

**What to do when it fails**
- Reproduce locally:
  - `flake8 app rosemary core`
  - `black --check app rosemary core` (or run `black app rosemary core` to auto-fix)
  - `isort --check-only app rosemary core` (or run `isort app rosemary core` to auto-fix)
- Fix the reported file/line, commit, push again.

---

### 3) Pytest
**Goal / guarantee**
- Runs the test suite using `pytest` and provisions a MariaDB service container for integration tests. :contentReference[oaicite:5]{index=5}
- Ignores Selenium tests via `--ignore-glob='*selenium*'`. :contentReference[oaicite:6]{index=6}

**Triggers**
- Runs on every `push` and on `pull_request` for all branches. :contentReference[oaicite:7]{index=7}

**Where to find reports**
- Action run logs (no separate artifact). :contentReference[oaicite:8]{index=8}

**What to do when it fails**
- Identify whether the failure is:
  - a unit test failure,
  - an integration failure related to DB connectivity/migrations/data,
  - or an environment/config mismatch.
- Reproduce locally when possible:
  - Ensure you can run MariaDB for tests with equivalent env vars and DB name.
  - Run the same command used in CI: `pytest app/modules/ --ignore-glob='*selenium*'`. :contentReference[oaicite:9]{index=9}
- If the failure is DB-related, check:
  - database init/migrations,
  - credentials and host/port assumptions,
  - test isolation (data leakage between tests).

---

### 4) OWASP Dependency-Check
**Goal / guarantee**
- Performs dependency vulnerability scanning.
- Produces a SARIF report and uploads it to GitHub **Code Scanning**.
- Enforces a CVSS threshold gate (`--failOnCVSS 7`). :contentReference[oaicite:10]{index=10}

**Triggers**
- Runs on `push` (all branches), `pull_request`, version tags (`v*`), and manual dispatch (`workflow_dispatch`). :contentReference[oaicite:11]{index=11}

**Where to find reports**
- **Security → Code scanning alerts** (uploaded SARIF).
- Action run logs for scan output and the “Fail if CVSS threshold hit” step. :contentReference[oaicite:12]{index=12}

**What to do when it fails**
- Check Code Scanning alerts to identify the dependency and CVE details.
- Decide remediation:
  - upgrade/patch dependency,
  - remove/replace dependency,
  - adjust dependency usage if false positive is well-justified (document rationale).
- Re-run by pushing a commit that updates dependencies or mitigations.

---

### 5) Trivy IaC Scan
**Goal / guarantee**
- Runs a Trivy filesystem scan and generates a JSON report (`trivy-report.json`) uploaded as an artifact. :contentReference[oaicite:13]{index=13}

**Triggers**
- Runs on `push` to any branch and on version tags (`v*`). :contentReference[oaicite:14]{index=14}

**Where to find reports**
- Action run → **Artifacts** → `trivy-report` (contains `trivy-report.json`). :contentReference[oaicite:15]{index=15}

**What to do when it fails**
- Open the Trivy step logs to see whether the scan itself errored.
- Download the artifact and inspect `trivy-report.json` for:
  - affected file/path,
  - vulnerability identifiers,
  - severity and recommended fixes.
- Apply changes to the relevant IaC/config files and push again.

---

## Repository Issue Automations (Operational CI for GitHub Issues)
These are not build pipelines, but they are enforced automation that affects issue lifecycle.

### 6) Issue Default Labels
**Goal / guarantee**
- Applies and maintains consistent labels based on Issue Form content (priority, type, and default status). :contentReference[oaicite:16]{index=16}

**Where to verify**
- Check the issue’s label set after creation or edits. :contentReference[oaicite:17]{index=17}

**When it might appear “broken”**
- If the expected `### Type` / `### Priority` fields are missing or edited incorrectly, label mapping may not apply as expected.

### 7) Auto-close when Acceptance Criteria is complete
**Goal / guarantee**
- Closes issues automatically when all **Acceptance criteria** checkboxes in the latest issue body are checked.
- Does **not** auto-close on “reopened”; evaluation happens on real content edits. :contentReference[oaicite:18]{index=18}

**Where to verify**
- Issue timeline will show automatic closure; the workflow run appears in Actions. :contentReference[oaicite:19]{index=19}

**What to do if it closes unexpectedly**
- Reopen the issue.
- Edit the issue body and add a new unchecked Acceptance Criteria item to keep it open until the new work is completed.

## Failure playbook (generic)
When any workflow fails:
1) Open the run in **Actions** and identify the failing job/step.
2) Read the error from the bottom up, then locate the first relevant stack trace or command error.
3) Reproduce locally with the same command when feasible.
4) Fix, commit, push, and confirm the rerun is green.
5) If the failure is security scanning, also confirm the result in **Security → Code scanning alerts** (Dependency-Check) or **Artifacts** (Trivy).

## Related Docs
- Branching strategy: `docs/BRANCHING_STRATEGY.md`
- Commit convention: `docs/COMMIT_CONVENTION.md`
- Issue templates: `docs/ISSUES_TEMPLATES.md`
- Labels guide: `docs/LABELS_GUIDE.md`
- Contribution flow: `CONTRIBUTING.md`
