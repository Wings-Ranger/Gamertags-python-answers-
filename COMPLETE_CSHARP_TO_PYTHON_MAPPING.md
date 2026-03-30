# COMPLETE_CSHARP_TO_PYTHON_MAPPING.md

Complete side-by-side translation of the C# gamertag project into Python.
Every construct is explained so you understand **why** Python looks different,
not just **what** the Python equivalent is.

---

## Program.cs → Python main() function

### C# `Program.cs`

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        bool runAgain = true;
        Gamertags gt = new Gamertags();

        while (runAgain)
        {
            gt.LoadGamertags();
            gt.ShowWelcomeMessage();
            gt.PrintAllGamertags();
            gt.PrintGamertagsEndingWithNumber();
            gt.PrintGamertagsNotStartingWithLetterOrDigit();

            Console.Write("Add new gamertag? (Y/N): ");
            string addChoice = Console.ReadLine().Trim().ToUpper();
            if (addChoice == "Y")
                gt.AddNewUsername();

            Console.Write("Run again? (Y/N): ");
            string answer = Console.ReadLine().Trim().ToUpper();
            runAgain = (answer == "Y");
        }
    }
}
```

### Python equivalent

```python
def main():
    run_again = True          # bool runAgain = true;
    gt = Gamertags()          # Gamertags gt = new Gamertags();

    while run_again:          # while (runAgain) { ... }
        gt.load_gamertags()
        gt.show_welcome_message()
        gt.print_all_gamertags()
        gt.print_gamertags_ending_with_number()
        gt.print_gamertags_not_starting_with_letter_or_digit()

        add_choice = input("Add new gamertag? (Y/N): ").strip().upper()
        if add_choice == "Y":
            gt.add_new_username()

        again = input("Run again? (Y/N): ").strip().upper()
        run_again = (again == "Y")

if __name__ == "__main__":
    main()
```

### Line-by-line differences explained

| C# | Python | Why it's different |
|---|---|---|
| `using System;` | *(not needed for basic I/O)* | Python built-ins don't require imports |
| `class Program { static void Main(...) }` | `def main():` + `if __name__ == "__main__":` | Python uses a convention, not enforced entry point |
| `bool runAgain = true;` | `run_again = True` | Python uses `True` (capital T); no type declaration |
| `new Gamertags()` | `Gamertags()` | No `new` keyword in Python |
| `Console.ReadLine().Trim().ToUpper()` | `input(...).strip().upper()` | Method names differ but purpose is identical |
| `runAgain = (answer == "Y");` | `run_again = (again == "Y")` | Same logic; Python naming convention uses underscores |

---

## Gamertags.cs → Python Gamertags class

### C# `Gamertags.cs`

```csharp
using System;
using System.IO;

class Gamertags
{
    private string[] gamertags;

    public void LoadGamertags()
    {
        gamertags = File.ReadAllLines("gamertags.txt");
    }

    public void ShowWelcomeMessage()
    {
        Console.Clear();
        Console.WriteLine("=== Gamertags App ===");
    }

    public void PrintAllGamertags()
    {
        Console.WriteLine("\n--- ALL GAMERTAGS ---");
        for (int i = 0; i < gamertags.Length; i++)
        {
            Console.WriteLine($"{i + 1}. {gamertags[i]}");
        }
    }

    public void PrintGamertagsEndingWithNumber()
    {
        Console.WriteLine("\n--- ENDING WITH NUMBER ---");
        foreach (string tag in gamertags)
        {
            if (tag.Length > 0 && char.IsDigit(tag[tag.Length - 1]))
                Console.WriteLine(tag);
        }
    }

    public void PrintGamertagsNotStartingWithLetterOrDigit()
    {
        Console.WriteLine("\n--- NOT STARTING WITH LETTER OR DIGIT ---");
        foreach (string tag in gamertags)
        {
            if (tag.Length > 0 && !char.IsLetterOrDigit(tag[0]))
                Console.WriteLine(tag);
        }
    }

    public void AddNewUsername()
    {
        Console.Write("Enter new gamertag: ");
        string newTag = Console.ReadLine().Trim();
        using (StreamWriter sw = File.AppendText("gamertags.txt"))
        {
            sw.WriteLine(newTag);
        }
        gamertags = File.ReadAllLines("gamertags.txt");
    }
}
```

### Python equivalent

```python
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")

class Gamertags:

    def __init__(self):
        self.gamertags = []               # private string[] gamertags;

    def load_gamertags(self):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"  ERROR: Could not find '{FILE_PATH}'.")
            self.gamertags = []

    def show_welcome_message(self):
        try:
            os.system("cls" if os.name == "nt" else "clear")
        except Exception:
            pass
        print("=" * 40)
        print("       GAMERTAGS APP (Python)")
        print("=" * 40)

    def print_all_gamertags(self):
        print("\n--- ALL GAMERTAGS ---")
        if not self.gamertags:
            print("  (no gamertags loaded)")
            return
        for i, tag in enumerate(self.gamertags, start=1):
            print(f"  {i}. {tag}")

    def print_gamertags_ending_with_number(self):
        print("\n--- GAMERTAGS ENDING WITH A NUMBER ---")
        found = False
        for tag in self.gamertags:
            if len(tag) > 0 and tag[-1].isdigit():
                print(f"  {tag}")
                found = True
        if not found:
            print("  (none found)")

    def print_gamertags_not_starting_with_letter_or_digit(self):
        print("\n--- GAMERTAGS NOT STARTING WITH A LETTER OR DIGIT ---")
        found = False
        for tag in self.gamertags:
            if len(tag) > 0 and not tag[0].isalnum():
                print(f"  {tag}")
                found = True
        if not found:
            print("  (none found)")

    def add_new_username(self):
        new_tag = input("  Enter new gamertag: ").strip()
        if not new_tag:
            print("  (nothing saved)")
            return
        try:
            with open(FILE_PATH, "a", encoding="utf-8") as f:
                f.write(new_tag + "\n")
            print(f"  '{new_tag}' saved!")
            self.load_gamertags()
        except IOError as e:
            print(f"  ERROR: {e}")
