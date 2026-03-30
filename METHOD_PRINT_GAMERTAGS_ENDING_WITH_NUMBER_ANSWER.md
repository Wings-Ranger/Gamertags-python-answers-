# METHOD_PRINT_GAMERTAGS_ENDING_WITH_NUMBER_ANSWER.md

## Method: print_gamertags_ending_with_number

**Purpose:** Display only the gamertags whose last character is a digit (0–9).

> For full filter explanation and test cases, also see:
> [`FILTER_1_ENDING_WITH_NUMBER_ANSWER.md`](FILTER_1_ENDING_WITH_NUMBER_ANSWER.md)

---

## Complete Working Code

```python
def print_gamertags_ending_with_number(self):
    """Print only gamertags whose last character is a digit (0–9)."""
    print("\n--- GAMERTAGS ENDING WITH A NUMBER ---")
    found = False

    for tag in self.gamertags:
        if len(tag) > 0 and tag[-1].isdigit():
            print(f"  {tag}")
            found = True

    if not found:
        print("  (none found)")
    print()
```

---

## How it fits in the class

```python
class Gamertags:
    def __init__(self):
        self.gamertags = []

    def load_gamertags(self):
        # ... loads file into self.gamertags

    def print_gamertags_ending_with_number(self):
        # ← This method uses self.gamertags after load_gamertags has been called
        print("\n--- GAMERTAGS ENDING WITH A NUMBER ---")
        found = False
        for tag in self.gamertags:
            if len(tag) > 0 and tag[-1].isdigit():
                print(f"  {tag}")
                found = True
        if not found:
            print("  (none found)")
        print()
```

Call order in main():
```python
gt.load_gamertags()                          # must come first
gt.print_gamertags_ending_with_number()      # then this
```

---

## Key Python concepts used

| Concept | Code | Purpose |
|---|---|---|
| Iteration | `for tag in self.gamertags:` | Loop through every gamertag |
| Length check | `len(tag) > 0` | Avoid IndexError on empty strings |
| Negative index | `tag[-1]` | Access the last character |
| isdigit() | `tag[-1].isdigit()` | Check if it is 0–9 |
| Boolean flag | `found = False` | Track if anything was printed |
| f-string | `f"  {tag}"` | Format the output line |

---

## Example Output

With gamertags: `["DragonSlayer99", "xXNightHawkXx", "StarPilot7", "NeonWolf3", "CobraKing"]`

```
--- GAMERTAGS ENDING WITH A NUMBER ---
  DragonSlayer99
  StarPilot7
  NeonWolf3
```

With gamertags: `["CobraKing", "xXNightHawkXx"]`

```
--- GAMERTAGS ENDING WITH A NUMBER ---
  (none found)
```
