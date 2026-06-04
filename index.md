---
title: "Using AI Coding Agents Responsibly with Sensitive Research Data"
author: "Author Name"
bibliography: references.bib
format:
  html: default
---

## Learning Objectives

By the end of this tutorial, you will be able to:

1.  Explain why AI coding agents create privacy, containment, validity, provenance, and disclosure risks in computational social science workflows.
2.  Set up a two-environment workflow for agent-assisted coding on mock data and agent-free analysis on protected real data.
3.  Use Git, Docker, mock data, `.gitignore`, and validation checks to reduce the risk that sensitive data reach an AI provider.
4.  Configure and use coding agents in a contained way.
5.  Document the workflow clearly for collaborators, reviewers, and readers.

## Target Audience

This tutorial is aimed at computational social science and computational communication researchers who use scripts, notebooks, Git, and command-line tools in research projects. It assumes basic familiarity with Git and Python or R-style analysis workflows, but it does not assume prior experience with AI coding agents.

The tutorial is also written for reviewers and collaborators who need to understand what it means when a manuscript states that agent-assisted code development was used without giving the agent access to protected data.

## Setting Up the Computational Environment

This tutorial uses only the Python standard library for its runnable examples. Docker is used to make the mock-data development environment reproducible and to teach containment principles.

Install the following tools locally:

- Git
- Docker Desktop or a compatible Docker installation
- An AI coding agent, such as Claude Code, ChatGPT Codex, GitHub Copilot-style tools, or a local/open-source coding agent
- Access to a clean protected environment, preferably an institutional server, HPC system, secure VM, or other environment approved for sensitive research data

The tutorial repository includes:

- `Dockerfile` and `docker-compose.yml` for local mock-data execution.
- `mock-data/posts.csv` as fake communication data.
- `src/analyze_posts.py` as a small example analysis script.
- `tests/` and `validation/` scripts for basic checks.
- Templates for agent rules, validation, safe debugging, and disclosure.

## Duration

Around half a day for reading and exercises. Around one day if readers also implement the workflow in an existing research project.

## Social Science Use Case

The running example is a computational communication project that analyzes platform posts. In a real project, posts might come from scraped social media, donated digital trace data, platform APIs, or restricted archives. Such data can include usernames, text, timestamps, profile URLs, images, video metadata, locations, and other personal or contextual information.

The tutorial uses fake mock data only. No real scraped communication data should appear in the public repository.

## Core Principle

AI coding agents can be useful for writing, refactoring, testing, and documenting code. They are also unreliable systems that may see prompts, files, terminal output, logs, screenshots, and tool results. In sensitive-data research, this creates a simple rule:

> Agents may help produce code, but they must not see protected data or directly produce research evidence.

The recommended workflow is therefore:

> Agent-assisted code development, agent-free protected analysis.

This architecture strongly mitigates privacy and containment risks. It does not, by itself, solve validity, interpretation, or accountability risks. Those require human review, transparent documentation, and validation.

## Basic Coding-Agent Concepts for Researchers and Reviewers

Coding agents vary by provider and interface, but most work by reading some combination of prompt text, open files, selected repository context, terminal output, logs, and tool results. Some can edit files, run shell commands, install packages, use Git, browse the web, inspect screenshots, or call external tools.

For researchers, the key containment question is not only "what did I paste into the chat?" It is also:

- Which files were open or indexed?
- Which directory did the agent start in?
- Which commands did the agent run?
- Which logs, stack traces, screenshots, or previews were visible?
- Which external tools, plugins, or telemetry systems were active?
- Could the agent read home folders, cloud drives, credentials, or protected data paths?

For reviewers, the key evidence is not the brand name of the agent. The key evidence is whether the project can show:

- Written agent rules.
- A repository structure that separates code, mock data, real data, logs, and outputs.
- Mock-data-only agent development.
- Agent-free execution on protected data.
- Validation checks that were not merely generated and accepted by the same agent.
- A disclosure statement explaining what the agent did and did not access.

### Minimal Agent Containment Rules

When using a coding agent:

