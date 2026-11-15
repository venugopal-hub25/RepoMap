# RepoMap

**Understand your codebase structure.**

RepoMap is a lightweight Python command-line tool that scans a project directory and visualizes its structure as a readable directory tree.

It helps developers quickly explore unfamiliar codebases, understand how files and folders are organized, and identify the overall project layout.

## Features

- **Recursive directory scanning** — explores project directories and their files.
- **Visual directory tree** — displays the project structure in a clean, readable format.
- **Smart directory filtering** — ignores common directories such as `.git`, `.venv`, `venv`, `__pycache__`, `node_modules`, and Python `.egg-info` metadata directories.
- **Environment file protection** — excludes `.env` and `.env.*` files from scan results.
- **Symbolic link handling** — skips symbolic links.
- **Custom scan path** — scan the current directory or specify another project directory.
- **Depth control** — limit how deeply RepoMap scans into a directory structure.
- **Custom exclusions** — specify additional directory names to ignore.
- **Tree export** — save the generated directory tree to a UTF-8 text file.
- **Automated tests** — includes tests for scanning, filtering, tree rendering, and exporting.

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

### 1. Scan the current directory

```bash
repomap
```

You can also run RepoMap as a Python module:

```bash
python -m repomap
```

### 2. Scan a specific directory

```bash
repomap /path/to/project
```

### 3. Limit directory depth

Use `--max-depth` to control how deeply RepoMap scans.

```bash
repomap . --max-depth 2
```

### 4. Export the directory tree

Use `--output` to save the generated directory tree to a text file.

```bash
repomap . --output structure.txt
```

The tree is displayed in the terminal and saved to the specified file.

### 5. Ignore additional directories

Use `--ignore` followed by one or more directory names.

```bash
repomap . --ignore build dist logs
```

Custom exclusions are added to RepoMap's built-in ignored directories.

### 6. Combine multiple options

RepoMap allows multiple options to be used together.

```bash
repomap . --max-depth 2 --ignore build dist --output structure.txt
```

### 7. Display available options

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

Run the automated test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The test suite covers directory scanning, built-in and custom exclusions, environment files, symbolic links, maximum scan depth, invalid paths, tree rendering, and UTF-8 text export.

## Technologies Used

- Python
- pathlib
- os
- argparse
- unittest
- Git and GitHub

## Project Status

RepoMap is actively under development. Its core directory scanning, tree rendering, command-line interface, package configuration, depth control, custom directory exclusions, text-file export, and automated tests are implemented.

More improvements and features are planned.

## Author

**Venugopal J.**

GitHub: [@venugopal-hub25](https://github.com/venugopal-hub25)
