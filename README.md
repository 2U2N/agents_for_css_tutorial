# Keeping Midas in the Sandbox

This repository is a draft GESIS Methods Hub-style tutorial on using AI coding agents responsibly with sensitive research data.

The tutorial explains a three-part workflow:

> Docker Sandboxes keep Midas, the coding agent, in a safe project directory. GitHub carries reviewed code across the bridge. The vault directory keeps real data and protected outputs away from the agent.

## Contents

- `index.md`: tutorial source.
- `AGENT_RULES.md`: project rules for agent-visible work.
- `.gitignore`: safety net for data, outputs, logs, credentials, caches, and local files.
- `docs/local-vm-appendix.md`: fallback notes for separating Midas and vault work on one device.
- `references.bib`: bibliography for the tutorial.
- `binder/`: Methods Hub rendering support.
- `notes.md`: drafting notes, kept separate from the article source.

## Current Scope

This is an article repository, not a reusable project template and not a runnable analysis package. The reusable template will be designed later after the tutorial argument is solid.

The current tutorial teaches the separation architecture. A future extension will explain how to communicate the shape of vault data to Midas without revealing raw rows, exact values, identifiers, text, timestamps, file paths, or real output snippets.

## Safety Notice

Do not place real data, credentials, private logs, protected outputs, screenshots, notebooks with real observations, or unsanitized error reports in this repository.

## Rendering

If Quarto is available, render the tutorial with:

```bash
quarto render index.md
```

## License

This project is released under the MIT License.
