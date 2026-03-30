# ANSWERS_14_python_classes.md

## Python Classes — Complete Answer Guide

---

## Class Definition

```python
# C#: class Gamertags { ... }
class Gamertags:
    """A class that manages a list of gamertags from a file."""
    pass   # Empty class — replace with actual code
```

---

## Constructor: `__init__`

```python
class Gamertags:
    def __init__(self):
        # C#: public Gamertags() { gamertags = new string[0]; }
        self.gamertags = []   # Instance attribute — each object gets its own list
```

`__init__` runs automatically when you create an object: `gt = Gamertags()`

---

## Instance Attributes

Attributes are data stored on each object.
In Python, they're created in `__init__` with `self.`:

```python
class Gamertags:
    def __init__(self):
        self.gamertags = []        # equivalent to C#: private string[] gamertags;
        self.file_path = ""        # could also store the file path here
```

---

## Methods

Methods are functions inside a class. They always take `self` as the first parameter.

```python
class Gamertags:
    def __init__(self):
        self.gamertags = []

    def load_gamertags(self):
        # self.gamertags refers to THIS object's list
        self.gamertags = ["DragonSlayer99", "StarPilot7"]

    def print_all_gamertags(self):
        for i, tag in enumerate(self.gamertags, start=1):
            print(f"  {i}. {tag}")
```

---

## Creating an Object (Instance)

```python
# C#: Gamertags gt = new Gamertags();
gt = Gamertags()          # no 'new' keyword in Python

# Call methods
gt.load_gamertags()
gt.print_all_gamertags()

# Access attributes
print(gt.gamertags)       # ['DragonSlayer99', 'StarPilot7']
print(len(gt.gamertags))  # 2
```

---

## `self` explained

`self` is the reference to the current object — like C#'s `this`.

```python
class Gamertags:
    def __init__(self):
        self.gamertags = []

    def load_gamertags(self):
        # self.gamertags — this object's gamertags list
        # If you forget self, Python looks for a local variable named 'gamertags'
        self.gamertags = ["DragonSlayer99"]   # CORRECT
        gamertags = ["DragonSlayer99"]         # local variable, NOT saved to object
```

---

## Complete Gamertags Class

```python
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")

class Gamertags:
    def __init__(self):
        self.gamertags = []

    def load_gamertags(self):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            self.gamertags = []

    def show_welcome_message(self):
        import os
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 40)
        print("       GAMERTAGS APP (Python)")
        print("=" * 40)

    def print_all_gamertags(self):
        print("\n--- ALL GAMERTAGS ---")
        if not self.gamertags:
            print("  (no gamertags loaded)")
            return
        for i, tag in enumerate(self.gamertags, start=1):
            print(f"  {i}. {tag}")

    def print_gamertags_ending_with_number(self):
        print("\n--- ENDING WITH NUMBER ---")
        found = False
        for tag in self.gamertags:
            if len(tag) > 0 and tag[-1].isdigit():
                print(f"  {tag}")
                found = True
        if not found:
            print("  (none found)")

    def print_gamertags_not_starting_with_letter_or_digit(self):
        print("\n--- NOT STARTING WITH LETTER OR DIGIT ---")
        found = False
        for tag in self.gamertags:
            if len(tag) > 0 and not tag[0].isalnum():
                print(f"  {tag}")
                found = True
        if not found:
            print("  (none found)")

    def add_new_username(self):
        new_tag = input("  Enter new gamertag: ").strip()
        if not new_tag:
            print("  (nothing saved)")
            return
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(new_tag + "\n")
        self.load_gamertags()
```

---

## C# vs Python class comparison

| C# | Python |
|---|---|
| `class Gamertags { }` | `class Gamertags:` |
| `public Gamertags() { }` | `def __init__(self):` |
| `private string[] gamertags;` | `self.gamertags = []` |
| `public void LoadGamertags()` | `def load_gamertags(self):` |
| `this.gamertags` | `self.gamertags` |
| `Gamertags gt = new Gamertags();` | `gt = Gamertags()` |
| `gt.LoadGamertags();` | `gt.load_gamertags()` |
