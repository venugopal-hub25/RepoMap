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

    def test_max_depth_one(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()
            (root / "src").mkdir()
            (root / "src" / "app.py").touch()

            files = scan_directory(root, max_depth=1)
            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertNotIn("app.py", names)

    def test_max_depth_two(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()
            (root / "src").mkdir()
            (root / "src" / "app.py").touch()
            (root / "src" / "nested").mkdir()
            (root / "src" / "nested" / "deep.py").touch()

            files = scan_directory(root, max_depth=2)
            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertIn("app.py", names)
            self.assertNotIn("deep.py", names)

    def test_rejects_zero_max_depth(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            with self.assertRaises(ValueError):
                scan_directory(root, max_depth=0)

    def test_rejects_negative_max_depth(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            with self.assertRaises(ValueError):
                scan_directory(root, max_depth=-1)

    def test_raises_error_for_nonexistent_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "missing"

            with self.assertRaises(FileNotFoundError):
                scan_directory(root)

    def test_raises_error_for_file_instead_of_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            file_path = root / "README.md"
            file_path.touch()

            with self.assertRaises(NotADirectoryError):
                scan_directory(file_path)

    def test_ignores_egg_info_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()
            egg_info = root / "sample.egg-info"
            egg_info.mkdir()
            (egg_info / "PKG-INFO").touch()

            files = scan_directory(root)
            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertNotIn("PKG-INFO", names)

    def test_ignores_custom_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()
            (root / "build").mkdir()
            (root / "build" / "output.py").touch()

            files = scan_directory(root, ignore_dirs={"build"})
            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertNotIn("output.py", names)

    def test_ignores_multiple_custom_directories(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").touch()

            for directory in ("build", "dist", "logs"):
                folder = root / directory
                folder.mkdir()
                (folder / "ignored.py").touch()

            files = scan_directory(
                root,
                ignore_dirs={"build", "dist", "logs"},
            )

            names = {file.name for file in files}

            self.assertIn("main.py", names)
            self.assertNotIn("ignored.py", names)

if __name__ == "__main__":
    unittest.main()
