"""Small mock-data analysis used by the tutorial.

The script validates a CSV of platform posts and writes aggregate summaries.
It is intentionally simple and uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


REQUIRED_COLUMNS = {
    "post_id",
    "user_id",
    "platform",
    "language",
    "created_at",
    "text",
    "label",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze mock communication data.")
    parser.add_argument("--input", required=True, help="Input CSV path.")
    parser.add_argument("--output", required=True, help="Output summary CSV path.")
    parser.add_argument(
        "--validation-report",
        required=True,
        help="Output validation JSON path.",
    )
    return parser.parse_args()


def read_posts(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("Input CSV has no header row.")
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            raise ValueError(f"Input CSV is missing required columns: {sorted(missing)}")
        return list(reader)


def validate_posts(rows: list[dict[str, str]]) -> dict[str, object]:
    post_ids = [row["post_id"] for row in rows]
    duplicate_ids = sorted(
        post_id for post_id, count in Counter(post_ids).items() if count > 1
    )
    missing_required_values = {
        column: sum(1 for row in rows if not row.get(column, "").strip())
        for column in REQUIRED_COLUMNS
    }
    invalid_timestamps = [
        row["post_id"]
        for row in rows
        if not _is_iso_timestamp(row.get("created_at", ""))
    ]
    labels = Counter(row["label"] for row in rows)
    languages = Counter(row["language"] for row in rows)
    platforms = Counter(row["platform"] for row in rows)

    return {
        "row_count": len(rows),
        "unique_post_ids": len(set(post_ids)),
        "duplicate_post_ids": duplicate_ids,
        "missing_required_values": missing_required_values,
        "invalid_timestamps": invalid_timestamps,
        "labels": dict(sorted(labels.items())),
        "languages": dict(sorted(languages.items())),
        "platforms": dict(sorted(platforms.items())),
        "passed": not duplicate_ids
        and not invalid_timestamps
        and all(count == 0 for count in missing_required_values.values()),
    }


def write_summary(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter((row["platform"], row["language"], row["label"]) for row in rows)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["platform", "language", "label", "n_posts"],
        )
        writer.writeheader()
        for (platform, language, label), count in sorted(counts.items()):
            writer.writerow(
                {
                    "platform": platform,
                    "language": language,
                    "label": label,
                    "n_posts": count,
                }
            )


def write_validation_report(report: dict[str, object], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")


def _is_iso_timestamp(value: str) -> bool:
    if not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def main() -> int:
    args = parse_args()
    rows = read_posts(Path(args.input))
    report = validate_posts(rows)
    write_summary(rows, Path(args.output))
    write_validation_report(report, Path(args.validation_report))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
