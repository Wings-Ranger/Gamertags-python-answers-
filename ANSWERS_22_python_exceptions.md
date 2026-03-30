# ANSWERS_22_python_exceptions.md

## Python Exception Types — Complete Answer Guide

---

## Common Built-in Exceptions

| Exception | When it occurs | Example |
|---|---|---|
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `PermissionError` | No file access permission | `open("/etc/shadow", "w")` |
| `IOError` | General I/O failure | Disk full, device error |
| `IndexError` | Index out of range | `""[0]`, `[][5]` |
| `ValueError` | Wrong value type | `int("abc")` |
| `TypeError` | Wrong argument type | `len(42)` |
| `KeyError` | Dict key missing | `d["missing"]` |
| `AttributeError` | Method/attribute not found | `None.strip()` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `NameError` | Variable not defined | using `true` (lowercase) |

---

## Exceptions in the Gamertags Project

### `FileNotFoundError`

```python
# Raised when gamertags.txt doesn't exist
try:
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("gamertags.txt not found!")
    self.gamertags = []
```

### `IndexError` (prevented by length check)

```python
tag = ""
# Without guard:
tag[-1].isdigit()    # IndexError: string index out of range

# With guard:
if len(tag) > 0 and tag[-1].isdigit():
    print(tag)       # Safe — only accesses [-1] if tag is non-empty
```

### `IOError` when writing

```python
try:
    with open(FILE_PATH, "a") as f:
        f.write(new_tag + "\n")
except IOError as e:
    print(f"Could not write: {e}")
```

---

## Exception Hierarchy

All exceptions inherit from `Exception` (like C#'s `Exception` base class).

```
BaseException
└── Exception
    ├── FileNotFoundError (also an OSError / IOError)
    ├── PermissionError   (also an OSError)
    ├── IndexError
    ├── ValueError
    ├── TypeError
    └── ... many more
```

Catching `Exception` catches most errors:
```python
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## Raising Your Own Exceptions

```python
def add_gamertag(tag):
    if not isinstance(tag, str):
        raise TypeError(f"Expected str, got {type(tag).__name__}")
    if len(tag) == 0:
        raise ValueError("Gamertag cannot be empty")
    return tag.strip()
```

---

## `as e` — accessing exception details

```python
try:
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print(f"Error: {e}")          # Error: [Errno 2] No such file or directory: '...'
    print(f"Message: {e.args}")   # Message: (2, 'No such file or directory')
```

---

## Best practices for this project

1. **Always** catch `FileNotFoundError` in `load_gamertags()`
2. **Always** catch `IOError` in `add_new_username()`
3. **Avoid** bare `except:` — it hides all errors including `KeyboardInterrupt`
4. **Set fallback values** in except blocks (`self.gamertags = []`)
5. **Don't silence errors** unless you have a good reason (like screen clearing)
