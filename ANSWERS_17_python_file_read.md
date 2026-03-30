# ANSWERS_17_python_file_read.md

## Python File Reading — Complete Answer Guide

---

## Reading All Lines

```python
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()
# lines = ["DragonSlayer99\n", "StarPilot7\n", "_CoolGamer_\n"]
```

**Important:** Each line has `\n` at the end. Use `.strip()` to remove it.

---

## Stripping Lines

```python
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]
# lines = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]
```

---

## Skipping Blank Lines

```python
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
# Blank lines in the file are excluded
```

The `if line.strip()` filter:
- `line.strip()` removes whitespace
- If result is `""` (empty), the condition is falsy → line is skipped

---

## Complete load_gamertags with error handling

```python
def load_gamertags(self):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"  ERROR: '{FILE_PATH}' not found.")
        self.gamertags = []
```

---

## Alternative: read() — read entire file as one string

```python
with open(FILE_PATH, "r") as f:
    content = f.read()
# content = "DragonSlayer99\nStarPilot7\n_CoolGamer_\n"

# Then split manually
lines = [line for line in content.split("\n") if line.strip()]
```

For the Gamertags project, `readlines()` is cleaner and preferred.

---

## Reading line by line (for large files)

```python
# Efficient for very large files — processes one line at a time
with open(FILE_PATH, "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()
        if stripped:
            self.gamertags.append(stripped)
```

---

## C# vs Python file reading

```csharp
// C# — one call, already stripped
string[] lines = File.ReadAllLines("gamertags.txt");
```

```python
# Python — needs strip() because readlines() keeps \n
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
```

The end result is the same: a list/array of clean strings, one per line.

---

## Test: verify what's loaded

```python
# After loading, add this temporarily to check:
print(f"Loaded {len(self.gamertags)} gamertags")
for i, tag in enumerate(self.gamertags, 1):
    print(f"  {i}: {repr(tag)}")   # repr() shows exact value including spaces
```

Expected output for sample file:
```
Loaded 10 gamertags
  1: 'DragonSlayer99'
  2: 'xXNightHawkXx'
  ...
```
