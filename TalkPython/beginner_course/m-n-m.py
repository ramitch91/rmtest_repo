import random


def main():
    show_header()
    play_game()


def show_header():
    print()
    print("-----------------------------")
    print("      M&M Guessing Game!")
    print("-----------------------------")
    print()


def play_game():
    mm_count = random.randint(1, 100)
    # mm_count = 57
    attempt_limit = 5
    attempts = 0

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()

    while attempts < attempt_limit:
        guess = get_guess()
        attempts += 1

        winner = check_for_win(guess, mm_count)
        if winner:
            print(f"Bye, you're done in {attempts}!")
            break

    if not winner:
        print(f"Sorry you did not win a free lunch. The correct number was {mm_count}.")


def get_guess():
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    return guess


def check_for_win(guess, mm_count):
    winner = False
    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
        winner = True
    elif mm_count < guess:
        print("Sorry, that is too HIGH!")
    else:
        print("Sorry, that is too LOW!")
    return winner


if __name__ == "__main__":
    main()