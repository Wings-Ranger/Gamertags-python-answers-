# ANSWERS_21_python_try_except.md

## Python try/except — Complete Answer Guide

---

## Basic Structure

```python
# C#:
# try { ... }
# catch (FileNotFoundException e) { ... }
# finally { ... }

# Python:
try:
    # Code that might fail
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    # Runs if FileNotFoundError is raised
    print("File not found!")
except Exception as e:
    # Catch-all for other errors
    print(f"Unexpected error: {e}")
finally:
    # Always runs (cleanup code)
    print("Done attempting file read.")
```

---

## Exception Types in the Gamertags Program

| Operation | Possible exception | Python exception class |
|---|---|---|
| Reading file | File doesn't exist | `FileNotFoundError` |
| Reading file | No permission | `PermissionError` |
| Writing file | No permission / disk full | `IOError` |
| String index | Empty string | `IndexError` |
| Type conversion | Invalid value | `ValueError` |

---

## File reading with error handling

```python
def load_gamertags(self):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"  ERROR: Could not find '{FILE_PATH}'.")
        print("  Please create a gamertags.txt file.")
        self.gamertags = []   # Ensure list is empty, not None
```

---

## File writing with error handling

```python
def add_new_username(self):
    new_tag = input("  Enter new gamertag: ").strip()
    if not new_tag:
        return

    try:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(new_tag + "\n")
        print(f"  '{new_tag}' saved!")
        self.load_gamertags()
    except IOError as e:
        print(f"  ERROR: Could not write to file. {e}")
```

---

## Re-raising exceptions

```python
try:
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print(f"File not found: {e}")
    raise    # Re-raise the same exception (C#: throw;)
```

---

## Multiple except blocks

```python
try:
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found.")
    self.gamertags = []
except PermissionError:
    print("Permission denied.")
    self.gamertags = []
except Exception as e:
    print(f"Unexpected: {e}")
    self.gamertags = []
```

---

## try/except vs if/else for file existence

```python
# C# style — check first
if not os.path.exists(FILE_PATH):
    print("File not found")
    return
with open(FILE_PATH, "r") as f:
    lines = f.readlines()

# Python style — EAFP (Easier to Ask Forgiveness than Permission)
# Python prefers try/except — it's more idiomatic and handles more edge cases
try:
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found")
```

The Python `try/except` approach is preferred because:
1. Avoids a race condition (file could disappear between the check and the open)
2. Handles more error types (permissions, etc.)
3. More idiomatic Python

---

## Silent error handling with pass

```python
try:
    os.system("cls" if os.name == "nt" else "clear")
except Exception:
    pass   # If screen clearing fails, just continue — not critical
```

Use `pass` only when you truly don't care about the error.
