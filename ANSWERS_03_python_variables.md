# ANSWERS_03_python_variables.md

## Python Variables — Complete Answer Guide

Covers: Variable declaration, types, naming, and scope basics.

---

## Declaring Variables

Python does NOT need type declarations. Just assign a value:

```python
# C# requires type:
# string name = "DragonSlayer99";
# int count = 10;
# bool flag = true;

# Python — just assign:
name = "DragonSlayer99"
count = 10
flag = True
```

---

## Core Data Types

```python
# String (text)
gamertag = "StarPilot7"
print(type(gamertag))    # <class 'str'>

# Integer
player_count = 10
print(type(player_count))  # <class 'int'>

# Boolean
run_again = True
run_again = False
print(type(run_again))   # <class 'bool'>

# List (equivalent to C# array or List<string>)
gamertags = ["DragonSlayer99", "StarPilot7", "CobraKing"]
print(type(gamertags))   # <class 'list'>

# None (equivalent to C# null)
result = None
print(type(result))      # <class 'NoneType'>
```

---

## Variables in the Gamertags Program

```python
# In main():
run_again = True           # bool — controls the while loop
gt = Gamertags()           # object — instance of the Gamertags class

# In Gamertags.__init__():
self.gamertags = []        # list — stores the loaded names

# In load_gamertags():
FILE_PATH = "..."          # str — path to the file

# In add_new_username():
new_tag = input(...).strip()  # str — the user's input

# In filters:
found = False              # bool — track if anything was printed
```

---

## Dynamic Typing

Variables can be reassigned to different types (unlike C#):

```python
x = 5          # int
x = "hello"    # now str — no error in Python
x = True       # now bool — still no error
```

This is a Python feature. Use it carefully — it can make bugs harder to spot.

---

## Constants (by convention)

Python doesn't have a built-in `const` keyword like C#.
Use ALL_CAPS names to signal a constant:

```python
FILE_PATH = "gamertags.txt"     # Treat as constant — don't reassign
MAX_TAGS = 1000                 # Treat as constant
```

---

## Checking a Variable's Type

```python
tag = "DragonSlayer99"

print(type(tag))              # <class 'str'>
print(isinstance(tag, str))   # True
print(isinstance(tag, int))   # False
```

---

## Gamertag examples

```python
# Single gamertag
tag = "DragonSlayer99"
print(f"Tag: {tag}")
print(f"Length: {len(tag)}")
print(f"First char: {tag[0]}")
print(f"Last char: {tag[-1]}")
print(f"Ends with number: {tag[-1].isdigit()}")

# Output:
# Tag: DragonSlayer99
# Length: 14
# First char: D
# Last char: 9
# Ends with number: True
```
