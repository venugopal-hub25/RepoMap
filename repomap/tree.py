
from pathlib import Path


def render_tree(root: Path, files: list[Path]) -> str:
    """Convert a list of file paths into a visual directory tree."""

    root = root.resolve()
    tree = {}

    # Build a nested structure from file paths.
    for file in files:
        relative_path = file.relative_to(root)
        current = tree

        for part in relative_path.parts:
            current = current.setdefault(part, {})

    # Convert the nested structure into tree text.
    lines = [f"{root.name}/"]

    def draw_branch(branch, prefix=""):
        entries = sorted(branch.items())

        for index, (name, children) in enumerate(entries):
            is_last = index == len(entries) - 1

            connector = "└── " if is_last else "├── "
            display_name = name + "/" if children else name
            lines.append(prefix + connector + display_name)

            if children:
                extension = "    " if is_last else "│   "
                draw_branch(children, prefix + extension)

    draw_branch(tree)

    return "\n".join(lines)