```

### Concept-by-concept comparison

#### 1. Class declaration

```csharp
class Gamertags { }                     // C#
```
```python
class Gamertags:                        # Python — no braces, uses indentation
    pass
```

#### 2. Instance field / attribute

```csharp
private string[] gamertags;            // C# — declared in class body
```
```python
def __init__(self):
    self.gamertags = []                 # Python — set inside __init__
```

Key difference: Python attributes are created in `__init__`, not declared at class level.
`self` is always the first parameter and refers to the current object (like C# `this`).

#### 3. Array vs List

```csharp
string[] gamertags = File.ReadAllLines("gamertags.txt");
// Fixed-size array of strings
```
```python
self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
# Dynamic list — can grow/shrink
```

#### 4. File reading

```csharp
gamertags = File.ReadAllLines("gamertags.txt");
// Reads all lines; each line already stripped of newline
```
```python
with open(FILE_PATH, "r", encoding="utf-8") as f:
    self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
# .strip() removes '\n' from each line
# 'with' block automatically closes the file
```

#### 5. For loop with index

```csharp
for (int i = 0; i < gamertags.Length; i++) {
    Console.WriteLine($"{i + 1}. {gamertags[i]}");
}
```
```python
for i, tag in enumerate(self.gamertags, start=1):
    print(f"  {i}. {tag}")
# enumerate() gives (index, value) pairs; start=1 begins count at 1
```

#### 6. Foreach loop

```csharp
foreach (string tag in gamertags) {
    Console.WriteLine(tag);
}
```
```python
for tag in self.gamertags:
    print(tag)
# Python for loop IS a foreach loop — no classic for(;;) needed for iteration
```

#### 7. Last character check

```csharp
tag[tag.Length - 1]        // C# — explicit length calculation
char.IsDigit(...)          // C# — static method on char
```
```python
tag[-1]                    # Python — negative index means "from the end"
tag[-1].isdigit()          # Python — string method called on the character
```

#### 8. First character check

```csharp
!char.IsLetterOrDigit(tag[0])
```
```python
not tag[0].isalnum()
# isalnum() = is alphabetic OR numeric (equivalent to C# IsLetterOrDigit)
```

#### 9. File append

```csharp
using (StreamWriter sw = File.AppendText("gamertags.txt")) {
    sw.WriteLine(newTag);
}
```
```python
with open(FILE_PATH, "a", encoding="utf-8") as f:
    f.write(new_tag + "\n")
# "a" = append mode — never overwrites existing content
# Must add "\n" manually (unlike C# WriteLine which adds it automatically)
```

#### 10. Error handling

```csharp
// C# — often uses if (File.Exists(...)) before reading
if (!File.Exists("gamertags.txt")) {
    Console.WriteLine("File not found");
    return;
}
gamertags = File.ReadAllLines("gamertags.txt");
```
```python
# Python — uses try/except which is cleaner and handles more cases
try:
    with open(FILE_PATH, "r") as f:
        self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("File not found")
    self.gamertags = []
```

#### 11. Screen clear

```csharp
Console.Clear();
```
```python
os.system("cls" if os.name == "nt" else "clear")
# os.name == "nt" means Windows; otherwise Mac/Linux use "clear"
```

#### 12. String interpolation

```csharp
Console.WriteLine($"{i + 1}. {gamertags[i]}");   // C# — $ prefix
```
```python
print(f"  {i}. {tag}")                             # Python — f prefix, same idea
```

---

## Summary table: C# → Python at a glance

| C# concept | Python equivalent |
|---|---|
| `class Foo { }` | `class Foo:` |
| `void Method()` | `def method(self):` |
| `string[]` | `list` |
| `new Foo()` | `Foo()` |
| `this.field` | `self.field` |
| `Console.WriteLine(x)` | `print(x)` |
| `Console.ReadLine()` | `input()` |
| `.Trim()` | `.strip()` |
| `.ToUpper()` | `.upper()` |
| `char.IsDigit(c)` | `c.isdigit()` |
| `char.IsLetterOrDigit(c)` | `c.isalnum()` |
| `File.ReadAllLines(path)` | `open(path).readlines()` with `.strip()` |
| `File.AppendText(path)` | `open(path, "a")` |
| `for (int i=0; i<n; i++)` | `for i in range(n):` |
| `foreach (var x in list)` | `for x in list:` |
| `tag[tag.Length - 1]` | `tag[-1]` |
| `bool flag = true;` | `flag = True` |
| `try { } catch (Exception e) { }` | `try: ... except Exception as e:` |
| `Console.Clear()` | `os.system("cls"/"clear")` |
| `using (var f = ...) { }` | `with open(...) as f:` |
