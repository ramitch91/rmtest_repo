"""
This module performs the file handling capabilities for the journaling program.
"""

# imports
from genericpath import exists
import os
from typing import List


def get_filename() -> str:
    """This module request for the user to enter the filename of the journal file
    that they want to use and then just returns the filename.

    Returns:
        filename (str): filename of the journal file
    """
    filename = input("Enter the journal filename: ")
    return filename


def get_full_filename(name: str):
    working_path = os.getcwd()
    filename = os.path.abspath(
        os.path.join(working_path, "TalkPython", "10Apps", "journal", name + ".jrl")
    )
    return filename


def load_file(name: str) -> list:
    """
    This module creates or loads a 'jrl' file named by the filename that is sent to the module by the calling program.

    Args:
        name (str): name of the journal file
    """
    data = []
    filename = get_full_filename(name)

    if exists(filename):
        print(f"...loading data from {filename}")
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
        print(f"...loaded {len(data)} entries")
        print()

    return data


def save_file(name: str, data: list):
    """
    This module saves the journal entries into the '.jrl' file named by the filename sent to this module by the calling program.  The entries will be in cronological order, with the oldest entry being first and the newest entry being last.

    Args:
        name (str): name of the journal file
        data (list): a list of journal entries
    """
    filename = get_full_filename(name)
    print(f"...saving to {filename}")
    with open(filename, "w") as fout:
        for entry in data:
            fout.write(entry + "\n")


def add_entry(data: list) -> list:
    """
    This module will request for a new journal entry from the user and append the entry to the list

    Args:
        data (list): the existing list of the journal entries

    Returns:
        data (list): a new list of the journal entries
    """
    new_entry = input("New entry: ")
    data.append(new_entry)
    return data


def delete_entry(data: list) -> list:

    data.reverse()
    del_entry = int(input("Which entry would you like to delete? (Enter #): "))
    del data[del_entry - 1]
    data.reverse()

    return data
