# ANSWERS_24_python_modules.md

## Python Modules — Complete Answer Guide

---

## What is a Module?

A module is a Python file that provides functions and variables you can import.
Python's standard library has hundreds of built-in modules.

In the Gamertags project, we use the `os` module.

---

## Importing Modules

```python
# Import the whole module
import os

# Use its functions with module prefix
os.system("cls")
os.path.abspath(__file__)

# Import specific function
from os.path import abspath, dirname, join

# Use without prefix
abspath(__file__)

# Import with alias
import os.path as osp
osp.join("/home", "gamertags.txt")
```

---

## The `os` Module — Used in This Project

```python
import os

# Operating system name
os.name           # "nt" = Windows, "posix" = Mac/Linux

# Run a shell command
os.system("cls")          # Clear screen on Windows
os.system("clear")        # Clear screen on Mac/Linux
os.system("cls" if os.name == "nt" else "clear")  # Cross-platform

# Current working directory
os.getcwd()               # e.g. "/home/user/projects"

# Environment variables
os.environ.get("PATH")    # Get PATH environment variable
```

---

## The `os.path` Submodule — For File Paths

```python
import os

# This script's absolute path
os.path.abspath(__file__)
# e.g. "/home/user/projects/gamertags_program.py"

# Directory of this script
os.path.dirname(os.path.abspath(__file__))
# e.g. "/home/user/projects"

# Join parts into a path (cross-platform)
os.path.join("/home/user/projects", "gamertags.txt")
# "/home/user/projects/gamertags.txt"

# Check if file exists
os.path.exists("/home/user/projects/gamertags.txt")  # True or False

# Get filename from full path
os.path.basename("/home/user/projects/gamertags.txt")  # "gamertags.txt"
```

---

## Building FILE_PATH Safely

```python
import os

# Combines all os.path calls to get the gamertags.txt path
# regardless of where you run the script from
FILE_PATH = os.path.join(
    os.path.dirname(      # directory part only
        os.path.abspath(__file__)   # absolute path of this script
    ),
    "gamertags.txt"       # the filename
)
```

---

## Other useful standard library modules

| Module | Purpose | Example use |
|---|---|---|
| `os` | Operating system interaction | File paths, shell commands |
| `sys` | Python interpreter info | `sys.exit()`, `sys.argv` |
| `pathlib` | Modern file paths | `Path(__file__).parent / "gamertags.txt"` |
| `re` | Regular expressions | Pattern matching |
| `datetime` | Date and time | `datetime.now()` |
| `json` | JSON parsing | `json.load(f)` |

---

## pathlib — modern alternative to os.path

```python
from pathlib import Path

# Modern path building (Python 3.4+)
FILE_PATH = Path(__file__).parent / "gamertags.txt"

# Read text file
lines = FILE_PATH.read_text(encoding="utf-8").splitlines()

# Append text
with FILE_PATH.open("a", encoding="utf-8") as f:
    f.write("NightOwl42\n")

# Check if exists
FILE_PATH.exists()   # True or False
```

Both `os.path` and `pathlib.Path` work. `os.path` is more traditional and widely understood.
`pathlib` is cleaner and more modern. Either is acceptable in the Gamertags project.
