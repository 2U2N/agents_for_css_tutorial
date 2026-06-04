from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from src.analyze_posts import read_posts, validate_posts, write_summary


class AnalyzePostsTest(unittest.TestCase):
    def test_valid_mock_data_passes_validation(self) -> None:
        rows = read_posts(Path("mock-data/posts.csv"))
        report = validate_posts(rows)

        self.assertTrue(report["passed"])
        self.assertEqual(report["row_count"], 8)
        self.assertEqual(report["duplicate_post_ids"], [])
        self.assertEqual(report["invalid_timestamps"], [])

    def test_duplicate_post_ids_fail_validation(self) -> None:
        rows = [
            {
                "post_id": "duplicate",
                "user_id": "mock-user-1",
                "platform": "ExampleNet",
                "language": "en",
                "created_at": "2026-01-05T10:00:00Z",
                "text": "Fake text.",
                "label": "neutral",
            },
            {
                "post_id": "duplicate",
                "user_id": "mock-user-2",
                "platform": "ExampleNet",
                "language": "en",
                "created_at": "2026-01-05T10:01:00Z",
                "text": "Different fake text.",
                "label": "neutral",
            },
        ]

        report = validate_posts(rows)

        self.assertFalse(report["passed"])
        self.assertEqual(report["duplicate_post_ids"], ["duplicate"])

    def test_summary_writes_aggregate_counts_without_text(self) -> None:
        rows = read_posts(Path("mock-data/posts.csv"))
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "summary.csv"
            write_summary(rows, output)
            with output.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                fieldnames = reader.fieldnames
                summary_rows = list(reader)

        self.assertEqual(fieldnames, ["platform", "language", "label", "n_posts"])
        self.assertGreater(len(summary_rows), 0)
        self.assertNotIn("text", fieldnames or [])


if __name__ == "__main__":
    unittest.main()
