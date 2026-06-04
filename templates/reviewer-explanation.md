# Reviewer Explanation Template

This project followed an agent-assisted code development and agent-free protected analysis workflow.

## Summary

AI coding agents were used only in an agent-safe development environment containing code, mock data, tests, documentation, and templates. The agents did not have access to protected research data, real-data outputs, credentials, unsanitized logs, screenshots, or notebooks containing real observations.

## Workflow Evidence

- The repository contains `AGENT_RULES.md`.
- The repository contains mock data only.
- Real data were stored outside the Git repository.
- Real-data analysis was run in a separate clean environment without AI coding-agent access.
- `.gitignore` blocks data, outputs, logs, credentials, caches, and notebook checkpoints.
- Safe debugging used sanitized structural reports rather than raw real-data examples.

## Validation Evidence

- Mock-data tests were run before real-data execution.
- Real-data execution was validated in the clean environment.
- Core transformations and final outputs were reviewed by human researchers.
- Agent-generated tests or explanations were not treated as independent verification.

## Limits

This workflow reduces privacy and containment risks. It does not eliminate the possibility of coding errors, flawed methodological choices, or incomplete validation. Human authors remain responsible for all research claims.
