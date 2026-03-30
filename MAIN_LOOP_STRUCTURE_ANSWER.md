# MAIN_LOOP_STRUCTURE_ANSWER.md

## Main Loop and Control Flow

**Purpose:** Understand how the Python `main()` function works, including the boolean flag, while loop, and run-again prompt.

---

## Complete Working Code

```python
def main():
    """Main program loop — runs the full app and asks to repeat."""
    gt = Gamertags()       # Create one Gamertags object
    run_again = True       # Boolean flag — starts True so loop runs at least once

    while run_again:
        # --- Step 1: Load data ---
        gt.load_gamertags()

        # --- Step 2: Welcome screen ---
        gt.show_welcome_message()

        # --- Step 3: Display all ---
        gt.print_all_gamertags()

        # --- Step 4: Filters ---
        gt.print_gamertags_ending_with_number()
        gt.print_gamertags_not_starting_with_letter_or_digit()

        # --- Step 5: Offer to add ---
        add_choice = input("Would you like to add a new gamertag? (Y/N): ").strip().upper()
        if add_choice == "Y":
            gt.add_new_username()

        # --- Step 6: Run again? ---
        again = input("\nRun again? (Y/N): ").strip().upper()
        run_again = (again == "Y")   # Only True if the user typed exactly "Y"

    print("\nThanks for using Gamertags App. Goodbye!")


if __name__ == "__main__":
    main()
```

---

## The Boolean Flag Pattern

### What is it?
A `bool` variable that controls how long a loop runs.
It is set to `True` to start, and set to `False` (or left True) based on user input each cycle.

### C# equivalent
```csharp
bool runAgain = true;
while (runAgain) {
    // ... do work ...
    Console.Write("Run again? (Y/N): ");
    string answer = Console.ReadLine().Trim().ToUpper();
    runAgain = (answer == "Y");
}
```

### Python equivalent
```python
run_again = True
while run_again:
    # ... do work ...
    again = input("Run again? (Y/N): ").strip().upper()
    run_again = (again == "Y")
```

These are **structurally identical**. Only the syntax differs.

---

## How `run_again = (again == "Y")` works

`(again == "Y")` is a comparison expression that produces `True` or `False`.

| User types | `again` | `again == "Y"` | `run_again` |
|---|---|---|---|
| `Y` | `"Y"` | `True` | `True` → loop again |
| `y` (after .upper()) | `"Y"` | `True` | `True` → loop again |
| `N` | `"N"` | `False` | `False` → stop |
| `n` (after .upper()) | `"N"` | `False` | `False` → stop |
| anything else | e.g. `"Q"` | `False` | `False` → stop |

The `.strip().upper()` chain ensures:
- `.strip()` — removes accidental spaces: `" Y "` → `"Y"`
- `.upper()` — normalises case: `"y"` → `"Y"`

This is the Python equivalent of C#'s `.Trim().ToUpper()`.

---

## Why call `load_gamertags()` inside the loop?

```python
while run_again:
    gt.load_gamertags()    # ← called at the START of each loop iteration
    ...
```

**Reason:** If the user adds a new gamertag in one run and then runs again,
the updated file is loaded fresh at the start of the next iteration.
This ensures the displayed list always reflects what's on disk.

Alternative (also valid): call it once before the loop:
```python
gt.load_gamertags()      # load once
while run_again:
    gt.show_welcome_message()
    gt.print_all_gamertags()
    ...
    # After add_new_username, reload is done inside that method
    again = input("Run again? (Y/N): ").strip().upper()
    if again == "Y":
        gt.load_gamertags()   # reload for next iteration
    run_again = (again == "Y")
```

The in-loop approach is simpler and less error-prone.

---

## `if __name__ == "__main__":` explained

```python
if __name__ == "__main__":
    main()
```

This is Python's equivalent of C#'s `static void Main()` entry point.

| Situation | `__name__` value | `main()` called? |
|---|---|---|
| You run `python COMPLETE_GAMERTAGS_PROGRAM.py` directly | `"__main__"` | ✅ YES |
| Another file does `import COMPLETE_GAMERTAGS_PROGRAM` | module name (not `"__main__"`) | ❌ NO |

This pattern is a Python convention. It allows the file to be both run directly
AND imported by other files without automatically executing `main()`.

---

## Complete program flow diagram

```
START
  │
  ▼
gt = Gamertags()
run_again = True
  │
  ▼
┌─────────────────────────────────────┐
│  while run_again:                   │
│                                     │
│  1. load_gamertags()                │
│  2. show_welcome_message()          │
│  3. print_all_gamertags()           │
│  4. print_gamertags_ending_...()    │
│  5. print_gamertags_not_start...()  │
│  6. add_choice = input(...)         │
│     if Y: add_new_username()        │
│  7. again = input("Run again?")     │
│     run_again = (again == "Y")      │
└─────────────────────────────────────┘
  │          │
  │ Yes      │ No
  └──────────┘
             │
             ▼
       "Goodbye!" message
             │
             ▼
            END
```

---

## Common Mistakes

### Mistake 1: Forgetting to call `load_gamertags()` at program start

```python
# WRONG — self.gamertags is still [] from __init__
while run_again:
    gt.show_welcome_message()
    gt.print_all_gamertags()   # prints "(no gamertags loaded)"
```

```python
# CORRECT
while run_again:
    gt.load_gamertags()        # always load first
    gt.show_welcome_message()
    ...
```

### Mistake 2: Using `input()` result directly without strip/upper

```python
# WRONG — "y " (with space) would not match "Y"
again = input("Run again? (Y/N): ")
run_again = (again == "Y")
```

```python
# CORRECT
again = input("Run again? (Y/N): ").strip().upper()
run_again = (again == "Y")
```

### Mistake 3: Using while True with no break

```python
# WORKS but harder to understand than the flag pattern
while True:
    ...
    again = input("Run again? (Y/N): ").strip().upper()
    if again != "Y":
        break
```

The boolean flag approach (`run_again = (again == "Y")`) is more readable and mirrors the C# version.

### Mistake 4: Not calling `if __name__ == "__main__":`

```python
# WORKS but is not best practice
main()
```

```python
# CORRECT — protects against accidental execution when imported
if __name__ == "__main__":
    main()
```
