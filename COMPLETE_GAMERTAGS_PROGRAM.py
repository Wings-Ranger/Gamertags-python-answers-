"""
COMPLETE_GAMERTAGS_PROGRAM.py
=============================
Full, working Python implementation of the Gamertags console app.
Matches C# behavior exactly, with detailed comments explaining each section.
Ready to run and study.

Original C# project by Wings-Ranger — Python answer key reference.

HOW TO RUN:
  1. Place this file in the same folder as gamertags.txt
     (or update FILE_PATH below to an absolute path)
  2. Run:  python COMPLETE_GAMERTAGS_PROGRAM.py

SAMPLE gamertags.txt contents (create this file first):
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
"""

import os   # Used for os.path to build a safe file path


# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------
# Build the file path relative to THIS script's location so it works
# no matter which directory you run the script from.
# This mirrors the C# approach of placing the file alongside the executable.
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gamertags.txt")


# ---------------------------------------------------------------------------
# CLASS: Gamertags
# ---------------------------------------------------------------------------
# In C#:  class Gamertags { ... }
# In Python: class Gamertags: ...
#
# The class owns:
#   - self.gamertags  — the list of names loaded from the file (like a C# array)
#   - All methods that act on that list
class Gamertags:
    """Manages a list of gamertags loaded from and saved to a text file."""

    # -----------------------------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------------------------
    # In C#:  public Gamertags() { ... }
    # In Python: def __init__(self): ...
    #
    # Called automatically when you write:  gt = Gamertags()
    def __init__(self):
        # self.gamertags stores the list (equivalent to C# string[] / List<string>)
        self.gamertags = []

    # -----------------------------------------------------------------------
    # METHOD 1: load_gamertags
    # -----------------------------------------------------------------------
    # C# equivalent:
    #   public void LoadGamertags() {
    #       gamertags = File.ReadAllLines("gamertags.txt");
    #   }
    #
    # Python reads files differently:
    #   - open() returns a file object
    #   - .readlines() gives a list of strings, each with a '\n' at the end
    #   - .strip() removes that '\n' and any surrounding whitespace
    #   - We skip blank lines so empty lines in the file don't create empty entries
    def load_gamertags(self):
        """Load gamertags from FILE_PATH into self.gamertags.
        Shows an error message if the file cannot be found."""
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                # Read every line, strip whitespace, and keep only non-empty lines
                self.gamertags = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"  ERROR: Could not find '{FILE_PATH}'.")
            print("  Please create a gamertags.txt file in the same folder as this script.")
            self.gamertags = []   # Ensure the list is empty so the rest of the program still runs

    # -----------------------------------------------------------------------
    # METHOD 2: show_welcome_message
    # -----------------------------------------------------------------------
    # C# equivalent:
    #   Console.Clear();
    #   Console.WriteLine("=== Gamertags App ===");
    #
    # os.system("cls") clears the screen on Windows; "clear" on Mac/Linux.
    # The try/except handles environments where clearing is not possible.
    def show_welcome_message(self):
        """Clear the screen and print a welcome banner."""
        try:
            os.system("cls" if os.name == "nt" else "clear")
        except Exception:
            pass   # If clearing fails, just continue — not critical

        print("=" * 40)
        print("       GAMERTAGS APP (Python)")
        print("=" * 40)
        print()   # Blank line for readability

    # -----------------------------------------------------------------------
    # METHOD 3: print_all_gamertags
    # -----------------------------------------------------------------------
    # C# equivalent:
    #   for (int i = 0; i < gamertags.Length; i++) {
    #       Console.WriteLine($"{i + 1}. {gamertags[i]}");
    #   }
    #
    # Python uses enumerate() to get both the index and value in a loop.
    # start=1 makes the numbering begin at 1 (not 0).
    def print_all_gamertags(self):
        """Display all gamertags, numbered from 1."""
        print("\n--- ALL GAMERTAGS ---")
        if not self.gamertags:
            print("  (no gamertags loaded)")
            return

        for i, tag in enumerate(self.gamertags, start=1):
            print(f"  {i}. {tag}")
        print()

    # -----------------------------------------------------------------------
    # METHOD 4: print_gamertags_ending_with_number
    # -----------------------------------------------------------------------
    # C# equivalent:
    #   foreach (string tag in gamertags) {
    #       if (tag.Length > 0 && char.IsDigit(tag[tag.Length - 1])) {
    #           Console.WriteLine(tag);
    #       }
    #   }
    #
    # Python:
    #   tag[-1]        → last character (Python supports negative indexing)
    #   .isdigit()     → True if the character is 0–9
    #   len(tag) > 0   → guard against empty strings
    def print_gamertags_ending_with_number(self):
        """Print only gamertags whose last character is a digit (0–9)."""
        print("\n--- GAMERTAGS ENDING WITH A NUMBER ---")
        found = False

        for tag in self.gamertags:
            # Guard: skip empty strings (should not happen after load, but safe)
            if len(tag) > 0 and tag[-1].isdigit():
                print(f"  {tag}")
                found = True

        if not found:
            print("  (none found)")
        print()

    # -----------------------------------------------------------------------
    # METHOD 5: print_gamertags_not_starting_with_letter_or_digit
    # -----------------------------------------------------------------------
    # C# equivalent:
    #   foreach (string tag in gamertags) {
    #       if (tag.Length > 0 && !char.IsLetterOrDigit(tag[0])) {
    #           Console.WriteLine(tag);
    #       }
    #   }
    #
    # Python:
    #   tag[0]         → first character
    #   .isalnum()     → True if the character is a letter (a–z, A–Z) or digit (0–9)
    #   not .isalnum() → True if it is NOT a letter or digit (symbols, spaces, etc.)
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

    # -----------------------------------------------------------------------
    # METHOD 6: add_new_username
    # -----------------------------------------------------------------------
    # C# equivalent:
    #   Console.Write("Enter new gamertag: ");
    #   string newTag = Console.ReadLine();
    #   using (StreamWriter sw = File.AppendText("gamertags.txt")) {
    #       sw.WriteLine(newTag);
    #   }
    #   gamertags = File.ReadAllLines("gamertags.txt");
    #
    # Python:
    #   input()          → equivalent to Console.ReadLine()
    #   .strip()         → removes accidental leading/trailing whitespace
    #   open(..., "a")   → opens the file in APPEND mode (adds to end, never overwrites)
    #   '\n' at the end  → ensures the new name is on its own line
    def add_new_username(self):
        """Prompt the user for a new gamertag, save it to the file, and reload."""
        print("\n--- ADD NEW GAMERTAG ---")
        new_tag = input("  Enter new gamertag: ").strip()

        if not new_tag:
            print("  (no name entered — nothing saved)")
            return

        try:
            with open(FILE_PATH, "a", encoding="utf-8") as f:
                f.write(new_tag + "\n")   # Append name on a new line
            print(f"  '{new_tag}' saved successfully!")
            self.load_gamertags()         # Reload so the new tag appears immediately
        except IOError as e:
            print(f"  ERROR: Could not write to file. {e}")


