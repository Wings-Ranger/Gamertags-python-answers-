# COMMON_MISTAKES_REFERENCE.md

## Common Mistakes and How to Fix Them

A reference guide for the most frequent errors when porting the Gamertags C# project to Python.

---

## Mistake 1: Off-by-one error in numbering

### The problem
```python
# WRONG — numbering starts at 0
for i in range(len(self.gamertags)):
    print(f"{i}. {self.gamertags[i]}")
# Output: 0. DragonSlayer99, 1. StarPilot7 ...
```

### The fix
```python
# CORRECT — use enumerate with start=1
for i, tag in enumerate(self.gamertags, start=1):
    print(f"  {i}. {tag}")
# Output: 1. DragonSlayer99, 2. StarPilot7 ...
```

---

## Mistake 2: Not stripping user input

### The problem
```python
# WRONG — user types " Y " (with spaces) and it doesn't match
answer = input("Run again? ").upper()
if answer == "Y":    # " Y " != "Y" — loop never continues!
    run_again = True
```

### The fix
```python
# CORRECT — strip removes leading/trailing whitespace
answer = input("Run again? ").strip().upper()
if answer == "Y":    # Works for "Y", "y", " Y ", etc.
    run_again = True
```

---

## Mistake 3: Forgetting to check string length before indexing

### The problem
```python
# WRONG — crashes with IndexError if tag is an empty string
if tag[-1].isdigit():
    print(tag)
```

### The fix
```python
# CORRECT — check length first
if len(tag) > 0 and tag[-1].isdigit():
    print(tag)
```

**Why does this happen?** An empty line in `gamertags.txt` becomes `""` after `.strip()`.
If not filtered out, accessing `""[-1]` raises `IndexError`.
The list comprehension in `load_gamertags` filters them, but defensive checks are still good practice.

---

## Mistake 4: File path issues (wrong working directory)

### The problem
```python
# WRONG — only works if script is run from its own directory
with open("gamertags.txt", "r") as f:
    ...
# FileNotFoundError when run from another directory
```

### The fix
```python
import os

# Build path relative to the script's own location
FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "gamertags.txt"
)

with open(FILE_PATH, "r") as f:
    ...
```

---

## Mistake 5: Using write mode instead of append mode

### The problem
```python
# WRONG — "w" DELETES all existing gamertags!
with open(FILE_PATH, "w") as f:
    f.write(new_tag + "\n")
```

### The fix
```python
# CORRECT — "a" appends to the end, never overwrites
with open(FILE_PATH, "a") as f:
    f.write(new_tag + "\n")
```

---

## Mistake 6: Forgetting `\n` when writing to file

### The problem
```python
# WRONG — new entry merges with previous last line
with open(FILE_PATH, "a") as f:
    f.write(new_tag)
# Result: last two lines become "ZeroHourNightOwl42" (joined!)
```

### The fix
```python
# CORRECT — always include \n at end
with open(FILE_PATH, "a") as f:
    f.write(new_tag + "\n")
```

---

## Mistake 7: Not reloading gamertags after adding a new one

### The problem
```python
# WRONG — new tag is saved to file but not in memory
with open(FILE_PATH, "a") as f:
    f.write(new_tag + "\n")
# self.gamertags still doesn't have the new tag
# Next display won't show it until the program restarts
```

### The fix
```python
# CORRECT — reload after saving
with open(FILE_PATH, "a") as f:
    f.write(new_tag + "\n")
self.load_gamertags()    # Refresh the in-memory list
```

---

## Mistake 8: Using `isnumeric()` instead of `isdigit()`

### The problem
```python
# RISKY — isnumeric() also matches ², ½, and other non-standard numeric characters
if tag[-1].isnumeric():
    print(tag)
# A gamertag ending with "²" would incorrectly appear
```

### The fix
```python
# CORRECT — isdigit() matches only 0–9 (matches C# char.IsDigit behavior)
if tag[-1].isdigit():
    print(tag)
```

---

## Mistake 9: Using `isalpha()` instead of `isalnum()` for filter 2

### The problem
```python
# WRONG — isalpha() only checks letters, not digits
# "1stPlace" starts with '1' (digit, not alpha)
# not '1'.isalpha() → True → "1stPlace" is incorrectly included!
if len(tag) > 0 and not tag[0].isalpha():
    print(tag)
```

### The fix
```python
# CORRECT — isalnum() checks both letters AND digits (matches C# IsLetterOrDigit)
if len(tag) > 0 and not tag[0].isalnum():
    print(tag)
```

---

## Mistake 10: Loop control problems — `run_again` never becoming False

### The problem
```python
# WRONG — always True; program never stops
while run_again:
    ...
    answer = input("Run again? ")
    if answer == "Y":
        run_again = True
    # Missing: else run_again = False
```

### The fix
```python
# CORRECT — assignment covers both cases
run_again = (answer.strip().upper() == "Y")
# True if "Y", False for anything else
```

---

## Mistake 11: `True` capitalisation error

### The problem
```python
# WRONG — Python is case-sensitive; 'true' is not defined
run_again = true    # NameError: name 'true' is not defined
```

### The fix
```python
# CORRECT — Python booleans are capitalized
run_again = True
run_again = False
```

---

## Mistake 12: Accessing `self` attributes without `self.`

### The problem
```python
class Gamertags:
    def __init__(self):
        self.gamertags = []

    def print_all_gamertags(self):
        for tag in gamertags:    # NameError: name 'gamertags' is not defined
            print(tag)
```

### The fix
```python
    def print_all_gamertags(self):
        for tag in self.gamertags:    # Always use self. to access instance attributes
            print(tag)
```

---

## Mistake 13: Forgetting to handle an empty gamertag list

### The problem
```python
# BAD — if list is empty, the header prints but nothing follows — confusing
def print_all_gamertags(self):
    print("--- ALL GAMERTAGS ---")
    for i, tag in enumerate(self.gamertags, start=1):
        print(f"  {i}. {tag}")
```

### The fix
```python
def print_all_gamertags(self):
    print("--- ALL GAMERTAGS ---")
    if not self.gamertags:
        print("  (no gamertags loaded)")
        return
    for i, tag in enumerate(self.gamertags, start=1):
        print(f"  {i}. {tag}")
```

---

## Quick Checklist — Before You Run Your Code

- [ ] `import os` is at the top of the file
- [ ] `FILE_PATH` uses `os.path.dirname(os.path.abspath(__file__))`
- [ ] File mode is `"a"` (not `"w"`) when appending
- [ ] Every `f.write(...)` ends with `"\n"`
- [ ] Every `input(...)` is followed by `.strip()`
- [ ] Both filters check `len(tag) > 0` before indexing
- [ ] Filter 2 uses `.isalnum()` (not `.isalpha()`)
- [ ] Filter 1 uses `.isdigit()` (not `.isnumeric()`)
- [ ] `run_again` uses `True`/`False` (capital T/F)
- [ ] All methods use `self.gamertags` (with `self.`)
- [ ] `self.load_gamertags()` is called inside the while loop
- [ ] `self.load_gamertags()` is called after `add_new_username()`
