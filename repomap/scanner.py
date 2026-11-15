
import os
from pathlib import Path


IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
}


def scan_directory(
    root: Path,
    max_depth: int | None = None,
    ignore_dirs: set[str] | None = None,
) -> list[Path]:
    """Scan a directory and return its files, excluding ignored folders."""
    if max_depth is not None and max_depth < 1:
        raise ValueError("max_depth must be a positive integer.")
    custom_ignored_dirs = ignore_dirs or set()
    ignored_dirs = IGNORED_DIRS | custom_ignored_dirs

    root = root.resolve()

    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    files = []

    for current_dir, dirnames, filenames in os.walk(root):
        current_path = Path(current_dir)
        current_depth = len(current_path.relative_to(root).parts)

        if max_depth is not None and current_depth >= max_depth - 1:
            dirnames.clear()
        dirnames[:] = sorted(
            name for name in dirnames
            if (
                name not in ignored_dirs
                and not name.startswith(".")
                and not name.endswith(".egg-info")
            )
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

    