1.  Start the agent only inside the dirty agent-safe repository.
2.  Do not open protected files in the same editor or workspace.
3.  Disable broad workspace indexing where possible.
4.  Deny unnecessary permissions, especially unrestricted file access, shell access, web access, screenshots, and secret access.
5.  Do not mount home folders, cloud storage, SSH keys, credentials, or real-data directories into the agent workspace.
6.  Review all proposed file changes before accepting them.
7.  Keep the agent away from real-data logs, tables, plots, screenshots, and error messages.
8.  Treat agent-generated tests and explanations as useful drafts, not as independent verification.

The companion file `AGENT_RULES.md` provides a project-level version of these rules.

## Two-Environment Architecture

The workflow uses two environments connected by a code-only Git repository.

``` text
Dirty agent environment              Code-only bridge             Clean protected environment
-------------------------            ----------------             ----------------------------
AI coding agent allowed        ->     GitHub/Codeberg/GitLab  ->   No AI coding agent
Docker allowed                        Reviewed code only           Real data live here
Mock data only                        No real outputs              Protected outputs stay here
Tests and docs                        No secrets or logs           Validation on real data
```

### Dirty Environment

The dirty environment is where agent-assisted development happens. It may be a local machine or a dirty VM. It contains:

- Code.
- Mock data.
- Tests.
- Documentation.
- Docker files.
- Agent instructions.

It must not contain:

- Real data.
- Real-data outputs.
- Secrets or credentials.
- Protected logs.
- Screenshots or notebooks showing real observations.

### Clean Environment

The clean environment is where real-data analysis happens. The default is an institutional server, HPC system, secure VM, or other environment approved for sensitive data. It contains:

- Real data stored outside the Git repository.
- Reviewed code pulled from Git.
- Protected outputs and validation logs.

It must not contain:

- AI coding agents.
- Agentic IDE plugins.
- Third-party LLM access to project files.
- Agent-visible logs, screenshots, or notebooks with real data.

### Fallback: Two Local VMs on One Device

If no institutional infrastructure is available, researchers may use two local VMs on the same device. This is a fallback, not the preferred option.

- Dirty VM: internet and agent access allowed; contains code, mock data, Docker, and tests.
- Clean VM: no agent installed; contains real data; pulls code from Git; stores real data outside synced or shared folders.
- Do not share clipboards, folders, screenshots, logs, or mounted home directories between the two VMs.
- Do not allow the dirty VM to browse the clean VM's files.
- Do not push real-data artifacts from the clean VM to Git.

This fallback still requires institutional, ethical, and legal approval for the data involved.

## Build the Agent-Safe Repository

A minimal repository should separate code, mock data, validation, documentation, and protected artifacts:

``` text
project/
  src/
  tests/
  mock-data/
  validation/
  docs/
  templates/
  AGENT_RULES.md
  .gitignore
  Dockerfile
  docker-compose.yml
  README.md
  LICENSE
  CITATION.cff
  index.md
```

Real data, real outputs, logs, credentials, and notebooks with real outputs should not be tracked by Git. The `.gitignore` in this repository blocks common risky paths such as:

``` text
data/
outputs/
logs/
.env
*.key
*.pem
*.sqlite
.ipynb_checkpoints/
```

Treat `.gitignore` as a safety net, not as the main protection. The main protection is that real data never enter the dirty environment.

## Develop with Docker and Mock Data

Docker helps make the dirty development environment reproducible. In this tutorial, the Docker container mounts only the repository and uses fake data.

Run the mock analysis locally:

``` bash
# dirty environment
docker compose run --rm dirty-dev python -m src.analyze_posts \
  --input mock-data/posts.csv \
  --output outputs/mock-summary.csv \
  --validation-report outputs/mock-validation.json
```

Run the tests:

``` bash
# dirty environment
docker compose run --rm dirty-dev python -m unittest discover -s tests
```

This container is not a complete security boundary. It is a reproducibility and containment aid. Do not mount home directories, cloud drives, credentials, SSH keys, or real-data folders.

## Run Real Data in the Clean Environment

On the clean environment, pull reviewed code from Git and point the script to real data stored outside the repository:

``` bash
# clean environment
python -m src.analyze_posts \
  --input /protected/data/posts.csv \
  --output /protected/outputs/summary.csv \
  --validation-report /protected/outputs/validation.json
```

The clean environment may use the same Docker image if institutional rules permit it:

``` bash
# clean environment
docker compose run --rm dirty-dev python -m src.analyze_posts \
  --input /protected/data/posts.csv \
  --output /protected/outputs/summary.csv \
  --validation-report /protected/outputs/validation.json
```

