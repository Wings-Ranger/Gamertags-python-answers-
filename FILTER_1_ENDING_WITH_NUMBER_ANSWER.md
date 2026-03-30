# FILTER_1_ENDING_WITH_NUMBER_ANSWER.md

## Filter: Print Gamertags Ending With a Number

**Rule:** Show only gamertags whose **last character** is a digit (0–9).

---

## Complete Working Code

```python
def print_gamertags_ending_with_number(self):
    """Print only gamertags whose last character is a digit (0–9)."""
    print("\n--- GAMERTAGS ENDING WITH A NUMBER ---")
    found = False

    for tag in self.gamertags:
        # Guard: only check if the string has at least one character
        if len(tag) > 0 and tag[-1].isdigit():
            print(f"  {tag}")
            found = True

    if not found:
        print("  (none found)")
    print()
```

---

## Explanation of Each Line

### `for tag in self.gamertags:`
Iterates over every string in the list.
- C# equivalent: `foreach (string tag in gamertags)`
- `tag` takes the value of each gamertag one at a time.

### `if len(tag) > 0`
**Safety check.** If a gamertag is an empty string `""`, then `tag[-1]` would crash with an `IndexError`.
Always check length before accessing a character by index.

### `and tag[-1].isdigit()`
- `tag[-1]` — Python negative indexing: `-1` always means the **last** character.
  - C# equivalent: `tag[tag.Length - 1]`
- `.isdigit()` — returns `True` if the character is `0`–`9`.
  - C# equivalent: `char.IsDigit(tag[tag.Length - 1])`

### `found = True` flag
Tracks whether anything was printed.
Used at the end to display a helpful "none found" message instead of showing a blank section.

---

## isdigit() vs isnumeric() — which to use?

| Method | What it matches | Use for this filter? |
|---|---|---|
| `.isdigit()` | Characters `0`–`9` only | ✅ YES |
| `.isnumeric()` | Digits + fractions (½) + superscripts (²) | ❌ NO — too broad |
| `.isdecimal()` | Only strict decimal digits 0–9 | ✅ Also works |

**Use `.isdigit()` for this filter.** It matches exactly what the C# `char.IsDigit()` matches.

---

## Test Cases

```python
# Test data
gamertags = [
    "DragonSlayer99",  # ends with 9 → INCLUDE
    "xXNightHawkXx",   # ends with x → exclude
    "_CoolGamer_",     # ends with _ → exclude
    "StarPilot7",      # ends with 7 → INCLUDE
    "!GhostHunter",    # ends with r → exclude
    "NeonWolf3",       # ends with 3 → INCLUDE
    ".ShadowBlade",    # ends with e → exclude
    "CobraKing",       # ends with g → exclude
    "ProPlayer1",      # ends with 1 → INCLUDE
    "",                # empty string → exclude (safe guard)
    "0",               # single digit → INCLUDE
    "abc",             # ends with c → exclude
]

# Expected output:
# DragonSlayer99
# StarPilot7
# NeonWolf3
# ProPlayer1
# 0
```

---

## Standalone test script

```python
# Run this to verify the filter logic independently (no class needed)

test_tags = [
    "DragonSlayer99",
    "xXNightHawkXx",
    "_CoolGamer_",
    "StarPilot7",
    "NeonWolf3",
    "ProPlayer1",
    "",
    "0",
]

print("--- GAMERTAGS ENDING WITH A NUMBER ---")
found = False
for tag in test_tags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(f"  {tag}")
        found = True

if not found:
    print("  (none found)")
```

**Expected output:**
```
--- GAMERTAGS ENDING WITH A NUMBER ---
  DragonSlayer99
  StarPilot7
  NeonWolf3
  ProPlayer1
  0
```

---

## Common Mistakes

### Mistake 1: Forgetting the length check

```python
# WRONG — crashes on empty strings
if tag[-1].isdigit():
    print(tag)
```

```python
# CORRECT
if len(tag) > 0 and tag[-1].isdigit():
    print(tag)
```

### Mistake 2: Using the wrong index

```python
# WRONG — checks the FIRST character, not the last
if tag[0].isdigit():
    print(tag)
```

```python
# CORRECT — -1 is the last character
if tag[-1].isdigit():
    print(tag)
```

### Mistake 3: Using isnumeric() instead of isdigit()

```python
# WRONG — isnumeric() matches ½, ² etc.
if tag[-1].isnumeric():
    print(tag)
```

```python
# CORRECT
if tag[-1].isdigit():
    print(tag)
```

### Mistake 4: Crashing instead of printing a message when nothing matches

```python
# BAD — blank output is confusing
for tag in self.gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(tag)
# (nothing printed if no match — user sees blank section)
```

```python
# GOOD — clear feedback to the user
found = False
for tag in self.gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(tag)
        found = True
if not found:
    print("  (none found)")
```

---

## Alternative Approaches

### Using a list comprehension

```python
def print_gamertags_ending_with_number(self):
    matching = [tag for tag in self.gamertags if len(tag) > 0 and tag[-1].isdigit()]
    print("\n--- GAMERTAGS ENDING WITH A NUMBER ---")
    if matching:
        for tag in matching:
            print(f"  {tag}")
    else:
        print("  (none found)")
```

This is more Pythonic but the original for-loop version is clearer for learners.

### Using filter() function

```python
matching = list(filter(lambda tag: len(tag) > 0 and tag[-1].isdigit(), self.gamertags))
```

Both work; the explicit for-loop is preferred for readability at beginner level.
