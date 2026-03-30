# ANSWERS_07_python_operators.md

## Python Operators — Complete Answer Guide

Covers: Arithmetic, comparison, logical, string, and membership operators.

---

## Comparison Operators

```python
# == equal
"Y" == "Y"          # True
"Y" == "y"          # False (case-sensitive)

# != not equal
"N" != "Y"          # True

# < > <= >=
len(tag) > 0        # True if tag has characters
count >= 10         # True if count is 10 or more
```

---

## Logical Operators

```python
# and — both must be True (C#: &&)
len(tag) > 0 and tag[-1].isdigit()

# or — at least one must be True (C#: ||)
answer == "Y" or answer == "YES"

# not — inverts True/False (C#: !)
not tag[0].isalnum()    # True if NOT alphanumeric
not self.gamertags      # True if list is empty
```

---

## Arithmetic Operators

```python
10 + 3    # 13
10 - 3    # 7
10 * 3    # 30
10 / 3    # 3.333...  (float division)
10 // 3   # 3         (integer division, C#: 10 / 3 for ints)
10 % 3    # 1         (remainder/modulo, C#: 10 % 3)
2 ** 3    # 8         (power, C#: Math.Pow(2,3))
```

---

## String Operators

```python
# Concatenation
"Hello" + " " + "World"    # "Hello World" (C#: + operator)

# Repetition
"=" * 40                    # "======...=" (40 equals signs)
"-" * 20                    # "---...---"

# Membership
"Dragon" in "DragonSlayer"  # True (C#: .Contains())
"xyz" not in "DragonSlayer" # True
```

---

## Assignment Operators

```python
count = 0        # assign
count += 1       # count = count + 1
count -= 1       # count = count - 1
count *= 2       # count = count * 2

run_again = True
run_again = (answer == "Y")   # assign result of comparison
```

---

## Identity Operators

```python
x = None

x is None       # True — check if x is exactly None (C#: x == null)
x is not None   # False
```

---

## Operator precedence (simplified)

From highest to lowest priority:
1. `()` — parentheses
2. `**` — power
3. `*`, `/`, `//`, `%` — multiply/divide
4. `+`, `-` — add/subtract
5. `<`, `>`, `<=`, `>=`, `==`, `!=` — comparisons
6. `not` — logical not
7. `and` — logical and
8. `or` — logical or

```python
# Always use parentheses for clarity
if (len(tag) > 0) and (tag[-1].isdigit()):
    print(tag)
# Same as:
if len(tag) > 0 and tag[-1].isdigit():
    print(tag)
```

---

## Gamertag operator examples

```python
tag = "DragonSlayer99"

# Length check
print(len(tag) > 0)                  # True

# Last character
print(tag[-1] == "9")                # True
print(tag[-1].isdigit())             # True

# Combined for filter 1
print(len(tag) > 0 and tag[-1].isdigit())    # True

# First character
print(tag[0] == "D")                 # True
print(tag[0].isalnum())              # True
print(not tag[0].isalnum())          # False

# Combined for filter 2
print(len(tag) > 0 and not tag[0].isalnum())  # False (D is alphanumeric)

# Test with a symbol-start tag
tag2 = "_CoolGamer_"
print(len(tag2) > 0 and not tag2[0].isalnum())  # True
```
