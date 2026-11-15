import tempfile
import unittest
from pathlib import Path

from repomap.scanner import scan_directory


class TestScanner(unittest.TestCase):

    def test_finds_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").write_text("print('Hello')")
            (root / "README.md").write_text("# RepoMap")

            files = scan_directory(root)

            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertIn("README.md", names)

    def test_ignores_virtual_environment(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()
            (root / ".venv").mkdir()
            (root / ".venv" / "ignored.py").touch()

            files = scan_directory(root)

            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertNotIn("ignored.py", names)
        
    def test_ignores_env_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()
            (root / ".env").touch()

            files = scan_directory(root)
            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertNotIn(".env", names)

    def test_ignores_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            target = root / "target.py"
            target.touch()

            link = root / "linked.py"

            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("Symbolic links are not supported")

            files = scan_directory(root)
            names = {file.name for file in files}

            self.assertIn("target.py", names)
            self.assertNotIn("linked.py", names)

if __name__ == "__main__":
    unittest.main()
