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

    matches = search_folders(folder, text)
    for m in matches:
        print(m)

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
    return text.lower()


def search_folders(folder, text):
    all_matches = []
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            continue
        matches = search_file(full_item, text)
        all_matches.extend(matches)
    return all_matches


def search_file(filename, search_text):
    matches = []
    with open(filename, "r", encoding='UTF-8') as fin:
        for line in fin:
            if line.lower().find(search_text) >= 0:
                matches.append(line)
    return matches


if __name__ == '__main__':
    main()
