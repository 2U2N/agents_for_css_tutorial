"""Check that the tutorial repository contains basic safety files."""

from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "index.md",
    ".gitignore",
    "AGENT_RULES.md",
    "Dockerfile",
    "docker-compose.yml",
    "mock-data/posts.csv",
    "templates/ai-use-disclosure.md",
    "templates/validation-checklist.md",
    "templates/safe-debugging-report.md",
    "templates/reviewer-explanation.md",
]

REQUIRED_GITIGNORE_PATTERNS = [
    "data/",
    "outputs/",
    "logs/",
    ".env",
    ".ipynb_checkpoints/",
    "*.key",
    "*.pem",
]


def main() -> int:
    root = Path.cwd()
    missing_files = [path for path in REQUIRED_FILES if not (root / path).exists()]
    gitignore_text = (root / ".gitignore").read_text(encoding="utf-8")
    missing_patterns = [
        pattern for pattern in REQUIRED_GITIGNORE_PATTERNS if pattern not in gitignore_text
    ]

    if missing_files:
        print("Missing required files:")
        for path in missing_files:
            print(f"- {path}")
    if missing_patterns:
        print("Missing .gitignore patterns:")
        for pattern in missing_patterns:
            print(f"- {pattern}")

    if missing_files or missing_patterns:
        return 1

    print("Repository safety check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
