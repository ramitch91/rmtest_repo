import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder or not folder.split():
        print("We can't search that location")
        return None

    text = get_text_from_user(folder)
    if not text or not text.split():
        print("We can't search for nothing")
        return None

    search_folders(folder, text)


def print_header():
    print("--------------------------")
    print("    FILE SEARCH APP")
    print("--------------------------")
    print()


def get_folder_from_user():
    folder = input("Enter a folder to search: ")
    if not folder or not folder.split():
        return None
    if not os.path.isdir(folder):
        return None
    return os.path.abspath(folder)


def get_text_from_user(folder):
    text = input("What do you want to search for [single phrases only]? ")
    return text


def search_folders(folder, text):
    print(f"Would search for {text} in {folder}")


if __name__ == '__main__':
    main()
