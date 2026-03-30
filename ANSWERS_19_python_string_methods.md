# ANSWERS_19_python_string_methods.md

## Python String Methods — Complete Answer Guide

All string methods relevant to the Gamertags project.

---

## Whitespace Handling

```python
tag = "  DragonSlayer99  "

tag.strip()     # "DragonSlayer99"       — both ends (C#: .Trim())
tag.lstrip()    # "DragonSlayer99  "     — left end only
tag.rstrip()    # "  DragonSlayer99"     — right end only
```

**Always use `.strip()` on:**
- User input from `input()`
- Lines read from files with `f.readlines()`

---

## Case Conversion

```python
tag = "DragonSlayer99"

tag.upper()    # "DRAGONSLAYER99"   (C#: .ToUpper())
tag.lower()    # "dragonslayer99"   (C#: .ToLower())
tag.title()    # "Dragonslayer99"   — first char of each word capitalised
tag.swapcase() # "dRAGONsLAYER99"  — toggle case
```

**Use in program:**
```python
answer = input("Run again? (Y/N): ").strip().upper()
if answer == "Y":
    run_again = True
```

---

## Checking Content

```python
tag = "DragonSlayer99"

tag.startswith("Dragon")   # True  (C#: .StartsWith())
tag.endswith("99")         # True  (C#: .EndsWith())
"Dragon" in tag            # True  (C#: .Contains())
tag.count("a")             # 1     — count occurrences
tag.find("Slayer")         # 6     — index of first match, -1 if not found
tag.index("Slayer")        # 6     — same but raises ValueError if not found
```

---

## Character Checks (called on single characters)

```python
c = "9"                # A single character

c.isdigit()            # True if 0–9
c.isalpha()            # True if a–z or A–Z
c.isalnum()            # True if letter or digit (a–z, A–Z, 0–9)
c.isspace()            # True if whitespace
c.isupper()            # True if uppercase letter
c.islower()            # True if lowercase letter

# For full string (all characters must match)
"hello".isalpha()      # True
"hello99".isalpha()    # False (has digits)
"hello99".isalnum()    # True (all alphanumeric)
"123".isdigit()        # True
```

---

## Replacing and Splitting

```python
tag = "Dragon Slayer 99"

tag.replace("Dragon", "Eagle")   # "Eagle Slayer 99"  (C#: .Replace())
tag.split(" ")                    # ["Dragon", "Slayer", "99"]
", ".join(["Dragon", "Slayer"])   # "Dragon, Slayer"   (C#: String.Join())
```

---

## Checking Empty String

```python
tag = ""

len(tag) == 0    # True
not tag          # True (empty string is falsy)
bool(tag)        # False

tag2 = "hello"
len(tag2) == 0   # False
not tag2         # False
bool(tag2)       # True
```

---

## All string methods used in the Gamertags program

```python
# In load_gamertags
line.strip()                          # Remove \n from file lines

# In show_welcome_message
"=" * 40                              # Repeat string

# In print_all_gamertags
f"  {i}. {tag}"                       # f-string formatting

# In filters
len(tag) > 0                          # Length check
tag[-1].isdigit()                     # Last char check
tag[0].isalnum()                      # First char check

# In main / add_new_username
input(...).strip().upper()            # Clean and normalise user input
answer == "Y"                         # String comparison
new_tag + "\n"                        # String concatenation
```
