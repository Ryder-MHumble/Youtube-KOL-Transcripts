from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEARCH = ROOT / "skills/kol-quote-research/scripts/search_transcripts.py"


class SearchTranscriptTests(unittest.TestCase):
    def search(self, query: str, *extra: str) -> list[dict]:
        result = subprocess.run(
            [sys.executable, str(SEARCH), query, "--json", "--limit", "8", *extra],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(result.stdout)

    def test_finds_ilya_research_view(self) -> None:
        results = self.search("age of scaling age of research generalization")
        self.assertTrue(results)
        self.assertTrue(any("Ilya Sutskever" in item["title"] for item in results))
        self.assertTrue(all(item["timestamp_url"].startswith("https://www.youtube.com/") for item in results))

    def test_person_filter(self) -> None:
        results = self.search("agents coding software", "--person", "Andrej Karpathy")
        self.assertTrue(results)
        self.assertTrue(all("Andrej Karpathy" in item["featured_people"] for item in results))

    def test_returns_exact_source_path_and_timestamp(self) -> None:
        results = self.search("token costs enterprise")
        self.assertTrue(results)
        top = results[0]
        self.assertIn("path", top)
        self.assertIn("quote", top)
        self.assertIn("timestamp", top)
        self.assertIn("t=", top["timestamp_url"])


if __name__ == "__main__":
    unittest.main()
