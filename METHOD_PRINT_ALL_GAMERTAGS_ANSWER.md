# METHOD_PRINT_ALL_GAMERTAGS_ANSWER.md

## Method: print_all_gamertags

**Purpose:** Display every gamertag in the list, numbered starting from 1.

---

## Complete Working Code

```python
def print_all_gamertags(self):
    """Display all gamertags, numbered from 1."""
    print("\n--- ALL GAMERTAGS ---")
    if not self.gamertags:
        print("  (no gamertags loaded)")
        return

    for i, tag in enumerate(self.gamertags, start=1):
        print(f"  {i}. {tag}")
    print()
```

---

## Explanation of Each Line

### `print("\n--- ALL GAMERTAGS ---")`
Prints a section header with a blank line before it (`\n`).
The `\n` creates a blank line above the header for readability.

### `if not self.gamertags:`
Checks whether the list is empty.
In Python, an empty list is **falsy** — `not []` is `True`.
This guard prevents printing a blank numbered section with nothing in it.
- `return` exits the method early (no further code runs).

### `for i, tag in enumerate(self.gamertags, start=1):`

`enumerate()` is the Pythonic way to loop with an index.

| Part | Meaning |
|---|---|
| `enumerate(self.gamertags)` | Produces `(0, "DragonSlayer99")`, `(1, "StarPilot7")`, etc. |
| `start=1` | Makes the count begin at 1 instead of 0 |
| `i` | The current number (1, 2, 3, ...) |
| `tag` | The current gamertag string |

C# equivalent:
```csharp
for (int i = 0; i < gamertags.Length; i++) {
    Console.WriteLine($"{i + 1}. {gamertags[i]}");
}
```

### `print(f"  {i}. {tag}")`
Prints the number and gamertag using an **f-string** (formatted string literal).
- `f"..."` — Python's version of C# `$"..."`
- `{i}` and `{tag}` are replaced with their values at runtime.
- The two leading spaces indent the output for readability.

### Final `print()`
Prints a blank line after the list, separating sections visually.

---

## Example Output

For gamertags: `["DragonSlayer99", "StarPilot7", "_CoolGamer_"]`

```
--- ALL GAMERTAGS ---
  1. DragonSlayer99
  2. StarPilot7
  3. _CoolGamer_

```

---

## Test Scenarios

### Scenario 1: Normal list
```python
self.gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]
```
Output:
```
--- ALL GAMERTAGS ---
  1. DragonSlayer99
  2. StarPilot7
  3. _CoolGamer_
```

### Scenario 2: Empty list
```python
self.gamertags = []
```
Output:
```
--- ALL GAMERTAGS ---
  (no gamertags loaded)
```

### Scenario 3: Single item
```python
self.gamertags = ["ProPlayer1"]
```
Output:
```
--- ALL GAMERTAGS ---
  1. ProPlayer1
```

---

## Common Mistakes

### Mistake 1: C-style for loop (unnecessary in Python)
```python
# WRONG — verbose and error-prone
for i in range(len(self.gamertags)):
    print(f"  {i + 1}. {self.gamertags[i]}")
```
```python
# CORRECT — Pythonic way
for i, tag in enumerate(self.gamertags, start=1):
    print(f"  {i}. {tag}")
```

### Mistake 2: Numbering starts at 0
```python
# WRONG — shows "0. DragonSlayer99, 1. StarPilot7 ..."
for i, tag in enumerate(self.gamertags):
    print(f"  {i}. {tag}")
```
```python
# CORRECT — start=1 makes it 1-based
for i, tag in enumerate(self.gamertags, start=1):
    print(f"  {i}. {tag}")
```

### Mistake 3: No empty-list check
```python
# BAD — prints "--- ALL GAMERTAGS ---" then nothing; confusing
def print_all_gamertags(self):
    print("\n--- ALL GAMERTAGS ---")
    for i, tag in enumerate(self.gamertags, start=1):
        print(f"  {i}. {tag}")
```

### Mistake 4: Using string concatenation instead of f-string
```python
# WORKS but harder to read
print("  " + str(i) + ". " + tag)
```
```python
# BETTER
print(f"  {i}. {tag}")
```
