# ANSWERS_11_python_for_loops.md

## Python For Loops — Complete Answer Guide

---

## Basic For Loop (like C# foreach)

```python
gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]

# C#: foreach (string tag in gamertags) { Console.WriteLine(tag); }
for tag in gamertags:
    print(tag)
# Output: DragonSlayer99, StarPilot7, _CoolGamer_
```

---

## For Loop with Index — enumerate()

```python
gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]

# Start numbering at 1 (not 0)
for i, tag in enumerate(gamertags, start=1):
    print(f"  {i}. {tag}")
# Output:
#   1. DragonSlayer99
#   2. StarPilot7
#   3. _CoolGamer_
```

C# equivalent:
```csharp
for (int i = 0; i < gamertags.Length; i++) {
    Console.WriteLine($"{i + 1}. {gamertags[i]}");
}
```

---

## For Loop with range()

```python
# range(n) produces 0, 1, 2, ..., n-1
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# range(start, stop) — start to stop-1
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)   # 0, 2, 4, 6, 8
```

---

## For Loop with Condition

```python
gamertags = ["DragonSlayer99", "xXNightHawkXx", "StarPilot7", "_CoolGamer_"]

# Filter: only process gamertags ending with a number
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(f"  {tag}")
# Output: DragonSlayer99, StarPilot7
```

---

## Nested For Loops

```python
# Loop through each tag, then each character
for tag in gamertags:
    print(f"\n{tag}:")
    for char in tag:
        print(f"  {char}")
```

---

## For Loop vs While Loop — when to use each

| Use `for` when | Use `while` when |
|---|---|
| Iterating over a known list/sequence | Repeating until a condition changes |
| Fixed number of iterations | Unknown number of iterations |
| `for tag in gamertags:` | `while run_again:` |

In this project:
- `for tag in self.gamertags:` — iterate the list
- `while run_again:` — keep running until user stops

---

## break and continue

```python
# break — exit the loop immediately
for tag in gamertags:
    if tag == "StopHere":
        break
    print(tag)

# continue — skip the rest of this iteration, move to next
for tag in gamertags:
    if len(tag) == 0:
        continue    # skip empty strings
    print(f"  {tag[-1].isdigit()}: {tag}")
```

---

## List comprehension (compact for loop)

```python
# Standard for loop
result = []
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        result.append(tag)

# Equivalent list comprehension (one line)
result = [tag for tag in gamertags if len(tag) > 0 and tag[-1].isdigit()]
```
