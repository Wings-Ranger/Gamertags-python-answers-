# FILE_OPERATIONS_ANSWER.md

## File I/O in Python — Complete Guide

Everything you need to know about reading and writing files for the Gamertags project.

---

## 1. Reading Files (equivalent to C# `File.ReadAllLines`)

### C# approach
```csharp
string[] lines = File.ReadAllLines("gamertags.txt");
```

### Python approach

```python
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
```

### Step-by-step breakdown

#### `open(FILE_PATH, "r", encoding="utf-8")`

| Parameter | Meaning |
|---|---|
| `FILE_PATH` | Path to the file |
| `"r"` | Read mode — file must exist |
| `encoding="utf-8"` | Character set — handles accented characters and symbols safely |

#### `with ... as f:`

The `with` statement is a **context manager**.
It automatically closes the file when the block exits — even if an error occurs.
Equivalent to C# `using (var f = File.OpenText(...)) { }`.

Without `with`:
```python
f = open(FILE_PATH, "r")
lines = f.readlines()
f.close()   # Easy to forget — causes resource leak
```

With `with` (correct):
```python
with open(FILE_PATH, "r") as f:
    lines = f.readlines()
# f is automatically closed here
```

#### `f.readlines()`

Returns a list of strings, one per line, **including the `\n` newline character**:
```python
["DragonSlayer99\n", "StarPilot7\n", "_CoolGamer_\n"]
```

#### `line.strip()`

Removes `\n` and any surrounding whitespace from each line:
```python
"DragonSlayer99\n".strip()   # → "DragonSlayer99"
"  StarPilot7  \n".strip()   # → "StarPilot7"
```

#### `if line.strip()` (the filter)

Skips blank lines. Without this, an empty line in the file becomes `""` in the list.

---

## 2. Appending to Files (equivalent to C# `File.AppendText`)

### C# approach
```csharp
using (StreamWriter sw = File.AppendText("gamertags.txt"))
{
    sw.WriteLine(newTag);   // WriteLine adds \r\n automatically
}
```

### Python approach
```python
with open(FILE_PATH, "a", encoding="utf-8") as f:
    f.write(new_tag + "\n")   # Must add \n manually
```

### File modes explained

| Mode | Meaning | File must exist? | Overwrites? |
|---|---|---|---|
| `"r"` | Read only | Yes (raises FileNotFoundError if not) | No |
| `"w"` | Write (create or overwrite) | No (creates if missing) | YES — dangerous! |
| `"a"` | Append (create or add to end) | No (creates if missing) | No |
| `"r+"` | Read and write | Yes | No (unless you seek) |

**IMPORTANT:** Never use `"w"` to add a gamertag — it would **delete** all existing ones!
Always use `"a"` for appending.

---

## 3. Relative vs Absolute Paths

### The problem with relative paths

```python
# This works ONLY if you run the script from the same directory it's in
with open("gamertags.txt", "r") as f:
    ...
```

If you run `python src/gamertags.py` from the project root, Python looks for
`gamertags.txt` in the **current working directory** (project root), not `src/`.

### The solution — path relative to the script

```python
import os

# Build path relative to THIS script's location
FILE_PATH = os.path.join(
    os.path.dirname(   # Get just the directory part
        os.path.abspath(__file__)  # Absolute path of this script
    ),
    "gamertags.txt"    # The filename to attach
)
```

With this approach, `gamertags.txt` is always expected to be **in the same folder as the script**.
Works regardless of what directory you run the script from.

---

## 4. Error Handling for Missing Files

```python
try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print(f"  ERROR: '{FILE_PATH}' not found.")
    print("  Create a gamertags.txt file in the same folder as this script.")
    self.gamertags = []
except PermissionError:
    print(f"  ERROR: No permission to read '{FILE_PATH}'.")
    self.gamertags = []
except Exception as e:
    print(f"  Unexpected error reading file: {e}")
    self.gamertags = []
```

For most cases, catching `FileNotFoundError` is sufficient.
Adding `except Exception as e:` as a catch-all ensures the program never crashes unexpectedly.

---

## 5. Complete File Operation Functions

### Read all gamertags

```python
def load_gamertags(self):
    """Read all gamertags from file into self.gamertags list."""
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"  ERROR: Could not find '{FILE_PATH}'.")
        self.gamertags = []
```

### Append a new gamertag

```python
def save_new_gamertag(name: str) -> bool:
    """Append a new gamertag to the file. Returns True on success."""
    if not name:
        return False
    try:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(name + "\n")
        return True
    except IOError as e:
        print(f"  ERROR: Could not write to file: {e}")
        return False
```

### Check if file exists

```python
import os

if os.path.exists(FILE_PATH):
    print("File found!")
else:
    print("File not found — creating a new one.")
    open(FILE_PATH, "w").close()   # Create empty file
```

---

## 6. Creating the gamertags.txt File

Before running the program, create `gamertags.txt` in the same folder as `COMPLETE_GAMERTAGS_PROGRAM.py`:

```
DragonSlayer99
xXNightHawkXx
_CoolGamer_
StarPilot7
!GhostHunter
NeonWolf3
.ShadowBlade
CobraKing
ProPlayer1
ZeroHour
```

Each name on its own line. No trailing spaces.

---

## Common Mistakes

### Mistake 1: Using write mode instead of append

```python
# WRONG — deletes all existing gamertags!
with open(FILE_PATH, "w") as f:
    f.write(new_tag + "\n")
```

### Mistake 2: Forgetting `\n` when writing

```python
# WRONG — next entry runs on the same line as this one
f.write(new_tag)
```

### Mistake 3: Not using `with` (forgetting to close the file)

```python
# RISKY — if error occurs before f.close(), file stays open
f = open(FILE_PATH, "a")
f.write(new_tag + "\n")
f.close()
```

### Mistake 4: Not stripping lines after readlines()

```python
# WRONG — self.gamertags contains "DragonSlayer99\n" with newline
self.gamertags = f.readlines()
```

### Mistake 5: No error handling for missing file

```python
# WRONG — crashes with ugly traceback if file is missing
with open(FILE_PATH, "r") as f:
    self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
```
