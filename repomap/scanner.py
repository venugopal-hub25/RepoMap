
import os
from pathlib import Path


IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
}


def scan_directory(root: Path) -> list[Path]:
    """Scan a directory and return its files, excluding ignored folders."""

    root = root.resolve()

    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    files = []

    for current_dir, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            name for name in dirnames
            if name not in IGNORED_DIRS and not name.startswith(".")
        )

        for filename in sorted(filenames):
            if filename == ".env" or filename.startswith(".env."):
                continue

            file_path = Path(current_dir) / filename

            if not file_path.is_symlink():
                files.append(file_path)

    return sorted(
        files,
        key=lambda path: path.relative_to(root).as_posix().lower()
    )

    
