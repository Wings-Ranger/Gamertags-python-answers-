# ANSWERS_13_python_lambda.md

## Python Lambda Expressions — Complete Answer Guide

---

## What is a Lambda?

A lambda is a small, anonymous function defined in one line.

```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2

# Same result
print(double(5))   # 10
```

---

## Lambda Syntax

```python
lambda parameters: expression
# No 'return' keyword — the expression is automatically returned
```

---

## Lambda with sort/filter/map

```python
gamertags = ["DragonSlayer99", "xXNightHawkXx", "_CoolGamer_", "StarPilot7"]

# Sort by length (shortest first)
sorted_tags = sorted(gamertags, key=lambda tag: len(tag))
print(sorted_tags)
# ['StarPilot7', '_CoolGamer_', 'xXNightHawkXx', 'DragonSlayer99']

# filter() — keep only items where function returns True
number_enders = list(filter(lambda tag: len(tag) > 0 and tag[-1].isdigit(), gamertags))
print(number_enders)
# ['DragonSlayer99', 'StarPilot7']

# map() — transform each item
uppercased = list(map(lambda tag: tag.upper(), gamertags))
print(uppercased)
# ['DRAGONSLAYER99', 'XXNIGHTHAWKXX', '_COOLGAMER_', 'STARTPILOT7']
```

---

## Lambda vs List Comprehension

For the Gamertags project, list comprehensions are cleaner and preferred over lambdas:

```python
# Lambda with filter()
result = list(filter(lambda tag: len(tag) > 0 and tag[-1].isdigit(), gamertags))

# Equivalent list comprehension (preferred)
result = [tag for tag in gamertags if len(tag) > 0 and tag[-1].isdigit()]
```

---

## When to use lambdas

Use lambdas when:
- Passing a simple function as an argument (e.g., `sorted(key=...`)
- The function is only used once

Use regular `def` functions when:
- The function is more than one expression
- The function is reused in multiple places
- Readability is a priority

---

## Gamertag examples with lambda

```python
gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_", "NightOwl42", "CobraKing"]

# Sort alphabetically
print(sorted(gamertags))

# Sort by last character
print(sorted(gamertags, key=lambda t: t[-1] if t else ""))

# Find first tag ending with a number
first_match = next((t for t in gamertags if len(t) > 0 and t[-1].isdigit()), None)
print(first_match)   # "DragonSlayer99"
```
