
import argparse
from pathlib import Path

from repomap.scanner import scan_directory


def main():
    parser = argparse.ArgumentParser(
        description="RepoMap - Understand your codebase structure."
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repository to scan."
    )

    args = parser.parse_args()

    root = Path(args.path)

    try:
        files = scan_directory(root)

        print(f"\nRepoMap scanned: {root.resolve()}")
        print(f"Total files found: {len(files)}\n")

        for file in files:
            print(file.relative_to(root.resolve()))

    except (FileNotFoundError, NotADirectoryError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
