# ANSWERS_20_python_string_format.md

## Python String Formatting — Complete Answer Guide

---

## f-strings (Formatted String Literals) — PREFERRED

```python
# Basic f-string (Python 3.6+)
tag = "DragonSlayer99"
index = 1

print(f"  {index}. {tag}")          # "  1. DragonSlayer99"
print(f"Length: {len(tag)}")         # "Length: 14"
print(f"Last char: {tag[-1]}")       # "Last char: 9"
print(f"Ends with number: {tag[-1].isdigit()}")  # "Ends with number: True"
```

C# equivalent: `$"  {index}. {tag}"`

---

## Expressions in f-strings

```python
tag = "DragonSlayer99"

print(f"{tag.upper()}")              # "DRAGONSLAYER99"
print(f"{len(tag)} characters")      # "14 characters"
print(f"{2 + 2}")                    # "4"
print(f"{'yes' if True else 'no'}") # "yes"
```

---

## Formatting numbers

```python
number = 3.14159

print(f"{number:.2f}")      # "3.14"  — 2 decimal places
print(f"{42:05d}")           # "00042" — padded to 5 digits with leading zeros
print(f"{1000:,}")           # "1,000" — thousands separator
```

---

## .format() method (older style)

```python
tag = "DragonSlayer99"
index = 1

# Positional
print("  {}. {}".format(index, tag))    # "  1. DragonSlayer99"

# Named
print("  {i}. {t}".format(i=index, t=tag))
```

---

## String concatenation (oldest style — avoid for complex cases)

```python
tag = "DragonSlayer99"
index = 1

# WORKS but harder to read
print("  " + str(index) + ". " + tag)

# f-string is cleaner
print(f"  {index}. {tag}")
```

---

## Divider lines using string repetition

```python
print("=" * 40)    # ========================================
print("-" * 20)    # --------------------
print("*" * 10)    # **********
```

---

## center(), ljust(), rjust() for alignment

```python
title = "GAMERTAGS APP"

print(title.center(40))             # Centered in 40 characters
print(title.center(40, "="))        # ============GAMERTAGS APP=============
print(title.ljust(40, "-"))         # GAMERTAGS APP---------------------------
print(title.rjust(40, "-"))         # ---------------------------GAMERTAGS APP
```

---

## Gamertag output formatting examples

```python
gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]

# Numbered list
for i, tag in enumerate(gamertags, start=1):
    print(f"  {i}. {tag}")
# Output:
#   1. DragonSlayer99
#   2. StarPilot7
#   3. _CoolGamer_

# Aligned with padding
for i, tag in enumerate(gamertags, start=1):
    print(f"  {i:2}. {tag:<20}")   # right-align index, left-align tag in 20 chars
# Output:
#    1. DragonSlayer99
#    2. StarPilot7
#    3. _CoolGamer_

# Error message with file path
file_path = "/home/user/gamertags.txt"
print(f"  ERROR: Could not find '{file_path}'.")
```
