import movie_svc


def main():
    print_header()
    search_loop()


def print_header():
    print()
    print('------------------------')
    print('   MOVIE SEARCH APP')
    print('------------------------')
    print()


def search_loop():
    search = "to force loop at least once"

    while search.lower() != 'x':
        search = input("What movie do you want to search for (x to Exit)? ")
        if search.lower() != 'x':
            results = movie_svc.find_movies(search)
            print(f"Found {len(results)} movies for search {search}")

            for r in results:
                print(f"{r.year} -- {r.title}")

            print()
    print('Exiting...')


if __name__ == '__main__':
    main()
