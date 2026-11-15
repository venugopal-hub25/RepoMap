
import argparse
from pathlib import Path

from repomap.scanner import scan_directory
from repomap.tree import render_tree, save_tree


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RepoMap - Understand your codebase structure."
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repository to scan.",
    )

    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum directory depth to scan.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Save the directory tree to a text file.",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )

    parser.add_argument(
        "--ignore",
        nargs="+",
        default=[],
        metavar="DIR",
        help="Additional directory names to ignore.",
    )

    args = parser.parse_args()
    root = Path(args.path)

    try:
        files = scan_directory(
            root,
            max_depth=args.max_depth,
            ignore_dirs=set(args.ignore),
        )

        # Exclude the output file from the generated directory tree.
        if args.output is not None:
            output_path = args.output.resolve()

            files = [
                file for file in files
                if file.resolve() != output_path
            ]

        print(f"\nRepoMap scanned: {root.resolve()}")
        print(f"Total files found: {len(files)}\n")

        tree = render_tree(root, files)
        print(tree)

        if args.output is not None:
            if args.output.is_file() and not args.force:
                raise FileExistsError(
                    f"Output file already exists: {args.output}. "
                    "Use --force to overwrite."
                )

            save_tree(tree, args.output)
            print(f"\nDirectory tree saved to: {args.output}")

    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
