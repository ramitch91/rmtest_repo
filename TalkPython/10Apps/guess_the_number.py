# Filename: guess_the_number

# imports
import random


def main():
    show_header()
    number = random.randint(1, 101)
    guess = 0
    while guess != number:
        guess = get_guess()
        if guess == 0:
            continue
        test_guess(number, guess)


def show_header():
    print()
    print("---------------------------")
    print("   Guess the Number App")
    print("---------------------------")
    print()


def get_guess():
    guess_text = input("Guess a Number between 1 and 100: ")

    try:
        guess = int(guess_text)
    except ValueError as ex:
        print("You did not enter an integer")
        guess = 0
        return guess

    return guess


def test_guess(number, guess):
    if number == guess:
        print(f"Yes! You got it. The number was {number}")
        return
    elif guess < number:
        test_answer = "LOWER"
    else:
        test_answer = "HIGHER"

    print(f"Sorry, the number is {test_answer} than the number")
    return


if __name__ == "__main__":
    main()