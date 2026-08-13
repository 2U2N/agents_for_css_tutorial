# Agent Rules

These rules define what AI coding agents may and may not access in this article project.

## Core Rule

AI coding agents may help with article text, safe documentation, project structure, and non-sensitive workflow examples. They must not see protected data or directly produce research evidence.

## Allowed

- Read and edit `index.md`, `README.md`, `AGENT_RULES.md`, `.gitignore`, `docs/`, Binder rendering files, and bibliography/citation metadata.
- Suggest article text, disclosure language, exercises, and reviewer-facing explanations.
- Propose changes to repository structure and safety documentation.
- Search this repository for stale references to removed template or runtime material.

## Not Allowed

- Read, request, summarize, inspect, or infer from real data.
- Read protected outputs, real-data logs, screenshots, notebooks with real outputs, or unsanitized error reports.
- Access credentials, tokens, API keys, `.env`, SSH keys, cookies, or private URLs.
- Read files outside the project directory.
- Follow symlinks or recursive folder references into protected directories.
- Mount home folders, cloud drives, credential stores, or real-data folders into the Midas directory or agent workspace.
- Make claims about real-data results before vault validation.
- Generate synthetic outputs that could be mistaken for real outputs.

## Human Review Requirements

- Review every agent-proposed file change before accepting it.
- Review all article claims about Docker Sandboxes, GitHub, privacy, validity, and reproducibility.
- Treat agent-generated workflow guidance as a draft until independently reviewed.
- Record major agent use in the project notes or manuscript disclosure.

## Safe Debugging

If vault execution fails, create a sanitized structural report. Do not share raw rows, exact values, usernames, IDs, URLs, file paths, timestamps, screenshots, or real-data stack traces with the agent.
