# CONSOLE_INPUT_OUTPUT_ANSWER.md

## Console Input and Output in Python — Complete Guide

All input/output patterns used in the Gamertags project, with C# comparisons.

---

## 1. `print()` vs `Console.WriteLine()`

### C# `Console.WriteLine()` equivalents in Python

| C# | Python | Notes |
|---|---|---|
| `Console.WriteLine("Hello")` | `print("Hello")` | Adds newline automatically |
| `Console.WriteLine()` | `print()` | Blank line |
| `Console.Write("Hello")` | `print("Hello", end="")` | No newline at end |
| `Console.WriteLine($"Hi {name}")` | `print(f"Hi {name}")` | f-string for variables |

### Examples

```python
# Basic output
print("Hello, Gamertags!")

# With a variable
name = "DragonSlayer99"
print(f"Welcome, {name}!")        # f-string (Python 3.6+)
print("Welcome, {}!".format(name)) # .format() — older style
print("Welcome, " + name + "!")    # Concatenation — works but less readable

# Multiple items
x = 1
y = "StarPilot7"
print(x, y)           # prints "1 StarPilot7" (space between items)
print(x, y, sep=", ") # prints "1, StarPilot7"

# No newline at end (like Console.Write)
print("Enter name: ", end="")   # Cursor stays on same line
name = input()
```

### Formatted output

```python
# Print a numbered list
gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]
for i, tag in enumerate(gamertags, start=1):
    print(f"  {i}. {tag}")

# Output:
#   1. DragonSlayer99
#   2. StarPilot7
#   3. _CoolGamer_

# Print a divider line
print("=" * 40)       # ========================================
print("-" * 40)       # ----------------------------------------
```

---

## 2. `input()` vs `Console.ReadLine()`

### C# `Console.ReadLine()` equivalent

```csharp
// C#
string answer = Console.ReadLine().Trim().ToUpper();
```

```python
# Python
answer = input("Run again? (Y/N): ").strip().upper()
```

### How `input()` works

- Displays the prompt string (if provided)
- Waits for the user to type and press Enter
- Returns the typed text as a **string** (always a string, never int/bool)
- Does NOT include the `\n` from pressing Enter in the returned value

```python
name = input("Enter your gamertag: ")
# If user types "DragonSlayer99" and presses Enter:
# name == "DragonSlayer99"
```

### Always `.strip()` user input

```python
name = input("Enter gamertag: ").strip()
# Removes accidental leading/trailing spaces and Enter characters
# "  DragonSlayer99  " → "DragonSlayer99"
```

---

## 3. Handling Yes/No Prompts

### The standard pattern

```python
answer = input("Run again? (Y/N): ").strip().upper()
if answer == "Y":
    run_again = True
else:
    run_again = False

# Shortened to one line:
run_again = (input("Run again? (Y/N): ").strip().upper() == "Y")
```

### Case-insensitive handling

`.upper()` converts `"y"` → `"Y"`, `"yes"` → `"YES"`, etc.
Without it, `"y"` would not match `"Y"`.

```python
# WRONG — "y" doesn't match "Y"
answer = input("Run again? ").strip()
if answer == "Y":     # Only matches uppercase Y

# CORRECT
answer = input("Run again? ").strip().upper()
if answer == "Y":     # Matches "Y", "y", "Y " (after strip)
```

### Accept "yes" or "Y"

```python
answer = input("Run again? (yes/no): ").strip().lower()
run_again = answer in ("y", "yes")
```

---

## 4. `Console.ReadKey()` equivalent — "Press any key to continue"

C# often uses `Console.ReadKey()` to pause.
Python's equivalent:

```python
input("\nPress Enter to continue...")
# Waits until user presses Enter
```

Or a more C#-like pause (cross-platform):
```python
import os

def pause():
    """Pause until user presses Enter."""
    input("\nPress Enter to continue...")
```

---

## 5. Clearing the Screen

```python
import os

# In the show_welcome_message method:
try:
    os.system("cls" if os.name == "nt" else "clear")
except Exception:
    pass
```

| OS | Command |
|---|---|
| Windows | `cls` |
| Mac / Linux | `clear` |

`os.name == "nt"` checks if the OS is Windows (`"nt"` = NT = Windows).
C# equivalent: `Console.Clear()`

---

## 6. Complete I/O Implementation Example

```python
import os

def show_welcome_message():
    """Clear screen and show banner."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass
    print("=" * 40)
    print("       GAMERTAGS APP (Python)")
    print("=" * 40)
    print()


def get_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return True for Y, False for N."""
    answer = input(prompt).strip().upper()
    return answer == "Y"


def get_non_empty_input(prompt: str) -> str:
    """Ask for input and keep asking until a non-empty value is given."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Please enter a value.")


# Usage
show_welcome_message()

if get_yes_no("Add a new gamertag? (Y/N): "):
    new_tag = get_non_empty_input("  Enter new gamertag: ")
    print(f"  Saving '{new_tag}'...")

run_again = get_yes_no("\nRun again? (Y/N): ")
```

---

## 7. Common Mistakes

### Mistake 1: Forgetting `.strip()` on input

```python
# WRONG — extra spaces cause comparison to fail
answer = input("Run again? ").upper()
if answer == "Y":     # " Y" != "Y"
```

### Mistake 2: Assuming input() returns a number

```python
# WRONG — input() ALWAYS returns a string
choice = input("Enter choice: ")
if choice == 1:       # Never True — "1" != 1
```

```python
# CORRECT — compare to string
if choice == "1":
# OR convert to int if you need arithmetic
number = int(input("Enter number: "))
```

### Mistake 3: Not handling `Console.Write` (no-newline print)

```python
# WRONG — extra blank line before user types
print("Enter name: ")   # println adds \n, then input adds its own prompt
name = input()
```

```python
# CORRECT — use input() with the prompt built in
name = input("Enter name: ")
```

### Mistake 4: Using print() without f-strings for variables

```python
# WORKS but hard to read
print("Tag: " + tag + " — index: " + str(i))
```

```python
# BETTER
print(f"Tag: {tag} — index: {i}")
```
