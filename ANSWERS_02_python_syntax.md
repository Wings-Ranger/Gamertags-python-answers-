# ANSWERS_02_python_syntax.md

## Python Syntax — Complete Answer Guide

Covers: Indentation, colons, comments, blocks, and basic structure.

---

## Indentation Rules

Python uses **indentation** (4 spaces) instead of `{}` curly braces to define code blocks.

```python
# C# style (does NOT work in Python):
# if (flag) { print("yes") }

# Python style:
if flag:
    print("yes")        # indented 4 spaces = inside the if block
    print("still yes")  # also inside
print("always runs")    # back to column 0 = outside the if block
```

### Gamertag example
```python
for tag in gamertags:
    if len(tag) > 0:              # 4 spaces in
        if tag[-1].isdigit():     # 8 spaces in
            print(f"  {tag}")     # 12 spaces in
```

---

## Colons

Every block header ends with a colon `:`:

```python
if condition:       # colon after if
    ...

for x in items:     # colon after for
    ...

while flag:         # colon after while
    ...

def my_function():  # colon after def
    ...

class MyClass:      # colon after class
    ...
```

---

## Comments

```python
# This is a single-line comment (like C# //)

# Multi-line is just multiple # comments
# There is no /* */ block comment in Python
# (There are triple-quoted strings used as docstrings, but they're not comments)

def load_gamertags(self):
    """This is a docstring — a string that documents the function."""
    pass
```

---

## No semicolons

```python
# WRONG (valid but bad style — not needed)
x = 5;
y = "DragonSlayer99";

# CORRECT
x = 5
y = "DragonSlayer99"
```

---

## Multiple statements on one line (avoid this)

```python
# WORKS but is bad style
x = 1; y = 2; z = 3

# BETTER — one statement per line
x = 1
y = 2
z = 3
```

---

## Line continuation

For long lines, use `\` to continue on the next line:

```python
# Long condition split across lines
if (len(tag) > 0
        and tag[-1].isdigit()
        and tag[0].isalnum()):
    print(tag)
```

---

## Case sensitivity

Python is **case-sensitive**:

```python
gamertag = "Dragon"
Gamertag = "Slayer"   # Different variable!
GAMERTAG = "Knight"   # Also different!

True    # boolean
true    # NameError! (not defined)
False   # boolean
false   # NameError! (not defined)
```

---

## Naming conventions (PEP 8 style guide)

| Type | Convention | Example |
|---|---|---|
| Variables | snake_case | `run_again`, `new_tag` |
| Functions/methods | snake_case | `load_gamertags()` |
| Classes | PascalCase | `Gamertags` |
| Constants | UPPER_SNAKE | `FILE_PATH` |
| Private (convention) | `_name` | `_helper_method()` |
