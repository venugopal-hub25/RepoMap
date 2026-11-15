# RepoMap

**Understand your codebase structure.**

RepoMap is a lightweight Python command-line tool that scans a project directory and visualizes its structure as a readable directory tree.

It helps developers quickly explore unfamiliar codebases, understand how files and folders are organized, and identify the overall project layout.

## Features

- **Recursive directory scanning** — explores project directories and their files.
- **Visual directory tree** — displays the project structure in a clean, readable format.
- **Smart directory filtering** — ignores common directories such as `.git`, `.venv`, `venv`, `__pycache__`, and `node_modules`.
- **Environment file protection** — excludes `.env` and `.env.*` files from scan results.
- **Symbolic link handling** — skips symbolic links.
- **Custom scan path** — scan the current directory or specify another project directory.
- **Depth control** — limit how deep RepoMap scans into a directory structure.
- **Automated tests** — includes unit tests for scanning and tree rendering.

## Example Output

```text
my-project/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
└── README.md
```

## Requirements

- Python 3.10 or later
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/venugopal-hub25/RepoMap.git
```

Navigate into the project directory:

```bash
cd RepoMap
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

Install RepoMap in editable mode:

```bash
python -m pip install -e .
```

## Usage

### Scan the current directory

```bash
repomap
```

You can also run it as a Python module:

```bash
python -m repomap
```

### Scan a specific directory

```bash
repomap /path/to/project
```

### Limit directory depth

Use `--max-depth` to control how deeply RepoMap scans.

```bash
repomap . --max-depth 2
```

### Display available options

```bash
repomap --help
```

## Project Structure

```text
RepoMap/
├── repomap/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── scanner.py
│   └── tree.py
├── tests/
│   ├── test_scanner.py
│   └── test_tree.py
├── README.md
├── .gitignore
└── pyproject.toml
```

## Running Tests

Run the unit test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The current test suite includes tests for directory scanning, ignored files and directories, symbolic links, maximum scan depth, and tree rendering.

## Technologies Used

- Python
- pathlib
- os
- argparse
- unittest
- Git and GitHub

## Project Status

RepoMap is actively under development. Its core directory scanning, tree rendering, command-line interface, package configuration, depth control, and initial automated tests are implemented.

More improvements and features are planned.

## Author

**Venugopal J.**

GitHub: [@venugopal-hub25](https://github.com/venugopal-hub25)
