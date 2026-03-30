# ANSWERS_01_python_intro.md

## Python Introduction — Complete Answer Guide

Covers: What Python is, how scripts run, and how it compares to C#.

---

## What is Python?

Python is a high-level, interpreted programming language.

| Feature | C# | Python |
|---|---|---|
| Execution | Compiled to IL, then JIT-compiled | Interpreted line by line |
| Type system | Statically typed (declare types) | Dynamically typed (inferred) |
| Syntax | Curly braces `{}` | Indentation (spaces/tabs) |
| Entry point | `static void Main()` | `if __name__ == "__main__": main()` |
| End of statement | `;` | Newline |

---

## How a Python script runs

```python
# hello_gamertags.py

# 1. Python reads this file top to bottom
# 2. It executes each line as it encounters it
# 3. Function/class definitions are stored but not run yet
# 4. The if __name__ == "__main__" block runs last

def greet():
    print("Welcome to Gamertags!")

if __name__ == "__main__":
    greet()    # This runs when you execute: python hello_gamertags.py
```

**Output:**
```
Welcome to Gamertags!
```

---

## Running a Python script

```bash
# In a terminal/command prompt:
python gamertags_program.py

# Or on some systems:
python3 gamertags_program.py
```

---

## Gamertags example: Hello World

```python
# The simplest Python program
print("Welcome to the Gamertags App!")

# With a variable
app_name = "Gamertags App"
version = 1
print(f"Welcome to {app_name} version {version}!")
```

**Output:**
```
Welcome to the Gamertags App!
Welcome to Gamertags App version 1!
```

---

## Python vs C# program structure

### C# (requires class + method + namespace)
```csharp
using System;

namespace GamertagsApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, Gamertags!");
        }
    }
}
```

### Python (much simpler)
```python
print("Hello, Gamertags!")
```

Python does not require a class to run code. A script can be as simple as one line.

---

## Key Python conventions

1. **Indentation is mandatory** — use 4 spaces (not tabs) consistently.
2. **No semicolons** — each statement ends with a newline.
3. **No type declarations** — Python infers types automatically.
4. **snake_case naming** — `load_gamertags` not `LoadGamertags`.
5. **Comments** use `#` (like `//` in C#).
