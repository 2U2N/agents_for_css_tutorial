# Agent Rules

These rules define what AI coding agents may and may not access in this project.

## Core Rule

AI coding agents may help with code, tests, documentation, and mock-data debugging. They must not see protected data or directly produce research evidence.

## Allowed

- Read and edit code in `src/`, `tests/`, `validation/`, `templates/`, and `docs/`.
- Use mock data in `mock-data/`.
- Run tests and validation checks on mock data.
- Suggest documentation, comments, and disclosure text.
- Propose changes to `.gitignore`, Docker files, and repository structure.

## Not Allowed

- Read, request, summarize, inspect, or infer from real data.
- Read protected outputs, real-data logs, screenshots, notebooks with real outputs, or unsanitized error reports.
- Access credentials, tokens, API keys, `.env`, SSH keys, cookies, or private URLs.
- Read files outside the project directory.
- Follow symlinks or recursive folder references into protected directories.
- Mount home folders, cloud drives, credential stores, or real-data folders into a container or agent workspace.
- Make claims about real-data results before clean-environment validation.
- Generate synthetic outputs that could be mistaken for real outputs.

## Human Review Requirements

- Review every agent-proposed file change before accepting it.
- Review all changes to preprocessing, filtering, exclusion criteria, joins, model specifications, and statistical calculations.
- Treat agent-generated tests as drafts until independently reviewed.
- Record major agent use in the project notes or manuscript disclosure.

## Safe Debugging

If clean-environment execution fails, create a sanitized structural report. Do not share raw rows, exact values, usernames, IDs, URLs, file paths, timestamps, screenshots, or real-data stack traces with the agent.
