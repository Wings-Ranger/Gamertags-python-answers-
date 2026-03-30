# ANSWERS_12_python_functions.md

## Python Functions — Complete Answer Guide

---

## Defining and Calling Functions

```python
# Define (C#: void Greet() { ... })
def greet():
    print("Welcome to Gamertags!")

# Call
greet()   # Output: Welcome to Gamertags!
```

---

## Functions with Parameters

```python
def print_tag(tag):
    print(f"  → {tag}")

print_tag("DragonSlayer99")   # Output:   → DragonSlayer99
```

---

## Functions with Return Values

```python
def ends_with_number(tag):
    """Return True if tag is non-empty and ends with a digit."""
    return len(tag) > 0 and tag[-1].isdigit()

# Usage
if ends_with_number("StarPilot7"):
    print("Ends with a number!")
```

---

## Functions with Default Parameters

```python
def show_tag(tag, prefix="  "):
    print(f"{prefix}{tag}")

show_tag("DragonSlayer99")          # "  DragonSlayer99" (default prefix)
show_tag("StarPilot7", prefix="→ ") # "→ StarPilot7"
```

---

## Methods vs Functions

- **Function:** standalone, not inside a class
- **Method:** inside a class, has `self` as first parameter

```python
# Function
def greet():
    print("Hello!")

# Method (inside a class)
class Gamertags:
    def load_gamertags(self):   # 'self' = reference to the object
        self.gamertags = []
```

---

## The 6 Methods of the Gamertags Class

```python
class Gamertags:
    def __init__(self):                                    # Constructor
    def load_gamertags(self):                              # Load from file
    def show_welcome_message(self):                        # Display banner
    def print_all_gamertags(self):                         # Show all tags
    def print_gamertags_ending_with_number(self):          # Filter 1
    def print_gamertags_not_starting_with_letter_or_digit(self):  # Filter 2
    def add_new_username(self):                            # Save new tag
```

---

## Early Return

```python
def print_all_gamertags(self):
    print("\n--- ALL GAMERTAGS ---")
    if not self.gamertags:
        print("  (no gamertags loaded)")
        return     # Exit the method here — nothing else runs
    for i, tag in enumerate(self.gamertags, start=1):
        print(f"  {i}. {tag}")
```

`return` without a value exits the function and returns `None` (equivalent to C# `return;` in a void method).

---

## Helper functions

```python
# Standalone helper (not a method)
def ends_with_number(tag):
    return len(tag) > 0 and tag[-1].isdigit()

def starts_with_symbol(tag):
    return len(tag) > 0 and not tag[0].isalnum()

# Use in the class
class Gamertags:
    def print_gamertags_ending_with_number(self):
        for tag in self.gamertags:
            if ends_with_number(tag):   # use helper
                print(f"  {tag}")
```

---

## C# to Python method naming

| C# | Python |
|---|---|
| `public void LoadGamertags()` | `def load_gamertags(self):` |
| `public void ShowWelcomeMessage()` | `def show_welcome_message(self):` |
| `public void PrintAllGamertags()` | `def print_all_gamertags(self):` |
| `public void AddNewUsername()` | `def add_new_username(self):` |

Python uses `snake_case` (underscores); C# uses `PascalCase` for methods.
