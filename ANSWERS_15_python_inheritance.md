# ANSWERS_15_python_inheritance.md

## Python Inheritance — Complete Answer Guide

---

## Basic Inheritance

```python
# Base class (parent)
class Player:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")


# Derived class (child) — inherits from Player
class GamertagPlayer(Player):
    def __init__(self, name, gamertag):
        super().__init__(name)       # Call parent constructor (C#: base(name))
        self.gamertag = gamertag

    def show_tag(self):
        print(f"  Gamertag: {self.gamertag}")


# Usage
p = GamertagPlayer("Alex", "DragonSlayer99")
p.greet()       # Inherited from Player: "Hello, I'm Alex"
p.show_tag()    # From GamertagPlayer: "  Gamertag: DragonSlayer99"
```

---

## `super()` — calling the parent class

```python
class GamertagPlayer(Player):
    def __init__(self, name, gamertag):
        super().__init__(name)   # C#: base(name)
        self.gamertag = gamertag

    def greet(self):             # Override parent method
        super().greet()          # Call parent version first
        print(f"  My tag: {self.gamertag}")
```

---

## Not used in this project

The Gamertags project uses a **single class** (`Gamertags`) with no inheritance.
Inheritance would be useful if you wanted:
- `GamertagsFile(Gamertags)` — a specialised version that handles different file formats
- `FilteredGamertags(Gamertags)` — a version with extra filtering capabilities

For the purpose of this project, inheritance is not needed.

---

## C# vs Python inheritance syntax

```csharp
// C#
class GamertagPlayer : Player
{
    public GamertagPlayer(string name, string gamertag) : base(name)
    {
        this.gamertag = gamertag;
    }
}
```

```python
# Python
class GamertagPlayer(Player):         # Inherits from Player
    def __init__(self, name, gamertag):
        super().__init__(name)         # Call parent __init__
        self.gamertag = gamertag
```

---

## isinstance() with inheritance

```python
p = GamertagPlayer("Alex", "DragonSlayer99")

isinstance(p, GamertagPlayer)   # True — direct type
isinstance(p, Player)            # True — also an instance of parent class
isinstance(p, str)               # False
```
