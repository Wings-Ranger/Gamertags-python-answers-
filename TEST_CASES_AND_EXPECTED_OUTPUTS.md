# TEST_CASES_AND_EXPECTED_OUTPUTS.md

## Test Cases and Expected Outputs

Use this file to verify your Python solution produces the correct output
for every feature of the Gamertags app.

---

## Sample gamertags.txt

Create this file in the same directory as your Python script before testing:

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

---

## Test 1: Load Gamertags

**Action:** Run the program.  
**Expected:** `self.gamertags` contains exactly these 10 items (no blank lines, no `\n` characters):

```
["DragonSlayer99", "xXNightHawkXx", "_CoolGamer_", "StarPilot7",
 "!GhostHunter", "NeonWolf3", ".ShadowBlade", "CobraKing", "ProPlayer1", "ZeroHour"]
```

**Verify with:**
```python
# Add this temporarily to load_gamertags after loading:
print(len(self.gamertags))          # Should print: 10
print(repr(self.gamertags[0]))      # Should print: 'DragonSlayer99' (no \n)
```

---

## Test 2: Print All Gamertags

**Expected output:**
```
--- ALL GAMERTAGS ---
  1. DragonSlayer99
  2. xXNightHawkXx
  3. _CoolGamer_
  4. StarPilot7
  5. !GhostHunter
  6. NeonWolf3
  7. .ShadowBlade
  8. CobraKing
  9. ProPlayer1
  10. ZeroHour
```

**Check:**
- Numbered starting from 1 (not 0)
- Each gamertag on its own line
- No extra whitespace around names

---

## Test 3: Filter 1 — Gamertags Ending With a Number

**Expected output:**
```
--- GAMERTAGS ENDING WITH A NUMBER ---
  DragonSlayer99
  StarPilot7
  NeonWolf3
  ProPlayer1
```

**Why these?**
- `DragonSlayer99` — ends with `9` ✅
- `xXNightHawkXx` — ends with `x` ❌
- `_CoolGamer_` — ends with `_` ❌
- `StarPilot7` — ends with `7` ✅
- `!GhostHunter` — ends with `r` ❌
- `NeonWolf3` — ends with `3` ✅
- `.ShadowBlade` — ends with `e` ❌
- `CobraKing` — ends with `g` ❌
- `ProPlayer1` — ends with `1` ✅
- `ZeroHour` — ends with `r` ❌

---

## Test 4: Filter 2 — Gamertags NOT Starting With Letter or Digit

**Expected output:**
```
--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---
  _CoolGamer_
  !GhostHunter
  .ShadowBlade
```

**Why these?**
- `DragonSlayer99` — starts with `D` (letter) ❌
- `xXNightHawkXx` — starts with `x` (letter) ❌
- `_CoolGamer_` — starts with `_` (symbol) ✅
- `StarPilot7` — starts with `S` (letter) ❌
- `!GhostHunter` — starts with `!` (symbol) ✅
- `NeonWolf3` — starts with `N` (letter) ❌
- `.ShadowBlade` — starts with `.` (symbol) ✅
- `CobraKing` — starts with `C` (letter) ❌
- `ProPlayer1` — starts with `P` (letter) ❌
- `ZeroHour` — starts with `Z` (letter) ❌

---

## Test 5: Add New Gamertag

**Input at prompt:** `NightOwl42`

**Expected console output:** `'NightOwl42' saved successfully!`

**Verify:** Open `gamertags.txt` — it should now have 11 lines with `NightOwl42` at the bottom.

**After reload, print_all_gamertags() should show:**
```
--- ALL GAMERTAGS ---
  1. DragonSlayer99
  ...
  10. ZeroHour
  11. NightOwl42
```

---

## Test 6: Add Empty Gamertag

**Input at prompt:** (press Enter without typing anything)

**Expected console output:** `(no name entered — nothing saved)`

**Verify:** `gamertags.txt` is unchanged.

---

## Test 7: Add Gamertag With Spaces Around It

**Input at prompt:** `  SpacedName  ` (with leading/trailing spaces)

**Expected:** Saved as `SpacedName` (stripped), not `  SpacedName  `.

**Verify:** Open `gamertags.txt` — line should be `SpacedName` with no extra spaces.

---

## Test 8: Run Again — Yes

**Input at "Run again?" prompt:** `Y`

**Expected:** Program loops back to the beginning, reloads gamertags, shows welcome screen again.

---

## Test 9: Run Again — No

**Input at "Run again?" prompt:** `N`

**Expected:** Program prints "Thanks for using Gamertags App. Goodbye!" and exits.

---

## Test 10: Run Again — Lowercase

**Input at "Run again?" prompt:** `y` (lowercase)

**Expected:** Same as typing `Y` — program loops again.
(The `.upper()` call normalises case.)

---

## Test 11: Missing gamertags.txt

**Setup:** Delete or rename `gamertags.txt` before running.

**Expected console output:**
```
  ERROR: Could not find '..../gamertags.txt'.
  Please create a gamertags.txt file in the same folder as this script.
```

Program should continue running without crashing, with an empty list.

---

## Test 12: Empty gamertags.txt

**Setup:** gamertags.txt exists but is completely empty.

**Expected print_all_gamertags output:**
```
--- ALL GAMERTAGS ---
  (no gamertags loaded)
```

**Expected filter outputs:**
```
--- GAMERTAGS ENDING WITH A NUMBER ---
  (none found)

--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---
  (none found)
```

---

## Test 13: gamertags.txt With Blank Lines

**Setup:** gamertags.txt contains:
```
DragonSlayer99

StarPilot7
```

(There is a blank line between them.)

**Expected:** Only 2 gamertags loaded — blank line is skipped.
```
--- ALL GAMERTAGS ---
  1. DragonSlayer99
  2. StarPilot7
```

---

## Quick Verification Script

Run this to test all core logic without the full program:

```python
# quick_test.py — run independently to verify logic

def ends_with_number(tag):
    return len(tag) > 0 and tag[-1].isdigit()

def starts_with_symbol(tag):
    return len(tag) > 0 and not tag[0].isalnum()

test_tags = [
    "DragonSlayer99", "xXNightHawkXx", "_CoolGamer_",
    "StarPilot7", "!GhostHunter", "NeonWolf3",
    ".ShadowBlade", "CobraKing", "ProPlayer1", "ZeroHour"
]

print("=== Filter 1: Ending with number ===")
for tag in test_tags:
    if ends_with_number(tag):
        print(f"  {tag}")

print("\n=== Filter 2: Not starting with letter/digit ===")
for tag in test_tags:
    if starts_with_symbol(tag):
        print(f"  {tag}")
```

**Expected output:**
```
=== Filter 1: Ending with number ===
  DragonSlayer99
  StarPilot7
  NeonWolf3
  ProPlayer1

=== Filter 2: Not starting with letter/digit ===
  _CoolGamer_
  !GhostHunter
  .ShadowBlade
```
