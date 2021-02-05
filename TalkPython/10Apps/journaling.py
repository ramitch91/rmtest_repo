""" 
This is a simple journaling program. It will store new entries in chronological orderbut the program will show the list in reverse order (showing the newest entry at the top)
"""

# imports
import journal
import sys


def main():
    print_header()
    filename = journal.get_filename()
    data = journal.load_file(filename)
    cmd = "Empty"

    while cmd != "x" or cmd:
        cmd = input(
            "What do you want to do? [a] Add, [d] Delete, [l] List, [x] Exit: "
        ).lower()
        if cmd == "x" or not cmd:
            journal.save_file(filename, data)
            sys.exit()
        elif cmd == "l":
            if not len(data):
                print("No entries to list")
                print()
                continue
            print(f"Your {len(data)} entries")
            print()
            for num, entry in enumerate(reversed(data)):
                print(f"{num + 1}. {entry}")
        elif cmd == "a":
            journal.add_entry(data)
        elif cmd == "d":
            journal.delete_entry(data)
        else:
            print("Not a valid command.")


def print_header():
    print()
    print("--------------------------")
    print("      Journal App")
    print("--------------------------")
    print()


if __name__ == "__main__":
    main()
