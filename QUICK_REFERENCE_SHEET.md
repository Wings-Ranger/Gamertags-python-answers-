# QUICK_REFERENCE_SHEET.md

## Python Quick Reference Sheet — Gamertags Project

A cheat sheet of every Python syntax, method, and pattern used in this project.

---

## Variables and Types

```python
# No type declaration needed
name = "DragonSlayer99"     # str
count = 10                  # int
flag = True                 # bool (capital T/F!)
items = []                  # list (empty)
items = ["a", "b", "c"]    # list with values
nothing = None              # None (like C# null)
```

---

## Strings

```python
tag = "DragonSlayer99"

len(tag)             # 14 — length of string (C#: tag.Length)
tag[0]               # 'D' — first character
tag[-1]              # '9' — last character (C#: tag[tag.Length-1])
tag.strip()          # remove leading/trailing whitespace (C#: .Trim())
tag.upper()          # "DRAGONSLAYER99" (C#: .ToUpper())
tag.lower()          # "dragonslayer99" (C#: .ToLower())
tag.split(",")       # split into list by delimiter
"sub" in tag         # True if substring found (C#: .Contains())

# Character checks (call on a single character)
tag[-1].isdigit()    # True if 0-9 (C#: char.IsDigit())
tag[0].isalpha()     # True if a-z or A-Z (C#: char.IsLetter())
tag[0].isalnum()     # True if letter OR digit (C#: char.IsLetterOrDigit())

# f-strings (like C# $"...")
print(f"Tag: {tag}, Length: {len(tag)}")
```

---

## Lists (equivalent to C# arrays/List<string>)

```python
gamertags = ["DragonSlayer99", "StarPilot7", "CobraKing"]

len(gamertags)           # 3 — number of items
gamertags[0]             # "DragonSlayer99" — first item
gamertags[-1]            # "CobraKing" — last item
gamertags.append("New")  # Add to end
gamertags[0] = "NewTag"  # Replace item

# Check if empty
if not gamertags:        # True when list is empty
    print("empty")

# Iterate
for tag in gamertags:
    print(tag)

# Iterate with index
for i, tag in enumerate(gamertags, start=1):
    print(f"{i}. {tag}")
```

---

## Conditions

```python
# if / elif / else
if answer == "Y":
    run_again = True
elif answer == "N":
    run_again = False
else:
    print("Invalid input")

# One-line conditional (ternary)
command = "cls" if os.name == "nt" else "clear"

# Truthiness
if tag:           # True if tag is non-empty string
if not tag:       # True if tag is empty string ""
if gamertags:     # True if list has items
if not gamertags: # True if list is empty
```

---

## Loops

```python
# while loop with boolean flag
run_again = True
while run_again:
    # ... do work ...
    answer = input("Run again? ").strip().upper()
    run_again = (answer == "Y")

# for loop (like C# foreach)
for tag in gamertags:
    print(tag)

# for loop with index (like C# for with i)
for i, tag in enumerate(gamertags, start=1):
    print(f"  {i}. {tag}")

# for loop with range
for i in range(10):      # 0, 1, 2, ..., 9
for i in range(1, 11):  # 1, 2, ..., 10
```

---

## Functions

```python
# Define a function
def greet(name):
    print(f"Hello, {name}!")

# Call it
greet("DragonSlayer99")

# With a return value
def is_valid_tag(tag):
    return len(tag) > 0

# With default parameter
def print_with_prefix(tag, prefix="  "):
    print(f"{prefix}{tag}")
```

---

## Classes

```python
class Gamertags:
    def __init__(self):            # Constructor (C#: public Gamertags())
        self.gamertags = []        # Instance attribute (C#: private string[] gamertags)

    def load_gamertags(self):      # Instance method (C#: public void LoadGamertags())
        # self refers to the current object (C#: this)
        self.gamertags = []

# Create an instance
gt = Gamertags()       # C#: Gamertags gt = new Gamertags();

# Call a method
gt.load_gamertags()    # C#: gt.LoadGamertags();

# Access attribute
print(gt.gamertags)    # C#: Console.WriteLine(gt.gamertags);
```

---

## File Operations

```python
import os

# Safe path building
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")

# Read all lines
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
# C#: File.ReadAllLines("gamertags.txt")

# Append a line
with open(FILE_PATH, "a", encoding="utf-8") as f:
    f.write(new_tag + "\n")   # Must add \n manually!
# C#: File.AppendText() + sw.WriteLine()

# File modes:
#  "r"  = read (file must exist)
#  "w"  = write (creates or OVERWRITES — dangerous!)
#  "a"  = append (creates or adds to end — safe)
```

---

## Error Handling

```python
# try / except (C#: try / catch)
try:
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found!")
    lines = []
except IOError as e:
    print(f"IO error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Input and Output

```python
# Print (C#: Console.WriteLine)
print("Hello!")
print(f"Tag: {tag}")
print()               # blank line

# Print without newline (C#: Console.Write)
print("Enter: ", end="")

# Input (C#: Console.ReadLine)
answer = input("Run again? (Y/N): ").strip().upper()

# Clear screen (C#: Console.Clear)
import os
os.system("cls" if os.name == "nt" else "clear")
```

---

## List Comprehensions (concise loops)

```python
# Basic: create a new list from an existing one
stripped = [line.strip() for line in lines]

# With condition: only include items that match
non_empty = [line.strip() for line in lines if line.strip()]

# Equivalent plain loop:
non_empty = []
for line in lines:
    cleaned = line.strip()
    if cleaned:
        non_empty.append(cleaned)

# Filter gamertags ending with a number
ending_with_num = [tag for tag in gamertags if len(tag) > 0 and tag[-1].isdigit()]
```

---

## Entry Point Pattern

```python
def main():
    # Your main program logic here
    pass

# This ensures main() only runs when THIS file is executed directly
# (not when imported by another file)
if __name__ == "__main__":
    main()
# C# equivalent: static void Main(string[] args) { }
```

---

## C# to Python Quick Lookup

| C# | Python |
|---|---|
| `bool flag = true;` | `flag = True` |
| `string tag = "x";` | `tag = "x"` |
| `int count = 0;` | `count = 0` |
| `string[] list = ...` | `list = [...]` |
| `new Foo()` | `Foo()` |
| `this.field` | `self.field` |
| `Console.WriteLine(x)` | `print(x)` |
| `Console.ReadLine()` | `input()` |
| `.Trim()` | `.strip()` |
| `.ToUpper()` | `.upper()` |
| `.Length` | `len(x)` |
| `char.IsDigit(c)` | `c.isdigit()` |
| `char.IsLetterOrDigit(c)` | `c.isalnum()` |
| `tag[tag.Length - 1]` | `tag[-1]` |
| `foreach (var x in list)` | `for x in list:` |
| `for (int i=0; ...)` | `for i, x in enumerate(list, start=1):` |
| `File.ReadAllLines(path)` | `open(path).readlines()` + `.strip()` |
| `File.AppendText(path)` | `open(path, "a")` |
| `Console.Clear()` | `os.system("cls"/"clear")` |
| `try { } catch (Exception e)` | `try: ... except Exception as e:` |
| `using (var f = ...)` | `with open(...) as f:` |
