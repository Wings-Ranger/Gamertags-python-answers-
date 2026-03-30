# ANSWERS_06_python_booleans.md

## Python Booleans — Complete Answer Guide

Covers: True/False, boolean expressions, truthy/falsy values.

---

## Boolean Basics

```python
run_again = True       # C#: bool runAgain = true;
found = False          # C#: bool found = false;

print(type(run_again))  # <class 'bool'>
```

**Important:** Python uses `True` and `False` with capital letters.
`true` and `false` (lowercase) are NOT defined and will raise `NameError`.

---

## Boolean Operators

```python
# and (C#: &&)
True and True    # True
True and False   # False
False and True   # False

# or (C#: ||)
True or False    # True
False or False   # False

# not (C#: !)
not True         # False
not False        # True
```

---

## Boolean Expressions in the Gamertags Program

```python
# run-again flag
run_again = (answer == "Y")          # True or False based on comparison

# Length AND character check (both must be true)
len(tag) > 0 and tag[-1].isdigit()  # True only if tag is non-empty AND last char is digit

# NOT operator for filter 2
not tag[0].isalnum()                 # True if first char is NOT a letter or digit

# Empty check
not self.gamertags                   # True when list is empty
```

---

## Truthy and Falsy Values

In Python, many values are automatically treated as `True` or `False` in conditions.

```python
# FALSY values (treated as False):
bool(False)     # False
bool(0)         # False
bool("")        # False — empty string
bool([])        # False — empty list
bool(None)      # False

# TRUTHY values (treated as True):
bool(True)      # True
bool(1)         # True
bool("hello")   # True — non-empty string
bool(["a"])     # True — non-empty list
bool(-1)        # True — any non-zero number
```

### Practical use in the Gamertags program

```python
# Check if list is empty
if not self.gamertags:
    print("  (no gamertags loaded)")
    return

# Check if string is empty
if not new_tag:
    print("  (nothing entered)")
    return

# These are equivalent to:
if len(self.gamertags) == 0:
    ...
if len(new_tag) == 0:
    ...
```

---

## Short-circuit evaluation

```python
# Python evaluates 'and' left-to-right and stops early
# This is why the length check must come BEFORE the character access

# Safe: if len is 0, Python never evaluates tag[-1] (which would crash)
if len(tag) > 0 and tag[-1].isdigit():
    print(tag)

# WRONG: tag[-1] could crash before len() check is even evaluated
if tag[-1].isdigit() and len(tag) > 0:
    print(tag)
```

---

## Comparison operators that produce booleans

```python
x = 5
x == 5     # True  — equal
x != 3     # True  — not equal
x > 3      # True  — greater than
x < 10     # True  — less than
x >= 5     # True  — greater or equal
x <= 5     # True  — less or equal

"Y" == "Y"          # True
answer == "Y"       # True or False depending on answer
run_again = (answer.strip().upper() == "Y")   # Boolean assignment
```
