# ANSWERS_09_python_if_else.md

## Python if/elif/else — Complete Answer Guide

---

## Basic if/else

```python
tag = "_CoolGamer_"

if len(tag) > 0 and not tag[0].isalnum():
    print(f"Symbol start: {tag}")
else:
    print(f"Letter/digit start: {tag}")
# Output: Symbol start: _CoolGamer_
```

---

## if/elif/else

```python
answer = input("Choice (Y/N/Q): ").strip().upper()

if answer == "Y":
    print("Running again...")
    run_again = True
elif answer == "N":
    print("Goodbye!")
    run_again = False
elif answer == "Q":
    print("Quitting immediately!")
    run_again = False
else:
    print("Invalid choice — defaulting to stop")
    run_again = False
```

---

## Nested if

```python
for tag in gamertags:
    if len(tag) > 0:              # outer: check not empty
        if tag[-1].isdigit():     # inner: check last char
            print(f"  Ends with number: {tag}")
```

Equivalent (combined with `and`):
```python
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(f"  Ends with number: {tag}")
```

---

## One-line conditional (ternary expression)

```python
# C#: command = (os.name == "nt") ? "cls" : "clear";
command = "cls" if os.name == "nt" else "clear"

run_again = True if answer == "Y" else False
# Simplified:
run_again = (answer == "Y")
```

---

## if with truthiness

```python
# Check if list is not empty
if self.gamertags:
    for tag in self.gamertags:
        print(tag)
else:
    print("No gamertags loaded")

# Check if string is not empty
new_tag = input("Enter gamertag: ").strip()
if not new_tag:
    print("Nothing entered")
    return
```

---

## Gamertag filter examples

```python
gamertags = ["DragonSlayer99", "_CoolGamer_", "StarPilot7", "!Ghost", "CobraKing"]

print("Filter 1 (ends with number):")
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(f"  {tag}")

print("\nFilter 2 (symbol start):")
for tag in gamertags:
    if len(tag) > 0 and not tag[0].isalnum():
        print(f"  {tag}")
```

Output:
```
Filter 1 (ends with number):
  DragonSlayer99
  StarPilot7

Filter 2 (symbol start):
  _CoolGamer_
  !Ghost
```
