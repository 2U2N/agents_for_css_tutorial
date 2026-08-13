# Keeping Midas in the Sandbox

This repository contains a GESIS Methods Hub-style tutorial on using AI coding agents responsibly with sensitive research data.

The tutorial explains a three-part workflow:

> Docker Sandboxes keep Midas, the coding agent, in a safe project directory. GitHub carries reviewed code across the bridge. The vault directory keeps real data and protected outputs away from the agent.

## Contents

- `index.md`: tutorial source.
- `Coding_Agent_Tutorial.bib`: references cited by the tutorial.
- `CITATION.cff`: citation metadata for the repository.
- `LICENSE`: MIT license for the tutorial.
- `binder/`: Methods Hub rendering support.
- `.gitignore`: safety net for data, outputs, logs, credentials, caches, and generated files.

## Scope

This tutorial explains the separation architecture, the use of sanitized data-shape descriptions, and the development and review of analysis code using fictional mock data.

The reusable project files and vault-side data-shape reporting tools are maintained separately in the [`2U2N/midas_template`](https://github.com/2U2N/midas_template) repository.

## License

This project is released under the MIT License.
