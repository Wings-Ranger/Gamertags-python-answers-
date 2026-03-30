# METHOD_LOAD_GAMERTAGS_ANSWER.md

## Method: load_gamertags

**Purpose:** Read all gamertag names from `gamertags.txt` into `self.gamertags` (a Python list).

---

## Complete Working Code

```python
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")

def load_gamertags(self):
    """Load gamertags from FILE_PATH into self.gamertags.
    Shows an error message if the file cannot be found."""
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"  ERROR: Could not find '{FILE_PATH}'.")
        print("  Please create a gamertags.txt file in the same folder as this script.")
        self.gamertags = []
```

---

## Explanation of Every Part

### `FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")`

This builds a **safe, absolute path** to the gamertags file.

| Part | What it does |
|---|---|
| `__file__` | The path of the current Python script |
| `os.path.abspath(__file__)` | Converts to absolute path (no `../` etc.) |
| `os.path.dirname(...)` | Gets just the directory (folder) part |
| `os.path.join(..., "gamertags.txt")` | Adds the filename to that folder |

**Why?** If you run the script from a different directory than where it lives,
a plain `"gamertags.txt"` might not be found. The `__file__`-based approach always works.

C# equivalent: placing the file in the same folder as the `.exe` and using `"gamertags.txt"` directly —
the runtime sets the working directory to the executable's folder automatically.
Python does NOT do this automatically, so we need the explicit path.

### `try: ... except FileNotFoundError:`

Handles the case where `gamertags.txt` does not exist.

- **Without this:** the program crashes with an ugly traceback.
- **With this:** the user sees a helpful message, and the program continues safely with an empty list.

C# equivalent:
```csharp
if (!File.Exists("gamertags.txt")) {
    Console.WriteLine("File not found");
    return;
}
```

### `with open(FILE_PATH, "r", encoding="utf-8") as f:`

- `open(...)` — opens the file
- `"r"` — read mode (no writing allowed)
- `encoding="utf-8"` — handles special characters safely
- `with ... as f:` — automatically closes the file when the block ends (even if an error occurs)

C# equivalent: `File.ReadAllLines("gamertags.txt")` — also auto-closes.

### `[line.strip() for line in f.readlines() if line.strip()]`

This is a **list comprehension** — a compact loop that builds a list.

Equivalent to:
```python
result = []
for line in f.readlines():
    cleaned = line.strip()
    if cleaned:           # skip blank lines
        result.append(cleaned)
self.gamertags = result
```

- `f.readlines()` — returns a list like `["DragonSlayer99\n", "StarPilot7\n", "\n"]`
- `line.strip()` — removes `\n` and any surrounding whitespace
- `if line.strip()` — skips lines that are empty after stripping

---

## Why not just `File.ReadAllLines` style?

C# `File.ReadAllLines` automatically strips newlines.
Python `f.readlines()` does NOT — each line keeps its trailing `\n`.
That's why `.strip()` is necessary.

---

## Test Scenarios

### Scenario 1: File exists and has content
```
gamertags.txt:
  DragonSlayer99
  StarPilot7
  _CoolGamer_
```
Result: `self.gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]`

### Scenario 2: File has blank lines
```
gamertags.txt:
  DragonSlayer99

  StarPilot7
```
Result: `self.gamertags = ["DragonSlayer99", "StarPilot7"]`
(Blank lines are filtered out by `if line.strip()`)

### Scenario 3: File does not exist
Result: Error message printed, `self.gamertags = []` — program continues safely.

### Scenario 4: File is completely empty
Result: `self.gamertags = []` — no crash.

---

## Common Mistakes

### Mistake 1: Using a relative path
```python
# RISKY — only works if you run the script from the correct directory
with open("gamertags.txt", "r") as f:
    ...
```
Use `FILE_PATH` with `os.path` instead.

### Mistake 2: Forgetting to strip lines
```python
# WRONG — self.gamertags will contain "DragonSlayer99\n" with a newline
self.gamertags = f.readlines()
```
Always use `.strip()`.

### Mistake 3: No error handling
```python
# WRONG — crashes if file is missing
with open(FILE_PATH, "r") as f:
    self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
```
Always wrap file operations in `try/except FileNotFoundError`.

### Mistake 4: Not resetting the list on error
```python
except FileNotFoundError:
    print("File not found")
    # Missing: self.gamertags = []
    # If load_gamertags is called again later, old data might still be there
```
Always set `self.gamertags = []` in the except block.
