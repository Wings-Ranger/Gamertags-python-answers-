# ANSWERS_16_python_file_open.md

## Python File Opening — Complete Answer Guide

---

## Opening a File

```python
# C#: using (var f = File.OpenText("gamertags.txt")) { ... }
with open("gamertags.txt", "r", encoding="utf-8") as f:
    content = f.read()
# File is automatically closed here
```

---

## File Modes

| Mode | Meaning | Creates if missing? | Overwrites? |
|---|---|---|---|
| `"r"` | Read only | No (FileNotFoundError) | No |
| `"w"` | Write (create/overwrite) | Yes | YES — careful! |
| `"a"` | Append | Yes | No |
| `"r+"` | Read and write | No | No |
| `"x"` | Create (fail if exists) | — | N/A |

---

## The `with` Statement

Always use `with open(...) as f:` — it automatically closes the file.

```python
# CORRECT — with statement
with open(FILE_PATH, "r") as f:
    lines = f.readlines()
# f is closed here automatically

# RISKY — manual close (easy to forget, especially if error occurs)
f = open(FILE_PATH, "r")
lines = f.readlines()
f.close()   # If exception above, this never runs
```

---

## Safe Path Building

```python
import os

# Always build the path relative to the script file
FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "gamertags.txt"
)
```

---

## Reading Methods

```python
with open(FILE_PATH, "r", encoding="utf-8") as f:
    all_content = f.read()         # Single string with all content
    lines = f.readlines()          # List of strings, one per line (with \n)
    first_line = f.readline()      # Read one line at a time
```

For the Gamertags project, use `readlines()` and strip each line:

```python
with open(FILE_PATH, "r", encoding="utf-8") as f:
    self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
```

---

## Writing Methods

```python
with open(FILE_PATH, "a", encoding="utf-8") as f:
    f.write("NightOwl42\n")       # Write string (must add \n manually)
```

---

## Checking if a File Exists

```python
import os

if os.path.exists(FILE_PATH):
    print("File found!")
else:
    print("File not found.")
```

---

## encoding="utf-8"

Always specify encoding to handle international characters (accented letters, etc.):

```python
with open(FILE_PATH, "r", encoding="utf-8") as f:   # CORRECT
    ...

with open(FILE_PATH, "r") as f:   # May fail on some systems with special characters
    ...
```
