
import tempfile
import unittest
from pathlib import Path

from repomap.tree import render_tree, save_tree


class TestTreeRenderer(unittest.TestCase):

    def test_renders_directory_tree(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "repomap").mkdir()
            (root / "repomap" / "scanner.py").touch()
            (root / "README.md").touch()

            files = [
                root / "repomap" / "scanner.py",
                root / "README.md",
            ]

            result = render_tree(root, files)

            self.assertIn("repomap/", result)
            self.assertIn("scanner.py", result)
            self.assertIn("README.md", result)
            self.assertIn("├──", result)

    def test_renders_empty_tree(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            result = render_tree(root, [])

            self.assertEqual(result, f"{root.name}/")

    def test_saves_tree_to_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            output_file = root / "structure.txt"
            tree = "my-project/\n├── main.py"

            save_tree(tree, output_file)

            saved_content = output_file.read_text(encoding="utf-8")

            self.assertEqual(saved_content, tree)

    def test_saves_unicode_tree_correctly(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output_file = root / "tree.txt"

            tree = "RepoMap/\n└── main.py"

            save_tree(tree, output_file)

            saved_content = output_file.read_text(encoding="utf-8")

            self.assertEqual(saved_content, tree)
if __name__ == "__main__":
    unittest.main()
