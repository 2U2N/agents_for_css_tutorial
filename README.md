# Agent-Assisted Code, Agent-Free Analysis

This repository is a draft GESIS Methods Hub-style tutorial on using AI coding agents responsibly with sensitive research data.

The core workflow is:

> Agent-assisted code development, agent-free protected analysis.

The repository contains only mock data and template materials. It is designed to teach a two-environment workflow:

- A dirty agent environment for coding, testing, documentation, Docker, and mock data.
- A clean protected environment for real data, real outputs, and final validation without AI coding-agent access.

## Contents

- `index.md`: tutorial source.
- `AGENT_RULES.md`: project rules for coding-agent use.
- `Dockerfile` and `docker-compose.yml`: local mock-data development environment.
- `mock-data/posts.csv`: fake communication data.
- `src/analyze_posts.py`: runnable example analysis.
- `tests/`: standard-library unit tests.
- `validation/check_repository.py`: repository safety check.
- `templates/`: disclosure, validation, reviewer, and debugging templates.
- `docs/local-vm-appendix.md`: fallback setup using two local VMs.

## Quick Start

Run the mock-data analysis:

```bash
docker compose run --rm dirty-dev python -m src.analyze_posts \
  --input mock-data/posts.csv \
  --output outputs/mock-summary.csv \
  --validation-report outputs/mock-validation.json
```

Run tests:

```bash
docker compose run --rm dirty-dev python -m unittest discover -s tests
```

Run repository checks:

```bash
python validation/check_repository.py
```

## Safety Notice

Do not place real data, credentials, private logs, protected outputs, or unsanitized error reports in this repository. Use the repository only for code, mock data, tests, documentation, and templates.

## License

This project is released under the MIT License.
