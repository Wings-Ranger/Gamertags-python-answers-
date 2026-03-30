# METHOD_PRINT_GAMERTAGS_NOT_STARTING_WITH_LETTER_DIGIT_ANSWER.md

## Method: print_gamertags_not_starting_with_letter_or_digit

**Purpose:** Display only gamertags whose first character is NOT a letter (a–z, A–Z) or digit (0–9).

> For full filter explanation and test cases, also see:
> [`FILTER_2_NOT_STARTING_WITH_LETTER_DIGIT_ANSWER.md`](FILTER_2_NOT_STARTING_WITH_LETTER_DIGIT_ANSWER.md)

---

## Complete Working Code

```python
def print_gamertags_not_starting_with_letter_or_digit(self):
    """Print only gamertags whose first character is NOT a letter or digit."""
    print("\n--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---")
    found = False

    for tag in self.gamertags:
        if len(tag) > 0 and not tag[0].isalnum():
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

    def print_gamertags_not_starting_with_letter_or_digit(self):
        # ← This method uses self.gamertags after load_gamertags has been called
        print("\n--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---")
        found = False
        for tag in self.gamertags:
            if len(tag) > 0 and not tag[0].isalnum():
                print(f"  {tag}")
                found = True
        if not found:
            print("  (none found)")
        print()
```

---

## Key Python concepts used

| Concept | Code | Purpose |
|---|---|---|
| Iteration | `for tag in self.gamertags:` | Loop through every gamertag |
| Length check | `len(tag) > 0` | Avoid IndexError on empty strings |
| First character | `tag[0]` | Access the first character (index 0) |
| isalnum() | `tag[0].isalnum()` | True if letter OR digit |
| Logical NOT | `not tag[0].isalnum()` | Inverts — True if NOT letter/digit |
| Boolean flag | `found = False` | Track if anything was printed |
| f-string | `f"  {tag}"` | Format the output line |

---

## Example Output

With gamertags: `["DragonSlayer99", "_CoolGamer_", "!GhostHunter", "StarPilot7", ".ShadowBlade"]`

```
--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---
  _CoolGamer_
  !GhostHunter
  .ShadowBlade
```

With gamertags: `["DragonSlayer99", "StarPilot7", "CobraKing"]`

```
--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---
  (none found)
```

---

## C# equivalent

```csharp
public void PrintGamertagsNotStartingWithLetterOrDigit()
{
    Console.WriteLine("\n--- NOT STARTING WITH LETTER OR DIGIT ---");
    bool found = false;
    foreach (string tag in gamertags)
    {
        if (tag.Length > 0 && !char.IsLetterOrDigit(tag[0]))
        {
            Console.WriteLine(tag);
            found = true;
        }
    }
    if (!found)
        Console.WriteLine("  (none found)");
}
```

The Python version is nearly identical in structure — only the syntax differs.
