# ANSWERS_10_python_while_loops.md

## Python While Loops — Complete Answer Guide

---

## Basic While Loop

```python
# C#: while (condition) { ... }
# Python:
run_again = True
while run_again:
    print("Loop is running")
    answer = input("Continue? (Y/N): ").strip().upper()
    run_again = (answer == "Y")
print("Loop ended")
```

---

## The Main Program Loop

```python
def main():
    gt = Gamertags()
    run_again = True              # Starts True — loop runs at least once

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
        run_again = (again == "Y")   # loop continues only if Y

    print("\nGoodbye!")
```

---

## while True with break

```python
# Alternative pattern (also valid)
while True:
    process()
    answer = input("Run again? ").strip().upper()
    if answer != "Y":
        break   # exit the loop
```

The boolean flag pattern (`run_again = (answer == "Y")`) is preferred
because it mirrors the C# version and is easier to read.

---

## Infinite loop risk

```python
# DANGER — this never stops:
run_again = True
while run_again:
    print("stuck!")
    # Missing: update run_again

# Always ensure the loop variable can become False
```

---

## While loop with count (not used in this project but good to know)

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
# Output: Count: 0, Count: 1, Count: 2, Count: 3, Count: 4
```

---

## C# vs Python while loop

```csharp
// C#
bool runAgain = true;
while (runAgain) {
    // work
    string answer = Console.ReadLine().Trim().ToUpper();
    runAgain = (answer == "Y");
}
```

```python
# Python — identical logic, different syntax
run_again = True
while run_again:
    # work
    answer = input().strip().upper()
    run_again = (answer == "Y")
```
