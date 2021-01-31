import os
import shutil


def main():
    print_header()
    folder = get_or_create_output_folder()
    print(folder)
    # download cats
    # display cats


def print_header():
    print()
    print("------------------------------")
    print("       Lol Cat Factory")
    print("------------------------------")
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f"Creating new directory at {full_path}")
        os.mkdir(full_path)

    return full_path


if __name__ == "__main__":
    main()