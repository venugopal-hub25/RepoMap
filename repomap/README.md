# RepoMap

**Understand your codebase structure.**

RepoMap is a lightweight Python command-line tool that scans a repository and displays its directory structure as a readable tree.

It helps developers quickly understand how files and folders are organised inside a project.

## Features

- Recursively scans project directories.
- Displays files in a visual directory-tree format.
- Ignores common unnecessary directories such as `.git`, `.venv`, `venv`, `__pycache__`, and `node_modules`.
- Excludes `.env` files.
- Skips symbolic links.
- Supports scanning a specified directory.
- Includes automated unit tests.

## Project Structure

```text
RepoMap/
├── repomap/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── scanner.py
│   └── tree.py
└── tests/
    ├── test_scanner.py
    └── test_tree.py
```

## Requirements

- Python 3.9 or later
- Git (for cloning the repository)

## Installation

Clone the repository:

```bash
git clone https://github.com/venugopal-hub25/RepoMap.git
```

Navigate into the project:

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

## Usage

Run RepoMap from the project directory:

```bash
python -m repomap
```

Scan a specific directory:

```bash
python -m repomap /path/to/project
```

Display available command-line options:

```bash
python -m repomap --help
```

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

## Running Tests

Run the automated test suite:

```bash
python -m unittest discover -s tests -v
```

The current test suite contains six tests covering directory scanning, ignored files, symbolic links, and tree rendering.

## Technologies Used

- Python
- pathlib
- os
- argparse
- unittest
- Git and GitHub

## Project Status

RepoMap is an actively developed project. Core directory scanning, tree rendering, CLI integration, and initial automated tests are implemented.

## Author

**Venugopal J.**

GitHub: [@venugopal-hub25](https://github.com/venugopal-hub25)