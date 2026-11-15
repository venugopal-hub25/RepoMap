
import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from repomap.cli import main


class TestCLI(unittest.TestCase):

    def test_handles_output_permission_error(self):
        with tempfile.TemporaryDirectory() as temp:
            output_path = Path(temp) / "structure.txt"
            error_output = io.StringIO()

            arguments = [
                "repomap",
                temp,
                "--output",
                str(output_path),
            ]

            with patch("sys.argv", arguments):
                with patch(
                    "repomap.cli.save_tree",
                    side_effect=PermissionError("Permission denied"),
                ):
                    with redirect_stderr(error_output):
                        with self.assertRaises(SystemExit) as error:
                            main()

            self.assertEqual(error.exception.code, 2)
            self.assertIn("Permission denied", error_output.getvalue())

    def test_handles_missing_output_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            output_path = Path(temp) / "missing" / "structure.txt"
            error_output = io.StringIO()

            arguments = [
                "repomap",
                temp,
                "--output",
                str(output_path),
            ]

            with patch("sys.argv", arguments):
                with redirect_stderr(error_output):
                    with self.assertRaises(SystemExit) as error:
                        main()

            self.assertEqual(error.exception.code, 2)
            self.assertIn(
                "No such file or directory",
                error_output.getvalue(),
            )

    def test_handles_output_path_that_is_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            output_path = Path(temp) / "existing_folder"
            output_path.mkdir()

            error_output = io.StringIO()

            arguments = [
                "repomap",
                temp,
                "--output",
                str(output_path),
            ]

            with patch("sys.argv", arguments):
                with redirect_stderr(error_output):
                    with self.assertRaises(SystemExit) as error:
                        main()

            self.assertEqual(error.exception.code, 2)
            self.assertIn("Is a directory", error_output.getvalue())

    def test_refuses_to_overwrite_existing_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "project"
            root.mkdir()
            (root / "main.py").touch()

            output_path = Path(temp) / "structure.txt"
            output_path.write_text("Original content", encoding="utf-8")

            error_output = io.StringIO()

            arguments = [
                "repomap",
                str(root),
                "--output",
                str(output_path),
            ]

            with patch("sys.argv", arguments):
                with redirect_stderr(error_output):
                    with self.assertRaises(SystemExit) as error:
                        main()

            self.assertEqual(error.exception.code, 2)
            self.assertEqual(
                output_path.read_text(encoding="utf-8"),
                "Original content",
            )
            self.assertIn("--force", error_output.getvalue())

    def test_force_overwrites_existing_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "project"
            root.mkdir()
            (root / "main.py").touch()

            output_path = Path(temp) / "structure.txt"
            output_path.write_text(
                "Original content",
                encoding="utf-8",
            )

            arguments = [
                "repomap",
                str(root),
                "--output",
                str(output_path),
                "--force",
            ]

            with patch("sys.argv", arguments):
                with redirect_stdout(io.StringIO()):
                    main()

            saved_content = output_path.read_text(encoding="utf-8")

            self.assertIn("project/", saved_content)
            self.assertIn("main.py", saved_content)
            self.assertNotIn("Original content", saved_content)

    def test_refuses_to_overwrite_existing_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "project"
            root.mkdir()
            (root / "main.py").touch()

            output_path = Path(temp) / "structure.txt"
            output_path.write_text(
                "Original content",
                encoding="utf-8",
            )

            error_output = io.StringIO()

            arguments = [
                "repomap",
                str(root),
                "--output",
                str(output_path),
            ]

            with patch("sys.argv", arguments):
                with redirect_stderr(error_output):
                    with self.assertRaises(SystemExit) as error:
                        main()

            self.assertEqual(error.exception.code, 2)
            self.assertEqual(
                output_path.read_text(encoding="utf-8"),
                "Original content",
            )
            self.assertIn("--force", error_output.getvalue())

if __name__ == "__main__":
    unittest.main()