If Docker is used on the clean side, do not install or run the coding agent there. The clean side is for execution and validation, not for agentic debugging.

## Safe Debugging Feedback Loop

Real-data analyses often fail in ways that mock data did not anticipate. The response should not be to paste raw errors, rows, screenshots, or tables into the agent.

Use this loop instead:

1.  Run the analysis in the clean environment.
2.  If it fails, create a sanitized structural error report.
3.  Remove real text, IDs, usernames, URLs, paths, file names, timestamps, exact values, and other identifying details.
4.  Add a mock fixture in the dirty environment that reproduces the structural issue.
5.  Ask the agent to fix the code using the mock fixture only.
6.  Review the change.
7.  Push reviewed code through Git.
8.  Rerun on the clean environment.

The template `templates/safe-debugging-report.md` provides a reusable structure.

## Validation Protocol

Validation must test more than whether the code runs.

At minimum, validate:

- Required columns and expected types.
- Row counts before and after each transformation.
- Duplicate IDs.
- Missingness patterns.
- Unit of analysis, such as post-level, user-level, or comment-level.
- Join keys and row retention after joins.
- Train/test separation if predictive modeling is used.
- Distribution checks for key variables.
- Label frequencies and unexpected labels.
- Model input and output dimensions.
- Final tables and figures against source outputs.

Run the included repository check:

``` bash
# dirty environment
python validation/check_repository.py
```

Treat agent-generated tests as helpful but insufficient. A human researcher should independently review core transformations and final outputs. For high-risk projects, ask a collaborator to reproduce key outputs without the coding agent.

## Transparency and Disclosure

A manuscript can disclose the workflow without exposing sensitive prompts or data. A short disclosure might say:

> We used AI coding agents for code drafting, refactoring, documentation, and mock-data debugging in an agent-safe development environment. The agents did not have access to the protected research data, real-data outputs, credentials, or unsanitized logs. Real-data analyses were executed in a separate protected environment without AI coding-agent access. We validated the code through mock-data tests, clean-environment execution checks, and human review of core transformations and final outputs.

A reviewer-facing statement can add:

> The repository contains mock data, validation scripts, an `.gitignore`, and `AGENT_RULES.md`. Real data and protected outputs were stored outside the repository and outside the agent-accessible environment. Sanitized debugging reports were used when real-data execution revealed issues.

See `templates/ai-use-disclosure.md`, `templates/reviewer-explanation.md`, and `templates/validation-checklist.md`.

## Exercises

### Exercise 1: Classify Files

Classify each item as agent-safe or protected:

- `src/analyze_posts.py`
- `mock-data/posts.csv`
- `/protected/data/posts.csv`
- `outputs/mock-summary.csv`
- `/protected/outputs/summary.csv`
- `.env`
- `templates/safe-debugging-report.md`
- `logs/real-run-error.log`

### Exercise 2: Audit `.gitignore`

Open `.gitignore` and check whether it blocks:

- Real data.
- Outputs.
- Logs.
- Credentials.
- Notebook checkpoints.
- Temporary files.
- Local environment metadata.

### Exercise 3: Review Agent Rules

Read `AGENT_RULES.md` and identify which rules protect privacy, which protect provenance, and which protect methodological validity.

### Exercise 4: Sanitize a Debugging Report

Use `templates/safe-debugging-report.md` to turn a hypothetical real-data failure into a structural report that does not reveal real text, IDs, names, paths, timestamps, or values.

### Exercise 5: Draft a Disclosure

Use `templates/ai-use-disclosure.md` to draft a manuscript disclosure statement for a project that used an AI coding agent only in the dirty environment.

## Conclusion

This workflow does not make AI coding agents harmless. It makes their use more bounded, inspectable, and reviewable.

The main norm is:

> Use agents to help develop code on mock data. Do not let agents see protected data. Do not let agents directly produce evidence. Validate before making claims.

The two-environment architecture strongly mitigates privacy and containment risks. It only partly mitigates validity risks. Those still require researcher judgment, independent checks, transparent disclosure, and careful peer review.

## References

The tutorial structure follows the public Methods Hub tutorial guidance and template [@gesis_methods_hub_guidelines; @gesis_methods_hub].