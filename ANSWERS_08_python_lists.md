# ANSWERS_08_python_lists.md

## Python Lists — Complete Answer Guide

Covers: Creating lists, accessing items, modifying, and iterating.

---

## Creating Lists

```python
# Empty list (C#: new List<string>() or string[])
gamertags = []

# List with values
gamertags = ["DragonSlayer99", "StarPilot7", "CobraKing"]

# List from file reading
gamertags = [line.strip() for line in f.readlines() if line.strip()]
```

---

## Accessing Items

```python
gamertags = ["DragonSlayer99", "StarPilot7", "CobraKing"]

gamertags[0]     # "DragonSlayer99" — first item (index 0)
gamertags[1]     # "StarPilot7"
gamertags[-1]    # "CobraKing" — last item
gamertags[-2]    # "StarPilot7" — second-to-last

len(gamertags)   # 3 — number of items (C#: gamertags.Length)
```

---

## Modifying Lists

```python
gamertags = ["DragonSlayer99", "StarPilot7"]

# Add to end (C#: List.Add())
gamertags.append("NightOwl42")
# ["DragonSlayer99", "StarPilot7", "NightOwl42"]

# Remove by value
gamertags.remove("StarPilot7")
# ["DragonSlayer99", "NightOwl42"]

# Replace item
gamertags[0] = "ProGamer99"
# ["ProGamer99", "NightOwl42"]

# Clear all items
gamertags.clear()   # or: gamertags = []
```

---

## Checking List Contents

```python
gamertags = ["DragonSlayer99", "StarPilot7", "CobraKing"]

# Is something in the list?
"StarPilot7" in gamertags       # True (C#: gamertags.Contains())
"NightOwl" in gamertags         # False

# Is the list empty?
len(gamertags) == 0             # True if empty
not gamertags                   # True if empty (Pythonic)
bool(gamertags)                 # False if empty, True if has items
```

---

## Iterating Lists

```python
gamertags = ["DragonSlayer99", "StarPilot7", "_CoolGamer_"]

# Simple iteration (C#: foreach)
for tag in gamertags:
    print(tag)

# With index, starting at 1 (C#: for loop with i)
for i, tag in enumerate(gamertags, start=1):
    print(f"  {i}. {tag}")
# Output:
#   1. DragonSlayer99
#   2. StarPilot7
#   3. _CoolGamer_

# With condition
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        print(tag)
# Output: DragonSlayer99, StarPilot7
```

---

## List Comprehensions

```python
gamertags = ["DragonSlayer99", "xXNightHawkXx", "StarPilot7", "_CoolGamer_"]

# Create new list from existing (with filter)
number_enders = [tag for tag in gamertags if len(tag) > 0 and tag[-1].isdigit()]
# ["DragonSlayer99", "StarPilot7"]

symbol_starters = [tag for tag in gamertags if len(tag) > 0 and not tag[0].isalnum()]
# ["_CoolGamer_"]

# Same as:
number_enders = []
for tag in gamertags:
    if len(tag) > 0 and tag[-1].isdigit():
        number_enders.append(tag)
```

---

## Lists vs C# Arrays

| Feature | C# `string[]` | C# `List<string>` | Python `list` |
|---|---|---|---|
| Fixed size? | Yes | No | No |
| Add items | No | `list.Add()` | `list.append()` |
| Length | `array.Length` | `list.Count` | `len(list)` |
| Access by index | `array[i]` | `list[i]` | `list[i]` |
| Last item | `array[array.Length-1]` | `list[list.Count-1]` | `list[-1]` |
| Iterate | `foreach (var x in array)` | `foreach (var x in list)` | `for x in list:` |
| Empty check | `array.Length == 0` | `list.Count == 0` | `not list` or `len(list) == 0` |

Python lists are dynamic — like C# `List<string>`, not `string[]`.
