import tempfile
import unittest
from pathlib import Path
from unittest import mock

from librarian_core.integrations import filesystem_duplicate_candidates, qmd_duplicate_candidates


class IntegrationTests(unittest.TestCase):
    def test_filesystem_duplicate_candidate(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "archive").mkdir()
            (root / "archive/dgx-spark.md").write_text("# DGX Spark\n")
            candidates = filesystem_duplicate_candidates(root, Path("notes/dgx_spark.md"))
            self.assertIn("archive/dgx-spark.md", candidates)

    @mock.patch("librarian_core.integrations.qmd_available", return_value=False)
    def test_qmd_absence_is_graceful(self, _):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.assertEqual(qmd_duplicate_candidates(root, Path("note.md"), "Note"), [])


if __name__ == "__main__":
    unittest.main()
