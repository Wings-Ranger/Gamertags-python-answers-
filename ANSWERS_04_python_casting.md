# ANSWERS_04_python_casting.md

## Python Type Casting — Complete Answer Guide

Covers: Converting between types, and why it matters for the Gamertags project.

---

## Type Conversion Functions

```python
# To string
str(42)          # "42"
str(True)        # "True"

# To integer
int("42")        # 42
int(3.9)         # 3 (truncates, does not round)

# To float
float("3.14")    # 3.14
float(5)         # 5.0

# To boolean
bool(0)          # False
bool(1)          # True
bool("")         # False (empty string)
bool("hello")    # True (non-empty string)
bool([])         # False (empty list)
bool(["a"])      # True (non-empty list)
```

---

## Where Casting Matters in the Gamertags Project

### `input()` always returns a string

```python
# input() ALWAYS returns a str, even if user types a number
answer = input("Run again? (Y/N): ")
print(type(answer))   # <class 'str'>

# So comparing to "Y" works correctly
if answer.strip().upper() == "Y":
    run_again = True
```

### Converting count to display

```python
count = len(self.gamertags)
print(f"Loaded {count} gamertags")   # f-string converts int automatically
print("Loaded " + str(count) + " gamertags")   # explicit conversion needed here
```

---

## Safe Type Conversion with try/except

```python
# What if the user types something unexpected?
raw = input("Enter a number: ")

try:
    number = int(raw)
    print(f"You entered: {number}")
except ValueError:
    print(f"'{raw}' is not a valid number.")
```

---

## Gamertag example: tag length as int

```python
tag = "DragonSlayer99"

length = len(tag)          # int: 14
length_str = str(length)   # str: "14"

print(f"Length: {length}")               # "Length: 14"
print("Length: " + str(length))          # Also works: "Length: 14"
print("Length: " + length)               # TypeError! Can't concatenate str + int
```

---

## Type checking (not casting)

```python
tag = "StarPilot7"

# Check what type something is
print(isinstance(tag, str))    # True
print(isinstance(tag, int))    # False

# In the filter — char is always a str (single-char string)
first_char = tag[0]            # 'S' — still a str, just length 1
print(type(first_char))        # <class 'str'>
first_char.isalnum()           # True — method works on single-char strings
```
