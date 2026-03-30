# ANSWERS_05_python_strings.md

## Python Strings — Complete Answer Guide

Covers: String creation, indexing, methods, and all string operations used in the Gamertags project.

---

## Creating Strings

```python
tag1 = "DragonSlayer99"    # double quotes
tag2 = 'StarPilot7'        # single quotes — both work
tag3 = ""                   # empty string
multi = """This is a
multi-line string"""
```

---

## String Indexing

```python
tag = "DragonSlayer99"

tag[0]     # 'D'  — first character
tag[1]     # 'r'  — second character
tag[-1]    # '9'  — last character
tag[-2]    # '9'  — second-to-last

# Slicing (substring)
tag[0:6]   # 'Dragon'  (characters 0 through 5)
tag[6:]    # 'Slayer99' (from index 6 to end)
tag[:6]    # 'Dragon'  (from start to index 5)
```

---

## Essential String Methods

```python
tag = "  DragonSlayer99  "

tag.strip()          # "DragonSlayer99"        — remove whitespace (C#: .Trim())
tag.lstrip()         # "DragonSlayer99  "      — left only
tag.rstrip()         # "  DragonSlayer99"      — right only
tag.upper()          # "  DRAGONSLAYER99  "    — (C#: .ToUpper())
tag.lower()          # "  dragonslayer99  "    — (C#: .ToLower())
tag.replace("Dragon", "Eagle")  # Replace substring
tag.split(" ")       # Split by space into list
"," .join(["a","b"]) # "a,b" — join list into string

len(tag)             # 18 — total length including spaces

# Check contents
"Dragon" in tag      # True — contains substring (C#: .Contains())
tag.startswith("Dr") # True
tag.endswith("99")   # True
```

---

## Character Checks

```python
c = "9"     # A single-character string

c.isdigit()   # True if 0-9
c.isalpha()   # True if a-z or A-Z
c.isalnum()   # True if letter or digit (a-z, A-Z, 0-9)
c.isspace()   # True if whitespace (space, tab, newline)
c.isupper()   # True if all uppercase
c.islower()   # True if all lowercase
```

---

## f-strings (formatted string literals)

```python
tag = "DragonSlayer99"
count = 10
index = 1

# f-string (Python 3.6+) — like C# $"..."
print(f"  {index}. {tag}")           # "  1. DragonSlayer99"
print(f"Loaded {count} gamertags")   # "Loaded 10 gamertags"
print(f"First: {tag[0]}, Last: {tag[-1]}")  # "First: D, Last: 9"

# Expressions inside f-strings
print(f"Length: {len(tag)}")         # "Length: 14"
print(f"Ends with number: {tag[-1].isdigit()}")  # "Ends with number: True"
```

---

## String comparison

```python
# Python strings compare like C# strings
"Y" == "Y"      # True
"Y" == "y"      # False (case-sensitive)
"Y" == "y".upper()  # True (normalise first)

# After strip().upper() — safe comparison
answer = input("Run again? ").strip().upper()
if answer == "Y":
    run_again = True
```

---

## Gamertag filter examples using string methods

```python
gamertags = ["DragonSlayer99", "xXNightHawkXx", "_CoolGamer_", "StarPilot7"]

# Filter 1: ends with a number
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(tag)    # DragonSlayer99, StarPilot7

# Filter 2: doesn't start with letter or digit
for tag in gamertags:
    if len(tag) > 0 and not tag[0].isalnum():
        print(tag)    # _CoolGamer_
```

---

## String repetition (used for divider lines)

```python
print("=" * 40)    # ========================================
print("-" * 20)    # --------------------
```

---

## Multi-line strings for banners

```python
banner = """
========================================
       GAMERTAGS APP (Python)
========================================
"""
print(banner)
```