# ---------------------------------------------------------------------------
# MAIN FUNCTION  (equivalent to C# static void Main)
# ---------------------------------------------------------------------------
# In C#:
#   static void Main(string[] args) {
#       bool runAgain = true;
#       while (runAgain) {
#           ...
#           Console.Write("Run again? (Y/N): ");
#           string answer = Console.ReadLine().Trim().ToUpper();
#           runAgain = (answer == "Y");
#       }
#   }
#
# Python uses a boolean flag (run_again) and a while loop in the same way.
# The flag starts as True so the loop executes at least once.
def main():
    """Main program loop — runs the full app and asks to repeat."""
    gt = Gamertags()          # Create one instance of the Gamertags class
    run_again = True           # Boolean flag — mirrors C# bool runAgain = true

    while run_again:           # Keep looping until the user says no
        gt.load_gamertags()            # Step 1: Load data from file
        gt.show_welcome_message()      # Step 2: Show welcome screen
        gt.print_all_gamertags()       # Step 3: Show all gamertags

        # Step 4: Show filter results
        gt.print_gamertags_ending_with_number()
        gt.print_gamertags_not_starting_with_letter_or_digit()

        # Step 5: Offer to add a new gamertag
        add_choice = input("Would you like to add a new gamertag? (Y/N): ").strip().upper()
        if add_choice == "Y":
            gt.add_new_username()

        # Step 6: Ask whether to run again
        # .strip()  — removes accidental spaces around the answer
        # .upper()  — makes Y and y both work (case-insensitive)
        again = input("\nRun again? (Y/N): ").strip().upper()
        run_again = (again == "Y")   # True only if the user typed Y

    print("\nThanks for using Gamertags App. Goodbye!")


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------
# This block runs only when you execute THIS file directly.
# It does NOT run if another file imports this module.
# Equivalent to C#'s program entry: static void Main(string[] args)
if __name__ == "__main__":
    main()
