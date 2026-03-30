# IMPLEMENTATION_WALKTHROUGH.md

## Step-by-Step Implementation Walkthrough

A day-by-day guide to building the Python Gamertags program from scratch.
Mirrors the 14-day plan in the main repo's `TWO_WEEK_PYTHON_HOMEWORK_PLAN.md`.

---

## Day 1–7: Foundation Work (Theory Days)

Days 1–7 are for learning Python concepts. No full code yet.
By end of Day 7 you should be able to explain:
- How Python scripts run
- What a list is and how it differs from a C# array
- How `for` and `while` loops work
- How functions and classes are defined
- How file reading and writing work
- How string character checks work

See the `ANSWERS_01_` through `ANSWERS_24_` technique files for complete examples.

---

## Day 8: Project Skeleton

**Goal:** Create the file structure and class skeleton.

### What you should create

**File structure:**
```
my_gamertags_project/
├── gamertags.txt          ← your list of names
└── gamertags_program.py   ← your Python code
```

**gamertags.txt contents (create this first):**
```
DragonSlayer99
xXNightHawkXx
_CoolGamer_
StarPilot7
!GhostHunter
NeonWolf3
.ShadowBlade
CobraKing
ProPlayer1
ZeroHour
```

**gamertags_program.py skeleton:**
```python
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")


class Gamertags:
    def __init__(self):
        self.gamertags = []

    def load_gamertags(self):
        pass   # TODO Day 9

    def show_welcome_message(self):
        pass   # TODO Day 9

    def print_all_gamertags(self):
        pass   # TODO Day 10

    def print_gamertags_ending_with_number(self):
        pass   # TODO Day 11

    def print_gamertags_not_starting_with_letter_or_digit(self):
        pass   # TODO Day 12

    def add_new_username(self):
        pass   # TODO Day 13


def main():
    gt = Gamertags()
    run_again = True
    while run_again:
        gt.load_gamertags()
        gt.show_welcome_message()
        gt.print_all_gamertags()
        gt.print_gamertags_ending_with_number()
        gt.print_gamertags_not_starting_with_letter_or_digit()
        add_choice = input("Add new gamertag? (Y/N): ").strip().upper()
        if add_choice == "Y":
            gt.add_new_username()
        again = input("\nRun again? (Y/N): ").strip().upper()
        run_again = (again == "Y")
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
```

**Day 8 checkpoint:** Run the skeleton — it should start, ask "Add new gamertag?" and "Run again?" without crashing. (All methods just `pass` so nothing is displayed yet.)

---

## Day 9: Data Loading and Welcome Sequence

**Goal:** Implement `load_gamertags()` and `show_welcome_message()`.

### Step 1: Implement `load_gamertags`

Replace `pass` in `load_gamertags` with:

```python
def load_gamertags(self):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"  ERROR: Could not find '{FILE_PATH}'.")
        self.gamertags = []
```

### Step 2: Implement `show_welcome_message`

```python
def show_welcome_message(self):
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass
    print("=" * 40)
    print("       GAMERTAGS APP (Python)")
    print("=" * 40)
    print()
```

**Day 9 verification:** Run the program. You should see the welcome banner and the app should not crash. `print_all_gamertags` still shows nothing (it's `pass`).

To confirm data loaded, temporarily add:
```python
print(f"Loaded {len(self.gamertags)} gamertags")
```
after `self.gamertags = [...]` — you should see "Loaded 10 gamertags". Remove it after checking.

---

## Day 10: Display All Gamertags

**Goal:** Implement `print_all_gamertags()`.

Replace `pass` with:

```python
def print_all_gamertags(self):
    print("\n--- ALL GAMERTAGS ---")
    if not self.gamertags:
        print("  (no gamertags loaded)")
        return
    for i, tag in enumerate(self.gamertags, start=1):
        print(f"  {i}. {tag}")
    print()
```

**Day 10 verification:** Run the program. You should see all 10 gamertags numbered 1–10.

---

## Day 11: Filter 1 — Ending With a Number

**Goal:** Implement `print_gamertags_ending_with_number()`.

Replace `pass` with:

```python
def print_gamertags_ending_with_number(self):
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

**Day 11 verification:** Run the program. You should see:
```
--- GAMERTAGS ENDING WITH A NUMBER ---
  DragonSlayer99
  StarPilot7
  NeonWolf3
  ProPlayer1
```

---

## Day 12: Filter 2 — Not Starting With Letter or Digit

**Goal:** Implement `print_gamertags_not_starting_with_letter_or_digit()`.

Replace `pass` with:

```python
def print_gamertags_not_starting_with_letter_or_digit(self):
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

**Day 12 verification:** Run the program. You should see:
```
--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---
  _CoolGamer_
  !GhostHunter
  .ShadowBlade
```

---

## Day 13: Add New Gamertag and Run-Again Loop

**Goal:** Implement `add_new_username()` and verify the run-again loop works.

Replace `pass` in `add_new_username` with:

```python
def add_new_username(self):
    print("\n--- ADD NEW GAMERTAG ---")
    new_tag = input("  Enter new gamertag: ").strip()
    if not new_tag:
        print("  (no name entered — nothing saved)")
        return
    try:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(new_tag + "\n")
        print(f"  '{new_tag}' saved successfully!")
        self.load_gamertags()
    except IOError as e:
        print(f"  ERROR: Could not write to file. {e}")
```

**Day 13 verification:**
1. Run the program.
2. When asked "Add new gamertag?", type `Y`.
3. Type a new gamertag (e.g., `NightOwl42`).
4. When asked "Run again?", type `Y`.
5. The new gamertag should now appear in the numbered list.
6. Check `gamertags.txt` — the new entry should be at the bottom.

---

## Day 14: Final Testing and Polish

**Goal:** Verify everything works together and handle edge cases.

### Final checklist

- [ ] Run the program fresh — all 10 gamertags load and display
- [ ] Filter 1 shows exactly: DragonSlayer99, StarPilot7, NeonWolf3, ProPlayer1
- [ ] Filter 2 shows exactly: _CoolGamer_, !GhostHunter, .ShadowBlade
- [ ] Add a new gamertag — it appears on the next run
- [ ] Type `y` (lowercase) at run-again prompt — program loops
- [ ] Type `N` at run-again prompt — program exits with "Goodbye!" message
- [ ] Press Enter without typing at add-gamertag prompt — nothing is saved
- [ ] Delete gamertags.txt and run — error message shows, no crash
- [ ] Empty gamertags.txt and run — "(no gamertags loaded)" shows

### Complete, working Day 14 code

Your completed code should match `COMPLETE_GAMERTAGS_PROGRAM.py` exactly.
Compare yours to that file and fix any differences.

---

## What Each Day Produces

| Day | What's new |
|---|---|
| 8 | Project structure, skeleton class, main loop (all `pass`) |
| 9 | Welcome banner displays, data loads from file |
| 10 | All gamertags listed and numbered |
| 11 | Filter 1 working |
| 12 | Filter 2 working |
| 13 | Add/save feature working, run-again loop verified |
| 14 | All edge cases handled, code clean and tested |
