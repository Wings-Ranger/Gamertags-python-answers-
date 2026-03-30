# STRING_VALIDATION_ANSWERS.md

## String Validation in Python — Complete Guide

All the string and character checks needed for the Gamertags project,
with examples, comparisons to C#, and complete validation functions.

---

## 1. Checking String Length Safely

### The problem
Accessing `tag[0]` or `tag[-1]` on an empty string causes:
```
IndexError: string index out of range
```

### The solution — always check length first

```python
# Pattern: check length before indexing
if len(tag) > 0 and tag[-1].isdigit():
    ...

# Pythonic shorthand — empty string is falsy
if tag and tag[-1].isdigit():
    ...
```

Both are equivalent. `if tag:` is `True` when tag has at least one character.
`if len(tag) > 0:` is more explicit and preferred for beginners.

---

## 2. Accessing First and Last Characters

```python
tag = "DragonSlayer99"

first = tag[0]    # 'D'  — index 0 = first character
last = tag[-1]    # '9'  — index -1 = last character

# C# equivalents:
# tag[0]              → tag[0]          (same!)
# tag[tag.Length - 1] → tag[-1]         (Python is shorter)
```

### Negative indexing explained

| Python index | Position |
|---|---|
| `tag[0]` | First character |
| `tag[1]` | Second character |
| `tag[-1]` | Last character |
| `tag[-2]` | Second-to-last |

```python
word = "Hello"
print(word[0])   # H
print(word[-1])  # o
print(word[-2])  # l
```

---

## 3. isdigit() vs isnumeric() vs isdecimal()

| Method | Matches | Use for gamertags? |
|---|---|---|
| `.isdigit()` | `0`–`9` only | ✅ YES — matches C# `char.IsDigit()` |
| `.isdecimal()` | `0`–`9` only (stricter than isdigit for some edge cases) | ✅ Also works |
| `.isnumeric()` | `0`–`9` PLUS fractions (½) and superscripts (²) | ❌ Too broad |

**Always use `.isdigit()` for the "ending with a number" filter.**

```python
print('9'.isdigit())    # True
print('²'.isdigit())    # True  ← superscript! (same as isnumeric here)
print('½'.isdigit())    # False ← fraction (isdigit is stricter than isnumeric for fractions)
print('a'.isdigit())    # False
```

For the gamertag filter, `'²'` should NOT be considered a "number" ending.
To be perfectly strict:
```python
tag[-1] in "0123456789"   # Most explicit — only ASCII digits
```
But `.isdigit()` is the standard idiomatic choice and matches C# behavior closely enough.

---

## 4. isalpha() vs isalnum()

| Method | Matches | C# equivalent |
|---|---|---|
| `.isalpha()` | Letters only (a–z, A–Z) | `char.IsLetter()` |
| `.isalnum()` | Letters AND digits (a–z, A–Z, 0–9) | `char.IsLetterOrDigit()` |
| `.isdigit()` | Digits only (0–9) | `char.IsDigit()` |

```python
print('A'.isalpha())    # True
print('3'.isalpha())    # False

print('A'.isalnum())    # True
print('3'.isalnum())    # True
print('_'.isalnum())    # False  ← underscore is NOT alphanumeric
print('!'.isalnum())    # False
```

**For filter 2, use `.isalnum()` because the rule is "not starting with a letter OR digit".**

```python
# These should be EXCLUDED (start with letter or digit)
"DragonSlayer99"[0].isalnum()   # True  → skip
"1stPlace"[0].isalnum()         # True  → skip

# These should be INCLUDED (start with symbol)
"_CoolGamer_"[0].isalnum()      # False → show
"!GhostHunter"[0].isalnum()     # False → show
".ShadowBlade"[0].isalnum()     # False → show
```

---

## 5. Complete Validation Functions

### Check if a gamertag ends with a number

```python
def ends_with_number(tag: str) -> bool:
    """Return True if tag is non-empty and its last character is a digit."""
    return len(tag) > 0 and tag[-1].isdigit()


# Usage
print(ends_with_number("DragonSlayer99"))   # True
print(ends_with_number("CobraKing"))        # False
print(ends_with_number(""))                 # False (safe — no crash)
print(ends_with_number("7"))                # True (single digit)
```

### Check if a gamertag does NOT start with a letter or digit

```python
def starts_with_symbol(tag: str) -> bool:
    """Return True if tag is non-empty and its first character is NOT a letter or digit."""
    return len(tag) > 0 and not tag[0].isalnum()


# Usage
print(starts_with_symbol("_CoolGamer_"))    # True
print(starts_with_symbol("!GhostHunter"))   # True
print(starts_with_symbol("DragonSlayer"))   # False
print(starts_with_symbol("1stPlace"))       # False (digit → alnum)
print(starts_with_symbol(""))               # False (safe — no crash)
```

---

## 6. Handling Unusual Input Safely

```python
# All of these should NOT crash the program:
edge_cases = [
    "",            # empty string
    " ",           # space only
    "\t",          # tab only
    "A",           # single letter
    "9",           # single digit
    "_",           # single symbol
    "  hello  ",   # padded with spaces
]

for tag in edge_cases:
    stripped = tag.strip()
    if len(stripped) > 0 and stripped[-1].isdigit():
        print(f"Ends with number: {repr(tag)}")
    elif len(stripped) > 0 and not stripped[0].isalnum():
        print(f"Starts with symbol: {repr(tag)}")
    else:
        print(f"Neither filter: {repr(tag)}")
```

**Note:** In the gamertags file, blank lines are skipped during `load_gamertags()`,
so you should never encounter empty strings in `self.gamertags`. The length check is still
a good defensive practice.

---

## 7. Quick Summary Table

| What you want to check | Python code | C# equivalent |
|---|---|---|
| String is not empty | `len(tag) > 0` or `if tag:` | `tag.Length > 0` |
| First character | `tag[0]` | `tag[0]` |
| Last character | `tag[-1]` | `tag[tag.Length - 1]` |
| Is a digit? | `c.isdigit()` | `char.IsDigit(c)` |
| Is a letter? | `c.isalpha()` | `char.IsLetter(c)` |
| Is letter or digit? | `c.isalnum()` | `char.IsLetterOrDigit(c)` |
| NOT letter or digit | `not c.isalnum()` | `!char.IsLetterOrDigit(c)` |
| Remove whitespace | `tag.strip()` | `tag.Trim()` |
| To uppercase | `tag.upper()` | `tag.ToUpper()` |
| To lowercase | `tag.lower()` | `tag.ToLower()` |
| Contains a substring | `"sub" in tag` | `tag.Contains("sub")` |
| String length | `len(tag)` | `tag.Length` |
